from psb.strategy import (
    Strategy,
    block_query,
    core_query,
    full_query,
    lint,
    numbered_lines,
    untagged_segments,
    wrap_term,
)


def make(blocks, combine=None, limits=None):
    return Strategy.from_dict({"blocks": blocks, "combine": combine, "limits": limits or []})


TWO = [
    {"id": "condition", "name": "Reflux", "terms": ['"Vesico-Ureteral Reflux"[Mesh]', "vesicoureteral reflux*[tiab]"]},
    {"id": "test", "name": "DMSA", "terms": ['"Technetium Tc 99m Dimercaptosuccinic Acid"[Mesh]', "DMSA[tiab]"]},
]


def test_queries_and_ablation_render():
    strategy = make(TWO)
    assert core_query(strategy) == (
        '("Vesico-Ureteral Reflux"[Mesh] OR vesicoureteral reflux*[tiab]) AND '
        '("Technetium Tc 99m Dimercaptosuccinic Acid"[Mesh] OR DMSA[tiab])'
    )
    assert core_query(strategy, exclude="condition") == block_query(strategy.blocks[1])


def test_custom_combine_substitutes_block_ids_only():
    strategy = make(TWO + [{"id": "us", "name": "US", "terms": ["ultrasonograph*[tiab]"]}], combine="condition AND (test OR us)")
    query = core_query(strategy)
    assert query.startswith('("Vesico-Ureteral Reflux"[Mesh]')
    assert "AND ((" in query and "OR (ultrasonograph*[tiab]))" in query


def test_limits_render_not_and_and():
    strategy = make(TWO, limits=[{"clause": "NOT (animals[mh] NOT humans[mh])", "rationale": "human studies"},
                                 {"clause": "english[la]", "rationale": "protocol"}])
    assert full_query(strategy) == f"(({core_query(strategy)}) NOT ((animals[mh] NOT humans[mh]))) AND (english[la])"


def test_wrap_term_only_wraps_top_level_operators():
    assert wrap_term("a[tiab] OR b[tiab]") == "(a[tiab] OR b[tiab])"
    assert wrap_term('"a OR b"[tiab]') == '"a OR b"[tiab]'
    assert wrap_term("(a[tiab] OR b[tiab])") == "(a[tiab] OR b[tiab])"


def test_numbered_lines_reference_blocks():
    lines = numbered_lines(make(TWO, limits=[{"clause": "english[la]", "rationale": "x"}]))
    assert [l["text"] for l in lines] == [
        '"Vesico-Ureteral Reflux"[Mesh]', "vesicoureteral reflux*[tiab]", "#1 OR #2",
        '"Technetium Tc 99m Dimercaptosuccinic Acid"[Mesh]', "DMSA[tiab]", "#4 OR #5",
        "#3 AND #6", "#7 AND english[la]",
    ]


def test_structural_errors():
    strategy = make([{"id": "AND", "terms": []}, {"id": "x", "terms": ["a[tiab]"]}, {"id": "x", "terms": ["b[tiab]"]}], combine="x AND y")
    errors = " | ".join(strategy.structural_errors())
    assert "invalid block id 'AND'" in errors and "duplicate block id 'x'" in errors
    assert "has no terms" in errors and "unknown block ids: y" in errors


def codes(issues):
    return {i["code"] for i in issues}


def test_lint_catches_silent_failures():
    strategy = make([{"id": "a", "name": "", "terms": [
        "cat*[tiab]", "asthma and wheeze[tiab]", '"heart attack*"[tiab:~3]', 'foo[tiab] NOT bar[tiab]',
        "heart attack[tiab]", "heart attack[tiab]", '"Asthma/therapy"[Mesh]', "asthma[majr]", "foo[xyz]",
    ]}])
    found = codes(lint(strategy))
    assert {"short_truncation", "lowercase_operator", "proximity_wildcard", "not_operator",
            "duplicate", "subheading", "major_topic", "unknown_tag"} <= found


def test_multiword_tagged_run_is_not_untagged():
    assert untagged_segments("urinary tract infection*[tiab]") == []
    assert untagged_segments('asthma OR "wheeze"[tiab]') == ["asthma"]
    assert untagged_segments('"wheeze" asthma[tiab]') == ['"wheeze"']


def test_lint_layers_and_protocol_roles():
    strategy = make([{"id": "c", "name": "", "terms": ['"Asthma"[Mesh]']}, {"id": "o", "name": "", "terms": ["mortality[tiab]"]}])
    concepts = [{"id": "c", "role": "search"}, {"id": "o", "role": "screen"}, {"id": "p", "role": "search"}]
    found = codes(lint(strategy, concepts=concepts))
    assert {"no_text_layer", "no_mesh_layer", "screen_concept_searched", "concept_without_block"} <= found


def test_limit_without_rationale():
    assert "limit_without_rationale" in codes(lint(make(TWO, limits=[{"clause": "english[la]"}])))
