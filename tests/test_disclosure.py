"""Gate A: private discovery and screening never reach builder-facing output.

Every command runs through the real ``cli.main()`` and ``cli.workspace()``. Each invocation's Workspace
builds the real PubMed client over an in-memory corpus (``conftest.CorpusTransport``), so the request log
and the caches are the production ones. A marker is planted in everything private: titles, abstracts,
indexing, queries, identifiers, reasons, source references, study groups, decision-file names and an
exception message. Builder-facing outputs are checked for the marker; the private outputs for content.
"""

import hashlib
import json

import pytest

from conftest import record
from psb import allocation, cli, deliver, disclosure, progress, reserved, validation
from psb.workspace import Workspace, write_json
from test_closing_round import PASS, write_round

SEEDS = ["1", "2"]
QUESTION = "Which treatments reduce asthma attacks?"
PROTOCOL = {"depth": "standard", "scope_confirmed": True, "as_of": None,
            "concepts": [{"id": "asthma", "name": "Asthma", "role": "search", "rationale": "the condition"}],
            "eligibility": {"include": ["asthma trials"], "exclude": []}}
STRATEGY = {"blocks": [{"id": "asthma", "name": "Asthma", "terms": ['"Asthma"[Mesh]', "asthma*[tiab]"]}], "limits": []}
STATE = ["- Records with a screening decision so far (all contexts): {n} of ~150 (standard)", "- Allocation is pending."]


class Private:
    """One variant of the private content: ``mark`` is planted in it, ``base`` places its PMIDs. With
    ``swap`` the screener excludes the sixth record and includes the nineteenth instead: the same counts."""

    def __init__(self, mark: str, base: int = 100, swap: bool = False):
        self.mark, self.upper = mark, mark.upper()
        self.pmids = [str(base + i) for i in range(24)]
        self.include, self.exclude = self.pmids[:18], self.pmids[18:]
        if swap:
            self.include = [p for p in self.include if p != self.pmids[5]] + [self.pmids[18]]
            self.exclude = [self.pmids[5]] + self.pmids[19:]
        self.review, self.pilot = f"{mark}review[tiab]", f"{mark}pilot[tiab]"
        self.nothing, self.bad = f"{mark}nothing[tiab]", f"{mark}bad[tiab]"
        self.doi, self.pmcid = f"10.1000/{mark}-doi", f"PMC{base}9"

    def corpus(self) -> tuple:
        p, up = self.pmids, self.upper
        atoms = {self.review: set(p[:5]), self.pilot: set(p[5:20]), self.nothing: set(), f'"{self.doi}"[doi]': {p[20]},
                 '"Asthma"[Mesh]': {*SEEDS, *p[:14]}, "asthma*[tiab]": {*SEEDS, *p}}
        records = {x: record(x, f"{up} title {x}", f"{up} abstract {x}", mesh=[f"{up} heading"]) for x in p}
        records.update({s: record(s, f"Seed {s}", "Asthma in children.") for s in SEEDS})
        links = {("1", "similar"): [(p[21], 30), (p[22], 20)], ("2", "similar"): [(p[23], 10)],
                 ("1", "refs"): [(p[0], 0)], ("2", "refs"): []}
        return atoms, records, links, {"ids": {self.pmcid: p[1]},
                                       "errors": {self.bad: f"Cannot search because {up}-ERROR is not a term"}}

    def files(self, directory) -> tuple:
        up = self.upper
        decisions = directory / f"{self.mark}-decisions.json"
        rows = [{"pmid": x, "decision": "include", "reason": f"{up} reason {x}", "group": f"{up}-GROUP-{x}",
                 "evidence": "abstract", "source_ref": f"{up} Table {x}"} for x in self.include]
        rows += [{"pmid": x, "decision": "exclude", "reason": f"{up} not a trial {x}", "evidence": "title"}
                 for x in self.exclude]
        decisions.write_text(json.dumps(rows), encoding="utf-8")
        mixed = directory / f"{self.mark}-mixed.json"
        mixed.write_text(json.dumps([
            {"pmid": "2", "decision": "include", "context": "builder", "reason": "the seed meets the criteria"},
            {"pmid": self.exclude[-1], "decision": "exclude", "context": "separate", "reason": f"{up} second look",
             "source_ref": f"{up} p.4"}]), encoding="utf-8")
        malformed = directory / f"{self.mark}-malformed.json"
        malformed.write_text("[{" + up, encoding="utf-8")
        bad_row = directory / f"{self.mark}-badrow.json"
        bad_row.write_text(json.dumps([{"pmid": f"{up}1", "decision": "include"}]), encoding="utf-8")
        return decisions, mixed, malformed, bad_row

    def worker(self, directory) -> list[list[str]]:
        decisions, mixed, _, _ = self.files(directory)
        return [["resolve", "--screening", self.doi, self.pmcid],
                ["sample", "--screening", "--purpose", "prior-reviews", self.review],
                ["sample", "--screening", "--purpose", "pilot", "--n", "20", self.pilot],
                ["sample", "--screening", "--purpose", "pilot", self.nothing],
                ["neighbors", "--screening", "--set", "seeds", "--links", "similar,refs"],
                ["fetch", "--screening", "--abstracts", *self.pmids],
                ["count", "--screening", "--purpose", "pilot", self.pilot],
                ["screen", "--context", "separate", "--file", str(decisions)],
                ["screen", "--file", str(mixed)]]

    def failing(self, directory) -> list[list[str]]:
        _, _, malformed, bad_row = self.files(directory)
        return [["screen", "--context", "separate", "--file", str(directory / f"{self.mark}-missing.json")],
                ["screen", "--context", "separate", "--file", str(malformed)],
                ["screen", "--file", str(bad_row)],
                ["sample", "--screening", self.pilot],
                ["count", "--screening", "--purpose", "pilot", self.bad],
                ["fetch", "--screening"]]


