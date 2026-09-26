"""`psb` command line. Every command prints one JSON object; failures exit non-zero with
``{"ok": false, "error": ...}``. Commands that touch PubMed log each request to the workspace."""

from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

from . import config, deliver, mesh, terms
from .evaluate import compare, evaluate
from .ncbi import LINKNAMES, NcbiError, PubMed
from .strategy import StrategyError, lint, numbered_lines, full_query
from .workspace import ROLES, Workspace, WorkspaceError, find_root, normalize_pmids, now, sha256_text


class UsageError(RuntimeError):
    pass


def emit(data: object) -> None:
    text = json.dumps(data, indent=2, ensure_ascii=False)
    try:
        sys.stdout.write(text + "\n")
    except UnicodeEncodeError:
        sys.stdout.write(json.dumps(data, indent=2, ensure_ascii=True) + "\n")


def workspace(args) -> Workspace:
    ws = Workspace(find_root(args.workspace), use_cache=not args.no_cache)
    ws.log({"type": "command", "argv": args.argv})
    return ws


def query_arg(args) -> str:
    if args.file:
        return Path(args.file).read_text(encoding="utf-8").strip()
    if not args.query:
        raise UsageError("give a query or --file")
    return " ".join(args.query).strip()


def pmid_args(ws: Workspace, pmids: list[str], set_names: list[str] | None) -> list[str]:
    found = normalize_pmids(pmids or [])
    for name in set_names or []:
        found += [p for p in ws.get_set(name).get("pmids", []) if p not in found]
    if not found:
        raise UsageError("no PMIDs given")
    return found


# -- commands ---------------------------------------------------------------------------------

def cmd_init(args) -> dict:
    ws = Workspace.create(Path(args.directory), args.question or "")
    return {"ok": True, "workspace": str(ws.root), "next": "fill protocol.json (concepts, roles, eligibility), then build strategy.json"}


def cmd_status(args) -> dict:
    ws = workspace(args)
    protocol = ws.protocol()
    strategy = ws.strategy()
    versions = ws.versions()
    sets = ws.sets()
    critic = sorted(p.name for p in (ws.root / "critic").glob("round-*.json"))
    concepts = protocol.get("concepts") or []
    todo = []
    if not protocol.get("question"):
        todo.append("state the plain-language question in protocol.json")
    if not concepts:
        todo.append("record concepts with roles (search / screen / optional) in protocol.json")
    if not protocol.get("scope_confirmed"):
        todo.append("confirm concept roles and limits with the user (or note why not in protocol.notes)")
    if not strategy.blocks:
        todo.append("draft strategy.json blocks")
    if not sets:
        todo.append("add known relevant PMIDs (psb set add) so recall can be measured")
    if not versions:
        todo.append("run psb eval")
    elif versions[-1]["strategy_sha256"] != sha256_text(json.dumps(strategy.to_dict(), sort_keys=True)):
        todo.append("strategy.json changed since the last psb eval")
    if not critic:
        todo.append("run a critic round (psb critic packet)")
    last = versions[-1]["evaluation"] if versions else {}
    return {
        "ok": True,
        "workspace": str(ws.root),
        "question": protocol.get("question"),
        "as_of": protocol.get("as_of"),
        "depth": protocol.get("depth"),
        "concepts": [{"id": c.get("id"), "role": c.get("role")} for c in concepts],
        "blocks": [{"id": b.id, "terms": len(b.terms)} for b in strategy.blocks],
        "sets": {name: {"role": d.get("role"), "size": len(d.get("pmids", []))} for name, d in sets.items()},
        "versions": len(versions),
        "last_eval": {"count": last.get("count"), "recall": {n: s.get("recall_percent") for n, s in (last.get("sets") or {}).items()}} if last else None,
        "critic_rounds": critic,
        "todo": todo,
    }


def cmd_count(args) -> dict:
    ws = workspace(args)
    result = ws.pubmed.search(query_arg(args))
    return {"ok": True, **result}


def cmd_fetch(args) -> dict:
    ws = workspace(args)
    pmids = pmid_args(ws, args.pmids, args.set)
    records = ws.ensure_records(pmids)
    rows = [
        {"pmid": p, "year": r.get("year"), "title": r.get("title"), "publication_types": r.get("publication_types"),
         "mesh": [h["name"] for h in r.get("mesh", [])][: args.mesh],
         **({"abstract": r.get("abstract")} if args.abstracts else {})}
        for p, r in records.items()
    ]
    return {"ok": True, "found": len(records), "missing": [p for p in pmids if p not in records], "records": rows}


