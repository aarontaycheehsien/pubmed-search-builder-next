"""`psb` command line. Every command prints one JSON object; failures exit non-zero with
``{"ok": false, "error": ...}``. Commands that touch PubMed log each request to the workspace.

An invocation that serves the separate screening context is restricted (disclosure.py): ``main``
decides that from the parsed arguments before anything else happens, and the invocation's own
Workspace then routes its requests, cache and logs, and its messages say only what is permitted."""

from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path

from . import allocation, config, deliver, disclosure, holdout, mesh, progress, reserved, terms, validation
from .evaluate import compare, evaluate
from .ncbi import LINKNAMES, NcbiError, PubMed
from .strategy import StrategyError, lint, numbered_lines, full_query
from .workspace import (LEGACY_ROLES, ORIGINS, PURPOSES, Workspace, WorkspaceError, find_root, normalize_pmids, now,
                        purpose_label, purpose_of, read_json, sha256_text)


class UsageError(RuntimeError):
    pass


def emit(data: object) -> None:
    text = json.dumps(data, indent=2, ensure_ascii=False)
    try:
        sys.stdout.write(text + "\n")
    except UnicodeEncodeError:
        sys.stdout.write(json.dumps(data, indent=2, ensure_ascii=True) + "\n")


SUBCOMMANDS = {"mesh": "mesh_command", "set": "set_command", "terms": "terms_command", "critic": "critic_command",
               "exposure": "exposure_command", "progress": "stage"}


def command_words(args) -> list[str]:
    """The command and its subcommand or progress stage: fixed words that never carry an argument."""
    words = [args.command]
    attr = SUBCOMMANDS.get(args.command)
    if attr and getattr(args, attr, None):
        words.append(getattr(args, attr))
    return words


def workspace(args) -> Workspace:
    # A restricted invocation's Workspace builds its client with the private cache and logger, and
    # its command row keeps only the command words in log.jsonl (the argv goes to screening/log.jsonl).
    ws = Workspace(find_root(args.workspace), use_cache=not args.no_cache, restricted=getattr(args, "restricted", False))
    ws.log({"type": "command", "command": command_words(args), "argv": args.argv})
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
    if not protocol.get("scope_confirmed") and not str(protocol.get("notes") or "").strip():
        todo.append("confirm concept roles and limits with the user (or note why not in protocol.notes)")
    if not strategy.blocks:
        todo.append("draft strategy.json blocks")
    if not sets and protocol.get("depth") != "quick":
        todo.append("add known relevant PMIDs (psb set add) so recall can be measured")
    held = allocation.summary(ws)
    included = any(row["decision"] == "include" for row in progress.decisions(ws).values())
    if held is None and (sets or included):
        todo.append("freeze the allocation of the known records (psb allocate --preview, then psb allocate)")
    elif held and held["stale"]:
        todo.append(f"the allocation is stale ({'; '.join(held['stale'])}): re-screen the reserved records, then "
                    "psb allocate --rebind")
    elif held and held["H"] and not held["released"] and not holdout.receipts(ws):
        todo.append("after the critic review, run the held-out test (psb holdout-test) before psb report")
    if not versions:
        todo.append("run psb eval")
    elif versions[-1]["strategy_sha256"] != sha256_text(json.dumps(strategy.to_dict(), sort_keys=True)):
        todo.append("strategy.json changed since the last psb eval")
    if not critic:
        todo.append("run a critic round (psb critic packet)")
    last = versions[-1]["evaluation"] if versions else {}
    delivery = deliver.verify_delivery(ws)
    if not delivery["ok"] and (ws.root / "validation-manifest.json").exists():
        todo.append(f"the delivery is no longer current: {delivery['error']}")
    sent, reminders = progress.stage_reminders(ws)
    todo += reminders
    try:
        left = deliver.rounds_left(ws)
    except (WorkspaceError, ValueError, OSError) as exc:  # psb status never fails because of critic files
        left = f"unknown ({exc})"
    return {
        "ok": True,
        "workspace": str(ws.root),
        "question": protocol.get("question"),
        "as_of": protocol.get("as_of"),
        "depth": protocol.get("depth"),
        "concepts": [{"id": c.get("id"), "role": c.get("role")} for c in concepts],
        "blocks": [{"id": b.id, "terms": len(b.terms)} for b in strategy.blocks],
        "sets": {name: {"purpose": purpose_label(d), "size": len(d.get("pmids", []))} for name, d in sets.items()},
        "allocation": held,
        "holdout_receipts": [{"number": r["number"], "status": r.get("status")} for r in holdout.receipts(ws)],
        "versions": len(versions),
        "last_eval": {"count": last.get("count"), "recall": {n: s.get("recall_percent") for n, s in (last.get("sets") or {}).items()}} if last else None,
        "critic_rounds": critic,
        "critic_rounds_left": left,
        "delivery": delivery,
        "stage_summaries_sent": sent,
        "todo": todo,
    }


