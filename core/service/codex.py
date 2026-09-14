from __future__ import annotations

import asyncio
import json
import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from core.settings import Settings, logger


MAX_PROMPT_LENGTH = 12_000
MAX_OUTPUT_LENGTH = 200_000
MAX_MODEL_CATALOG_LENGTH = 2_000_000
CODEX_STREAM_LIMIT = 8 * 1024 * 1024
MAX_RPC_FRAME = 128 * 1024 * 1024
MODEL_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}$")
REASONING_DESCRIPTIONS = {
    "low": "быстрый ответ с облегчённым рассуждением",
    "medium": "баланс скорости и глубины",
    "high": "повышенная глубина рассуждения",
    "xhigh": "максимальная глубина рассуждения",
    "max": "предельная глубина рассуждения",
    "ultra": "ультра-режим с дополнительной агентной работой",
}
APPROVAL_POLICY = "on-request"
APPROVALS_REVIEWER = "auto_review"
SPEED_ALIASES = {
    "default": "default",
    "normal": "default",
    "обычно": "default",
    "обычная": "default",
    "приоритет": "priority",
    "priority": "priority",
    "fast": "priority",
    "быстро": "priority",
    "быстрый": "priority",
    "1.5x": "priority",
}
SPEED_LABELS = {"default": "normal", "priority": "fast"}
CODEX_PROMPT_PATH = Path("core/prompts/codex.md")


class CodexError(RuntimeError):
    pass


class CodexBusy(CodexError):
    pass


@dataclass(slots=True)
class _State:
    binary: str = "codex"
    codex_home: Path = field(default_factory=Path)
    model: str = "gpt-5.6-luna"
    reasoning_effort: str = "xhigh"
    service_tier: str = "default"
    timeout: int = 0
    mcp_url: str = "http://127.0.0.1:8000/mcp"
    mcp_transport: str = "streamable-http"
    workdir: Path = field(default_factory=Path.cwd)
    thread_state_path: Path = field(default_factory=Path)
    models: list[dict[str, Any]] = field(default_factory=list)
    process: asyncio.subprocess.Process | None = None
    reader_task: asyncio.Task[None] | None = None
    stderr_task: asyncio.Task[None] | None = None
    write_lock: asyncio.Lock = field(default_factory=asyncio.Lock)
    start_lock: asyncio.Lock = field(default_factory=asyncio.Lock)
    pending: dict[int, asyncio.Future[dict[str, Any]]] = field(default_factory=dict)
    events: asyncio.Queue[dict[str, Any]] = field(default_factory=asyncio.Queue)
    next_request_id: int = 1
    thread_id: str | None = None
    initialized: bool = False


_state = _State()
_ask_lock = asyncio.Lock()


def configure(settings: Settings) -> None:
    _state.binary = settings.codex.binary
    _state.codex_home = settings.codex.home.expanduser().resolve()
    _state.model = settings.codex.model
    _state.reasoning_effort = settings.codex.reasoning_effort
    _state.service_tier = settings.codex.service_tier
    _state.timeout = max(0, settings.codex.timeout)
    _state.mcp_url = settings.codex.mcp_url
    _state.mcp_transport = settings.mcp.transport
    _state.workdir = settings.paths.project_root
    _state.thread_state_path = _state.workdir / "core" / "data" / "codex_thread.json"
    _state.models.clear()
    _state.thread_id = None


def current_model() -> str:
    return _state.model


def current_reasoning() -> str:
    return _state.reasoning_effort


def current_speed() -> str:
    return SPEED_LABELS[_state.service_tier]


def _developer_instructions() -> str:
    prompt_path = _state.workdir / CODEX_PROMPT_PATH
    try:
        instructions = prompt_path.read_text(encoding="utf-8").strip()
    except OSError as exc:
        raise CodexError("Не удалось прочитать файл инструкций Codex: codex.md") from exc
    if not instructions:
        raise CodexError("Файл инструкций Codex пуст: codex.md")
    return instructions


def set_speed(speed: str) -> str:
    normalized = SPEED_ALIASES.get(speed.strip().lower())
    if normalized is None:
        raise ValueError("Режимы скорости: normal или fast.")
    _state.service_tier = normalized
    return current_speed()


def set_model(model: str) -> str:
    model = model.strip()
    if not MODEL_NAME.fullmatch(model):
        raise ValueError("Имя модели содержит недопустимые символы.")
    _state.model = model
    return model


