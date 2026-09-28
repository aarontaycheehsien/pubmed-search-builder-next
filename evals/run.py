#!/usr/bin/env python3
"""Evaluation CLI.

    python evals/run.py baselines [TOPIC ...]            score naive and reference strategies
    python evals/run.py score TOPIC --strategy-file F     score any strategy
    python evals/run.py generate TOPIC --driver claude    run a skill end to end, then score it
    python evals/run.py freeze TOPIC ...                  freeze never-run topics as held-out
    python evals/run.py report                            aggregate results into evals/RESULTS.md

Results are written under evals/results/<topic>/ as small JSON scorecards. Generated runs happen
in a directory outside the repository (default: <temp>/psb-evals) so the agent cannot read the
answer keys; only the strategy, audit and scorecard are copied back.

Topics are split in evals/splits.json: dev (tune the skill on these), heldout (frozen before their
first run; using one needs --heldout, is logged, and never keeps misses) and retired.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import statistics
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import drivers  # noqa: E402
import harness  # noqa: E402
from psb import config, deliver  # noqa: E402
from psb.workspace import Workspace  # noqa: E402

DEFAULT_RUNS_ROOT = Path(tempfile.gettempdir()) / "psb-evals"
MIN_RUNS = 3
TIE_POINTS = 0.05  # mean recalls closer than this count as a tie
WORKLOAD_FLAG = 2.0  # flag a paired topic whose result counts differ by more than this factor


def stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def find_strategy_file(run_dir: Path, *, require_protected: bool = False, effective_as_of: str | None = None) -> Path | None:
    """The agent's final strategy, wherever it actually wrote it.

    The prompt asks for ``./final_strategy.txt``, but a skill with its own filing convention
    (e.g. keeping everything under a ``work/`` directory) may write it one level down instead.
    Preferring the root path first keeps the common case exact; falling back to ``work/`` scores
    a skill's real output rather than discarding a completed, on-topic run over a path detail.
    """
    if require_protected:
        previous = os.environ.get("PSB_AS_OF")
        try:
            if effective_as_of:
                os.environ["PSB_AS_OF"] = effective_as_of
            verified = deliver.verify_delivery(Workspace(run_dir / "work"))
            return Path(verified["query_file"]) if verified["ok"] else None
        finally:
            if previous is None:
                os.environ.pop("PSB_AS_OF", None)
            else:
                os.environ["PSB_AS_OF"] = previous
    for candidate in (run_dir / "final_strategy.txt", run_dir / "work" / "final_strategy.txt"):
        if candidate.exists() and candidate.read_text(encoding="utf-8").strip():
            return candidate
    return None


def anon_dir(topic: str) -> str:
    """A non-identifying directory name for the agent-visible run path.

    A short citation-style id (e.g. "Bos_2018") in the agent's own cwd is itself a leak: the
    agent can read it from `pwd`/an error message/a sandbox banner without ever being told the
    review's identity, and for a named topic it hands over exactly the citation key. Only our own
    ``evals/results/<topic>/`` path (never shown to the agent) uses the readable id.
    """
    return "run-" + hashlib.sha256(topic.encode("utf-8")).hexdigest()[:16]


def save(topic: str, name: str, data: dict) -> Path:
    path = harness.RESULTS / re.sub(r"[^A-Za-z0-9_.-]", "_", topic) / f"{name}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


# -- splits ---------------------------------------------------------------------------------------

def guard_topic(fixture: dict, *, allow_heldout: bool) -> str:
    """The topic's split; refuses retired and unassigned topics, and held-out ones without ``--heldout``."""
    splits = harness.load_splits()
    split = harness.split_of(fixture["id"], splits)
    if split == "retired":
        raise SystemExit(f"{fixture['id']} is retired: {splits['retired'][fixture['id']]}")
    if split == "unassigned":
        raise SystemExit(f"{fixture['id']} is in no split: add it to dev in evals/splits.json, or freeze it "
                         "as held-out with `run.py freeze` before its first run")
    if split == "heldout" and not allow_heldout:
        raise SystemExit(f"{fixture['id']} is held out: pass --heldout to use it (the use is logged in "
                         f"{harness.HELDOUT_LEDGER.name}, and misses are not kept)")
    return split