def psb(capsys, root, *argv):
    code = cli.main(["--workspace", str(root), *argv])
    return code, json.loads(capsys.readouterr().out)


def start(directory, capsys, corpus, variant: Private, mode: str = "standard"):
    """A workspace with confirmed scope and two seeds, and the variant's corpus behind every client."""
    atoms, records, links, extra = variant.corpus()
    transport = corpus(atoms, records, links, **extra)
    directory.mkdir(parents=True, exist_ok=True)
    root = directory / "run"
    assert cli.main(["init", str(root), "--question", QUESTION]) == 0
    capsys.readouterr()
    protocol = json.loads((root / "protocol.json").read_text(encoding="utf-8"))
    write_json(root / "protocol.json", {**protocol, **PROTOCOL})
    if mode != "standard":
        assert psb(capsys, root, "progress", "mode", mode)[0] == 0
    code, _ = psb(capsys, root, "set", "add", "seeds", *SEEDS, "--role", "seed")
    assert code == 0
    return root, transport


def run_worker(capsys, root, variant: Private, directory) -> tuple[list[dict], list[dict]]:
    done = []
    for argv in variant.worker(directory):
        code, out = psb(capsys, root, *argv)
        assert code == 0, (argv, out)
        done.append(out)
    failed = []
    for argv in variant.failing(directory):
        code, out = psb(capsys, root, *argv)
        assert code == 1 and out["ok"] is False, (argv, out)
        failed.append(out)
    return done, failed


def views(capsys, root) -> dict[str, dict]:
    """What the builder reads: status, the Step 3 summary, the message list and the log tail."""
    found = {}
    for name, argv in {"status": ["status"], "known": ["progress", "known-records"], "list": ["progress", "list"],
                       "log": ["log", "--tail", "1000"]}.items():
        code, out = psb(capsys, root, *argv)
        assert code == 0, (name, out)
        found[name] = out
    return found


def assert_clean(mark: str, **outputs) -> None:
    for name, value in outputs.items():
        text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)
        at = text.lower().find(mark)
        assert at < 0, f"{name} leaks private content: {text[max(0, at - 100):at + 100]!r}"


