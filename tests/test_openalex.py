"""OpenAlex as a second source of known records: client, routes, tiers, frame sample, profile, audit."""

import json

import pytest

from conftest import FakeOpenAlex, record
from psb import cli, deliver, progress
from psb.cache import Cache
from psb.evaluate import evaluate
from psb.http import TransportError
from psb.openalex import OpenAlex, OpenAlexError, doi_of, normalise_id, pmid_of
from psb.progress import record_batch
from psb.workspace import write_json

ATOMS = {
    '"Asthma"[Mesh]': {"1", "2", "3", "5", "7"}, "asthma*[tiab]": {"1", "2", "4", "6", "8"},
    '"Child"[Mesh]': {"1", "2", "3", "4", "6"}, "child*[tiab]": {"5", "7", "8", "9"},
}
RECORDS = {str(p): record(str(p), f"Record {p}", "Asthma in children.") for p in range(1, 13)}
STRATEGY = {"blocks": [
    {"id": "asthma", "name": "Asthma", "terms": ['"Asthma"[Mesh]', "asthma*[tiab]"]},
    {"id": "child", "name": "Children", "terms": ['"Child"[Mesh]', "child*[tiab]"]},
], "combine": None, "limits": []}
WORKS = {
    "W100": {"pmid": "50", "title": "Asthma review", "type": "review", "refs": ["W1", "W2", "W3", "W90", "W91"]},
    "W200": {"doi": "10.9999/review", "title": "Asthma review in education", "type": "review", "refs": ["W5"]},
    "W300": {"pmid": "60", "title": "Commentary", "refs": []},
    "W1": {"pmid": "1", "topic": ("T1", "Paediatric asthma")},
    "W2": {"pmid": "2", "topic": ("T1", "Paediatric asthma")},
    "W3": {"pmid": "3", "topic": ("T1", "Paediatric asthma")},
    "W5": {"pmid": "5", "topic": ("T2", "School health")},
    "W6": {"pmid": "6", "topic": ("T2", "School health")},
    "W7": {"pmid": "7", "cites": ["W1"], "topic": ("T2", "School health")},
    "W8": {"pmid": "8", "cites": ["W6"], "topic": ("T2", "School health")},
    "W9": {"pmid": "9", "topic": ("T2", "School health")},
    "W90": {"doi": "10.1000/x"},
    "W91": {"title": "Grey report"},
}


@pytest.fixture
def ws(make_ws, monkeypatch):
    workspace, fake = make_ws(ATOMS, RECORDS)
    fake.doi_map = {"10.1000/x": "4"}
    workspace.openalex = FakeOpenAlex(WORKS)
    write_json(workspace.root / "strategy.json", STRATEGY)

    def opened(args):
        workspace.log({"type": "command", "argv": args.argv})
        return workspace

    monkeypatch.setattr(cli, "workspace", opened)
    return workspace


def psb(capsys, *argv):
    code = cli.main(list(argv))
    return code, json.loads(capsys.readouterr().out)


# -- client ---------------------------------------------------------------------------------------

def test_identifiers_normalise_to_openalex_paths():
    assert normalise_id("https://openalex.org/w123") == "W123"
    assert normalise_id("00123") == "pmid:123"
    assert normalise_id("https://doi.org/10.1000/ABC") == "doi:10.1000/abc"
    assert normalise_id("PMC456") == "pmcid:PMC456"
    with pytest.raises(OpenAlexError):
        normalise_id("not an id")
    work = {"ids": {"pmid": "https://pubmed.ncbi.nlm.nih.gov/0042"}, "doi": "https://doi.org/10.5555/Y"}
    assert pmid_of(work) == "42" and doi_of(work) == "10.5555/y"


class Transport:
    def __init__(self, bodies=(), error=None):
        self.bodies, self.error, self.calls = list(bodies), error, []

    def request(self, url, params, **kwargs):
        self.calls.append((url, dict(params), kwargs.get("headers")))
        if self.error:
            raise self.error
        return self.bodies.pop(0)


def page(*pmids):
    return json.dumps({"meta": {"count": len(pmids)}, "results": [
        {"id": f"https://openalex.org/W{p}", "ids": {"pmid": f"https://pubmed.ncbi.nlm.nih.gov/{p}"}} for p in pmids]}).encode()


def test_client_asks_in_chunks_caches_and_keeps_the_key_out_of_logs(tmp_path):
    log = []
    transport = Transport([page(*range(1, 51)), page(51, 52)])
    client = OpenAlex(cache=Cache(tmp_path), log=log.append, transport=transport, api_key="secret")
    pmids = [str(p) for p in range(1, 53)]
    assert len(client.by_pmids(pmids)) == 52
    assert [c[1]["filter"].count("|") for c in transport.calls] == [49, 1]
    assert transport.calls[0][2]["Authorization"] == "Bearer secret"
    assert client.by_pmids(pmids).keys() == {str(p) for p in range(1, 53)}  # served from the cache
    assert len(transport.calls) == 2
    assert [e["cache"] for e in log] == [False, False, True, True]
    assert "secret" not in json.dumps(log) and "secret" not in json.dumps([p.read_text() for p in tmp_path.rglob("*.json")])


