import json

from psb.evaluate import compare, evaluate
from psb.strategy import Strategy
from psb.workspace import write_json

ATOMS = {
    '"Asthma"[Mesh]': {"1", "2", "3"},
    "asthma*[tiab]": {"1", "2", "4"},
    '"Child"[Mesh]': {"1", "2", "5"},
    "child*[tiab]": {"1", "6"},
    "english[la]": {"1", "2", "4", "5", "6"},
}
BLOCKS = [
    {"id": "asthma", "name": "Asthma", "terms": ['"Asthma"[Mesh]', "asthma*[tiab]"]},
    {"id": "child", "name": "Children", "terms": ['"Child"[Mesh]', "child*[tiab]"]},
]


def setup(make_ws, blocks=BLOCKS, limits=None, sets=None):
    ws, fake = make_ws(ATOMS)
    write_json(ws.root / "strategy.json", {"blocks": blocks, "combine": None, "limits": limits or []})
    for name, (role, pmids) in (sets or {"seeds": ("seed", ["1", "3", "4", "99"])}).items():
        ws.save_set(name, role, pmids)
    return ws, fake


def test_counts_recall_and_failing_blocks(make_ws):
    ws, _ = setup(make_ws)
    result = evaluate(ws)
    assert result["ok"] and result["count"] == 2  # {1,2}
    seeds = result["sets"]["seeds"]
    assert seeds["not_in_pubmed"] == ["99"]
    assert (seeds["in_pubmed"], seeds["retrieved"], seeds["recall_percent"]) == (3, 1, 33.3)
    misses = {m["pmid"]: m["failing_blocks"] for m in result["misses"]}
    assert misses == {"3": ["child"], "4": ["child"]}
    assert result["block_recall"]["child"]["retrieved"] == 1
    counts = {l["text"]: l["count"] for l in result["lines"]}
    assert counts["#1 OR #2"] == 4 and counts["#3 AND #6"] == 2


def test_ablation_shows_what_each_block_costs(make_ws):
    ws, _ = setup(make_ws)
    ablation = {a["drop"]: a for a in evaluate(ws)["ablation"]}
    assert ablation["child"]["known_gained"] == 2 and ablation["child"]["gained_pmids"] == ["3", "4"]
    assert ablation["asthma"]["known_gained"] == 0


def test_limits_report_known_records_they_remove(make_ws):
    ws, _ = setup(make_ws, blocks=[BLOCKS[0]], limits=[{"clause": "english[la]", "rationale": "protocol"}])
    result = evaluate(ws)
    assert result["count"] == 3 and result["count_without_limits"] == 4
    assert [m for m in result["misses"] if m["lost_to_limits"]][0]["pmid"] == "3"


def test_structural_error_stops_before_any_search(make_ws):
    ws, fake = setup(make_ws, blocks=[{"id": "x", "terms": []}])
    result = evaluate(ws)
    assert result["ok"] is False and fake.queries == []


def test_compare_flags_lost_known_records_but_not_removed_ones(make_ws):
    ws, _ = setup(make_ws, blocks=[BLOCKS[0]])
    first = evaluate(ws)
    ws.save_version(first, "baseline")
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "asthma", "name": "", "terms": ['"Asthma"[Mesh]']}]})
    second = evaluate(ws)
    diff = compare(ws.versions()[-1], second, ws.strategy().to_dict())
    assert diff["regression"] and diff["known_lost"] == ["4"]
    assert diff["changes"]["asthma"]["terms_removed"] == ["asthma*[tiab]"]
    # Dropping record 4 from the set is a set edit, not a lost record.
    ws.save_set("seeds", "seed", ["1", "3"])
    third = evaluate(ws)
    assert compare(ws.versions()[-1], third, ws.strategy().to_dict())["known_lost"] == []


def test_no_sets_reports_recall_not_measured(make_ws):
    ws, _ = make_ws(ATOMS)
    write_json(ws.root / "strategy.json", {"blocks": BLOCKS})
    result = evaluate(ws)
    assert result["sets"] == {} and "recall not measured" in result["note"]


# -- optional blocks: what AND-ing a concept would do, measured without changing the query --------

from psb import validation  # noqa: E402
from psb.evaluate import loss_upper_bound  # noqa: E402
from psb.progress import record_batch  # noqa: E402

CHILD = {"id": "child", "name": "Children", "terms": ['"Child"[Mesh]', "child*[tiab]"]}


def optional_setup(make_ws, pmids=("1", "2", "3", "4"), optional=(CHILD,)):
    ws, fake = make_ws(ATOMS)
    write_json(ws.root / "strategy.json", {"blocks": [BLOCKS[0]], "combine": None, "limits": [], "optional": list(optional)})
    ws.save_set("seeds", "seed", list(pmids))
    return ws, fake


def test_optional_block_reports_count_and_known_records_lost(make_ws):
    ws, _ = optional_setup(make_ws)
    result = evaluate(ws)
    assert result["ok"] and result["count"] == 4  # the asthma block alone: the optional block is not searched
    assert "child" not in result["query"].lower()
    [row] = result["optional_blocks"]
    assert (row["id"], row["count_alone"], row["count_now"], row["count_if_added"], row["reduction_percent"]) == ("child", 4, 4, 2, 50.0)
    known = row["known"]
    assert known["retrieved_now"] == 4 and known["lost_if_added"] == ["3", "4"] and known["lost_by_set"] == {"seeds": ["3", "4"]}
    assert known["block_recall"] == {"retrieved": 2, "of": 4, "recall_percent": 50.0}
    assert "would lose 2 of the 4" in row["reading"]


