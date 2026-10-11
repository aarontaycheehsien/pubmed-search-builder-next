"""Evaluator-owned pairing receipts. Never stage these into the builder's workspace."""
from __future__ import annotations

import hashlib
import os
import shutil
from pathlib import Path

import harness
from psb import allocation, progress, validation
from psb.workspace import Workspace, read_json, write_json


def path_for(run_dir):
    key = hashlib.sha256(str(Path(run_dir).resolve()).encode()).hexdigest()
    return harness.EVALS / ".pairing" / f"{key}.json"


def start(run_dir, fixture, args, *, skill_hash, driver_version, checkpoint=None):
    data = {"version": 1, "fixture_sha256": harness.fixture_hash(fixture), "topic": fixture["id"],
            "as_of": fixture.get("as_of"), "condition": args.condition,
            "seeds": sorted(fixture.get("seeds") or []) if args.condition == "seeded" else [],
            "driver": args.driver, "driver_version": driver_version, "model": args.model,
            "effort": (args.effort or "medium") if args.driver == "codex" else None,
            "depth": args.depth, "screening_budget": progress.SCREEN_BUDGET[args.depth],
            "skill_hash": skill_hash, "checkpoint": checkpoint,
            "semantic_enabled": bool(getattr(args, "semantic_miss_hunt", False)), "status": "running"}
    write_json(path_for(run_dir), data)
    return data


def complete(run_dir, fixture, card):
    path = path_for(run_dir)
    data = read_json(path)
    work = Workspace(Path(run_dir) / "work")
    data.update(status=card["status"], leakage=card.get("leakage", []),
                semantic=card.get("semantic_miss_hunt", {"performed": False}),
                strategy_sha256=validation.digest(card.get("strategy")),
                screening_used=len(progress.decisions(work)),
                exposed_gold=sorted(harness.gold_exposed(fixture, Path(run_dir)), key=int))
    manifest = work.root / "validation-manifest.json"
    data["delivery_sha256"] = validation.digest(read_json(manifest)) if manifest.exists() else None
    data["experiment_status"] = ("incomplete" if data["semantic_enabled"] and not data["semantic"].get("performed")
                                 else "completed" if data["status"] == "ok" else "invalid")
    write_json(path, data)
    return data


def validate(run_dirs, fixture, condition):
    if len(run_dirs) != 2:
        raise harness.HarnessError("comparison requires exactly two runs")
    metadata = []
    for directory in run_dirs:
        path = path_for(directory)
        if not path.exists():
            raise harness.HarnessError("pairing metadata missing; legacy/manual runs cannot establish a matched experiment")
        data = read_json(path)
        if (data.get("version") != 1 or data.get("fixture_sha256") != harness.fixture_hash(fixture)
                or data.get("condition") != condition or data.get("as_of") != fixture.get("as_of")):
            raise harness.HarnessError("paired run has a different fixture, cutoff or seed condition")
        if data.get("status") != "ok" or data.get("leakage"):
            raise harness.HarnessError("paired runs must be valid completed deliveries without leakage")
        if data.get("semantic_enabled") and not data.get("semantic", {}).get("performed"):
            raise harness.HarnessError("semantic experiment is incomplete: enabled miss hunting did not finish")
        if not data.get("semantic_enabled") and data.get("semantic", {}).get("performed"):
            raise harness.HarnessError("control run unexpectedly performed semantic discovery")
        if not data.get("model"):
            raise harness.HarnessError("paired runs require an explicitly recorded model; an unknown default is not comparable")
        required = ("seeds", "driver", "driver_version", "effort", "depth", "screening_budget",
                    "screening_used", "skill_hash", "checkpoint", "semantic_enabled", "exposed_gold")
        if any(key not in data for key in required) or not data.get("driver_version") or not data.get("skill_hash"):
            raise harness.HarnessError("paired run has incomplete experiment metadata")
        if data.get("screening_used", 0) > data["screening_budget"]:
            raise harness.HarnessError("paired run exceeded the shared screening budget")
        manifest = Path(directory) / "work" / "validation-manifest.json"
        if not manifest.exists() or validation.digest(read_json(manifest)) != data.get("delivery_sha256"):
            raise harness.HarnessError("delivery no longer matches its evaluator-owned pairing receipt")
        query = (Path(directory) / "work" / "final-query.txt").read_text(encoding="utf-8")
        if validation.digest(" ".join(query.split())) != data.get("strategy_sha256"):
            raise harness.HarnessError("strategy no longer matches its scored run")
        metadata.append(data)
    a, b = metadata
    fields = ("as_of", "condition", "seeds", "driver", "driver_version", "model", "effort", "depth", "screening_budget", "skill_hash", "checkpoint")
    differing = [key for key in fields if a.get(key) != b.get(key)]
    if differing:
        raise harness.HarnessError("paired runs differ in " + ", ".join(differing))
    return metadata


