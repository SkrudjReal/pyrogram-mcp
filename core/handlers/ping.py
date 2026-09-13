import time

from asyncmy.pool import Pool
from pyrogram import Client
from pyrogram.types import Message, User
from redis.asyncio import Redis

from core.data.tricks import tricks
from core.utils.db_api.repo import RequestsRepo


async def ping(
    app: Client, msg: Message, me: User, pool: Pool, repo: RequestsRepo, redis: Redis
):

    result_ping = ""

    time_start = time.perf_counter_ns()
    mesg = await msg.reply(tricks["ping"]["ping"])
    result_ping += str(round((time.perf_counter_ns() - time_start) / 10**6, 3))
    await mesg.edit_text(tricks["ping"]["ping_speed"].format(result_ping))
    await msg.delete()