def cmd_sample(args) -> dict:
    ws = workspace(args)
    query = query_arg(args)
    first = ws.pubmed.search(query, retmax=0)
    total = first["count"]
    if not total:
        return {"ok": True, "count": 0, "records": []}
    start = random.Random(args.seed).randrange(max(1, min(total, 9999) - args.n + 1)) if args.random else 0
    pmids = ws.pubmed.search(query, retmax=args.n, retstart=start)["pmids"]
    records = ws.ensure_records(pmids)
    return {
        "ok": True, "count": total, "retstart": start,
        "records": [{"pmid": p, "year": r.get("year"), "title": r.get("title")} for p, r in records.items()],
    }


def cmd_neighbors(args) -> dict:
    ws = workspace(args)
    pmids = pmid_args(ws, args.pmids, args.set)
    known = {p for d in ws.sets().values() for p in d.get("pmids", [])} if args.exclude_known else set()
    scores: dict[str, dict] = {}
    for link in args.links.split(","):
        link = link.strip()
        if link not in LINKNAMES:
            raise UsageError(f"unknown link {link!r}; use {', '.join(LINKNAMES)}")
        for pmid in pmids:
            for row in ws.pubmed.links(pmid, link)[: args.max_per_seed]:
                entry = scores.setdefault(row["pmid"], {"pmid": row["pmid"], "from": [], "links": set(), "best_score": 0})
                entry["from"].append(pmid)
                entry["links"].add(link)
                entry["best_score"] = max(entry["best_score"], row["score"] or 0)
    candidates = [e for p, e in scores.items() if p not in known and p not in pmids]
    if ws.pubmed.as_of and candidates:
        dated = ws.pubmed.existing([e["pmid"] for e in candidates])
        candidates = [e for e in candidates if e["pmid"] in dated]
    candidates.sort(key=lambda e: (-len(set(e["from"])), -e["best_score"], e["pmid"]))
    rows = [{**e, "links": sorted(e["links"]), "from": sorted(set(e["from"]))} for e in candidates[: args.limit]]
    return {"ok": True, "seeds": len(pmids), "candidates": len(candidates), "shown": len(rows), "rows": rows,
            "note": "Neighbours are candidates, not relevant records: screen them before using them for mining."}


def cmd_resolve(args) -> dict:
    ws = workspace(args)
    resolved, unresolved = {}, []
    pmcids = [i for i in args.ids if i.upper().startswith("PMC")]
    if pmcids:
        resolved.update(ws.pubmed.idconv(pmcids))
    for ident in args.ids:
        if ident in resolved:
            continue
        clean = ident.strip()
        if clean.isdigit():
            resolved[ident] = clean
        elif clean.lower().startswith(("10.", "doi:", "https://doi.org/")):
            doi = clean.split("doi.org/")[-1].removeprefix("doi:").strip()
            hits = ws.pubmed.search(f'"{doi}"[doi]', retmax=2, dated=False)["pmids"]
            if len(hits) == 1:
                resolved[ident] = hits[0]
    unresolved = [i for i in args.ids if i not in resolved]
    exists = ws.pubmed.existing(resolved.values()) if resolved else set()
    return {"ok": True, "resolved": resolved, "not_in_pubmed_or_after_as_of": sorted(set(resolved.values()) - exists), "unresolved": unresolved}


def cmd_mesh(args) -> dict:
    ws = workspace(args)
    if args.mesh_command == "lookup":
        return {"ok": True, **mesh.lookup(ws.pubmed, " ".join(args.term), limit=args.limit)}
    return {"ok": True, **mesh.show(ws.pubmed, " ".join(args.identifier), counts=not args.no_counts)}