def test_unknown_work_is_none_and_a_spent_budget_says_so():
    client = OpenAlex(transport=Transport(error=TransportError("HTTP 404 for x: not found", transient=False)), api_key="")
    assert client.work("pmid:1") is None
    client = OpenAlex(transport=Transport(error=TransportError("HTTP 429 for x: daily budget exhausted", transient=True)), api_key="")
    with pytest.raises(OpenAlexError, match="budget is used up"):
        client.work("pmid:1")


# -- reference lists: tier A ----------------------------------------------------------------------

def test_openalex_reference_list_maps_to_pmids_and_counts_as_independent(ws, capsys):
    code, out = psb(capsys, "neighbors", "50", "--links", "refs", "--source", "openalex")
    assert code == 0, out
    assert [r["pmid"] for r in out["rows"]] == ["1", "2", "3", "4"]  # 4 through the DOI and the PMC converter
    assert out["not_in_pubmed"]["count"] == 1 and out["not_in_pubmed"]["works"][0]["work"] == "W91"
    batch = progress.batches(ws)[-1]
    assert batch["via"] == "openalex:refs" and batch["origins"]["1"] == ["50"]
    text = out["progress"]["text"]
    assert "(OpenAlex)" in text and "no PMID" in text and "Reference lists (backward): 4" in text
    ws.save_set("benchmark", "benchmark", ["1", "2", "3", "4"])
    free = evaluate(ws)["known_without_keyword_search"]
    assert free["in_pubmed"] == 4 and free["held_out"]["in_pubmed"] == 4
    assert free["anchors"]["top"] == {"anchor": "50", "records": 4, "share_percent": 100.0}


def test_a_review_outside_pubmed_is_followed_by_its_doi(ws, capsys):
    code, out = psb(capsys, "neighbors", "10.9999/review", "--links", "refs", "--source", "openalex")
    assert code == 0 and [r["pmid"] for r in out["rows"]] == ["5"] and out["rows"][0]["from"] == ["W200"]


def test_a_missing_reference_list_is_not_read_as_no_references(ws, capsys):
    code, out = psb(capsys, "neighbors", "60", "--links", "refs", "--source", "openalex")
    assert code == 0 and out["no_reference_list"] == ["60"] and out["rows"] == []
    assert "not that the work has no references" in out["note"]


def test_pubmed_reference_list_miss_points_to_openalex(make_ws, monkeypatch, capsys):
    workspace, _ = make_ws(ATOMS, RECORDS, {("50", "refs"): []})
    monkeypatch.setattr(cli, "workspace", lambda args: workspace)
    code, out = psb(capsys, "neighbors", "50", "--links", "refs")
    assert code == 0 and "--source openalex" in out["note"]


# -- forward citations: tier B ----------------------------------------------------------------------

def test_forward_citations_of_independent_records_are_their_own_tier(ws):
    record_batch(ws, "openalex:refs", "refs", ["1"], total=1, origin=["50"], origins={"1": ["50"]})
    record_batch(ws, "pilot", "Pilot search", ["6"], total=1, query="asthma")
    record_batch(ws, "openalex:citedin", "citing", ["7"], total=1, origin=["1"], origins={"7": ["1"]})
    record_batch(ws, "openalex:citedin", "citing", ["8"], total=1, origin=["6"], origins={"8": ["6"]})
    ws.save_set("benchmark", "benchmark", ["1"])
    ws.save_set("relevant", "relevant", ["6"])
    ws.save_set("validation", "validation", ["7", "8"])
    result = evaluate(ws)
    assert result["known_without_keyword_search"]["in_pubmed"] == 1  # neither citing record joins tier A
    cited = result["known_from_citation_of_independent"]
    assert cited["in_pubmed"] == 1 and cited["held_out"] == {"in_pubmed": 1, "retrieved": 1}  # 7 only: 8 cites a pilot hit
    assert "not part of the recall bound" in cited["reading"]


# -- anchors --------------------------------------------------------------------------------------

def test_one_review_supplying_most_independent_records_is_flagged(ws):
    record_batch(ws, "neighbors:refs", "refs", ["1", "2", "3", "4", "5"], total=5, origin=["50"])
    record_batch(ws, "openalex:refs", "refs", ["6"], total=1, origin=["W200"])
    ws.save_set("benchmark", "benchmark", ["1", "2", "3", "4", "5", "6"])
    free = evaluate(ws)["known_without_keyword_search"]
    assert free["anchors"]["concentrated"] and free["anchors"]["top"]["share_percent"] == 83.3
    assert "second review" in free["reading"]
    assert "One review supplies 5 of the 6" in "\n".join(progress._free_recall({"sets": {"x": {}}, "known_without_keyword_search": free}))


def test_few_independent_records_are_not_called_concentrated(ws):
    record_batch(ws, "neighbors:refs", "refs", ["1", "2"], total=2, origin=["50"])
    ws.save_set("benchmark", "benchmark", ["1", "2"])
    assert not evaluate(ws)["known_without_keyword_search"]["anchors"]["concentrated"]


