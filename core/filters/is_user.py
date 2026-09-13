from pyrogram import filters


async def func(_, __, msg):
    return msg.from_user is not None


is_user = filters.create(func)
