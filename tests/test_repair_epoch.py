"""Repair after the held-out test: release, a fresh critic epoch, and no claim of an independent test."""

import json

import pytest

from psb import allocation, cli, deliver, holdout, interpret
from psb.evaluate import evaluate
from psb.workspace import WorkspaceError, read_json, write_json
from test_allocation import FULL, HELD, MESH_ONLY, make_pool, through_critic
from test_closing_round import PASS, write_round


def delivered_with_misses(make_ws):
    ws, fake = make_pool(make_ws, terms=MESH_ONLY)
    allocation.freeze(ws, choice="keep-holdout")
    through_critic(ws)
    write_round(ws, 2, [], PASS, closing=True)
    assert holdout.run(ws)["records"]["retrieved"] == 4
    assert deliver.report(ws)["ok"]
    return ws, fake


def repair_round(ws, number, *, closing=False):
    evaluation = ws.attempts()[-1]["evaluation"]
    data = {"round": number, "epoch": 2, **({"closing": True} if closing else {}),
            "strategy_version": evaluation.get("version"), "review_sha256": evaluation["review_sha256"],
            "domains": PASS, "findings": [],
            "issue_dispositions": [{"issue_id": i["id"], "status": "accepted-risk", "response": "Reviewed",
                                    "evidence": "Fixture"} for i in evaluation["validation"]["review_required"]]}
    write_json(ws.root / "critic" / f"round-{number}.json", data)


def test_release_returns_the_holdout_to_development_and_keeps_the_receipt(make_ws, capsys, monkeypatch):
    ws, _ = delivered_with_misses(make_ws)
    monkeypatch.setattr(cli, "workspace", lambda args: ws)
    assert cli.main(["holdout-release", "--reason", "repair the two missed records"]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["released"] == 6 and out["receipts_kept"] == [1]
    assert ws.reserved_pmids() == set() and set(HELD) <= ws.set_pmids("development")
    assert holdout.receipts(ws)[0]["records"]["retrieved"] == 4
    assert not deliver.verify_delivery(ws)["ok"]
    with pytest.raises(WorkspaceError, match="already released"):
        allocation.release(ws, "again")
    with pytest.raises(WorkspaceError, match="released for repair"):
        holdout.run(ws)


def test_the_repair_gets_its_own_critic_epoch_and_honest_wording(make_ws):
    ws, _ = delivered_with_misses(make_ws)
    allocation.release(ws, "repair the two missed records")
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "asthma", "name": "Asthma", "terms": FULL}]})
    evaluation = evaluate(ws)
    deliver.record_evaluation(ws, evaluation, note="repair")
    ws.save_attempt(evaluation)
    assert deliver.current_epoch(ws) == 2
    packet = deliver.critic_packet(ws).read_text(encoding="utf-8")
    assert "# Critic packet, round 3\n" in packet and '"epoch": 2' in packet and "**Repair review.**" in packet
    repair_round(ws, 3)
    assert deliver.next_round(ws, evaluation, deliver.critic_rounds(ws))[1] == "closing"  # one repair revision round
    result = deliver.report(ws)
    assert result["ok"], result
    manifest = read_json(ws.root / "validation-manifest.json")
    text = manifest["holdout"]["text"]
    assert manifest["holdout"]["case"] == "released" and "receipt" not in manifest["holdout"]
    assert interpret.TEXT["repaired"].format(r=4, x=6, id=1) in text
    assert interpret.TEXT["none"] in text
    assert "retrieved all" not in text and "6/6" not in text
    assert "- **Result:** The earlier query retrieved 4/6 held-out records (receipt 1); this query has no held-out test." in text


def test_rounds_cannot_go_back_or_ahead_of_the_epoch(make_ws):
    ws, _ = delivered_with_misses(make_ws)
    allocation.release(ws, "repair")
    evaluation = evaluate(ws)
    deliver.record_evaluation(ws, evaluation, note="repair")
    ws.save_attempt(evaluation)
    repair_round(ws, 3)
    write_json(ws.root / "critic" / "round-4.json", {**read_json(ws.root / "critic" / "round-3.json"), "round": 4, "epoch": 3})
    blockers = {b["code"] for b in deliver.review_gate(ws, evaluation)["blockers"]}
    assert "critic_invalid" in blockers
    write_json(ws.root / "critic" / "round-4.json", {**read_json(ws.root / "critic" / "round-3.json"), "round": 4, "epoch": 1})
    problems = deliver._closing_problems(deliver.critic_rounds(ws))
    assert (4, "a round cannot return to an earlier epoch") in problems
