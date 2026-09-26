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
    ws.save_version(evaluate(ws), "first")
    return ws


def test_packet_and_report_use_evaluated_numbers(make_ws):
    ws = evaluated(make_ws)
    packet = deliver.critic_packet(ws).read_text(encoding="utf-8")
    assert "Treatments for asthma?" in packet and "| 3 | `#1 OR #2` | 3 |" in packet
    audit = deliver.report(ws).read_text(encoding="utf-8")
    assert "Total records: 3" in audit and "| seeds | seed" in audit and "No critic round was run." in audit
    assert '("Asthma"[Mesh] OR asthma*[tiab])' in audit


def test_report_refuses_stale_evaluation(make_ws):
    ws = evaluated(make_ws)
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "asthma", "terms": ["asthma*[tiab]"]}]})
    with pytest.raises(WorkspaceError, match="changed since the last psb eval"):
        deliver.report(ws)


def round_file(ws, number, findings, domains=None):
    data = {"round": number, "strategy_version": 1,
            "domains": domains or {d: {"verdict": "pass"} for d in deliver.DOMAINS}, "findings": findings}
    path = ws.root / "critic" / f"round-{number}.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


def test_check_round_enforces_verdicts_and_carries_open_findings(make_ws):
    ws = evaluated(make_ws)
    first = round_file(ws, 1, [{"id": "F1", "severity": "must-fix", "kind": "lexical", "status": "open"}])
    assert deliver.check_round(ws, first) == {"ok": True, "problems": [], "open_must_fix": ["F1"]}
    second = round_file(ws, 2, [], domains={"translation": {"verdict": "pass"}})
    result = deliver.check_round(ws, second)
    assert not result["ok"]
    assert any("F1" in p for p in result["problems"]) and any("operators" in p for p in result["problems"])
    third = round_file(ws, 3, [{"id": "F1", "severity": "must-fix", "kind": "lexical", "status": "rejected"}])
    assert any("needs a response" in p for p in deliver.check_round(ws, third)["problems"])
