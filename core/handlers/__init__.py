import re

from dispyro import Dispatcher
from pyrogram import Client, filters

from .codex import ask_codex, model_command, reasoning_command, speed_command
from .ping import ping
from .watcher import archive_deleted_messages, archive_edited_message, archive_message


COMMAND_FLAGS = re.IGNORECASE


async def setup_handlers(apps_dp: dict[str, tuple[Client, Dispatcher]]):
    # register handlers
    dp = apps_dp["dp"]
    dp.message.register(
        ping,
        filters=filters.me & filters.regex(r"^пинг$", flags=COMMAND_FLAGS),
    )
    dp.message.register(
        model_command,
        filters=filters.me
        & filters.regex(r"^\.модель(?:\s+\S+)?$", flags=COMMAND_FLAGS),
    )
    dp.message.register(
        reasoning_command,
        filters=filters.me
        & filters.regex(
            r"^(?:/reasoning(?:@\w+)?|\.мышление)$", flags=COMMAND_FLAGS
        ),
    )
    dp.message.register(
        speed_command,
        filters=filters.me
        & filters.regex(r"^\.скорость(?:\s+\S+)?$", flags=COMMAND_FLAGS),
    )
    dp.message.register(
        ask_codex,
        filters=filters.me
        & filters.regex(r"^ам(?:\s+.+)?$", flags=COMMAND_FLAGS),
    )
    dp.message.register(archive_message)
    dp.edited_message.register(archive_edited_message)
    dp.deleted_messages.register(archive_deleted_messages)
