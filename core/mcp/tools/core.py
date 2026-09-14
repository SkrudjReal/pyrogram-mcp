from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

from core.mcp.errors import safe
from core.runtime import get_runtime
from core.service import telegram
from core.telegram.serialization import to_jsonable


async def _json(action: Any) -> Any:
    return to_jsonable(await action)


def register(mcp: FastMCP) -> None:
    read = ToolAnnotations(readOnlyHint=True, openWorldHint=True)
    write = ToolAnnotations(destructiveHint=False, openWorldHint=True)

    @mcp.tool(
        title="Get current Telegram account", annotations=read, structured_output=True
    )
    async def get_me() -> dict[str, Any]:
        """Return the current Kurigram account."""
        return await safe(
            "get_me", lambda: _json(telegram.get_me(get_runtime().client))
        )

    @mcp.tool(title="List Telegram chats", annotations=read, structured_output=True)
    async def list_chats(
        chat_type: str | None = None, limit: int = 20
    ) -> dict[str, Any]:
        """List dialogs. chat_type may be private, bot, group, supergroup or channel."""
        return await safe(
            "list_chats",
            lambda: _json(
                telegram.list_chats(
                    get_runtime().client, chat_type=chat_type, limit=limit
                )
            ),
        )

    @mcp.tool(title="Get Telegram chat", annotations=read, structured_output=True)
    async def get_chat(chat_id: int | str) -> dict[str, Any]:
        """Return metadata for a chat ID, username or supported Telegram link."""
        return await safe(
            "get_chat", lambda: _json(telegram.get_chat(get_runtime().client, chat_id))
        )

    @mcp.tool(title="Get Telegram messages", annotations=read, structured_output=True)
    async def get_messages(
        chat_id: int | str,
        message_ids: list[int] | None = None,
        limit: int = 20,
        offset_id: int = 0,
    ) -> dict[str, Any]:
        """Read up to 100 messages. Batch known IDs in message_ids.

        For older history, pass the smallest returned ID as offset_id (exclusive).
        Use search_messages with from_user to find an author's messages efficiently.
        """
        return await safe(
            "get_messages",
            lambda: _json(
                telegram.get_messages(
                    get_runtime().client,
                    chat_id,
                    ids=message_ids,
                    limit=limit,
                    offset_id=offset_id,
                )
            ),
        )

    @mcp.tool(title="Search messages in chat", annotations=read, structured_output=True)
    async def search_messages(
        chat_id: int | str, query: str = "", limit: int = 20,
        from_user: int | str | None = None, offset: int = 0,
        min_id: int = 0, max_id: int = 0,
    ) -> dict[str, Any]:
        """Server-side search, up to 100 results. from_user='me' finds own messages.

        Empty query allows author-only search. min_id/max_id are exclusive bounds.
        Page older results with max_id=min(returned IDs), preserving all filters;
        stop on an empty page. offset is a result offset, not a message ID.
        """
        return await safe(
            "search_messages",
            lambda: _json(
                telegram.search_messages(
                    get_runtime().client, chat_id, query, limit=limit,
                    from_user=from_user, offset=offset, min_id=min_id, max_id=max_id,
                )
            ),
        )

    @mcp.tool(
        title="Search messages globally", annotations=read, structured_output=True
    )
    async def search_global(query: str, limit: int = 20) -> dict[str, Any]:
        """Search public Telegram message index when supported by Kurigram."""
        return await safe(
            "search_global",
            lambda: _json(
                telegram.search_global(get_runtime().client, query, limit=limit)
            ),
        )

    @mcp.tool(
        title="Resolve Telegram username", annotations=read, structured_output=True
    )
    async def resolve_username(username: str) -> dict[str, Any]:
        """Resolve a username to a serialized Telegram user or chat."""
        return await safe(
            "resolve_username",
            lambda: _json(telegram.resolve_username(get_runtime().client, username)),
        )

    @mcp.tool(title="Send Telegram message", annotations=write, structured_output=True)
    async def send_message(
        chat_id: int | str,
        text: str,
        reply_to_message_id: int | None = None,
        message_thread_id: int | None = None,
        disable_notification: bool | None = None,
    ) -> dict[str, Any]:
        """Send a text message, optionally as a reply or forum-topic message."""
        return await safe(
            "send_message",
            lambda: _json(
                telegram.send_message(
                    get_runtime().client,
                    chat_id,
                    text,
                    reply_to_message_id=reply_to_message_id,
                    message_thread_id=message_thread_id,
                    disable_notification=disable_notification,
                )
            ),
        )

    @mcp.tool(title="Edit Telegram message", annotations=write, structured_output=True)
    async def edit_message(
        chat_id: int | str, message_id: int, text: str
    ) -> dict[str, Any]:
        """Edit a message sent by the current account."""
        return await safe(
            "edit_message",
            lambda: _json(
                telegram.edit_message(get_runtime().client, chat_id, message_id, text)
            ),
        )

    @mcp.tool(
        title="Delete Telegram messages", annotations=write, structured_output=True
    )
    async def delete_messages(
        chat_id: int | str, message_ids: int | list[int], revoke: bool = True
    ) -> dict[str, Any]:
        """Delete one or more messages and return the affected count."""
        return await safe(
            "delete_messages",
            lambda: telegram.delete_messages(
                get_runtime().client, chat_id, message_ids, revoke=revoke
            ),
        )

    @mcp.tool(
        title="Forward Telegram messages", annotations=write, structured_output=True
    )
    async def forward_messages(
        chat_id: int | str, from_chat_id: int | str, message_ids: int | list[int]
    ) -> dict[str, Any]:
        """Forward one or more messages while retaining the original link."""
        return await safe(
            "forward_messages",
            lambda: _json(
                telegram.forward_messages(
                    get_runtime().client, chat_id, from_chat_id, message_ids
                )
            ),
        )

    @mcp.tool(title="Copy Telegram message", annotations=write, structured_output=True)
    async def copy_message(
        chat_id: int | str,
        from_chat_id: int | str,
        message_id: int,
        caption: str | None = None,
    ) -> dict[str, Any]:
        """Copy a message without linking it to the source."""
        return await safe(
            "copy_message",
            lambda: _json(
                telegram.copy_message(
                    get_runtime().client,
                    chat_id,
                    from_chat_id,
                    message_id,
                    caption=caption,
                )
            ),
        )

    @mcp.tool(
        title="Mark Telegram chat as read", annotations=write, structured_output=True
    )
    async def mark_as_read(chat_id: int | str) -> dict[str, Any]:
        """Mark the chat history as read."""
        return await safe(
            "mark_as_read", lambda: telegram.mark_as_read(get_runtime().client, chat_id)
        )

    @mcp.tool(title="Get message context", annotations=read, structured_output=True)
    async def get_message_context(
        chat_id: int | str, message_id: int, context_size: int = 10
    ) -> dict[str, Any]:
        """Return nearby messages around a target message."""
        return await safe(
            "get_message_context",
            lambda: _json(
                telegram.get_message_context(
                    get_runtime().client, chat_id, message_id, context_size=context_size
                )
            ),
        )

    @mcp.tool(title="Get chat context", annotations=read, structured_output=True)
    async def get_chat_context(chat_id: int | str, limit: int = 20) -> dict[str, Any]:
        """Return chat metadata and recent messages in one request."""
        return await safe(
            "get_chat_context",
            lambda: _chat_context(get_runtime().client, chat_id, limit),
        )


async def _chat_context(client: Any, chat_id: int | str, limit: int) -> dict[str, Any]:
    chat = await telegram.get_chat(client, chat_id)
    messages = await telegram.get_messages(client, chat_id, limit=limit)
    return {"chat": to_jsonable(chat), "messages": to_jsonable(messages)}
