"""Gate B: verbose progress messages. The setting, bounded templates and their edge cases, equivalence
of the scientific work with verbose off and on, and the cost (see bench_verbose.py for the benchmark)."""

import itertools
import json
import time
import unicodedata
import uuid
from pathlib import Path

import pytest

import bench_verbose
from psb import allocation, cli, deliver, evaluate, holdout, progress, reserved, validation
from psb import workspace as workspace_module
from psb.workspace import Workspace, write_json
from test_closing_round import PASS, write_round
from test_disclosure import PROTOCOL, QUESTION, STRATEGY as TWO_TERMS, Private
from test_progress import STRATEGY, build, psb, text, ws  # noqa: F401 - ws is a fixture

SETTINGS = "progress-settings.json"


def verbose(workspace):
    progress.write_mode(workspace, "verbose")


def details(message: str) -> list[str]:
    return message.split("\nDetails:\n", 1)[1].splitlines() if "\nDetails:\n" in message else []


def bounded(message: str) -> None:
    lines = details(message)
    added = "\n".join(["Details:", *lines])
    assert len(added.split()) <= 80 and len(added) <= 800 and len([l for l in lines if "omitted" not in l]) <= 3
    assert not any(unicodedata.category(c)[0] == "C" for c in message.replace("\n", ""))


# -- the setting -------------------------------------------------------------------------------------

def test_the_setting_defaults_to_standard_and_round_trips(ws, capsys):
    code, out = psb(capsys, "progress", "mode")
    assert code == 0 and out == {"ok": True, "mode": "standard"} and not (ws.root / SETTINGS).exists()
    code, out = psb(capsys, "progress", "mode", "verbose")
    assert code == 0 and out["progress"]["text"] == (
        "**PSB · Progress messages**\nVerbose: completion messages now add up to three bounded details. Searches, "
        "screening and what stays private are unchanged.")
    assert json.loads((ws.root / SETTINGS).read_text(encoding="utf-8")) == {"version": 1, "mode": "verbose"}
    assert psb(capsys, "progress", "mode")[1]["mode"] == "verbose"
    code, out = psb(capsys, "progress", "mode", "standard")
    assert out["progress"]["text"].endswith("Standard: completion messages are back to their usual length.")
    assert psb(capsys, "progress", "mode")[1] == {"ok": True, "mode": "standard"}
    listed = psb(capsys, "progress", "list")[1]["messages"]
    assert [m["event"] for m in listed] == ["progress-mode", "progress-mode"]
    assert not list(ws.root.glob(".progress-settings-*"))


@pytest.mark.parametrize("content", ["{", "[]", '{"mode": "verbose"}', '{"version": 2, "mode": "verbose"}',
                                     '{"version": true, "mode": "verbose"}', '{"version": 1, "mode": "loud"}',
                                     '{"version": 1, "mode": "verbose", "extra": 1}'])
def test_an_invalid_setting_falls_back_with_a_notice_and_is_not_repaired(ws, capsys, content):
    (ws.root / SETTINGS).write_text(content, encoding="utf-8")
    code, out = psb(capsys, "progress", "mode")
    assert code == 0 and out["mode"] == "standard" and out["progress_notice"] == progress.SETTINGS_NOTICE
    text(capsys, "set", "add", "seeds", "1", "2", "--role", "seed")
    write_json(ws.root / "strategy.json", STRATEGY)
    code, out = psb(capsys, "eval", "--brief")
    assert out["progress_notice"] == progress.SETTINGS_NOTICE and not details(out["progress"]["text"])
    code, out = psb(capsys, "mesh", "lookup", "asthma")
    assert "progress" not in out and out["progress_notice"] == progress.SETTINGS_NOTICE
    assert (ws.root / SETTINGS).read_text(encoding="utf-8") == content
    psb(capsys, "progress", "mode", "verbose")  # setting it again replaces it
    assert progress.read_mode(ws) == ("verbose", None)