def cmd_count(args) -> dict:
    ws = workspace(args)
    query = query_arg(args)
    reserved.check_query(ws, query)
    result = ws.pubmed.search(query)
    body = {"ok": True, **result}
    if args.purpose and args.restricted:
        progress.attach_restricted(body, ws, f"search:{args.purpose}")
    elif args.purpose:
        progress.attach(body, ws, f"search:{args.purpose}", {"query": query, "count": result["count"],
                                                            "translation": result["translation"], "issues": result["issues"]})
    return body


def cmd_fetch(args) -> dict:
    ws = workspace(args)
    pmids = pmid_args(ws, args.pmids, args.set)
    if not args.screening:
        reserved.refuse(ws, pmids, "fetching")
    records = ws.ensure_records(pmids, private=args.screening)
    rows = [
        {"pmid": p, "year": r.get("year"), "title": r.get("title"), "publication_types": r.get("publication_types"),
         "mesh": [h["name"] for h in r.get("mesh", [])][: args.mesh],
         **({"abstract": r.get("abstract")} if args.abstracts else {})}
        for p, r in records.items()
    ]
    if not args.screening and records:
        reserved.record(ws, list(records), "abstract" if args.abstracts else "title", "fetch")
    body = {"ok": True, "found": len(records), "missing": [p for p in pmids if p not in records], "records": rows,
            **({"store": "screening (private to the separate screening context)"} if args.screening else {})}
    if args.restricted:
        progress.attach_restricted(body, ws, "fetch", processed=len(records))
    return body


def cmd_sample(args) -> dict:
    if args.restricted and args.purpose not in progress.CANDIDATE_PURPOSES:
        # A private sample must leave a candidate batch: the allocation reads origins from it.
        raise UsageError("sample --screening needs --purpose prior-reviews or --purpose pilot, so that its records "
                         "are recorded as a candidate batch")
    ws = workspace(args)
    query = query_arg(args)
    if not args.screening:
        reserved.check_query(ws, query)
    first = ws.pubmed.search(query, retmax=0)
    total = first["count"]
    if not total:
        body = {"ok": True, "count": 0, "records": []}
        if args.restricted:
            progress.attach_restricted(body, ws, f"search:{args.purpose}", processed=0)
        elif args.purpose:
            progress.attach(body, ws, f"search:{args.purpose}", {"query": query, "count": 0, "shown": 0,
                                                                "translation": first["translation"], "issues": first["issues"]})
        return body
    start = random.Random(args.seed).randrange(max(1, min(total, 9999) - args.n + 1)) if args.random else 0
    # Reserved records are skipped without a trace: over-fetch by their number so the page stays full.
    hidden = 0 if args.screening else len(ws.reserved_pmids())
    page = ws.pubmed.search(query, retmax=args.n + hidden, retstart=start)["pmids"]
    pmids = page if args.screening else reserved.visible(ws, page)[: args.n]
    records = ws.ensure_records(pmids, private=args.screening)
    if not args.screening and records:
        reserved.record(ws, list(records), "title", "sample")
    body = {
        "ok": True, "count": total, "retstart": start,
        "records": [{"pmid": p, "year": r.get("year"), "title": r.get("title")} for p, r in records.items()],
    }
    # The batch is scientific provenance (allocation origins): recorded whatever the message does.
    batch = None
    if args.purpose in progress.CANDIDATE_PURPOSES and records:
        label = f"{progress.PURPOSES[args.purpose]} {progress.code(progress.clean(query, 80))}"
        batch = progress.record_batch(ws, args.purpose, label, list(records), total=total, query=query,
                                      private=args.restricted)["batch"]
    if args.restricted:
        progress.attach_restricted(body, ws, f"search:{args.purpose}", processed=len(records))
    elif args.purpose:
        found = {"query": query, "count": total, "shown": len(records), "retstart": start, "random": args.random,
                 "seed": args.seed, "translation": first["translation"], "issues": first["issues"],
                 "records": body["records"]}
        if batch:
            found["batch"] = batch
        progress.attach(body, ws, f"search:{args.purpose}", found)
    return body


