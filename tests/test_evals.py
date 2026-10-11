import json
import sys
from pathlib import Path

from conftest import FakePubMed

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "evals"))

import drivers  # noqa: E402
import harness  # noqa: E402

FIXTURE = {
    "id": "T1", "question": "Asthma in children?", "as_of": "2015-01-01", "seeds": ["1"],
    "gold_pmids": ["1", "2", "3", "4"], "eligibility": ["children", "asthma"],
    "naive_blocks": [{"id": "a", "terms": ["asthma", "wheezing disorder"]}, {"id": "c", "terms": ["child"]}],
}


def fake():
    return FakePubMed({"asthma[tiab]": {"1", "2", "3", "9"}, '"wheezing disorder"[tiab]': {"4"}, "child[tiab]": {"1", "2", "4", "9"}})


def test_naive_query_is_or_within_and_across():
    assert harness.naive_query(FIXTURE) == '(asthma[tiab] OR "wheezing disorder"[tiab]) AND (child[tiab])'


def test_score_excludes_seeds_and_reports_unseen_recall():
    result = harness.score(FIXTURE, harness.naive_query(FIXTURE), exclude={"1"}, seen={"2"}, pm=fake())
    assert (result["gold_reachable"], result["retrieved"], result["recall_percent"]) == (3, 2, 66.7)
    assert result["missed"] == ["3"] and result["count"] == 4 and result["nnr"] == 2.0
    assert (result["gold_seen_by_agent"], result["unseen_retrieved"], result["unseen_recall_percent"]) == (1, 1, 50.0)


def test_strict_unseen_excludes_exposed_records_outside_sets():
    result = harness.score(FIXTURE, "asthma[tiab]", seen={"2"}, exposed={"2", "3"}, pm=fake())
    assert result["unseen_recall_percent"] == 66.7
    assert result["strict_unseen_total"] == 2
    assert result["strict_unseen_retrieved"] == 1
    assert result["strict_unseen_recall_percent"] == 50.0
    empty = harness.score(FIXTURE, "asthma[tiab]", exposed=set(FIXTURE["gold_pmids"]), pm=fake())
    assert empty["strict_unseen_recall_percent"] is None


def test_exposure_includes_builder_uncertain_excluded_and_nongold_companions(tmp_path):
    from psb.workspace import append_jsonl, write_json
    work = tmp_path / "work"
    append_jsonl(work / "exposure.jsonl", {"pmid": "99", "kind": "abstract"})
    append_jsonl(work / "screening.jsonl", {"pmid": "99", "group": "trial", "context": "builder", "decision": "exclude"})
    append_jsonl(work / "screening.jsonl", {"pmid": "1", "group": "trial", "context": "separate", "decision": "include"})
    append_jsonl(work / "screening.jsonl", {"pmid": "2", "context": "builder", "decision": "uncertain"})
    append_jsonl(work / "screening.jsonl", {"pmid": "3", "context": "separate", "decision": "include"})
    write_json(work / "sets" / "development.json", {"pmids": ["4"]})
    assert harness.gold_exposed(FIXTURE, tmp_path) == {"1", "2", "4"}


def test_common_unseen_pair_uses_union_and_never_returns_gold_identities():
    result = harness.score_common_unseen(FIXTURE, "asthma[tiab]", "child[tiab]", exposed_a={"1"},
                                        exposed_b={"2"}, pm=fake())
    assert result["a"]["strict_unseen_total"] == result["b"]["strict_unseen_total"] == 2
    assert result["a"]["strict_unseen_retrieved"] == result["b"]["strict_unseen_retrieved"] == 1
    assert result["gold_gained"] == result["gold_lost"] == 1
    assert "missed" not in json.dumps(result) and "pmids" not in json.dumps(result)


def test_semantic_experiment_is_opt_in_and_preserves_total_budget():
    normal = drivers.prompt_for(FIXTURE, seeds=[], depth="standard")
    assert "Enable the experimental" not in normal
    treatment = drivers.prompt_for(FIXTURE, seeds=[], depth="standard", semantic_miss_hunt=True)
    assert "do not increase the total budget" in treatment
    assert "one bounded repair round" in treatment


def test_prompt_never_contains_gold_beyond_seeds():
    prompt = drivers.prompt_for(FIXTURE, seeds=[], depth="standard")
    assert "Asthma in children?" in prompt and "- children" in prompt
    assert "don't have any known relevant articles" in prompt and "2015-01-01" in prompt
    seeded = drivers.prompt_for(FIXTURE, seeds=["1"], depth="quick")
    assert "PMIDs): 1" in seeded and "quick depth" in seeded


def test_leakage_flags_answer_key_mentions_and_undated_searches(tmp_path):
    work = tmp_path / "work"
    work.mkdir()
    entries = [{"type": "ncbi", "endpoint": "esearch.fcgi", "params": {"db": "pubmed", "term": "x", "maxdate": "2015/01/01"}},
               {"type": "ncbi", "endpoint": "esearch.fcgi", "params": {"db": "pubmed", "term": "y"}}]
    (work / "log.jsonl").write_text("\n".join(json.dumps(e) for e in entries), encoding="utf-8")
    problems = harness.leakage(FIXTURE, tmp_path, "I opened evals/fixtures to check")
    assert any("evals/fixtures" in p for p in problems) and any("1 PubMed searches" in p for p in problems)
    assert harness.leakage(FIXTURE, tmp_path / "nowhere", "clean transcript") == []