def comparable(found: dict[str, dict], root) -> dict:
    """Builder views with the workspace path and log timestamps (permitted operational metadata) removed."""
    text = json.dumps(found, ensure_ascii=False).replace(json.dumps(str(root))[1:-1], "<ws>")
    data = json.loads(text)
    for row in data["log"]["tail"]:
        row.pop("ts", None)
    return data


# -- the whole private workflow ------------------------------------------------------------------

@pytest.mark.parametrize("mode", ["standard", "verbose"])
def test_private_workflow_never_reaches_builder_outputs(tmp_path, capsys, corpus, mode):
    """In verbose mode too: privacy comes before verbosity, so every restricted text is the same."""
    v = Private("qxz")
    root, transport = start(tmp_path, capsys, corpus, v, mode)
    done, failed = run_worker(capsys, root, v, tmp_path)
    resolve, review, pilot, nothing, neighbours, fetched, counted, screened, mixed = done

    # The separate context still gets the full scientific results it screens from.
    assert resolve["resolved"] == {v.doi: v.pmids[20], v.pmcid: v.pmids[1]}
    assert [r["title"] for r in review["records"]] == [f"QXZ title {p}" for p in v.pmids[:5]]
    assert len(pilot["records"]) == 15 and nothing["count"] == 0
    assert {r["pmid"] for r in neighbours["rows"]} == {v.pmids[0], *v.pmids[21:]}
    assert fetched["found"] == 24 and fetched["records"][0]["abstract"] == f"QXZ abstract {v.pmids[0]}"
    assert counted["count"] == 15
    assert screened["decisions"]["include"] == v.include and mixed["recorded"] == 2

    # Each restricted invocation says only what is permitted, and its stored row is the same text.
    head = "**PSB · Step 3/7 Known records · {}**"
    lead = "Run in the separate screening context; details are kept private."
    expected = [
        [head.format("Identifier resolution"), lead, "- Identifiers processed: 2", *STATE],
        [head.format("Prior-review search"), lead, "- Records processed: 5", *STATE],
        [head.format("Pilot search"), lead, "- Records processed: 15", *STATE],
        [head.format("Pilot search"), lead, "- Records processed: 0", *STATE],
        [head.format("Similar articles + Citation search, backward"), lead, "- Records processed: 4", *STATE],
        [head.format("Records retrieved"), lead, "- Records processed: 24", *STATE],
        [head.format("Pilot search"), lead, *STATE],
        [head.format("Screening"), "Recorded decisions for 24 candidates in the separate screening context; details "
                                   "are kept private.", *STATE],
        [head.format("Screening"), "Recorded decisions for 2 candidates; detailed attribution is withheld.", *STATE],
    ]
    counts = [0, 0, 0, 0, 0, 0, 0, 24, 25]
    for out, lines, n in zip(done, expected, counts):
        assert out["progress"]["text"] == "\n".join(lines).format(n=n)
    stored = {m["seq"]: m for m in progress.messages(Workspace(root))}
    assert all(stored[o["progress"]["seq"]]["text"] == o["progress"]["text"] for o in done)

    # A failed restricted command: the raw error reaches stdout (the separate context) and the private
    # log only; the message and its stored row are fixed.
    operations = ["Screening", "Screening", "Screening", "A candidate search", "A search count", "Record retrieval"]
    for out, operation in zip(failed, operations):
        assert out["progress"]["text"] == "\n".join([
            "**PSB · Step 3/7 Known records · Separate screening**",
            f"{operation} did not complete in the separate screening context; details are kept private.",
            *STATE]).format(n=25)
    stored = {m["seq"]: m for m in progress.messages(Workspace(root))}
    assert all(set(stored[o["progress"]["seq"]]) == {"event", "step", "text", "seq", "sha256", "disclosure_version"}
               for o in failed)
    assert "QXZ-ERROR" in failed[4]["error"] and "qxz-missing.json" in failed[0]["error"]
    private_log = (root / "screening" / "log.jsonl").read_text(encoding="utf-8")
    assert "QXZ-ERROR" in private_log and "qxz-missing.json" in private_log and v.pilot in private_log

    # Recorded exposure and scientific metadata are untouched by presentation.
    ws = Workspace(root)
    latest = progress.decisions(ws)
    assert latest["2"]["context"] == "builder" and latest[v.exclude[-1]]["context"] == "separate"
    assert latest[v.pmids[0]]["group"] == f"QXZ-GROUP-{v.pmids[0]}"
    assert {e["pmid"] for e in reserved.events(ws)} == set(SEEDS)  # private commands recorded no exposure
    batches = progress.batches(ws)
    assert [b["via"] for b in batches] == ["resolve", "prior-reviews", "pilot", "neighbors:similar,refs"]
    assert all(b["private"] and b["query"] is None and b["from"] == [] for b in batches)
    raw = [json.loads(line) for line in (root / "screening" / "batches.jsonl").read_text(encoding="utf-8").splitlines()]
    assert [b["batch"] for b in raw] == [b["batch"] for b in batches] and raw[2]["query"] == v.pilot
    assert raw[3]["from"] == SEEDS

    before = views(capsys, root)
    code, preview = psb(capsys, root, "allocate", "--preview")
    assert code == 0 and (preview["N"], preview["U"], preview["H"]) == (20, 18, 6)
    assert preview["unscreened_development"] == ["1"]
    known = before["known"]["progress"]["text"]
    assert "- Eligible, not yet allocated: 18 records from the separate screening context (not listed)" in known
    assert not any(p in known for p in v.pmids)
    assert "- Screening: 25 screened → 19 include · 6 exclude · 0 uncertain (separate context 24 · builder 1)" in known

    # Origins come from the private batches; the freeze and its bindings are unchanged.
    proposal = allocation.propose(ws)
    origins = {u["id"]: u["origins"] for u in proposal["units"]}
    assert origins[v.pmids[0]] == ["citation-backward", "prior-review", "similar-articles"]
    assert origins[v.pmids[1]] == ["prior-review", "user-supplied"]
    assert origins[v.pmids[6]] == ["pilot-search"] and origins["1"] == ["user-supplied"]
    code, frozen = psb(capsys, root, "allocate", "--keep-holdout")
    assert code == 0 and frozen["allocation"]["holdout"] == {"units": 6, "records": 6}
    assert ws.allocation()["bindings"]["screening_rows"] == 26

    # A later private include is counted, never listed.
    code, late = psb(capsys, root, "screen", "--context", "separate", "--include", "999")
    assert code == 0 and "- Allocation is pending." not in late["progress"]["text"]
    after = views(capsys, root)
    assert ("- Included after the allocation, not in a set: 1 record from the separate screening context (not listed)"
            in after["known"]["progress"]["text"])

    write_json(root / "strategy.json", STRATEGY)
    code, evaluation = psb(capsys, root, "eval", "--brief")
    assert code == 0, evaluation
    assert ("\nDetails:\n" in evaluation["progress"]["text"]) is (mode == "verbose")  # the mode really applied
    code, packet = psb(capsys, root, "critic", "packet")
    assert code == 0
    packet_text = (root / "critic" / "packet-1.md").read_text(encoding="utf-8")

    assert_clean("qxz", **{f"before_{k}": x for k, x in before.items()}, **{f"after_{k}": x for k, x in after.items()},
                 preview=preview, frozen=frozen, late=late["progress"], evaluation=evaluation, packet=packet,
                 packet_text=packet_text, failed=[f["progress"] for f in failed], done=[d["progress"] for d in done],
                 progress_file=(root / "progress.jsonl").read_text(encoding="utf-8"),
                 log_file=(root / "log.jsonl").read_text(encoding="utf-8"),
                 candidates_file=(root / "candidates.jsonl").read_text(encoding="utf-8"))

    # Request accounting stays meaningful: every request is logged once, and only the failed one is unlogged.
    code, log = psb(capsys, root, "log")
    assert log["ncbi_requests"] - log["from_cache"] == len(transport.calls) - 1
    assert log["from_cache"] >= 1  # the private count reused the private sample's cached search

    # Every stage summary before the held-out test.
    write_round(Workspace(root), 1, [], PASS)
    assert psb(capsys, root, "critic", "check")[0] == 0
    stages = {}
    for stage in ("intake", "scope", "known-records", "vocabulary", "test", "critic"):
        code, stages[stage] = psb(capsys, root, "progress", stage)
        assert code == 0, (stage, stages[stage])
    assert_clean("qxz", **stages)

    # The authorized post-test audit keeps its record-level evidence.
    for argv in (["holdout-test"], ["report"]):
        code, out = psb(capsys, root, *argv)
        assert code == 0, (argv, out)
    audit = (root / "audit.md").read_text(encoding="utf-8")
    held = sorted(p for u in ws.allocation()["units"] if u["purpose"] == "holdout" for p in u["members"])
    assert all(f"QXZ reason {p}" in audit and f"QXZ Table {p}" in audit for p in held)
    snapshot = validation.digest(validation.input_snapshot(ws))
    views(capsys, root)
    assert deliver.verify_delivery(ws)["ok"] and validation.digest(validation.input_snapshot(ws)) == snapshot


