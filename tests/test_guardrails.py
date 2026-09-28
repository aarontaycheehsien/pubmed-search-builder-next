"""Observable final-delivery invariants, using deterministic PubMed/MeSH evidence."""
import copy
import hashlib
import json
import os
from pathlib import Path

import pytest

from psb import cli, deliver, mesh, validation
from psb.evaluate import evaluate
from psb.ncbi import NcbiError, PubMed
from psb.strategy import Strategy, lint
from psb.translation import translation_issues
from psb.workspace import WorkspaceError, read_json, write_json
from test_ncbi import ScriptedTransport, esearch_body


def setup(make_ws, *, term='"Asthma"[Mesh]', second="asthma*[tiab]", depth="standard"):
    ws, pm = make_ws({term: {"1"}, second: {"2"}})
    protocol = ws.protocol()
    protocol.update(depth=depth, concepts=[{"id": "topic", "role": "search", "name": "Asthma", "rationale": "Review question"}])
    write_json(ws.root / "protocol.json", protocol)
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "topic", "terms": [term, second]}]})
    return ws, pm


def snapshot(ws, **kwargs):
    ev = evaluate(ws, **kwargs)
    deliver.record_evaluation(ws, ev)
    ws.save_attempt(ev)
    return ev


def review(ws, ev, *, number=1, findings=None, accept=True):
    data = {"round": number, "strategy_version": ev["version"], "review_sha256": ev["review_sha256"],
            "domains": {d: {"verdict": "pass"} for d in deliver.DOMAINS}, "findings": findings or [],
            "issue_dispositions": [dict(issue_id=i["id"], status="accepted-risk",
                response="Intended interpretation verified for this clause", evidence="Compared the clause translation and Boolean role",
                query=i.get("query"), translation=i.get("translation"))
                for i in ev["validation"]["review_required"]] if accept else []}
    write_json(ws.root / "critic" / f"round-{number}.json", data)
    return data


def codes(result):
    return {i["code"] for i in result.get("blockers", result.get("validation", {}).get("blockers", []))}


@pytest.mark.parametrize("bad", [
    "cat*[tiab]", '"heart attack*"[tiab:~3]', '"heart attack"[mh:~3]',
    '"heart attack"[tiab:~-1]', '"heart attack[tiab]', "heart[tiab",
    "(heart[tiab] and attack[tiab])", "heart[tiab] AND", "heart[tiab] OR OR attack[tiab]",
    "heart[tiab])", "()[tiab]", '"heart"[tiab:~0]',
    "(heart[tiab] OR attack[tiab])[tiab]", "“heart attack”[tiab]", '"anti–inflammatory"[tiab]',
    "heart attack[tiab]",
])
def test_lint_errors_cannot_evaluate_successfully(make_ws, bad):
    ws, pm = setup(make_ws, second=bad)
    result = evaluate(ws)
    assert not result["ok"] and result["validation"]["blockers"]
    assert pm.queries == []


@pytest.mark.parametrize("combine", ["topic AND", "topic OR (topic AND)", "topic topic", "topic XOR topic"])
def test_bad_combination_blocked(make_ws, combine):
    ws, _ = setup(make_ws)
    data = ws.strategy().to_dict()
    data["combine"] = combine
    write_json(ws.root / "strategy.json", data)
    assert not evaluate(ws)["ok"]


def test_limit_clause_errors_are_checked(make_ws):
    ws, _ = setup(make_ws)
    data = ws.strategy().to_dict()
    data["limits"] = [{"clause": '"heart attack*"[tiab:~1]', "rationale": "test"}]
    write_json(ws.root / "strategy.json", data)
    ev = evaluate(ws)
    assert "proximity_wildcard" in codes(ev)
    assert any(i["location"] == "limit:1" for i in ev["validation"]["blockers"])


def test_excessive_wildcards_block_before_network(make_ws):
    ws, pm = setup(make_ws)
    data = ws.strategy().to_dict()
    data["blocks"][0]["terms"] = [f"asthma{n}*[tiab]" for n in range(257)]
    write_json(ws.root / "strategy.json", data)
    assert "too_many_wildcards" in codes(evaluate(ws)) and not pm.queries


