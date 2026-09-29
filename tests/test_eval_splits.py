"""Dev/held-out splits, provenance, run status and the versioned report."""

import argparse
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "evals"))

import harness  # noqa: E402
import run  # noqa: E402

FIXTURE = {"id": "T1", "question": "Asthma in children?", "as_of": "2015-01-01", "seeds": ["1"],
           "gold_pmids": ["1", "2", "3", "4"]}


@pytest.fixture
def evals_dir(tmp_path, monkeypatch):
    """A private copy of the harness's on-disk layout: fixtures, results, splits and ledger."""
    fixtures = tmp_path / "fixtures" / "suite"
    fixtures.mkdir(parents=True)
    for topic in ("T1", "T2", "T3"):
        (fixtures / f"{topic}.json").write_text(json.dumps({**FIXTURE, "id": topic}), encoding="utf-8")
    monkeypatch.setattr(harness, "FIXTURES", tmp_path / "fixtures")
    monkeypatch.setattr(harness, "RESULTS", tmp_path / "results")
    monkeypatch.setattr(harness, "EVALS", tmp_path)
    monkeypatch.setattr(harness, "SPLITS", tmp_path / "splits.json")
    monkeypatch.setattr(harness, "HELDOUT_LEDGER", tmp_path / "heldout-ledger.jsonl")
    harness.SPLITS.write_text(json.dumps({"dev": ["T1"], "heldout": {}, "retired": {"T3": "broken gold"}}),
                              encoding="utf-8")
    return tmp_path


def test_repository_splits_cover_every_fixture_and_hold_frozen_hashes():
    splits = harness.load_splits()
    ids = {json.loads(p.read_text(encoding="utf-8"))["id"] for p in harness.fixture_paths()}
    assigned = set(splits["dev"]) | set(splits["heldout"]) | set(splits["retired"])
    assert ids <= assigned, f"fixtures in no split: {sorted(ids - assigned)}"
    assert not set(splits["dev"]) & set(splits["heldout"])
    for path in harness.fixture_paths():
        harness.load_fixture(str(path))  # raises if a frozen held-out fixture changed


def test_fixture_hash_ignores_key_order_and_private_keys():
    reordered = dict(reversed(list(FIXTURE.items())))
    assert harness.fixture_hash(FIXTURE) == harness.fixture_hash({**reordered, "_path": "x"})
    assert harness.fixture_hash(FIXTURE) != harness.fixture_hash({**FIXTURE, "question": "Asthma?"})


def test_guard_refuses_retired_unassigned_and_unflagged_heldout(evals_dir):
    assert run.guard_topic(harness.load_fixture("T1"), allow_heldout=False) == "dev"
    with pytest.raises(SystemExit, match="retired"):
        run.guard_topic(harness.load_fixture("T3"), allow_heldout=True)
    with pytest.raises(SystemExit, match="no split"):
        run.guard_topic(harness.load_fixture("T2"), allow_heldout=True)
    run.cmd_freeze(argparse.Namespace(topics=["T2"]))
    with pytest.raises(SystemExit, match="--heldout"):
        run.guard_topic(harness.load_fixture("T2"), allow_heldout=False)
    assert run.guard_topic(harness.load_fixture("T2"), allow_heldout=True) == "heldout"


def test_freeze_refuses_seen_or_assigned_topics_and_detects_later_edits(evals_dir):
    with pytest.raises(SystemExit, match="already dev"):
        run.cmd_freeze(argparse.Namespace(topics=["T1"]))
    (harness.RESULTS / "T2").mkdir(parents=True)
    (harness.RESULTS / "T2" / "naive-noseed.json").write_text("{}", encoding="utf-8")
    with pytest.raises(SystemExit, match="cannot be held out"):
        run.cmd_freeze(argparse.Namespace(topics=["T2"]))
    (harness.RESULTS / "T2" / "naive-noseed.json").unlink()
    run.cmd_freeze(argparse.Namespace(topics=["T2"]))
    assert harness.split_of("T2") == "heldout"
    path = harness.FIXTURES / "suite" / "T2.json"
    path.write_text(json.dumps({**FIXTURE, "id": "T2", "gold_pmids": ["1", "2"]}), encoding="utf-8")
    with pytest.raises(harness.HarnessError, match="changed after it was frozen"):
        harness.load_fixture("T2")


def test_heldout_cards_drop_misses_and_uses_are_logged(evals_dir):
    card = {"topic": "T2", "recall_percent": 50.0, "missed": ["3"], "final_message": "found 1 and 2", "count": 9}
    sealed = run.seal(card, "heldout")
    assert "missed" not in sealed and "final_message" not in sealed
    assert sealed["recall_percent"] == 50.0 and sealed["split"] == "heldout"
    assert run.seal(card, "dev")["missed"] == ["3"]
    harness.record_heldout_look({"topic": "T2", "command": "score"})
    entry = json.loads(harness.HELDOUT_LEDGER.read_text(encoding="utf-8").splitlines()[-1])
    assert entry["topic"] == "T2" and entry["at"]


