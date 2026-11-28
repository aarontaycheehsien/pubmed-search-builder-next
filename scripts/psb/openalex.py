"""OpenAlex client for known-record discovery.

PubMed holds a reference list mostly for reviews in PMC, and nothing outside MEDLINE/PubMed.
OpenAlex holds deposited reference lists for most works with a DOI, citing works across the
index, and a topic classification. psb uses it only to find candidate known records, which
are mapped back to PMIDs: it never searches OpenAlex for the review itself.

Every request is logged in the workspace (``type: openalex``) and cached there like NCBI
responses. The API key, when set, travels in the Authorization header and is never logged
or cached.
"""

from __future__ import annotations

import json
import re
import urllib.parse
from typing import Callable, Iterable

from .cache import Cache
from .config import read_env
from .http import Policy, Transport, TransportError

BASE_URL = "https://api.openalex.org"
LIST_FIELDS = ("id,ids,doi,display_name,publication_year,publication_date,type,primary_topic,"
               "referenced_works_count,cited_by_count")
ORIGIN_FIELDS = LIST_FIELDS + ",referenced_works"
ID_CHUNK = 50      # values per OR filter (OpenAlex allows up to 100)
PER_PAGE = 100     # OpenAlex maximum
MAX_PAGES = 25
_WORK = re.compile(r"W[1-9]\d*", re.I)
_PMCID = re.compile(r"(?:pmcid:\s*)?(PMC[1-9]\d*)", re.I)
_DOI = re.compile(r"10\.\d{4,9}/\S+", re.I)
_BUDGET = re.compile(r"budget|credits|daily|insufficient", re.I)


class OpenAlexError(RuntimeError):
    pass


def normalise_id(raw: str) -> str:
    """An OpenAlex path identifier for a PMID, DOI, PMCID or OpenAlex work ID."""
    value = urllib.parse.unquote(str(raw).strip()).rstrip("/")
    tail = re.sub(r"^https?://(?:api\.)?openalex\.org/(?:works/)?", "", value, flags=re.I)
    if _WORK.fullmatch(tail):
        return tail.upper()
    pmid = re.sub(r"^(?:https?://pubmed\.ncbi\.nlm\.nih\.gov/|pmid:\s*)", "", value, flags=re.I)
    if pmid.isdigit() and pmid.strip("0"):
        return "pmid:" + pmid.lstrip("0")
    if m := _PMCID.fullmatch(re.sub(r"^https?://(?:www\.)?(?:ncbi\.nlm\.nih\.gov/pmc|pmc\.ncbi\.nlm\.nih\.gov)/articles/", "", value, flags=re.I)):
        return "pmcid:" + m[1].upper()
    doi = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", value, flags=re.I)
    if _DOI.fullmatch(doi):
        return "doi:" + doi.lower()
    raise OpenAlexError(f"expected a PMID, DOI, PMCID or OpenAlex work ID: {raw!r}")


def work_id(work: dict) -> str:
    value = str(work.get("id") or "").rsplit("/", 1)[-1]
    if not _WORK.fullmatch(value):
        raise OpenAlexError("OpenAlex returned a work without a valid ID")
    return value.upper()


def pmid_of(work: dict) -> str | None:
    raw = str(((work.get("ids") or {}).get("pmid")) or "")
    digits = raw.rstrip("/").rsplit("/", 1)[-1]
    return digits.lstrip("0") if digits.isdigit() and digits.strip("0") else None


def doi_of(work: dict) -> str | None:
    raw = str(work.get("doi") or (work.get("ids") or {}).get("doi") or "")
    doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", raw, flags=re.I)
    return doi.lower() if _DOI.fullmatch(doi) else None


def topic_of(work: dict) -> dict | None:
    topic = work.get("primary_topic") or {}
    if not isinstance(topic, dict) or not topic.get("id"):
        return None
    return {"id": str(topic["id"]).rsplit("/", 1)[-1], "name": topic.get("display_name") or ""}


def brief(work: dict) -> dict:
    """The fields psb shows and stores for a work."""
    return {"work": work_id(work), "pmid": pmid_of(work), "doi": doi_of(work), "title": work.get("display_name") or "",
            "year": work.get("publication_year"), "type": work.get("type"), "topic": topic_of(work),
            "references": work.get("referenced_works_count"), "cited_by": work.get("cited_by_count")}


