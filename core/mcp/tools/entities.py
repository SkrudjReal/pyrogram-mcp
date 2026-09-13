from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

from core.mcp.errors import safe
from core.runtime import get_runtime
from core.telegram.client_api import call_client
from core.telegram.resolve import clamp_limit
from core.telegram.serialization import to_jsonable


async def _call(method: str, params: dict[str, Any] | None = None) -> Any:
    return to_jsonable(await call_client(get_runtime().client, method, params))


def register(mcp: FastMCP) -> None:
    read = ToolAnnotations(readOnlyHint=True, openWorldHint=True)
    write = ToolAnnotations(destructiveHint=False, openWorldHint=True)
    destructive = ToolAnnotations(destructiveHint=True, openWorldHint=True)

    @mcp.tool(title="List Telegram contacts", annotations=read, structured_output=True)
    async def list_contacts() -> dict[str, Any]:
        """Return contacts from the current Telegram account."""
        return await safe("list_contacts", lambda: _call("get_contacts"))

    @mcp.tool(
        title="Search Telegram contacts", annotations=read, structured_output=True
    )
    async def search_contacts(query: str, limit: int = 20) -> dict[str, Any]:
        """Search contacts and users by a name substring."""
        return await safe(
            "search_contacts",
            lambda: _call(
                "search_contacts", {"query": query, "limit": clamp_limit(limit)}
            ),
        )

    @mcp.tool(title="Add Telegram contact", annotations=write, structured_output=True)
    async def add_contact(
        user_id: int | str,
        first_name: str,
        last_name: str = "",
        phone_number: str = "",
        share_phone_number: bool = False,
    ) -> dict[str, Any]:
        """Add an existing Telegram user to contacts."""
        return await safe(
            "add_contact",
            lambda: _call(
                "add_contact",
                {
                    "user_id": user_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone_number": phone_number,
                    "share_phone_number": share_phone_number,
                },
            ),
        )

    @mcp.tool(
        title="Delete Telegram contact", annotations=destructive, structured_output=True
    )
    async def delete_contact(user_id: int | str) -> dict[str, Any]:
        """Delete one Telegram contact."""
        return await safe(
            "delete_contact", lambda: _call("delete_contacts", {"user_ids": user_id})
        )

    @mcp.tool(
        title="Block Telegram user", annotations=destructive, structured_output=True
    )
    async def block_user(user_id: int | str) -> dict[str, Any]:
        """Block a Telegram user."""
        return await safe(
            "block_user", lambda: _call("block_user", {"user_id": user_id})
        )

    @mcp.tool(title="Unblock Telegram user", annotations=write, structured_output=True)
    async def unblock_user(user_id: int | str) -> dict[str, Any]:
        """Unblock a Telegram user."""
        return await safe(
            "unblock_user", lambda: _call("unblock_user", {"user_id": user_id})
        )

    @mcp.tool(title="List chat members", annotations=read, structured_output=True)
    async def get_participants(
        chat_id: int | str, query: str = "", limit: int = 50
    ) -> dict[str, Any]:
        """List members of a group or channel."""
        return await safe(
            "get_participants",
            lambda: _call(
                "get_chat_members",
                {
                    "chat_id": chat_id,
                    "query": query,
                    "limit": clamp_limit(limit, maximum=100),
                },
            ),
        )

    @mcp.tool(title="Create Telegram group", annotations=write, structured_output=True)
    async def create_group(
        title: str, users: int | str | list[int | str]
    ) -> dict[str, Any]:
        """Create a basic Telegram group."""
        return await safe(
            "create_group",
            lambda: _call("create_group", {"title": title, "users": users}),
        )

    @mcp.tool(
        title="Create Telegram supergroup", annotations=write, structured_output=True
    )
    async def create_supergroup(title: str, is_forum: bool = False) -> dict[str, Any]:
        """Create a Telegram supergroup, optionally as a forum."""
        return await safe(
            "create_supergroup",
            lambda: _call("create_supergroup", {"title": title, "is_forum": is_forum}),
        )

    @mcp.tool(
        title="Create Telegram channel", annotations=write, structured_output=True
    )
    async def create_channel(title: str, description: str = "") -> dict[str, Any]:
        """Create a Telegram broadcast channel."""
        return await safe(
            "create_channel",
            lambda: _call(
                "create_channel", {"title": title, "description": description}
            ),
        )

    @mcp.tool(title="Set chat title", annotations=write, structured_output=True)
    async def set_chat_title(chat_id: int | str, title: str) -> dict[str, Any]:
        """Change a group or channel title."""
        return await safe(
            "set_chat_title",
            lambda: _call("set_chat_title", {"chat_id": chat_id, "title": title}),
        )

    @mcp.tool(
        title="Leave Telegram chat", annotations=destructive, structured_output=True
    )
    async def leave_chat(chat_id: int | str) -> dict[str, Any]:
        """Leave a group, supergroup or channel."""
        return await safe(
            "leave_chat", lambda: _call("leave_chat", {"chat_id": chat_id})
        )

    @mcp.tool(title="Create forum topic", annotations=write, structured_output=True)
    async def create_forum_topic(
        chat_id: int | str,
        title: str,
        icon_color: int | None = None,
        icon_emoji_id: int | None = None,
    ) -> dict[str, Any]:
        """Create a topic in a Telegram forum supergroup."""
        return await safe(
            "create_forum_topic",
            lambda: _call(
                "create_forum_topic",
                {
                    "chat_id": chat_id,
                    "title": title,
                    "icon_color": icon_color,
                    "icon_emoji_id": icon_emoji_id,
                },
            ),
        )

    @mcp.tool(title="List forum topics", annotations=read, structured_output=True)
    async def list_topics(chat_id: int | str, limit: int = 50) -> dict[str, Any]:
        """List topics in a Telegram forum supergroup."""
        return await safe(
            "list_topics",
            lambda: _call(
                "get_forum_topics",
                {"chat_id": chat_id, "limit": clamp_limit(limit, maximum=100)},
            ),
        )

    @mcp.tool(title="Ban chat member", annotations=destructive, structured_output=True)
    async def ban_user(
        chat_id: int | str, user_id: int | str, until_date: int | None = None
    ) -> dict[str, Any]:
        """Ban a member from a group or channel."""
        return await safe(
            "ban_user",
            lambda: _call(
                "ban_chat_member",
                {"chat_id": chat_id, "user_id": user_id, "until_date": until_date},
            ),
        )

    @mcp.tool(title="Unban chat member", annotations=write, structured_output=True)
    async def unban_user(chat_id: int | str, user_id: int | str) -> dict[str, Any]:
        """Remove a member ban without adding the user back."""
        return await safe(
            "unban_user",
            lambda: _call(
                "unban_chat_member", {"chat_id": chat_id, "user_id": user_id}
            ),
        )

    @mcp.tool(
        title="Update Telegram profile", annotations=write, structured_output=True
    )
    async def update_profile(
        first_name: str | None = None,
        last_name: str | None = None,
        bio: str | None = None,
    ) -> dict[str, Any]:
        """Update the current account profile fields."""
        return await safe(
            "update_profile",
            lambda: _call(
                "update_profile",
                {"first_name": first_name, "last_name": last_name, "bio": bio},
            ),
        )