@pytest.mark.parametrize("mode", ["standard", "verbose"])
def test_paired_private_content_gives_identical_builder_outputs(tmp_path, capsys, corpus, mode):
    """Different private queries, records, reasons, groups, identifiers and file names; the same counts."""
    seen = []
    for name, mark, base in (("a", "qxz", 100), ("b", "jvw", 300)):
        v = Private(mark, base)
        directory = tmp_path / name
        root, _ = start(directory, capsys, corpus, v, mode)
        done, failed = run_worker(capsys, root, v, directory)
        before = views(capsys, root)
        code, preview = psb(capsys, root, "allocate", "--preview")
        code, frozen = psb(capsys, root, "allocate", "--keep-holdout")
        after = views(capsys, root)
        assert_clean(mark, before=before, after=after, preview=preview, frozen=frozen)
        seen.append({"done": [d["progress"] for d in done], "failed": [f["progress"] for f in failed],
                     "before": comparable(before, root), "after": comparable(after, root),
                     "preview": preview, "frozen": frozen})
    assert seen[0] == seen[1]


def test_a_builder_screen_of_privately_screened_records_gives_no_feedback(tmp_path, capsys, corpus):
    """The builder screens a record the separate context also discovered and screened: its message is the
    same whether the private decision was include or exclude."""
    texts = []
    for name, mark, swap in (("a", "qxz", False), ("b", "jvw", True)):
        v = Private(mark, swap=swap)
        directory = tmp_path / name
        root, _ = start(directory, capsys, corpus, v)
        run_worker(capsys, root, v, directory)
        assert progress.decisions(Workspace(root))[v.pmids[5]]["decision"] == ("exclude" if swap else "include")
        code, out = psb(capsys, root, "screen", "--include", v.pmids[5], "--reason", "a trial")
        assert code == 0
        texts.append(out["progress"]["text"])
        assert progress.decisions(Workspace(root))[v.pmids[5]]["context"] == "builder"  # exposure is recorded
    assert texts[0] == texts[1] == "\n".join([
        "**PSB · Step 3/7 Known records · Screening**",
        "Screened 1 candidate: 1 include · 0 exclude · 0 uncertain",
        f"- {progress.WITHHELD}: 1 screened",
        "- Records with a screening decision so far (all contexts): 25 of ~150 (standard)",
        "- Included but not yet in a set: 105; plus 18 records from the separate screening context (not listed)"])


