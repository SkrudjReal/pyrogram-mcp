import logging
import os
from dataclasses import dataclass
from pathlib import Path

from environs import Env
from pytz import timezone


@dataclass
class App:
    api_id: int
    api_hash: str
    phone_number: str


@dataclass
class MysqlDB:
    ip: str
    db: str
    password: str
    user: str
    enabled: bool


@dataclass
class RedisDB:
    ip: str
    enabled: bool


@dataclass
class MCP:
    transport: str
    host: str
    port: int


@dataclass
class Codex:
    binary: str
    home: Path
    model: str
    reasoning_effort: str
    service_tier: str
    timeout: int
    mcp_url: str


@dataclass
class Paths:
    project_root: Path
    session_name: str
    media_roots: tuple[Path, ...]


@dataclass
class Settings:
    app: App
    db: MysqlDB
    redis: RedisDB
    mcp: MCP
    codex: Codex
    paths: Paths


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def get_settings(path: str | Path | None = None) -> Settings:
    settings_path = Path(
        path or os.getenv("SETTINGS_PATH", PROJECT_ROOT / "settings.env")
    )
    if not settings_path.exists():
        raise FileNotFoundError(f"Environment file {settings_path} not found.")
    env = Env()
    env.read_env(str(settings_path))
    transport = env.str("MCP_TRANSPORT", default="stdio")
    if transport not in {"stdio", "sse", "streamable-http"}:
        raise ValueError("MCP_TRANSPORT must be stdio, sse or streamable-http")
    service_tier = env.str("CODEX_SERVICE_TIER", default="default").strip().lower()
    if service_tier not in {"default", "priority"}:
        raise ValueError("CODEX_SERVICE_TIER must be default or priority")
    return Settings(
        app=App(
            api_id=env.int("API_ID"),
            api_hash=env.str("API_HASH"),
            phone_number=env.str("PHONE_NUMBER", default=""),
        ),
        db=MysqlDB(
            ip=env.str("MYSQL_IP", default=env.str("ip", default="127.0.0.1")),
            db=env.str("MYSQL_DB", default=env.str("db", default="telegram")),
            user=env.str("MYSQL_USER", default=env.str("user", default="root")),
            password=env.str(
                "MYSQL_PASSWORD", default=env.str("password", default="")
            ),
            enabled=env.bool("MYSQL_ENABLED", default=True),
        ),
        redis=RedisDB(
            ip=env.str("REDIS_IP", default="127.0.0.1"),
            enabled=env.bool("REDIS_ENABLED", default=True),
        ),
        mcp=MCP(
            transport=transport,
            host=env.str("MCP_HOST", default="127.0.0.1"),
            port=env.int("MCP_PORT", default=8000),
        ),
        codex=Codex(
            binary=env.str("CODEX_BIN", default="codex"),
            home=Path(
                env.str(
                    "CODEX_HOME",
                    default="~/.local/share/pyrogram-mcp/codex",
                )
            ).expanduser(),
            model=env.str("CODEX_MODEL", default="gpt-5.6-luna"),
            reasoning_effort=env.str("CODEX_REASONING_EFFORT", default="xhigh"),
            service_tier=service_tier,
            timeout=env.int("CODEX_TIMEOUT", default=0),
            mcp_url=env.str(
                "CODEX_MCP_URL",
                default=(
                    f"http://{env.str('MCP_HOST', default='127.0.0.1')}"
                    f":{env.int('MCP_PORT', default=8000)}/mcp"
                ),
            ),
        ),
        paths=Paths(
            project_root=PROJECT_ROOT,
            session_name=env.str("SESSION_NAME", default="pyrogram_mcp"),
            media_roots=tuple(
                Path(item.strip()).expanduser().resolve()
                for item in env.str("MEDIA_ROOTS", default="").split(",")
                if item.strip()
            ),
        ),
    )


def setup_logger(name: str = "pyrogram", level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logging.getLogger("pyrogram").setLevel(logging.INFO)
    logging.getLogger("asyncmy").setLevel(logging.ERROR)

    if not logger.hasHandlers():
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s | %(name)s: %(message)s"
        )

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger


logger = setup_logger(level=logging.INFO)
moscow_tz = timezone("Europe/Moscow")
