from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger("pyrogram_mcp")


def error_result(operation: str, error: Exception) -> dict[str, Any]:
    name = type(error).__name__
    code = name.upper()
    result: dict[str, Any] = {
        "ok": False,
        "error": {
            "code": code,
            "type": name,
            "message": str(error),
            "operation": operation,
        },
    }
    retry_after = getattr(error, "value", None)
    if isinstance(retry_after, int):
        result["error"]["retry_after"] = retry_after
    logger.warning("Telegram tool failed: %s (%s)", operation, code)
    return result


async def safe(operation: str, action: Any) -> dict[str, Any]:
    try:
        return {"ok": True, "data": await action()}
    except Exception as error:  # noqa: BLE001 - tool boundary must return structured errors
        return error_result(operation, error)
