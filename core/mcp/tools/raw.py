from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

from core.mcp.errors import safe
from core.runtime import get_runtime
from core.telegram.raw_api import describe_raw, invoke_raw, search_raw
from core.telegram.serialization import to_jsonable


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        title="Search Kurigram raw API",
        annotations=ToolAnnotations(readOnlyHint=True, openWorldHint=False),
        structured_output=True,
    )
    async def raw_search(
        query: str = "", namespace: str = "functions", limit: int = 50, offset: int = 0
    ) -> dict[str, Any]:
        """Find Kurigram raw functions or constructible raw types by name."""
        return await safe(
            "raw_search", lambda: _raw_search(query, namespace, limit, offset)
        )

    @mcp.tool(
        title="Describe Kurigram raw object",
        annotations=ToolAnnotations(readOnlyHint=True, openWorldHint=False),
        structured_output=True,
    )
    async def raw_describe(method: str, namespace: str = "functions") -> dict[str, Any]:
        """Return the canonical raw path, TL id and constructor parameters."""
        return await safe("raw_describe", lambda: _raw_describe(method, namespace))

    @mcp.tool(
        title="Invoke Kurigram raw function",
        annotations=ToolAnnotations(
            destructiveHint=True, idempotentHint=False, openWorldHint=True
        ),
        structured_output=True,
    )
    async def raw_call(
        method: str, params: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Invoke any installed pyrogram.raw.functions class through Kurigram.

        Use raw_search/raw_describe first. TL objects use {"_": "types.Type", ...};
        resolve a chat peer with {"_": "__resolve_peer__", "value": "@name"}.
        """
        runtime = get_runtime()
        return await safe("raw_call", lambda: _raw_call(runtime.client, method, params))


async def _raw_search(
    query: str, namespace: str, limit: int, offset: int
) -> dict[str, Any]:
    return {
        "namespace": namespace,
        "results": search_raw(query, namespace, limit, offset),
    }


async def _raw_describe(method: str, namespace: str) -> dict[str, Any]:
    return describe_raw(method, namespace)


async def _raw_call(
    client: Any, method: str, params: dict[str, Any] | None
) -> dict[str, Any]:
    result = await invoke_raw(client, method, params)
    return {"method": method, "result": to_jsonable(result)}