def cmd_set(args) -> dict:
    ws = workspace(args)
    if args.set_command == "list":
        return {"ok": True, "roles": ROLES, "sets": {n: {"role": d["role"], "size": len(d["pmids"]), "source": d.get("source")} for n, d in ws.sets().items()}}
    if args.set_command == "add":
        existing = ws.get_set(args.name)["pmids"] if ws.set_path(args.name).exists() else []
        pmids = existing + [p for p in normalize_pmids(args.pmids) if p not in existing]
        return {"ok": True, **ws.save_set(args.name, args.role, pmids, source=args.source, note=args.note)}
    if args.set_command == "remove":
        data = ws.get_set(args.name)
        drop = set(normalize_pmids(args.pmids))
        return {"ok": True, **ws.save_set(args.name, data["role"], [p for p in data["pmids"] if p not in drop], source=data.get("source", ""), note=data.get("note", ""))}
    # split: move a random fraction of one set into a held-out validation set
    data = ws.get_set(args.name)
    pmids = list(data["pmids"])
    rng = random.Random(args.seed)
    held = sorted(rng.sample(pmids, max(1, round(len(pmids) * args.fraction)))) if pmids else []
    if len(pmids) - len(held) < 1:
        raise UsageError("split would leave nothing for development")
    ws.save_set(args.name, data["role"], [p for p in pmids if p not in held], source=data.get("source", ""), note=data.get("note", ""))
    out = ws.save_set(args.into, "validation", held, source=f"split from {args.name} (seed {args.seed}, fraction {args.fraction})")
    return {"ok": True, "development": len(pmids) - len(held), "validation": len(held), "validation_set": out["name"],
            "note": "Do not mine the validation set. Every psb eval shows its recall, so it is consulted repeatedly: report it as semi-independent."}


def cmd_lint(args) -> dict:
    ws = workspace(args)
    strategy = ws.strategy()
    issues = lint(strategy, concepts=ws.protocol().get("concepts") or [])
    body = {"ok": not any(i["severity"] == "error" for i in issues), "issues": issues}
    if not strategy.structural_errors():
        body["lines"] = [{"n": l["n"], "text": l["text"]} for l in numbered_lines(strategy)]
        body["query"] = full_query(strategy)
    return body


def cmd_eval(args) -> dict:
    ws = workspace(args)
    evaluation = evaluate(ws, term_counts=not args.no_term_counts)
    if not evaluation.get("ok"):
        return evaluation
    versions = ws.versions()
    previous = versions[-1] if versions else None
    strategy = ws.strategy().to_dict()
    changed = previous is None or previous["strategy_sha256"] != sha256_text(json.dumps(strategy, sort_keys=True))
    diff = compare(previous, evaluation, strategy)
    if diff:
        evaluation["since_previous"] = diff
    if changed or args.note:
        if diff and diff["regression"] and not args.note:
            evaluation["warning"] = "this version lost known relevant records; record why with --note or revert"
        saved = ws.save_version(evaluation, args.note or "")
        evaluation["version"] = saved["version"]
    else:
        evaluation["version"] = previous["version"] if previous else None
        evaluation["saved"] = "unchanged strategy; no new version"
    if args.brief:
        evaluation.pop("lines", None)
        evaluation.pop("retrieved_known", None)
        evaluation.pop("known_in_pubmed", None)
    else:
        evaluation.pop("known_in_pubmed", None)
    return evaluation


def cmd_terms(args) -> dict:
    ws = workspace(args)
    strategy = ws.strategy()
    if args.terms_command == "rank":
        if args.set:
            held_out = {n for n, d in ws.sets().items() if d.get("role") in {"validation", "benchmark"}}
            bad = [n for n in args.set if n in held_out]
            if bad and not args.allow_held_out:
                raise UsageError(f"{', '.join(bad)} is held out; mining it would make its recall meaningless")
            pmids = pmid_args(ws, [], args.set)
        else:
            pmids = ws.mining_pmids()
        if not pmids:
            raise UsageError("no mining records: add a seed or relevant set")
        records = list(ws.ensure_records(pmids).values())
        return {"ok": True, **terms.rank(ws.pubmed, records, strategy, fields=args.fields.split(","),
                                          budget=args.budget, min_df=args.min_df, include_covered=args.include_covered)}
    versions = ws.versions()
    if not versions:
        raise UsageError("run psb eval first")
    evaluation = versions[-1]["evaluation"]
    missed = [m["pmid"] for m in evaluation.get("misses", []) if not args.set or set(m["sets"]) & set(args.set)]
    records = list(ws.ensure_records(missed).values())
    return {"ok": True, "version": versions[-1]["version"], "misses": terms.miss_report(records, evaluation, strategy),
            "note": "Vocabulary from missed records is a candidate. Adding a term to recover a validation miss "
                    "makes that set part of development; say so in the audit."}