def cmd_neighbors(args) -> dict:
    ws = workspace(args)
    pmids = pmid_args(ws, args.pmids, args.set)
    # Neighbours of a reserved record are derived from its content; reserved neighbours are skipped.
    reserved.refuse(ws, pmids, "listing neighbours")
    hidden = ws.reserved_pmids()
    known = {p for d in ws.sets().values() for p in d.get("pmids", [])} if args.exclude_known else set()
    known |= hidden
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
    body = {"ok": True, "seeds": len(pmids), "candidates": len(candidates), "shown": len(rows), "rows": rows,
            "note": "Neighbours are candidates, not relevant records: screen them before using them for mining."}
    links = [link.strip() for link in args.links.split(",")]
    sets = sorted(set(args.set or []))
    batch = None
    if rows:
        batch = progress.record_batch(ws, "neighbors:" + ",".join(links), progress.neighbors_label(links, pmids, sets),
                                      [r["pmid"] for r in rows], total=len(candidates), origin=pmids,
                                      private=args.restricted)["batch"]
    if args.restricted:
        return progress.attach_restricted(body, ws, "neighbors", processed=len(rows), links=links)

    def data() -> dict:
        in_sets = {p for d in ws.sets().values() for p in d.get("pmids", [])}
        found = {"links": links, "from": pmids, "sets": sets, "candidates": len(candidates),
                 "shown": len(rows), "exclude_known": args.exclude_known,
                 "per_link": {link: sum(1 for e in candidates if link in e["links"]) for link in links},
                 "known": sum(1 for p in scores if p in in_sets and p not in pmids),
                 "rows": rows, "max_per_seed": args.max_per_seed}
        if batch:
            found["batch"] = batch
        return found
    return progress.attach(body, ws, "neighbors", data)


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
            # PubMed answers 0005[uid] as 5: store the PMID it will report, or the existence check
            # wrongly calls the record missing. An all-zero identifier is not a PMID.
            if clean.lstrip("0"):
                resolved[ident] = clean.lstrip("0")
        elif clean.lower().startswith(("10.", "doi:", "https://doi.org/")):
            doi = clean.split("doi.org/")[-1].removeprefix("doi:").strip()
            hits = ws.pubmed.search(f'"{doi}"[doi]', retmax=2, dated=False)["pmids"]
            if len(hits) == 1:
                resolved[ident] = hits[0]
    unresolved = [i for i in args.ids if i not in resolved]
    exists = ws.pubmed.existing(resolved.values()) if resolved else set()
    body = {"ok": True, "resolved": resolved, "not_in_pubmed_or_after_as_of": sorted(set(resolved.values()) - exists), "unresolved": unresolved}
    # Screening normalises PMIDs, so the batch must too, or attribution misses "00123".
    usable = [v for v in map(str, resolved.values()) if v.isdigit() and v.strip("0")]
    found = sorted({p for p in normalize_pmids(usable) if p in exists}, key=int)
    batch = progress.record_batch(ws, "resolve", "Resolved identifiers", found, total=len(found),
                                  private=args.restricted)["batch"] if found else None
    if args.restricted:
        return progress.attach_restricted(body, ws, "resolve", processed=len(args.ids))
    message = {**body, "given": len(args.ids)}
    if batch:
        message["batch"] = batch
    return progress.attach(body, ws, "resolve", message)


def cmd_mesh(args) -> dict:
    ws = workspace(args)
    if args.mesh_command == "lookup":
        body = {"ok": True, **mesh.lookup(ws.pubmed, " ".join(args.term), limit=args.limit)}
        name, data = "mesh-lookup", {"query": body["query"], "matches": body["matches"]}
    else:
        body = {"ok": True, **mesh.show(ws.pubmed, " ".join(args.identifier), counts=not args.no_counts)}
        name, data = "mesh-show", {"record": body, "no_counts": args.no_counts}
    # MeSH commands have a message only in verbose mode, and are never restricted.
    mode, notice = progress.read_mode(ws)
    if notice:
        body["progress_notice"] = notice
    if mode == "verbose":
        progress.attach(body, ws, name, data, verbose=True)
    return body


