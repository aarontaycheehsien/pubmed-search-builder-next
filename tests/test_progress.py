"""Standardised progress messages: fixed templates, deterministic text, no effect on delivery."""

import json
import os
import re
from pathlib import Path

import pytest

from conftest import record
from psb import cli, deliver, progress, validation
from psb.workspace import write_json

ATOMS = {
    '"Asthma"[Mesh]': {"1", "2", "5"}, "asthma*[tiab]": {"1", "3", "6"},
    '"Child"[Mesh]': {"1", "2", "3", "6"}, "child*[tiab]": {"1", "2", "3", "5"},
}
RECORDS = {p: record(p, f"Record {p}", "Asthma in children.") for p in "12345678"}
LINKS = {("1", "similar"): [("5", 30), ("6", 20), ("7", 10)], ("2", "similar"): [("5", 25)],
         ("1", "refs"): [("7", 0), ("8", 0)], ("2", "refs"): []}
PROTOCOL = {
    "concepts": [
        {"id": "asthma", "name": "Asthma", "role": "search", "rationale": "condition, reliably indexed"},
        {"id": "child", "name": "Children", "role": "search", "rationale": "population named in abstracts"},
        {"id": "outcome", "name": "Exacerbations", "role": "screen", "rationale": "outcomes are\nreported unevenly"},
    ],
    "eligibility": {"include": ["children with asthma", "any intervention"], "exclude": ["case reports"]},
    "limits": [{"limit": "English", "reason": "translation budget"}],
    "depth": "standard", "scope_confirmed": True,
}
STRATEGY = {"blocks": [
    {"id": "asthma", "name": "Asthma", "terms": ['"Asthma"[Mesh]', "asthma*[tiab]"]},
    {"id": "child", "name": "Children", "terms": ['"Child"[Mesh]', "child*[tiab]"]},
]}


@pytest.fixture
def ws(make_ws, monkeypatch):
    workspace, _ = make_ws(ATOMS, RECORDS, LINKS, question="Which treatments reduce asthma attacks in children?")
    protocol = workspace.protocol()
    protocol.update(PROTOCOL)
    write_json(workspace.root / "protocol.json", protocol)

    def opened(args):
        workspace.log({"type": "command", "argv": args.argv})
        return workspace

    monkeypatch.setattr(cli, "workspace", opened)
    return workspace


def psb(capsys, *argv):
    code = cli.main(list(argv))
    return code, json.loads(capsys.readouterr().out)


def text(capsys, *argv):
    code, out = psb(capsys, *argv)
    assert code == 0, out
    return out["progress"]["text"]


def review(ws, number=1):
    evaluation = deliver.latest_evaluation(ws)
    write_json(ws.root / "critic" / f"round-{number}.json", {
        "round": number, "strategy_version": evaluation["version"], "review_sha256": evaluation["review_sha256"],
        "domains": {d: {"verdict": "pass", "note": "ok"} for d in deliver.DOMAINS},
        "findings": [{"id": "F1", "domain": "text_words", "severity": "document", "kind": "lexical",
                      "finding": "Consider wheez*", "recommendation": "test it", "status": "accepted-risk",
                      "response": "tested; adds noise only"}],
        "issue_dispositions": []})


def build(ws, capsys):
    """The whole workflow, returning every relayed message in order."""
    sent = [text(capsys, "progress", "intake-request"), text(capsys, "progress", "intake"), text(capsys, "progress", "scope"),
            text(capsys, "set", "add", "seeds", "1", "2", "--role", "seed"),
            text(capsys, "neighbors", "--set", "seeds", "--links", "similar,refs", "--exclude-known"),
            text(capsys, "sample", "--purpose", "pilot", "asthma*[tiab]"),
            text(capsys, "screen", "--include", "5", "6", "--exclude", "7", "--uncertain", "8", "--reason", "abstract"),
            text(capsys, "screen", "--include", "3"),
            text(capsys, "set", "add", "relevant", "5", "6", "3", "--role", "relevant", "--source", "screened"),
            text(capsys, "progress", "known-records")]
    write_json(ws.root / "strategy.json", STRATEGY)
    sent += [text(capsys, "progress", "vocabulary"),
             text(capsys, "eval", "--note", "first draft", "--brief"),
             text(capsys, "progress", "test"),
             text(capsys, "critic", "packet")]
    review(ws)
    sent += [text(capsys, "critic", "check"), text(capsys, "progress", "critic"),
             text(capsys, "report"), text(capsys, "progress", "deliver")]
    return sent


