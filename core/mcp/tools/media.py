from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

from core.mcp.errors import safe
from core.runtime import get_runtime
from core.service import media
from core.telegram.serialization import to_jsonable


async def _json(action: Any) -> Any:
    return to_jsonable(await action)


def register(mcp: FastMCP) -> None:
    read = ToolAnnotations(readOnlyHint=True, openWorldHint=True)
    write = ToolAnnotations(destructiveHint=False, openWorldHint=True)
    runtime = get_runtime

    @mcp.tool(title="Get message media info", annotations=read, structured_output=True)
    async def get_media_info(chat_id: int | str, message_id: int) -> dict[str, Any]:
        """Return the media kind and metadata for a message."""
        rt = runtime()
        return await safe(
            "get_media_info",
            lambda: _json(media.get_media_info(rt.client, chat_id, message_id)),
        )

    @mcp.tool(title="Send Telegram file", annotations=write, structured_output=True)
    async def send_file(
        chat_id: int | str, file_path: str, caption: str | None = None
    ) -> dict[str, Any]:
        """Send a local file from configured MEDIA_ROOTS as a document."""
        rt = runtime()
        return await safe(
            "send_file",
            lambda: _json(
                media.send_file(
                    rt.client, rt.allowed_roots, chat_id, file_path, caption
                )
            ),
        )

    @mcp.tool(
        title="Download Telegram media", annotations=write, structured_output=True
    )
    async def download_media(
        chat_id: int | str, message_id: int, file_path: str | None = None
    ) -> dict[str, Any]:
        """Download message media under configured MEDIA_ROOTS."""
        rt = runtime()
        return await safe(
            "download_media",
            lambda: media.download_media(
                rt.client, rt.allowed_roots, chat_id, message_id, file_path
            ),
        )

    @mcp.tool(title="Upload Telegram file", annotations=write, structured_output=True)
    async def upload_file(file_path: str) -> dict[str, Any]:
        """Upload a local file from configured MEDIA_ROOTS and return its raw input file."""
        rt = runtime()
        return await safe(
            "upload_file",
            lambda: _json(media.upload_file(rt.client, rt.allowed_roots, file_path)),
        )

    @mcp.tool(
        title="Send Telegram voice note", annotations=write, structured_output=True
    )
    async def send_voice(
        chat_id: int | str, file_path: str, caption: str | None = None
    ) -> dict[str, Any]:
        """Send an .ogg or .opus voice note from configured MEDIA_ROOTS."""
        rt = runtime()
        return await safe(
            "send_voice",
            lambda: _json(
                media.send_voice(
                    rt.client, rt.allowed_roots, chat_id, file_path, caption
                )
            ),
        )

    @mcp.tool(title="Send Telegram sticker", annotations=write, structured_output=True)
    async def send_sticker(chat_id: int | str, file_path: str) -> dict[str, Any]:
        """Send a .webp or .tgs sticker from configured MEDIA_ROOTS."""
        rt = runtime()
        return await safe(
            "send_sticker",
            lambda: _json(
                media.send_sticker(rt.client, rt.allowed_roots, chat_id, file_path)
            ),
        )

    @mcp.tool(title="Set profile photo", annotations=write, structured_output=True)
    async def set_profile_photo(file_path: str) -> dict[str, Any]:
        """Set the current account profile photo from configured MEDIA_ROOTS."""
        rt = runtime()
        return await safe(
            "set_profile_photo",
            lambda: _json(
                media.set_profile_photo(rt.client, rt.allowed_roots, file_path)
            ),
        )

    @mcp.tool(title="Edit chat photo", annotations=write, structured_output=True)
    async def edit_chat_photo(chat_id: int | str, file_path: str) -> dict[str, Any]:
        """Set a chat photo from configured MEDIA_ROOTS."""
        rt = runtime()
        return await safe(
            "edit_chat_photo",
            lambda: _json(
                media.edit_chat_photo(rt.client, rt.allowed_roots, chat_id, file_path)
            ),
        )
