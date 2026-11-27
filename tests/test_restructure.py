import pytest

from psb.restructure import RestructureError, replacement, restructure, title_form
from psb.strategy import Block
from psb.workspace import read_json, write_json

ATOMS = {
    '"Thing"[Mesh]': {"1", "2"},
    "thing[tiab]": {"1", "2", "3"},
    "generic[tiab]": {"1"} | {str(n) for n in range(4, 21)},
    "generic[ti]": {"6"},
    '"Qual"[Mesh]': {"1", "4"},
    "qual[tiab]": {"4", "5"},
    "qual[ti]": set(),
}
STRATEGY = {
    "blocks": [{"id": "thing", "name": "Thing", "terms": ['"Thing"[Mesh]', "thing[tiab]", "generic[tiab]"]}],
    "optional": [{"id": "q", "name": "Qualifier", "terms": ['"Qual"[Mesh]', "qual[tiab]"]},
                 {"id": "textonly", "name": "Text only", "terms": ["qual[tiab]"]}],
    "combine": None, "limits": [],
}


def setup(make_ws, seeds=("1", "2", "3")):
    ws, fake = make_ws(ATOMS)
    write_json(ws.root / "strategy.json", STRATEGY)
    if seeds:
        ws.save_set("seeds", "seed", list(seeds))
    return ws


def test_title_form_keeps_proximity():
    assert title_form("generic[tiab]") == "generic[ti]"
    assert title_form('"a b"[tiab:~2]') == '"a b"[ti:~2]'
    assert title_form('"Thing"[Mesh]') is None


def test_replacement_keeps_title_mentions_and_qualified_abstract_mentions():
    q = Block("q", "", ['"Qual"[Mesh]', "qual[tiab]"])
    assert replacement("generic[tiab]", q) == '(generic[ti] OR (generic[tiab] AND ("Qual"[Mesh] OR qual[tiab])))'
    assert replacement('"Thing"[Mesh]', q) == '("Thing"[Mesh] AND ("Qual"[Mesh] OR qual[tiab]))'


def test_restructures_a_noisy_term_and_refuses_one_that_loses_a_known_record(make_ws):
    ws = setup(make_ws)
    result = restructure(ws, "q", top=5)
    assert (result["count_before"], result["count_after"]) == (20, 6)  # {1,2,3} + title {6} + qualified {1,4,5}
    decisions = {row["term"]: row["decision"] for row in result["terms"]}
    assert decisions == {"generic[tiab]": "restructured", "thing[tiab]": "refused"}
    refused = next(r for r in result["terms"] if r["decision"] == "refused")
    assert refused["known_lost"] == ["3"]
    terms = read_json(ws.root / "strategy.json")["blocks"][0]["terms"]
    assert terms[1] == "thing[tiab]" and terms[2].startswith("(generic[ti] OR")


def test_dry_run_leaves_the_strategy_alone(make_ws):
    ws = setup(make_ws)
    restructure(ws, "q", dry_run=True)
    assert read_json(ws.root / "strategy.json")["blocks"][0]["terms"][2] == "generic[tiab]"


def test_qualifier_needs_mesh_and_text_words(make_ws):
    ws = setup(make_ws)
    with pytest.raises(RestructureError, match="MeSH"):
        restructure(ws, "textonly")
    with pytest.raises(RestructureError, match="no optional block"):
        restructure(ws, "missing")


def test_refuses_to_run_without_known_records(make_ws):
    ws = setup(make_ws, seeds=())
    with pytest.raises(RestructureError, match="no known record"):
        restructure(ws, "q")
