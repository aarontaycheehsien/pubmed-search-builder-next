"""Optional concepts: measured as candidate blocks, sampled, decided, and gated over the budget."""

import pytest

from psb import deliver, optional
from psb.evaluate import evaluate
from psb.strategy import Strategy, StrategyError, lint
from psb.workspace import write_json

# 10 COVID records; 4 of them mention lifestyle. Known relevant: 1 and 2 (lifestyle), 5 (not).
ATOMS = {"covid*[tiab]": {str(i) for i in range(1, 11)}, "lifestyle[tiab]": {"1", "2", "3", "4", "50"}}
COVID = {"id": "covid", "name": "COVID-19", "terms": ["covid*[tiab]"]}
LIFESTYLE = {"id": "lifestyle", "name": "Lifestyle", "terms": ["lifestyle[tiab]"]}
CONCEPTS = [{"id": "covid", "name": "COVID-19", "role": "search", "category": False, "rationale": "exposure"},
            {"id": "lifestyle", "name": "Lifestyle", "role": "optional", "category": False, "rationale": "topic-defining outcome"}]


def build(make_ws, *, budget=5, candidates=True, depth="standard"):
    ws, fake = make_ws(ATOMS, records={str(i): {"pmid": str(i), "title": f"record {i}"} for i in range(1, 11)}, question="COVID and lifestyle?")
    protocol = ws.protocol()
    protocol.update(concepts=[dict(c) for c in CONCEPTS], workload_budget=budget, depth=depth)
    write_json(ws.root / "protocol.json", protocol)
    write_json(ws.root / "strategy.json", {"blocks": [COVID], "limits": [], **({"candidates": [LIFESTYLE]} if candidates else {})})
    ws.save_set("relevant", "relevant", ["1", "2", "5"])
    return ws, fake


def codes(evaluation):
    return {i["code"]: i for i in evaluation["validation"]["issues"]}


def test_candidates_are_measured_but_never_searched(make_ws):
    ws, _ = build(make_ws)
    evaluation = evaluate(ws)
    assert "lifestyle" not in evaluation["query"] and evaluation["count"] == 10
    row = evaluation["optional"][0]
    assert (row["placement"], row["count_without_block"], row["count_with_block"], row["reduction_percent"]) == ("candidate", 10, 4, 60.0)
    assert row["known_lost"] == ["5"] and row["known_lost_by_set"] == {"relevant": ["5"]}
    assert row["removed_count"] == 6 and "NOT (lifestyle[tiab])" in row["removed_query"]
    assert row["status"] == "undecided"


def test_over_budget_requires_a_decision_and_under_budget_does_not(make_ws):
    ws, _ = build(make_ws, budget=5)
    found = codes(evaluate(ws))
    assert found["optional_undecided"]["blocking"] and found["over_workload_budget"]["requires_review"]


def test_under_budget_measures_without_gating(make_ws, tmp_path):
    ws, _ = build(make_ws, budget=100)
    evaluation = evaluate(ws)
    assert evaluation["optional"][0]["count_with_block"] == 4
    assert not {"optional_undecided", "over_workload_budget"} & set(codes(evaluation))


def test_untested_optional_concept_blocks_over_budget(make_ws):
    ws, _ = build(make_ws, candidates=False)
    assert codes(evaluate(ws))["optional_untested"]["blocking"]


def test_sample_draws_only_removed_records_and_decide_binds_to_the_strategy(make_ws):
    ws, _ = build(make_ws)
    drawn = optional.sample(ws, "lifestyle", n=3)
    assert len(drawn["pmids"]) == 3 and set(drawn["pmids"]) <= {"5", "6", "7", "8", "9", "10"}
    result = optional.decide(ws, "lifestyle", choice="leave_out", reason="loses known record 5", screened=None, relevant=[])
    assert not result["moved"] and result["decision"]["loss_sample"]["screened"] == drawn["pmids"]
    evaluation = evaluate(ws)
    assert evaluation["optional"][0]["status"] == "current"
    assert "loss_sample_short" in codes(evaluation)  # 3 screened, 6 removed, 30 required -> 6 needed
    optional.sample(ws, "lifestyle", n=30)
    optional.decide(ws, "lifestyle", choice="leave_out", reason="loses known record 5", screened=None, relevant=["5"])
    found = codes(evaluate(ws))
    assert not {"loss_sample_short", "optional_undecided", "optional_decision_stale"} & set(found)
    covid = ws.strategy().blocks[0]
    write_json(ws.root / "strategy.json", {"blocks": [{**COVID, "terms": covid.terms + ["sars*[tiab]"]}], "candidates": [LIFESTYLE]})
    assert codes(evaluate(ws))["optional_decision_stale"]["blocking"]


def test_deciding_and_moves_the_block_and_flags_known_losses(make_ws):
    ws, _ = build(make_ws)
    optional.sample(ws, "lifestyle", n=30)
    result = optional.decide(ws, "lifestyle", choice="and", reason="halves the workload", screened=None, relevant=[])
    strategy = ws.strategy()
    assert result["moved"] and [b.id for b in strategy.blocks] == ["covid", "lifestyle"] and not strategy.candidates
    evaluation = evaluate(ws)
    assert "lifestyle[tiab]" in evaluation["query"] and evaluation["optional"][0]["status"] == "current"
    found = codes(evaluation)
    assert found["optional_and_loses_known"]["requires_review"] and found["optional_and_loses_known"]["pmids"] == ["5"]
    assert "screen_concept_searched" not in found


