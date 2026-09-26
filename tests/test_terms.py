from conftest import FakePubMed, record

from psb import terms
from psb.strategy import Strategy

STRATEGY = Strategy.from_dict({"blocks": [{"id": "c", "name": "", "terms": [
    '"Vesico-Ureteral Reflux"[Mesh]', "urinary tract infection*[tiab]", "UTI[tiab] OR UTIs[tiab]"]}]})


def test_coverage_is_truncation_and_hyphen_aware():
    memo = {}
    assert terms.covered("urinary tract infections", "tiab", STRATEGY, memo)
    assert terms.covered("urinary-tract infection", "tiab", STRATEGY, memo)
    assert terms.covered("UTIs", "tiab", STRATEGY, memo)
    assert not terms.covered("urinary infection", "tiab", STRATEGY, memo)
    assert terms.covered("Vesico-Ureteral Reflux", "mesh", STRATEGY, memo)
    assert not terms.covered("Child", "mesh", STRATEGY, memo)


def test_noise_filters():
    assert terms.noise_reason("Humans", "mesh") == "non_topical"
    assert terms.noise_reason("results", "tiab") == "section_label"
    assert terms.noise_reason("95 ci", "tiab") == "statistical"
    assert terms.noise_reason("IL-6", "tiab") is None


RECORDS = [
    record("1", "Renal scarring after febrile urinary tract infection", "DMSA scintigraphy detects renal scarring.",
           ["Humans", "Vesico-Ureteral Reflux", "Radionuclide Imaging"]),
    record("2", "Renal scarring in children", "Voiding cystourethrography and DMSA scintigraphy compared.",
           ["Humans", "Radionuclide Imaging"]),
    record("3", "Unrelated title", "Nothing shared here at all.", ["Humans"]),
]


def test_rank_scores_uncovered_terms_with_lift():
    pm = FakePubMed({'"renal scarring"[tiab]': {str(i) for i in range(10)}, "DMSA[tiab]": {"1", "2"},
                     '"Radionuclide Imaging"[Mesh]': {"1", "2", "3"}})
    result = terms.rank(pm, RECORDS, STRATEGY, fields=["tiab", "mesh"], budget=10)
    scored = {r["term"].lower(): r for r in result["scored"]}
    assert "renal scarring" in scored and scored["renal scarring"]["df"] == 2
    assert scored["renal scarring"]["lift"] is not None
    assert "humans" not in scored  # non-topical check tag
    assert all(not r["in_strategy"] for r in result["scored"])
    assert "urinary tract infection" not in scored  # already covered


def test_miss_report_lists_missing_vocabulary():
    evaluation = {"misses": [{"pmid": "2", "failing_blocks": ["c"], "lost_to_limits": False, "sets": ["seeds"]}]}
    [row] = terms.miss_report([RECORDS[1]], evaluation, STRATEGY)
    assert row["failing_blocks"] == ["c"]
    assert "Radionuclide Imaging" in row["mesh_not_in_strategy"] and "Humans" not in row["mesh_not_in_strategy"]
    assert any("dmsa scintigraphy" == t for t in row["text_not_in_strategy"])


def test_generic_terms_rank_after_distinctive_ones():
    pm = FakePubMed({})
    pm.count = lambda query: 3_000_000 if "scintigraphy" in query else 2
    result = terms.rank(pm, RECORDS, STRATEGY, fields=["tiab"], budget=40)
    order = [r["term"].lower() for r in result["scored"]]
    assert order.index("renal scarring") < order.index("scintigraphy")
    assert next(r for r in result["scored"] if r["term"].lower() == "scintigraphy")["generic"]
