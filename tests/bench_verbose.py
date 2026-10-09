"""What verbose progress messages cost, offline.

    python tests/bench_verbose.py [runs]

One synthetic, representative run (three blocks, one of 65 terms; known records with a miss; a pilot
search and a neighbour search; many short MeSH commands; two evaluations, term mining and miss
diagnosis) is executed in standard and in verbose mode over the same in-memory corpus, through the
real client and cache. For each mode it reports the progress messages, the characters relayed to the
user (``progress.text``), the characters of tool output (the JSON the agent reads), the NCBI requests,
and the median runtime over repeated runs. Characters only: no token counts without a tokenizer.
"""

from __future__ import annotations

import contextlib
import io
import json
import statistics
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from conftest import CorpusPubMed, CorpusTransport, record  # noqa: E402
from psb import cli, progress  # noqa: E402
from psb import workspace as workspace_module  # noqa: E402
from psb.workspace import write_json  # noqa: E402

UNIVERSE = [str(p) for p in range(1, 201)]
KNOWN = [str(p) for p in range(1, 32)]
BLOCKS = {
    "intervention": [f"zeta{n:02d}[tiab]" for n in range(65)],
    "condition": ['"Asthma"[Mesh]', *[f"asthma{n}[tiab]" for n in range(9)]],
    "population": ['"Child"[Mesh]', *[f"child{n}[tiab]" for n in range(4)]],
}
MESH = [("lookup", "asthma"), ("lookup", "child"), ("show", "Asthma"), ("show", "Child")] * 6
MESH_COMMANDS = len(MESH)


def corpus() -> CorpusTransport:
    numbers = [int(p) for p in UNIVERSE]
    atoms = {f"zeta{n:02d}[tiab]": {str(p) for p in numbers if p % 65 == n} if n < 60 else set() for n in range(65)}
    atoms.update({f"asthma{n}[tiab]": {str(p) for p in numbers if p % 9 == n} for n in range(9)})
    atoms.update({f"child{n}[tiab]": {str(p) for p in numbers if p % 4 == n and p != 31} for n in range(4)})
    atoms.update({'"Asthma"[Mesh]': set(UNIVERSE[:150]), '"Child"[Mesh]': set(UNIVERSE) - {"31"}})
    records = {p: record(p, f"Trial {p} of an inhaled therapy for asthma in children",
                         "Asthma in children treated with inhaled corticosteroids.", mesh=["Asthma", "Child"])
               for p in UNIVERSE}
    links = {("1", "similar"): [("150", 20), ("151", 10), ("152", 5)]}
    return CorpusTransport(atoms, records, links)


def commands() -> list[list[str]]:
    return [["set", "add", "known", *KNOWN, "--purpose", "development"], ["allocate"],
            ["sample", "--purpose", "pilot", "asthma1[tiab]"], ["neighbors", "1", "--links", "similar"],
            *[["mesh", kind, term] for kind, term in MESH],
            ["eval", "--note", "first draft"], ["terms", "rank", "--budget", "10"], ["terms", "miss"],
            ["eval", "--no-term-counts", "--note", "recheck"]]


def run_once(directory: Path, mode: str) -> dict:
    transport = corpus()
    original = workspace_module.CLIENT
    workspace_module.CLIENT = lambda **kw: CorpusPubMed(transport=transport, **kw)
    root = directory / "run"
    out = io.StringIO()
    try:
        with contextlib.redirect_stdout(out):
            cli.main(["init", str(root), "--question", "Which inhaled therapies help children with asthma?"])
        protocol = json.loads((root / "protocol.json").read_text(encoding="utf-8"))
        protocol.update(depth="standard", scope_confirmed=True,
                        concepts=[{"id": b, "name": b, "role": "search", "rationale": "searched"} for b in BLOCKS])
        write_json(root / "protocol.json", protocol)
        write_json(root / "strategy.json", {"blocks": [{"id": b, "name": b, "terms": t} for b, t in BLOCKS.items()]})
        if mode == "verbose":
            with contextlib.redirect_stdout(io.StringIO()):
                cli.main(["--workspace", str(root), "progress", "mode", "verbose"])
        results, started = [], time.perf_counter()
        for argv in commands():
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                cli.main(["--workspace", str(root), *argv])
            results.append(out.getvalue())
        elapsed = time.perf_counter() - started
    finally:
        workspace_module.CLIENT = original
    sent = [json.loads(r)["progress"] for r in results if "progress" in json.loads(r)]
    texts = [m["text"] for m in sent]
    sections = ["Details:\n" + t.split("\nDetails:\n", 1)[1] for t in texts if "\nDetails:\n" in t]
    return {"messages": len(texts), "relay_chars": sum(len(t) for t in texts), "texts": texts,
            "mesh_chars": sum(len(m["text"]) for m in sent if m["event"].startswith("mesh-")),
            "tool_chars": sum(len(r) for r in results), "requests": len(transport.calls),
            "trace": transport.calls, "seconds": elapsed, "sections": sections}


def measure(directory: Path, runs: int = 7) -> dict:
    found = {}
    for mode in ("standard", "verbose"):
        rounds = [run_once(Path(tempfile.mkdtemp(dir=directory)), mode) for _ in range(runs)]
        found[mode] = {**rounds[-1], "median_seconds": statistics.median(r["seconds"] for r in rounds)}
    return found


def main(argv: list[str]) -> None:
    runs = int(argv[0]) if argv else 7
    with tempfile.TemporaryDirectory() as directory:
        result = measure(Path(directory), runs)
    standard, verbose = result["standard"], result["verbose"]
    print(f"{len(commands())} commands per run ({MESH_COMMANDS} MeSH), median of {runs} runs")
    print(f"{'':10} {'messages':>9} {'relayed chars':>14} {'tool-output chars':>18} {'requests':>9} {'median s':>9}")
    for name, row in result.items():
        print(f"{name:10} {row['messages']:>9} {row['relay_chars']:>14,} {row['tool_chars']:>18,} {row['requests']:>9} "
              f"{row['median_seconds']:>9.3f}")
    new = verbose["messages"] - standard["messages"]
    enriched = verbose["relay_chars"] - verbose["mesh_chars"] - standard["relay_chars"]
    tool = verbose["tool_chars"] - standard["tool_chars"]
    print(f"added relayed characters: {enriched:,} on the {standard['messages']} existing messages "
          f"(+{100 * enriched / standard['relay_chars']:.0f}%), and {verbose['mesh_chars']:,} in {new} new MeSH "
          f"messages ({verbose['mesh_chars'] / max(1, new):.0f} each)")
    print(f"added tool-output characters: {tool:,} (+{100 * tool / standard['tool_chars']:.0f}%); largest Details "
          f"section {max(len(s) for s in verbose['sections'])} characters, "
          f"{max(len(s.split()) for s in verbose['sections'])} words; identical request trace: "
          f"{standard['trace'] == verbose['trace']}")


if __name__ == "__main__":
    main(sys.argv[1:])
