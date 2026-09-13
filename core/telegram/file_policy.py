from __future__ import annotations

from pathlib import Path


class FilePolicyError(ValueError): ...


_FORBIDDEN_PARTS = {"..", "~"}
_MAX_FILE_BYTES = 200 * 1024 * 1024


def _roots(allowed_roots: tuple[Path, ...]) -> tuple[Path, ...]:
    if not allowed_roots:
        raise FilePolicyError("File tools are disabled; configure MEDIA_ROOTS first")
    return tuple(root.resolve() for root in allowed_roots)


def _candidate(
    raw_path: str | None, allowed_roots: tuple[Path, ...], *, default_dir: bool
) -> Path:
    roots = _roots(allowed_roots)
    if raw_path is None or not raw_path.strip():
        if not default_dir:
            raise FilePolicyError("file_path is required")
        return roots[0] / "downloads"
    value = raw_path.strip()
    path = Path(value)
    if any(part in _FORBIDDEN_PARTS for part in path.parts) or any(
        token in value for token in ("*", "?", "[", "]", "{", "}")
    ):
        raise FilePolicyError("Path contains a forbidden traversal or wildcard")
    return path if path.is_absolute() else roots[0] / path


def _inside(path: Path, roots: tuple[Path, ...]) -> bool:
    return any(path == root or root in path.parents for root in roots)


def readable(raw_path: str, allowed_roots: tuple[Path, ...]) -> Path:
    roots = _roots(allowed_roots)
    path = _candidate(raw_path, roots, default_dir=False).resolve(strict=True)
    if not _inside(path, roots) or not path.is_file():
        raise FilePolicyError("Path must be a readable file inside MEDIA_ROOTS")
    if path.stat().st_size > _MAX_FILE_BYTES:
        raise FilePolicyError(f"File exceeds {_MAX_FILE_BYTES} byte limit")
    return path


def writable(raw_path: str | None, allowed_roots: tuple[Path, ...]) -> Path:
    roots = _roots(allowed_roots)
    path = _candidate(raw_path, roots, default_dir=True)
    path = path.resolve()
    if not _inside(path, roots):
        raise FilePolicyError("Path must stay inside MEDIA_ROOTS")
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