def test_a_decision_placed_against_its_choice_is_misplaced(make_ws):
    ws, _ = build(make_ws, budget=3)  # still over budget once the block is AND-ed (4 records)
    optional.sample(ws, "lifestyle", n=30)
    optional.decide(ws, "lifestyle", choice="and", reason="halves the workload", screened=None, relevant=[])
    protocol = ws.protocol()
    protocol["concepts"][1]["decision"]["choice"] = "leave_out"
    write_json(ws.root / "protocol.json", protocol)
    assert codes(evaluate(ws))["optional_decision_misplaced"]["blocking"]


def test_decide_rejects_relevant_records_that_were_not_screened(make_ws):
    ws, _ = build(make_ws)
    with pytest.raises(StrategyError, match="among the screened"):
        optional.decide(ws, "lifestyle", choice="leave_out", reason="x", screened=["6"], relevant=["7"])


def test_loss_sample_must_come_from_the_removed_records(make_ws):
    ws, _ = build(make_ws)
    optional.decide(ws, "lifestyle", choice="leave_out", reason="x", screened=["1", "2", "3", "4", "6", "7"], relevant=[])
    assert codes(evaluate(ws))["loss_sample_invalid"]["pmids"] == ["1", "2", "3", "4"]


def test_budget_defaults_by_depth_and_can_be_switched_off():
    assert optional.workload_budget({"depth": "standard"}) == 10_000
    assert optional.workload_budget({"depth": "thorough"}) == 20_000
    assert optional.workload_budget({"depth": "quick"}) is None
    assert optional.workload_budget({"depth": "standard", "workload_budget": None}) is None
    assert optional.workload_budget({"depth": "standard", "workload_budget": 500}) == 500


def test_strategy_round_trips_candidates_and_rejects_clashing_ids():
    data = {"blocks": [COVID], "combine": None, "limits": [], "candidates": [LIFESTYLE]}
    assert Strategy.from_dict(data).to_dict() == data
    assert "candidates" not in Strategy.from_dict({"blocks": [COVID]}).to_dict()
    clash = Strategy.from_dict({"blocks": [COVID], "candidates": [{**LIFESTYLE, "id": "covid"}]})
    assert any("duplicates" in e for e in clash.structural_errors())


def test_lint_flags_a_candidate_that_is_not_an_optional_concept():
    strategy = Strategy.from_dict({"blocks": [COVID], "candidates": [LIFESTYLE]})
    issues = lint(strategy, concepts=[CONCEPTS[0]])
    assert "candidate_without_optional_concept" in {i["code"] for i in issues}


def test_audit_and_packet_show_the_tested_optional_concepts(make_ws):
    ws, _ = build(make_ws, budget=100)
    optional.sample(ws, "lifestyle", n=30)
    optional.decide(ws, "lifestyle", choice="leave_out", reason="loses known record 5", screened=None, relevant=[])
    evaluation = evaluate(ws)
    deliver.record_evaluation(ws, evaluation, note="first")
    ws.save_attempt(evaluation)
    packet = deliver.critic_packet(ws).read_text(encoding="utf-8")
    assert "### Tested optional concepts" in packet
    assert "| Lifestyle | left out | 10 / 4 | 60.0% | 5 | 0/6 (up to 39% of removed records could be relevant) | loses known record 5 |" in packet


def test_draw_samples_beyond_the_esearch_window_through_date_bins():
    import datetime as dt
    import re

    class Big:
        """25,000 records spread evenly over Entrez dates 1990-2020."""
        as_of = "2020-12-31"
        first, last = dt.date(1990, 1, 1), dt.date(2020, 12, 31)
        total = 25_000

        def span(self, query):
            dates = re.findall(r'"(\d{4}/\d{2}/\d{2})"\[edat\]', query)
            lo, hi = (dt.datetime.strptime(d, "%Y/%m/%d").date() for d in dates) if dates else (self.first, self.last)
            lo, hi = max(lo, self.first), min(hi, self.last)
            per_day = self.total / ((self.last - self.first).days + 1)
            return lo, hi, max(0, round(((hi - lo).days + 1) * per_day)) if hi >= lo else 0

        def count(self, query):
            return self.total

        def search(self, query, *, retmax=0, retstart=0, dated=True):
            lo, hi, n = self.span(query)
            return {"count": n, "pmids": [f"{lo:%Y%m%d}{retstart:05d}"] if retmax else []}

    drawn = optional.draw(Big(), "x[tiab]", 40, seed=3)
    assert drawn["count"] == 25_000 and len(drawn["pmids"]) == 40 and "bins" in drawn["frame"]
    years = sorted(int(p[:4]) for p in drawn["pmids"])
    assert years[0] < 2000 and years[-1] > 2010  # spread over the whole range, not the newest 9,999