def test_a_failed_write_fails_and_keeps_the_previous_setting(ws, capsys, monkeypatch):
    verbose(ws)
    with monkeypatch.context() as patch:
        def broken(source, target):
            raise OSError("disk full")
        patch.setattr(progress.os, "replace", broken)
        code, out = psb(capsys, "progress", "mode", "standard")
    assert code == 1 and out["ok"] is False and "disk full" in out["error"]
    assert progress.read_mode(ws) == ("verbose", None) and not list(ws.root.glob(".progress-settings-*"))


def test_the_setting_needs_a_workspace_and_only_mode_takes_a_value(tmp_path, capsys, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("PSB_WORKSPACE", raising=False)
    assert cli.main(["progress", "mode", "verbose"]) == 1
    assert "no workspace found" in json.loads(capsys.readouterr().out)["error"]
    assert cli.main(["progress", "list", "verbose"]) == 1
    assert "only psb progress mode takes a value" in json.loads(capsys.readouterr().out)["error"]
    with pytest.raises(SystemExit):
        cli.main(["progress", "mode", "loud"])


def test_each_invocation_reads_the_current_setting(tmp_path, capsys, corpus):
    """The real cli.workspace() path: switching back and forth, one command at a time."""
    from test_disclosure import start
    root, _ = start(tmp_path, capsys, corpus, Private("qxz"))
    write_json(root / "strategy.json", TWO_TERMS)
    seen = []
    for mode in ("verbose", "standard", "verbose"):
        assert cli.main(["--workspace", str(root), "progress", "mode", mode]) == 0
        capsys.readouterr()
        assert cli.main(["--workspace", str(root), "eval", "--brief"]) == 0
        seen.append(bool(details(json.loads(capsys.readouterr().out)["progress"]["text"])))
    assert seen == [True, False, True]


# -- templates ---------------------------------------------------------------------------------------

def test_standard_mode_does_no_detail_work(ws, capsys, monkeypatch):
    calls = []

    def spy(workspace, data):
        calls.append(1)
        raise AssertionError("detail work in standard mode")
    for name in list(progress.DETAILS):
        monkeypatch.setitem(progress.DETAILS, name, spy)
    sent = build(ws, capsys)
    code, out = psb(capsys, "mesh", "lookup", "asthma")
    assert calls == [] and "progress" not in out and not any("Details:" in m for m in sent)
    assert not any("progress_notice" in json.dumps(m) for m in sent)


def test_discovery_details_explain_the_route_with_examples(ws, capsys):
    verbose(ws)
    text(capsys, "set", "add", "seeds", "1", "2", "--role", "seed")
    message = text(capsys, "neighbors", "--set", "seeds", "--links", "similar,refs", "--exclude-known")
    assert details(message) == [
        "- Method: similar articles and reference lists (backward) of 2 records, up to 50 per record and link, "
        "ranked by the number of linking records, then score",
        "- Example: PMID 5, linked from 2 records", "- Example: PMID 6, linked from 1 record", "- 2 more details omitted"]
    assert details(text(capsys, "sample", "--purpose", "pilot", "asthma*[tiab]")) == [
        "- Method: the first 3 records of 3, in the order PubMed returned them",
        "- PubMed translation: `asthma*[tiab]`", "- Example: PMID 1, `Record 1`", "- 2 more details omitted"]
    assert details(text(capsys, "sample", "--purpose", "noise-check", "--random", "--n", "2", "child*[tiab]"))[0] == (
        "- Method: 2 records of 4 from offset 0, the offset chosen at random with seed 1")
    assert details(text(capsys, "sample", "--purpose", "pilot", "nothing[tiab]")) == [
        "- Method: no records matched, so none were shown", "- PubMed translation: `nothing[tiab]`"]
    assert details(text(capsys, "count", "--purpose", "noise-check", "child*[tiab]")) == [
        "- PubMed translation: `child*[tiab]`"]
    assert details(text(capsys, "resolve", "0005", "10.1/none")) == [
        "- Method: PMIDs as given; DOIs by a [doi] search that must return exactly one record; every PMID then "
        "checked against PubMed"]


def test_mesh_messages_appear_only_in_verbose_mode(ws, capsys):
    code, out = psb(capsys, "mesh", "lookup", "asthma")
    assert code == 0 and "progress" not in out
    verbose(ws)
    assert text(capsys, "mesh", "lookup", "asthma") == (
        "**PSB · Step 4/7 Vocabulary · MeSH lookup**\n`asthma`: 1 candidate record returned\nDetails:\n"
        "- `Asthma` (D001249, descriptor)")
    assert text(capsys, "mesh", "lookup", "nothing at all") == (
        "**PSB · Step 4/7 Vocabulary · MeSH lookup**\n`nothing at all`: 0 candidate records returned")
    assert text(capsys, "mesh", "show", "Asthma", "--no-counts") == "\n".join([
        "**PSB · Step 4/7 Vocabulary · MeSH record**", "Details retrieved for `Asthma` (D001249, descriptor)",
        "- PubMed counts: not requested (--no-counts)", "Details:", "- Scope note: none returned",
        "- Entry terms: 1 returned, e.g. `Bronchial Asthma`", "- Narrower headings: 0 returned"])
    # Measured zero stays zero; the labels are PubMed's own.
    assert "- PubMed counts: `[Mesh]` 3 · `[Mesh:noexp]` 0" in text(capsys, "mesh", "show", "Asthma")


def test_mesh_lookup_lists_the_exact_heading_first():
    """NCBI's order is not by relevance (live: `asthma` returned Asthma, Occupational before Asthma)."""
    matches = [{"name": "Asthma, Occupational", "ui": "D059366", "type": "descriptor"},
               {"name": "Dyspnea, Paroxysmal", "ui": "D004418", "type": "descriptor"},
               {"name": "Asthma", "ui": "D001249", "type": "descriptor"},
               {"name": "Status Asthmaticus", "ui": "D013224", "type": "descriptor"}]
    rows = progress.section(progress.DETAILS["mesh-lookup"](None, {"query": "  ASTHMA ", "matches": matches}))
    assert rows == ["Details:", "- `Asthma` (D001249, descriptor)", "- `Asthma, Occupational` (D059366, descriptor)",
                    "- `Dyspnea, Paroxysmal` (D004418, descriptor)", "- 1 more detail omitted"]


def test_mesh_details_label_supplementary_records_and_escape_untrusted_text(ws, capsys, monkeypatch):
    name = "Sjögren`s ‮compound\x07 " + "x" * 200
    children = [{"ds_meshui": f"D{n:06d}", "ds_meshterms": [f"Child {n}"]} for n in range(100)]
    records = {"qxz": {"ds_meshui": "C000001", "ds_meshterms": [name, "Qxz compound", "Entry *one*", "Entry | two"],
                       "ds_scopenote": "Use **bold** <b>|pipes|</b>\x1b[31m " + "word " * 100,
                       "ds_idxlinks": [{"children": [str(68000000 + n) for n in range(100)]}]},
               **{str(68000000 + n): row for n, row in enumerate(children)}}
    monkeypatch.setattr(ws.pubmed, "mesh_records", records)
    verbose(ws)
    message = text(capsys, "mesh", "show", "Qxz compound")
    bounded(message)
    lines = message.splitlines()
    assert lines[1].startswith("Details retrieved for ``Sjögren`s compound ") and lines[1].endswith("…`` (C000001, supplementary)")
    assert lines[2] == "- PubMed counts: `[nm]` 0" and "‮" not in message and "\x1b" not in message
    assert "- Scope note: Use \\*\\*bold\\*\\* \\<b\\>\\|pipes\\|\\</b\\> \\[31m word" in message
    assert "- Narrower headings: 100 returned (the list stops at 100), e.g. `Child 0`, `Child 1`, `Child 2`" in message


def test_term_mining_examples_and_their_limits(ws, capsys):
    verbose(ws)
    text(capsys, "set", "add", "seeds", "1", "2", "--role", "seed")
    write_json(ws.root / "strategy.json", STRATEGY)
    rows = details(text(capsys, "terms", "rank", "--budget", "3"))
    assert rows and all(r.startswith("- `") and " records · " in r for r in rows if "omitted" not in r)
    assert details(text(capsys, "terms", "rank", "--budget", "0")) == [
        "- Examples: none; no candidates were scored (background-count budget 0)"]
    text(capsys, "set", "add", "old", "5", "6", "--purpose", "comparison")
    assert details(text(capsys, "terms", "rank", "--set", "old", "--include-comparison", "--budget", "3")) == [
        "- Examples withheld: comparison records were mined, so the candidates' development-only provenance is not "
        "established"]


def test_miss_details_give_vocabulary_from_development_records_only(ws, capsys):
    verbose(ws)
    text(capsys, "set", "add", "seeds", "1", "3", "--role", "seed")
    text(capsys, "set", "add", "old", "6", "--purpose", "comparison")
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "asthma", "name": "Asthma", "terms": ['"Asthma"[Mesh]']}]})
    psb(capsys, "eval", "--brief")
    code, out = psb(capsys, "terms", "miss")
    rows = details(out["progress"]["text"])
    assert {m["pmid"] for m in out["misses"]} == {"3", "6"}  # the scientific output is unchanged
    assert rows[0].startswith("- PMID 3: fails asthma; ")
    assert rows[1] == "- PMID 6: fails asthma (comparison record: no vocabulary examples)"


