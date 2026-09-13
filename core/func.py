from pyrogram.types import User


def full_name_getter(user: User) -> str:
    """Returns full name of user"""
    if user.last_name:
        return f"{user.first_name} {user.last_name}"
    return user.first_name