def test_leakage_accepts_the_evaluators_inline_as_of_bound(tmp_path):
    from psb.evaluate import effective_query
    work = tmp_path / "work"
    work.mkdir()
    bounded = effective_query('asthma[tiab] OR "wheezing disorder"[tiab]', FIXTURE["as_of"])
    assert '[crdt]' in bounded
    legacy = effective_query('asthma[tiab] OR "wheezing disorder"[tiab]', FIXTURE["as_of"], 'edat')  # an older run
    evasions = [
        '(asthma[tiab]) AND ("1800/01/01"[crdt] : "2015/01/01"[edat])',  # the two ends name different fields
        effective_query("asthma[tiab]", "2020-01-01"),  # bound later than as_of
        'asthma[tiab] OR child[tiab] AND ("1800/01/01"[edat] : "2015/01/01"[edat])',  # binds one operand only
        '(asthma[tiab]) OR (child[tiab]) AND ("1800/01/01"[edat] : "2015/01/01"[edat])',
        'asthma[tiab] OR ("1800/01/01"[edat] : "2015/01/01"[edat])',
    ]
    entries = [{"endpoint": "esearch.fcgi", "params": {"db": "pubmed", "term": t}} for t in [bounded, legacy, *evasions]]
    (work / "log.jsonl").write_text("\n".join(json.dumps(e) for e in entries), encoding="utf-8")
    assert harness.leakage(FIXTURE, tmp_path, "clean transcript") == [f"{len(evasions)} PubMed searches ran without the as_of bound"]


def test_leakage_reads_the_separate_contexts_private_request_log(tmp_path):
    work = tmp_path / "work"
    (work / "screening").mkdir(parents=True)
    # A restricted invocation leaves an accounting row in log.jsonl and the full row in screening/log.jsonl.
    (work / "log.jsonl").write_text(json.dumps({"type": "ncbi", "endpoint": "esearch.fcgi", "cache": False}) + "\n",
                                    encoding="utf-8")
    full = {"type": "ncbi", "endpoint": "esearch.fcgi", "params": {"db": "pubmed", "term": "y"}, "cache": False}
    (work / "screening" / "log.jsonl").write_text(json.dumps(full) + "\n", encoding="utf-8")
    assert harness.leakage(FIXTURE, tmp_path, "clean transcript") == ["1 PubMed searches ran without the as_of bound"]


def test_leakage_skips_a_log_line_torn_by_a_concurrent_writer(tmp_path):
    work = tmp_path / "work"
    work.mkdir()
    good = {"type": "ncbi", "endpoint": "esearch.fcgi", "params": {"db": "pubmed", "term": "x", "maxdate": "2015/01/01"}}
    (work / "log.jsonl").write_text(json.dumps(good) + "\n" + '{"ts": "x", "type": "ncbi", "para', encoding="utf-8")
    assert harness.leakage(FIXTURE, tmp_path, "clean transcript") == []


def test_leakage_ignores_the_run_directorys_own_path(tmp_path):
    run_dir = tmp_path / "runs" / "T1" / "some-label"
    run_dir.mkdir(parents=True)
    raw = str(run_dir)
    once = raw.replace(chr(92), chr(92) * 2)  # single JSON escaping
    twice = once.replace(chr(92), chr(92) * 2)  # a JSON blob nested as a string value, re-escaped
    # A tool echoing its own cwd trivially "mentions" the id via the run directory name, at
    # whatever escaping depth a (possibly nested) JSON transcript renders it.
    transcript = f'{{"cwd": "{raw}"}} and {{"cwd": "{once}"}} and {{"nested": "{{\\"cwd\\": \\"{twice}\\"}}"}}'
    assert harness.leakage(FIXTURE, run_dir, transcript) == []
    # A genuine mention elsewhere in the transcript is still caught.
    assert harness.leakage(FIXTURE, run_dir, transcript + " topic T1 is a CLEF TAR review") != []


def test_gold_seen_reads_agent_sets(tmp_path):
    sets = tmp_path / "work" / "sets"
    sets.mkdir(parents=True)
    (sets / "relevant.json").write_text(json.dumps({"role": "relevant", "pmids": ["2", "77"]}), encoding="utf-8")
    assert harness.gold_seen(FIXTURE, tmp_path) == {"2"}


def test_gold_reserved_reads_the_allocation_until_release(tmp_path):
    work = tmp_path / "work"
    work.mkdir()
    units = [{"id": "1", "members": ["1"], "purpose": "holdout"}, {"id": "2", "members": ["2"], "purpose": "development"}]
    (work / "allocation.json").write_text(json.dumps({"units": units}), encoding="utf-8")
    assert harness.gold_reserved(FIXTURE, tmp_path) == {"1"} & set(FIXTURE["gold_pmids"])
    (work / "allocation-log.jsonl").write_text(json.dumps({"type": "release"}) + "\n", encoding="utf-8")
    assert harness.gold_reserved(FIXTURE, tmp_path) == set()
    (work / "screening.jsonl").write_text("\n".join(json.dumps(r) for r in [
        {"pmid": "1", "decision": "include", "context": "separate"}, {"pmid": "2", "decision": "include"}]),
        encoding="utf-8")
    assert harness.screening_contexts(tmp_path) == {"separate": 1, "builder": 1}


def test_stage_skill_copies_skill_but_not_evals(tmp_path):
    run = tmp_path / "run"
    run.mkdir()
    staged = drivers.stage_skill(harness.REPO, run)
    assert (staged / "SKILL.md").exists() and (staged / "scripts" / "psb.py").exists()
    assert not (staged / "evals").exists() and not (staged / "tests").exists()
