"""Crash recovery, structured repair evidence, budget enforcement and final receipts."""
import json

import pytest

from psb import allocation, deliver, holdout, miss_hunt, progress, reserved, semantic_repair, validation
from psb.workspace import WorkspaceError, read_json, write_json
from test_miss_hunt import Provider, evaluated, ready, work
from test_allocation import make_pool, through_critic


@pytest.mark.parametrize("stage", ["pending", "batch", "exposure", "receipt"])
def test_completion_recovers_without_duplicate_events(ready, monkeypatch, stage):
    ws, _ = ready
    provider = Provider({"topic": [work("2"), work("3")]})
    if stage == "batch":
        target, name = progress, "record_batch"
    elif stage == "exposure":
        target, name = reserved, "record"
    else:
        target, name = miss_hunt, "write_json"
    original = getattr(target, name)
    fired = False

    def crash(*args, **kwargs):
        nonlocal fired
        result = original(*args, **kwargs)
        matches = (stage in {"batch", "exposure"} or
                   str(args[0]).endswith("pending.json" if stage == "pending" else miss_hunt.RECEIPT))
        if matches and not fired:
            fired = True
            raise OSError("simulated process interruption after durable write")
        return result

    monkeypatch.setattr(target, name, crash)
    with pytest.raises(OSError):
        miss_hunt.run(ws, ["topic"], client=provider)
    monkeypatch.setattr(target, name, original)
    if stage == "receipt":
        assert miss_hunt.summary(ws)["performed"]
    else:
        miss_hunt.run(ws, ["topic"], client=provider)
    assert len(provider.calls) == 1
    assert len(progress.batches(ws)) == 1
    assert [e["pmid"] for e in reserved.events(ws)] == ["2", "3"]


def discover(ws):
    miss_hunt.run(ws, ["topic"], client=Provider({"topic": [work("2")]}))
    progress.record_screening(ws, include=["2"], evidence="abstract", reason="Meets criteria")
    ws.save_set("development", "development", ["2"], origin=["semantic-search"])


def decision(**changes):
    return {"pmid": "2", "diagnosis": "vocabulary", "disposition": "repair",
            "rationale": "Broader eligible concept", "general_concept": "Bronchospasm",
            "evidence": ["MeSH scope note and independent terminology evidence"], **changes}


def test_repair_requires_diagnosis_and_measures_new_material(ready):
    ws, pm = ready
    discover(ws)
    with pytest.raises(WorkspaceError, match="repair decisions"):
        semantic_repair.check_repair(ws)
    for invalid in ("", None, 123):
        with pytest.raises(WorkspaceError, match="general_concept"):
            semantic_repair.save_decisions(ws, {"decisions": [decision(general_concept=invalid)]})
    semantic_repair.save_decisions(ws, {"decisions": [decision()]})
    pm.atoms["bronchospasm[tiab]"] = {"2", "3", "4"}
    strategy = ws.strategy().to_dict()
    strategy["blocks"][0]["terms"].append("bronchospasm[tiab]")
    write_json(ws.root / "strategy.json", strategy)
    result = semantic_repair.check_repair(ws, sample_size=2)
    assert result["incremental_count"] == 3 and result["sample_pmids"] == ["3", "4"]
    assert result["confirmed_retrieved"] == ["2"]
    assert "semantic_screening_pending" in {i["code"] for i in semantic_repair.gate(ws)}
    progress.record_screening(ws, include=["3"], exclude=["4"], evidence="abstract")
    assert not semantic_repair.gate(ws)
    assert semantic_repair.summary(ws)["sample_outcomes"] == {"include": 1, "exclude": 1, "uncertain": 0}
    assert "Broader eligible concept" in "\n".join(semantic_repair.critic_lines(ws))
    before = len(progress.batches(ws)), len(reserved.events(ws))
    assert semantic_repair.check_repair(ws, sample_size=2) == {"ok": True, **result}
    assert before == (len(progress.batches(ws)), len(reserved.events(ws)))


def test_retained_miss_has_explicit_evidence_and_cannot_be_called_repaired(ready):
    ws, _ = ready
    discover(ws)
    semantic_repair.save_decisions(ws, {"decisions": [decision()]})
    semantic_repair.check_repair(ws)
    assert "semantic_repair_unretrieved" in {i["code"] for i in semantic_repair.gate(ws)}
    semantic_repair.save_decisions(ws, {"decisions": [decision(disposition="retain-miss", diagnosis="searchable-information")]})
    semantic_repair.check_repair(ws)
    assert not semantic_repair.gate(ws)


