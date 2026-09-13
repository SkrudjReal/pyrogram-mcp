<div align="center">

# ⚡ pyrogram-mcp

**High-Performance Telegram Userbot & Model Context Protocol (MCP) Server**  
*Built with [Kurigram], [dispyro], and [FastMCP] with an integrated, persistent OpenAI Codex App-Server Bridge.*

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![MCP Specification](https://img.shields.io/badge/MCP-Protocol-blueviolet.svg?style=flat)](https://modelcontextprotocol.io/)
[![FastMCP](https://img.shields.io/badge/FastMCP-Server-0052CC.svg?style=flat)](https://gofastmcp.com/)
[![Poetry](https://img.shields.io/badge/packaging-Poetry-blue.svg?style=flat&logo=poetry&logoColor=white)](https://python-poetry.org/)
[![Dispyro](https://img.shields.io/badge/dispatcher-dispyro-orange.svg?style=flat)](https://pypi.org/project/dispyro/)
[![Kurigram](https://img.shields.io/badge/MTProto-Kurigram-26A5E4.svg?style=flat&logo=telegram&logoColor=white)](https://github.com/kurigram-org/kurigram)

---

</div>

`pyrogram-mcp` bridges native Telegram operations directly into LLM agent workflows (such as OpenAI Codex, Claude Code, and Cursor) via the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/). It runs as both an interactive Telegram userbot and an MCP server over a **single shared Kurigram session**, cleanly separating Telegram update dispatching, core business operations, and MCP tool adapters into isolated layers.

---

## 🌟 Key Highlights

- 🔄 **Unified Single Session**: Shares one active MTProto session and `asyncio` event loop across userbot handlers, background workers, and MCP tool executions — eliminating session lockouts and duplicate polling.
- 🛠️ **Dual-Layer MCP Tooling**:
  - **High-Level Tools**: Clean abstractions for managing chats, reading message history, sending media, search, contacts, and moderation.
  - **Dynamic Reflection**: Runtime introspection into installed Kurigram MTProto methods (`raw_search`, `raw_describe`, `raw_call`) and high-level client methods (`client_search`, `client_describe`, `client_call`).
- 🤖 **Persistent Codex App-Server Bridge**: Issue commands directly inside Telegram using `ам <запрос>` to trigger a long-running, stateful OpenAI Codex session powered by `gpt-5.6-luna`.
- 🌐 **Flexible MCP Transports**: Supports **Streamable HTTP** (`http://127.0.0.1:8000/mcp`) for long-lived daemon connections and **stdio** for direct process execution.
- 🛡️ **Owner-Only Security**: All Telegram commands enforce strict `filters.me` checks; MCP filesystem access is sandboxed via configurable `MEDIA_ROOTS`.

---

## 🏗️ Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                    MCP Clients / Codex                      │
└──────────────────────────────┬──────────────────────────────┘
                               │ (HTTP / stdio)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│    core/mcp/tools          FastMCP Schemas & Adapters       │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│    core/service            Telegram Operations & Policy     │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│    core/telegram           Peer Resolution & Raw MTProto    │
└──────────────┬───────────────────────────────┬──────────────┘
               │                               │
               ▼                               ▼
┌─────────────────────────────┐ ┌─────────────────────────────┐
│       Kurigram Client       │ │     dispyro Dispatcher      │
│   (Shared MTProto Engine)   │ │  (Telegram Update Handlers) │
└─────────────────────────────┘ └─────────────────────────────┘
```

Detailed architectural diagrams and implementation notes are available in [`IMPLEMENTATION_PLAN.md`](IMPLEMENTATION_PLAN.md).  
Userbot command behavior and conventions are specified in [`COMMANDS.md`](COMMANDS.md).

---

## 📋 Requirements

| Requirement | Minimum Version | Notes |
| :--- | :--- | :--- |
| **Python** | `3.12+` | Modern `asyncio` runtime required |
| **Telegram API** | — | `API_ID` & `API_HASH` from [my.telegram.org](https://my.telegram.org) |
| **Poetry** | Latest | Dependency management & environment isolation |
| **Codex CLI** | `0.154+` | Required for Codex bridge (`gpt-5.6-luna`) |
| **MySQL / Redis** | Optional | Only needed if persistence / caching is enabled |

---

## 🚀 Quickstart

### 1. Clone & Install

```bash
git clone <repository-url>
cd pyrogram-mcp
poetry install --no-root
```

### 2. Configure Environment

```bash
cp settings.env.example settings.env
```

Open `settings.env` and supply your Telegram credentials:

```env
API_ID=1234567
API_HASH=your_telegram_api_hash
PHONE_NUMBER=+1234567890

# Minimal standalone configuration (disable optional databases)
MYSQL_ENABLED=false
REDIS_ENABLED=false

# MCP & Codex Bridge
MCP_TRANSPORT=streamable-http
MCP_HOST=127.0.0.1
MCP_PORT=8000
```

### 3. Launch

```bash
poetry run python3 app.py
```

> [!NOTE]
> On first startup, Kurigram may prompt you for Telegram authorization (SMS/Telegram code and optional 2FA password). The session file is saved securely to `core/sessions/` (which is excluded by `.gitignore`).

---

## 🔌 MCP Transport & Configuration

### Streamable HTTP (Recommended)

When Codex or an external MCP client connects to an existing running instance of `pyrogram-mcp`, use Streamable HTTP:

```env
MCP_TRANSPORT=streamable-http
MCP_HOST=127.0.0.1
MCP_PORT=8000
```

- **MCP Endpoint**: `http://127.0.0.1:8000/mcp`
- Required for the interactive Telegram `ам` bridge.

### stdio

When an MCP client manages the server lifecycle directly as a subprocess, configure:

```env
MCP_TRANSPORT=stdio
```

---

## 🧠 OpenAI Codex Bridge

The Codex bridge manages a single, persistent `codex app-server` process with durable conversational threads saved to `core/data/codex_thread.json`.

### Environment & Authentication Isolation

By default, native Codex state is isolated in its own workspace:

```env
CODEX_HOME=~/.local/share/pyrogram-mcp/codex
```

This prevents project rollouts and threads from polluting your main user or VS Code Codex environment.

- **Reusing existing auth**: If `~/.codex/auth.json` is present, the bridge automatically creates a symlink so credentials are not duplicated.
- **Manual login**: If no existing credentials exist:
  ```bash
  CODEX_HOME=~/.local/share/pyrogram-mcp/codex codex login
  ```

### Bridge Tuning

```env
CODEX_BIN=codex
CODEX_MODEL=gpt-5.6-luna
CODEX_REASONING_EFFORT=xhigh
CODEX_SERVICE_TIER=default
CODEX_TIMEOUT=180
```

---

## 💬 Telegram Commands

> [!IMPORTANT]
> All userbot commands are strictly **owner-only** (`filters.me`) and case-insensitive.

| Command | Description | Example |
| :--- | :--- | :--- |
| `пинг` | Verifies userbot responsiveness | `пинг` |
| `.модель` | Lists available Codex models and reasoning levels | `.модель` |
| `.модель <slug>` | Switches active Codex model | `.модель gpt-5.6-sol` |
| `.мышление` / `/reasoning` | Shows current model and active reasoning effort | `.мышление` |
| `.скорость` | Displays current Codex service tier | `.скорость` |
| `.скорость <normal\|fast>` | Switches service tier (`обычно`, `быстро`, `1.5x`) | `.скорость fast` |
| `ам <запрос>` | Sends prompt to persistent Codex agent | `ам Покажи последние 20 сообщений из чата <chat_id>` |

For complete usage guides and command behavior, see [`COMMANDS.md`](COMMANDS.md).

---

## 🔍 Dynamic Kurigram Raw API

`pyrogram-mcp` introspects the installed Kurigram package dynamically at runtime rather than relying on static, hardcoded MTProto classes:

1. **`raw_search`**: Search for MTProto functions and types by pattern.
2. **`raw_describe`**: Inspect method signatures, parameter types, and docstrings.
3. **`raw_call`**: Execute any MTProto function dynamically with JSON arguments.

### Example: Calling Raw MTProto

```json
{
  "peer": {
    "_": "types.InputPeerSelf"
  },
  "limit": 50
}
```

### Peer Resolver Helper

To resolve usernames or channel IDs seamlessly without manual conversion, use the `__resolve_peer__` token:

```json
{
  "_": "__resolve_peer__",
  "value": "@channel_name"
}
```

---

## 🔒 Security & Repository Hygiene

- 🚫 **Do Not Commit Secrets**: Never commit `settings.env`, `.session` files in `core/sessions/`, `auth.json`, or runtime logs.
- 📂 **Sandboxed File Access**: Restrict `MEDIA_ROOTS` strictly to directories intended for MCP file access (e.g. `/tmp/pyrogram-mcp-media`).
- 🔐 **Restricted Command Scope**: Userbot commands are protected with `filters.me`; destructive write actions are clearly annotated in the tool schema.

---

## 🧪 Development & Quality Checks

Run local checks prior to committing changes:

```bash
# Verify syntax and bytecode compilation
poetry run python3 -m compileall -q .

# Verify total registered MCP tools
poetry run python3 -c 'from core.mcp.server import mcp; print(f"Registered MCP tools: {len(mcp._tool_manager._tools)}")'
```

---

## 📄 License

Distributed under the terms appropriate for your deployment. Refer to the repository license or contact the maintainers before redistribution.

[FastMCP]: https://gofastmcp.com/
[Kurigram]: https://github.com/kurigram-org/kurigram
[Poetry]: https://python-poetry.org/
[dispyro]: https://pypi.org/project/dispyro/
