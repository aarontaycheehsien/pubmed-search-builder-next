"""NCBI E-utilities client for PubMed and MeSH.

Every request is appended to the workspace log as a side effect, so provenance needs no
separate bookkeeping step. When the workspace sets ``as_of``, every PubMed search is bounded
to records added to PubMed on or before that date.
"""

from __future__ import annotations

import json
import re
import time
import xml.etree.ElementTree as ET
from typing import Callable, Iterable

from .cache import Cache
from .config import read_env
from .http import Policy, Transport, TransportError
from .translation import translation_issues

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
IDCONV_URL = "https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/"
DEFAULT_TOOL = "pubmed-search-builder"
POST_THRESHOLD = 1400
UID_CHUNK = 100
FETCH_CHUNK = 200
BODY_ERROR_RETRIES = 3
_XML_ERROR = re.compile(rb"<ERROR>(.*?)</ERROR>", re.DOTALL)
LINKNAMES = {
    "similar": "pubmed_pubmed",
    "citedin": "pubmed_pubmed_citedin",
    "refs": "pubmed_pubmed_refs",
}


class NcbiError(RuntimeError):
    pass


def body_error(raw: bytes) -> str | None:
    """E-utilities reports backend failures inside HTTP 200 bodies; find them.

    Reading ``count`` from such a body gives 0, silently turning an outage into "this query
    retrieves nothing". ``errorlist`` (phrases not found) is ordinary output, not an error.
    """
    stripped = raw.lstrip()[:1]
    if stripped == b"<":
        match = _XML_ERROR.search(raw)
        return (match.group(1).decode("utf-8", errors="replace").strip() or "unspecified error") if match else None
    if stripped != b"{":
        return None
    try:
        payload = json.loads(raw.decode("utf-8", errors="replace"), strict=False)
    except ValueError:
        return None
    if not isinstance(payload, dict):
        return None
    for node in (payload, payload.get("esearchresult"), payload.get("elinkresult")):
        if isinstance(node, dict):
            message = node.get("ERROR") or node.get("error")
            if isinstance(message, str) and message.strip():
                return message.strip()
            if isinstance(message, list) and message:
                return "; ".join(map(str, message))
    return None


def _text(node: ET.Element | None) -> str:
    return " ".join("".join(node.itertext()).split()) if node is not None else ""


def parse_article(article: ET.Element) -> dict[str, object]:
    citation = article.find("MedlineCitation")
    data = article.find("PubmedData")
    art = citation.find("Article") if citation is not None else None
    journal = art.find("Journal") if art is not None else None
    pubdate = journal.find("./JournalIssue/PubDate") if journal is not None else None
    year = _text(pubdate.find("Year")) if pubdate is not None else ""
    if not year and pubdate is not None:
        year = _text(pubdate.find("MedlineDate"))[:4]

    abstract = []
    for part in art.findall("./Abstract/AbstractText") if art is not None else []:
        label = part.attrib.get("Label")
        text = _text(part)
        if text:
            abstract.append(f"{label}: {text}" if label else text)

    ids = {node.attrib.get("IdType"): _text(node) for node in (data.findall("./ArticleIdList/ArticleId") if data is not None else [])}
    mesh = []
    for heading in citation.findall("./MeshHeadingList/MeshHeading") if citation is not None else []:
        descriptor = heading.find("DescriptorName")
        if descriptor is not None:
            mesh.append(
                {
                    "ui": descriptor.attrib.get("UI", ""),
                    "name": _text(descriptor),
                    "major": descriptor.attrib.get("MajorTopicYN") == "Y",
                    "qualifiers": [_text(q) for q in heading.findall("QualifierName")],
                }
            )
    return {
        "pmid": _text(citation.find("PMID")) if citation is not None else "",
        "title": _text(art.find("ArticleTitle")) if art is not None else "",
        "abstract": "\n".join(abstract),
        "journal": _text(journal.find("Title")) if journal is not None else "",
        "year": year,
        "doi": ids.get("doi", ""),
        "pmcid": ids.get("pmc", ""),
        "publication_types": [_text(n) for n in art.findall("./PublicationTypeList/PublicationType")] if art is not None else [],
        "mesh": mesh,
        "keywords": [_text(n) for n in citation.findall("./KeywordList/Keyword")] if citation is not None else [],
        "status": citation.attrib.get("Status", "") if citation is not None else "",
    }


