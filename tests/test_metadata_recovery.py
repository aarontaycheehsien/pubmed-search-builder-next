"""Metadata correction after closing must recover without resetting review history."""
import shutil
import sys
from pathlib import Path

import pytest

from psb import deliver, validation
from psb.evaluate import evaluate
from psb.workspace import WorkspaceError, read_json, write_json
from test_closing_round import PASS, write_round
from test_deliver import evaluated


def closed(make_ws):
    ws = evaluated(make_ws)
    for n in (1, 2, 3):
        write_round(ws, n, [], PASS, closing=n == 3)
    assert deliver.report(ws)["ok"]
    return ws


def edit(ws, **fields):
    write_json(ws.root / "protocol.json", {**ws.protocol(), **fields})


@pytest.mark.parametrize("key,value", [("scope_confirmed", True), ("notes", "User authorized proceeding without questions.")])
def test_metadata_recovers_after_closing_with_fresh_full_receipt(make_ws, key, value):
    ws = closed(make_ws)
    old = read_json(ws.root / "validation-manifest.json")
    query = (ws.root / "final-query.txt").read_bytes()
    rounds = {p.name: p.read_bytes() for p in deliver.round_paths(ws)}
    edit(ws, **{key: value})
    status = deliver.verify_delivery(ws)
    assert not status["ok"] and f"protocol.{key}" in status["error"]
    assert "run psb report again" in status["error"]
    # Reproduce the agent's unnecessary eval, too: it must preserve the review binding.
    ev = evaluate(ws)
    deliver.record_evaluation(ws, ev, note="metadata correction")
    ws.save_attempt(ev)
    assert deliver.report(ws)["ok"]
    assert deliver.verify_delivery(ws)["ok"]
    new = read_json(ws.root / "validation-manifest.json")
    assert new["input_sha256"] != old["input_sha256"]
    assert new["review_sha256"] == old["review_sha256"]
    assert (ws.root / "final-query.txt").read_bytes() == query
    assert {p.name: p.read_bytes() for p in deliver.round_paths(ws)} == rounds
    audit = (ws.root / "audit.md").read_text(encoding="utf-8")
    assert ("Scope confirmed by user: yes" if key == "scope_confirmed" else value) in audit
    with pytest.raises(WorkspaceError, match="closing round reviewed the current strategy"):
        deliver.critic_packet(ws)


def test_metadata_only_needs_report_without_an_extra_eval(make_ws):
    ws = closed(make_ws)
    edit(ws, notes="Corrected audit metadata")
    assert deliver.report(ws)["ok"]
    assert deliver.verify_delivery(ws)["ok"]


def test_correction_from_confirmed_to_unconfirmed_recovers(make_ws):
    ws = closed(make_ws)
    edit(ws, scope_confirmed=True)
    assert deliver.report(ws)["ok"]
    edit(ws, scope_confirmed=False)
    assert not deliver.verify_delivery(ws)["ok"]
    assert deliver.report(ws)["ok"]
    assert "Scope confirmed by user: no" in (ws.root / "audit.md").read_text(encoding="utf-8")


def test_metadata_correction_does_not_waive_technical_errors(make_ws, monkeypatch):
    from test_guardrails import add_issue
    ws = closed(make_ws)
    edit(ws, notes="Metadata correction")
    add_issue(ws.pubmed, monkeypatch, code="filter_value_not_found", severity="error")
    result = deliver.report(ws)
    assert not result["ok"] and "filter_value_not_found" in {b["code"] for b in result["blockers"]}


@pytest.mark.parametrize("section,value", [
    ("question", "Changed question"),
    ("eligibility", {"include": ["adults"], "exclude": []}),
    ("limits", [{"clause": "english[la]", "rationale": "requested"}]),
    ("concepts", [{"id": "asthma", "name": "Asthma", "role": "search", "rationale": "Different scope"}]),
    ("as_of", "2015-01-01"),
])
def test_substantive_protocol_change_keeps_review_stale(make_ws, section, value):
    ws = closed(make_ws)
    edit(ws, **{section: value})
    result = deliver.report(ws)
    assert not result["ok"] and "critic_stale" in {b["code"] for b in result["blockers"]}


def test_known_set_change_keeps_review_stale(make_ws):
    ws = closed(make_ws)
    ws.save_set("additional", "relevant", ["2"])
    assert "critic_stale" in {b["code"] for b in deliver.report(ws)["blockers"]}


def test_live_translation_change_still_needs_review(make_ws, monkeypatch):
    ws = closed(make_ws)
    edit(ws, notes="Metadata correction")
    search = ws.pubmed.search
    def changed(*args, **kwargs):
        result = search(*args, **kwargs)
        result["translation"] += " translated differently"
        return result
    monkeypatch.setattr(ws.pubmed, "search", changed)
    assert "critic_stale" in {b["code"] for b in deliver.report(ws)["blockers"]}


def test_metadata_edit_during_publication_fails_closed(make_ws, monkeypatch):
    ws = closed(make_ws)
    audit = deliver._audit
    def changed(*args):
        text = audit(*args)
        edit(ws, notes="Changed during publication")
        return text
    monkeypatch.setattr(deliver, "_audit", changed)
    assert "publication_failed" in {b["code"] for b in deliver.report(ws)["blockers"]}
    assert not deliver.verify_delivery(ws)["ok"]


def test_legacy_critic_hash_does_not_authorize_new_report(make_ws):
    ws = closed(make_ws)
    e = ws.attempts()[-1]["evaluation"]
    legacy = validation.digest({"inputs": e["input_sha256"], "query": e["query"],
        "issues": sorted(i["id"] for i in e["validation"]["issues"]),
        "translations": [(x.get("query"), x.get("translation")) for x in e.get("lines", [])],
        "translation": e.get("translation"),
        "vocabulary": validation.stable([{k:v for k,v in row.items() if k != "checked_at"} for row in e.get("vocabulary", [])]),
        "retrieved": e.get("retrieved_known", []), "present": e.get("known_in_pubmed", [])})
    path = ws.root / "critic/round-3.json"
    data = read_json(path)
    write_json(path, {**data, "review_sha256": legacy})
    assert "critic_stale" in {b["code"] for b in deliver.report(ws)["blockers"]}
    assert read_json(path)["review_sha256"] == legacy


def test_harness_requires_canonical_workspace_even_with_valid_nested_delivery(make_ws, tmp_path, monkeypatch):
    ws = closed(make_ws)
    run_dir = tmp_path / "isolated"
    nested = run_dir / "work/delivery"
    shutil.copytree(ws.root, nested)
    # Bind the fake client without changing the harness's workspace selection.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "evals"))
    import run
    from psb.workspace import Workspace
    def workspace(path):
        copy = Workspace(path)
        copy.pubmed = ws.pubmed
        return copy
    monkeypatch.setattr(run, "Workspace", workspace)
    assert deliver.verify_delivery(workspace(nested))["ok"]
    assert run.find_strategy_file(run_dir, require_protected=True) is None
