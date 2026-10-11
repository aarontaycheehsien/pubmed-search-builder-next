"""Offline provider, PubMed membership, holdout boundaries and resumable discovery."""
import json

import pytest

from conftest import record
from psb import allocation, cli, deliver, holdout, miss_hunt, progress, reserved
from psb.evaluate import evaluate
from psb.http import TransportError
from psb.ncbi import NcbiError
from psb.openalex import OpenAlex
from psb.workspace import WorkspaceError, read_json, write_json
from test_allocation import HELD, make_pool, through_critic


def work(pmid, **extra):
    return {"id": f"https://openalex.org/W{pmid}", "ids": {"pmid": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}"}, **extra}


class Provider:
    def __init__(self, responses):
        self.responses, self.calls = responses, []

    def search(self, query, limit):
        self.calls.append((query, limit))
        response = self.responses[query]
        if isinstance(response, Exception):
            raise response
        return {"results": response[:limit]}


def evaluated(ws):
    result = evaluate(ws)
    assert result["ok"]
    ws.save_version(result, "Provisional strategy")


@pytest.fixture
def ready(make_ws):
    ws, pm = make_ws({"asthma[tiab]": {"1"}}, {str(p): record(str(p), f"Title {p}") for p in range(1, 8)})
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "a", "name": "Asthma", "terms": ["asthma[tiab]"]}]})
    allocation.freeze(ws)
    evaluated(ws)
    return ws, pm


def test_filters_membership_cutoff_known_and_duplicates_before_exposure(ready, monkeypatch):
    ws, pm = ready
    progress.record_screening(ws, exclude=["3"], reason="already screened")
    original = pm.existing
    monkeypatch.setattr(pm, "existing", lambda ids: original(ids) - {"4"})
    provider = Provider({"population": [work("1"), work("2"), work("3"), work("4"), {"id": "unresolved"}],
                         "intervention": [work("2"), work("5")]})
    allocation_bytes = (ws.root / "allocation.json").read_bytes()
    strategy_bytes = (ws.root / "strategy.json").read_bytes()
    result = miss_hunt.run(ws, ["population", "intervention"], client=provider)
    assert [r["pmid"] for r in result["candidates"]] == ["2", "5"]
    assert len(result["candidates"][0]["sources"]) == 2
    assert result["counts"] == {"returned": 7, "unresolved": 1, "already_known": 1,
                                "unavailable_at_cutoff": 1, "available_new": 3, "already_retrieved": 1,
                                "candidate_misses": 2, "queued": 2}
    assert {e["pmid"] for e in reserved.events(ws)} == {"2", "5"}
    assert not ws.set_pmids("development")
    assert not (ws.root / "records.jsonl").exists()  # identifiers only; no fetch before screening
    assert (ws.root / "allocation.json").read_bytes() == allocation_bytes
    assert (ws.root / "strategy.json").read_bytes() == strategy_bytes
    assert allocation.routes(ws)["2"] == {"semantic-search": False}
    assert miss_hunt.summary(ws)["awaiting_screening"] == 2


def test_reserved_records_and_known_companions_never_reach_receipt(make_ws):
    ws, pm = make_pool(make_ws)
    allocation.freeze(ws, choice="keep-holdout")
    group = next(u["group"] for u in ws.allocation()["units"] if u["purpose"] == "holdout")
    progress.record_screening(ws, uncertain=["999"], context="separate", group=group)
    evaluated(ws)
    provider = Provider({"topic": [work(HELD[0]), work("999"), work("998")]})
    pm.universe.add("998")
    result = miss_hunt.run(ws, ["topic"], client=provider)
    assert [c["pmid"] for c in result["candidates"]] == ["998"]
    text = json.dumps(result)
    assert HELD[0] not in text and "999" not in text
    assert not ({e["pmid"] for e in reserved.events(ws)} & {HELD[0], "999"})
    assert "999" in ws.reserved_pmids()


def test_screening_budget_is_shared_and_one_completed_batch_only(ready):
    ws, _ = ready
    progress.record_screening(ws, exclude=[str(p) for p in range(1000, 1148)])
    result = miss_hunt.run(ws, ["topic"], client=Provider({"topic": [work("2"), work("3"), work("4")]}))
    assert result["screening_limit"] == 2 and result["counts"]["queued"] == 2
    with pytest.raises(WorkspaceError, match="one miss-hunt batch"):
        miss_hunt.run(ws, ["topic"], client=Provider({}))


