from apscheduler.schedulers.asyncio import AsyncIOScheduler
from asyncmy.cursors import DictCursor
from asyncmy.pool import Pool
from pyrogram import Client


async def scheduler_tasks(pool: Pool | None, app: Client, scheduler: AsyncIOScheduler):
    # Example

    # Scheduler tasks
    # scheduler.add_job(job, 'cron', hour=22, args=(pool,bot,))

    # Loop tasks
    # asyncio.create_task(loop_task.repeat_initialize_data(pool, app_scam_db_helper))
    ...


async def example_task(pool: Pool):
    """
    Example task for scheduler, asyncio.create_task.
    """
    sql = "SELECT * FROM data_table;"
    sql1 = "UPDATE data_table SET status=1;"

    async with pool.acquire() as conn, conn.cursor(DictCursor) as cur:
        await cur.execute(sql)
        await cur.fetchall()
        await cur.execute(sql1)
