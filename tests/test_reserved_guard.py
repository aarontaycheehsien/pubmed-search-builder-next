"""The guard: held-out records stay out of the builder's view from the freeze until the test."""

import json
import re

import pytest

from psb import allocation, cli, deliver, progress, reserved, validation
from psb.evaluate import evaluate
from psb.workspace import write_json
from test_allocation import HELD, MESH_ONLY, make_pool, through_critic


@pytest.fixture
def frozen(make_ws, capsys, monkeypatch):
    ws, fake = make_pool(make_ws)
    allocation.freeze(ws, choice="keep-holdout")
    monkeypatch.setattr(cli, "workspace", lambda args: ws)
    return ws, fake


def run(capsys, *argv):
    code = cli.main(list(argv))
    return code, json.loads(capsys.readouterr().out)


def test_fetch_refuses_reserved_records_but_the_screener_store_is_private(frozen, capsys):
    ws, _ = frozen
    code, out = run(capsys, "fetch", "101", "103")
    assert code == 1 and "reserved for the held-out test" in out["error"] and "103" not in out["error"]
    assert not (ws.root / "records.jsonl").exists()
    code, out = run(capsys, "fetch", "103", "--screening", "--abstracts")
    assert code == 0 and out["records"][0]["pmid"] == "103"
    assert (ws.root / "screening" / "records.jsonl").exists() and not (ws.root / "records.jsonl").exists()
    assert reserved.events(ws) == []
    code, out = run(capsys, "fetch", "101")
    assert code == 0 and [e["pmid"] for e in reserved.events(ws)] == ["101"]


def test_samples_skip_reserved_records_and_keep_the_page_full(frozen, capsys):
    ws, _ = frozen
    code, out = run(capsys, "sample", "--purpose", "noise-check", "--n", "5", "asthma*[tiab]")
    shown = [r["pmid"] for r in out["records"]]
    assert code == 0 and len(shown) == 5 and not set(shown) & set(HELD)
    assert not {e["pmid"] for e in reserved.events(ws)} & set(HELD)
    code, out = run(capsys, "sample", "--screening", "--purpose", "pilot", "--n", "25", "asthma*[tiab]")
    assert set(HELD) <= {r["pmid"] for r in out["records"]}


@pytest.mark.parametrize("command", ["count", "sample"])
@pytest.mark.parametrize("query", ["103[uid]", "asthma*[tiab] AND 0103[pmid]", "(114)"])
def test_queries_naming_reserved_pmids_are_refused(frozen, capsys, command, query):
    code, out = run(capsys, command, query)
    assert code == 1 and "reveal whether the strategy retrieves it" in out["error"]


def test_neighbours_never_start_from_or_list_reserved_records(frozen, capsys):
    ws, fake = frozen
    fake._links = {("101", "similar"): [("103", 50), ("150", 40)]}
    code, out = run(capsys, "neighbors", "103")
    assert code == 1 and "reserved" in out["error"]
    code, out = run(capsys, "neighbors", "101")
    assert code == 0 and [r["pmid"] for r in out["rows"]] == ["150"]


def test_sets_cannot_take_reserved_records(frozen, capsys):
    code, out = run(capsys, "set", "add", "more", "103", "--purpose", "development")
    assert code == 1 and "reserved" in out["error"]
    code, out = run(capsys, "set", "add", "more", "103", "--purpose", "comparison")
    assert code == 1


def test_development_evidence_never_includes_the_holdout(frozen, capsys):
    ws, fake = frozen
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "asthma", "name": "Asthma", "terms": MESH_ONLY}]})
    evaluation = through_critic(ws)
    text = json.dumps(evaluation)
    assert not any(f'"{p}"' in text for p in HELD)
    assert {m["pmid"] for m in evaluation["misses"]} == {"116", "117", "119", "120"}
    missed = next(i for i in evaluation["validation"]["review_required"] if i["code"] == "known_records_missed")
    assert {m["pmid"] for m in missed["evidence"]} == {"116", "117", "119", "120"}
    packet = deliver.critic_packet(ws).read_text(encoding="utf-8")
    assert "6 units are reserved for one retrieval test" in packet
    assert not any(re.search(rf"(?<![0-9a-f]){p}(?![0-9a-f])", packet) for p in HELD)
    code, out = run(capsys, "terms", "miss")
    assert code == 0 and {m["pmid"] for m in out["misses"]} == {"116", "117", "119", "120"}
    code, out = run(capsys, "status")
    assert not any(f'"{p}"' in json.dumps(out) for p in HELD)


def test_held_out_retrieval_does_not_move_the_critic_binding(frozen):
    ws, fake = frozen
    first = evaluate(ws)
    fake.atoms["asthma*[tiab]"] -= {"115"}  # only a held-out record's retrieval changes
    second = evaluate(ws)
    assert first["review_sha256"] == second["review_sha256"]
    assert validation.input_snapshot(ws)["allocation"] == validation.digest(ws.allocation())


def test_builder_screening_of_a_reserved_record_is_recorded_as_exposure(frozen, capsys):
    ws, _ = frozen
    code, out = run(capsys, "screen", "--include", "113", "--reason", "seen in a journal alert")
    assert code == 0 and [(e["pmid"], e["kind"]) for e in reserved.events(ws)] == [("113", "screened")]


def test_mining_and_messages_never_reach_reserved_records(frozen, capsys):
    ws, _ = frozen
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "asthma", "name": "Asthma", "terms": MESH_ONLY}]})
    assert not set(ws.mining_pmids()) & set(HELD)
    code, out = run(capsys, "terms", "rank", "--budget", "0")
    assert code == 0 and out["records"] == 14
    for stage in ("known-records",):
        code, out = run(capsys, "progress", stage)
        assert not any(p in out["progress"]["text"] for p in HELD)
    assert not set(progress._included_unset(ws)) & set(HELD)


def test_separate_context_reasons_stay_private(make_ws):
    ws, _ = make_pool(make_ws)
    public = (ws.root / "screening.jsonl").read_text(encoding="utf-8")
    assert "RCT 103" not in public and "Table 2" not in public
    assert progress.private_decisions(ws)["103"] == {"pmid": "103", "decision": "include", "reason": "RCT 103",
                                                     "source_ref": "Table 2"}
    assert progress.decisions(ws)["103"]["context"] == "separate" and progress.decisions(ws)["103"]["private"]