def test_screening_message_has_the_agreed_shape(ws, capsys):
    psb(capsys, "set", "add", "seeds", "1", "2", "--role", "seed")
    psb(capsys, "neighbors", "--set", "seeds", "--links", "similar,refs", "--exclude-known")
    psb(capsys, "sample", "--purpose", "pilot", "asthma*[tiab]")
    message = text(capsys, "screen", "--include", "5", "6", "3", "--exclude", "7", "--uncertain", "8")
    assert message == (
        "**PSB · Step 3/7 Known records · Screening**\n"
        "Screened 5 candidates: 3 include · 1 exclude · 1 uncertain\n"
        "- Similar articles + backward citations from 2 records (set seeds) (C1): 4 screened → 2 include\n"
        "- Pilot search `asthma*[tiab]` (C2): 1 screened → 1 include\n"
        "- Screening budget used: 5 of ~150 (standard)\n"
        "- Included but not yet in a set: 3, 5, 6")


def test_candidate_searches_are_announced(ws, capsys):
    psb(capsys, "set", "add", "seeds", "1", "2", "--role", "seed")
    assert text(capsys, "neighbors", "--set", "seeds", "--links", "similar,refs", "--exclude-known") == (
        "**PSB · Step 3/7 Known records · Similar articles + Citation search, backward**\n"
        "Found 4 candidate records linked to 2 known records (set seeds)\n"
        "- Similar articles: 3\n"
        "- Reference lists (backward): 2\n"
        "- Already in a known-record set: 0 (excluded)\n"
        "- Shown for screening: 4 records as candidate batch C1")
    assert text(capsys, "sample", "--purpose", "prior-reviews", "asthma*[tiab]") == (
        "**PSB · Step 3/7 Known records · Prior-review search**\n"
        "Prior-review search: 3 records for `asthma*[tiab]`\n"
        "- Shown: 3 reviews to check against the scope (batch C2)")
    assert text(capsys, "count", "--purpose", "noise-check", "child*[tiab]") == (
        "**PSB · Step 5/7 Test & revise · Noise check**\n"
        "Noise check: 4 records for `child*[tiab]`\n"
        "- Count only; no records shown")
    code, out = psb(capsys, "count", "child*[tiab]")
    assert code == 0 and "progress" not in out


def test_every_stage_reports_and_status_stops_reminding(ws, capsys):
    sent = build(ws, capsys)
    headers = [m.splitlines()[0] for m in sent]
    for step, name in progress.STEPS.items():
        assert any(h.startswith(f"**PSB · Step {step}/7 {name} · ") for h in headers), name
    known = sent[9]
    assert "Known relevant records: 5 for development · 0 held out" in known
    assert "- Screening: 5 screened → 3 include · 1 exclude · 1 uncertain" in known
    assert "- Candidate searches: 2 (1 neighbour search, 1 pilot search)" in known
    assert known.endswith("Next: Step 4/7 Vocabulary: build MeSH and [tiab] terms for each searched concept.")
    assert "- Asthma (asthma): 2 terms — 1 MeSH · 1 text-word · 0 other" in sent[10]
    assert "- Concepts not searched: Exacerbations (screen)" in sent[10]
    assert "- Recall: seeds 2/2 (100.0%) · relevant 3/3 (100.0%)" in sent[11]
    assert "| Exacerbations | Screened | outcomes are reported unevenly |" in sent[2]
    assert "Round 1 (revision 1 of 2) packet written for v1" in sent[13]
    assert sent[-2].startswith("**PSB · Step 7/7 Deliver · Report**\nDelivered: final query validated live")
    final = sent[-1]
    assert "| seeds | seed" in final and progress.PRESS in final and "```text\n" in final
    code, status = psb(capsys, "status")
    assert all(status["stage_summaries_sent"].values()) and not any("psb progress" in t for t in status["todo"])


def test_messages_are_deterministic_and_logged(ws, capsys):
    build(ws, capsys)
    for stage in progress.STAGES:
        once = progress.render(ws, f"stage:{stage}")["text"]
        assert once == progress.render(ws, f"stage:{stage}")["text"]
    code, out = psb(capsys, "progress", "list")
    texts = [m["text"] for m in out["messages"]]
    assert [m["seq"] for m in out["messages"]] == list(range(1, len(texts) + 1))
    assert not any(re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}", t) for t in texts)


def test_progress_files_never_touch_the_delivery(ws, capsys):
    build(ws, capsys)
    before = validation.digest(validation.input_snapshot(ws))
    assert deliver.verify_delivery(ws)["ok"]
    text(capsys, "screen", "--exclude", "4")
    text(capsys, "progress", "known-records")
    text(capsys, "progress", "deliver")
    assert validation.digest(validation.input_snapshot(ws)) == before
    assert deliver.verify_delivery(ws)["ok"]