def test_unknown_field_needs_authority_and_bad_fields_block(make_ws):
    ws, _ = setup(make_ws, second="asthma[newfield]")
    assert evaluate(ws)["ok"]
    data = ws.strategy().to_dict()
    data["blocks"][0]["terms"][-1] = "asthma[imaginary]"
    write_json(ws.root / "strategy.json", data)
    assert "unknown_tag" in codes(evaluate(ws))


def test_eight_warnings_cannot_hide_later_errors():
    rows = translation_issues("cat*[tiab]", '"cat"[Title/Abstract]',
                              warnings=["warning " + str(n) for n in range(12)],
                              errors={"fieldsnotfound": ["bogus"]})
    assert {"field_not_found", "truncation_dropped"} <= {r["code"] for r in rows}
    assert len(rows) > 8


def test_group_tag_and_typographic_characters_are_named():
    from psb import syntax
    assert "group_field_tag" in {c for c, _ in syntax.problems("(asthma OR wheeze)[tiab]")}
    assert "typographic_character" in {c for c, _ in syntax.problems("“Asthma”[Mesh]")}
    assert not syntax.problems('("asthma"[tiab] OR wheeze[tiab]) AND child*[tiab]')


@pytest.mark.parametrize("query,warnings,errors", [
    ('"Randomised Controlled Trial"[pt] OR asthma[tiab]',
     {"quotedphrasesnotfound": ['"Randomised Controlled Trial"[pt]']}, None),
    ("systematicx[sb] OR asthma[tiab]", None, {"phrasesnotfound": ["systematicx"], "fieldsnotfound": []}),
    ("englsh[la] OR asthma[tiab]", None, {"phrasesnotfound": ["englsh"], "fieldsnotfound": []}),
])
def test_unknown_filter_value_is_a_technical_blocker(query, warnings, errors):
    rows = [validation.identify(r) for r in translation_issues(query, '"asthma"[Title/Abstract]', None, warnings, errors)]
    assert [r["code"] for r in rows] == ["filter_value_not_found"]
    assert rows[0]["blocking"] and not rows[0]["requires_review"]


def test_free_text_not_found_stays_a_review_item():
    rows = translation_issues('"frobnicated widget"[tiab] OR englsh[tiab] OR english[la]', "t", None,
                              {"quotedphrasesnotfound": ['"frobnicated widget"[tiab]']},
                              {"phrasesnotfound": ["englsh"]})
    assert {r["code"] for r in rows} == {"quoted_phrase_not_found", "phrase_not_found"}
    assert not any(validation.identify(r)["blocking"] for r in rows)


def test_filter_value_blocker_cannot_be_waived(make_ws, monkeypatch):
    ws, pm = setup(make_ws)
    add_issue(pm, monkeypatch, code="filter_value_not_found", severity="error")
    ev = snapshot(ws)
    review(ws, ev)
    result = deliver.report(ws)
    assert not result["ok"] and "filter_value_not_found" in codes(result)
    assert not (ws.root / "final-query.txt").exists()


def test_tagged_subheading_normalisation_is_not_atm():
    rows = translation_issues("drug therapy[sh]", '"drug therapy"[Subheading]',
                              [{"from": "drug therapy[sh]", "to": '"drug therapy"[Subheading]'}])
    assert "automatic_term_mapping" not in {r["code"] for r in rows}


def test_expanded_wildcard_is_not_proof_of_dropped_truncation():
    rows = translation_issues("asthm*[tiab]", '"asthma"[Title/Abstract] OR "asthmatic"[Title/Abstract]')
    assert "truncation_dropped" not in {r["code"] for r in rows}


def test_explicit_all_field_alias_is_not_unintended_fallback():
    rows = translation_issues('"asthma"[all]', '"asthma"[All Fields]')
    assert "all_fields_fallback" not in {r["code"] for r in rows}


def test_date_range_is_not_untagged_text():
    from psb.strategy import term_issues
    rows = term_issues('"1800/01/01"[Date - Publication] : "2020/01/01"[Date - Publication]')
    assert not rows


