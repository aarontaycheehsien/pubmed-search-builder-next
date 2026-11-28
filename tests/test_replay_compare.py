import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "evals"))

import replay
from psb.ncbi import NcbiError


def test_compare_measures_both_differences_even_when_counts_tie(monkeypatch):
    original = "old[tiab] OR shared[tiab]"
    revised = "new[tiab] OR shared[tiab]"
    cutoff = 'AND ("1800/01/01"[crdt] : "2023/03/31"[crdt])'
    answers = {original: ["1", "2", "3"], revised: ["1", "4", "5"],
               f"({revised}) NOT ({original})": ["4", "5"],
               f"({original}) NOT ({revised})": ["2", "3"]}
    client = replay.PubMed()

    def search(query, *, retmax):
        bounded_answers = {f"({term}) {cutoff}": ids for term, ids in answers.items()}
        ids = bounded_answers[query]
        return {"count": len(ids), "pmids": ids[:retmax], "issues": []}

    def among(query, gold):
        return set(search(query, retmax=10)["pmids"]) & set(gold)

    monkeypatch.setattr(client, "search", search)
    monkeypatch.setattr(client, "among", among)
    result = replay.compare_queries(client, original, revised,
                                    {"as_of": "2023-03-31", "gold_pmids": ["3", "5"]}, limit=1)
    assert result["added"]["pmids"] == ["4"]
    assert result["added"]["fixture_gold_pmids"] == ["5"]
    assert result["removed"]["pmids"] == ["2"]
    assert result["removed"]["fixture_gold_pmids"] == ["3"]
    assert result["added"]["complete"] is False
    assert result["removed"]["count"] == result["added"]["count"] == 2


def test_compare_rejects_an_incomplete_response(monkeypatch):
    client = replay.PubMed()
    monkeypatch.setattr(client, "search", lambda query, retmax: {"count": 1, "pmids": [], "issues": []})
    with pytest.raises(NcbiError, match="incomplete"):
        replay.compare_queries(client, "old", "new", {"gold_pmids": []}, limit=25)


def test_nursing_case_keeps_original_limits_and_other_terms():
    topic = "Liu_2023_VR_nursing"
    directory = Path(replay.__file__).parent
    card = directory / "results" / topic / "lean-optimal-codex-noseed-20260927T101600Z.json"
    original = json.loads(card.read_text(encoding="utf-8"))["strategy"]
    revised = (directory / "cases" / topic / "computerized-simulation.txt").read_text(encoding="utf-8").strip()
    addition = ' OR "computerized simulation*"[tiab] OR "computerised simulation*"[tiab]'
    assert revised.count(addition) == 1
    assert revised.replace(addition, "") == original