def cmd_set(args) -> dict:
    ws = workspace(args)
    if args.set_command == "list":
        return {"ok": True, "purposes": PURPOSES,
                "sets": {n: {"purpose": purpose_label(d), "size": len(d.get("pmids", [])), "source": d.get("source")}
                         for n, d in ws.sets().items()}}
    if args.set_command == "add":
        purpose = LEGACY_ROLES.get(args.purpose or args.role, args.purpose or args.role)
        if not purpose:
            raise UsageError("give --purpose development or --purpose comparison")
        previous = ws.get_set(args.name) if ws.set_path(args.name).exists() else {}
        existing = previous.get("pmids", [])
        given = [p for p in normalize_pmids(args.pmids) if p not in existing]
        reserved.refuse(ws, given, "adding to a set")
        late = allocation.late_companions(ws, given) if purpose == "development" else []
        given = [p for p in given if p not in late]
        pmids = existing + given
        origin = sorted(set(previous.get("origin") or []) | set(args.origin or []) |
                        ({"user-supplied"} if args.role == "seed" else set()))
        body = {"ok": True, **ws.save_set(args.name, purpose, pmids, source=args.source or previous.get("source", ""),
                                          note=args.note or previous.get("note", ""), origin=origin)}
        if late:
            body["late_companions"] = len(late)
            body["note"] = (f"{len(late)} record(s) report a study reserved for the held-out test: they were kept out "
                            "of development, are never mined, and do not change the test's denominators")
        if purpose == "development" and given:
            # Development records are checked at every evaluation: their retrieval is fed back.
            reserved.record(ws, given, "feedback", "set add")
        return progress.attach(body, ws, "set", {"name": args.name, "purpose": purpose, "origin": origin,
                                                 "before": len(existing), "after": len(pmids), "added": given,
                                                 "late": len(late), "overlap": body["overlap_with_other_purposes"]})
    if args.set_command == "remove":
        data = ws.get_set(args.name)
        drop = set(normalize_pmids(args.pmids))
        body = {"ok": True, **ws.save_set(args.name, purpose_of(data), [p for p in data["pmids"] if p not in drop],
                                          source=data.get("source", ""), note=data.get("note", ""),
                                          origin=data.get("origin") or [])}
        return progress.attach(body, ws, "set", {"name": args.name, "purpose": purpose_of(data), "before": len(data["pmids"]),
                                                 "after": len(body["pmids"]), "removed": [p for p in data["pmids"] if p in drop],
                                                 "overlap": body["overlap_with_other_purposes"]})
    raise UsageError("psb set split is withdrawn: records the builder has seen cannot become an independent test by "
                     "moving them. Screen candidates in the separate context and use psb allocate.")


def cmd_lint(args) -> dict:
    ws = workspace(args)
    strategy = ws.strategy()
    issues = lint(strategy, concepts=ws.protocol().get("concepts") or [])
    body = {"ok": not any(i["severity"] == "error" for i in issues), "issues": issues}
    if not strategy.structural_errors():
        body["lines"] = [{"n": l["n"], "text": l["text"]} for l in numbered_lines(strategy)]
        body["query"] = full_query(strategy)
    return body


def _eval_signature(evaluation: dict) -> tuple:
    return (evaluation.get("count"), evaluation.get("review_sha256"),
            validation.digest(evaluation.get("translation_issues", [])),
            validation.digest(evaluation.get("sets", {})))


def cmd_eval(args) -> dict:
    ws = workspace(args)
    evaluation = evaluate(ws, term_counts=not args.no_term_counts)
    deliver.record_evaluation(ws, evaluation, note=args.note)
    attempt = ws.save_attempt(evaluation)
    output = dict(evaluation, attempt_id=attempt["attempt_id"])
    progress.attach(output, ws, "eval", {"evaluation": evaluation, "note": args.note,
                                         "term_counts": not args.no_term_counts})
    if args.brief:
        output.pop("lines", None)
        output.pop("retrieved_known", None)
    output.pop("known_in_pubmed", None)
    return output


def cmd_terms(args) -> dict:
    ws = workspace(args)
    strategy = ws.strategy()
    if args.terms_command == "rank":
        bad: list[str] = []
        if args.set:
            comparison = {n for n, d in ws.sets().items() if purpose_of(d) == "comparison"}
            bad = [n for n in args.set if n in comparison]
            if bad and not args.include_comparison:
                raise UsageError(f"{', '.join(bad)} is a comparison list; it is not mined unless you pass "
                                 "--include-comparison")
            pmids = reserved.visible(ws, pmid_args(ws, [], args.set))
        else:
            pmids = ws.mining_pmids(include_comparison=args.include_comparison)
            bad = sorted(n for n, d in ws.sets().items() if purpose_of(d) == "comparison") if args.include_comparison else []
        if not pmids:
            raise UsageError("no mining records: add a development set")
        records = list(ws.ensure_records(pmids).values())
        reserved.record(ws, [str(r.get("pmid")) for r in records], "indexing", "terms rank")
        body = {"ok": True, **terms.rank(ws.pubmed, records, strategy, fields=args.fields.split(","),
                                          budget=args.budget, min_df=args.min_df, include_covered=args.include_covered)}
        return progress.attach(body, ws, "terms-rank", {"sets": sorted(set(args.set or [])), "comparison_mined": sorted(set(bad)),
                                                        "records": body["records"], "candidates": body["candidates"],
                                                        "already_covered": body["already_covered"], "scored": len(body["scored"]),
                                                        "budget": args.budget, "ranking": body["scored"]})
    versions = ws.versions()
    if not versions:
        raise UsageError("run psb eval first")
    attempts = ws.attempts()
    evaluation = attempts[-1]["evaluation"] if attempts else versions[-1]["evaluation"]
    missed = reserved.visible(ws, [m["pmid"] for m in evaluation.get("misses", [])
                                   if not args.set or set(m["sets"]) & set(args.set)])
    records = list(ws.ensure_records(missed).values())
    if records:
        reserved.record(ws, [str(r.get("pmid")) for r in records], "indexing", "terms miss")
    body = {"ok": True, "version": versions[-1]["version"], "misses": terms.miss_report(records, evaluation, strategy),
            "note": "Vocabulary from missed records is a candidate: test each term with psb eval. Held-out records "
                    "are never diagnosed here; their misses are offered as a repair after the held-out test."}
    return progress.attach(body, ws, "terms-miss", {"version": body["version"], "report": body["misses"],
                                                    "misses": [m for m in evaluation.get("misses", []) if m["pmid"] in missed]})