def test_tree_hash_tracks_content_but_not_env_or_caches(tmp_path):
    (tmp_path / "scripts" / "__pycache__").mkdir(parents=True)
    (tmp_path / "SKILL.md").write_text("v1\n", encoding="utf-8")
    base = harness.tree_hash(tmp_path)
    (tmp_path / ".env").write_text("NCBI_EMAIL=a@b.c", encoding="utf-8")
    (tmp_path / "scripts" / "__pycache__" / "x.pyc").write_bytes(b"\0")
    assert harness.tree_hash(tmp_path) == base
    (tmp_path / "SKILL.md").write_bytes(b"v1\r\n")
    assert harness.tree_hash(tmp_path) == base  # a CRLF checkout is the same skill
    (tmp_path / "SKILL.md").write_text("v2\n", encoding="utf-8")
    assert harness.tree_hash(tmp_path) != base


@pytest.mark.parametrize("card, errors, expected", [
    ({"run": {"returncode": 1, "seconds": 9}}, "", "infra"),
    ({"run": {"returncode": 1, "seconds": 900}}, '{"type":"error","message":"You’ve hit your usage limit."}', "infra"),
    ({"run": {"returncode": 1, "seconds": 900}}, "", "no-delivery"),
    ({"run": {"returncode": 0, "seconds": 900}, "valid": False, "error": "no final_strategy.txt"}, "", "no-delivery"),
    ({"run": {"returncode": None, "seconds": 60, "timed_out": True}}, "", "timeout"),
    ({"run": {"returncode": 0, "seconds": 900}, "recall_percent": 90.0, "leakage": ["x"], "valid": False}, "", "leakage"),
    ({"run": {"returncode": 0, "seconds": 900}, "recall_percent": 90.0, "leakage": [], "valid": True},
     "rate limit hit once, then recovered", "ok"),
    ({"status": "infra", "recall_percent": None}, "", "infra"),
    ({"run": {"returncode": 1, "seconds": 169}, "workspace_started": False}, "", "infra"),
    ({"run": {"returncode": 1, "seconds": 169}, "workspace_started": True}, "", "no-delivery"),
])
def test_run_status(card, errors, expected):
    assert harness.run_status(card, errors) == expected


def card(topic, source, recall, count, scored, version=None, status=None, driver="codex"):
    c = {"topic": topic, "source": source, "driver": driver, "condition": "noseed", "scored": scored,
         "recall_percent": recall, "count": count, "valid": recall is not None,
         "run": {"returncode": 0 if recall is not None else 1, "seconds": 900 if recall is not None else 8}}
    if version:
        c["skill"] = {"hash": version * 64, "dirty": False}
    if status:
        c["status"] = status
    return c


def write_cards(cards):
    for i, c in enumerate(cards):
        run.save(c["topic"], f"card-{i}", c)


def test_report_shows_latest_version_pairs_topics_and_discounts_infra(evals_dir):
    harness.SPLITS.write_text(json.dumps({"dev": ["T1", "T2"], "heldout": {}, "retired": {"T3": "broken"}}),
                              encoding="utf-8")
    write_cards([
        card("T1", "generated:ours", 50.0, 100, "20260101T000000Z"),               # legacy: hidden by default
        card("T1", "generated:ours", 100.0, 500, "20260201T000000Z", version="a"),
        card("T1", "generated:ours", None, None, "20260201T010000Z", version="a"),  # quota failure
        card("T1", "generated:lean-optimal", 90.0, 100, "20260101T000000Z"),
        card("T2", "generated:ours", 80.0, 100, "20260201T000000Z", version="a"),
        card("T2", "generated:lean-optimal", 80.0, 100, "20260101T000000Z"),
        card("T3", "generated:ours", 10.0, 100, "20260201T000000Z", version="a"),
        {"topic": "T1", "source": "naive", "condition": "noseed", "recall_percent": 40.0, "count": 50, "scored": "x"},
    ])
    run.cmd_report(argparse.Namespace(all_versions=False, pair=["generated:ours", "generated:lean-optimal"]))
    text = (evals_dir / "RESULTS.md").read_text(encoding="utf-8")
    assert "## Development topics" in text and "## Retired topics" in text and "- T3: broken" in text
    assert "1 win, 1 tie, 0 loss" in text and "1 topic(s) where A returns more than 2×" in text
    assert "| T1 | generated:ours (codex) | noseed | aaaaaaaaaa | 1/1 +1 infra † | 100.0 |" in text
    assert "| 50.0 |" not in text and "| naive | noseed | baseline |" in text
    assert "T3 | generated:ours" not in text
    run.cmd_report(argparse.Namespace(all_versions=True, pair=["generated:ours", "generated:lean-optimal"]))
    assert "| T1 | generated:ours (codex) | noseed | legacy | 1/1 † | 50.0 |" in (evals_dir / "RESULTS.md").read_text(encoding="utf-8")
