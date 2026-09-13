from __future__ import annotations

from typing import Any


def chat_id(value: int | str) -> int | str:
    """Keep usernames/links intact and normalize numeric identifiers."""
    if isinstance(value, bool):
        raise TypeError("chat_id must be an integer or string")
    if isinstance(value, int):
        return value
    value = value.strip()
    if not value:
        raise ValueError("chat_id must not be empty")
    try:
        return int(value)
    except ValueError:
        return value


def message_ids(value: int | list[int]) -> int | list[int]:
    if isinstance(value, bool):
        raise TypeError("message_ids must contain integers")
    if isinstance(value, int):
        return value
    if not value or any(
        isinstance(item, bool) or not isinstance(item, int) for item in value
    ):
        raise ValueError("message_ids must contain at least one integer")
    return value


def clamp_limit(value: int, *, default: int = 20, maximum: int = 100) -> int:
    if value <= 0:
        return default
    return min(value, maximum)


async def resolve_peer_marker(client: Any, value: Any) -> Any:
    return await client.resolve_peer(chat_id(value))
