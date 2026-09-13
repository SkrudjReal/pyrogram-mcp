from __future__ import annotations

from typing import Any

from core.telegram.file_policy import readable, writable
from core.telegram.resolve import chat_id


async def _message(client: Any, target: int | str, message_id: int) -> Any:
    return await client.get_messages(chat_id(target), message_id)


async def get_media_info(
    client: Any, target: int | str, message_id: int
) -> dict[str, Any]:
    message = await _message(client, target, message_id)
    if message is None:
        raise ValueError("Message not found")
    media = getattr(message, "media", None)
    if media is None:
        return {
            "chat_id": chat_id(target),
            "message_id": message_id,
            "has_media": False,
        }
    result = {"chat_id": chat_id(target), "message_id": message_id, "has_media": True}
    for name in (
        "photo",
        "video",
        "document",
        "audio",
        "voice",
        "sticker",
        "animation",
    ):
        value = getattr(message, name, None)
        if value is not None:
            result["media_type"] = name
            result["media"] = value
            break
    return result


async def send_file(
    client: Any,
    allowed_roots: tuple[Any, ...],
    target: int | str,
    file_path: str,
    caption: str | None = None,
) -> Any:
    path = readable(file_path, allowed_roots)
    return await client.send_document(
        chat_id(target), document=str(path), caption=caption
    )


async def download_media(
    client: Any,
    allowed_roots: tuple[Any, ...],
    target: int | str,
    message_id: int,
    file_path: str | None = None,
) -> str:
    message = await _message(client, target, message_id)
    if message is None:
        raise ValueError("Message not found")
    path = writable(file_path, allowed_roots)
    result = await client.download_media(message, file_name=str(path))
    if result is None:
        raise RuntimeError("Kurigram did not return a downloaded file")
    return str(result)


async def upload_file(
    client: Any, allowed_roots: tuple[Any, ...], file_path: str
) -> Any:
    path = readable(file_path, allowed_roots)
    return await client.save_file(str(path))


async def send_voice(
    client: Any,
    allowed_roots: tuple[Any, ...],
    target: int | str,
    file_path: str,
    caption: str | None = None,
) -> Any:
    path = readable(file_path, allowed_roots)
    if path.suffix.lower() not in {".ogg", ".opus"}:
        raise ValueError("send_voice accepts only .ogg and .opus")
    return await client.send_voice(chat_id(target), voice=str(path), caption=caption)


async def send_sticker(
    client: Any,
    allowed_roots: tuple[Any, ...],
    target: int | str,
    file_path: str,
) -> Any:
    path = readable(file_path, allowed_roots)
    if path.suffix.lower() not in {".webp", ".tgs"}:
        raise ValueError("send_sticker accepts only .webp and .tgs")
    return await client.send_sticker(chat_id(target), sticker=str(path))


async def set_profile_photo(
    client: Any, allowed_roots: tuple[Any, ...], file_path: str
) -> Any:
    path = readable(file_path, allowed_roots)
    return await client.set_profile_photo(photo=str(path))


async def edit_chat_photo(
    client: Any, allowed_roots: tuple[Any, ...], target: int | str, file_path: str
) -> Any:
    path = readable(file_path, allowed_roots)
    return await client.set_chat_photo(chat_id(target), photo=str(path))
