#!/usr/bin/env python3
"""Evaluation CLI.

    python evals/run.py baselines [TOPIC ...]            score naive and reference strategies
    python evals/run.py score TOPIC --strategy-file F     score any strategy
    python evals/run.py generate TOPIC --driver claude    run a skill end to end, then score it
    python evals/run.py report                            aggregate results into evals/RESULTS.md

Results are written under evals/results/<topic>/ as small JSON scorecards. Generated runs happen
in a directory outside the repository (default: <temp>/psb-evals) so the agent cannot read the
answer keys; only the strategy, audit and scorecard are copied back.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shutil
import statistics
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import drivers  # noqa: E402
import harness  # noqa: E402
from psb import config  # noqa: E402

DEFAULT_RUNS_ROOT = Path(tempfile.gettempdir()) / "psb-evals"


def stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def save(topic: str, name: str, data: dict) -> Path:
    path = harness.RESULTS / re.sub(r"[^A-Za-z0-9_.-]", "_", topic) / f"{name}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def topics(names: list[str]) -> list[dict]:
    if names:
        return [harness.load_fixture(n) for n in names]
    return [harness.load_fixture(str(p)) for p in harness.fixture_paths()]


def cmd_baselines(args) -> int:
    for fixture in topics(args.topics):
        pm = harness.client(fixture, use_cache=not args.no_cache)
        for source, query in harness.baseline_queries(fixture).items():
            for condition, exclude in (("noseed", set()), ("seeded", set(fixture.get("seeds") or []))):
                if condition == "seeded" and not exclude:
                    continue
                result = harness.score(fixture, query, exclude=exclude, pm=pm)
                card = {"topic": fixture["id"], "source": source, "condition": condition, "strategy": query,
                        "scored": stamp(), **result}
                save(fixture["id"], f"{source}-{condition}", card)
                print(f"{fixture['id'][:30]:31} {source:9} {condition:7} recall={result['recall_percent']}% "
                      f"({result['retrieved']}/{result['gold_reachable']}) count={result['count']:,}")
    return 0


def cmd_score(args) -> int:
    fixture = harness.load_fixture(args.topic)
    query = Path(args.strategy_file).read_text(encoding="utf-8")
    exclude = set(fixture.get("seeds") or []) if args.condition == "seeded" else set()
    print(json.dumps(harness.score(fixture, query, exclude=exclude), indent=2))
    return 0


def child_env(skill_dir: Path, as_of: str | None) -> dict:
    env = {k: v for k, v in os.environ.items() if not k.startswith(("CLAUDECODE", "CLAUDE_CODE_ENTRYPOINT"))}
    for key, value in config.parse_env_file(skill_dir / ".env").items():
        env.setdefault(key, value)
    env.pop("PSB_WORKSPACE", None)
    if as_of:
        env["PSB_AS_OF"] = as_of
    env["PYTHONIOENCODING"] = "utf-8"
    return env


def cmd_generate(args) -> int:
    fixture = harness.load_fixture(args.topic)
    skill_dir = Path(args.skill).resolve()
    skill_name = args.skill_name or skill_dir.name
    seeds = list(fixture.get("seeds") or []) if args.condition == "seeded" else []
    if args.condition == "seeded" and not seeds:
        raise SystemExit(f"{fixture['id']} has no seeds")
    status = 0
    for repeat in range(args.runs):
        label = f"{skill_name}-{args.driver}-{args.condition}-{stamp()}"
        run_dir = Path(args.runs_root) / re.sub(r"[^A-Za-z0-9_.-]", "_", fixture["id"]) / label
        run_dir.mkdir(parents=True)
        drivers.stage_skill(skill_dir, run_dir)
        (run_dir / "work").mkdir()
        prompt = drivers.prompt_for(fixture, seeds=seeds, depth=args.depth)
        (run_dir / "prompt.txt").write_text(prompt, encoding="utf-8")
        print(f"[{repeat + 1}/{args.runs}] {fixture['id']} {label}\n  run dir: {run_dir}", flush=True)
        run = drivers.DRIVERS[args.driver](prompt, run_dir, env=child_env(skill_dir, fixture.get("as_of")),
                                           timeout=args.timeout, model=args.model)
        transcript = ""
        for name in ("transcript.json", "transcript.jsonl"):
            if (run_dir / name).exists():
                transcript = (run_dir / name).read_text(encoding="utf-8", errors="replace")
        card = {"topic": fixture["id"], "source": f"generated:{skill_name}", "driver": args.driver,
                "model": args.model, "condition": args.condition, "depth": args.depth, "run_dir": str(run_dir),
                "scored": stamp(), "run": {k: v for k, v in run.items() if k != "final_message"},
                "final_message": run.get("final_message", "")}
        strategy_path = run_dir / "final_strategy.txt"
        if strategy_path.exists() and strategy_path.read_text(encoding="utf-8").strip():
            query = strategy_path.read_text(encoding="utf-8")
            seen = harness.gold_seen(fixture, run_dir) - set(seeds)
            card["strategy"] = " ".join(query.split())
            card.update(harness.score(fixture, query, exclude=set(seeds), seen=seen))
            card["leakage"] = harness.leakage(fixture, run_dir, transcript)
            card["valid"] = not card["leakage"]
        else:
            card["valid"] = False
            card["error"] = "no final_strategy.txt"
            status = 2
        name = f"{label}"
        out = save(fixture["id"], name, card)
        for extra in ("audit.md",):
            if (run_dir / "work" / extra).exists():
                shutil.copy2(run_dir / "work" / extra, out.with_suffix(".audit.md"))
        print(f"  recall={card.get('recall_percent')}% ({card.get('retrieved')}/{card.get('gold_reachable')}) "
              f"unseen={card.get('unseen_recall_percent')}% count={card.get('count')} "
              f"cost=${card['run'].get('cost_usd')} seconds={card['run'].get('seconds')} "
              f"leakage={card.get('leakage')}\n  scorecard: {out}", flush=True)
    return status


def cmd_report(args) -> int:
    cards = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(harness.RESULTS.glob("*/*.json"))]
    rows: dict[tuple, list[dict]] = {}
    for card in cards:
        if card.get("recall_percent") is None and card.get("valid") is not False:
            continue
        rows.setdefault((card["topic"], card["source"], card.get("condition", "noseed"), card.get("driver", "")), []).append(card)
    lines = [
        "# Evaluation results",
        "",
        f"Generated {stamp()} by `python evals/run.py report`.",
        "",
        "Recall is over gold records in PubMed on or before `as_of`; in the seeded condition the three seeds are "
        "excluded. `unseen` recall leaves out gold records the agent itself screened into its sets. NNR is total "
        "results divided by gold retrieved: a workload proxy, not precision. Generated rows show the mean (min-max) "
        "over valid runs.",
        "",
        "| Topic | Source | Condition | Runs | Recall % | Unseen recall % | Results | NNR | Cost $ |",
        "|---|---|---|---:|---|---|---:|---:|---:|",
    ]

    def spread(values: list) -> str:
        values = [v for v in values if v is not None]
        if not values:
            return "n/a"
        mean = round(statistics.mean(values), 1)
        return f"{mean}" if len(values) == 1 else f"{mean} ({min(values)}-{max(values)})"

    for (topic, source, condition, driver), group in sorted(rows.items()):
        valid = [c for c in group if c.get("valid", True) and c.get("recall_percent") is not None]
        label = source + (f" ({driver})" if driver else "")
        costs = [c.get("run", {}).get("cost_usd") for c in valid]
        lines.append(
            f"| {topic[:40]} | {label} | {condition} | {len(valid)}/{len(group)} | {spread([c['recall_percent'] for c in valid])} "
            f"| {spread([c.get('unseen_recall_percent') for c in valid])} | {spread([c.get('count') for c in valid])} "
            f"| {spread([c.get('nnr') for c in valid])} | {spread(costs)} |"
        )
    path = harness.EVALS / "RESULTS.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {path} ({len(rows)} rows)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--env-file", default=str(harness.REPO / ".env"))
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("baselines")
    p.add_argument("topics", nargs="*")
    p.add_argument("--no-cache", action="store_true")
    p.set_defaults(func=cmd_baselines)
    p = sub.add_parser("score")
    p.add_argument("topic")
    p.add_argument("--strategy-file", required=True)
    p.add_argument("--condition", choices=["noseed", "seeded"], default="noseed")
    p.set_defaults(func=cmd_score)
    p = sub.add_parser("generate")
    p.add_argument("topic")
    p.add_argument("--driver", choices=sorted(drivers.DRIVERS), default="claude")
    p.add_argument("--condition", choices=["noseed", "seeded"], default="noseed")
    p.add_argument("--depth", default="standard")
    p.add_argument("--skill", default=str(harness.REPO), help="skill directory to test (default: this repo)")
    p.add_argument("--skill-name", help="label for results (default: directory name)")
    p.add_argument("--model")
    p.add_argument("--runs", type=int, default=1)
    p.add_argument("--timeout", type=int, default=5400)
    p.add_argument("--runs-root", default=str(DEFAULT_RUNS_ROOT))
    p.set_defaults(func=cmd_generate)
    p = sub.add_parser("report")
    p.set_defaults(func=cmd_report)
    args = parser.parse_args()
    if args.env_file and Path(args.env_file).exists():
        config.use_env_file(args.env_file)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