# -- routing: request log and cache ---------------------------------------------------------------

def test_restricted_requests_use_the_private_cache_and_log(tmp_path, capsys, corpus, monkeypatch):
    v = Private("qxz")
    root, transport = start(tmp_path, capsys, corpus, v)
    shared, private = root / ".cache", root / "screening" / ".cache"
    files = lambda d: sorted(d.glob("*/*.json")) if d.is_dir() else []  # noqa: E731
    calls = len(transport.calls)
    code, out = psb(capsys, root, "sample", "--screening", "--purpose", "pilot", v.pilot)
    assert code == 0 and len(transport.calls) > calls and files(private) and not files(shared)
    made = [(u, json.dumps(p, sort_keys=True)) for u, p in transport.calls[calls:]]
    assert len(set(made)) == len(made)  # no request is repeated to fill a second cache
    rows = Workspace(root).log_entries()
    restricted = rows[-(len(transport.calls) - calls) - 1:]
    assert all(set(r) <= set(disclosure.LOG_FIELDS) for r in restricted)
    assert [r["type"] for r in restricted][0] == "command" and restricted[0]["command"] == ["sample"]
    full = [json.loads(line) for line in (root / "screening" / "log.jsonl").read_text(encoding="utf-8").splitlines()]
    assert full[0]["argv"][-1] == v.pilot and full[1]["params"]["term"] == v.pilot

    # The same search again is served from the private cache, for the whole operation.
    calls = len(transport.calls)
    code, out = psb(capsys, root, "count", "--screening", v.pilot)
    assert code == 0 and len(transport.calls) == calls
    assert Workspace(root).log_entries()[-1]["cache"] is True
    # The builder's own search never reads the private cache, and its rows keep their detail.
    code, out = psb(capsys, root, "count", v.pilot)
    assert code == 0 and len(transport.calls) == calls + 1 and files(shared)
    last = Workspace(root).log_entries()
    assert last[-2]["argv"][-1] == v.pilot and last[-1]["params"]["term"] == v.pilot

    # The cache switches still work, and nothing is requested twice to fill both caches.
    before = files(private)
    calls = len(transport.calls)
    code, out = psb(capsys, root, "--no-cache", "count", "--screening", v.pilot)
    assert code == 0 and len(transport.calls) == calls + 1 and files(private) == before
    monkeypatch.setenv("PSB_CACHE", "off")
    code, out = psb(capsys, root, "count", "--screening", v.review)
    assert code == 0 and len(transport.calls) == calls + 2 and files(private) == before


