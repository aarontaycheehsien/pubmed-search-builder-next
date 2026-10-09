"""Offline test doubles: a PubMed that evaluates Boolean queries over a small in-memory corpus, and the
same corpus behind the real client's transport (``CorpusTransport``) for request-log and cache tests."""

from __future__ import annotations

import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from psb import ncbi, wildcards  # noqa: E402
from psb import workspace as workspace_module  # noqa: E402
from psb.ncbi import PubMed  # noqa: E402
from psb.workspace import Workspace  # noqa: E402


class FakePubMed(PubMed):
    """``atoms`` maps a query atom (e.g. ``asthma[tiab]``) to the PMIDs it retrieves."""

    def __init__(self, atoms: dict[str, set[str]], records: dict[str, dict] | None = None, links: dict | None = None):
        super().__init__()
        self.atoms = {self._key(k): set(v) for k, v in atoms.items()}
        self.records = records or {}
        self._links = links or {}
        self.universe = set().union(*self.atoms.values(), self.records.keys()) if self.atoms else set(self.records)
        self.queries: list[str] = []

    mesh_records = {
        "asthma": {"ds_meshui": "D001249", "ds_meshterms": ["Asthma", "Bronchial Asthma"]},
        "child": {"ds_meshui": "D002648", "ds_meshterms": ["Child", "Children"]},
        "therapy": {"ds_meshui": "Q000628", "ds_meshterms": ["therapy"]},
        "drug therapy": {"ds_meshui": "Q000188", "ds_meshterms": ["drug therapy"]},
    }

    def mesh_search(self, term, *, retmax=10):
        name = term.split("[")[0].strip('"').casefold()
        return [key for key, row in self.mesh_records.items() if name in [n.casefold() for n in row["ds_meshterms"]]]

    def mesh_summary(self, uids):
        return [self.mesh_records[uid] for uid in uids]

    def mesh_descriptor(self, ui):
        return {"identifier": ui, "allowableQualifier": ["http://id.nlm.nih.gov/mesh/Q000628", "http://id.nlm.nih.gov/mesh/Q000188"]}

    def field_names(self):
        return {"tiab", "title/abstract", "newfield"}

    @staticmethod
    def _key(atom: str) -> str:
        return " ".join(atom.split()).lower()

    # recursive descent: expr := and_expr (OR and_expr)* ; and_expr := unary ((AND|NOT) unary)*
    def _evaluate(self, query: str) -> set[str]:
        tokens = wildcards._TOKEN.findall(query)
        position = 0

        def peek():
            return tokens[position] if position < len(tokens) else None

        def take():
            nonlocal position
            position += 1
            return tokens[position - 1]

        def atom() -> set[str]:
            words = []
            while peek() is not None and peek() not in ("(", ")") and peek().upper() not in ("AND", "OR", "NOT"):
                token = take()
                if token.startswith("["):
                    words[-1] = words[-1] + token
                else:
                    words.append(token)
            text = " ".join(words)
            if text.lower().endswith("[edat]"):
                return set(self.universe)
            if text.lower().endswith("[uid]"):
                pmid = text[:-5]
                return {pmid} if pmid in self.universe else set()
            return set(self.atoms.get(self._key(text), set()))

        def unary() -> set[str]:
            if peek() == "(":
                take()
                value = expr()
                take()
                return value
            return atom()

        def and_expr() -> set[str]:
            value = unary()
            while peek() is not None and peek().upper() in ("AND", "NOT"):
                op = take().upper()
                right = unary()
                value = value & right if op == "AND" else value - right
            return value

        def expr() -> set[str]:
            value = and_expr()
            while peek() is not None and peek().upper() == "OR":
                take()
                value = value | and_expr()
            return value

        return expr()

    def search(self, query, *, retmax=0, retstart=0, sort=None, dated=True):
        self.queries.append(query)
        found = sorted(self._evaluate(query), key=int)
        return {"query": query, "count": len(found), "pmids": found[retstart : retstart + retmax],
                "translation": query, "term_counts": [], "issues": []}

    def fetch(self, pmids):
        return [self.records[p] for p in pmids if p in self.records]

    def links(self, pmid, link):
        return [{"pmid": p, "score": s} for p, s in self._links.get((pmid, link), [])]


def record(pmid: str, title: str, abstract: str = "", mesh: list[str] | None = None, keywords: list[str] | None = None) -> dict:
    return {"pmid": pmid, "title": title, "abstract": abstract, "year": "2020", "keywords": keywords or [],
            "mesh": [{"ui": "", "name": m, "major": False, "qualifiers": []} for m in mesh or []],
            "publication_types": ["Journal Article"], "status": "MEDLINE"}


@pytest.fixture
def make_ws(tmp_path):
    def factory(atoms, records=None, links=None, question="Q?") -> tuple[Workspace, FakePubMed]:
        ws = Workspace.create(tmp_path / "run", question)
        fake = FakePubMed(atoms, records, links)
        ws.pubmed = fake
        return ws, fake

    return factory