def cmd_critic(args) -> dict:
    ws = workspace(args)
    if args.critic_command == "packet":
        path = deliver.critic_packet(ws)
        return {"ok": True, "packet": str(path),
                "next": "give only this file to a fresh-context reviewer (subagent) and save its JSON as "
                        f"critic/round-N.json; then run psb critic check"}
    path = Path(args.round) if args.round else max((ws.root / "critic").glob("round-*.json"), default=None)
    if path is None:
        raise UsageError("no critic/round-*.json to check")
    return {"round_file": str(path), **deliver.check_round(ws, path)}


def cmd_report(args) -> dict:
    if args.fresh:
        args.no_cache = True
        args.note = args.note or "final counts, run live"
        args.no_term_counts = False
        args.brief = True
        refreshed = cmd_eval(args)  # a note always saves a version, so the live counts are recorded
        if not refreshed.get("ok"):
            return refreshed
    ws = workspace(args)
    path = deliver.report(ws)
    open_must = [f.get("id") for r in deliver.critic_rounds(ws)[-1:] for f in r.get("findings", [])
                 if f.get("status") == "open" and f.get("severity") == "must-fix"]
    return {"ok": True, "report": str(path), "open_must_fix_findings": open_must}


def cmd_log(args) -> dict:
    ws = Workspace(find_root(args.workspace))
    entries = ws.log_entries()
    ncbi = [e for e in entries if e.get("type") == "ncbi"]
    return {"ok": True, "entries": len(entries), "ncbi_requests": len(ncbi),
            "from_cache": sum(1 for e in ncbi if e.get("cache")), "tail": entries[-args.tail:] if args.tail else []}


def cmd_doctor(args) -> dict:
    pm = PubMed()
    result = pm.search("asthma[tiab]", dated=False)
    return {"ok": True, "email_configured": bool(pm.email), "api_key_configured": bool(pm.api_key),
            "rate_per_second": pm.per_second, "test_query": "asthma[tiab]", "test_count": result["count"]}


def cmd_cache(args) -> dict:
    ws = Workspace(find_root(args.workspace))
    if args.clear:
        return {"ok": True, "removed": ws.pubmed.cache.clear()}
    entries = list((ws.root / ".cache").glob("*/*.json")) if (ws.root / ".cache").is_dir() else []
    return {"ok": True, "entries": len(entries), "directory": str(ws.root / ".cache")}