def finish_checkpoint(run_dir, fixture, run_result):
    """Validate the evaluator's stop point without ever consulting gold retrieval."""
    path = path_for(run_dir)
    data = read_json(path)
    ws = Workspace(Path(run_dir) / "work")
    transcript = "\n".join(p.read_text(encoding="utf-8", errors="replace")
                           for p in (Path(run_dir) / "transcript.json", Path(run_dir) / "transcript.jsonl") if p.exists())
    if harness.leakage(fixture, Path(run_dir), transcript):
        raise harness.HarnessError("checkpoint failed the leakage check")
    previous = os.environ.get("PSB_AS_OF")
    try:
        if fixture.get("as_of"):
            os.environ["PSB_AS_OF"] = fixture["as_of"]
        versions = ws.versions()
        evaluation = versions[-1]["evaluation"] if versions else {}
        if (run_result.get("returncode") != 0 or run_result.get("timed_out") or ws.allocation() is None
                or not evaluation.get("ok") or not evaluation.get("validation", {}).get("complete")
                or allocation.state(ws)["stale"]
                or evaluation.get("input_sha256") != validation.digest(validation.input_snapshot(ws))):
            raise harness.HarnessError("checkpoint needs a successful current evaluation and frozen allocation")
        if (list((ws.root / "holdout").glob("*.json")) or list((ws.root / "critic").glob("round-*.json"))
                or (ws.root / "semantic-miss-hunt.json").exists()):
            raise harness.HarnessError("checkpoint must precede semantic discovery, critic and held-out test")
        remaining = data["screening_budget"] - len(progress.decisions(ws))
        if remaining < 30:
            raise harness.HarnessError("checkpoint must preserve at least 30 screenings for matched continuations")
        data.update(status="checkpoint", checkpoint=harness.tree_hash(ws.root), remaining_budget=remaining)
        write_json(path, data)
        return data
    finally:
        if previous is None:
            os.environ.pop("PSB_AS_OF", None)
        else:
            os.environ["PSB_AS_OF"] = previous


def restore_checkpoint(source, destination, fixture, args, *, skill_hash, driver_version):
    source = Path(source)
    metadata = read_json(path_for(source))
    expected = {"fixture_sha256": harness.fixture_hash(fixture), "condition": args.condition,
                "driver": args.driver, "model": args.model, "depth": args.depth,
                "effort": (args.effort or "medium") if args.driver == "codex" else None,
                "skill_hash": skill_hash, "driver_version": driver_version}
    if metadata.get("status") != "checkpoint" or any(metadata.get(k) != v for k, v in expected.items()):
        raise harness.HarnessError("checkpoint scope, model or skill differs from the requested continuation")
    if harness.tree_hash(source / "work") != metadata.get("checkpoint"):
        raise harness.HarnessError("checkpoint workspace changed after it was sealed")
    shutil.copytree(source / "work", Path(destination) / "work", dirs_exist_ok=True)
    return metadata["checkpoint"]