def topics(names: list[str], *, allow_heldout: bool = False) -> list[tuple[dict, str]]:
    """(fixture, split) pairs. Named topics must be usable; with no names, every dev topic, plus
    held-out ones when ``allow_heldout``."""
    if names:
        return [(f, guard_topic(f, allow_heldout=allow_heldout)) for f in map(harness.load_fixture, names)]
    splits = harness.load_splits()
    chosen = []
    for path in harness.fixture_paths():
        fixture = harness.load_fixture(str(path))
        split = harness.split_of(fixture["id"], splits)
        if split == "dev" or (split == "heldout" and allow_heldout):
            chosen.append((fixture, split))
        else:
            print(f"skipping {fixture['id']} ({split})", file=sys.stderr)
    return chosen


def seal(card: dict, split: str) -> dict:
    """Tag a scorecard with its split and drop what a held-out card must never keep."""
    card = {**card, "split": split}
    return harness.redact_heldout(card) if split == "heldout" else card


def cmd_freeze(args) -> int:
    """Add topics to the held-out set. Only a topic that is in no split and was never scored qualifies."""
    splits = harness.load_splits()
    for name in args.topics:
        fixture = harness.load_fixture(name)
        topic = fixture["id"]
        split = harness.split_of(topic, splits)
        if split != "unassigned":
            raise SystemExit(f"{topic} is already {split}; only a topic in no split can be frozen as held-out")
        existing = harness.RESULTS / re.sub(r"[^A-Za-z0-9_.-]", "_", topic)
        if existing.exists() and any(existing.iterdir()):
            raise SystemExit(f"{topic} already has results in {existing}: it has been seen and cannot be held out")
        splits["heldout"][topic] = {"sha256": harness.fixture_hash(fixture), "frozen": stamp()}
        print(f"froze {topic}")
    harness.SPLITS.write_text(json.dumps(splits, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


# -- scoring ----------------------------------------------------------------------------------------

def cmd_baselines(args) -> int:
    for fixture, split in topics(args.topics, allow_heldout=args.heldout):
        if split == "heldout":
            harness.record_heldout_look({"topic": fixture["id"], "command": "baselines"})
        pm = harness.client(fixture, use_cache=not args.no_cache)
        for source, query in harness.baseline_queries(fixture).items():
            for condition, exclude in (("noseed", set()), ("seeded", set(fixture.get("seeds") or []))):
                if condition == "seeded" and not exclude:
                    continue
                result = harness.score(fixture, query, exclude=exclude, pm=pm)
                card = {"topic": fixture["id"], "source": source, "condition": condition, "strategy": query,
                        "scored": stamp(), "status": "ok", **result}
                save(fixture["id"], f"{source}-{condition}", seal(card, split))
                print(f"{fixture['id'][:30]:31} {source:9} {condition:7} recall={result['recall_percent']}% "
                      f"({result['retrieved']}/{result['gold_reachable']}) count={result['count']:,}")
    return 0


def cmd_score(args) -> int:
    fixture = harness.load_fixture(args.topic)
    split = guard_topic(fixture, allow_heldout=args.heldout)
    query = Path(args.strategy_file).read_text(encoding="utf-8")
    exclude = set(fixture.get("seeds") or []) if args.condition == "seeded" else set()
    result = harness.score(fixture, query, exclude=exclude)
    if split == "heldout":
        harness.record_heldout_look({"topic": fixture["id"], "command": "score", "condition": args.condition})
        result = harness.redact_heldout(result)
    print(json.dumps(result, indent=2))
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


def generate_once(args, fixture: dict, split: str, *, skill_dir: Path, skill_name: str, seeds: list[str],
                  provenance: dict) -> dict:
    base = f"{skill_name}-{args.driver}-{args.condition}-{stamp()}"
    label, suffix = base, 1
    while (Path(args.runs_root) / anon_dir(fixture["id"]) / label).exists():  # parallel runs started in the same second
        suffix += 1
        label = f"{base}-{suffix}"
    run_dir = Path(args.runs_root) / anon_dir(fixture["id"]) / label
    run_dir.mkdir(parents=True)
    staged = drivers.stage_skill(skill_dir, run_dir)
    skill_hash = harness.tree_hash(staged)  # before the run: an agent may write inside its skill copy
    (run_dir / "work").mkdir()
    prompt = drivers.prompt_for(fixture, seeds=seeds, depth=args.depth)
    (run_dir / "prompt.txt").write_text(prompt, encoding="utf-8")
    print(f"  {fixture['id']} {label}\n  run dir: {run_dir}", flush=True)
    extra = {"effort": args.effort} if args.driver == "codex" and args.effort else {}
    run = drivers.DRIVERS[args.driver](prompt, run_dir, env=child_env(skill_dir, fixture.get("as_of")),
                                       timeout=args.timeout, model=args.model, **extra)
    transcript = ""
    for name in ("transcript.json", "transcript.jsonl"):
        if (run_dir / name).exists():
            transcript = (run_dir / name).read_text(encoding="utf-8", errors="replace")
    card = {"topic": fixture["id"], "source": f"generated:{skill_name}", "driver": args.driver,
            "model": args.model, "effort": args.effort, "condition": args.condition, "depth": args.depth, "run_label": label,
            "scored": stamp(), "skill": {"name": skill_name, "hash": skill_hash, **provenance["skill"]},
            "harness": provenance["harness"], "driver_version": provenance["driver_version"],
            "run": {k: v for k, v in run.items() if k != "final_message"},
            "final_message": run.get("final_message", "")}
    protected = (skill_dir / "scripts" / "psb" / "validation.py").exists()
    strategy_path = find_strategy_file(run_dir, require_protected=protected, effective_as_of=fixture.get("as_of"))
    if strategy_path is not None:
        query = strategy_path.read_text(encoding="utf-8")
        seen = harness.gold_seen(fixture, run_dir) - set(seeds)
        card["strategy"] = " ".join(query.split())
        card["strategy_path"] = strategy_path.relative_to(run_dir).as_posix()
        card.update(harness.score(fixture, query, exclude=set(seeds), seen=seen))
        card["leakage"] = harness.leakage(fixture, run_dir, transcript)
    else:
        card["error"] = "no current protected delivery" if protected else "no final_strategy.txt"
        unfinished = harness.diagnostic_handoff(run_dir)
        if unfinished:  # what the undelivered query would have retrieved; never counted as delivered
            scored = harness.score(fixture, unfinished["query"], exclude=set(seeds))
            card["unfinished"] = {"blockers": unfinished["blockers"],
                                  **{k: scored[k] for k in ("count", "gold_reachable", "retrieved", "recall_percent")}}
    card["status"] = harness.run_status(card, drivers.error_text(run_dir))
    card["valid"] = card["status"] == "ok"
    out = save(fixture["id"], label, seal(card, split))
    if split == "heldout":
        harness.record_heldout_look({"topic": fixture["id"], "command": "generate", "run_label": label,
                                     "skill_hash": card["skill"]["hash"], "skill_commit": card["skill"].get("commit"),
                                     "driver": args.driver, "condition": args.condition, "status": card["status"]})
    else:  # an audit names the records a strategy found and missed, so held-out runs never keep one
        for report_name in ("audit.md", "report.md"):  # our own skill vs. others' naming
            report_path = run_dir / "work" / report_name
            if report_path.exists():
                shutil.copy2(report_path, out.with_suffix(".audit.md"))
                break
    print(f"  status={card['status']} recall={card.get('recall_percent')}% "
          f"({card.get('retrieved')}/{card.get('gold_reachable')}) unseen={card.get('unseen_recall_percent')}% "
          f"count={card.get('count')} cost=${card['run'].get('cost_usd')} seconds={card['run'].get('seconds')} "
          f"leakage={card.get('leakage')}\n  scorecard: {out}", flush=True)
    return card


def cmd_generate(args) -> int:
    fixture = harness.load_fixture(args.topic)
    split = guard_topic(fixture, allow_heldout=args.heldout)
    skill_dir = Path(args.skill).resolve()
    skill_name = args.skill_name or skill_dir.name
    seeds = list(fixture.get("seeds") or []) if args.condition == "seeded" else []
    if args.condition == "seeded" and not seeds:
        raise SystemExit(f"{fixture['id']} has no seeds")
    provenance = {"skill": harness.git_state(skill_dir), "harness": harness.git_state(harness.EVALS),
                  "driver_version": drivers.driver_version(args.driver)}
    status = 0
    for repeat in range(args.runs):
        for attempt in range(args.retry_infra + 1):
            print(f"[{repeat + 1}/{args.runs}]" + (f" infra retry {attempt}" if attempt else ""), flush=True)
            card = generate_once(args, fixture, split, skill_dir=skill_dir, skill_name=skill_name, seeds=seeds,
                                 provenance=provenance)
            if card["status"] != "infra" or attempt == args.retry_infra:
                break
            print(f"  infrastructure failure; retrying in {args.retry_wait}s", flush=True)
            time.sleep(args.retry_wait)
        if card["status"] != "ok":
            status = 2
    return status


# -- report ---------------------------------------------------------------------------------------

def card_version(card: dict) -> str:
    """``baseline`` for naive/reference cards, ``legacy`` for runs scored before versions were
    recorded, otherwise the staged skill's hash (``+dirty`` when its checkout had edits)."""
    if not str(card.get("source", "")).startswith("generated:"):
        return "baseline"
    skill = card.get("skill") or {}
    if not skill.get("hash"):
        return "legacy"
    return skill["hash"][:10] + ("+dirty" if skill.get("dirty") else "")


def latest_versions(cards: list[dict]) -> dict[tuple, str]:
    """The version of the most recently scored run of each (source, driver)."""
    latest: dict[tuple, tuple[str, str]] = {}
    for card in cards:
        key = (card["source"], card.get("driver", ""))
        if key not in latest or card.get("scored", "") > latest[key][0]:
            latest[key] = (card.get("scored", ""), card_version(card))
    return {key: version for key, (_, version) in latest.items()}


def spread(values: list) -> str:
    values = [v for v in values if v is not None]
    if not values:
        return "n/a"
    mean = round(statistics.mean(values), 1)
    return f"{mean}" if len(values) == 1 else f"{mean} ({min(values)}-{max(values)})"


def mean_of(values: list) -> float | None:
    values = [v for v in values if v is not None]
    return statistics.mean(values) if values else None


def results_table(groups: dict[tuple, list[dict]]) -> list[str]:
    lines = ["| Topic | Source | Condition | Version | Runs | Recall % | Unseen recall % | Results | NNR | Cost $ |",
             "|---|---|---|---|---:|---|---|---:|---:|---:|"]
    for (topic, source, condition, driver, version), group in sorted(groups.items()):
        statuses = [harness.run_status(c) for c in group]
        ok = [c for c, s in zip(group, statuses) if s == "ok"]
        attempted = sum(s != "infra" for s in statuses)
        infra = len(group) - attempted
        thin = source.startswith("generated:") and len(ok) < MIN_RUNS
        runs = f"{len(ok)}/{attempted}" + (f" +{infra} infra" if infra else "") + (" †" if thin else "")
        label = source + (f" ({driver})" if driver else "")
        lines.append(
            f"| {topic[:40]} | {label} | {condition} | {version} | {runs} | {spread([c['recall_percent'] for c in ok])} "
            f"| {spread([c.get('unseen_recall_percent') for c in ok])} | {spread([c.get('count') for c in ok])} "
            f"| {spread([c.get('nnr') for c in ok])} | {spread([c.get('run', {}).get('cost_usd') for c in ok])} |")
    return lines


def paired_table(groups: dict[tuple, list[dict]], a: str, b: str) -> list[str]:
    """Topic-by-topic comparison of two sources: recall win/tie/loss and the ratio of result counts."""
    ok: dict[tuple, list[dict]] = {}
    for (topic, source, condition, driver, _), group in groups.items():
        if source in (a, b):
            ok.setdefault((driver, condition, topic, source), []).extend(
                c for c in group if harness.run_status(c) == "ok")
    lines = []
    for driver, condition in sorted({(d, c) for d, c, _, _ in ok}):
        paired = sorted({t for d, c, t, _ in ok if (d, c) == (driver, condition)
                         and ok.get((d, c, t, a)) and ok.get((d, c, t, b))})
        if not paired:
            continue
        tally = {"win": 0, "tie": 0, "loss": 0}
        heavy = thin_topics = 0
        rows = []
        for topic in paired:
            ca, cb = ok[(driver, condition, topic, a)], ok[(driver, condition, topic, b)]
            ra, rb = mean_of([c["recall_percent"] for c in ca]), mean_of([c["recall_percent"] for c in cb])
            na, nb = mean_of([c.get("count") for c in ca]), mean_of([c.get("count") for c in cb])
            result = "tie" if abs(ra - rb) < TIE_POINTS else "win" if ra > rb else "loss"
            tally[result] += 1
            ratio = round(na / nb, 2) if na is not None and nb else None
            flagged = ratio is not None and (ratio > WORKLOAD_FLAG or ratio < 1 / WORKLOAD_FLAG)
            heavy += bool(ratio is not None and ratio > WORKLOAD_FLAG)
            thin = len(ca) < MIN_RUNS or len(cb) < MIN_RUNS
            thin_topics += thin
            rows.append(f"| {topic[:40]} | {round(ra, 1)} | {round(rb, 1)} | {result} | {round(na or 0):,} "
                        f"| {round(nb or 0):,} | {ratio}{' ⚠' if flagged else ''} | {len(ca)}/{len(cb)}{' †' if thin else ''} |")
        lines += [f"**A = {a} vs B = {b}** ({driver or 'no driver'}, {condition}): {tally['win']} win, {tally['tie']} tie, "
                  f"{tally['loss']} loss on recall; {heavy} topic(s) where A returns more than {WORKLOAD_FLAG:g}× B's results; "
                  f"{thin_topics} topic(s) with fewer than {MIN_RUNS} ok runs a side.",
                  "",
                  "| Topic | Recall A | Recall B | Recall | Results A | Results B | Ratio A/B | Runs A/B |",
                  "|---|---:|---:|---|---:|---:|---:|---:|", *rows, ""]
    return lines


def cmd_report(args) -> int:
    cards = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(harness.RESULTS.glob("*/*.json"))]
    splits = harness.load_splits()
    latest = latest_versions([c for c in cards if str(c.get("source", "")).startswith("generated:")])
    by_split: dict[str, dict[tuple, list[dict]]] = {}
    for card in cards:
        version = card_version(card)
        if not args.all_versions and version != "baseline" and latest.get((card["source"], card.get("driver", ""))) != version:
            continue
        key = (card["topic"], card["source"], card.get("condition", "noseed"), card.get("driver", ""), version)
        by_split.setdefault(harness.split_of(card["topic"], splits), {}).setdefault(key, []).append(card)
    lines = [
        "# Evaluation results",
        "",
        f"Generated {stamp()} by `python evals/run.py report{' --all-versions' if args.all_versions else ''}`.",
        "",
        "Recall is over gold records in PubMed on or before `as_of`; in the seeded condition the three seeds are "
        "excluded. `unseen` recall leaves out gold records the agent itself screened into its sets. NNR is total "
        "results divided by gold retrieved: a workload proxy, not precision. Generated rows show the mean (min-max) "
        "over `ok` runs.",
        "",
        "Version is a hash of the skill as staged into the run (`legacy`: scored before versions were recorded). "
        + ("Every version is shown." if args.all_versions else
           "Only the latest version of each skill and driver is shown; `--all-versions` shows the rest.")
        + " Runs is ok/attempted; infrastructure failures (quota, rate limits) are not attempts."
        + f" † fewer than {MIN_RUNS} ok runs. ⚠ result counts differ by more than {WORKLOAD_FLAG:g}×.",
        "",
    ]
    sections = (
        ("dev", "Development topics", "Skill changes may be motivated only by these topics."),
        ("heldout", "Held-out topics",
         "Frozen before their first run; misses and audits are never kept. Claim an improvement only from the "
         f"latest version with at least {MIN_RUNS} ok runs a side. Every use is logged in "
         f"`evals/{harness.HELDOUT_LEDGER.name}`."),
        ("unassigned", "Unassigned topics", "Not in `evals/splits.json`; assign them before drawing conclusions."),
    )
    for split, title, note in sections:
        groups = by_split.get(split)
        if groups:
            lines += [f"## {title}", "", note, "", *paired_table(groups, *args.pair), *results_table(groups), ""]
    if splits["retired"]:
        lines += ["## Retired topics", "", *[f"- {t}: {why}" for t, why in sorted(splits["retired"].items())], ""]
    path = harness.EVALS / "RESULTS.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {path} ({sum(len(g) for g in by_split.values())} rows)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--env-file", default=str(harness.REPO / ".env"))
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("baselines")
    p.add_argument("topics", nargs="*")
    p.add_argument("--no-cache", action="store_true")
    p.add_argument("--heldout", action="store_true", help="also score held-out topics (logged; misses not kept)")
    p.set_defaults(func=cmd_baselines)
    p = sub.add_parser("score")
    p.add_argument("topic")
    p.add_argument("--strategy-file", required=True)
    p.add_argument("--condition", choices=["noseed", "seeded"], default="noseed")
    p.add_argument("--heldout", action="store_true", help="allow a held-out topic (logged; misses not shown)")
    p.set_defaults(func=cmd_score)
    p = sub.add_parser("generate")
    p.add_argument("topic")
    p.add_argument("--driver", choices=sorted(drivers.DRIVERS), default="claude")
    p.add_argument("--condition", choices=["noseed", "seeded"], default="noseed")
    p.add_argument("--depth", default="standard")
    p.add_argument("--skill", default=str(harness.REPO), help="skill directory to test (default: this repo)")
    p.add_argument("--skill-name", help="label for results (default: directory name)")
    p.add_argument("--model")
    p.add_argument("--effort", choices=["low", "medium", "high"], help="codex model_reasoning_effort (default: medium)")
    p.add_argument("--runs", type=int, default=1)
    p.add_argument("--timeout", type=int, default=5400)
    p.add_argument("--runs-root", default=str(DEFAULT_RUNS_ROOT))
    p.add_argument("--heldout", action="store_true", help="allow a held-out topic (logged; misses not kept)")
    p.add_argument("--retry-infra", type=int, default=0, help="retry a run that failed on quota/rate limits up to N times")
    p.add_argument("--retry-wait", type=int, default=300, help="seconds to wait before an infra retry")
    p.set_defaults(func=cmd_generate)
    p = sub.add_parser("freeze", help="add never-run topics to the held-out set")
    p.add_argument("topics", nargs="+")
    p.set_defaults(func=cmd_freeze)
    p = sub.add_parser("report")
    p.add_argument("--all-versions", action="store_true", help="show every skill version, not only the latest")
    p.add_argument("--pair", nargs=2, default=["generated:ours", "generated:lean-optimal"], metavar=("A", "B"),
                   help="two sources to compare topic by topic")
    p.set_defaults(func=cmd_report)
    args = parser.parse_args()
    if args.env_file and Path(args.env_file).exists():
        config.use_env_file(args.env_file)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