def cmd_critic(args) -> dict:
    ws = workspace(args)
    if args.critic_command == "packet":
        rounds = deliver.critic_rounds(ws)
        path = deliver.critic_packet(ws, anyway=args.anyway)
        body = {"ok": True, "packet": str(path),
                "next": "give only this file to a fresh-context reviewer (subagent) and save its JSON as "
                        f"critic/round-N.json; then run psb critic check"}
        return progress.attach(body, ws, "critic-packet", {"rounds_before": rounds, "packet": path.name})
    if args.critic_command == "override":
        body = {"ok": True, **deliver.override_finding(ws, args.finding, args.reason)}
        return progress.attach(body, ws, "critic-override", {"id": args.finding})
    if args.critic_command == "extend":
        body = {"ok": True, **deliver.extend_review(ws, args.reason)}
        return progress.attach(body, ws, "critic-extend", {"reason": args.reason, "after_round": body["after_round"]})
    paths = deliver.round_paths(ws)
    path = Path(args.round) if args.round else (paths[-1] if paths else None)
    if path is None:
        raise UsageError("no critic/round-*.json to check")
    body = {"round_file": str(path), **deliver.check_round(ws, path)}
    data = read_json(path)
    if isinstance(data, dict) and type(data.get("round")) is int:
        return progress.attach(body, ws, "critic-check", {"round": data, "check": dict(body)})
    return progress.attach(body, ws, "critic-invalid", {"file": path.name, "problems": body.get("problems")})


def cmd_report(args) -> dict:
    ws = workspace(args)
    result = deliver.report(ws, diagnostic=args.diagnostic, note=args.note)
    return progress.attach(result, ws, "report", {"result": dict(result), "diagnostic": args.diagnostic})


def cmd_screen(args) -> dict:
    ws = workspace(args)
    entries = progress.record_screening(ws, include=args.include, exclude=args.exclude, uncertain=args.uncertain,
                                        reason=args.reason, file=args.file, context=args.context, group=args.group,
                                        origin=args.origin, evidence=args.evidence, source_ref=args.source_ref)
    # A reserved record screened by the builder has been seen: record it rather than hide it.
    seen = [e["pmid"] for e in entries if e.get("context") != "separate" and e["pmid"] in ws.reserved_pmids()]
    if seen:
        reserved.record(ws, seen, "screened", "screen")
    body = {"ok": True, "recorded": len(entries),
            "decisions": {d: [e["pmid"] for e in entries if e["decision"] == d] for d in progress.DECISIONS},
            "note": ("Screening decisions are a record only. Eligible records enter the allocation pool; psb allocate "
                     "assigns them to development or the held-out test.")}
    if args.restricted:
        # Presentation only: each row keeps the context it was given (builder when none was).
        return progress.attach_restricted(body, ws, "screen", recorded=len(entries),
                                          separate_only=all(e.get("context") == "separate" for e in entries))
    return progress.attach(body, ws, "screen", {"entries": entries})


def cmd_allocate(args) -> dict:
    ws = workspace(args)
    if args.rebind:
        event = allocation.rebind(ws)
        body = {"ok": True, "removed": len(event["removed"]), "allocation": allocation.summary(ws)}
        return progress.attach(body, ws, "allocation", {"rebind": True})
    if args.preview:
        proposal = allocation.propose(ws, seed=args.seed)
        body = {"ok": True, "N": proposal["N"], "U": proposal["U"], "H": proposal["H"], "reason": proposal["reason"],
                "pool": proposal["pool"], "development": proposal["development"], "holdout": proposal["holdout"],
                "studies": proposal["studies"], "unavailable": len(proposal["unavailable"]),
                "on_comparison": len(proposal["on_comparison"]),
                "unscreened_development": progress.builder_visible(ws, proposal["unscreened"]),
                "next": ("relay the message and record the user's choice: psb allocate --keep-holdout or "
                         "--all-development (--proceed-default when they asked you not to wait)") if proposal["H"]
                        else "no holdout is proposed: psb allocate freezes every unit for development"}
        return progress.attach(body, ws, "allocation-preview", {"proposal": proposal})
    choice = ("keep-holdout" if args.keep_holdout else "all-development" if args.all_development
              else "proceed-default" if args.proceed_default else None)
    allocation.freeze(ws, choice=choice, seed=args.seed, reserve=args.reserve)
    body = {"ok": True, "allocation": allocation.summary(ws)}
    return progress.attach(body, ws, "allocation", {"rebind": False})