def test_shared_budget_covers_incremental_sample_and_rescreening_is_separate(ready):
    ws, pm = ready
    write_json(ws.root / "experiment-budget.json", {"limit": 2})
    discover(ws)
    semantic_repair.save_decisions(ws, {"decisions": [decision()]})
    pm.atoms["asthma[tiab]"] |= {"2", "3", "4"}
    # Change the Boolean query too: simulate a repair, not a provider snapshot change.
    pm.atoms["bronchospasm[tiab]"] = {"2", "3", "4"}
    pm.atoms["asthma[tiab]"] = {"1"}
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "a", "terms": ["asthma[tiab]", "bronchospasm[tiab]"]}]})
    result = semantic_repair.check_repair(ws)
    assert result["sample_limit"] == 1 and len(result["sample_pmids"]) == 1
    progress.record_screening(ws, exclude=result["sample_pmids"])
    progress.record_screening(ws, include=["2"], evidence="full-text")
    with pytest.raises(progress.ProgressError, match="shared candidate budget"):
        progress.record_screening(ws, include=["4"])


def test_delivery_binds_discovery_decisions_measurement_and_screening(make_ws):
    ws, pm = make_pool(make_ws)
    allocation.freeze(ws, choice="keep-holdout")
    evaluated(ws)
    pm.universe.add("998")
    miss_hunt.run(ws, ["topic"], client=Provider({"topic": [work("998")]}))
    progress.record_screening(ws, uncertain=["998"], evidence="abstract")
    semantic_repair.check_repair(ws)
    through_critic(ws)
    holdout.run(ws)
    assert deliver.report(ws)["ok"]
    assert deliver.verify_delivery(ws)["ok"]
    manifest = read_json(ws.root / "validation-manifest.json")
    assert manifest["semantic_evidence"]["check_sha256"]
    path = ws.root / semantic_repair.CHECK
    original = read_json(path)
    write_json(path, {**original, "incremental_count": 999})
    assert not deliver.verify_delivery(ws)["ok"]
    write_json(path, original)
    assert deliver.verify_delivery(ws)["ok"]
    progress.record_screening(ws, exclude=["998"], evidence="full-text")
    assert not deliver.verify_delivery(ws)["ok"]


def test_ordinary_progress_does_not_invalidate_semantic_inputs(ready):
    ws, _ = ready
    discover(ws)
    before = validation.input_snapshot(ws)
    progress.record_batch(ws, "pilot", "unrelated accounting", ["7"], total=1)
    assert validation.input_snapshot(ws) == before


def test_incremental_journal_retry_and_stale_scope(ready, monkeypatch):
    ws, pm = ready
    discover(ws)
    semantic_repair.save_decisions(ws, {"decisions": [decision()]})
    pm.atoms["bronchospasm[tiab]"] = {"2", "3"}
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "a", "terms": ["asthma[tiab]", "bronchospasm[tiab]"]}]})
    original = semantic_repair.write_json

    def crash(path, data):
        if path.name == semantic_repair.CHECK:
            raise OSError("interrupted after journaling")
        return original(path, data)

    monkeypatch.setattr(semantic_repair, "write_json", crash)
    with pytest.raises(OSError):
        semantic_repair.check_repair(ws)
    before = len(progress.batches(ws)), len(reserved.events(ws)), len(pm.queries)
    monkeypatch.setattr(semantic_repair, "write_json", original)
    semantic_repair.check_repair(ws)
    assert before == (len(progress.batches(ws)), len(reserved.events(ws)), len(pm.queries))
    protocol = ws.protocol()
    protocol["question"] = "A changed scientific scope"
    write_json(ws.root / "protocol.json", protocol)
    assert "semantic_repair_stale" in {i["code"] for i in semantic_repair.gate(ws)}


def test_repair_count_error_cannot_be_recorded_as_zero(ready, monkeypatch):
    ws, pm = ready
    discover(ws)
    semantic_repair.save_decisions(ws, {"decisions": [decision(disposition="retain-miss")]})
    search = pm.search

    def rejected(query, **kwargs):
        result = search(query, **kwargs)
        if query == "(asthma[tiab])":
            return {**result, "count": 0, "issues": [{"severity": "error"}]}
        return result

    monkeypatch.setattr(pm, "search", rejected)
    with pytest.raises(WorkspaceError, match="retrieval count"):
        semantic_repair.check_repair(ws)
    assert not (ws.root / semantic_repair.CHECK).exists()