def test_status_reminds_without_blocking(ws, capsys):
    code, status = psb(capsys, "status")
    assert "send the Step 1 summary: psb progress intake" in status["todo"]
    assert "send the Step 2 summary: psb progress scope" in status["todo"]
    text(capsys, "progress", "intake")
    code, status = psb(capsys, "status")
    assert status["stage_summaries_sent"]["intake"] and not any("progress intake" in t for t in status["todo"])


def test_screen_rejects_bad_input_and_latest_decision_wins(ws, capsys):
    code, out = psb(capsys, "screen", "--include", "5", "--exclude", "5")
    assert code == 1 and "two decisions" in out["error"]
    code, out = psb(capsys, "screen", "--include", "abc")
    assert code == 1 and "not a PMID" in out["error"]
    code, out = psb(capsys, "screen")
    assert code == 1 and "at least one PMID" in out["error"]
    text(capsys, "screen", "--include", "5")
    message = text(capsys, "screen", "--exclude", "5")
    assert "- Not from a logged psb search: 1 screened → 0 include" in message
    assert "- Decisions changed from an earlier screen: 5" in message
    assert progress.decisions(ws)["5"]["decision"] == "exclude"


def test_screen_reads_a_decisions_file(ws, capsys, tmp_path):
    path = tmp_path / "decisions.json"
    path.write_text(json.dumps([{"pmid": "5", "decision": "include", "reason": "RCT in children"},
                                {"pmid": "7", "decision": "exclude"}]), encoding="utf-8")
    code, out = psb(capsys, "screen", "--file", str(path))
    assert code == 0 and out["decisions"] == {"include": ["5"], "exclude": ["7"], "uncertain": []}
    assert progress.decisions(ws)["5"]["reason"] == "RCT in children"


def test_preconditions_and_unknown_stages_fail_with_fixed_errors(ws, capsys):
    code, out = psb(capsys, "progress", "vocabulary")
    assert code == 1 and out["error"] == "strategy.json has no blocks yet"
    code, out = psb(capsys, "progress", "deliver")
    assert code == 1 and out["error"] == "psb report has not run yet"
    with pytest.raises(SystemExit):
        cli.main(["progress", "nonsense"])
    with pytest.raises(progress.ProgressError):
        progress.render(ws, "nonsense")


def test_free_text_is_cleaned_and_fenced():
    assert progress.clean("a\n\n  b\tc", 100) == "a b c"
    assert progress.clean("x" * 50, 10) == "x" * 9 + "…"
    assert progress.code("a`b") == "``a`b``"
    assert progress.code("`a") == "`` `a ``"
    assert progress.render(None, "intake-request", {"have_question": True})["text"].splitlines()[2].startswith("1. Known relevant")


def test_non_ascii_text_reaches_stdout_as_utf8(ws, capsysbinary):
    protocol = ws.protocol()
    protocol["question"] = "Sjögren’s syndrome → dry eye?"
    write_json(ws.root / "protocol.json", protocol)
    assert cli.main(["progress", "intake"]) == 0
    raw = capsysbinary.readouterr().out
    assert "Sjögren’s syndrome → dry eye?" in json.loads(raw.decode("utf-8"))["progress"]["text"]


GOLDEN = Path(__file__).parent / "golden" / "progress_sequence.md"


def test_whole_message_sequence_matches_golden(ws, capsys):
    """Every template, pinned. Regenerate deliberately with PSB_UPDATE_GOLDEN=1 and review the diff."""
    sent = "\n\n---\n\n".join(build(ws, capsys)).replace(str(ws.root), "<workspace>") + "\n"
    if os.environ.get("PSB_UPDATE_GOLDEN"):
        GOLDEN.parent.mkdir(exist_ok=True)
        GOLDEN.write_text(sent, encoding="utf-8")
    assert sent == GOLDEN.read_text(encoding="utf-8")


def prepared(ws, capsys):
    text(capsys, "set", "add", "seeds", "1", "2", "--role", "seed")
    write_json(ws.root / "strategy.json", STRATEGY)


def test_blocked_eval_never_claims_missing_sets(ws, capsys):
    text(capsys, "set", "add", "seeds", "1", "2", "--role", "seed")
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "asthma", "terms": ["cat*[tiab]"]}]})
    code, out = psb(capsys, "eval", "--brief")
    assert code == 1 and out["progress"]["text"] == (
        "**PSB · Step 5/7 Test & revise · Evaluation v1**\n"
        "v1: not measured\n"
        "- Recall: not measured (evaluation did not complete)\n"
        "- Checks: 1 blocker (short_truncation) · 1 need critic review · lint 1 error, 1 warning")


