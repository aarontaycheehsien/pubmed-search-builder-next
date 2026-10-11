"""Evaluator receipts enforce matching and keep checkpoint/exposure state sealed."""
import argparse
import shutil

import pytest

from psb.workspace import read_json, write_json
from test_eval_splits import FIXTURE, evals_dir
from test_miss_hunt import ready
import harness
import pairing
import run


def args(**changes):
    return argparse.Namespace(**{**dict(condition="noseed", driver="codex", model="test-model",
                                      effort=None, depth="standard", semantic_miss_hunt=False), **changes})


@pytest.fixture
def pair(evals_dir):
    directories = [evals_dir / "control", evals_dir / "semantic"]
    for index, directory in enumerate(directories):
        pairing.start(directory, FIXTURE, args(semantic_miss_hunt=bool(index)),
                      skill_hash="skill", driver_version="1")
        write_json(directory / "work" / "validation-manifest.json", {"test": True})
        (directory / "work" / "final-query.txt").write_text("asthma[tiab]\n", encoding="utf-8")
        pairing.complete(directory, FIXTURE, {"status": "ok", "strategy": "asthma[tiab]",
                                             "semantic_miss_hunt": {"performed": bool(index)}})
    return directories


def test_completed_pair_uses_frozen_exposures(pair):
    metadata = pairing.validate(pair, FIXTURE, "noseed")
    assert all(r["experiment_status"] == "completed" for r in metadata)
    # Post-delivery bookkeeping must not shrink the scored denominator.
    (pair[0] / "work" / "screening.jsonl").write_text('{"pmid":"2","decision":"include"}\n')
    assert pairing.validate(pair, FIXTURE, "noseed")[0]["exposed_gold"] == []


@pytest.mark.parametrize("field,value", [("model", "different"), ("driver", "claude"),
    ("driver_version", "2"), ("effort", "high"), ("depth", "thorough"),
    ("screening_budget", 400), ("seeds", ["1"]), ("checkpoint", "different"), ("skill_hash", "different")])
def test_mismatched_settings_rejected(pair, field, value):
    path = pairing.path_for(pair[1])
    write_json(path, {**read_json(path), field: value})
    with pytest.raises(harness.HarnessError, match=field):
        pairing.validate(pair, FIXTURE, "noseed")


@pytest.mark.parametrize("changes,message", [
    ({"model": None}, "explicitly recorded model"),
    ({"status": "timeout"}, "valid completed"),
    ({"leakage": ["gold exposed"]}, "without leakage"),
    ({"semantic": {"performed": False}}, "incomplete"),
    ({"semantic_enabled": False}, "control run"),
    ({"screening_used": 151}, "budget"),
    ({"fixture_sha256": "changed"}, "fixture"),
    ({"as_of": "2026-01-01"}, "cutoff"),
    ({"delivery_sha256": "changed"}, "delivery"),
    ({"strategy_sha256": "changed"}, "strategy"),
])
def test_invalid_pairs_rejected(pair, changes, message):
    path = pairing.path_for(pair[1])
    write_json(path, {**read_json(path), **changes})
    with pytest.raises(harness.HarnessError, match=message):
        pairing.validate(pair, FIXTURE, "noseed")


def test_missing_metadata_and_incomplete_treatment(pair):
    metadata = pairing.complete(pair[1], FIXTURE, {"status": "ok", "strategy": "asthma[tiab]"})
    assert metadata["experiment_status"] == "incomplete"
    pairing.path_for(pair[0]).unlink()
    with pytest.raises(harness.HarnessError, match="metadata missing"):
        pairing.validate(pair, FIXTURE, "noseed")


def test_report_excludes_incomplete_treatments():
    common = {"status": "ok", "recall_percent": 99, "count": 10, "semantic_miss_hunt_enabled": True,
              "semantic_miss_hunt": {"performed": False}, "experiment_status": "incomplete"}
    groups = {("topic", "generated:treatment", "noseed", "codex", "version"): [common],
              ("topic", "generated:control", "noseed", "codex", "version"): [
                  {"status": "ok", "recall_percent": 50, "count": 10}]}
    table = "\n".join(run.results_table(groups))
    assert "incomplete experiment" in table and "99" not in table
    assert run.paired_table(groups, "generated:treatment", "generated:control") == []


def test_checkpoint_sealing_restore_and_tampering(ready, evals_dir, monkeypatch):
    ws, _ = ready
    fixture = {**FIXTURE, "as_of": None}
    source = evals_dir / "checkpoint"
    shutil.copytree(ws.root, source / "work")
    ws.root = source / "work"
    monkeypatch.setattr(pairing, "Workspace", lambda path: ws)
    pairing.start(source, fixture, args(), skill_hash="skill", driver_version="1")
    result = pairing.finish_checkpoint(source, fixture, {"returncode": 0})
    assert result["remaining_budget"] == 150
    target = evals_dir / "continuation"
    assert pairing.restore_checkpoint(source, target, fixture, args(), skill_hash="skill", driver_version="1") == result["checkpoint"]
    assert harness.tree_hash(target / "work") == result["checkpoint"]
    with pytest.raises(harness.HarnessError, match="model or skill"):
        pairing.restore_checkpoint(source, target, fixture, args(model="other"), skill_hash="skill", driver_version="1")
    (ws.root / "strategy.json").write_text('{}')
    with pytest.raises(harness.HarnessError, match="changed after"):
        pairing.restore_checkpoint(source, target, fixture, args(), skill_hash="skill", driver_version="1")


def test_checkpoint_rejects_leakage_before_sealing(ready, evals_dir, monkeypatch):
    ws, _ = ready
    monkeypatch.setattr(pairing, "Workspace", lambda path: ws)
    source = evals_dir / "checkpoint"
    source.mkdir()
    pairing.start(source, FIXTURE, args(), skill_hash="skill", driver_version="1")
    (source / "transcript.json").write_text('"read evals/fixtures"')
    with pytest.raises(harness.HarnessError, match="leakage"):
        pairing.finish_checkpoint(source, FIXTURE, {"returncode": 0})
    assert read_json(pairing.path_for(source))["status"] == "running"
