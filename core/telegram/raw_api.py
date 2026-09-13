from __future__ import annotations

import base64
import importlib
import inspect
import pkgutil
from dataclasses import dataclass
from typing import Any

from pyrogram import raw
from pyrogram.raw.core import TLObject


class RawAPIError(ValueError): ...


@dataclass(frozen=True, slots=True)
class RawEntry:
    kind: str
    canonical: str
    module: str
    name: str
    object_id: int | None
    cls: type[TLObject]


class RawCatalog:
    def __init__(self) -> None:
        self._functions: dict[str, RawEntry] | None = None
        self._types: dict[str, RawEntry] | None = None

    @staticmethod
    def _load(package: Any, kind: str) -> dict[str, RawEntry]:
        if not hasattr(package, "__path__"):
            raise RawAPIError(f"Kurigram raw {kind} package is unavailable")

        entries: dict[str, RawEntry] = {}
        for module_info in pkgutil.walk_packages(
            package.__path__, package.__name__ + "."
        ):
            module = importlib.import_module(module_info.name)
            for name, candidate in inspect.getmembers(module, inspect.isclass):
                if candidate.__module__ != module.__name__:
                    continue
                if not issubclass(candidate, TLObject) or candidate is TLObject:
                    continue
                qualname = getattr(candidate, "QUALNAME", "")
                if not qualname.startswith(f"{kind}."):
                    continue
                entry = RawEntry(
                    kind=kind,
                    canonical=qualname,
                    module=module.__name__,
                    name=name,
                    object_id=getattr(candidate, "ID", None),
                    cls=candidate,
                )
                for alias in (qualname, qualname.removeprefix(f"{kind}."), name):
                    entries.setdefault(alias.casefold(), entry)
                entries.setdefault(
                    module.__name__.removeprefix("pyrogram.raw.").casefold(), entry
                )
        return entries

    @property
    def functions(self) -> dict[str, RawEntry]:
        if self._functions is None:
            self._functions = self._load(raw.functions, "functions")
        return self._functions

    @property
    def types(self) -> dict[str, RawEntry]:
        if self._types is None:
            self._types = self._load(raw.types, "types")
        return self._types

    def resolve(self, method: str, *, kind: str = "functions") -> RawEntry:
        clean = method.strip().removeprefix("pyrogram.raw.").casefold()
        if kind not in {"functions", "types"}:
            raise RawAPIError("raw namespace must be functions or types")
        entries = self.functions if kind == "functions" else self.types
        entry = entries.get(clean)
        if entry is None:
            raise RawAPIError(f"Unknown raw {kind}: {method}")
        return entry

    def search(
        self,
        query: str = "",
        *,
        namespace: str = "functions",
        limit: int = 50,
        offset: int = 0,
    ) -> list[dict[str, Any]]:
        if namespace not in {"functions", "types", "all"}:
            raise RawAPIError("namespace must be functions, types or all")
        entries = []
        sources = []
        if namespace in {"functions", "all"}:
            sources.append(self.functions)
        if namespace in {"types", "all"}:
            sources.append(self.types)
        query = query.strip().casefold()
        for source in sources:
            unique = {entry.canonical: entry for entry in source.values()}
            entries.extend(unique.values())
        entries.sort(key=lambda entry: entry.canonical)
        if query:
            entries = [
                entry
                for entry in entries
                if query in entry.canonical.casefold()
                or query in entry.module.casefold()
            ]
        return [
            {
                "kind": entry.kind,
                "method": entry.canonical,
                "module": entry.module,
                "id": entry.object_id,
            }
            for entry in entries[
                max(offset, 0) : max(offset, 0) + max(1, min(limit, 200))
            ]
        ]

    def describe(self, method: str, *, kind: str = "functions") -> dict[str, Any]:
        entry = self.resolve(method, kind=kind)
        parameters = []
        for parameter in inspect.signature(entry.cls).parameters.values():
            parameters.append(
                {
                    "name": parameter.name,
                    "required": parameter.default is inspect.Parameter.empty,
                    "type": str(parameter.annotation)
                    if parameter.annotation is not inspect.Parameter.empty
                    else None,
                    "default": None
                    if parameter.default is inspect.Parameter.empty
                    else parameter.default,
                }
            )
        return {
            "kind": entry.kind,
            "method": entry.canonical,
            "module": entry.module,
            "class": entry.name,
            "id": entry.object_id,
            "parameters": parameters,
            "doc": inspect.getdoc(entry.cls) or "",
        }


catalog = RawCatalog()


async def _decode(value: Any, client: Any) -> Any:
    return await _decode_at_depth(value, client, 0)


async def _decode_at_depth(value: Any, client: Any, depth: int) -> Any:
    if depth > 8:
        raise RawAPIError("raw parameter nesting exceeds depth limit")
    if isinstance(value, list):
        return [await _decode_at_depth(item, client, depth + 1) for item in value]
    if not isinstance(value, dict):
        return value

    marker = value.get("_") or value.get("__type__")
    if marker == "__resolve_peer__":
        if set(value) - {"_", "__type__", "value"} or "value" not in value:
            raise RawAPIError("__resolve_peer__ requires only a value")
        return await client.resolve_peer(value["value"])
    if marker == "__bytes__":
        try:
            return base64.b64decode(value["base64"], validate=True)
        except (KeyError, TypeError, ValueError) as exc:
            raise RawAPIError("__bytes__ requires valid base64") from exc
    if isinstance(marker, str) and marker.startswith("types."):
        entry = catalog.resolve(marker, kind="types")
        params = {
            key: await _decode_at_depth(item, client, depth + 1)
            for key, item in value.items()
            if key not in {"_", "__type__"}
        }
        try:
            return entry.cls(**params)
        except TypeError as exc:
            raise RawAPIError(
                f"Invalid parameters for {entry.canonical}: {exc}"
            ) from exc
    return {
        key: await _decode_at_depth(item, client, depth + 1)
        for key, item in value.items()
    }


async def invoke_raw(
    client: Any, method: str, params: dict[str, Any] | None = None
) -> Any:
    if not isinstance(params, dict):
        raise RawAPIError("params must be an object")
    entry = catalog.resolve(method, kind="functions")
    decoded = {key: await _decode(value, client) for key, value in params.items()}
    try:
        request = entry.cls(**decoded)
    except TypeError as exc:
        raise RawAPIError(f"Invalid parameters for {entry.canonical}: {exc}") from exc
    return await client.invoke(request)


def search_raw(
    query: str = "", namespace: str = "functions", limit: int = 50, offset: int = 0
) -> list[dict[str, Any]]:
    return catalog.search(query, namespace=namespace, limit=limit, offset=offset)


def describe_raw(method: str, namespace: str = "functions") -> dict[str, Any]:
    if namespace == "all":
        namespace = (
            "types"
            if method.strip().removeprefix("pyrogram.raw.").startswith("types.")
            else "functions"
        )
    return catalog.describe(method, kind=namespace)