def test_exhausted_budget_makes_no_provider_request(ready):
    ws, _ = ready
    progress.record_screening(ws, exclude=[str(p) for p in range(1000, 1150)])
    provider = Provider({})
    with pytest.raises(WorkspaceError, match="budget is exhausted"):
        miss_hunt.run(ws, ["topic"], client=provider)
    assert not provider.calls


def test_failure_is_not_a_miss_and_retry_reuses_frozen_response(ready, monkeypatch):
    ws, pm = ready
    provider = Provider({"topic": [work("2")]})
    among = pm.among
    monkeypatch.setattr(pm, "among", lambda *a: (_ for _ in ()).throw(NcbiError("outage")))
    with pytest.raises(NcbiError):
        miss_hunt.run(ws, ["topic"], client=provider)
    assert not (ws.root / miss_hunt.RECEIPT).exists() and not reserved.events(ws)
    with pytest.raises(WorkspaceError, match="bound to its original"):
        miss_hunt.run(ws, ["different"], client=provider)
    monkeypatch.setattr(pm, "among", among)
    result = miss_hunt.run(ws, ["topic"], client=provider)
    assert result["counts"]["queued"] == 1 and len(provider.calls) == 1


def test_provider_partial_failure_resumes_without_repeating_first_query(ready):
    ws, _ = ready
    provider = Provider({"one": [work("2")], "two": WorkspaceError("quota")})
    with pytest.raises(WorkspaceError, match="quota"):
        miss_hunt.run(ws, ["one", "two"], client=provider)
    provider.responses["two"] = [work("3")]
    result = miss_hunt.run(ws, ["one", "two"], client=provider)
    assert [q for q, _ in provider.calls] == ["one", "two", "two"]
    assert result["counts"]["queued"] == 2


def test_archived_response_integrity_is_checked_before_resume(ready):
    ws, _ = ready
    provider = Provider({"one": [work("2")], "two": WorkspaceError("quota")})
    with pytest.raises(WorkspaceError):
        miss_hunt.run(ws, ["one", "two"], client=provider)
    path = ws.root / miss_hunt.PRIVATE / "response-1.json"
    data = read_json(path)
    data["response"]["results"] = [work("3")]
    write_json(path, data)
    with pytest.raises(WorkspaceError, match="hash check"):
        miss_hunt.run(ws, ["one", "two"], client=provider)
    assert not reserved.events(ws)
    assert miss_hunt.summary(ws) == {"performed": False, "attempted": True}


def test_retrospective_semantic_discovery_requires_create_date(ready, monkeypatch):
    ws, _ = ready
    monkeypatch.setenv("PSB_AS_OF", "2020-01-01")
    (ws.root / "cutoff.json").unlink()
    with pytest.raises(WorkspaceError, match="Create Date cutoff"):
        miss_hunt.run(ws, ["topic"], client=Provider({}))


def test_miss_hunt_survives_critic_holdout_and_protected_delivery(make_ws):
    ws, pm = make_pool(make_ws)
    allocation.freeze(ws, choice="keep-holdout")
    evaluated(ws)
    pm.universe.add("998")
    miss_hunt.run(ws, ["topic"], client=Provider({"topic": [work("998")]}))
    progress.record_screening(ws, uncertain=["998"], evidence="abstract", origin=["semantic-search"])
    through_critic(ws)
    holdout.run(ws)
    result = deliver.report(ws)
    assert result["ok"], result
    assert deliver.verify_delivery(ws)["ok"]
    audit = (ws.root / "audit.md").read_text(encoding="utf-8")
    assert "Experimental semantic miss hunting" in audit and '"uncertain": 1' in audit
    assert "semantic search" in audit
    assert not any(u.get("id") == "998" for u in ws.allocation()["units"])


@pytest.mark.parametrize("queries,limit,per_query", [([], 30, 50), (["a"] * 4, 30, 50), (["a", "a"], 30, 50),
                                                   ([" "], 30, 50), (["x" * 2001], 30, 50),
                                                   (["a"], 31, 50), (["a"], 30, 51)])
def test_invalid_bounds_fail_before_provider(ready, queries, limit, per_query):
    ws, _ = ready
    provider = Provider({})
    with pytest.raises(WorkspaceError):
        miss_hunt.run(ws, queries, limit=limit, per_query=per_query, client=provider)
    assert not provider.calls


