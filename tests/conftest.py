"""Offline test doubles: a PubMed that evaluates Boolean queries over a small in-memory corpus."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from psb import wildcards  # noqa: E402
from psb.ncbi import PubMed  # noqa: E402
from psb.openalex import OpenAlex  # noqa: E402
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

    doi_map: dict[str, str] = {}

    def idconv(self, ids):
        return {i: self.doi_map[i.lower()] for i in ids if i.lower() in self.doi_map}


class FakeOpenAlex(OpenAlex):
    """Serves /works requests from ``works`` ({"W1": {...}}), parsing the filters psb sends."""

    def __init__(self, works: dict[str, dict] | None = None, fail: str | None = None):
        super().__init__(api_key="")
        self.store = {}
        for wid, work in (works or {}).items():
            self.add(wid, **work)
        self.fail = fail
        self.calls: list[tuple[str, dict]] = []

    def add(self, wid, *, pmid=None, doi=None, title="", year=2020, type="article", refs=(), cites=(), topic=None):
        self.store[wid] = {"id": f"https://openalex.org/{wid}", "ids": {"openalex": f"https://openalex.org/{wid}",
                           **({"pmid": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}"} if pmid else {})},
                           "doi": f"https://doi.org/{doi}" if doi else None, "display_name": title or wid,
                           "publication_year": year, "type": type,
                           "referenced_works": [f"https://openalex.org/{r}" for r in refs], "referenced_works_count": len(refs),
                           "cites": list(cites), "cited_by_count": 0,
                           "primary_topic": {"id": f"https://openalex.org/{topic[0]}", "display_name": topic[1]} if topic else None}

    def _match(self, work, name, value):
        options = value.split("|")
        if name == "ids.openalex":
            return work["id"].rsplit("/", 1)[-1] in options
        if name == "ids.pmid":
            return work["ids"].get("pmid", "").rsplit("/", 1)[-1] in options
        if name == "cites":
            return value in work["cites"]
        if name == "type":
            return work["type"] in options
        if name == "primary_topic.id":
            return bool(work["primary_topic"]) and work["primary_topic"]["id"].rsplit("/", 1)[-1] in options
        if name == "has_pmid":
            return bool(work["ids"].get("pmid")) == (value == "true")
        if name == "to_publication_date":
            return work["publication_year"] <= int(value[:4])
        raise AssertionError(f"unexpected filter {name}")

    def request(self, path, params):
        self.calls.append((path, dict(params)))
        if self.fail:
            from psb.openalex import OpenAlexError
            raise OpenAlexError(self.fail)
        if path.startswith("/works/"):
            ident = path.split("/", 2)[2]
            for wid, work in self.store.items():
                if ident in (wid, f"pmid:{work['ids'].get('pmid', '').rsplit('/', 1)[-1]}",
                             f"doi:{(work['doi'] or '').removeprefix('https://doi.org/')}"):
                    return work
            return None
        rows = list(self.store.values())
        for clause in filter(None, params.get("filter", "").split(",")):
            name, value = clause.split(":", 1)
            rows = [w for w in rows if self._match(w, name, value)]
        if params.get("search"):
            words = params["search"].lower().split()
            rows = [w for w in rows if all(word in w["display_name"].lower() for word in words)]
        rows.sort(key=lambda w: w["id"])
        if params.get("sample"):
            import random as _random
            rows = _random.Random(int(params.get("seed", 0))).sample(rows, min(len(rows), int(params["sample"])))
        per = int(params.get("per-page", 25))
        return {"meta": {"count": len(rows), "next_cursor": None}, "results": rows[:per]}


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
        ws.openalex = FakeOpenAlex()
        return ws, fake

    return factory