def test_a_broken_private_log_never_brings_raw_content_back(tmp_path, capsys, corpus):
    v = Private("qxz")
    root, transport = start(tmp_path, capsys, corpus, v)
    (root / "screening" / "log.jsonl").mkdir(parents=True)  # the private log cannot be written
    calls = len(transport.calls)
    code, out = psb(capsys, root, "sample", "--screening", "--purpose", "pilot", v.pilot)
    assert code == 1 and len(transport.calls) == calls  # fails closed, before any request
    assert out["progress"]["text"].startswith("**PSB · Step 3/7 Known records · Separate screening**\nA candidate "
                                              "search did not complete")
    assert_clean("qxz", progress=out["progress"], progress_file=(root / "progress.jsonl").read_text(encoding="utf-8"),
                 log_file=(root / "log.jsonl").read_text(encoding="utf-8"))


def test_a_failing_restricted_message_keeps_only_the_exception_class(tmp_path, capsys, corpus, monkeypatch):
    v = Private("qxz")
    root, _ = start(tmp_path, capsys, corpus, v)
    def broken(ws, data):
        raise KeyError("QXZ private detail")
    monkeypatch.setitem(progress.EVENTS, "separate:search:pilot", (3, broken))
    code, out = psb(capsys, root, "sample", "--screening", "--purpose", "pilot", v.pilot)
    assert code == 0 and out["progress"]["error"] == "KeyError" and len(out["records"]) == 10
    assert_clean("qxz", progress=out["progress"], progress_file=(root / "progress.jsonl").read_text(encoding="utf-8"))
    assert "QXZ private detail" in (root / "screening" / "log.jsonl").read_text(encoding="utf-8")


# -- policy ---------------------------------------------------------------------------------------

@pytest.mark.parametrize("argv,expected", [
    (["sample", "--screening", "--purpose", "pilot", "x"], True), (["sample", "x"], False),
    (["fetch", "--screening", "1"], True), (["count", "--screening", "x"], True), (["count", "x"], False),
    (["neighbors", "--screening", "1"], True), (["resolve", "--screening", "1"], True), (["resolve", "1"], False),
    (["screen", "--context", "separate", "--include", "1"], True), (["screen", "--file", "f.json"], True),
    (["screen", "--include", "1"], False), (["screen", "--context", "builder", "--include", "1"], False),
    (["status"], False), (["progress", "list"], False), (["mesh", "lookup", "x"], False)])
