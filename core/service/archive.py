from __future__ import annotations

import json
from typing import Any

from core.telegram.serialization import to_jsonable

_TTL_SECONDS = 7 * 24 * 60 * 60


def snapshot_key(chat_id: int, message_id: int) -> str:
    return f"telegram:mcp:snapshot:{chat_id}:{message_id}"


async def save_message(redis: Any, message: Any, *, event: str = "new") -> None:
    if redis is None or getattr(message, "chat", None) is None:
        return
    record = {
        "event": event,
        "chat_id": message.chat.id,
        "message_id": message.id,
        "message": to_jsonable(message),
    }
    await redis.set(
        snapshot_key(message.chat.id, message.id),
        json.dumps(record, ensure_ascii=False),
        ex=_TTL_SECONDS,
    )


async def mark_deleted(redis: Any, message: Any) -> None:
    if redis is None or getattr(message, "chat", None) is None:
        return
    key = snapshot_key(message.chat.id, message.id)
    snapshot = await redis.get(key)
    record = json.loads(snapshot) if snapshot else {}
    record.update(
        {"event": "deleted", "chat_id": message.chat.id, "message_id": message.id}
    )
    await redis.set(key, json.dumps(record, ensure_ascii=False), ex=_TTL_SECONDS)
