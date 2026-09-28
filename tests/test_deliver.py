import json

import pytest

from psb import deliver
from psb.evaluate import evaluate
from psb.workspace import WorkspaceError, write_json

ATOMS = {'"Asthma"[Mesh]': {"1", "2"}, "asthma*[tiab]": {"1", "3"}}
STRATEGY = {"blocks": [{"id": "asthma", "name": "Asthma", "terms": ['"Asthma"[Mesh]', "asthma*[tiab]"]}], "limits": []}


def evaluated(make_ws):
    ws, _ = make_ws(ATOMS, question="Treatments for asthma?")
    protocol = ws.protocol()
    protocol["concepts"] = [{"id": "asthma", "name": "Asthma", "role": "search", "rationale": "topic anchor"}]
    write_json(ws.root / "protocol.json", protocol)
    write_json(ws.root / "strategy.json", STRATEGY)
    ws.save_set("seeds", "seed", ["1", "3", "4"])
    evaluation = evaluate(ws)
    deliver.record_evaluation(ws, evaluation, note="first")
    ws.save_attempt(evaluation)
    return ws


def test_packet_and_report_use_evaluated_numbers(make_ws):
    ws = evaluated(make_ws)
    packet = deliver.critic_packet(ws).read_text(encoding="utf-8")
    assert "Treatments for asthma?" in packet and "| 3 | `#1 OR #2` | 3 | none |" in packet
    round_file(ws, 1, [])
    result = deliver.report(ws)
    assert result["ok"], result
    audit = (ws.root / "audit.md").read_text(encoding="utf-8")
    assert "Total records: 3" in audit and "| seeds | seed" in audit and "Round 1 on version 1" in audit
    assert '("Asthma"[Mesh] OR asthma*[tiab])' in audit


def test_packet_leads_with_scope_and_translation_checks(make_ws):
    ws, _ = make_ws(ATOMS, question="Treatments for asthma?")
    protocol = ws.protocol()
    protocol["concepts"] = [{"id": "asthma", "name": "Asthma", "role": "search", "rationale": "topic anchor"}]
    protocol["eligibility"] = {"include": ["asthma of any type (allergic, exercise-induced)"], "exclude": []}
    write_json(ws.root / "protocol.json", protocol)
    write_json(ws.root / "strategy.json", STRATEGY)
    evaluation = evaluate(ws)
    deliver.record_evaluation(ws, evaluation, note="first")
    ws.save_attempt(evaluation)
    packet = deliver.critic_packet(ws).read_text(encoding="utf-8")
    scope = packet[packet.index("## Scope"):packet.index("| # | Search |")]
    assert "| Asthma | search | topic anchor |" in scope
    assert "- asthma of any type (allergic, exercise-induced)" in scope and "Eligibility (exclude)" not in scope
    assert "bare name" in scope and "direction" in scope


def test_report_refuses_stale_evaluation(make_ws):
    ws = evaluated(make_ws)
    round_file(ws, 1, [])
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "asthma", "terms": ["asthma*[tiab]"]}]})
    result = deliver.report(ws)
    assert not result["ok"] and "critic_stale" in {b["code"] for b in result["blockers"]}
    assert not (ws.root / "final-query.txt").exists()


def round_file(ws, number, findings, domains=None):
    evaluation = ws.attempts()[-1]["evaluation"]
    findings = [{"domain": "text_words", "finding": "A documented concern", **f} for f in findings]
    data = {"round": number, "strategy_version": 1, "review_sha256": evaluation["review_sha256"],
            "issue_dispositions": [{"issue_id": i["id"], "status": "accepted-risk", "response": "Reviewed the scope", "evidence": "Fixture topic requirements"} for i in evaluation["validation"]["review_required"]],
            "domains": domains or {d: {"verdict": "pass"} for d in deliver.DOMAINS}, "findings": findings}
    path = ws.root / "critic" / f"round-{number}.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


def test_check_round_enforces_verdicts_and_carries_open_findings(make_ws):
    ws = evaluated(make_ws)
    first = round_file(ws, 1, [{"id": "F1", "severity": "must-fix", "kind": "lexical", "status": "open"}])
    checked = deliver.check_round(ws, first)
    assert not checked["ok"] and checked["open_must_fix"] == ["F1"]
    second = round_file(ws, 2, [], domains={"translation": {"verdict": "pass"}})
    result = deliver.check_round(ws, second)
    assert not result["ok"]
    assert any(b["code"] == "critic_invalid" for b in result["blockers"])
    third = round_file(ws, 3, [{"id": "F1", "severity": "must-fix", "kind": "lexical", "status": "rejected"}])
    assert "needs a response" in json.dumps(deliver.check_round(ws, third))