def test_the_policy_is_a_function_of_the_parsed_arguments(argv, expected):
    assert disclosure.restricted(cli.build_parser().parse_args(argv)) is expected


def test_a_screen_file_without_context_is_restricted_but_records_builder(tmp_path, capsys, corpus):
    v = Private("qxz")
    root, _ = start(tmp_path, capsys, corpus, v)
    path = tmp_path / "qxz-plain.json"
    path.write_text(json.dumps([{"pmid": v.pmids[0], "decision": "include", "reason": "QXZ reason"}]), encoding="utf-8")
    code, out = psb(capsys, root, "screen", "--file", str(path))
    assert code == 0 and out["progress"]["text"].splitlines()[1] == ("Recorded decisions for 1 candidate; detailed "
                                                                     "attribution is withheld.")
    ws = Workspace(root)
    assert progress.decisions(ws)[v.pmids[0]]["context"] == "builder"
    assert progress.decisions(ws)[v.pmids[0]]["reason"] == "QXZ reason"  # a builder decision keeps its reason
    unit = next(u for u in allocation.pool(ws)["units"] if u["id"] == v.pmids[0])
    assert unit["exposed"] and unit["exposure"][0]["reasons"] == ["screened by the builder"]


def test_a_record_the_builder_saw_stays_exposed(tmp_path, capsys, corpus):
    v = Private("qxz")
    root, _ = start(tmp_path, capsys, corpus, v)
    assert psb(capsys, root, "fetch", v.pmids[0])[0] == 0  # the builder sees its title
    for argv in (["fetch", "--screening", "--abstracts", v.pmids[0]],
                 ["screen", "--context", "separate", "--include", v.pmids[0]]):
        assert psb(capsys, root, *argv)[0] == 0
    unit = next(u for u in allocation.pool(Workspace(root))["units"] if u["id"] == v.pmids[0])
    assert unit["exposed"] and unit["exposure"][0]["reasons"] == ["title shown by psb fetch"]


def test_private_count_and_neighbours_keep_their_guards(tmp_path, capsys, corpus):
    v = Private("qxz")
    root, _ = start(tmp_path, capsys, corpus, v)
    run_worker(capsys, root, v, tmp_path)
    assert psb(capsys, root, "allocate", "--keep-holdout")[0] == 0
    held = sorted(Workspace(root).reserved_pmids())
    code, out = psb(capsys, root, "count", "--screening", f"{held[0]}[uid]")
    assert code == 1 and "reveal whether the strategy retrieves it" in out["error"]
    code, out = psb(capsys, root, "neighbors", "--screening", held[0])
    assert code == 1 and "reserved" in out["error"]
    assert out["progress"]["text"].splitlines()[1].startswith("A neighbour search did not complete")


# -- history ----------------------------------------------------------------------------------------

LEGACY_PROGRESS = [
    {"event": "stage:scope", "step": 2, "text": "scope summary", "seq": 1},
    {"event": "search:pilot", "step": 3, "text": "Pilot search: 3 records for `qxz[tiab]`", "seq": 2},
    {"event": "screen", "step": 3, "text": "- Pilot search `qxz[tiab]` (C1): 3 screened → 2 include", "seq": 3},
    {"event": "neighbors", "step": 3, "text": "qxz neighbours", "seq": 4},
    {"event": "resolve", "step": 3, "text": "qxz resolved", "seq": 5},
    {"event": "stage:known-records", "step": 3, "text": "Eligible, not yet allocated: 101, 102 qxz", "seq": 6},
    {"event": "set", "step": 3, "text": "Set seeds", "seq": 7, "error": "TypeError: qxz"},
    {"event": "critic-check", "step": 6, "text": "Round 1", "seq": 8},
    {"event": "mystery", "step": 3, "text": "qxz", "seq": 9},
    {"event": "eval", "step": 5, "text": "v1", "seq": 10, "disclosure_version": 1, "secret": "qxz"},
    {"event": "unknown-new", "step": 3, "text": "qxz", "seq": 11, "disclosure_version": 1},
    {"event": "separate:screen", "step": 3, "text": "safe", "seq": 12, "disclosure_version": 2},
]
LEGACY_LOG = [
    {"ts": "t1", "type": "init", "question": "qxz question"},
    {"ts": "t2", "type": "command", "argv": ["--workspace", "w", "count", "qxz[tiab]"]},
    {"ts": "t3", "type": "ncbi", "endpoint": "esearch.fcgi", "params": {"term": "qxz[tiab]"}, "cache": False},
    {"ts": "t4", "type": "command", "argv": ["--workspace", "w", "mesh", "lookup", "qxz"]},
    {"ts": "t5", "type": "command", "argv": ["screen", "--file", "qxz.json"]},
    {"ts": "t6", "type": "command", "argv": ["sample", "--screening", "qxz[tiab]"]},
    {"ts": "t7", "type": "set", "name": "qxz", "purpose": "development", "size": 3},
    {"ts": "t8", "type": "allocation", "N": 20, "U": 18, "H": 6, "choice": "keep-holdout"},
    {"ts": "t9", "type": "ncbi", "endpoint": "efetch.fcgi", "params": {"id": "101"}, "cache": True},
    {"ts": "t10", "type": "command", "argv": ["qxz-unknown"]},
    {"ts": "t11", "type": "command", "argv": ["progress", "known-records"]},
]