def test_quick_scope_waiver_is_not_reported_as_missing(make_ws, monkeypatch):
    ws, _ = setup(make_ws, depth="quick")
    protocol = ws.protocol()
    protocol["notes"] = "User asked to proceed with assumptions and no seeds"
    write_json(ws.root / "protocol.json", protocol)
    monkeypatch.setattr(cli, "workspace", lambda args: ws)
    import argparse
    monkeypatch.setattr(cli, "find_root", lambda value: ws.root)
    # status opens a read-only workspace directly; no client requests are needed.
    result = cli.cmd_status(argparse.Namespace(workspace=str(ws.root)))
    assert not any("confirm concept" in t or "add known relevant" in t for t in result["todo"])


def add_issue(pm, monkeypatch, *, code="quoted_phrase_not_found", severity="warning", translation=None):
    original = pm.search
    def search(query, **kwargs):
        found = original(query, **kwargs)
        # The full query can look fine; the individual line still needs to be checked.
        if query == "asthma*[tiab]":
            found["translation"] = translation or query
            found["issues"] = [{"code": code, "severity": severity, "message": "Review this clause",
                                "query": query, "translation": found["translation"], "evidence": "phrase index warning"}]
        return found
    monkeypatch.setattr(pm, "search", search)


def test_line_only_technical_error_cannot_be_waived(make_ws, monkeypatch):
    ws, pm = setup(make_ws)
    add_issue(pm, monkeypatch, code="field_not_found", severity="error")
    ev = snapshot(ws)
    review(ws, ev)
    assert not ev["ok"] and "field_not_found" in codes(ev)
    result = deliver.report(ws)
    assert not result["ok"] and "field_not_found" in codes(result)
    assert not (ws.root / "final-query.txt").exists()


def test_phrase_warning_with_hits_requires_specific_review(make_ws, monkeypatch):
    ws, pm = setup(make_ws)
    add_issue(pm, monkeypatch)
    ev = snapshot(ws)
    assert ev["ok"] and ev["count"] == 2
    review(ws, ev, accept=False)
    assert "review_unresolved" in codes(deliver.report(ws))
    review(ws, ev)
    assert deliver.report(ws)["ok"]


def test_changed_translation_reopens_accepted_phrase_review(make_ws, monkeypatch):
    ws, pm = setup(make_ws)
    add_issue(pm, monkeypatch)
    ev = snapshot(ws)
    review(ws, ev)
    add_issue(pm, monkeypatch, translation='"asthma"[All Fields]')
    result = deliver.report(ws)
    assert {"critic_stale", "review_unresolved"} <= codes(result)
    assert ws.attempts()[-1]["evaluation"]["count"] == ev["count"]


def test_bare_generic_acceptance_does_not_close_phrase_review(make_ws, monkeypatch):
    ws, pm = setup(make_ws)
    add_issue(pm, monkeypatch)
    ev = snapshot(ws)
    data = review(ws, ev)
    data["issue_dispositions"][0].pop("translation")
    write_json(ws.root / "critic" / "round-1.json", data)
    assert "review_unresolved" in codes(deliver.report(ws))


@pytest.mark.parametrize("term,status", [('"Imaginary Disorder"[Mesh]', "not_found"),
    ('"Bronchial Asthma"[Mesh]', "not_canonical"), ('"Asthma"[nm]', "wrong_type")])
def test_vocabulary_canonical_and_type_failures(make_ws, term, status):
    ws, _ = setup(make_ws, term=term)
    assert "vocabulary_" + status in codes(evaluate(ws))


def test_valid_zero_hit_heading_is_not_invalid(make_ws, monkeypatch):
    ws, pm = setup(make_ws)
    monkeypatch.setitem(pm.atoms, pm._key('"Asthma"[Mesh]'), set())
    ev = snapshot(ws)
    assert ev["ok"] and ev["vocabulary"][0]["status"] == "verified"
    review(ws, ev)
    assert deliver.report(ws)["ok"]


