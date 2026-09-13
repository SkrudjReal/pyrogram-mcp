from __future__ import annotations

import base64
from datetime import date, datetime, time
from enum import Enum
from typing import Any

from pyrogram.raw.core import TLObject

_MASKED_FIELDS = {"code", "phone", "token", "autologin_token", "logout_tokens"}
_MAX_DEPTH = 8
_MAX_ITEMS = 200


def _slots(value: Any) -> list[str]:
    names: list[str] = []
    for cls in type(value).__mro__:
        slots = getattr(cls, "__slots__", ())
        names.extend((slots,) if isinstance(slots, str) else slots)
    return list(dict.fromkeys(name for name in names if isinstance(name, str)))


def to_jsonable(value: Any, *, depth: int = 0, seen: set[int] | None = None) -> Any:
    """Convert Kurigram and ordinary Python values to bounded JSON data."""
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, bytes):
        return {"_": "__bytes__", "base64": base64.b64encode(value).decode("ascii")}
    if isinstance(value, (datetime, date, time)):
        return value.isoformat()
    if isinstance(value, Enum):
        return (
            value.value
            if isinstance(value.value, (str, int, float, bool))
            else value.name
        )
    if depth >= _MAX_DEPTH:
        return f"<{type(value).__name__}: depth limit>"

    seen = seen or set()
    object_id = id(value)
    if object_id in seen:
        return f"<{type(value).__name__}: recursive>"

    if isinstance(value, dict):
        seen.add(object_id)
        result = {
            str(key): to_jsonable(item, depth=depth + 1, seen=seen)
            for key, item in list(value.items())[:_MAX_ITEMS]
        }
        seen.discard(object_id)
        return result
    if isinstance(value, (list, tuple, set, frozenset)):
        seen.add(object_id)
        result = [
            to_jsonable(item, depth=depth + 1, seen=seen)
            for item in list(value)[:_MAX_ITEMS]
        ]
        seen.discard(object_id)
        return result

    names = _slots(value)
    if not names and hasattr(value, "__dict__"):
        names = list(vars(value))
    if names:
        seen.add(object_id)
        result = {"_": getattr(value, "QUALNAME", type(value).__name__)}
        for name in names[:_MAX_ITEMS]:
            if name.startswith("_") or not hasattr(value, name):
                continue
            item = getattr(value, name)
            if item is None:
                continue
            result[name] = (
                "*" * 9
                if name in _MASKED_FIELDS
                else to_jsonable(item, depth=depth + 1, seen=seen)
            )
        seen.discard(object_id)
        return result

    if isinstance(value, TLObject):
        return {"_": getattr(value, "QUALNAME", type(value).__name__)}
    return str(value)