def cmd_holdout_test(args) -> dict:
    ws = workspace(args)
    receipt = holdout.run(ws)
    evaluation = deliver.latest_evaluation(ws)
    message = holdout.message(ws, receipt, evaluation)
    body = {"ok": receipt.get("status") != "incomplete", "receipt": receipt["number"], "status": receipt["status"],
            "repeat": bool(receipt.get("repeat")), "interpretation": message["text"],
            "next": ("psb report delivers the tested query unchanged" if receipt["status"] != "incomplete"
                     else "the PubMed check did not complete: run psb holdout-test again")}
    return progress.attach(body, ws, "holdout-test", {"text": message["text"], "status": receipt["status"]})


def cmd_holdout_release(args) -> dict:
    ws = workspace(args)
    event = allocation.release(ws, args.reason)
    body = {"ok": True, "released": len(event["members"]), "receipts_kept": event["receipts"],
            "next": "revise the strategy with the released records as development, psb eval, then the repair critic round"}
    return progress.attach(body, ws, "holdout-release", {"event": event})


def cmd_exposure(args) -> dict:
    ws = workspace(args)
    entries = reserved.record(ws, normalize_pmids(args.pmids), args.kind, "declared", note=args.note, declared=True)
    return {"ok": True, "recorded": len(entries),
            "note": "Declared exposure counts as exposure: these records go to development, or qualify the held-out result."}


def cmd_progress(args) -> dict:
    if args.value is not None and args.stage != "mode":
        raise UsageError("only psb progress mode takes a value (verbose or standard)")
    if args.stage == "intake-request":
        return {"ok": True, "stage": args.stage,
                "progress": progress.render(None, "intake-request", {"have_question": args.have_question})}
    ws = workspace(args)
    if args.stage == "list":
        # Public projections: rows written before the disclosure policy are filtered by event name.
        shown, omitted = disclosure.public_messages(progress.messages(ws), frozenset(progress.EVENTS))
        return {"ok": True, "messages": shown, "omitted": omitted,
                **({"note": disclosure.OMITTED_NOTE} if omitted else {})}
    if args.stage == "mode":
        # Presentation only: never search depth, screening or what stays private.
        if args.value is None:
            mode, notice = progress.read_mode(ws)
            return {"ok": True, "mode": mode, **({"progress_notice": notice} if notice else {})}
        progress.write_mode(ws, args.value)
        return {"ok": True, "mode": args.value, "progress": progress.emit(ws, "progress-mode", {"mode": args.value})}
    return {"ok": True, "stage": args.stage, "progress": progress.emit(ws, f"stage:{args.stage}")}