def test_vocabulary_service_failure_is_unverified(make_ws, monkeypatch):
    ws, pm = setup(make_ws)
    def unavailable(*args, **kwargs):
        raise NcbiError("service unavailable")
    monkeypatch.setattr(pm, "mesh_search", unavailable)
    ev = evaluate(ws)
    assert not ev["validation"]["complete"] and "vocabulary_unverified" in codes(ev)
    assert "vocabulary_not_found" not in codes(ev)


def test_qualifier_compatibility(make_ws, monkeypatch):
    ws, pm = setup(make_ws, term='"Asthma/therapy"[Mesh]')
    assert evaluate(ws)["ok"]
    monkeypatch.setattr(pm, "mesh_descriptor", lambda ui: {"identifier": ui, "allowableQualifier": []})
    assert "qualifier_incompatible" in codes(evaluate(ws))


def test_ambiguous_vocabulary_never_chooses_first(make_ws, monkeypatch):
    ws, pm = setup(make_ws)
    original = pm.mesh_summary
    monkeypatch.setattr(pm, "mesh_summary", lambda ids: original(ids) * 2)
    assert "vocabulary_ambiguous" in codes(evaluate(ws))


@pytest.mark.parametrize("change", ["protocol", "set", "as_of", "environment"])
def test_input_changes_invalidate_critic(make_ws, monkeypatch, change):
    ws, _ = setup(make_ws)
    ev = snapshot(ws)
    review(ws, ev)
    if change in {"protocol", "as_of"}:
        p = ws.protocol()
        p["question" if change == "protocol" else "as_of"] = "Changed question" if change == "protocol" else "2020-01-01"
        write_json(ws.root / "protocol.json", p)
    elif change == "set":
        ws.save_set("seeds", "seed", ["1"])
    else:
        monkeypatch.setenv("PSB_AS_OF", "2020-01-01")
    assert "critic_stale" in codes(deliver.report(ws))


def test_quick_requires_critic_and_partial_eval_cannot_supply_it(make_ws):
    ws, _ = setup(make_ws, depth="quick")
    snapshot(ws, term_counts=False)
    with pytest.raises(WorkspaceError, match="complete"):
        deliver.critic_packet(ws)
    assert "critic_missing" in codes(deliver.report(ws))


def test_counts_and_timestamps_can_change_without_stale_review(make_ws, monkeypatch):
    ws, pm = setup(make_ws)
    ev = snapshot(ws)
    review(ws, ev)
    monkeypatch.setitem(pm.atoms, pm._key('"Asthma"[Mesh]'), {"1", "3"})
    result = deliver.report(ws)
    assert result["ok"], result
    assert "Total records: 3" in Path(result["report"]).read_text(encoding="utf-8")
    assert len(ws.versions()) == 1 and len(ws.attempts()) == 2


def finding(status="open", response=""):
    return {"id": "F1", "domain": "text_words", "severity": "must-fix", "kind": "lexical",
            "finding": "Relevant terminology requires review", "status": status, "response": response}


def test_omitted_open_finding_remains_blocking(make_ws):
    ws, _ = setup(make_ws)
    ev = snapshot(ws)
    review(ws, ev, findings=[finding()])
    review(ws, ev, number=2)
    result = deliver.report(ws)
    assert {"critic_open", "critic_dropped"} <= codes(result)


def test_resolved_finding_needs_explanation(make_ws):
    ws, _ = setup(make_ws)
    ev = snapshot(ws)
    review(ws, ev, findings=[finding("resolved")])
    assert "critic_invalid" in codes(deliver.report(ws))
    review(ws, ev, findings=[finding("resolved", "Checked the recorded vocabulary and evaluated the revised expression")])
    assert deliver.report(ws)["ok"]


@pytest.mark.parametrize("malformed", [{"domains": []}, {"findings": {}}, {"findings": [None]}, {"issue_dispositions": [None]}])
def test_malformed_review_fails_closed(make_ws, malformed):
    ws, _ = setup(make_ws)
    ev = snapshot(ws)
    data = review(ws, ev)
    data.update(malformed)
    write_json(ws.root / "critic" / "round-1.json", data)
    result = deliver.report(ws)
    assert not result["ok"] and Path(result["diagnostic"]).exists()