def eval_details(ws, capsys, strategy, *argv) -> list[str]:
    write_json(ws.root / "strategy.json", strategy)
    code, out = psb(capsys, "eval", "--brief", *argv)
    bounded(out["progress"]["text"])
    return details(out["progress"]["text"])


def test_eval_details_put_warnings_first_and_label_coverage(ws, capsys):
    verbose(ws)
    assert eval_details(ws, capsys, STRATEGY) == ["- Block coverage: not measured (no known-record sets)"]
    text(capsys, "set", "add", "seeds", "1", "2", "3", "5", "6", "--role", "seed")
    three = {"blocks": [*STRATEGY["blocks"], {"id": "trial", "name": "Trials", "terms": ["child*[tiab]", "nothing[tiab]"]}]}
    assert eval_details(ws, capsys, three) == [
        "- Zero hits: line 8 `nothing[tiab]`",
        "- Ablation: without `trial`, 1 more known record retrieved (5 records)",
        "- Block `asthma`: 5/5 (development records)",
        "- 4 more details omitted"]
    assert eval_details(ws, capsys, three, "--no-term-counts")[0] == "- Ablation: without `trial`, 1 more known record retrieved (5 records)"
    assert eval_details(ws, capsys, STRATEGY, "--no-term-counts")[0] == "- Term checks: not run (--no-term-counts)"
    text(capsys, "set", "add", "old", "2", "7", "--purpose", "comparison")  # overlapping, and one outside development
    rows = eval_details(ws, capsys, {**STRATEGY, "combine": "asthma AND child"})
    assert "- Block `asthma`: 5/6 (combined known-record coverage)" in rows


