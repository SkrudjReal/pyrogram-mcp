from __future__ import annotations

from typing import Any

from core.service.archive import mark_deleted, save_message


async def archive_message(app: Any, message: Any, redis: Any = None) -> None:
    await save_message(redis, message)


async def archive_edited_message(app: Any, message: Any, redis: Any = None) -> None:
    await save_message(redis, message, event="edited")


async def archive_deleted_messages(
    app: Any, messages: list[Any], redis: Any = None
) -> None:
    for message in messages:
        await mark_deleted(redis, message)
