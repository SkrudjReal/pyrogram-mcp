from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Runtime:
    client: Any
    me: Any
    dispatcher: Any = None
    redis: Any = None
    pool: Any = None
    repo: Any = None
    allowed_roots: tuple[Any, ...] = ()


_runtime: Runtime | None = None


def set_runtime(runtime: Runtime) -> None:
    global _runtime
    _runtime = runtime


def get_runtime() -> Runtime:
    if _runtime is None:
        raise RuntimeError("Telegram runtime is not initialized")
    return _runtime


def clear_runtime() -> None:
    global _runtime
    _runtime = None
