from __future__ import annotations

from typing import Any

from core.telegram.resolve import chat_id, clamp_limit, message_ids


async def get_me(client: Any) -> Any:
    return await client.get_me()


async def list_chats(
    client: Any, *, limit: int = 20, chat_type: str | None = None
) -> list[Any]:
    result = []
    for_chat_type = chat_type.casefold() if chat_type else None
    async for dialog in client.get_dialogs(limit=clamp_limit(limit)):
        chat = dialog.chat
        current_type = getattr(getattr(chat, "type", None), "value", None)
        if for_chat_type and current_type != for_chat_type:
            continue
        result.append(chat)
    return result


async def get_chat(client: Any, target: int | str) -> Any:
    return await client.get_chat(chat_id(target), force_full=False)


async def get_messages(
    client: Any,
    target: int | str,
    *,
    ids: list[int] | None = None,
    limit: int = 20,
    offset_id: int = 0,
) -> Any:
    target = chat_id(target)
    if ids is not None:
        return await client.get_messages(target, message_ids(ids))
    result = []
    async for message in client.get_chat_history(
        target, limit=clamp_limit(limit), offset_id=max(offset_id, 0)
    ):
        result.append(message)
    return result


async def search_messages(
    client: Any, target: int | str, query: str, *, limit: int = 20
) -> list[Any]:
    result = []
    async for message in client.search_messages(
        chat_id(target), query=query, limit=clamp_limit(limit)
    ):
        result.append(message)
    return result


async def search_global(client: Any, query: str, *, limit: int = 20) -> list[Any]:
    method = getattr(client, "search_global", None)
    if method is None:
        raise NotImplementedError("This Kurigram version has no search_global method")
    result = []
    async for message in method(query=query, limit=clamp_limit(limit)):
        result.append(message)
    return result


async def resolve_username(client: Any, username: str) -> Any:
    username = username.strip()
    if not username:
        raise ValueError("username must not be empty")
    return await client.get_users(username.removeprefix("@"))


async def send_message(
    client: Any,
    target: int | str,
    text: str,
    *,
    reply_to_message_id: int | None = None,
    message_thread_id: int | None = None,
    disable_notification: bool | None = None,
) -> Any:
    return await client.send_message(
        chat_id(target),
        text,
        reply_to_message_id=reply_to_message_id,
        message_thread_id=message_thread_id,
        disable_notification=disable_notification,
    )


async def edit_message(
    client: Any, target: int | str, message_id: int, text: str
) -> Any:
    return await client.edit_message_text(chat_id(target), message_id, text=text)


async def delete_messages(
    client: Any, target: int | str, ids: int | list[int], *, revoke: bool = True
) -> int:
    return await client.delete_messages(
        chat_id(target), message_ids(ids), revoke=revoke
    )


async def forward_messages(
    client: Any, target: int | str, source: int | str, ids: int | list[int]
) -> Any:
    return await client.forward_messages(
        chat_id(target), chat_id(source), message_ids(ids)
    )


async def copy_message(
    client: Any,
    target: int | str,
    source: int | str,
    message_id: int,
    *,
    caption: str | None = None,
) -> Any:
    return await client.copy_message(
        chat_id(target),
        from_chat_id=chat_id(source),
        message_id=message_id,
        caption=caption,
    )


async def mark_as_read(client: Any, target: int | str) -> Any:
    return await client.read_chat_history(chat_id(target))


async def get_message_context(
    client: Any, target: int | str, message_id: int, *, context_size: int = 10
) -> list[Any]:
    size = clamp_limit(context_size, default=10, maximum=50)
    result = []
    async for message in client.get_chat_history(
        chat_id(target), limit=(size * 2) + 1, offset_id=message_id + size
    ):
        result.append(message)
    return result