async def list_models() -> list[dict[str, Any]]:
    if _state.models:
        return _state.models
    await start()
    result = await _rpc(
        "model/list",
        {"includeHidden": True, "limit": 100},
        timeout=30,
    )
    models = result.get("data")
    if not isinstance(models, list):
        raise CodexError("Codex вернул каталог без списка моделей.")
    normalized = []
    for item in models:
        if not isinstance(item, dict):
            continue
        slug = item.get("id") or item.get("model")
        if not isinstance(slug, str) or not slug:
            continue
        normalized.append(
            {
                "slug": slug,
                "display_name": item.get("displayName") or slug,
                "supported_reasoning_levels": [
                    {
                        "effort": option.get("reasoningEffort"),
                        "description": option.get("description"),
                    }
                    for option in item.get("supportedReasoningEfforts", [])
                    if isinstance(option, dict) and option.get("reasoningEffort")
                ],
            }
        )
    if len(json.dumps(normalized, ensure_ascii=False)) > MAX_MODEL_CATALOG_LENGTH:
        raise CodexError("Каталог моделей Codex слишком большой.")
    _state.models = normalized
    return _state.models


def reasoning_info(models: list[dict[str, Any]]) -> dict[str, Any]:
    selected = next(
        (item for item in models if item.get("slug") == _state.model),
        None,
    )
    levels = []
    if selected:
        levels = [
            item.get("effort")
            for item in selected.get("supported_reasoning_levels", [])
            if isinstance(item, dict) and item.get("effort")
        ]
    return {
        "model": _state.model,
        "effort": _state.reasoning_effort,
        "description": REASONING_DESCRIPTIONS.get(
            _state.reasoning_effort, "уровень, переданный в конфигурацию Codex"
        ),
        "supported": levels,
        "catalog_match": selected is not None,
    }