def test_lossless_optional_block_on_few_records_is_not_called_safe(make_ws):
    ws, _ = optional_setup(make_ws, pmids=("1", "2"))
    [row] = evaluate(ws)["optional_blocks"]
    assert row["known"]["lost_if_added"] == [] and row["known"]["loss_upper_95_percent"] == 77.6
    assert "weak evidence: only 2 of them were found independently" in row["reading"] and "up to 77.6%" in row["reading"]


def test_optional_block_says_which_misses_it_would_have_matched(make_ws):
    ws, _ = optional_setup(make_ws, pmids=("1", "5"))  # 5 is about children, and the asthma block misses it
    [row] = evaluate(ws)["optional_blocks"]
    assert row["known"]["missed_now_but_in_block"] == ["5"]


def test_optional_block_bound_rests_on_records_no_keyword_search_led_to(make_ws):
    ws, _ = optional_setup(make_ws)
    record_batch(ws, "pilot", "Pilot search", ["1", "2"], total=2, query="asthma child")
    record_batch(ws, "neighbors:similar", "Similar articles", ["3"], total=1, origin=["1"])  # inherits the pilot's wording
    known = evaluate(ws)["optional_blocks"][0]["known"]
    assert known["by_route"] == {"independent": {"retrieved_now": 1, "lost_if_added": 1},  # 4: supplied, in no batch
                                 "keyword_derived": {"retrieved_now": 3, "lost_if_added": 1}}
    assert known["loss_upper_95_percent"] == 100.0


def test_lossless_optional_block_on_keyword_found_records_reports_the_loss_as_unmeasured(make_ws):
    ws, _ = optional_setup(make_ws, pmids=("1", "2"))
    record_batch(ws, "pilot", "Pilot search", ["1", "2"], total=2, query="asthma child")
    [row] = evaluate(ws)["optional_blocks"]
    assert row["known"]["lost_if_added"] == [] and row["known"]["loss_upper_95_percent"] is None
    assert "only 0 of them were found independently" in row["reading"] and "the loss is unmeasured" in row["reading"]
    ws.save_set("seeds", "seed", [str(n) for n in (1, 2)])
    record_batch(ws, "neighbors:refs", "Review references", ["1", "2"], total=2, origin=["9"])  # later batch: pilot still first
    assert evaluate(ws)["optional_blocks"][0]["known"]["by_route"]["independent"]["retrieved_now"] == 0


def test_optional_block_without_known_records_gives_counts_only(make_ws):
    ws, _ = make_ws(ATOMS)
    write_json(ws.root / "strategy.json", {"blocks": [BLOCKS[0]], "optional": [CHILD]})
    [row] = evaluate(ws)["optional_blocks"]
    assert row["count_if_added"] == 2 and "known" not in row and "count alone" in row["reading"]


def test_optional_blocks_do_not_change_the_query_or_the_review_binding(make_ws):
    plain, _ = make_ws(ATOMS)
    write_json(plain.root / "strategy.json", {"blocks": [BLOCKS[0]]})
    plain.save_set("seeds", "seed", ["1", "2", "3", "4"])
    before = evaluate(plain)
    assert "optional" not in before["inputs"]["strategy"] and "optional_blocks" not in before
    write_json(plain.root / "strategy.json", {"blocks": [BLOCKS[0]], "optional": [CHILD]})
    after = evaluate(plain)
    assert after["query"] == before["query"] and after["retrieved_known"] == before["retrieved_known"]
    assert after["input_sha256"] != before["input_sha256"]  # the optional block is an input: edit it, then re-evaluate
    # Its counts are not part of what the critic binds to: a count that moves does not make a review stale.
    moved = dict(after, optional_blocks=[dict(after["optional_blocks"][0], count_if_added=1)])
    assert validation.review_fingerprint(moved) == after["review_sha256"]


def test_optional_block_change_is_reported_since_previous(make_ws):
    ws, _ = optional_setup(make_ws, optional=())
    ws.save_version(evaluate(ws), "baseline")
    write_json(ws.root / "strategy.json", {"blocks": [BLOCKS[0]], "optional": [CHILD]})
    diff = compare(ws.versions()[-1], evaluate(ws), ws.strategy().to_dict())
    assert diff["changes"]["_optional"] == {"before": [], "after": ["child"]} and not diff["regression"]


def test_loss_upper_bound_matches_exact_binomial_values():
    assert loss_upper_bound(0, 10) == 25.9 and loss_upper_bound(0, 20) == 13.9 and loss_upper_bound(0, 30) == 9.5
    assert loss_upper_bound(1, 20) == 21.6 and loss_upper_bound(2, 50) == 12.1
    assert loss_upper_bound(0, 0) is None and loss_upper_bound(5, 5) == 100.0


def test_optional_block_that_pubmed_rejects_does_not_stop_the_evaluation(make_ws):
    from psb import deliver, progress
    from psb.ncbi import NcbiError

    ws, fake = optional_setup(make_ws)
    answer = fake.search

    def search(query, **kwargs):
        if "child" in query.lower():
            raise NcbiError("PubMed rejected the query")
        return answer(query, **kwargs)

    fake.search = search
    result = evaluate(ws)
    assert result["ok"] and result["validation"]["complete"] and result["count"] == 4
    [row] = result["optional_blocks"]
    assert row["error"] == "PubMed rejected the query" and row["reading"].startswith("Not measured")
    assert "not measured" in progress._optional_lines(result)[0]
    assert "| Children (child) | not measured | not measured | n/a | n/a | n/a |" in deliver._optional_table(result)
