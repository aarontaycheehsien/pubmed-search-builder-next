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


def test_mining_excludes_held_out_records(tmp_path):
    ws = Workspace.create(tmp_path / "w", "Q")
    ws.save_set("seeds", "seed", ["1", "2", "3"])
    ws.save_set("found", "relevant", ["3", "4"])
    out = ws.save_set("validation", "validation", ["2"])
    assert out["overlap_with_other_roles"] == {"seeds": ["2"]}
    assert ws.mining_pmids() == ["1", "3", "4"]
    with pytest.raises(WorkspaceError):
        ws.save_set("x", "gold", ["1"])


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
    assert out["pmids"] == ["1", "2", "3", "4"]
    code, out = run(capsys, "--workspace", root, "set", "split", "seeds", "--fraction", "0.5", "--seed", "3")
    assert out["development"] == 2 and out["validation"] == 2
    strategy = {"blocks": [{"id": "asthma", "name": "Asthma", "terms": ['"Asthma"[Mesh]', "asthma*[tiab]"]}]}
    (tmp_path / "run" / "strategy.json").write_text(json.dumps(strategy), encoding="utf-8")
    code, out = run(capsys, "--workspace", root, "lint")
    assert code == 0 and out["lines"][-1]["text"] == "#1 OR #2"
    code, out = run(capsys, "--workspace", root, "status")
    assert "run psb eval" in out["todo"] and out["sets"]["validation"]["role"] == "validation"
    code, out = run(capsys, "--workspace", root, "terms", "rank", "--set", "validation")
    assert code == 1 and "held out" in out["error"]
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