def _load_thread_id() -> str | None:
    try:
        payload = json.loads(_state.thread_state_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except (OSError, json.JSONDecodeError) as exc:
        logger.warning("Codex thread state cannot be read: %s", exc)
        return None
    thread_id = payload.get("thread_id") if isinstance(payload, dict) else None
    return thread_id if isinstance(thread_id, str) and thread_id else None


def _save_thread_id(thread_id: str) -> None:
    _state.thread_state_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = _state.thread_state_path.with_suffix(".tmp")
    temporary_path.write_text(
        json.dumps({"thread_id": thread_id}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary_path.replace(_state.thread_state_path)


def _server_args() -> list[str]:
    return [
        _state.binary,
        "app-server",
        "--listen",
        "stdio://",
        "-c",
        f"mcp_servers.pyrogram_mcp.url={json.dumps(_state.mcp_url)}",
    ]


def _codex_env() -> dict[str, str]:
    home = _state.codex_home
    home.mkdir(parents=True, exist_ok=True, mode=0o700)

    # Keep native Codex state separate from VS Code while reusing the existing
    # login. The credential remains in ~/.codex/auth.json and is not copied.
    auth_path = home / "auth.json"
    shared_auth = Path.home() / ".codex" / "auth.json"
    default_home = (Path.home() / ".codex").resolve()
    if (
        home != default_home
        and not auth_path.exists()
        and not auth_path.is_symlink()
        and shared_auth.is_file()
    ):
        try:
            auth_path.symlink_to(shared_auth)
        except FileExistsError:
            pass

    environment = os.environ.copy()
    environment["CODEX_HOME"] = str(home)
    return environment


def _is_ready() -> bool:
    process = _state.process
    return bool(
        process
        and process.returncode is None
        and _state.initialized
        and _state.thread_id
    )


async def _fail_pending(error: CodexError) -> None:
    for future in tuple(_state.pending.values()):
        if not future.done():
            future.set_exception(error)
    _state.pending.clear()


async def _stream_lines(stream: asyncio.StreamReader):
    """Read JSONL independently of StreamReader's readline limit."""
    pending = bytearray()
    while chunk := await stream.read(64 * 1024):
        parts = chunk.split(b"\n")
        for index, part in enumerate(parts):
            if len(pending) + len(part) > MAX_RPC_FRAME:
                raise CodexError("Ответ Codex превышает лимит 128 MiB; сессия сохранена.")
            pending.extend(part)
            if index < len(parts) - 1:
                yield bytes(pending)
                pending.clear()
    if pending:
        yield bytes(pending)


async def _reader_loop(process: asyncio.subprocess.Process) -> None:
    assert process.stdout is not None
    error = CodexError("Соединение с Codex app-server закрыто.")
    try:
        async for line in _stream_lines(process.stdout):
            try:
                payload = json.loads(line)
            except json.JSONDecodeError:
                logger.warning("Codex app-server returned a non-JSON line")
                continue
            if not isinstance(payload, dict):
                continue
            request_id = payload.get("id")
            if request_id is not None and "method" not in payload:
                future = _state.pending.get(request_id)
                if future and not future.done():
                    future.set_result(payload)
            elif request_id is not None and payload.get("method"):
                asyncio.create_task(_handle_server_request(payload))
            else:
                await _state.events.put(payload)
    except asyncio.CancelledError:
        raise
    except CodexError as exc:
        error = exc
        logger.error("%s", exc)
    except Exception:
        logger.exception("Codex app-server reader failed")
    finally:
        _state.initialized = False
        await _fail_pending(error)


async def _stderr_loop(process: asyncio.subprocess.Process) -> None:
    assert process.stderr is not None
    try:
        async for line in _stream_lines(process.stderr):
            logger.debug("codex app-server: %s", line.decode(errors="replace").rstrip())
    except asyncio.CancelledError:
        raise
    except Exception:
        logger.exception("Codex app-server stderr reader failed")


async def _send(message: dict[str, Any]) -> None:
    process = _state.process
    if not process or not process.stdin:
        raise CodexError("Codex app-server не запущен.")
    data = (json.dumps(message, ensure_ascii=False, separators=(",", ":")) + "\n").encode()
    async with _state.write_lock:
        try:
            process.stdin.write(data)
            await process.stdin.drain()
        except (BrokenPipeError, ConnectionError) as exc:
            raise CodexError("Соединение с Codex app-server разорвано.") from exc


def _rpc_error_message(error: Any) -> str:
    if isinstance(error, dict):
        message = error.get("message")
        if isinstance(message, str) and message:
            return message
    return "Codex app-server вернул ошибку RPC."


async def _rpc(method: str, params: dict[str, Any] | None = None, timeout: int = 30) -> dict[str, Any]:
    loop = asyncio.get_running_loop()
    request_id = _state.next_request_id
    _state.next_request_id += 1
    future: asyncio.Future[dict[str, Any]] = loop.create_future()
    _state.pending[request_id] = future
    try:
        await _send({"method": method, "id": request_id, "params": params or {}})
        response = await asyncio.wait_for(future, timeout=timeout)
    except asyncio.TimeoutError as exc:
        raise CodexError(f"Codex app-server не ответил на {method}.") from exc
    finally:
        _state.pending.pop(request_id, None)
    if response.get("error") is not None:
        raise CodexError(_rpc_error_message(response["error"]))
    result = response.get("result")
    return result if isinstance(result, dict) else {}


def _thread_params() -> dict[str, Any]:
    return {
        "cwd": str(_state.workdir),
        "model": _state.model,
        "config": {"model_reasoning_effort": _state.reasoning_effort},
        "serviceTier": _state.service_tier,
        "developerInstructions": _developer_instructions(),
        "approvalPolicy": APPROVAL_POLICY,
        "approvalsReviewer": APPROVALS_REVIEWER,
        "sandbox": "workspace-write",
    }


async def _handle_server_request(request: dict[str, Any]) -> None:
    method = request.get("method")
    request_id = request.get("id")
    if method in {
        "item/commandExecution/requestApproval",
        "item/fileChange/requestApproval",
        "execCommandApproval",
        "applyPatchApproval",
    }:
        result: dict[str, Any] = {"decision": "acceptForSession"}
    elif method == "mcpServer/elicitation/request":
        result = {"action": "decline"}
    elif method == "item/tool/requestUserInput":
        result = {"answers": {}}
    elif method == "item/permissions/requestApproval":
        result = {
            "permissions": {
                "fileSystem": {"write": [str(_state.workdir)]},
                "network": {"enabled": False},
            },
            "scope": "turn",
            "strictAutoReview": True,
        }
    else:
        logger.warning("Unsupported Codex app-server request: %s", method)
        await _send(
            {
                "id": request_id,
                "error": {"code": -32601, "message": f"Unsupported method: {method}"},
            }
        )
        return
    await _send({"id": request_id, "result": result})


async def _stop_process() -> None:
    process = _state.process
    if not process:
        return
    await _fail_pending(CodexError("Codex app-server остановлен."))
    if process.stdin:
        process.stdin.close()
    if process.returncode is None:
        process.terminate()
        try:
            await asyncio.wait_for(process.wait(), timeout=5)
        except asyncio.TimeoutError:
            process.kill()
            await process.wait()
    for task in (_state.reader_task, _state.stderr_task):
        if task and not task.done():
            task.cancel()
    tasks = [task for task in (_state.reader_task, _state.stderr_task) if task]
    if tasks:
        await asyncio.gather(*tasks, return_exceptions=True)
    _state.process = None
    _state.reader_task = None
    _state.stderr_task = None
    _state.initialized = False


async def start() -> None:
    if _state.mcp_transport != "streamable-http":
        raise CodexError("Для команды «ам» нужен MCP_TRANSPORT=streamable-http.")
    if _is_ready():
        return
    async with _state.start_lock:
        if _is_ready():
            return
        await _stop_process()
        try:
            _state.process = await asyncio.create_subprocess_exec(
                *_server_args(),
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=_state.workdir,
                env=_codex_env(),
                limit=CODEX_STREAM_LIMIT,
            )
            process = _state.process
            _state.reader_task = asyncio.create_task(_reader_loop(process))
            _state.stderr_task = asyncio.create_task(_stderr_loop(process))
            await _rpc(
                "initialize",
                {
                    "clientInfo": {
                        "name": "pyrogram-mcp",
                        "title": "pyrogram-mcp Telegram bridge",
                        "version": "0.1.0",
                    }
                },
                timeout=30,
            )
            await _send({"method": "initialized", "params": {}})

            saved_thread_id = _load_thread_id()
            if saved_thread_id:
                try:
                    result = await _rpc(
                        "thread/resume",
                        {**_thread_params(), "threadId": saved_thread_id},
                        timeout=30,
                    )
                except CodexError as exc:
                    logger.warning("Saved Codex thread cannot be resumed: %s", exc)
                    raise
                else:
                    thread = result.get("thread")
                    if isinstance(thread, dict) and isinstance(thread.get("id"), str):
                        _state.thread_id = thread["id"]
                    else:
                        raise CodexError("Codex не восстановил сохранённый thread; новая сессия не создана.")

            if not _state.thread_id:
                result = await _rpc("thread/start", {**_thread_params(), "ephemeral": False})
                thread = result.get("thread")
                thread_id = thread.get("id") if isinstance(thread, dict) else None
                if not isinstance(thread_id, str) or not thread_id:
                    raise CodexError("Codex app-server не вернул идентификатор thread.")
                _state.thread_id = thread_id
                _save_thread_id(thread_id)
            else:
                _save_thread_id(_state.thread_id)
            _state.initialized = True
            logger.info(
                "Codex app-server started, home=%s, thread=%s",
                _state.codex_home,
                _state.thread_id,
            )
        except (CodexError, OSError):
            await _stop_process()
            raise


async def stop() -> None:
    async with _state.start_lock:
        await _stop_process()


def _turn_error_message(turn: dict[str, Any]) -> str:
    error = turn.get("error")
    if isinstance(error, dict):
        message = error.get("message")
        if isinstance(message, str) and message:
            return message
    if isinstance(error, str) and error:
        return error
    return "Codex не завершил запрос."


def _model_error(message: str) -> CodexError:
    lowered = message.lower()
    if "unknown model" in lowered or "requires a newer codex" in lowered:
        return CodexError(
            f"Модель «{_state.model}» недоступна в текущей версии Codex CLI. "
            "Выберите модель из списка через «.модель» или обновите Codex CLI."
        )
    return CodexError(message)


async def _interrupt(thread_id: str, turn_id: str) -> None:
    try:
        await _rpc(
            "turn/interrupt",
            {"threadId": thread_id, "turnId": turn_id},
            timeout=5,
        )
    except CodexError:
        logger.debug("Unable to interrupt timed-out Codex turn", exc_info=True)


async def _wait_for_turn(thread_id: str, turn_id: str) -> str:
    deadline = asyncio.get_running_loop().time() + _state.timeout if _state.timeout else None
    deltas: dict[str, list[str]] = {}
    message_order: list[str] = []
    completed_messages: dict[str, tuple[str | None, str]] = {}
    while True:
        remaining = deadline - asyncio.get_running_loop().time() if deadline else None
        if remaining is not None and remaining <= 0:
            await _interrupt(thread_id, turn_id)
            raise CodexError("Codex не ответил вовремя.")
        try:
            event = await asyncio.wait_for(
                _state.events.get(), timeout=min(remaining, 1) if remaining is not None else 1
            )
        except asyncio.TimeoutError:
            if not _is_ready():
                raise CodexError("Соединение с Codex app-server закрыто.")
            continue
        method = event.get("method")
        params = event.get("params")
        if not isinstance(params, dict):
            continue
        if params.get("threadId") != thread_id:
            continue
        if params.get("turnId") not in (None, turn_id):
            continue
        event_turn = params.get("turn")
        if isinstance(event_turn, dict) and event_turn.get("id") != turn_id:
            continue
        if method == "item/agentMessage/delta":
            item_id = params.get("itemId")
            delta = params.get("delta")
            if isinstance(item_id, str) and isinstance(delta, str):
                if item_id not in deltas:
                    deltas[item_id] = []
                    message_order.append(item_id)
                deltas[item_id].append(delta)
        elif method == "item/completed":
            item = params.get("item")
            if isinstance(item, dict) and item.get("type") == "agentMessage":
                item_id = item.get("id")
                text = item.get("text")
                if isinstance(item_id, str) and isinstance(text, str):
                    completed_messages[item_id] = (item.get("phase"), text)
        elif method == "error":
            error = params.get("error")
            if isinstance(error, dict) and isinstance(error.get("message"), str):
                raise _model_error(error["message"])
        elif method == "turn/completed":
            turn = params.get("turn")
            if not isinstance(turn, dict):
                raise CodexError("Codex завершил turn без результата.")
            if turn.get("status") not in {"completed", "success"}:
                raise _model_error(_turn_error_message(turn))
            final_messages = [
                text
                for phase, text in completed_messages.values()
                if phase == "final_answer"
            ]
            if final_messages:
                result = final_messages[-1]
            else:
                unknown_messages = [
                    text
                    for phase, text in completed_messages.values()
                    if phase is None
                ]
                result = unknown_messages[-1] if unknown_messages else "".join(
                    "".join(deltas[item_id]) for item_id in message_order
                )
            result = result.strip()
            if not result:
                raise CodexError("Codex завершился без ответа.")
            if len(result) > MAX_OUTPUT_LENGTH:
                result = result[:MAX_OUTPUT_LENGTH].rstrip() + "\n…"
            return result


async def _turn(user_prompt: str) -> str:
    if not _state.thread_id:
        raise CodexError("Codex thread не инициализирован.")
    result = await _rpc(
        "turn/start",
        {
            "threadId": _state.thread_id,
            "input": [{"type": "text", "text": user_prompt}],
            "model": _state.model,
            "effort": _state.reasoning_effort,
            "serviceTier": _state.service_tier,
            "approvalPolicy": APPROVAL_POLICY,
            "approvalsReviewer": APPROVALS_REVIEWER,
        },
        timeout=30,
    )
    turn = result.get("turn")
    turn_id = turn.get("id") if isinstance(turn, dict) else None
    if not isinstance(turn_id, str) or not turn_id:
        raise CodexError("Codex app-server не вернул идентификатор turn.")
    return await _wait_for_turn(_state.thread_id, turn_id)


async def ask(user_prompt: str) -> str:
    user_prompt = user_prompt.strip()
    if not user_prompt:
        raise ValueError("Пустой запрос.")
    if len(user_prompt) > MAX_PROMPT_LENGTH:
        raise ValueError(f"Запрос слишком длинный; максимум {MAX_PROMPT_LENGTH} символов.")
    if _state.mcp_transport != "streamable-http":
        raise CodexError("Для команды «ам» нужен MCP_TRANSPORT=streamable-http.")
    if _ask_lock.locked():
        raise CodexBusy("Предыдущий запрос Codex ещё выполняется.")

    async with _ask_lock:
        await start()
        return await _turn(user_prompt)
