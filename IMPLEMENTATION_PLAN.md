# pyrogram-mcp: архитектурный план и статус реализации

## Цель

Перенести функциональность `telegram-mcp` с Telethon на Kurigram, сохранив
доступ агента к Telegram через MCP и используя существующий dispyro runtime.
MCP и Telegram handlers работают в одном процессе и используют один
подключённый Kurigram `Client`.

Источники:

- исходный `telegram-mcp` — список пользовательских возможностей и исходный
  MCP-контракт.
- [Kurigram](https://github.com/kurigram-org/kurigram) — high-level API и
  генерируемые `pyrogram.raw.functions`, `pyrogram.raw.types`.

## Архитектура

```text
MCP client / agent
        |
        v
core/mcp/tools       понятные typed tools + raw gateway
        |
        v
core/service         операции Telegram, валидация, пагинация, ошибки
        |
        v
core/telegram        resolve, serialization, raw catalog
        |
        v
Kurigram Client <---- dispyro Dispatcher <---- Telegram updates
        |
        +---- Redis: быстрый кеш и snapshots удаляемых сообщений
        +---- MySQL: долговременные данные и события
```

### Границы модулей

- `app.py` — lifecycle процесса, общий runtime, режим MCP и graceful shutdown.
- `core/runtime.py` — типизированный контейнер `Client`, `Dispatcher`, Redis,
  MySQL и `me`.
- `core/mcp/server.py` — FastMCP server и transport.
- `core/mcp/registry.py` — явная регистрация tool-модулей.
- `core/mcp/tools/` — MCP-схемы и короткие адаптеры к сервисам.
- `core/service/` — бизнес-операции без зависимости от MCP protocol.
- `core/telegram/resolve.py` — numeric ID, username, invite и peer resolution.
- `core/telegram/serialization.py` — безопасное преобразование Kurigram
  objects в JSON-compatible данные.
- `core/telegram/raw_api.py` — динамический каталог всего установленного
  `pyrogram.raw.functions` и `pyrogram.raw.types`.
- `core/handlers/` — dispyro updates; watcher сохраняет snapshots до удаления.
- `core/utils/db_api/` — MySQL repositories; Redis используется для горячего
  кеша и deduplication.

Инструменты не содержат Telegram-бизнес-логику. Raw-классы не копируются в
проект: каталог строится из фактически установленного Kurigram, поэтому после
обновления Kurigram доступны новые raw API без ручного переписывания MCP.

## MCP-контракт

На установленном для проверки Kurigram `2.2.26` каталог содержит 837 raw
функций, 1719 constructible raw types и 374 high-level async Client methods;
MCP публикует 46 named/discovery tools. Эти числа могут меняться вместе с
версией Kurigram, каталог строится динамически при запуске.

### Понятные high-level tools

Первая группа должна покрыть ежедневные сценарии агента:

- `get_me`, `list_chats`, `get_chat`, `get_messages`, `get_message_context`;
- `search_messages`, `search_global`, `resolve_username`;
- `send_message`, `reply_to_message`, `edit_message`, `delete_message`;
- `forward_messages`, `copy_messages`, `mark_as_read`;
- `send_file`, `download_media`, `get_media_info`;
- `list_contacts`, `search_contacts`, `add_contact`, `block_user`;
- `get_participants`, `get_admins`, `ban_user`, `unban_user`;
- `list_topics`, `create_forum_topic`, реакции, inline-кнопки и polls.

### Полный raw API

Все raw-функции доступны через компактный discovery/call контракт:

- `raw_search(query, namespace="functions", limit=50)` — ищет функции и
  типы в реально установленном Kurigram.
- `raw_describe(method)` — возвращает canonical path, TL ID, сигнатуру,
  required/optional параметры и return type.
- `raw_call(method, params)` — создаёт raw TL function и вызывает
  `await client.invoke(...)`.

Canonical examples:

```text
functions.messages.GetHistory
functions.channels.ToggleForum
types.InputPeerChannel
```

Для TL-параметров используются JSON-объекты с `_`:

```json
{
  "peer": {"_": "types.InputPeerSelf"},
  "limit": 50
}
```

Для адресатов с username/ID используется явный маркер:

```json
{"_": "__resolve_peer__", "value": "@channel"}
```

Бинарные значения передаются как `{"_": "__bytes__", "base64": "..."}`.
Ответы сериализуются рекурсивно с сохранением `_`, TL-полей и base64 для bytes.

Сотни raw-функций не регистрируются отдельными MCP tools: это увеличивает
описание tool-сервера и замедляет выбор инструмента агентом. Discovery перед
`raw_call` сохраняет полный охват API и короткий список MCP tools.

## Lifecycle и transport

1. Загрузить настройки по абсолютному пути проекта.
2. Открыть Redis/MySQL только если они включены конфигурацией.
3. Запустить один Kurigram client и прогреть peer cache через dialogs.
4. Создать dispyro Dispatcher, зарегистрировать handlers и MCP registry.
5. Запустить `stdio` для локального агента или `streamable-http` для общего
   процесса под PM2.
6. На остановке отменить MCP/background tasks, остановить scheduler,
   dispatcher/client и закрыть pools.

Codex bridge uses a dedicated `CODEX_HOME` for this project. Its native
rollouts, config and thread history are separate from the user's VS Code
Codex home, while an existing `~/.codex/auth.json` may be reused through a
symlink so the project does not duplicate credentials. The application still
keeps one long-lived app-server process and one durable thread id in
`core/data/codex_thread.json`.

`stdio` остаётся режимом по умолчанию для совместимости с MCP-клиентами.
`MCP_TRANSPORT=streamable-http` нужен для долгоживущего процесса, к которому
подключаются несколько агентов. Один session-файл не открывается несколькими
процессами.

## Безопасность и надёжность

- raw-вызов разрешает только классы, найденные внутри
  `pyrogram.raw.functions`/`pyrogram.raw.types`; произвольный import запрещён.
- Имена методов нормализуются и проверяются по каталогу.
- Ограничить размер MCP-входа и ответа, глубину рекурсивной сериализации и
  размер файлов.
- Путь медиа должен находиться в разрешённых roots; запретить traversal и
  wildcard-пути.
- Ошибки возвращаются с кодом, типом, сообщением и `retry_after` для
  `FloodWait`.
- Изменяющие инструменты имеют destructive/idempotent annotations.
- Отправка после сетевого timeout не повторяется автоматически: Telegram мог
  принять первый запрос.
- Перед удалением сохраняется сообщение в Redis/MySQL; delete update содержит
  только идентификаторы.
- Не запускать PM2, Docker и systemd polling одновременно: Telegram
  `getUpdates` конфликтует.

## Этапы

### Этап 1 — вертикальный MCP slice

- [x] Зафиксировать архитектурный план.
- [x] Общий runtime и graceful shutdown.
- [x] `stdio`/`streamable-http` transport.
- [x] `get_me`, `list_chats`, `get_chat`, `get_messages`.
- [x] raw catalog, `raw_search`, `raw_describe`, `raw_call`.
- [x] `client_search`, `client_describe`, `client_call` для полного async
  high-level surface Kurigram.

### Этап 2 — сообщения и поиск

- [x] send/reply/edit/delete.
- [x] forward/copy и mark as read.
- [x] ограниченная pagination и `get_message_context`/`get_chat_context`.
- [x] единый structured error mapper.

### Этап 3 — media и Telegram entities

- [x] download/upload/send media с server-side roots и лимитами.
- [x] contacts, profile, chats, groups и forum topics.
- [ ] moderation extensions, reactions, buttons, polls, stickers/GIF через
  отдельные named tools; временно доступны через `client_call`/raw.

### Этап 4 — watcher/context

- [x] dispyro handlers для message, edited message, deleted messages и media.
- [x] Redis snapshots до удаления с TTL.
- [ ] MySQL persistence для долговременного archive/context индекса.

### Этап 5 — проверка эксплуатации

- [x] import/compile, Ruff и MCP schema inspection.
- [x] runnable checks raw path resolution, decode/encode, archive и file guard.
- [ ] MCP Inspector/реальный MCP client.
- [ ] реальное чтение и безопасный тестовый write в Telegram.
- [ ] restart, FloodWait, cancellation, session lock, PM2 logs.

## Критерий готовности

Агент видит короткий каталог high-level tools, умеет найти любую raw-функцию
через discovery, вызвать её через Kurigram с typed TL-параметрами и получить
JSON-compatible результат. Все операции используют единый client и проходят
через общий error/path policy.
