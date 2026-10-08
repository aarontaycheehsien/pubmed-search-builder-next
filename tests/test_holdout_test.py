"""The held-out test: preconditions, one receipt per binding, and delivery of the tested query unchanged."""

import json

import pytest

from psb import allocation, cli, deliver, holdout, interpret, progress, reserved
from psb.ncbi import NcbiError
from psb.workspace import WorkspaceError, read_json, write_json
from test_allocation import HELD, MESH_ONLY, make_pool, through_critic


def ready(make_ws, *, terms=None, choice="keep-holdout", **kwargs):
    ws, fake = make_pool(make_ws, **kwargs)
    allocation.freeze(ws, choice=choice)
    if terms:
        write_json(ws.root / "strategy.json", {"blocks": [{"id": "asthma", "name": "Asthma", "terms": terms}]})
    through_critic(ws)
    return ws, fake


def test_the_test_waits_for_the_allocation_evaluation_and_critic(make_ws):
    ws, _ = make_pool(make_ws)
    with pytest.raises(WorkspaceError, match="freeze the allocation"):
        holdout.run(ws)
    allocation.freeze(ws, choice="keep-holdout")
    with pytest.raises(WorkspaceError, match="run psb eval"):
        holdout.run(ws)
    from psb.evaluate import evaluate
    evaluation = evaluate(ws)
    deliver.record_evaluation(ws, evaluation)
    ws.save_attempt(evaluation)
    with pytest.raises(WorkspaceError, match="critic review .*critic_missing"):
        holdout.run(ws)


def test_no_holdout_means_no_test(make_ws):
    ws, _ = ready(make_ws, choice="all-development")
    with pytest.raises(WorkspaceError, match="no records are held out"):
        holdout.run(ws)


def test_all_retrieved_receipt_delivers_with_the_fixed_text(make_ws, capsys, monkeypatch):
    ws, _ = ready(make_ws)
    monkeypatch.setattr(cli, "workspace", lambda args: ws)
    assert cli.main(["holdout-test"]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["status"] == "complete" and out["receipt"] == 1
    receipt = holdout.receipts(ws)[0]
    assert receipt["records"] == {"eligible": 6, "retrieved": 6, "missed": [], "unavailable": []}
    assert receipt["studies"] == {"eligible": 6, "retrieved": 6} and receipt["distinct_studies"]
    text = out["interpretation"]
    assert "- **Result:** 6/6 eligible held-out records retrieved; 0 missed; studies 6/6." in text
    assert interpret.TEXT["all"].format(x=6) in text
    assert "about **73.5%** of the time" in text and interpret.TEXT["selection"] in text
    assert "- **Delivery and next step:** " + interpret.TEXT["delivered"] in text
    assert "Sources (units): prior-review 6. Screening: screened only in the separate context (evidence basis: abstract)." in text
    assert "Grouping: one record per study, verified. Exposure: none recorded." in text
    assert out["progress"]["text"] == "**PSB · Step 7/7 Deliver · Held-out test**\n" + text
    # A repeat returns the same receipt.
    assert cli.main(["holdout-test"]) == 0
    assert json.loads(capsys.readouterr().out)["repeat"] and len(holdout.receipts(ws)) == 1
    assert cli.main(["report"]) == 0
    capsys.readouterr()
    audit = (ws.root / "audit.md").read_text(encoding="utf-8")
    manifest = read_json(ws.root / "validation-manifest.json")
    assert text in audit and manifest["holdout"]["text"] == text and manifest["holdout"]["receipt"] == 1
    assert "| 103 | 103 | yes | prior-review | RCT 103 | Table 2 |" in audit
    assert cli.main(["progress", "deliver"]) == 0
    assert text in json.loads(capsys.readouterr().out)["progress"]["text"]
    assert deliver.verify_delivery(ws)["ok"]


def test_misses_are_delivered_unchanged_with_a_repair_offer(make_ws):
    ws, _ = ready(make_ws, terms=MESH_ONLY)
    receipt = holdout.run(ws)
    assert receipt["records"]["retrieved"] == 4 and receipt["records"]["missed"] == ["115", "118"]
    result = deliver.report(ws)
    assert result["ok"], result
    manifest = read_json(ws.root / "validation-manifest.json")
    text = manifest["holdout"]["text"]
    assert "- **Result:** 4/6 eligible held-out records retrieved; 2 missed; studies 4/6 (missed: PMIDs 115, 118)." in text
    assert interpret.TEXT["partial"].format(r=4, x=6, m=2) in text
    assert f"{interpret.TEXT['delivered']} {interpret.TEXT['repair_offer']}" in text
    assert "illustration" not in text and "would still retrieve" not in text
    # Holdout misses never became a mandatory critic review.
    evaluation = deliver.latest_evaluation(ws)
    missed = [i for i in evaluation["validation"]["review_required"] if i["code"] == "known_records_missed"]
    assert not {m["pmid"] for i in missed for m in i["evidence"]} & set(HELD)


def test_a_changed_strategy_cannot_claim_the_test(make_ws):
    ws, _ = ready(make_ws, terms=MESH_ONLY)
    holdout.run(ws)
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "asthma", "name": "Asthma",
                                                       "terms": ['"Asthma"[Mesh]', "asthma*[tiab]"]}]})
    through_critic(ws, number=2)
    with pytest.raises(WorkspaceError, match="psb holdout-release"):
        holdout.run(ws)
    assert "holdout_strategy_changed" in {b["code"] for b in deliver.report(ws)["blockers"]}


