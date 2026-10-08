"""The fixed interpretation: every case, the rounding rules, and agreement with reporting.md."""

from pathlib import Path

import pytest

from psb import interpret

REPORTING = Path(__file__).resolve().parents[1] / "references" / "reporting.md"


def unit(pmid, members=None, *, grouping="verified", origins=("prior-review",), exposure=()):
    return {"id": pmid, "members": list(members or [pmid]), "grouping": grouping, "origins": list(origins),
            "contexts": ["separate"], "evidence": ["abstract"], "exposure": list(exposure)}


def state(held=(), development=3, *, n=None, choice="keep-holdout", reason=None, released=None):
    held = list(held)
    dev = [unit(str(900 + i)) for i in range(development)]
    return {"allocation": {"N": len(held) + development if n is None else n, "choice": choice, "reason": reason,
                           "created": "2026-10-01T00:00:00+00:00"},
            "held": held, "development": dev, "released": released, "late": [], "removed": {}}


def receipt(r, x, *, distinct=True, studies=True, exposure=None, missed=None, status="complete"):
    return {"number": 1, "status": status, "created": "2026-10-02T00:00:00+00:00",
            "binding": {"as_of": "2026-09-30"}, "distinct_studies": distinct,
            "records": {"eligible": x, "retrieved": r, "missed": missed or [str(500 + i) for i in range(x - r)],
                        "unavailable": []},
            "studies": {"eligible": x, "retrieved": r} if studies else None, "exposure": exposure or []}


def lines(result):
    return {label: next(l for l in result["text"].split("\n") if l.startswith(f"- **{label}:** "))
            .removeprefix(f"- **{label}:** ") for label in interpret.LABELS}


@pytest.mark.parametrize("x,expected", [(1, "95.0%"), (2, "90.3%"), (3, "85.7%"), (6, "73.5%"), (14, "48.8%"),
                                        (134, "0.1%"), (135, "<0.1%"), (300, "<0.1%")])
def test_the_illustration_rounds_half_up_and_floors_at_point_one(x, expected):
    assert interpret.percent(x) == expected


def test_three_of_three_gives_the_fixed_statement_with_eighty_five_point_seven():
    held = [unit("101"), unit("102"), unit("103")]
    result = interpret.render(state(held), receipt(3, 3))
    got = lines(result)
    assert result["case"] == "all"
    assert got["Allocation"] == "Development: 3 units (3 records); held-out test: 3 units (3 records); you kept the proposed holdout."
    assert got["Result"] == "3/3 eligible held-out records retrieved; 0 missed; studies 3/3."
    assert got["Interpretation"] == interpret.TEXT["all"].format(x=3)
    assert got["Size context"] == (
        "For scale only: a search that misses **5%** of relevant studies would still retrieve all **3** test studies "
        "about **85.7%** of the time, assuming independent, representative sampling. This is an illustration of the "
        "test's ability to detect misses, not an estimate of this search's actual recall. " + interpret.TEXT["selection"])
    assert got["Delivery and next step"] == interpret.TEXT["delivered"]
    assert "100% recall" not in result["text"] and "validation passed" not in result["text"]


def test_a_larger_all_retrieved_set_scales_the_illustration():
    held = [unit(str(100 + i)) for i in range(14)]
    assert "about **48.8%** of the time" in interpret.render(state(held), receipt(14, 14))["text"]


@pytest.mark.parametrize("held,kwargs", [
    ([unit("101", ["101", "102"]), unit("103")], {"distinct": False}),
    ([unit("101", grouping="unverified"), unit("103", grouping="unverified")], {"distinct": False, "studies": False}),
])
def test_the_illustration_is_omitted_without_verified_distinct_studies(held, kwargs):
    got = lines(interpret.render(state(held), receipt(3, 3, **kwargs)))
    assert got["Size context"] == f"{interpret.TEXT['omitted']} {interpret.TEXT['selection']}"


@pytest.mark.parametrize("r", [4, 0])
def test_partial_and_zero_retrieval_show_a_gap_and_offer_repair(r):
    held = [unit(str(100 + i)) for i in range(6)]
    result = interpret.render(state(held), receipt(r, 6))
    got = lines(result)
    assert result["case"] == "partial"
    assert got["Interpretation"] == interpret.TEXT["partial"].format(r=r, x=6, m=6 - r)
    assert got["Size context"] == interpret.TEXT["selection"]
    assert got["Delivery and next step"] == f"{interpret.TEXT['delivered']} {interpret.TEXT['repair_offer']}"
    assert f"{r}/6 eligible held-out records retrieved; {6 - r} missed" in got["Result"]


