from __future__ import annotations

from pyrogram import Client, enums
from pyrogram.types import Message

from core.service import codex
from core.settings import logger


MAX_TELEGRAM_TEXT = 3900


def _chunks(text: str) -> list[str]:
    return [text[index : index + MAX_TELEGRAM_TEXT] for index in range(0, len(text), MAX_TELEGRAM_TEXT)]


async def _reply(message: Message, text: str) -> None:
    for chunk in _chunks(text) or [""]:
        await message.reply_text(chunk, parse_mode=enums.ParseMode.DISABLED)


async def _finish(status: Message, message: Message, text: str) -> None:
    chunks = _chunks(text) or [""]
    try:
        await status.edit_text(chunks[0], parse_mode=enums.ParseMode.DISABLED)
    except Exception:
        logger.exception("Failed to edit Codex status message")
        await _reply(message, text)
        return
    for chunk in chunks[1:]:
        await message.reply_text(chunk, parse_mode=enums.ParseMode.DISABLED)


async def ask_codex(app: Client, msg: Message) -> None:
    prompt = (msg.text or "").partition(" ")[2].strip()
    if not prompt:
        await _reply(msg, "Использование: ам <текст запроса>")
        return
    status = await msg.reply_text(
        "⏳ Codex обрабатывает запрос…",
        parse_mode=enums.ParseMode.DISABLED,
    )
    try:
        result = await codex.ask(prompt)
    except codex.CodexBusy as exc:
        await _finish(status, msg, str(exc))
    except (codex.CodexError, ValueError) as exc:
        await _finish(status, msg, f"Ошибка: {exc}")
    except Exception:
        logger.exception("Unhandled error in Codex Telegram handler")
        await _finish(status, msg, "Ошибка: не удалось получить ответ от Codex.")
    else:
        await _finish(status, msg, result)


async def model_command(app: Client, msg: Message) -> None:
    argument = (msg.text or "").partition(" ")[2].strip()
    if argument:
        try:
            selected = codex.set_model(argument)
        except ValueError as exc:
            await _reply(msg, f"Ошибка: {exc}")
            return
        await _reply(
            msg,
            f"Модель установлена: {selected}\nReasoning: {codex.current_reasoning()}",
        )
        return

    try:
        models = await codex.list_models()
    except codex.CodexError as exc:
        await _reply(msg, f"Ошибка: {exc}")
        return

    lines = [f"Текущая модель: {codex.current_model()}", "", "Модели Codex:"]
    listed = set()
    for item in models:
        slug = str(item["slug"])
        listed.add(slug)
        title = item.get("display_name") or slug
        levels = ", ".join(
            str(level.get("effort"))
            for level in item.get("supported_reasoning_levels", [])
            if isinstance(level, dict) and level.get("effort")
        )
        suffix = f" [{levels}]" if levels else ""
        lines.append(f"{slug} — {title}{suffix}")
    if codex.current_model() not in listed:
        current_suffix = f" [{codex.current_reasoning()}]"
        lines.append(f"{codex.current_model()} — текущая локальная модель{current_suffix}")
    lines.append("\nВыбор: .модель <slug>")
    await _reply(msg, "\n".join(lines))


async def reasoning_command(app: Client, msg: Message) -> None:
    try:
        models = await codex.list_models()
    except codex.CodexError:
        models = []
    info = codex.reasoning_info(models)
    lines = [
        f"Текущая модель: {info['model']}",
        f"Reasoning: {info['effort']} — {info['description']}",
    ]
    if info["supported"]:
        lines.append(f"Доступные уровни модели: {', '.join(info['supported'])}")
    else:
        lines.append("Карточка текущей модели отсутствует в каталоге; показан локальный effort Codex.")
    await _reply(msg, "\n".join(lines))


async def speed_command(app: Client, msg: Message) -> None:
    argument = (msg.text or "").partition(" ")[2].strip()
    if argument:
        try:
            selected = codex.set_speed(argument)
        except ValueError as exc:
            await _reply(msg, f"Ошибка: {exc}")
            return
        await _reply(msg, f"Скорость Codex установлена: {selected}")
        return
    await _reply(
        msg,
        f"Скорость Codex: {codex.current_speed()}\n"
        "Доступно: normal (обычная) и fast (быстрая, приоритетная).\n"
        "Выбор: .скорость <normal|fast>",
    )
