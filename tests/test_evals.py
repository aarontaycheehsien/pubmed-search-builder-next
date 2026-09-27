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


def test_stage_skill_copies_skill_but_not_evals(tmp_path):
    run = tmp_path / "run"
    run.mkdir()
    staged = drivers.stage_skill(harness.REPO, run)
    assert (staged / "SKILL.md").exists() and (staged / "scripts" / "psb.py").exists()
    assert not (staged / "evals").exists() and not (staged / "tests").exists()
