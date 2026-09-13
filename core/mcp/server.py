from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "pyrogram-mcp",
    instructions=(
        "Telegram userbot tools backed by one Kurigram client. Use high-level tools "
        "for common operations; use raw_search and raw_describe before raw_call."
    ),
)


def _register_tools() -> None:
    from .tools import client, core, entities, media, raw

    core.register(mcp)
    raw.register(mcp)
    client.register(mcp)
    media.register(mcp)
    entities.register(mcp)


_register_tools()


def configure_mcp(host: str, port: int) -> None:
    mcp.settings.host = host
    mcp.settings.port = port


async def run_mcp(transport: str) -> None:
    if transport == "streamable-http":
        await mcp.run_streamable_http_async()
    elif transport == "sse":
        await mcp.run_sse_async()
    else:
        await mcp.run_stdio_async()
