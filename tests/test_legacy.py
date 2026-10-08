"""Workspaces from before held-out testing: readable, verifiable, never upgraded into an independent test."""

import json

from psb import allocation, deliver, progress, validation
from psb.evaluate import evaluate
from psb.workspace import read_json, write_json
from test_deliver import ATOMS, STRATEGY, round_file


def legacy(make_ws):
    """Role-labelled set files, as an earlier version of the skill wrote them."""
    ws, fake = make_ws(ATOMS, question="Treatments for asthma?")
    protocol = ws.protocol()
    protocol["concepts"] = [{"id": "asthma", "name": "Asthma", "role": "search", "rationale": "topic anchor"}]
    write_json(ws.root / "protocol.json", protocol)
    write_json(ws.root / "strategy.json", STRATEGY)
    (ws.root / "sets" / "seeds.json").write_text(json.dumps({"role": "seed", "pmids": ["1"]}), encoding="utf-8")
    (ws.root / "sets" / "validation.json").write_text(json.dumps({"role": "validation", "pmids": ["2", "3"]}), encoding="utf-8")
    return ws, fake


def test_a_legacy_workspace_needs_the_allocation_step_before_delivery(make_ws):
    ws, _ = legacy(make_ws)
    evaluation = evaluate(ws)
    deliver.record_evaluation(ws, evaluation)
    ws.save_attempt(evaluation)
    round_file(ws, 1, [])
    assert "allocation_missing" in {b["code"] for b in deliver.report(ws)["blockers"]}


def test_a_legacy_validation_set_is_a_comparison_list_not_a_test(make_ws):
    ws, _ = legacy(make_ws)
    allocation.freeze(ws)
    evaluation = evaluate(ws)
    deliver.record_evaluation(ws, evaluation)
    ws.save_attempt(evaluation)
    assert evaluation["sets"]["validation"]["purpose"] == "comparison"
    assert evaluation["sets"]["validation"]["label"] == \
        "comparison (legacy: consulted during development as a validation set)"
    round_file(ws, 1, [])
    assert deliver.report(ws)["ok"]
    text = read_json(ws.root / "validation-manifest.json")["holdout"]["text"]
    assert "- **validation:** 2/2 retrieved. These records were not screened into the allocation pool" in text
    assert "held-out records retrieved" not in text
    assert json.loads((ws.root / "sets" / "validation.json").read_text(encoding="utf-8")) == \
        {"role": "validation", "pmids": ["2", "3"]}


def test_a_policy_one_delivery_still_verifies_as_legacy(make_ws, monkeypatch):
    ws, _ = legacy(make_ws)
    allocation.freeze(ws)
    evaluation = evaluate(ws)
    deliver.record_evaluation(ws, evaluation)
    ws.save_attempt(evaluation)
    round_file(ws, 1, [])
    assert deliver.report(ws)["ok"]
    # Rewrite the receipt the way policy 1 bound it: no allocation in the inputs.
    (ws.root / "allocation.json").unlink()
    manifest = read_json(ws.root / "validation-manifest.json")
    manifest.update(policy_version="1", input_sha256=validation.digest(validation.input_snapshot_v1(ws)))
    manifest.pop("holdout")
    write_json(ws.root / "validation-manifest.json", manifest)
    result = deliver.verify_delivery(ws)
    assert result["ok"] and result["legacy"] and "predate held-out testing" in result["note"]
    message = progress.render(ws, "stage:deliver")["text"]
    assert "Legacy delivery (policy 1): its recall labels predate held-out testing." in message
    manifest["policy_version"] = "0"
    write_json(ws.root / "validation-manifest.json", manifest)
    assert not deliver.verify_delivery(ws)["ok"]
