import json

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