def cmd_log(args) -> dict:
    ws = Workspace(find_root(args.workspace))
    entries = ws.log_entries()
    ncbi = [e for e in entries if e.get("type") == "ncbi"]
    # The counts include every row; the tail shows accounting fields only.
    tail, omitted = disclosure.public_log(entries[-args.tail:], build_parser().vocabulary) if args.tail else ([], 0)
    return {"ok": True, "entries": len(entries), "ncbi_requests": len(ncbi),
            "from_cache": sum(1 for e in ncbi if e.get("cache")), "tail": tail, "tail_omitted": omitted}


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
        p.add_argument("--purpose", choices=sorted(progress.PURPOSES),
                       help="announce this search to the user (prior-reviews and pilot also record a candidate batch)")
        if name == "sample":
            p.add_argument("--n", type=int, default=10)
            p.add_argument("--random", action="store_true", help="sample from a random offset")
            p.add_argument("--seed", type=int, default=1)
            p.add_argument("--screening", action="store_true",
                           help="separate screening context only (needs --purpose prior-reviews or pilot): records go "
                                "to the private store, no exposure")
        else:
            p.add_argument("--screening", action="store_true", help=PRIVATE_HELP)
        p.set_defaults(func=func)

    p = sub.add_parser("fetch", help="fetch and store records")
    p.add_argument("pmids", nargs="*")
    p.add_argument("--set", action="append")
    p.add_argument("--abstracts", action="store_true")
    p.add_argument("--mesh", type=int, default=12, help="MeSH headings shown per record")
    p.add_argument("--screening", action="store_true",
                   help="separate screening context only: records go to the private store, no exposure")
    p.set_defaults(func=cmd_fetch)

    p = sub.add_parser("neighbors", help="similar, citing, or cited records of known PMIDs")
    p.add_argument("pmids", nargs="*")
    p.add_argument("--set", action="append")
    p.add_argument("--links", default="similar")
    p.add_argument("--max-per-seed", type=int, default=50)
    p.add_argument("--limit", type=int, default=100)
    p.add_argument("--exclude-known", action="store_true", help="drop PMIDs already in a set")
    p.add_argument("--screening", action="store_true", help=PRIVATE_HELP)
    p.set_defaults(func=cmd_neighbors)

    p = sub.add_parser("resolve", help="PMIDs from PMIDs, DOIs, or PMCIDs")
    p.add_argument("ids", nargs="+")
    p.add_argument("--screening", action="store_true", help=PRIVATE_HELP)
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

    p = sub.add_parser("set", help="PMID sets with a purpose (development or comparison)")
    ssub = p.add_subparsers(dest="set_command", required=True)
    ssub.add_parser("list")
    q = ssub.add_parser("add")
    q.add_argument("name")
    q.add_argument("pmids", nargs="+")
    group = q.add_mutually_exclusive_group(required=True)
    group.add_argument("--purpose", choices=sorted(PURPOSES))
    group.add_argument("--role", choices=sorted(LEGACY_ROLES), help="legacy name, mapped to a purpose")
    q.add_argument("--origin", action="append", choices=ORIGINS)
    q.add_argument("--source", default="")
    q.add_argument("--note", default="")
    q = ssub.add_parser("remove")
    q.add_argument("name")
    q.add_argument("pmids", nargs="+")
    q = ssub.add_parser("split", help="withdrawn: use psb allocate")
    q.add_argument("name", nargs="?")
    q.add_argument("--into")
    q.add_argument("--fraction", type=float)
    q.add_argument("--seed", type=int)
    p.set_defaults(func=cmd_set)

    p = sub.add_parser("screen", help="record screening decisions on candidate records")
    p.add_argument("--include", nargs="+", default=[])
    p.add_argument("--exclude", nargs="+", default=[])
    p.add_argument("--uncertain", nargs="+", default=[])
    p.add_argument("--reason", default="", help="reason recorded with every decision in this call")
    p.add_argument("--file", help="JSON list of {pmid, decision, reason, context, group, origin, evidence, source_ref}")
    p.add_argument("--context", choices=progress.CONTEXTS,
                   help="separate: screened only in the separate screening context (reasons kept private)")
    p.add_argument("--group", help="study key shared by reports of one study (e.g. a registration ID)")
    p.add_argument("--origin", action="append", choices=ORIGINS)
    p.add_argument("--evidence", choices=progress.EVIDENCE, help="what the decision was based on")
    p.add_argument("--source-ref", help="where inclusion was verified, e.g. Table 2 of PMID 123")
    p.set_defaults(func=cmd_screen)

    p = sub.add_parser("exposure", help="declare records the builder has seen")
    esub = p.add_subparsers(dest="exposure_command", required=True)
    q = esub.add_parser("declare")
    q.add_argument("pmids", nargs="+")
    q.add_argument("--kind", required=True, choices=reserved.KINDS)
    q.add_argument("--note", default="")
    p.set_defaults(func=cmd_exposure)

    p = sub.add_parser("allocate", help="freeze the split of eligible records into development and held-out units")
    choice = p.add_mutually_exclusive_group()
    choice.add_argument("--preview", action="store_true", help="counts only, and the choice message when a holdout is proposed")
    choice.add_argument("--keep-holdout", action="store_true")
    choice.add_argument("--all-development", action="store_true")
    choice.add_argument("--proceed-default", action="store_true", help="keep the proposed holdout: the user asked not to be asked")
    choice.add_argument("--reserve", nargs="+", help="the user's designated test records (replaces the automatic holdout)")
    choice.add_argument("--rebind", action="store_true", help="after an eligibility or as_of change and re-screening")
    p.add_argument("--seed", type=int, default=1)
    p.set_defaults(func=cmd_allocate)

    sub.add_parser("holdout-test", help="one retrieval test of the frozen query on the held-out records").set_defaults(
        func=cmd_holdout_test)
    p = sub.add_parser("holdout-release", help="return the held-out records to development to repair the search")
    p.add_argument("--reason", required=True)
    p.set_defaults(func=cmd_holdout_release)

    p = sub.add_parser("progress", help="the standard progress message for a workflow step, the message list, "
                                        "or the progress mode")
    stages = ["intake-request", *progress.STAGES, "list", "mode"]
    p.add_argument("stage", choices=stages)
    p.add_argument("value", nargs="?", choices=progress.MODES, help="with mode: verbose or standard")
    p.add_argument("--have-question", action="store_true", help="intake-request: the question is already known")
    p.set_defaults(func=cmd_progress)

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
    q.add_argument("--include-comparison", action="store_true", help="also mine comparison lists")
    q = tsub.add_parser("miss", help="diagnose missed known records from the last eval")
    q.add_argument("--set", action="append")
    p.set_defaults(func=cmd_terms)

    p = sub.add_parser("critic", help="PRESS critic packet and round check")
    csub = p.add_subparsers(dest="critic_command", required=True)
    q = csub.add_parser("packet", help="write critic/packet-N.md from the latest evaluated version")
    q.add_argument("--anyway", action="store_true",
                   help="issue the last revision, closing or verification round although technical blockers remain")
    q = csub.add_parser("check", help="validate a critic/round-N.json")
    q.add_argument("round", nargs="?")
    q = csub.add_parser("override", help="after the closing round, deliver over an open must-fix judgment you disagree with")
    q.add_argument("finding")
    q.add_argument("--reason", required=True, help="why the finding is wrong for this search, with the evidence")
    q = csub.add_parser("extend", help="only when the user asks: one more review period after the verification round, "
                                       "once per build")
    q.add_argument("--reason", required=True, help="why the user granted it (what made the review stale)")
    p.set_defaults(func=cmd_critic)

    p = sub.add_parser("report", help="render audit.md from the workspace")
    p.add_argument("--fresh", action="store_true", help="compatible alias: reporting always validates live")
    p.add_argument("--diagnostic", action="store_true", help="write unfinished diagnostic output only; no final query")
    p.add_argument("--note", default="")
    p.set_defaults(func=cmd_report)

    p = sub.add_parser("log", help="summarise the workspace log")
    p.add_argument("--tail", type=int, default=0)
    p.set_defaults(func=cmd_log)

    sub.add_parser("doctor", help="check NCBI configuration with one live query").set_defaults(func=cmd_doctor)
    p = sub.add_parser("cache", help="inspect or clear the workspace cache")
    p.add_argument("--clear", action="store_true")
    p.set_defaults(func=cmd_cache)
    # The words a public log row may show: each command and its subcommands or progress stages.
    parser.vocabulary = {name: frozenset() for name in sub.choices}
    parser.vocabulary.update(mesh=frozenset(msub.choices), set=frozenset(ssub.choices), terms=frozenset(tsub.choices),
                             critic=frozenset(csub.choices), exposure=frozenset(esub.choices),
                             progress=frozenset(stages))
    return parser


