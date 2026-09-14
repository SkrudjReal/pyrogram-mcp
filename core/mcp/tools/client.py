from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

from core.mcp.errors import safe
from core.runtime import get_runtime
from core.telegram.client_api import call_client, describe_client, search_client
from core.telegram.serialization import to_jsonable


def register(mcp: FastMCP) -> None:
    @mcp.tool(
        title="Search Kurigram client methods",
        annotations=ToolAnnotations(readOnlyHint=True, openWorldHint=False),
        structured_output=True,
    )
    async def client_search(
        query: str = "", limit: int = 50, offset: int = 0
    ) -> dict[str, Any]:
        """Find available high-level async Kurigram Client methods."""
        return await safe(
            "client_search",
            lambda: _search(get_runtime().client, query, limit, offset),
        )

    @mcp.tool(
        title="Describe Kurigram client method",
        annotations=ToolAnnotations(readOnlyHint=True, openWorldHint=False),
        structured_output=True,
    )
    async def client_describe(method: str) -> dict[str, Any]:
        """Return the signature and documentation of a high-level Client method."""
        return await safe(
            "client_describe", lambda: _describe(get_runtime().client, method)
        )

    @mcp.tool(
        title="Call Kurigram client method",
        annotations=ToolAnnotations(destructiveHint=True, openWorldHint=True),
        structured_output=True,
    )
    async def client_call(
        method: str, params: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Call an available high-level async Kurigram method after client_describe.

        Lifecycle and authentication methods are excluded. Prefer named tools for common
        operations; params must match the described signature.
        Async generators return at most 100 items, even with limit=0; this is
        a page, not a complete export. Continue using the method's cursor.
        """
        return await safe(
            "client_call",
            lambda: _call(get_runtime().client, method, params),
        )


async def _search(client: Any, query: str, limit: int, offset: int) -> dict[str, Any]:
    return {"results": search_client(client, query, limit, offset)}


async def _describe(client: Any, method: str) -> dict[str, Any]:
    return describe_client(client, method)


async def _call(client: Any, method: str, params: dict[str, Any] | None) -> Any:
    return to_jsonable(await call_client(client, method, params))