# -- frame sample -----------------------------------------------------------------------------------

def test_frame_sample_hides_retrieval_and_estimates_recall_only_when_complete(ws, capsys):
    code, out = psb(capsys, "sample", "--source", "openalex", "--purpose", "frame", "--topic", "T2", "--n", "5")
    assert code == 0, out
    sampled = [r["pmid"] for r in out["records"]]
    assert sorted(sampled, key=int) == ["5", "6", "7", "8", "9"]
    assert all(set(r) == {"pmid", "year", "title"} for r in out["records"]) and "not shown" in out["note"]
    assert progress.batches(ws)[-1]["via"] == "openalex:frame"
    psb(capsys, "screen", "--include", "5", "6", "7", "8", "--uncertain", "9", "--reason", "meets criteria")
    ws.save_set("frame", "validation", ["5", "6", "7"])
    frame = evaluate(ws)["known_from_frame_sample"]
    assert frame["missing_from_sets"] == ["8"] and "incomplete" in frame["reading"] and frame["uncertain"] == 1
    ws.save_set("frame", "validation", ["5", "6", "7", "8"])
    frame = evaluate(ws)["known_from_frame_sample"]
    assert (frame["in_pubmed"], frame["retrieved"], frame["missing_from_sets"]) == (4, 4, [])
    assert frame["recall_lower_95_percent"] == 47.3


def test_frame_membership_ignores_which_batch_showed_a_record_first(ws):
    record_batch(ws, "pilot", "Pilot search", ["5"], total=1, query="asthma")
    record_batch(ws, "openalex:frame", "frame", ["5", "9"], total=2, query="frame")
    progress.record_screening(ws, include=["5", "9"], reason="eligible")
    ws.save_set("frame", "validation", ["5", "9"])
    frame = evaluate(ws)["known_from_frame_sample"]
    assert frame["screened_in"] == 2 and frame["retrieved"] == 1  # 9 is a real miss, 5 still counts


def test_frame_purpose_needs_openalex(ws, capsys):
    code, out = psb(capsys, "sample", "asthma", "--purpose", "frame")
    assert code == 1 and "--source openalex" in out["error"]


# -- prior reviews ----------------------------------------------------------------------------------

def test_pubmed_prior_review_sample_reports_openalex_reference_counts(make_ws, monkeypatch, capsys):
    workspace, _ = make_ws({"review[tiab]": {"50", "60"}}, {"50": record("50", "A review"), "60": record("60", "B review")})
    workspace.openalex = FakeOpenAlex(WORKS)
    monkeypatch.setattr(cli, "workspace", lambda args: workspace)
    code, out = psb(capsys, "sample", "review[tiab]", "--purpose", "prior-reviews")
    assert code == 0 and {r["pmid"]: r["refs_openalex"] for r in out["records"]} == {"50": 5, "60": 0}
    workspace.openalex = FakeOpenAlex(fail="OpenAlex request failed: blocked")
    code, out = psb(capsys, "sample", "review[tiab]", "--purpose", "prior-reviews")
    assert code == 0 and out["openalex"].startswith("unavailable") and "refs_openalex" not in out["records"][0]


def test_openalex_prior_reviews_include_reviews_outside_pubmed(ws, capsys):
    code, out = psb(capsys, "sample", "asthma review", "--source", "openalex", "--purpose", "prior-reviews")
    assert code == 0 and {r["work"] for r in out["records"]} == {"W100", "W200"}
    assert {r["work"]: r["pmid"] for r in out["records"]}["W200"] is None
    assert progress.batches(ws)[-1]["via"] == "openalex:prior-reviews"
    code, out = psb(capsys, "sample", "asthma", "--source", "openalex", "--purpose", "pilot")
    assert code == 1


# -- profile and audit ------------------------------------------------------------------------------

def test_profile_flags_topics_in_the_result_with_no_known_record(ws, capsys):
    ws.save_set("seeds", "seed", ["1", "2", "3"])
    code, out = psb(capsys, "known", "profile", "--n", "20")
    assert code == 0, out
    assert out["gaps"] == ["T2"] and "School health" in out["reading"] and "not evidence of recall" in out["reading"]


def test_audit_reports_each_citation_search_in_tarcis_terms(ws, capsys):
    psb(capsys, "neighbors", "50", "--links", "refs", "--source", "openalex")
    ws.save_set("benchmark", "benchmark", ["1", "2"])
    progress.record_screening(ws, include=["1", "2"], reason="eligible")
    section = "\n".join(deliver._citation_section(evaluate(ws)))
    assert "TARCiS" in section and "| OpenAlex | backward | 1 | 4 | 4 | 2 |" in section


def test_an_origin_published_after_the_as_of_date_is_not_followed(ws, capsys, monkeypatch):
    monkeypatch.setenv("PSB_AS_OF", "2019-06-30")
    ws.openalex.store["W100"]["publication_date"] = "2020-03-01"
    code, out = psb(capsys, "neighbors", "50", "--links", "refs", "--source", "openalex")
    assert code == 0 and out["after_as_of"] == ["50"] and out["rows"] == []
    assert "published after the as-of date" in out["note"]
