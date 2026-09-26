"""Workspace-scoped response cache.

Responses live inside one run workspace, so a count fetched for one review is never served
to another. Counts and links go stale as PubMed grows (24 h); record content does not (30 d).
Credentials are never part of a key or an entry.
"""

from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path
from typing import Mapping

VOLATILE_TTL = 24 * 3600
RECORD_TTL = 30 * 24 * 3600
RECORD_ENDPOINTS = frozenset({"efetch.fcgi", "esummary.fcgi"})
UNKEYED = frozenset({"api_key", "email", "tool"})


def cache_key(endpoint: str, params: Mapping[str, str]) -> str:
    keyed = {k: v for k, v in sorted(params.items()) if k not in UNKEYED}
    raw = json.dumps([endpoint, keyed], sort_keys=True, ensure_ascii=True)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


class Cache:
    def __init__(self, directory: Path | None, *, enabled: bool = True, clock=time.time) -> None:
        self.directory = directory
        self.enabled = enabled and directory is not None
        self._clock = clock
        self.hits = 0
        self.misses = 0

    def _path(self, key: str) -> Path:
        assert self.directory is not None
        return self.directory / key[:2] / f"{key}.json"

    def get(self, endpoint: str, params: Mapping[str, str]) -> bytes | None:
        if not self.enabled:
            return None
        path = self._path(cache_key(endpoint, params))
        try:
            entry = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            self.misses += 1
            return None
        ttl = RECORD_TTL if endpoint in RECORD_ENDPOINTS else VOLATILE_TTL
        if self._clock() - float(entry.get("stored_at", 0)) > ttl:
            self.misses += 1
            return None
        self.hits += 1
        return str(entry["body"]).encode("utf-8")

    def put(self, endpoint: str, params: Mapping[str, str], body: bytes) -> None:
        if not self.enabled:
            return
        path = self._path(cache_key(endpoint, params))
        path.parent.mkdir(parents=True, exist_ok=True)
        entry = {"stored_at": self._clock(), "endpoint": endpoint, "body": body.decode("utf-8", errors="replace")}
        tmp = path.with_suffix(".tmp")
        tmp.write_text(json.dumps(entry), encoding="utf-8")
        tmp.replace(path)

    def clear(self) -> int:
        if self.directory is None or not self.directory.is_dir():
            return 0
        removed = 0
        for path in self.directory.glob("*/*.json"):
            path.unlink()
            removed += 1
        return removed