def test_zero_hit_candidate_searches_are_worded_by_purpose(ws, capsys):
    assert text(capsys, "sample", "--purpose", "pilot", "nothing[tiab]") == (
        "**PSB · Step 3/7 Known records · Pilot search**\n"
        "Pilot search: 0 records for `nothing[tiab]`\n"
        "- No records to screen")
    assert text(capsys, "sample", "--purpose", "prior-reviews", "nothing[tiab]").endswith("\n- No reviews to check")


def test_blocked_report_diagnostic_and_not_delivered_summary(ws, capsys):
    prepared(ws, capsys)
    text(capsys, "eval", "--brief")
    code, out = psb(capsys, "report")
    assert code == 1 and out["progress"]["text"] == (
        "**PSB · Step 7/7 Deliver · Report blocked**\n"
        "Not delivered: 1 blocker\n"
        "- Blockers: critic_missing\n"
        "- Diagnostic output: diagnostic-audit.md (unfinished; not a final query)")
    assert text(capsys, "progress", "deliver") == (
        "**PSB · Step 7/7 Deliver · Not delivered**\n"
        "No current delivery: no protected final query was issued\n"
        "- Delivery check: missing validation-manifest.json\n"
        "- Blockers at the last report: critic_missing\n"
        "- Diagnostic output: diagnostic-audit.md (unfinished; not a final query)")
    text(capsys, "critic", "packet")
    review(ws)
    code, out = psb(capsys, "report", "--diagnostic")
    assert code == 1 and out["progress"]["text"] == (
        "**PSB · Step 7/7 Deliver · Diagnostic check**\n"
        "Diagnostic only: no blockers found; psb report would deliver\n"
        "- Blockers: none\n"
        "- Diagnostic output: diagnostic-audit.md (unfinished; not a final query)")


def test_a_failing_message_never_changes_the_command_result(ws, capsys, monkeypatch):
    def broken(ws, data):
        raise TypeError("boom")
    monkeypatch.setitem(progress.EVENTS, "set", (3, broken))
    code, out = psb(capsys, "set", "add", "seeds", "1", "2", "--role", "seed")
    assert code == 0 and out["ok"] and out["pmids"] == ["1", "2"] and ws.get_set("seeds")["pmids"] == ["1", "2"]
    assert out["progress"]["text"] == (
        "**PSB · Step 3/7 Known records · set**\n"
        "Progress message unavailable (TypeError); the command itself ran: see its JSON result.")
    assert progress.messages(ws)[-1]["error"] == "TypeError: boom"


def test_malformed_critic_round_returns_json_not_a_crash(ws, capsys):
    prepared(ws, capsys)
    text(capsys, "eval", "--brief")
    text(capsys, "critic", "packet")
    write_json(ws.root / "critic" / "round-1.json", {"round": 1, "domains": [], "findings": "not a list"})
    code, out = psb(capsys, "critic", "check")
    assert code == 1 and not out["ok"] and out["problems"]
    message = out["progress"]["text"]
    assert message.startswith("**PSB · Step 6/7 Critic · Round 1 result**\nRound 1 (revision): 0 domains pass · 0 revise")
    assert "- Findings: 0 must-fix · 0 should-fix · 0 document" in message and "- Check: " in message
    write_json(ws.root / "critic" / "round-1.json", {"round": "one"})
    code, out = psb(capsys, "critic", "check")
    assert code == 1 and out["progress"]["text"] == (
        "**PSB · Step 6/7 Critic · Round file invalid**\n"
        "round-1.json was not checked: 1 problem: round must be an object with a positive integer round number\n"
        "- Fix the round file and run psb critic check again")


def test_mining_a_held_out_set_says_so(ws, capsys):
    text(capsys, "set", "add", "validation", "5", "6", "--role", "validation")
    write_json(ws.root / "strategy.json", STRATEGY)
    message = text(capsys, "terms", "rank", "--set", "validation", "--allow-held-out", "--budget", "0")
    assert message.splitlines()[1] == ("Mined candidate terms from 2 records (sets validation; includes held-out "
                                       "validation, which now count as development)")
    text(capsys, "set", "add", "seeds", "1", "2", "--role", "seed")
    assert "; held-out sets excluded)" in text(capsys, "terms", "rank", "--budget", "0")