# -- parser ------------------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="psb", description="PubMed search builder tools")
    parser.add_argument("--workspace", help="run workspace (default: nearest directory with protocol.json)")
    parser.add_argument("--no-cache", action="store_true", help="bypass the workspace NCBI cache")
    parser.add_argument("--env-file", help="read NCBI settings from this file instead of the skill's .env")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("init", help="create a run workspace")
    p.add_argument("directory")
    p.add_argument("--question", default="")
    p.set_defaults(func=cmd_init)

    sub.add_parser("status", help="what exists and what is still to do").set_defaults(func=cmd_status)

    for name, func, help_text in (("count", cmd_count, "count a query and show PubMed's translation"),
                                  ("sample", cmd_sample, "fetch a few records a query retrieves")):
        p = sub.add_parser(name, help=help_text)
        p.add_argument("query", nargs="*")
        p.add_argument("--file")
        if name == "sample":
            p.add_argument("--n", type=int, default=10)
            p.add_argument("--random", action="store_true", help="sample from a random offset")
            p.add_argument("--seed", type=int, default=1)
        p.set_defaults(func=func)

    p = sub.add_parser("fetch", help="fetch and store records")
    p.add_argument("pmids", nargs="*")
    p.add_argument("--set", action="append")
    p.add_argument("--abstracts", action="store_true")
    p.add_argument("--mesh", type=int, default=12, help="MeSH headings shown per record")
    p.set_defaults(func=cmd_fetch)

    p = sub.add_parser("neighbors", help="similar, citing, or cited records of known PMIDs")
    p.add_argument("pmids", nargs="*")
    p.add_argument("--set", action="append")
    p.add_argument("--links", default="similar")
    p.add_argument("--max-per-seed", type=int, default=50)
    p.add_argument("--limit", type=int, default=100)
    p.add_argument("--exclude-known", action="store_true", help="drop PMIDs already in a set")
    p.set_defaults(func=cmd_neighbors)

    p = sub.add_parser("resolve", help="PMIDs from PMIDs, DOIs, or PMCIDs")
    p.add_argument("ids", nargs="+")
    p.set_defaults(func=cmd_resolve)

    p = sub.add_parser("mesh", help="MeSH lookup and details")
    msub = p.add_subparsers(dest="mesh_command", required=True)
    q = msub.add_parser("lookup")
    q.add_argument("term", nargs="+")
    q.add_argument("--limit", type=int, default=8)
    q = msub.add_parser("show")
    q.add_argument("identifier", nargs="+", help="descriptor UI (D...) or exact heading")
    q.add_argument("--no-counts", action="store_true")
    p.set_defaults(func=cmd_mesh)

    p = sub.add_parser("set", help="PMID sets with roles")
    ssub = p.add_subparsers(dest="set_command", required=True)
    ssub.add_parser("list")
    q = ssub.add_parser("add")
    q.add_argument("name")
    q.add_argument("pmids", nargs="+")
    q.add_argument("--role", required=True, choices=sorted(ROLES))
    q.add_argument("--source", default="")
    q.add_argument("--note", default="")
    q = ssub.add_parser("remove")
    q.add_argument("name")
    q.add_argument("pmids", nargs="+")
    q = ssub.add_parser("split")
    q.add_argument("name")
    q.add_argument("--into", default="validation")
    q.add_argument("--fraction", type=float, default=0.3)
    q.add_argument("--seed", type=int, default=1)
    p.set_defaults(func=cmd_set)

    sub.add_parser("lint", help="offline checks and the numbered line set").set_defaults(func=cmd_lint)

    p = sub.add_parser("eval", help="count, recall, misses, ablation, and change since last version")
    p.add_argument("--note", default="", help="why this version changed")
    p.add_argument("--no-term-counts", action="store_true")
    p.add_argument("--brief", action="store_true", help="omit per-line counts")
    p.set_defaults(func=cmd_eval)

    p = sub.add_parser("terms", help="term mining")
    tsub = p.add_subparsers(dest="terms_command", required=True)
    q = tsub.add_parser("rank", help="rank candidate terms from known relevant records")
    q.add_argument("--set", action="append")
    q.add_argument("--fields", default="tiab,mesh")
    q.add_argument("--budget", type=int, default=40, help="background counts to spend")
    q.add_argument("--min-df", type=int, default=2)
    q.add_argument("--include-covered", action="store_true")
    q.add_argument("--allow-held-out", action="store_true")
    q = tsub.add_parser("miss", help="diagnose missed known records from the last eval")
    q.add_argument("--set", action="append")
    p.set_defaults(func=cmd_terms)

    p = sub.add_parser("critic", help="PRESS critic packet and round check")
    csub = p.add_subparsers(dest="critic_command", required=True)
    csub.add_parser("packet", help="write critic/packet-N.md from the latest evaluated version")
    q = csub.add_parser("check", help="validate a critic/round-N.json")
    q.add_argument("round", nargs="?")
    p.set_defaults(func=cmd_critic)

    p = sub.add_parser("report", help="render audit.md from the workspace")
    p.add_argument("--fresh", action="store_true", help="re-run the evaluation live (no cache) first")
    p.add_argument("--note", default="")
    p.set_defaults(func=cmd_report)

    p = sub.add_parser("log", help="summarise the workspace log")
    p.add_argument("--tail", type=int, default=0)
    p.set_defaults(func=cmd_log)

    sub.add_parser("doctor", help="check NCBI configuration with one live query").set_defaults(func=cmd_doctor)
    p = sub.add_parser("cache", help="inspect or clear the workspace cache")
    p.add_argument("--clear", action="store_true")
    p.set_defaults(func=cmd_cache)
    return parser


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    parser = build_parser()
    args = parser.parse_args(argv)
    args.argv = argv
    if args.env_file:
        config.use_env_file(args.env_file)
    try:
        result = args.func(args)
    except (WorkspaceError, StrategyError, UsageError, NcbiError, ValueError, OSError) as exc:
        emit({"ok": False, "error": str(exc), "error_type": type(exc).__name__})
        return 1
    emit(result)
    return 0 if result.get("ok", True) else 1