def test_round_files_are_sorted_numerically(make_ws):
    ws, _ = setup(make_ws)
    for n in (10, 2, 1):
        write_json(ws.root / "critic" / f"round-{n}.json", {"round": n})
    assert [r["round"] for r in deliver.critic_rounds(ws)] == [1, 2, 10]


def test_external_critic_check_checks_the_supplied_file(make_ws, tmp_path):
    ws, _ = setup(make_ws)
    ev = snapshot(ws)
    data = review(ws, ev)
    external = tmp_path / "external-round.json"
    data["findings"] = [finding()]
    write_json(external, data)
    assert not deliver.check_round(ws, external)["ok"]


def test_artifacts_agree_and_include_effective_as_of(make_ws):
    ws, pm = setup(make_ws)
    p = ws.protocol()
    p["as_of"] = "2020-01-01"
    write_json(ws.root / "protocol.json", p)
    ev = snapshot(ws)
    review(ws, ev)
    result = deliver.report(ws)
    assert result["ok"], result
    manifest = read_json(ws.root / "validation-manifest.json")
    query = (ws.root / "final-query.txt").read_text(encoding="utf-8").strip()
    assert query == manifest["query"] == ws.attempts()[-1]["evaluation"]["query"]
    assert '"2020/01/01"[edat]' in query and query in pm.queries
    assert query in Path(result["report"]).read_text(encoding="utf-8")
    for name, digest in manifest["artifacts"].items():
        assert hashlib.sha256((ws.root / name).read_bytes()).hexdigest() == digest


def test_failure_archives_old_artifacts_and_saves_attempt(make_ws):
    ws, _ = setup(make_ws)
    ev = snapshot(ws)
    review(ws, ev)
    assert deliver.report(ws)["ok"]
    old = (ws.root / "final-query.txt").read_bytes()
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "topic", "terms": ["cat*[tiab]"]}]})
    result = deliver.report(ws)
    assert not result["ok"]
    assert not any((ws.root / name).exists() for name in deliver.ARTIFACTS)
    assert next((ws.root / "history" / "deliveries").glob("*/final-query.txt")).read_bytes() == old
    assert ws.attempts()[-1]["evaluation"]["delivery_blockers"]


def test_diagnostic_mode_never_publishes(make_ws):
    ws, _ = setup(make_ws)
    ev = snapshot(ws)
    review(ws, ev)
    result = deliver.report(ws, diagnostic=True)
    assert not result["ok"] and Path(result["diagnostic"]).exists()
    assert not any((ws.root / name).exists() for name in deliver.ARTIFACTS)


def test_publication_failure_removes_partial_current_artifacts(make_ws, monkeypatch):
    ws, _ = setup(make_ws)
    review(ws, snapshot(ws))
    replace = Path.replace
    def broken(path, target):
        if path.name == "validation-manifest.json" and Path(target).parent == ws.root:
            raise OSError("simulated publication failure")
        return replace(path, target)
    monkeypatch.setattr(Path, "replace", broken)
    result = deliver.report(ws)
    assert not result["ok"] and "publication_failed" in codes(result)
    assert Path(result["diagnostic"]).exists()
    assert not any((ws.root / name).exists() for name in deliver.ARTIFACTS)


def test_ncbi_malformed_search_is_not_zero_results():
    pm = PubMed(transport=ScriptedTransport([b'{"esearchresult": {}}']))
    with pytest.raises(NcbiError, match="malformed"):
        pm.search("asthma[tiab]")


def test_receipt_rejects_changed_artifact_and_current_inputs(make_ws):
    ws, _ = setup(make_ws)
    review(ws, snapshot(ws))
    assert deliver.report(ws)["ok"] and deliver.verify_delivery(ws)["ok"]
    path = ws.root / "final-query.txt"
    original = path.read_bytes()
    path.write_text("changed query", encoding="utf-8")
    assert not deliver.verify_delivery(ws)["ok"]
    path.write_bytes(original)
    protocol = ws.protocol()
    protocol["question"] = "A different review question"
    write_json(ws.root / "protocol.json", protocol)
    assert not deliver.verify_delivery(ws)["ok"]