def test_override_reports_the_latest_round_of_the_finding(ws, capsys):
    finding = {"id": "F1", "domain": "translation", "finding": "AND-ed population", "recommendation": "screen it",
               "status": "open"}
    write_json(ws.root / "critic" / "round-1.json",
               {"round": 1, "findings": [{**finding, "severity": "should-fix", "kind": "lexical"}]})
    write_json(ws.root / "critic" / "round-2.json",
               {"round": 2, "closing": True, "findings": [{**finding, "severity": "must-fix", "kind": "structural"}]})
    message = text(capsys, "critic", "override", "F1", "--reason", "population is reliably indexed")
    assert message.splitlines()[1] == "Overrode F1 (must-fix, structural) after the closing round"


def test_scope_reminder_after_confirmation(ws, capsys):
    protocol = ws.protocol()
    protocol["scope_confirmed"] = False
    write_json(ws.root / "protocol.json", protocol)
    assert text(capsys, "progress", "scope").endswith("\n".join(progress.SCOPE_DECISION))
    code, status = psb(capsys, "status")
    assert not any("Step 2" in t for t in status["todo"])
    protocol["scope_confirmed"] = True
    write_json(ws.root / "protocol.json", protocol)
    code, status = psb(capsys, "status")
    assert "send the Step 2 summary again (it changed since it was sent): psb progress scope" in status["todo"]


def test_scope_message_is_a_fixed_table(ws, capsys):
    """Rows by role, escaped cells, criteria in full, and the question even when notes exist."""
    protocol = ws.protocol()
    protocol.update(scope_confirmed=False, notes="Defaults used for depth and limits.", limits=[], concepts=[
        {"id": "setting", "name": "Primary care", "role": "optional", "rationale": "may narrow too far"},
        {"id": "outcome", "name": "Exacerbations", "role": "screen", "rationale": "reported unevenly"},
        {"id": "asthma", "name": "Asthma", "role": "search", "rationale": "condition | indexed"},
        {"id": "odd", "name": "Odd", "role": "maybe"},
        {"id": "child", "role": "search", "rationale": "population"},
    ])
    write_json(ws.root / "protocol.json", protocol)
    assert text(capsys, "progress", "scope") == "\n".join([
        "**PSB · Step 2/7 Scope · Summary**",
        "Question: Which treatments reduce asthma attacks in children?",
        "",
        "| Concept | Role | Why |",
        "|---|---|---|",
        "| Asthma | Searched | condition \\| indexed |",
        "| child | Searched | population |",
        "| Exacerbations | Screened | reported unevenly |",
        "| Primary care | Optional | may narrow too far |",
        "| Odd | maybe (unrecognised) | not recorded |",
        "",
        "2 searched · 1 screened · 1 optional concepts",
        "Limits (applied to the search): none",
        "",
        "Eligibility criteria (applied at screening):",
        "- Include: children with asthma",
        "- Include: any intervention",
        "- Exclude: case reports",
        "",
        *progress.SCOPE_MEANING,
        "",
        *progress.SCOPE_DECISION,
    ])


def test_confirmed_scope_keeps_the_table_and_drops_the_question(ws, capsys):
    protocol = ws.protocol()
    protocol.update(eligibility={})
    write_json(ws.root / "protocol.json", protocol)
    message = text(capsys, "progress", "scope")
    assert "| Concept | Role | Why |\n|---|---|---|\n| Asthma | Searched |" in message
    assert "Eligibility criteria (applied at screening): none recorded" in message
    assert progress.SCOPE_MEANING[0] not in message and progress.SCOPE_DECISION[0] not in message
    assert message.endswith("Scope confirmed by the user.\nNext: Step 3/7 Known records: add seeds, look for prior "
                            "reviews, run pilot and citation searches, and screen up to ~150 candidates (standard).")


def test_a_corrupt_attempt_does_not_break_status(ws, capsys):
    (ws.root / "attempts").mkdir(exist_ok=True)
    (ws.root / "attempts" / "broken.json").write_text("{", encoding="utf-8")
    code, status = psb(capsys, "status")
    assert code == 0 and any(t.startswith("progress state could not be read") for t in status["todo"])


def test_resolved_pmids_with_leading_zeros_are_found_and_attributed(ws, capsys):
    code, out = psb(capsys, "resolve", "0005", "000")
    assert code == 0 and out["resolved"] == {"0005": "5"}
    assert out["not_in_pubmed_or_after_as_of"] == [] and out["unresolved"] == ["000"]
    assert progress.batches(ws)[-1]["pmids"] == ["5"]
    assert "- Resolved identifiers (C1): 1 screened → 1 include" in text(capsys, "screen", "--include", "5")
