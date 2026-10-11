"""Bounded OpenAlex semantic retrieval. Never return article content to the builder.

API contract: https://help.openalex.org/api/semantic-search/
Responses are archived by miss_hunt in the private screening store, not a shared cache.
"""
from __future__ import annotations

import json
import re

from .config import read_env
from .http import Policy, Transport, TransportError
from .workspace import WorkspaceError


class OpenAlex:
    def __init__(self, transport=None):
        self.transport = transport or Transport()

    def search(self, query: str, limit: int) -> dict:
        params = {"search.semantic": query, "per-page": str(limit), "select": "id,ids,doi"}
        key = read_env("OPENALEX_API_KEY")
        if key:
            params["api_key"] = key
        try:
            raw = self.transport.request("https://api.openalex.org/works", params,
                                         policy=Policy(per_second=1))
        except TransportError:
            # Provider error bodies may echo keys, queries or record content. Never relay them.
            raise WorkspaceError("OpenAlex semantic request failed; check OPENALEX_API_KEY, network access "
                                 "and quota, then retry the same miss-hunt command") from None
        try:
            data = json.loads(raw)
        except (ValueError, UnicodeError):
            raise WorkspaceError("OpenAlex returned invalid JSON") from None
        rows = data.get("results") if isinstance(data, dict) else None
        if not isinstance(rows, list) or len(rows) > limit or any(not isinstance(r, dict) for r in rows):
            raise WorkspaceError("OpenAlex returned an invalid or oversized semantic result list")
        # Persist only identifiers: even an unexpected provider field cannot expose content.
        return {"results": [{
            "id": r.get("id") if re.fullmatch(r"https://openalex.org/W[0-9]+", str(r.get("id"))) else None,
            "ids": {k: v for k, v in (r.get("ids") or {}).items() if k in {"pmid", "doi"} and isinstance(v, str)}
            if isinstance(r.get("ids"), dict) else {},
            "doi": r.get("doi") if isinstance(r.get("doi"), str) else None,
        } for r in rows]}