def test_older_rows_are_filtered_by_name_without_changing_any_file(tmp_path, capsys, corpus):
    v = Private("qxz")
    root, _ = start(tmp_path, capsys, corpus, v)
    (root / "progress.jsonl").write_text("".join(json.dumps(r) + "\n" for r in LEGACY_PROGRESS), encoding="utf-8")
    (root / "log.jsonl").write_text("".join(json.dumps(r) + "\n" for r in LEGACY_LOG), encoding="utf-8")
    digest = hashlib.sha256((root / "progress.jsonl").read_bytes()).hexdigest()

    code, out = psb(capsys, root, "progress", "list")
    assert [m["seq"] for m in out["messages"]] == [1, 7, 8, 10] and out["omitted"] == 8 and out["note"]
    assert all(set(m) == {"seq", "event", "step", "text"} for m in out["messages"])
    assert hashlib.sha256((root / "progress.jsonl").read_bytes()).hexdigest() == digest
    log_digest = hashlib.sha256((root / "log.jsonl").read_bytes()).hexdigest()
    code, out = psb(capsys, root, "log", "--tail", "100")
    assert hashlib.sha256((root / "log.jsonl").read_bytes()).hexdigest() == log_digest
    assert out["entries"] == 12 and out["ncbi_requests"] == 2 and out["from_cache"] == 1  # every row still counts
    assert out["tail"][:6] == [
        {"ts": "t1", "type": "init"},
        {"ts": "t3", "type": "ncbi", "endpoint": "esearch.fcgi", "cache": False},
        {"ts": "t4", "type": "command", "command": ["mesh", "lookup"]},
        {"ts": "t7", "type": "set", "size": 3},
        {"ts": "t8", "type": "allocation", "N": 20, "U": 18, "H": 6},
        {"ts": "t9", "type": "ncbi", "endpoint": "efetch.fcgi", "cache": True}]
    assert out["tail"][6] == {"ts": "t11", "type": "command", "command": ["progress", "known-records"]}
    assert out["tail"][7]["command"] == ["progress", "list"] and out["tail_omitted"] == 4
    assert_clean("qxz", tail=out["tail"])


def test_vocabulary_counts_read_marked_and_older_command_rows(tmp_path, capsys, corpus):
    v = Private("qxz")
    root, _ = start(tmp_path, capsys, corpus, v)
    write_json(root / "strategy.json", STRATEGY)
    with (root / "log.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps({"type": "command", "argv": ["--workspace", "w", "mesh", "lookup", "asthma"]}) + "\n")
    assert psb(capsys, root, "mesh", "lookup", "asthma")[0] == 0
    assert psb(capsys, root, "mesh", "show", "Asthma")[0] == 0
    code, out = psb(capsys, root, "progress", "vocabulary")
    assert "- MeSH lookups: 2 · MeSH records inspected: 1" in out["progress"]["text"]
