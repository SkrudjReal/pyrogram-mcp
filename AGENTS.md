# pyrogram-mcp agent instructions

## Project goal

`pyrogram-mcp` is a Telegram userbot and MCP server built on Kurigram and
dispyro. Telegram updates, MCP tools and the Codex bridge share one Kurigram
client and one asyncio runtime.

Read `IMPLEMENTATION_PLAN.md` before changing architecture or adding a new
MCP surface. Keep the plan and README current when behavior changes.

## Architecture boundaries

- `app.py` owns startup, shutdown, the shared runtime and background tasks.
- `core/runtime.py` is the shared client/dispatcher/database container.
- `core/handlers/` contains dispyro Telegram update handlers only.
- `core/mcp/` contains MCP registration and thin tool adapters.
- `core/service/` contains Telegram business operations without MCP protocol
  code.
- `core/telegram/` contains peer resolution, raw API discovery and
  JSON-compatible serialization.
- `core/utils/db_api/` contains MySQL repositories; Redis is for hot cache,
  snapshots and deduplication.

Do not duplicate Telegram business logic in MCP tools or handlers. Use the
installed Kurigram APIs and inspect the installed package before guessing a
signature. Keep raw API access dynamic through discovery instead of copying
the generated Kurigram raw classes into this project.

## MCP and Telegram rules

- Preserve the single active Kurigram session. Never start a second Telegram
  polling/client process against the same session file.
- Keep `MCP_TRANSPORT=streamable-http` for the Codex bridge and local MCP URL
  `http://127.0.0.1:8000/mcp` unless configuration explicitly changes it.
- All Telegram commands must remain owner-only with `filters.me`.
- The Codex Telegram commands are `ам`, `.модель`, `.мышление`,
  `/reasoning`, `.скорость` and `пинг`.
- `ам` is a direct request to Codex. It must not forward the literal prompt
  through Telegram unless the user explicitly asks for a Telegram action.
- The Codex bridge uses one long-lived `codex app-server` process, one durable
  thread and `core/data/codex_thread.json`. Its `CODEX_HOME` must remain
  project-specific so native rollouts are isolated from VS Code; reuse an
  existing login through a symlink rather than copying credentials. Do not
  replace it with a new `codex exec` process per message.
- Codex approval handling is automatic review in a workspace-write sandbox;
  do not silently change it to an unrestricted policy.

## Command reference

- `COMMANDS.md` is the canonical user-facing Telegram command reference.
- If the owner asks to show commands, the command list or help, read
  `COMMANDS.md` and send the current file content or the relevant section.
  Do not reconstruct the command list from memory or invent undocumented
  commands.
- Keep `COMMANDS.md` updated whenever a Telegram command or its arguments
  change.

## Safety and data handling

- Never log, print or commit API credentials, session files or auth tokens.
- Validate chat IDs, raw method names, serialized values, media roots and file
  sizes at trust boundaries.
- Do not retry Telegram writes after an ambiguous network timeout.
- Preserve the pre-delete snapshot path for deleted-message archiving.
- Do not run PM2, Docker and another polling instance simultaneously.

## Development workflow

Before handing off a code change, run:

```bash
ruff check .
python3 -m compileall -q .
```

For MCP changes, also inspect the registered tool count and run the smallest
focused behavior check available. For lifecycle changes, verify startup,
graceful shutdown, the MCP HTTP endpoint and the absence of duplicate
Telegram/Codex processes. Stop locally started `app.py` after verification
unless the user explicitly asks to keep it running.
