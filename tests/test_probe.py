"""Category probes: records naming only a member of a category block."""

import pytest

from psb import deliver, probe
from psb.evaluate import evaluate
from psb.strategy import StrategyError
from psb.workspace import write_json

# Systematic reviews 1-12. The environment block finds 1-4. Reviews 5-8 name only an exposure
# (phthalate, arsenic); 9-12 are about something else.
ATOMS = {"systematic review*[tiab]": {str(i) for i in range(1, 13)}, "environment*[tiab]": {"1", "2", "3", "4"},
         "exposure*[tiab]": {"5", "6", "7", "8", "9"}, "phthalate*[tiab]": {"5", "6"}, "arsenic[tiab]": {"7", "8"}}
SR = {"id": "reviews", "name": "Systematic reviews", "terms": ["systematic review*[tiab]"]}
ENV = {"id": "env", "name": "Environmental health", "terms": ["environment*[tiab]"]}
CONCEPTS = [{"id": "reviews", "name": "Systematic reviews", "role": "search", "category": False, "rationale": "report type"},
            {"id": "env", "name": "Environmental health", "role": "search", "category": True, "rationale": "topic"}]


def build(make_ws, depth="standard"):
    ws, _ = make_ws(ATOMS, records={str(i): {"pmid": str(i), "title": f"review {i}"} for i in range(1, 13)})
    protocol = ws.protocol()
    protocol.update(concepts=[dict(c) for c in CONCEPTS], depth=depth, workload_budget=None)
    write_json(ws.root / "protocol.json", protocol)
    write_json(ws.root / "strategy.json", {"blocks": [SR, ENV], "limits": []})
    ws.save_set("seeds", "seed", ["1"])
    return ws


def codes(ws):
    return {i["code"] for i in evaluate(ws)["validation"]["issues"]}


def test_unprobed_category_blocks_delivery_at_standard(make_ws):
    assert "category_unprobed" in codes(build(make_ws))


def test_quick_depth_does_not_require_probes(make_ws):
    assert "category_unprobed" not in codes(build(make_ws, depth="quick"))


def test_probe_samples_what_the_block_misses_within_the_other_blocks(make_ws):
    ws = build(make_ws)
    drawn = probe.draw_probe(ws, "env", "exposure*[tiab]", n=30)
    assert drawn["outside_count"] == 5 and set(drawn["sample"]) == {"5", "6", "7", "8", "9"}
    assert "NOT (environment*[tiab])" in drawn["query"] and "systematic review*[tiab]" in drawn["query"]


def test_relevant_findings_must_be_known_and_force_another_probe(make_ws):
    ws = build(make_ws)
    probe.draw_probe(ws, "env", "exposure*[tiab]", n=30)
    with pytest.raises(StrategyError, match="known set"):
        probe.record_probe(ws, "env", ["5", "7"])
    ws.save_set("relevant", "relevant", ["5", "7"])
    probe.record_probe(ws, "env", ["5", "7"])
    evaluation = evaluate(ws)
    found = {i["code"] for i in evaluation["validation"]["issues"]}
    assert "category_probe_found_relevant" in found and "known_records_missed" in found
    # widen the block with the members the records named, then probe again
    write_json(ws.root / "strategy.json", {"blocks": [SR, {**ENV, "terms": ENV["terms"] + ["phthalate*[tiab]", "arsenic[tiab]"]}]})
    probe.draw_probe(ws, "env", "exposure*[tiab]", n=30)
    probe.record_probe(ws, "env", [])
    assert not {"category_probe_found_relevant", "category_unprobed", "known_records_missed"} & codes(ws)


def test_probe_stays_valid_while_the_block_only_grows(make_ws):
    ws = build(make_ws)
    probe.draw_probe(ws, "env", "exposure*[tiab]", n=30)
    probe.record_probe(ws, "env", [])
    write_json(ws.root / "strategy.json", {"blocks": [SR, {**ENV, "terms": ENV["terms"] + ["pollut*[tiab]"]}]})
    assert "category_probe_stale" not in codes(ws)
    write_json(ws.root / "strategy.json", {"blocks": [SR, {**ENV, "terms": ["pollut*[tiab]"]}]})
    assert "category_probe_stale" in codes(ws)


def test_spent_probe_budget_turns_into_a_review_item(make_ws):
    ws = build(make_ws)
    ws.save_set("relevant", "relevant", ["5", "7"])
    for _ in range(2):
        probe.draw_probe(ws, "env", "exposure*[tiab]", n=30)
        probe.record_probe(ws, "env", ["5"])
    issues = {i["code"]: i for i in evaluate(ws)["validation"]["issues"]}
    assert issues["category_probe_budget_spent"]["requires_review"] and "category_probe_found_relevant" not in issues


def test_packet_shows_the_probe_history(make_ws):
    ws = build(make_ws)
    probe.draw_probe(ws, "env", "exposure*[tiab]", n=30)
    probe.record_probe(ws, "env", [])
    evaluation = evaluate(ws)
    deliver.record_evaluation(ws, evaluation, note="first")
    ws.save_attempt(evaluation)
    packet = deliver.critic_packet(ws).read_text(encoding="utf-8")
    assert "### Category probes" in packet and "| Environmental health | 1 | `exposure*[tiab]` | 5 | 0/5 |" in packet


def test_every_searched_concept_must_declare_whether_it_is_a_category(make_ws):
    ws = build(make_ws)
    protocol = ws.protocol()
    del protocol["concepts"][0]["category"]
    write_json(ws.root / "protocol.json", protocol)
    issues = {i["code"]: i for i in evaluate(ws)["validation"]["issues"]}
    assert issues["category_undeclared"]["blocking"] and issues["category_undeclared"]["location"] == "concept:reviews"