def test_must_run_after_allocation_and_eval_before_holdout(ready):
    ws, _ = ready
    held = ws.root / "holdout" / "receipt-1.json"
    write_json(held, {"status": "complete"})
    with pytest.raises(WorkspaceError, match="before the held-out test"):
        miss_hunt.run(ws, ["topic"])
    held.unlink()
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "a", "terms": ["wheeze[tiab]"]}]})
    with pytest.raises(WorkspaceError, match="psb eval"):
        miss_hunt.run(ws, ["topic"])
    (ws.root / "allocation.json").unlink()
    with pytest.raises(WorkspaceError, match="freeze the allocation"):
        miss_hunt.run(ws, ["topic"])


def test_doi_resolution_is_unambiguous_and_dated(ready):
    _, pm = ready
    pm.atoms['"10.1234/good"[doi]'] = {"2"}
    pm.atoms['"10.1234/ambiguous"[doi]'] = {"2", "3"}
    assert miss_hunt._resolve(pm, {"doi": "https://doi.org/10.1234/good"}) == "2"
    assert miss_hunt._resolve(pm, {"doi": "10.1234/ambiguous"}) is None
    assert miss_hunt._resolve(pm, {"doi": '10.1234/x" OR 99[uid]'}) is None
    assert miss_hunt._resolve(pm, {"ids": {"pmid": "http://www.ncbi.nlm.nih.gov/pubmed/0002"}}) == "2"


def test_summary_tracks_uncertainty_resolution_without_promoting_records(ready):
    ws, _ = ready
    miss_hunt.run(ws, ["topic"], client=Provider({"topic": [work("2"), work("3")]}))
    progress.record_screening(ws, uncertain=["2"], exclude=["3"], evidence="abstract")
    assert miss_hunt.summary(ws)["screening"] == {"include": 0, "exclude": 1, "uncertain": 1}
    progress.record_screening(ws, include=["2"], evidence="full-text", source_ref="Methods")
    summary = miss_hunt.summary(ws)
    assert summary["full_text_decisions"] == 1 and summary["screening_decisions"] == 3
    assert summary["confirmed_in_development"] == 0
    ws.save_set("development", "development", ["2"], origin=["semantic-search"])
    assert miss_hunt.summary(ws)["confirmed_in_development"] == 1
    assert "not recall" in "\n".join(miss_hunt.audit_lines(ws))


def test_cli_dispatch_and_progress(ready, monkeypatch, capsys, tmp_path):
    ws, _ = ready
    monkeypatch.setattr(cli, "workspace", lambda args: ws)
    monkeypatch.setattr(miss_hunt, "OpenAlex", lambda: Provider({"topic": [work("2")]}))
    query_file = tmp_path / "queries.json"
    write_json(query_file, ["topic"])
    assert cli.main(["miss-hunt", "--queries", str(query_file)]) == 0
    result = json.loads(capsys.readouterr().out)
    assert result["progress"]["step"] == 5
    assert cli.main(["miss-hunt", "--summary"]) == 0
    assert json.loads(capsys.readouterr().out)["awaiting_screening"] == 1


def test_openalex_contract_and_secret_safe_errors(monkeypatch):
    monkeypatch.setenv("OPENALEX_API_KEY", "secret-value")

    class Transport:
        def request(self, url, params, **kwargs):
            assert url == "https://api.openalex.org/works"
            assert params == {"search.semantic": "topic", "per-page": "5", "select": "id,ids,doi", "api_key": "secret-value"}
            assert kwargs["policy"].per_second == 1
            return json.dumps({"results": [{**work("2"), "title": "Never exposed"}]}).encode()

    assert "Never exposed" not in json.dumps(OpenAlex(Transport()).search("topic", 5))

    class Failing:
        def request(self, *a, **kw):
            raise TransportError("secret-value", transient=False)

    with pytest.raises(WorkspaceError) as caught:
        OpenAlex(Failing()).search("topic", 5)
    assert "secret-value" not in str(caught.value)


@pytest.mark.parametrize("payload", [b"not json", b"{}", b'{"results": [null]}', b'{"results": [{}, {}]}'])
def test_malformed_provider_response_is_not_an_empty_discovery(payload):
    class Transport:
        def request(self, *a, **kw):
            return payload
    with pytest.raises(WorkspaceError):
        OpenAlex(Transport()).search("topic", 1)


@pytest.mark.parametrize("response", [
    {"count": 0, "pmids": [], "issues": [{"severity": "error"}]},
    {"count": 1, "pmids": [], "issues": []},
    {"count": 1, "pmids": ["999"], "issues": []},
])
def test_membership_failures_cannot_masquerade_as_misses(ready, monkeypatch, response):
    _, pm = ready
    monkeypatch.setattr(pm, "search", lambda *a, **kw: response)
    with pytest.raises(NcbiError):
        pm.among("asthma[tiab]", ["2"])