def test_comparison_only_coverage_is_labelled_combined(ws, capsys):
    verbose(ws)
    text(capsys, "set", "add", "old", "1", "6", "7", "--purpose", "comparison")
    rows = eval_details(ws, capsys, STRATEGY)
    assert "- Block `asthma`: 2/3 (combined known-record coverage)" in rows


def test_eval_details_say_what_was_not_run(ws, capsys, monkeypatch):
    verbose(ws)
    text(capsys, "set", "add", "seeds", "1", "2", "--role", "seed")
    one = {"blocks": [STRATEGY["blocks"][0]]}
    write_json(ws.root / "strategy.json", one)
    data = {"evaluation": evaluate.evaluate(ws, term_counts=False), "term_counts": False}
    rows = [r for _, _, r in sorted(progress.DETAILS["eval"](ws, data))]
    assert rows == ["- Term checks: not run (--no-term-counts)", "- Block `asthma`: 2/2 (development records)",
                    "- Ablation: not run (one block)"]
    combined = {**STRATEGY, "combine": "asthma AND child"}
    write_json(ws.root / "strategy.json", combined)
    rows = [r for _, _, r in sorted(progress.DETAILS["eval"](ws, {"evaluation": evaluate.evaluate(ws)}))]
    assert "- Ablation: skipped: ablation needs the default AND combination" in rows
    write_json(ws.root / "strategy.json", {"blocks": [{"id": "asthma", "terms": ["cat*[tiab]"]}]})
    code, out = psb(capsys, "eval", "--brief")  # blocked: the evaluation did not complete
    assert details(out["progress"]["text"]) == ["- Details: not available (the evaluation did not complete)"]


