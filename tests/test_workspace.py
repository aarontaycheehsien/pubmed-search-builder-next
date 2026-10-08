import json
import os

import pytest

from psb import cli
from psb.workspace import Workspace, WorkspaceError, normalize_pmids


def test_normalize_pmids():
    assert normalize_pmids(["001", "2, 3", "1"]) == ["1", "2", "3"]
    with pytest.raises(WorkspaceError):
        normalize_pmids(["12a"])
    with pytest.raises(WorkspaceError):
        normalize_pmids(["000"])


def test_mining_uses_development_sets_only(tmp_path):
    ws = Workspace.create(tmp_path / "w", "Q")
    ws.save_set("seeds", "seed", ["1", "2", "3"])
    ws.save_set("found", "development", ["3", "4"], origin=["pilot-search"])
    out = ws.save_set("old", "validation", ["5"])
    assert out["purpose"] == "comparison" and out["overlap_with_other_purposes"] == {}
    assert ws.mining_pmids() == ["1", "2", "3", "4"]
    assert ws.mining_pmids(include_comparison=True) == ["1", "2", "3", "4", "5"]
    with pytest.raises(WorkspaceError):
        ws.save_set("x", "gold", ["1"])
    with pytest.raises(WorkspaceError, match="psb allocate"):
        ws.save_set("x", "holdout", ["1"])
    with pytest.raises(WorkspaceError, match="origin"):
        ws.save_set("x", "development", ["1"], origin=["web"])


def test_legacy_sets_are_mapped_on_read_and_never_rewritten(tmp_path):
    ws = Workspace.create(tmp_path / "w", "Q")
    raw = '{"role": "validation", "pmids": ["7"], "source": "split", "note": ""}\n'
    (ws.root / "sets" / "old.json").write_text(raw, encoding="utf-8")
    from psb.workspace import purpose_label, purpose_of
    data = ws.get_set("old")
    assert purpose_of(data) == "comparison"
    assert purpose_label(data) == "comparison (legacy: consulted during development as a validation set)"
    assert ws.mining_pmids() == []
    assert (ws.root / "sets" / "old.json").read_text(encoding="utf-8") == raw


def test_create_refuses_existing_workspace(tmp_path):
    Workspace.create(tmp_path / "w", "Q")
    with pytest.raises(WorkspaceError):
        Workspace.create(tmp_path / "w", "Q")


def run(capsys, *argv):
    code = cli.main(list(argv))
    return code, json.loads(capsys.readouterr().out)


def test_cli_offline_flow(tmp_path, capsys):
    root = str(tmp_path / "run")
    code, out = run(capsys, "init", root, "--question", "Asthma in children?")
    assert code == 0 and out["ok"]
    code, out = run(capsys, "--workspace", root, "set", "add", "seeds", "1", "2", "3", "4", "--role", "seed")
    assert out["pmids"] == ["1", "2", "3", "4"] and out["purpose"] == "development" and out["origin"] == ["user-supplied"]
    code, out = run(capsys, "--workspace", root, "set", "split", "seeds", "--fraction", "0.5", "--seed", "3")
    assert code == 1 and "psb allocate" in out["error"]
    code, out = run(capsys, "--workspace", root, "set", "add", "old", "9", "--purpose", "comparison")
    assert out["purpose"] == "comparison"
    strategy = {"blocks": [{"id": "asthma", "name": "Asthma", "terms": ['"Asthma"[Mesh]', "asthma*[tiab]"]}]}
    (tmp_path / "run" / "strategy.json").write_text(json.dumps(strategy), encoding="utf-8")
    code, out = run(capsys, "--workspace", root, "lint")
    assert code == 0 and out["lines"][-1]["text"] == "#1 OR #2"
    code, out = run(capsys, "--workspace", root, "status")
    assert "run psb eval" in out["todo"] and out["sets"]["old"]["purpose"] == "comparison"
    assert any("psb allocate" in t for t in out["todo"])
    code, out = run(capsys, "--workspace", root, "terms", "rank", "--set", "old")
    assert code == 1 and "comparison list" in out["error"]
    log = (tmp_path / "run" / "log.jsonl").read_text(encoding="utf-8")
    assert '"type": "command"' in log


def test_cli_reports_missing_workspace(tmp_path, capsys, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("PSB_WORKSPACE", raising=False)
    code, out = run(capsys, "status")
    assert code == 1 and "no workspace found" in out["error"]


def test_env_as_of_overrides_protocol(tmp_path, monkeypatch):
    ws = Workspace.create(tmp_path / "w", "Q")
    monkeypatch.setenv("PSB_AS_OF", "2015-06-30")
    assert ws.pubmed.as_of == "2015-06-30"


def test_log_entries_skips_a_line_torn_by_a_concurrent_writer(tmp_path):
    ws = Workspace.create(tmp_path / "w", "Q")
    ws.log({"type": "command", "argv": ["one"]})
    # Simulate two processes' single os.write calls landing back to back with no newline between
    # them, which tears the JSON on the shared boundary line.
    with (ws.root / "log.jsonl").open("a", encoding="utf-8") as handle:
        handle.write('{"ts": "x", "type": "ncbi", "para')
        handle.write('ms": {"term": "asthma"}}\n')
    ws.log({"type": "command", "argv": ["two"]})
    entries = ws.log_entries()
    assert [e["argv"] for e in entries if e.get("type") == "command"] == [["one"], ["two"]]


def test_log_write_is_one_os_level_call(tmp_path, monkeypatch):
    ws = Workspace.create(tmp_path / "w", "Q")
    calls = []
    real_write = os.write
    monkeypatch.setattr(os, "write", lambda fd, data: calls.append(data) or real_write(fd, data))
    ws.log({"type": "command", "argv": ["x"]})
    assert len(calls) == 1


def test_read_json_accepts_a_byte_order_mark(tmp_path):
    # Windows PowerShell's Out-File/Set-Content write UTF-8 with a BOM; an agent saving a critic
    # round that way must not turn a passing report into finalization_failed.
    from psb.workspace import read_json
    path = tmp_path / "round-1.json"
    path.write_bytes(b"\xef\xbb\xbf" + b'{"round": 1}')
    assert read_json(path) == {"round": 1}
