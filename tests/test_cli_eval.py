"""cmd_eval version-dedup behaviour: a repeated evaluation with the same result should not pad
the history, even when a --note is given (report --fresh always passes one)."""

import argparse

import pytest

from psb import cli
from psb.workspace import write_json

ATOMS = {'"Asthma"[Mesh]': {"1", "2"}, "asthma*[tiab]": {"1", "3"}}
STRATEGY = {"blocks": [{"id": "asthma", "name": "Asthma", "terms": ['"Asthma"[Mesh]', "asthma*[tiab]"]}], "limits": []}


def eval_args(note="", brief=True):
    return argparse.Namespace(note=note, no_term_counts=True, brief=brief)


@pytest.fixture
def ws(make_ws, monkeypatch):
    workspace, _ = make_ws(ATOMS, question="Asthma?")
    write_json(workspace.root / "strategy.json", STRATEGY)
    workspace.save_set("seeds", "seed", ["1", "2", "3"])
    monkeypatch.setattr(cli, "workspace", lambda args: workspace)
    return workspace


def test_repeated_note_only_call_does_not_duplicate_version(ws):
    first = cli.cmd_eval(eval_args())
    assert first["version"] == 1
    second = cli.cmd_eval(eval_args(note="final counts, run live"))
    assert second["version"] == 1 and "identical" in second["saved"]
    third = cli.cmd_eval(eval_args(note="final counts, run live"))
    assert third["version"] == 1 and len(ws.versions()) == 1


def test_a_real_change_still_saves_a_new_version(ws):
    cli.cmd_eval(eval_args())
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "asthma", "terms": ['"Asthma"[Mesh]']}]})
    changed = cli.cmd_eval(eval_args(note="final counts, run live"))
    assert changed["version"] == 2 and len(ws.versions()) == 2


def test_note_alone_still_saves_when_result_actually_differs(ws, monkeypatch):
    cli.cmd_eval(eval_args())
    # Same strategy text, but the live PubMed answer drifted (e.g. a record was reindexed).
    monkeypatch.setitem(ws.pubmed.atoms, ws.pubmed._key('"Asthma"[Mesh]'), {"1", "2", "9"})
    drifted = cli.cmd_eval(eval_args(note="final counts, run live"))
    assert drifted["version"] == 2
