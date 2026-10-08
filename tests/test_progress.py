"""Standardised progress messages: fixed templates, deterministic text, no effect on delivery."""

import json

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
        "- Shown for screening: 3 records as candidate batch C2")
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
    assert "- Exacerbations (outcome): screen — outcomes are reported unevenly" in sent[2]
    assert "Round 1 (revision 1 of 2) packet written for v1" in sent[13]
    assert sent[-2].startswith("**PSB · Step 7/7 Deliver · Report**\nDelivered: final query validated live")
    final = sent[-1]
    assert "| seeds | seed" in final and progress.PRESS in final and "```text\n" in final
    code, status = psb(capsys, "status")
    assert all(status["progress"].values()) and not any("psb progress" in t for t in status["todo"])


def test_messages_are_deterministic_and_logged(ws, capsys):
    build(ws, capsys)
    for stage in progress.STAGES:
        once = progress.render(ws, f"stage:{stage}")["text"]
        assert once == progress.render(ws, f"stage:{stage}")["text"]
    code, out = psb(capsys, "progress", "list")
    texts = [m["text"] for m in out["messages"]]
    assert [m["seq"] for m in out["messages"]] == list(range(1, len(texts) + 1))
    assert all("seq" not in t and "20" + "26-" not in t for t in texts)


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
    assert status["progress"]["intake"] and not any("progress intake" in t for t in status["todo"])


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