def chunks(values: list[str], size: int) -> Iterable[list[str]]:
    for start in range(0, len(values), size):
        yield values[start : start + size]


def uid_block(pmids: Iterable[str]) -> str:
    return " OR ".join(f"{pmid}[uid]" for pmid in pmids)


class PubMed:
    def __init__(
        self,
        *,
        transport: Transport | None = None,
        cache: Cache | None = None,
        log: Callable[[dict], None] | None = None,
        as_of: str | None = None,
    ) -> None:
        self.email = read_env("NCBI_EMAIL")
        self.api_key = read_env("NCBI_API_KEY")
        self.tool = read_env("NCBI_TOOL", DEFAULT_TOOL)
        self.per_second = 10.0 if self.api_key else 3.0
        self.transport = transport or Transport()
        self.cache = cache or Cache(None)
        self.log = log or (lambda entry: None)
        self.as_of = as_of
        self.requests = 0

    # -- transport -------------------------------------------------------------------------

    def _params(self, params: dict[str, str]) -> dict[str, str]:
        merged = {"tool": self.tool}
        if self.email:
            merged["email"] = self.email
        if self.api_key:
            merged["api_key"] = self.api_key
        merged.update(params)
        return merged

    def request(self, endpoint: str, params: dict[str, str], *, method: str = "GET", url: str | None = None) -> bytes:
        merged = self._params(params) if url is None else dict(params)
        visible = {k: v for k, v in params.items() if k not in {"api_key", "email"}}
        cached = self.cache.get(endpoint, merged)
        if cached is not None and body_error(cached) is None:
            self.log({"type": "ncbi", "endpoint": endpoint, "params": visible, "cache": True})
            return cached
        headers = {"User-Agent": f"{self.tool}/2.0" + (f" ({self.email})" if self.email else "")}
        failure = ""
        for attempt in range(BODY_ERROR_RETRIES + 1):
            try:
                body = self.transport.request(
                    url or f"{BASE_URL}/{endpoint}",
                    merged,
                    method=method,
                    headers=headers,
                    policy=Policy(per_second=self.per_second),
                )
            except TransportError as exc:
                raise NcbiError(str(exc)) from exc
            self.requests += 1
            failure = body_error(body) or ""
            if not failure:
                self.cache.put(endpoint, merged, body)
                self.log({"type": "ncbi", "endpoint": endpoint, "params": visible, "cache": False})
                return body
            if "cannot search because" in failure.casefold():
                raise NcbiError(f"PubMed rejected the query (not an outage): {failure}")
            if attempt < BODY_ERROR_RETRIES:
                time.sleep(2**attempt)
        raise NcbiError(f"NCBI {endpoint} kept reporting an error: {failure}")

    def _json(self, endpoint: str, params: dict[str, str], *, method: str = "GET") -> dict:
        raw = self.request(endpoint, params, method=method)
        try:
            # eLink sometimes embeds raw control characters in strings.
            data = json.loads(raw.decode("utf-8"), strict=endpoint != "elink.fcgi")
        except (UnicodeDecodeError, ValueError) as exc:
            raise NcbiError(f"NCBI returned invalid JSON from {endpoint}: {exc}") from exc
        if not isinstance(data, dict):
            raise NcbiError(f"NCBI {endpoint} returned a non-object JSON body")
        return data

    # -- PubMed ----------------------------------------------------------------------------

    def search(self, query: str, *, retmax: int = 0, retstart: int = 0, sort: str | None = None, dated: bool = True) -> dict:
        params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": str(retmax), "retstart": str(retstart)}
        if sort:
            params["sort"] = sort
        if dated and self.as_of:
            params.update({"datetype": "edat", "mindate": "1800/01/01", "maxdate": self.as_of.replace("-", "/")})
        data = self._json("esearch.fcgi", params, method="POST" if len(query) > POST_THRESHOLD else "GET")
        result = data.get("esearchresult", {})
        translation = str(result.get("querytranslation", ""))
        stack = [
            {"term": item.get("term", ""), "field": item.get("field", ""), "count": int(item.get("count", 0) or 0)}
            for item in result.get("translationstack", []) or []
            if isinstance(item, dict)
        ]
        return {
            "query": query,
            "count": int(result.get("count", 0) or 0),
            "pmids": [str(p) for p in result.get("idlist", [])],
            "translation": translation,
            "term_counts": stack,
            "issues": translation_issues(
                query, translation, result.get("translationset"), result.get("warninglist"), result.get("errorlist")
            ),
        }

    def count(self, query: str) -> int:
        return self.search(query)["count"]

    def among(self, query: str, pmids: Iterable[str]) -> set[str]:
        """The subset of ``pmids`` that ``query`` retrieves (within the as-of window)."""
        found: set[str] = set()
        for chunk in chunks(sorted(set(pmids)), UID_CHUNK):
            combined = f"({query}) AND ({uid_block(chunk)})" if query else uid_block(chunk)
            found.update(self.search(combined, retmax=len(chunk))["pmids"])
        return found

    def existing(self, pmids: Iterable[str]) -> set[str]:
        """PMIDs that exist in PubMed (and were added by ``as_of``, when set)."""
        return self.among("", pmids)

    def fetch(self, pmids: Iterable[str]) -> list[dict]:
        records: list[dict] = []
        for chunk in chunks([str(p) for p in pmids], FETCH_CHUNK):
            raw = self.request(
                "efetch.fcgi", {"db": "pubmed", "id": ",".join(chunk), "retmode": "xml"},
                method="POST" if len(chunk) > 50 else "GET",
            )
            try:
                root = ET.fromstring(raw)
            except ET.ParseError as exc:
                raise NcbiError(f"efetch returned invalid XML: {exc}") from exc
            records.extend(parse_article(node) for node in root.findall("./PubmedArticle"))
        return records

    def links(self, pmid: str, link: str) -> list[dict]:
        """Neighbours of one PMID. ``link`` is similar, citedin, or refs."""
        linkname = LINKNAMES[link]
        params = {"dbfrom": "pubmed", "db": "pubmed", "id": str(pmid), "linkname": linkname, "retmode": "json"}
        if link == "similar":
            params["cmd"] = "neighbor_score"
        data = self._json("elink.fcgi", params)
        rows = []
        for linkset in data.get("linksets", []) or []:
            for db in linkset.get("linksetdbs", []) or []:
                if db.get("linkname") != linkname:
                    continue
                for item in db.get("links", []) or []:
                    if isinstance(item, dict):
                        rows.append({"pmid": str(item.get("id", "")), "score": int(item["score"]) if str(item.get("score", "")).isdigit() else None})
                    else:
                        rows.append({"pmid": str(item), "score": None})
        return [row for row in rows if row["pmid"] and row["pmid"] != str(pmid)]

    def idconv(self, ids: list[str]) -> dict[str, str]:
        """Map PMCIDs/DOIs to PMIDs through the PMC ID converter."""
        params = {"ids": ",".join(ids), "format": "json", "tool": self.tool}
        if self.email:
            params["email"] = self.email
        raw = self.request("idconv", params, url=IDCONV_URL)
        data = json.loads(raw.decode("utf-8"))
        return {
            str(item.get("requested-id", "")): str(item.get("pmid", ""))
            for item in data.get("records", [])
            if item.get("pmid")
        }

    # -- MeSH ------------------------------------------------------------------------------

    def mesh_search(self, term: str, *, retmax: int = 10) -> list[str]:
        data = self._json("esearch.fcgi", {"db": "mesh", "term": term, "retmode": "json", "retmax": str(retmax)})
        return [str(uid) for uid in data.get("esearchresult", {}).get("idlist", [])]

    def mesh_summary(self, uids: list[str]) -> list[dict]:
        if not uids:
            return []
        data = self._json("esummary.fcgi", {"db": "mesh", "id": ",".join(uids), "retmode": "json"})
        result = data.get("result", {})
        return [result[uid] for uid in result.get("uids", []) if isinstance(result.get(uid), dict)]
