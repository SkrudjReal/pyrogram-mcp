from dataclasses import dataclass

from asyncmy.cursors import DictCursor


@dataclass
class RequestsRepo:
    cur: DictCursor = None

    ### SQL Simple Queries ###

    async def select_all(
        self,
        cur: DictCursor,
        sql: str,
        params: tuple | None = None,
        use_index_zero: bool = True,
    ):
        await cur.execute(sql, params)
        result = await cur.fetchall()
        if result:
            return result[0] if use_index_zero else result
        else:
            return None

    async def select_one(self, cur: DictCursor, sql: str, params: tuple | None = None):
        await cur.execute(sql, params)
        result = await cur.fetchone()
        return next(iter(result.values())) if result else None

    ### Main Elements ###

    async def get_user_example_(self, cur: DictCursor, link: int | str):
        return await self.select_all(
            cur, "SELECT * FROM Users WHERE user_id=%s OR username=%s;", (link, link)
        )

    ### Add main elements ###

    async def add_data_user_example_(
        self, cur: DictCursor, user_id: int, full_name: str, username: str | None = None
    ):
        query = "UPDATE Users SET username=NULL WHERE user_id!=%s AND username=%s;"
        query1 = (
            "INSERT INTO Users (user_id, full_name, username) VALUES (%s, %s, %s) "
            "ON DUPLICATE KEY UPDATE"
            " full_name=%s,"
            " username=%s;"
        )
        await cur.execute(query, (user_id, username))
        params = (user_id, full_name, username, full_name, username)
        await cur.execute(query1, params)
