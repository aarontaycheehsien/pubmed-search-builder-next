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
    assert result["sets"] == {} and "retrieval not measured" in result["note"]


def test_sets_carry_their_purpose_and_legacy_label(make_ws):
    ws, _ = setup(make_ws, sets={"seeds": ("seed", ["1", "3"]), "old": ("validation", ["4"])})
    result = evaluate(ws)
    assert result["sets"]["seeds"]["purpose"] == "development" and result["sets"]["seeds"]["label"] == "development"
    assert result["sets"]["old"]["purpose"] == "comparison"