@pytest.mark.parametrize("reason,material", [
    ("small", "No holdout was proposed: fewer than 10 eligible units."),
    ("exposed", "No holdout was proposed: no unexposed units: every eligible record was seen by the builder."),
    ("quick", "No holdout was proposed: quick depth."),
])
def test_no_holdout_names_the_reason(reason, material):
    got = lines(interpret.render(state(choice=None, reason=reason)))
    assert got["Result"] == "No held-out test was performed."
    assert got["Test material and separation"] == material
    assert got["Interpretation"] == interpret.TEXT["none"]
    assert got["Size context"] == got["Delivery and next step"] == interpret.TEXT["not_applicable"]


def test_choosing_all_development_is_said_as_such():
    got = lines(interpret.render(state(choice="all-development")))
    assert got["Allocation"].endswith("held-out test: none; you chose to use every record for development.")
    assert got["Test material and separation"] == "You chose to use every record for development."


def test_no_eligible_records():
    got = lines(interpret.render(state(development=0, choice=None, reason="empty")))
    assert got["Allocation"] == "No eligible reference records."
    assert got["Interpretation"] == interpret.TEXT["no_records"]


@pytest.mark.parametrize("status,reason", [
    ("incomplete", "the PubMed check did not complete (timeout)"),
    ("empty", "none of the held-out records is in PubMed by the effective date"),
    (None, "the held-out test has not been run yet"),
])
def test_unavailable_results_are_never_zero_recall_or_success(status, reason):
    held = [unit("101")]
    test = {"number": 1, "status": status, "reason": reason, "binding": {}} if status else None
    got = lines(interpret.render(state(held), test))
    assert got["Interpretation"] == interpret.TEXT["unavailable"].format(reason=reason)
    assert got["Size context"] == interpret.TEXT["no_result"]


def test_compromised_exposure_is_qualified_and_counted():
    held = [unit("101", exposure=[{"pmid": "101", "reasons": ["abstract shown by psb fetch"]}]), unit("102")]
    test = receipt(2, 2, exposure=[{"unit": "101", "reasons": ["PMID 101: abstract shown by psb fetch"]}])
    result = interpret.render(state(held, choice="designated"), test)
    got = lines(result)
    assert got["Interpretation"].endswith(interpret.TEXT["exposure"].format(
        detail="unit 101 (PMID 101: abstract shown by psb fetch)"))
    assert "Exposure: 1 unit with recorded exposure." in got["Test material and separation"]
    assert got["Allocation"].endswith("your designated test set.")


def test_shared_vocabulary_origins_are_flagged():
    held = [unit("101", origins=["similar-articles"]), unit("102", origins=["pilot-search"]), unit("103")]
    got = lines(interpret.render(state(held), receipt(3, 3)))
    assert got["Test material and separation"].startswith(
        "Sources (units): prior-review 1, pilot-search 1, similar-articles 1 (2 units found by similar-articles or "
        "pilot searches, which share vocabulary with development records or the builder's queries).")


def test_comparison_lists_follow_the_six_lines():
    result = interpret.render(state(choice=None, reason="small"), comparison=[{"name": "old", "retrieved": 1, "in_pubmed": 2}])
    assert result["text"].split("\n")[-1] == "- " + interpret.TEXT["comparison"].format(name="old", r=1, x=2)


def test_a_repaired_query_never_claims_the_earlier_test():
    held = [unit(str(100 + i)) for i in range(6)]
    got = lines(interpret.render(state(held, released={"reason": "repair two misses"}), receipt(4, 6)))
    assert got["Allocation"] == ("Development: 9 units (9 records), including the 6 units formerly held out (you kept "
                                 "the proposed holdout; released for repair: repair two misses).")
    assert got["Interpretation"] == interpret.TEXT["none"]
    assert got["Delivery and next step"] == interpret.TEXT["repaired"].format(r=4, x=6, id=1)
    untested = lines(interpret.render(state(held, released={"reason": "user asked"})))
    assert untested["Delivery and next step"] == interpret.TEXT["released_untested"]


def test_reporting_md_quotes_every_template_verbatim():
    text = " ".join(REPORTING.read_text(encoding="utf-8").split())
    missing = [key for key, template in interpret.TEXT.items() if " ".join(template.split()) not in text]
    assert not missing, f"references/reporting.md does not quote: {missing}"