def articles_xml(records: list[dict]) -> bytes:
    """An efetch body for ``records``, as ``ncbi.parse_article`` reads it."""
    root = ET.Element("PubmedArticleSet")
    for r in records:
        article = ET.SubElement(root, "PubmedArticle")
        citation = ET.SubElement(article, "MedlineCitation", Status=r.get("status") or "MEDLINE")
        ET.SubElement(citation, "PMID").text = r["pmid"]
        art = ET.SubElement(citation, "Article")
        journal = ET.SubElement(art, "Journal")
        ET.SubElement(journal, "Title").text = r.get("journal") or "Journal"
        ET.SubElement(ET.SubElement(ET.SubElement(journal, "JournalIssue"), "PubDate"), "Year").text = r.get("year") or ""
        ET.SubElement(art, "ArticleTitle").text = r.get("title") or ""
        if r.get("abstract"):
            ET.SubElement(ET.SubElement(art, "Abstract"), "AbstractText").text = r["abstract"]
        types = ET.SubElement(art, "PublicationTypeList")
        for kind in r.get("publication_types") or []:
            ET.SubElement(types, "PublicationType").text = kind
        headings = ET.SubElement(citation, "MeshHeadingList")
        for m in r.get("mesh") or []:
            ET.SubElement(ET.SubElement(headings, "MeshHeading"), "DescriptorName", UI=m.get("ui") or "",
                          MajorTopicYN="Y" if m.get("major") else "N").text = m["name"]
        keywords = ET.SubElement(citation, "KeywordList")
        for word in r.get("keywords") or []:
            ET.SubElement(keywords, "Keyword").text = word
        ET.SubElement(ET.SubElement(article, "PubmedData"), "ArticleIdList")
    return ET.tostring(root, encoding="utf-8")


class CorpusTransport:
    """The E-utilities over an in-memory corpus, behind the real ``PubMed`` client, so its request log and
    cache run as they do live. ``calls`` lists every request that reached the network; ``errors`` maps a
    search term to the error PubMed reports for it; ``ids`` maps PMCIDs to PMIDs."""

    def __init__(self, atoms, records=None, links=None, *, ids=None, errors=None):
        self.corpus = FakePubMed(atoms, records, links)
        self.ids = ids or {}
        self.errors = errors or {}
        self.calls: list[tuple[str, dict]] = []

    def request(self, url, params, **kwargs):
        self.calls.append((url, dict(params)))
        if url.startswith(ncbi.IDCONV_URL):
            asked = params["ids"].split(",")
            return json.dumps({"records": [{"requested-id": i, "pmid": self.ids[i]} for i in asked if i in self.ids]}).encode()
        endpoint = url.rsplit("/", 1)[-1]
        if endpoint == "esearch.fcgi":
            term = params["term"]
            if term in self.errors:
                return json.dumps({"esearchresult": {"ERROR": self.errors[term]}}).encode()
            found = sorted(self.corpus._evaluate(term), key=int)
            start, size = int(params.get("retstart", 0)), int(params.get("retmax", 0))
            return json.dumps({"esearchresult": {"count": str(len(found)), "idlist": found[start:start + size],
                                                 "querytranslation": term}}).encode()
        if endpoint == "efetch.fcgi":
            return articles_xml([self.corpus.records[p] for p in params["id"].split(",") if p in self.corpus.records])
        if endpoint == "elink.fcgi":
            link = {name: short for short, name in ncbi.LINKNAMES.items()}[params["linkname"]]
            rows = self.corpus.links(params["id"], link)
            items = [{"id": r["pmid"], "score": str(r["score"])} for r in rows] if link == "similar" else [r["pmid"] for r in rows]
            return json.dumps({"linksets": [{"linksetdbs": [{"linkname": params["linkname"], "links": items}]}]}).encode()
        raise AssertionError(f"unexpected request to {url}")

    def endpoints(self) -> list[str]:
        return [url.rsplit("/", 1)[-1] if not url.startswith(ncbi.IDCONV_URL) else "idconv" for url, _ in self.calls]


class CorpusPubMed(PubMed):
    """The real client over a ``CorpusTransport``; only MeSH authority and field lookups stay fake."""
    mesh_records = FakePubMed.mesh_records
    mesh_search = FakePubMed.mesh_search
    mesh_summary = FakePubMed.mesh_summary
    mesh_descriptor = FakePubMed.mesh_descriptor
    field_names = FakePubMed.field_names


@pytest.fixture
def corpus(monkeypatch):
    """Install a corpus behind every Workspace's client. The Workspace still builds the client itself, with
    the cache and logger it chose, through the real ``cli.workspace()``."""
    def install(atoms, records=None, links=None, **kwargs) -> CorpusTransport:
        transport = CorpusTransport(atoms, records, links, **kwargs)
        monkeypatch.setattr(workspace_module, "CLIENT", lambda **kw: CorpusPubMed(transport=transport, **kw))
        return transport

    return install
