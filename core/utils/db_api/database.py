from asyncmy import create_pool
from asyncmy.pool import Pool

from core.settings import Settings


async def create_mysql_pool(settings: Settings) -> Pool | None:
    """
    Create a connection pool to the MySQL database.
    """
    if not settings.db.enabled:
        return None
    return await create_pool(
        host=settings.db.ip,
        port=3306,
        user=settings.db.user,
        password=settings.db.password,
        db=settings.db.db,
        autocommit=True,
    )


async def db_setup(pool: Pool | None):
    if pool is None:
        return

    # users_table = (
    #     'CREATE TABLE IF NOT EXISTS Users ('
    #     ' user_id BIGINT(16) NOT NULL PRIMARY KEY,'
    #     ' full_name VARCHAR(128) NOT NULL,'
    #     ' username VARCHAR(32) DEFAULT NULL'
    #     ');'
    # )

    # tasks = [
    #     users_table,
    # ]

    # async with pool.acquire() as conn:
    #     async with conn.cursor() as cur:
    #         for ex in tasks:
    #             await cur.execute(ex)
