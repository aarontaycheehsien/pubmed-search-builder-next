"""Offline test doubles: a PubMed that evaluates Boolean queries over a small in-memory corpus."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from psb import wildcards  # noqa: E402
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