def test_a_failing_detail_renderer_sends_the_standard_message_with_a_notice(ws, capsys, monkeypatch):
    text(capsys, "set", "add", "seeds", "1", "2", "--role", "seed")
    write_json(ws.root / "strategy.json", STRATEGY)
    psb(capsys, "eval", "--brief")
    standard = psb(capsys, "eval", "--brief")[1]["progress"]["text"]  # a re-evaluation, like the next one
    verbose(ws)

    def broken(workspace, data):
        raise KeyError("boom")
    monkeypatch.setitem(progress.DETAILS, "eval", broken)
    code, out = psb(capsys, "eval", "--brief")
    assert code == 0 and out["ok"] and out["progress"]["text"] == standard
    assert out["progress_notice"] == "Verbose details could not be prepared (KeyError); the standard message was sent"


def test_sections_are_capped_ordered_and_say_what_was_left_out():
    rows = [(2, i, f"- info {i}") for i in range(5)] + [(1, 9, "- warning late"), (0, 7, "- error")]
    expected = ["Details:", "- error", "- warning late", "- info 0", "- 4 more details omitted"]
    assert progress.section(rows) == expected and progress.section(list(reversed(rows))) == expected
    long = [(2, i, "- " + "word " * 30) for i in range(3)]
    assert progress.section(long) == ["Details:", long[0][2], long[1][2], "- 1 more detail omitted"]
    assert progress.section([(2, 0, "- " + "x" * 900)]) == ["Details:", "- 1 more detail omitted"]
    assert progress.section([]) == []
    for size in (1, 7, 40, 120, 300):
        many = [(i % 3, i, "- row " + "é" * (size % 97) + " w" * (size % 23)) for i in range(size % 11 + 1)]
        chosen = progress.section(many)
        added = "\n".join(chosen)
        assert len(added.split()) <= 80 and len(added) <= 800 and len(chosen) <= 5
        assert all(line in {r for _, _, r in many} for line in chosen[1:] if "omitted" not in line)


def test_untrusted_text_is_one_line_and_escaped():
    assert progress._plain("a\x00b​c‮d\n\te", 50) == "a b c d e"
    assert progress._escaped("*x* _y_ [z](u) <b> `c` | # ~", 80) == "\\*x\\* \\_y\\_ \\[z\\](u) \\<b\\> \\`c\\` \\| \\# \\~"
    assert progress._term("a`b") == "``a`b``" and progress._term("") == "`?`"
    cut = progress._escaped("*" * 300, 20)
    assert cut.endswith("…") and "\\*" in cut and not cut.endswith("\\…")


# -- equivalence -------------------------------------------------------------------------------------

def fix_clocks(monkeypatch):
    stamp = lambda: "2026-01-01T00:00:00+00:00"  # noqa: E731
    for module in (workspace_module, allocation, cli, deliver, evaluate, holdout, reserved):
        monkeypatch.setattr(module, "now", stamp)
    ticks, ids = itertools.count(1), itertools.count(1)
    monkeypatch.setattr(time, "time_ns", lambda: next(ticks))
    monkeypatch.setattr(uuid, "uuid4", lambda: uuid.UUID(int=next(ids)))