PRIVATE_HELP = ("separate screening context only: private request log and cache; the progress message keeps the "
                "details private")
HANDLED = (WorkspaceError, StrategyError, UsageError, NcbiError, ValueError, OSError)


def restricted_failure(args, exc: Exception) -> dict:
    """The fixed message for a failed restricted invocation, also written to progress.jsonl. The raw error
    goes to screening/log.jsonl; stdout keeps it for the separate context that ran the command."""
    facts = {"operation": disclosure.operation(args)}
    try:
        ws = Workspace(find_root(args.workspace), use_cache=False, restricted=True)
    except Exception:  # noqa: BLE001 - without a workspace the message is returned, not stored
        return progress.render(None, "separate:failed", facts)
    try:
        ws.log({"type": "error", "command": command_words(args), "error": str(exc), "error_type": type(exc).__name__})
    except Exception:  # noqa: BLE001 - a failed private write never brings the error back
        pass
    try:
        return progress.emit(ws, "separate:failed", facts)
    except Exception:  # noqa: BLE001
        return progress.render(None, "separate:failed", facts)


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    # Progress text is relayed to the user verbatim: print real characters, not \u escapes.
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except (ValueError, OSError):
            pass
    parser = build_parser()
    args = parser.parse_args(argv)
    args.argv = argv
    # Before any workspace is opened, anything is logged or any request is made; this call only.
    args.restricted = disclosure.restricted(args)
    if args.env_file:
        config.use_env_file(args.env_file)
    try:
        result = args.func(args)
    except Exception as exc:  # noqa: BLE001 - every failure of a restricted invocation gets the fixed message
        if not args.restricted and not isinstance(exc, HANDLED):
            raise
        failure = {"ok": False, "error": str(exc), "error_type": type(exc).__name__}
        if args.restricted:
            failure["progress"] = restricted_failure(args, exc)
        emit(failure)
        return 1
    emit(result)
    return 0 if result.get("ok", True) else 1
