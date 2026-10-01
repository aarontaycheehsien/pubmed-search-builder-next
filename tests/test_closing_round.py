"""The closing critic round: the way out when the last revision round asks for changes."""

import json
import sys
from pathlib import Path

import pytest

from psb import deliver
from psb.evaluate import evaluate
from psb.workspace import WorkspaceError, write_json
from test_deliver import evaluated

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "evals"))
import harness  # noqa: E402

OPEN = {"id": "F1", "domain": "text_words", "severity": "must-fix", "kind": "lexical", "finding": "missing synonym", "status": "open"}
REVISE = {d: {"verdict": "revise" if d == "text_words" else "pass"} for d in deliver.DOMAINS}
PASS = {d: {"verdict": "pass"} for d in deliver.DOMAINS}


def write_round(ws, number, findings, domains, *, closing=False):
    evaluation = ws.attempts()[-1]["evaluation"]
    data = {"round": number, **({"closing": True} if closing else {}), "strategy_version": evaluation.get("version"),
            "review_sha256": evaluation["review_sha256"], "domains": domains, "findings": findings,
            "issue_dispositions": [{"issue_id": i["id"], "status": "accepted-risk", "response": "Reviewed",
                                    "evidence": "Fixture"} for i in evaluation["validation"]["review_required"]]}
    path = ws.root / "critic" / f"round-{number}.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


def revise_strategy(ws):
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "asthma", "name": "Asthma", "terms": [
        '"Asthma"[Mesh]', "asthma*[tiab]", "wheez*[tiab]"]}], "limits": []})
    evaluation = evaluate(ws)
    deliver.record_evaluation(ws, evaluation, note="answer F1")
    ws.save_attempt(evaluation)


def exhaust_revision_rounds(ws):
    """Standard depth: two revision rounds, the second still asking for changes."""
    write_round(ws, 1, [OPEN], REVISE)
    write_round(ws, 2, [OPEN], REVISE)
    revise_strategy(ws)  # the fix makes round 2 stale, with no revision round left


def test_last_revision_round_asking_for_changes_is_no_longer_a_dead_end(make_ws):
    ws = evaluated(make_ws)
    exhaust_revision_rounds(ws)
    assert "critic_stale" in {b["code"] for b in deliver.report(ws)["blockers"]}
    packet = deliver.critic_packet(ws).read_text(encoding="utf-8")
    assert "round 3 (closing)" in packet and '"closing": true' in packet
    write_round(ws, 3, [{**OPEN, "status": "resolved", "response": "wheez*[tiab] added in version 2"}], PASS, closing=True)
    assert deliver.check_round(ws, ws.root / "critic" / "round-3.json")["ok"]
    assert deliver.report(ws)["ok"]


def test_closing_round_cannot_raise_new_substantive_findings(make_ws):
    ws = evaluated(make_ws)
    exhaust_revision_rounds(ws)
    new = {"id": "F2", "domain": "operators", "severity": "should-fix", "kind": "structural", "finding": "new idea", "status": "open"}
    path = write_round(ws, 3, [{**OPEN, "status": "resolved", "response": "added"}, new], PASS, closing=True)
    checked = deliver.check_round(ws, path)
    assert not checked["ok"] and any("may only verify earlier findings" in str(b.get("evidence")) for b in checked["blockers"])
    write_round(ws, 3, [{**OPEN, "status": "resolved", "response": "added"}, {**new, "severity": "document"}], PASS, closing=True)
    assert deliver.check_round(ws, path)["ok"]


def test_closing_round_that_still_asks_for_revision_ends_in_diagnostic(make_ws):
    ws = evaluated(make_ws)
    exhaust_revision_rounds(ws)
    write_round(ws, 3, [OPEN], REVISE, closing=True)
    result = deliver.report(ws)
    assert not result["ok"] and {"critic_open", "critic_revise"} <= {b["code"] for b in result["blockers"]}
    with pytest.raises(WorkspaceError, match="closing round reviewed the current strategy"):
        deliver.critic_packet(ws)


def test_revision_rounds_beyond_the_budget_without_closing_are_blocked(make_ws):
    ws = evaluated(make_ws)
    for number in (1, 2, 3):
        write_round(ws, number, [], PASS)
    assert "critic_budget" in {b["code"] for b in deliver.report(ws)["blockers"]}


def test_closing_round_must_be_last(make_ws):
    ws = evaluated(make_ws)
    write_round(ws, 1, [], PASS, closing=True)
    write_round(ws, 2, [], PASS)
    assert "critic_invalid" in {b["code"] for b in deliver.report(ws)["blockers"]}


def test_harness_reads_the_query_and_blockers_of_a_diagnostic_handoff(make_ws, tmp_path):
    ws = evaluated(make_ws)
    result = deliver.report(ws)  # no critic round yet: refused, with a diagnostic handoff
    assert not result["ok"]
    run_dir = ws.root.parent
    (run_dir / "work").mkdir(exist_ok=True)
    (run_dir / "work" / "diagnostic-audit.md").write_text(
        (ws.root / "diagnostic-audit.md").read_text(encoding="utf-8"), encoding="utf-8")
    handoff = harness.diagnostic_handoff(run_dir)
    assert "asthma*[tiab]" in handoff["query"] and handoff["blockers"] == ["critic_missing"]
    assert harness.diagnostic_handoff(tmp_path / "nowhere") is None


def test_after_closing_only_must_fix_blocks(make_ws):
    ws = evaluated(make_ws)
    exhaust_revision_rounds(ws)
    should = {**OPEN, "severity": "should-fix", "kind": "reporting"}
    write_round(ws, 3, [should], REVISE, closing=True)
    assert deliver.report(ws)["ok"]