def scientific_run(directory: Path, mode: str, capsys, corpus, monkeypatch) -> tuple[list, list, Path]:
    """One whole build with fixed clocks; returns each command's JSON (presentation removed) and the
    request trace. Commands run from the workspace, so the logged argv carries no path."""
    fix_clocks(monkeypatch)
    v = Private("qxz")
    atoms, records, links, extra = v.corpus()
    transport = corpus(atoms, records, links, **extra)
    directory.mkdir()
    monkeypatch.chdir(directory)
    monkeypatch.delenv("PSB_WORKSPACE", raising=False)
    outputs = []

    def call(*argv):
        code = cli.main(list(argv))
        out = json.loads(capsys.readouterr().out)
        outputs.append((argv, code, {k: v for k, v in out.items() if k not in {"progress", "progress_notice"}}))
        assert code == 0 or argv[0] == "report", (argv, out)
        return out

    call("init", "run", "--question", QUESTION)
    root = (directory / "run").resolve()
    monkeypatch.chdir(root)
    write_json(root / "protocol.json", {**json.loads((root / "protocol.json").read_text(encoding="utf-8")), **PROTOCOL})
    if mode == "verbose":
        progress.write_mode(Workspace(root), "verbose")
    call("set", "add", "seeds", "1", "2", "--role", "seed")
    for argv in v.worker(Path(".")):
        call(*argv)
    call("sample", "--purpose", "pilot", v.review)
    call("neighbors", "1", "--links", "similar")
    call("resolve", "1")
    call("allocate", "--preview")
    call("allocate", "--keep-holdout")
    call("mesh", "lookup", "asthma")
    call("mesh", "show", "Asthma")
    write_json(root / "strategy.json", TWO_TERMS)
    call("eval", "--note", "first draft")
    call("terms", "rank", "--budget", "3")
    call("terms", "miss")
    call("critic", "packet")
    write_round(Workspace(root), 1, [], PASS)
    call("critic", "check")
    call("holdout-test")
    call("report")
    call("progress", "deliver")
    return outputs, transport.calls, root


def files(root: Path) -> dict[str, object]:
    """Every workspace file but the presentation-only ones; cache entries without their storage time."""
    found = {}
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        name = path.relative_to(root).as_posix()
        if name in {"progress.jsonl", SETTINGS}:
            continue
        content = path.read_text(encoding="utf-8").replace(json.dumps(str(root))[1:-1], "<root>").replace(str(root), "<root>")
        if "/.cache/" in f"/{name}":
            content = {k: v for k, v in json.loads(content).items() if k != "stored_at"}
        found[name] = content
    return found


def test_verbose_mode_changes_nothing_but_the_messages(tmp_path, capsys, corpus, monkeypatch):
    runs = {}
    for mode in ("standard", "verbose"):
        outputs, calls, root = scientific_run(tmp_path / mode, mode, capsys, corpus, monkeypatch)
        text_of = json.dumps(outputs, ensure_ascii=False).replace(json.dumps(str(root))[1:-1], "<root>")
        runs[mode] = {"outputs": json.loads(text_of), "calls": calls, "files": files(root), "root": root}
    standard, verbose_run = runs["standard"], runs["verbose"]
    assert standard["calls"] == verbose_run["calls"]  # no extra request, in the same order
    assert standard["outputs"] == verbose_run["outputs"]
    assert standard["files"] == verbose_run["files"]
    assert any("Details:" in m["text"] for m in progress.messages(Workspace(verbose_run["root"])))
    for run in runs.values():
        ws = Workspace(run["root"])
        assert deliver.verify_delivery(ws)["ok"]
    # Adding or switching the setting after delivery leaves the delivery verifiable.
    ws = Workspace(standard["root"])
    snapshot = validation.digest(validation.input_snapshot(ws))
    for mode in ("verbose", "standard"):
        assert cli.main(["--workspace", str(ws.root), "progress", "mode", mode]) == 0
        assert cli.main(["--workspace", str(ws.root), "progress", "deliver"]) == 0
        capsys.readouterr()
        assert deliver.verify_delivery(ws)["ok"] and validation.digest(validation.input_snapshot(ws)) == snapshot


# -- cost --------------------------------------------------------------------------------------------

def test_the_benchmark_adds_bounded_text_and_no_requests(tmp_path):
    result = bench_verbose.measure(tmp_path, runs=1)
    standard, verbose_run = result["standard"], result["verbose"]
    assert standard["requests"] == verbose_run["requests"] and standard["trace"] == verbose_run["trace"]
    assert verbose_run["messages"] - standard["messages"] == bench_verbose.MESH_COMMANDS  # MeSH messages only
    assert 0 < verbose_run["relay_chars"] - standard["relay_chars"] <= 801 * verbose_run["messages"]
    assert all(len(added) <= 800 for added in verbose_run["sections"])