def test_report_bypasses_existing_cache(make_ws, monkeypatch):
    ws, pm = setup(make_ws)
    review(ws, snapshot(ws))
    pm.cache.enabled = True
    original = pm.search
    states = []
    def search(*args, **kwargs):
        states.append(pm.cache.enabled)
        return original(*args, **kwargs)
    monkeypatch.setattr(pm, "search", search)
    assert deliver.report(ws)["ok"]
    assert states and not any(states) and pm.cache.enabled


def test_inputs_changed_during_publication_fail_closed(make_ws, monkeypatch):
    ws, _ = setup(make_ws)
    review(ws, snapshot(ws))
    original = deliver._audit
    def audit(*args):
        content = original(*args)
        protocol = ws.protocol()
        protocol["question"] = "Changed during publication"
        write_json(ws.root / "protocol.json", protocol)
        return content
    monkeypatch.setattr(deliver, "_audit", audit)
    assert "publication_failed" in codes(deliver.report(ws))
    assert not any((ws.root / name).exists() for name in deliver.ARTIFACTS)


def test_phrase_guidance_does_not_silently_repair(make_ws, monkeypatch):
    ws, pm = setup(make_ws)
    before = ws.strategy_text()
    add_issue(pm, monkeypatch)
    ev = evaluate(ws)
    item = next(i for i in ev["validation"]["review_required"] if i["code"] == "quoted_phrase_not_found")
    assert item["review_guidance"]["candidates"] and ws.strategy_text() == before


def test_protected_harness_does_not_fall_back_to_handwritten_query(tmp_path):
    import run
    (tmp_path / "work").mkdir()
    (tmp_path / "final_strategy.txt").write_text("asthma[tiab]", encoding="utf-8")
    assert run.find_strategy_file(tmp_path, require_protected=True) is None


def test_cli_report_default_and_fresh_have_same_gate(make_ws, monkeypatch, capsys):
    ws, _ = setup(make_ws)
    monkeypatch.setattr(cli, "workspace", lambda args: ws)
    assert cli.main(["report"]) == 1
    assert json.loads(capsys.readouterr().out)["ok"] is False
    ev = snapshot(ws)
    review(ws, ev)
    assert cli.main(["report", "--fresh"]) == 0
    assert json.loads(capsys.readouterr().out)["ok"] is True
    assert cli.main(["report", "--diagnostic"]) == 1
    assert json.loads(capsys.readouterr().out)["ok"] is False
    assert not (ws.root / "final-query.txt").exists()


def test_backend_failure_never_issues_query(make_ws, monkeypatch):
    ws, pm = setup(make_ws)
    def failed(*args, **kwargs):
        raise NcbiError("PubMed rejected the query")
    monkeypatch.setattr(pm, "search", failed)
    result = deliver.report(ws)
    assert "validation_unavailable" in codes(result)
    assert not (ws.root / "final-query.txt").exists()
    assert ws.attempts()[-1]["evaluation"]["delivery_blockers"]


@pytest.mark.skipif(os.environ.get("PSB_LIVE_TESTS") != "1", reason="opt-in live NCBI smoke test")
def test_live_authority_and_translation():
    pm = PubMed()
    evidence, issues = mesh.validate_query(pm, '"Asthma/therapy"[Mesh]', "live-test")
    assert not issues and evidence[0]["ui"] == "D001249"
    found = pm.search('"Asthma"[Mesh] OR asthma[tiab]')
    assert isinstance(found["count"], int) and found["translation"]
    assert not any(i["severity"] == "error" for i in found["issues"])
    for bad in ('"Randomised Controlled Trial"[pt] OR asthma[tiab]', "systematicx[sb] OR asthma[tiab]"):
        assert "filter_value_not_found" in {i["code"] for i in pm.search(bad)["issues"]}
    assert not any(i["severity"] == "error" for i in pm.search('"Randomized Controlled Trial"[pt] OR english[la]')["issues"])
