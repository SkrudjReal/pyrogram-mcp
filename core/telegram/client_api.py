from __future__ import annotations

import base64
import importlib
import inspect
from dataclasses import dataclass
from datetime import datetime
from typing import Any

_DENIED = {
    "authorize",
    "check_password",
    "connect",
    "disconnect",
    "export_session_string",
    "idle",
    "invoke",
    "log_out",
    "run",
    "send_code",
    "sign_in",
    "sign_up",
    "start",
    "stop",
    "terminate",
}


@dataclass(frozen=True, slots=True)
class ClientMethod:
    name: str
    signature: str
    function: Any


def _decode(value: Any) -> Any:
    if isinstance(value, list):
        return [_decode(item) for item in value]
    if not isinstance(value, dict):
        return value
    marker = value.get("_") or value.get("__type__")
    if marker == "__bytes__":
        return base64.b64decode(value["base64"], validate=True)
    if marker == "__datetime__":
        return datetime.fromisoformat(value["value"])
    if isinstance(marker, str) and marker.startswith("types."):
        cls = getattr(
            importlib.import_module("pyrogram.types"),
            marker.removeprefix("types."),
            None,
        )
        if cls is None:
            raise ValueError(f"Unknown high-level Kurigram type: {marker}")
        return cls(
            **{
                key: _decode(item)
                for key, item in value.items()
                if key not in {"_", "__type__"}
            }
        )
    if isinstance(marker, str) and marker.startswith("enums."):
        enum = getattr(
            importlib.import_module("pyrogram.enums"),
            marker.removeprefix("enums."),
            None,
        )
        if enum is None:
            raise ValueError(f"Unknown Kurigram enum: {marker}")
        enum_value = value.get("value")
        return (
            enum[enum_value]
            if isinstance(enum_value, str) and enum_value in enum.__members__
            else enum(enum_value)
        )
    return {key: _decode(item) for key, item in value.items()}


def _catalog(client: Any) -> dict[str, ClientMethod]:
    methods = {}
    for name in dir(client):
        if name.startswith("_") or name in _DENIED:
            continue
        try:
            method = getattr(client, name)
        except (AttributeError, RuntimeError, TypeError):
            continue
        target = method
        while getattr(target, "__wrapped__", None) is not None:
            target = target.__wrapped__
        if not (
            inspect.iscoroutinefunction(target) or inspect.isasyncgenfunction(target)
        ):
            continue
        methods[name.casefold()] = ClientMethod(
            name, str(inspect.signature(method)), method
        )
    return methods


def search_client(
    client: Any, query: str = "", limit: int = 50, offset: int = 0
) -> list[dict[str, str]]:
    query = query.strip().casefold()
    methods = [
        method
        for method in _catalog(client).values()
        if query in method.name.casefold()
    ]
    methods.sort(key=lambda method: method.name)
    start = max(offset, 0)
    return [
        {"method": method.name, "signature": method.signature}
        for method in methods[start : start + max(1, min(limit, 200))]
    ]


def describe_client(client: Any, name: str) -> dict[str, str]:
    method = _catalog(client).get(name.strip().casefold())
    if method is None:
        raise ValueError(f"Unknown or unavailable Kurigram client method: {name}")
    return {
        "method": method.name,
        "signature": method.signature,
        "doc": inspect.getdoc(method.function) or "",
    }


async def call_client(
    client: Any, name: str, params: dict[str, Any] | None = None
) -> Any:
    method = _catalog(client).get(name.strip().casefold())
    if method is None:
        raise ValueError(f"Unknown or unavailable Kurigram client method: {name}")
    params = params or {}
    if not isinstance(params, dict):
        raise TypeError("params must be an object")
    result = method.function(**{key: _decode(value) for key, value in params.items()})
    if inspect.isasyncgen(result):
        items = []
        async for item in result:
            items.append(item)
            if len(items) >= 100:
                break
        return items
    return await result
