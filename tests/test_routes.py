"""Known records by discovery route: retrieval by route in the Step 5 and Step 7 summaries, and how the known
records were found in the audit. Until the held-out test, routes that only the separate context gave are not
named (they would describe the searches that also found the held-out records); afterwards every route is."""

import json
import os

from psb import allocation, deliver, holdout, progress
from psb.evaluate import evaluate
from test_allocation import make_pool, through_critic
from test_closing_round import PASS, write_round
from test_deliver import evaluated

BUCKET = ("- Development retrieval by route: separate screening context 14/14 (routes of records found only in the "
          "separate context are named after the held-out test)")


def frozen(make_ws, *, via=None):
    """The 20-record pool screened in the separate context (origin prior-review), frozen with a holdout and
    evaluated; ``via`` adds a private candidate batch over the pool."""
    ws, fake = make_pool(make_ws)
    if via:
        progress.record_batch(ws, via, "private", [str(p) for p in range(101, 121)], total=20, private=True)
    allocation.freeze(ws, choice="keep-holdout")
    through_critic(ws)
    return ws, fake


def stage_line(ws, stage, start):
    return next((l for l in progress.render(ws, f"stage:{stage}")["text"].splitlines() if l.startswith(start)), None)


def test_routes_are_private_unless_the_builder_gave_them(make_ws):
    ws, _ = make_pool(make_ws)
    ws.save_set("seeds", "development", ["1"], origin=["user-supplied"])
    progress.record_batch(ws, "pilot", "Pilot search `x`", ["101"], total=1)  # the builder's own search
    progress.record_batch(ws, "neighbors:similar", "private", ["102"], total=1, private=True)
    with (ws.root / "candidates.jsonl").open("a", encoding="utf-8") as handle:  # a batch from before marking
        handle.write(json.dumps({"batch": "C3", "via": "neighbors:citedin", "label": "old", "pmids": ["103"]}) + "\n")
    found = allocation.routes(ws)
    assert found["1"] == {"user-supplied": False}
    assert found["101"] == {"pilot-search": False, "prior-review": True}  # the screener's own origin is private
    assert found["102"] == {"similar-articles": True, "prior-review": True}
    assert found["103"] == {"citation-forward": True, "prior-review": True}
    assert allocation._origins(ws) == {p: set(r) for p, r in found.items()}


def test_private_routes_are_one_bucket_until_the_held_out_test(make_ws):
    ws, _ = frozen(make_ws)
    assert not holdout.routes_disclosed(ws)
    assert stage_line(ws, "test", "- Development retrieval by route") == BUCKET
    holdout.run(ws)
    assert holdout.routes_disclosed(ws)
    assert stage_line(ws, "test", "- Development retrieval by route") == (
        "- Development retrieval by route: prior review 14/14 (a record found by several routes counts under each)")


def test_the_private_method_never_changes_the_text_before_the_test(make_ws, tmp_path):
    lines = []
    for name, via in (("a", "pilot"), ("b", "neighbors:similar")):
        ws, _ = frozen(make_ws, via=via)
        lines.append(progress.render(ws, "stage:test")["text"])
        os.rename(ws.root, tmp_path / name)  # make_ws reuses tmp_path / "run"
    assert lines[0] == lines[1] and BUCKET in lines[0]


def test_the_builders_own_routes_are_named_before_the_test(make_ws):
    ws, _ = make_pool(make_ws)
    ws.save_set("seeds", "development", ["101"], origin=["user-supplied"])  # exposed: goes to development
    allocation.freeze(ws, choice="keep-holdout")
    through_critic(ws)
    line = stage_line(ws, "test", "- Development retrieval by route")
    assert line.startswith("- Development retrieval by route: user-supplied 1/1 · separate screening context ")


def test_after_delivery_every_route_is_reported_and_the_diagnostic_stays_clean(make_ws):
    ws, fake = frozen(make_ws, via="pilot")
    result = deliver.report(ws)  # before the held-out test: a diagnostic only
    assert not result["ok"] and "How the known records were found" not in (ws.root / "diagnostic-audit.md").read_text(
        encoding="utf-8")
    write_round(ws, 2, [], PASS, closing=True)
    holdout.run(ws)
    assert deliver.report(ws)["ok"]
    audit = (ws.root / "audit.md").read_text(encoding="utf-8")
    assert ("| Route | Records | Screened | Eligible | Development retrieved | Held out retrieved |\n"
            "|---|---:|---:|---:|---:|---:|\n"
            "| prior review | 20 | 20 | 20 | 14/14 | 6/6 |\n"
            "| pilot search | 20 | 20 | 20 | 14/14 | 6/6 |") in audit
    final = progress.render(ws, "stage:deliver")["text"]
    assert "- Development retrieval by route: prior review 14/14 · pilot search 14/14" in final
    assert "- Held-out retrieval by route (units): prior review 6/6 · pilot search 6/6" in final
    assert deliver.verify_delivery(ws)["ok"]


def test_routes_are_presentation_only(make_ws):
    ws, _ = make_pool(make_ws)
    allocation.freeze(ws, choice="keep-holdout")
    before = evaluate(ws)
    progress.record_batch(ws, "pilot", "private", ["101", "102"], total=2, private=True)
    after = evaluate(ws)
    assert before["review_sha256"] == after["review_sha256"] and set(before) == set(after)
    assert "route" not in json.dumps(after)


def test_workspaces_without_routes_keep_their_messages(make_ws):
    ws = evaluated(make_ws)
    assert stage_line(ws, "test", "- Development retrieval by route") is None
