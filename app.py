import asyncio
import os
from typing import Any

import uvloop
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from asyncmy.pool import Pool
from dispyro import Dispatcher
from dispyro.enums import RunLogic
from pyrogram import Client, enums, idle
from redis.asyncio import Redis

from core.func import full_name_getter

# local imports
from core.handlers import setup_handlers
from core.mcp.server import configure_mcp, run_mcp
from core.runtime import Runtime, clear_runtime, set_runtime
from core.service.loop_task import scheduler_tasks
from core.service.codex import configure as configure_codex
from core.service.codex import start as start_codex
from core.service.codex import stop as stop_codex
from core.settings import Settings, get_settings, logger
from core.utils.db_api.database import create_mysql_pool, db_setup
from core.utils.db_api.repo import RequestsRepo


async def on_startup(app: Client):
    me = await app.get_me()
    logger.info(f"App {full_name_getter(me)} [{me.id}] - PID {os.getpid()} запущено.")


async def start_client(
    settings: Settings,
    pool: Pool | None,
    redis: Redis | None,
    ses_name: str | None = None,
) -> tuple[Client, Dispatcher, Any]:
    session_name = ses_name or settings.paths.session_name
    session_path = settings.paths.project_root / "core" / "sessions" / session_name
    app = Client(
        str(session_path),
        settings.app.api_id,
        settings.app.api_hash,
        phone_number=settings.app.phone_number,
        parse_mode=enums.ParseMode.HTML,
    )
    await app.start()
    repo = RequestsRepo()
    me = await app.get_me()
    dp = Dispatcher(
        app, me=me, repo=repo, pool=pool, redis=redis, run_logic=RunLogic.UNLIMITED
    )
    return app, dp, me


async def close_runtime(runtime: Runtime, scheduler: AsyncIOScheduler | None) -> None:
    if scheduler and scheduler.running:
        scheduler.shutdown(wait=False)
    if runtime.client.is_connected:
        await runtime.client.stop()
    if runtime.redis:
        await runtime.redis.aclose()
    if runtime.pool:
        runtime.pool.close()
        await runtime.pool.wait_closed()
    clear_runtime()


async def main():
    settings = get_settings()
    configure_codex(settings)
    redis = (
        Redis(host=settings.redis.ip, port=6379, decode_responses=True)
        if settings.redis.enabled
        else None
    )
    scheduler = AsyncIOScheduler()
    pool = None
    app = None
    mcp_task = None
    runtime = None
    codex_started = False
    try:
        pool = await create_mysql_pool(settings)
        app, dp, me = await start_client(settings, pool, redis)
        await db_setup(pool)
        if pool:
            await scheduler_tasks(pool, app, scheduler)
        await setup_handlers({"app": app, "dp": dp})
        runtime = Runtime(
            client=app,
            dispatcher=dp,
            me=me,
            redis=redis,
            pool=pool,
            repo=RequestsRepo(),
            allowed_roots=settings.paths.media_roots,
        )
        set_runtime(runtime)
        configure_mcp(settings.mcp.host, settings.mcp.port)
        mcp_task = asyncio.create_task(run_mcp(settings.mcp.transport))
        await start_codex()
        codex_started = True
        await on_startup(app)
        scheduler.start()
        await idle()
    finally:
        if codex_started:
            await stop_codex()
        if mcp_task:
            mcp_task.cancel()
            await asyncio.gather(mcp_task, return_exceptions=True)
        if runtime:
            await close_runtime(runtime, scheduler)
        else:
            if app and app.is_connected:
                await app.stop()
            if redis:
                await redis.aclose()
            if pool:
                pool.close()
                await pool.wait_closed()


if __name__ == "__main__":
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    asyncio.run(main())