class OpenAlex:
    def __init__(self, *, cache: Cache | None = None, log: Callable[[dict], None] | None = None,
                 transport: Transport | None = None, api_key: str | None = None, per_second: float | None = None) -> None:
        self.api_key = read_env("OPENALEX_API_KEY") if api_key is None else api_key
        self.per_second = per_second if per_second is not None else 10.0
        self.cache = cache or Cache(None, enabled=False)
        self.log = log or (lambda entry: None)
        self.transport = transport or Transport()
        self.requests = 0

    # -- transport ---------------------------------------------------------------------------

    def request(self, path: str, params: dict[str, str]) -> dict | None:
        """One GET. Returns None for 404 (an unknown work), raises OpenAlexError otherwise."""
        endpoint = "openalex" + path
        cached = self.cache.get(endpoint, params)
        if cached is not None:
            self.log({"type": "openalex", "path": path, "params": params, "cache": True})
            return json.loads(cached.decode("utf-8"))
        headers = {"Accept": "application/json", "User-Agent": "pubmed-search-builder/2.0"}
        if self.api_key:
            headers["Authorization"] = "Bearer " + self.api_key
        try:
            body = self.transport.request(BASE_URL + urllib.parse.quote(path, safe="/:"), params, headers=headers,
                                          policy=Policy(per_second=self.per_second))
        except TransportError as exc:
            message = str(exc)
            if message.startswith("HTTP 404"):
                self.log({"type": "openalex", "path": path, "params": params, "cache": False, "status": 404})
                return None
            if message.startswith("HTTP 429") and _BUDGET.search(message):
                raise OpenAlexError("OpenAlex refused the request: the API budget is used up. Set OPENALEX_API_KEY, "
                                    "add credit, or wait for the daily reset. " + message) from exc
            raise OpenAlexError(f"OpenAlex request failed: {message}") from exc
        self.requests += 1
        try:
            data = json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, ValueError) as exc:
            raise OpenAlexError(f"OpenAlex returned invalid JSON for {path}") from exc
        if not isinstance(data, dict):
            raise OpenAlexError(f"OpenAlex returned a non-object JSON body for {path}")
        self.cache.put(endpoint, params, body)
        self.log({"type": "openalex", "path": path, "params": params, "cache": False})
        return data

    def _list(self, params: dict[str, str]) -> tuple[list[dict], int]:
        data = self.request("/works", params)
        if data is None:
            raise OpenAlexError("OpenAlex /works answered 404")
        meta, rows = data.get("meta") or {}, data.get("results")
        if not isinstance(rows, list) or not isinstance(meta.get("count"), int):
            raise OpenAlexError("malformed OpenAlex list response: meta.count and results are required")
        return rows, meta["count"]

    # -- works -------------------------------------------------------------------------------

    def work(self, identifier: str, *, select: str = ORIGIN_FIELDS) -> dict | None:
        return self.request("/works/" + normalise_id(identifier), {"select": select})

    def works(self, field: str, values: Iterable[str], *, select: str = LIST_FIELDS) -> list[dict]:
        """Works whose ``field`` matches any of ``values``, asked for in OR chunks."""
        ordered = list(dict.fromkeys(str(v) for v in values if str(v)))
        found: list[dict] = []
        for start in range(0, len(ordered), ID_CHUNK):
            chunk = ordered[start:start + ID_CHUNK]
            rows, count = self._list({"filter": f"{field}:{'|'.join(chunk)}", "per-page": str(PER_PAGE), "select": select})
            if count > PER_PAGE:
                raise OpenAlexError(f"OpenAlex matched {count} works for {len(chunk)} identifiers; the lookup is ambiguous")
            found += rows
        return found

    def by_ids(self, work_ids: Iterable[str], *, select: str = LIST_FIELDS) -> list[dict]:
        return self.works("ids.openalex", [normalise_id(w) for w in work_ids], select=select)

    def by_pmids(self, pmids: Iterable[str], *, select: str = LIST_FIELDS) -> dict[str, dict]:
        found = {}
        for work in self.works("ids.pmid", pmids, select=select):
            pmid = pmid_of(work)
            if pmid:
                found.setdefault(pmid, work)
        return found

    def citing(self, identifier: str, *, limit: int, until: str | None = None) -> tuple[list[dict], int]:
        """Works that cite one work (forward citation), most cited first, up to ``limit``."""
        filters = [f"cites:{normalise_id(identifier)}"]
        if until:
            filters.append(f"to_publication_date:{until}")
        rows: list[dict] = []
        cursor, total = "*", 0
        for _ in range(MAX_PAGES):
            params = {"filter": ",".join(filters), "per-page": str(min(PER_PAGE, max(1, limit))), "cursor": cursor,
                      "sort": "cited_by_count:desc", "select": LIST_FIELDS}
            data = self.request("/works", params) or {}
            page, meta = data.get("results"), data.get("meta") or {}
            if not isinstance(page, list) or not isinstance(meta.get("count"), int):
                raise OpenAlexError("malformed OpenAlex citing-works response")
            total = meta["count"]
            rows += page
            cursor = meta.get("next_cursor")
            if not page or not cursor or len(rows) >= limit:
                break
        return rows[:limit], total

    def _take_pages(self, params: dict[str, str], n: int) -> tuple[list[dict], int]:
        page_size = min(PER_PAGE, max(1, n))
        params = {**params, "per-page": str(page_size), "select": LIST_FIELDS}
        rows, total = self._list(params)
        page = rows
        number = 1
        while len(rows) < min(n, total) and len(page) == page_size:
            number += 1
            page, _ = self._list({**params, "page": str(number)})
            rows = rows + page
        return rows[:n], total

    def search(self, text: str, *, filters: list[str], n: int) -> tuple[list[dict], int]:
        return self._take_pages({"search": text, "filter": ",".join(filters)}, n)

    def sample(self, *, filters: list[str], n: int, seed: int) -> tuple[list[dict], int]:
        """A seeded random sample of works matching ``filters`` (OpenAlex's own sampler)."""
        return self._take_pages({"filter": ",".join(filters), "sample": str(n), "seed": str(seed)}, n)