def test_the_report_needs_the_test(make_ws):
    ws, _ = ready(make_ws)
    assert "holdout_test_missing" in {b["code"] for b in deliver.report(ws)["blockers"]}


def test_an_incomplete_test_shows_no_counts_and_can_be_rerun(make_ws, monkeypatch):
    ws, fake = ready(make_ws)
    real = fake.among
    def failing(query, pmids):
        raise NcbiError("timeout")
    monkeypatch.setattr(fake, "among", failing)
    receipt = holdout.run(ws)
    assert receipt["status"] == "incomplete" and "records" not in receipt
    message = holdout.message(ws, receipt)["text"]
    assert "- **Result:** Not available: the PubMed check did not complete (timeout)." in message
    assert "Do not interpret this as zero recall or a successful test." in message
    monkeypatch.setattr(fake, "among", real)
    assert "holdout_test_incomplete" in {b["code"] for b in deliver.report(ws)["blockers"]}
    assert holdout.run(ws)["status"] == "complete"
    assert deliver.report(ws)["ok"]


def test_an_empty_denominator_delivers_with_its_fixed_wording(make_ws, monkeypatch):
    ws, fake = ready(make_ws)
    existing = fake.existing
    monkeypatch.setattr(fake, "existing", lambda pmids: existing(pmids) - set(HELD))
    receipt = holdout.run(ws)
    assert receipt["status"] == "empty" and receipt["records"]["eligible"] == 0
    monkeypatch.setattr(fake, "existing", existing)
    assert deliver.report(ws)["ok"]
    text = read_json(ws.root / "validation-manifest.json")["holdout"]["text"]
    assert ("No interpretable held-out retrieval result is available because **none of the held-out records is in "
            "PubMed by the effective date**.") in text


def test_exposure_after_the_reservation_qualifies_the_result(make_ws):
    ws, _ = ready(make_ws)
    reserved.record(ws, ["113"], "description", "declared", note="the user described it", declared=True)
    receipt = holdout.run(ws)
    assert receipt["exposure"] == [{"unit": "113", "reasons": ["PMID 113: description declared after the reservation"]}]
    text = holdout.message(ws, receipt)["text"]
    assert ("**Independence limitation:** unit 113 (PMID 113: description declared after the reservation). These "
            "results must not be described as an unexposed independent test.") in text
    assert "Exposure: 1 unit with recorded exposure." in text


def test_the_interpretation_drifts_only_with_a_new_binding(make_ws, monkeypatch):
    ws, _ = ready(make_ws)
    holdout.run(ws)
    monkeypatch.setattr(interpret, "TEMPLATE_VERSION", "2")
    assert "holdout_test_stale" in {b["code"] for b in deliver.report(ws)["blockers"]}
    assert holdout.run(ws)["number"] == 2
    assert deliver.report(ws)["ok"]
