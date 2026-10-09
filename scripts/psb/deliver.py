"""Evidence-bound critic review and fail-closed publication at the library boundary."""
from __future__ import annotations

import json
import os
import re
import time
from contextlib import contextmanager
from pathlib import Path

from . import allocation, holdout, validation
from .evaluate import evaluate, compare
from .strategy import Strategy
from .workspace import Workspace, WorkspaceError, now, purpose_label, read_json, write_json, sha256_text

DOMAINS = ["translation", "operators", "subject_headings", "text_words", "syntax", "limits_filters"]
SEVERITIES = {"must-fix", "should-fix", "document"}
KINDS = {"lexical", "structural", "scope", "filter", "syntax", "reporting"}
STATUSES = {"open", "resolved", "rejected", "accepted-risk"}
ARTIFACTS = ("validation-manifest.json", "final-query.txt", "audit.md")
# After the closing round, a must-fix finding of these kinds is a judgment the agent may disagree
# with: the query is delivered with the objection on the audit's first page for the human peer
# reviewer. Syntax and filter findings, and technical blockers, are never overridable.
OVERRIDABLE_KINDS = {"lexical", "structural", "scope", "reporting"}


def record_evaluation(ws: Workspace, evaluation: dict, *, note: str = "") -> None:
    versions = ws.versions()
    previous = versions[-1] if versions else None
    attempts = ws.attempts()
    last_eval = next((a["evaluation"] for a in reversed(attempts) if a.get("evaluation", {}).get("count") is not None), None)
    comparison = ({"evaluation": last_eval, "strategy": last_eval["inputs"]["strategy"],
                   "version": last_eval.get("version")} if last_eval and last_eval.get("inputs") else previous)
    diff = compare(comparison, evaluation, evaluation["inputs"]["strategy"])
    if diff:
        evaluation["since_previous"] = diff
    strategy_hash = sha256_text(json.dumps(evaluation["inputs"]["strategy"], sort_keys=True))
    if previous is None or previous["strategy_sha256"] != strategy_hash:
        saved = ws.save_version(evaluation, note)
        evaluation["version"] = saved["version"]
    else:
        evaluation["version"] = previous["version"]
        evaluation["saved"] = "identical strategy; evaluation recorded as a separate attempt"


def round_paths(ws: Workspace) -> list[Path]:
    def number(path):
        match = re.fullmatch(r"round-(\d+)\.json", path.name)
        if not match:
            raise WorkspaceError(f"invalid critic filename: {path.name}")
        return int(match[1])
    return sorted((ws.root / "critic").glob("round-*.json"), key=number)


def critic_rounds(ws: Workspace) -> list[dict]:
    rounds = []
    seen = set()
    for path in round_paths(ws):
        data = read_json(path)
        expected = int(path.stem.split("-")[1])
        if not isinstance(data, dict) or type(data.get("round")) is not int or data["round"] != expected or expected in seen:
            raise WorkspaceError(f"invalid or duplicate critic round: {path.name}")
        seen.add(expected)
        rounds.append(data)
    return rounds


def round_findings(data: dict) -> list[dict]:
    """A round's well-formed findings. A malformed ``findings`` value is reported by
    ``_round_problems``; every other reader treats it as empty instead of crashing."""
    findings = data.get("findings")
    return [f for f in findings if isinstance(f, dict)] if isinstance(findings, list) else []


def critic_overrides(ws: Workspace) -> list[dict]:
    path = ws.root / "critic" / "overrides.json"
    if not path.exists():
        return []
    data = read_json(path)
    if not isinstance(data, list) or any(not isinstance(o, dict) for o in data):
        raise WorkspaceError("critic/overrides.json must be a list of objects")
    return data


def critic_extensions(ws: Workspace) -> list[dict]:
    """The review extension the user granted after the verification round (at most one per build)."""
    path = ws.root / "critic" / "extensions.json"
    if not path.exists():
        return []
    data = read_json(path)
    if not isinstance(data, list) or any(not isinstance(e, dict) for e in data):
        raise WorkspaceError("critic/extensions.json must be a list of objects")
    return data


def critic_digest(rounds: list[dict], overrides: list[dict], extensions: list[dict] | None = None) -> str:
    """The critic evidence a delivery rests on: rounds alone when nothing was overridden or extended, so
    earlier deliveries keep their digest."""
    if extensions:
        return validation.digest({"rounds": rounds, "overrides": overrides, "extensions": extensions})
    return validation.digest(rounds) if not overrides else validation.digest({"rounds": rounds, "overrides": overrides})


def critic_evidence(ws: Workspace) -> str:
    return critic_digest(critic_rounds(ws), critic_overrides(ws), critic_extensions(ws))


def _override_problems(finding: dict | None, closed_out: bool) -> list[str]:
    if not closed_out:
        return ["overrides apply only after the closing round"]
    if finding is None:
        return ["no such finding"]
    if finding.get("status") != "open" or finding.get("severity") != "must-fix":
        return ["only an open must-fix finding can be overridden"]
    if finding.get("kind") not in OVERRIDABLE_KINDS:
        return [f"a {finding.get('kind')!r} finding cannot be overridden (only {', '.join(sorted(OVERRIDABLE_KINDS))})"]
    return []


def override_finding(ws: Workspace, finding_id: str, reason: str) -> dict:
    """Record disagreement with an open must-fix judgment after the closing round."""
    if not _nonempty(reason):
        raise WorkspaceError("give the reason you disagree, with the evidence for it")
    rounds = critic_rounds(ws)
    if not rounds:
        raise WorkspaceError("no critic round to override")
    active = {f.get("id"): f for r in rounds for f in round_findings(r)}
    problems = _override_problems(active.get(finding_id), bool(rounds[-1].get("closing")))
    if problems:
        raise WorkspaceError(f"{finding_id}: {problems[0]}")
    overrides = [o for o in critic_overrides(ws) if o.get("id") != finding_id]
    overrides.append({"id": finding_id, "round": rounds[-1]["round"], "response": reason.strip(), "created": now()})
    write_json(ws.root / "critic" / "overrides.json", overrides)
    return {"overridden": finding_id, "next": "run psb report; the audit will open with this objection and your reason"}


def latest_evaluation(ws: Workspace) -> dict:
    attempts = ws.attempts()
    if not attempts:
        raise WorkspaceError("run psb eval: legacy evaluations need fresh validation")
    evaluation = attempts[-1]["evaluation"]
    if evaluation.get("input_sha256") != validation.digest(validation.input_snapshot(ws)):
        raise WorkspaceError("workspace changed since the last psb eval; run psb eval first")
    return evaluation


def _line_table(evaluation: dict) -> list[str]:
    rows = ["| # | Search | Results | Diagnostics |", "|---:|---|---:|---|"]
    for line in evaluation.get("lines", []):
        text = line["text"].replace("|", "\\|")
        issues = "; ".join(f"{i['severity']}: {i['code']}" for i in line.get("issues", [])) or "none"
        rows.append(f"| {line['n']} | `{text}` | {line['count']:,} | {issues} |")
    return rows


def _scope_section(evaluation: dict) -> list[str]:
    protocol = (evaluation.get("inputs") or {}).get("protocol") or {}
    eligibility = protocol.get("eligibility") or {}
    rows = ["## Scope", "", f"Question: {protocol.get('question') or '(none)'}", "",
            "| Concept | Role | Rationale |", "|---|---|---|"]
    for concept in protocol.get("concepts") or []:
        rows.append(f"| {concept.get('name') or concept.get('id')} | {concept.get('role')} | "
                    f"{str(concept.get('rationale') or '').replace('|', '/')} |")
    for label in ("include", "exclude"):
        items = eligibility.get(label) if isinstance(eligibility, dict) else None
        if items:
            rows += ["", f"Eligibility ({label}):", *[f"- {item}" for item in items]]
    rows += ["", "Translation checks: (1) every member that the question or eligibility names for a searched "
             "concept is covered by its own bare name, not only by a phrase narrowed with the parent's wording "
             "(`mediation`, not only `\"mediation model*\"`); (2) a searched block that names one direction or step "
             "of a process, or an event in some participants (switching back, discontinuation), is fragile: "
             "recommend searching the process in either direction and screening the direction.", ""]
    return rows


def _recall_table(evaluation: dict) -> list[str]:
    """Development and comparison retrieval. Legacy evaluations carry a role, labelled as legacy."""
    rows = ["| Set | Purpose | In PubMed | Retrieved | Retrieved % |", "|---|---|---:|---:|---:|"]
    for name, data in (evaluation.get("sets") or {}).items():
        recall = "n/a" if data["recall_percent"] is None else f"{data['recall_percent']}%"
        rows.append(f"| {name} | {data.get('label') or purpose_label(data)} | {data['in_pubmed']} | {data['retrieved']} | {recall} |")
    return rows


def _nonempty(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _round_problems(data: dict) -> list[str]:
    problems = []
    if not round_epoch(data):
        problems.append("epoch must be a positive integer")
    domains = data.get("domains")
    if not isinstance(domains, dict):
        return problems + ["domains must be an object"]
    for domain in DOMAINS:
        row = domains.get(domain)
        if not isinstance(row, dict) or not isinstance(row.get("verdict"), str) or row.get("verdict") not in {"pass", "revise"}:
            problems.append(f"domain {domain!r} needs a verdict of pass or revise")
    findings = data.get("findings")
    if not isinstance(findings, list):
        return problems + ["findings must be a list"]
    ids = set()
    for f in findings:
        if not isinstance(f, dict):
            problems.append("finding must be an object")
            continue
        fid = f.get("id")
        if not _nonempty(fid) or fid in ids:
            problems.append("finding id missing or duplicated")
        else:
            ids.add(fid)
        if any(not isinstance(f.get(k), str) or f.get(k) not in allowed for k, allowed in (("domain", DOMAINS), ("severity", SEVERITIES), ("kind", KINDS), ("status", STATUSES))):
            problems.append(f"{fid}: invalid domain, severity, kind or status")
        if not _nonempty(f.get("finding")):
            problems.append(f"{fid}: finding explanation required")
        if f.get("status") != "open" and not _nonempty(f.get("response")):
            problems.append(f"{fid}: disposition needs a response explaining why")
    return problems


def revision_budget(depth: str | None) -> int:
    """Revision rounds per depth. One closing round may follow them (see ``review_gate``)."""
    return {"quick": 1, "standard": 2, "thorough": 3}.get(depth or "standard", 2)


# The closing round, plus one verification round when the strategy or scope changed after it.
MAX_CLOSING_ROUNDS = 2
# A repair after the held-out test is targeted and the strategy was already reviewed: each repair epoch
# allows one revision round, then the closing and verification rounds, at every depth. A review
# extension the user grants has the same budget.
REPAIR_BUDGET = 1


class ReviewExhausted(WorkspaceError):
    """The verification round of the current review period is used, and the review is not current."""


def current_epoch(ws: Workspace) -> int:
    """1, plus one for each release of held-out records for repair and for a review extension the user
    granted. Rounds count per epoch."""
    return (1 + sum(1 for e in ws.allocation_events() if e.get("type") == "release")
            + len(critic_extensions(ws)))


def epoch_kind(ws: Workspace, epoch: int) -> str:
    """``initial``, ``extension`` (opened by psb critic extend) or ``repair`` (opened by a release)."""
    if epoch == 1:
        return "initial"
    return "extension" if any(e.get("epoch") == epoch for e in critic_extensions(ws)) else "repair"


def round_epoch(data: dict) -> int:
    epoch = data.get("epoch", 1)
    return epoch if type(epoch) is int and epoch >= 1 else 0


def epoch_budget(ws: Workspace, epoch: int | None = None) -> int:
    epoch = current_epoch(ws) if epoch is None else epoch
    return revision_budget(ws.protocol().get("depth")) if epoch == 1 else REPAIR_BUDGET


def _closing_problems(rounds: list[dict]) -> list[tuple[int, str]]:
    """A closing round verifies how earlier findings were handled; it cannot open a new front.

    Without it, a last revision round that asks for changes is a dead end: fixing the strategy
    makes the critic stale with no round left, and leaving the findings open blocks delivery.
    The same dead end recurs if anything the critic reviewed changes after the closing round, so
    one more closing round (a verification round) may follow it; nothing may follow that within the
    epoch. A release for repair starts a new epoch, whose rounds count afresh.
    """
    problems = []
    earlier: set[str] = set()
    closings = 0
    epoch = 1
    for r in rounds:
        findings = round_findings(r)
        if round_epoch(r) < epoch:
            problems.append((r.get("round"), "a round cannot return to an earlier epoch"))
        elif round_epoch(r) > epoch:
            epoch, closings = round_epoch(r), 0
        if not r.get("closing") and closings:
            problems.append((r.get("round"), "a revision round cannot follow a closing round"))
        if r.get("closing"):
            closings += 1
            if closings > MAX_CLOSING_ROUNDS:
                problems.append((r.get("round"), f"at most {MAX_CLOSING_ROUNDS} closing rounds (one verification "
                                 "round after a late change)"))
            for f in findings:
                if f.get("id") not in earlier and f.get("severity") != "document":
                    problems.append((r.get("round"), f"{f.get('id')}: a closing round may only verify earlier findings; "
                                     "a new concern must be severity 'document'"))
        earlier.update(str(f.get("id")) for f in findings)
    return problems


def review_gate(ws: Workspace, evaluation: dict, *, rounds: list[dict] | None = None,
                overrides: list[dict] | None = None) -> dict:
    blockers = []
    rounds = critic_rounds(ws) if rounds is None else rounds
    overrides = critic_overrides(ws) if overrides is None else overrides
    if not rounds:
        return {"blockers": [validation.issue("critic_missing", "A current internal critic is required at every depth")], "findings": []}
    latest = rounds[-1]
    active = {}
    for r in rounds:
        problems = _round_problems(r)
        if problems:
            blockers.append(validation.issue("critic_invalid", "Invalid critic round", location=f"critic:{r.get('round')}", evidence=problems))
            continue
        for f in r["findings"]:
            active[f["id"]] = f
    for number, problem in _closing_problems(rounds):
        blockers.append(validation.issue("critic_invalid", "Invalid closing round", location=f"critic:{number}", evidence=[problem]))
    epoch = current_epoch(ws)
    if any(round_epoch(r) > epoch for r in rounds):
        blockers.append(validation.issue("critic_invalid", "A critic round names a repair epoch that has not started"))
    if blockers:
        return {"blockers": blockers, "findings": list(active.values())}
    if latest.get("review_sha256") != evaluation.get("review_sha256"):
        blockers.append(validation.issue("critic_stale", "Critic must review the current inputs, translation and known-record retrieval"))
    budget = revision_budget(evaluation["inputs"]["protocol"].get("depth")) if epoch == 1 else REPAIR_BUDGET
    if sum(bool(r.get("review_sha256")) and not r.get("closing") for r in rounds if round_epoch(r) == epoch) > budget:
        blockers.append(validation.issue("critic_budget", "Critic revision budget exhausted; use the closing round or deliver a diagnostic handoff"))
    # After the closing round no review is left to act on a should-fix finding, so it is delivered
    # as a documented open concern; only a must-fix finding still stops the query.
    closed_out = bool(latest.get("closing"))
    overridden = {}
    # An override answers one round; after a verification round it must be made again.
    for o in [o for o in overrides or [] if o.get("round") == latest.get("round")]:
        problems = _override_problems(active.get(o.get("id")), closed_out)
        if not _nonempty(o.get("response")):
            problems.append("an override needs a response")
        if problems:
            blockers.append(validation.issue("override_invalid", "Invalid critic override", location=f"critic:{o.get('id')}", evidence=problems))
        else:
            overridden[o["id"]] = {**active[o["id"]], "override": o["response"]}
    blocking_severities = {"must-fix"} if closed_out else {"must-fix", "should-fix"}
    for fid, f in active.items():
        if f["status"] == "open" and f["severity"] in blocking_severities and fid not in overridden:
            blockers.append(validation.issue("critic_open", "Finding needs a disposition", location=f"critic:{fid}", evidence=f))
    # An omitted finding must be explicitly carried forward, even if its old status was open.
    current_ids = {f.get("id") for f in latest.get("findings", []) if isinstance(f, dict)} if isinstance(latest.get("findings"), list) else set()
    for fid, f in active.items():
        if f["status"] == "open" and fid not in current_ids:
            blockers.append(validation.issue("critic_dropped", "Earlier open finding was omitted", location=f"critic:{fid}"))
    dispositions = latest.get("issue_dispositions", [])
    if not isinstance(dispositions, list) or any(not isinstance(d, dict) for d in dispositions):
        dispositions = []
        blockers.append(validation.issue("critic_invalid", "issue_dispositions must be a list of objects"))
    by_id = {}
    for d in dispositions:
        iid = d.get("issue_id")
        if not isinstance(iid, str) or iid in by_id:
            blockers.append(validation.issue("critic_invalid", "Missing or duplicate issue disposition ID"))
        else:
            by_id[iid] = d
    for item in evaluation["validation"]["review_required"]:
        d = by_id.get(item["id"], {})
        valid = isinstance(d.get("status"), str) and d.get("status") in {"accepted-risk", "rejected"} and _nonempty(d.get("response")) and _nonempty(d.get("evidence"))
        if item["code"] in validation.PHRASE_CODES:
            valid = valid and d.get("query") == item.get("query") and d.get("translation") == item.get("translation")
        if not valid:
            blockers.append(validation.issue("review_unresolved", "Mandatory issue review is incomplete", location=item["location"], issue_id=item["id"], evidence=item))
    for domain, row in (latest.get("domains") or {}).items():
        if isinstance(row, dict) and row.get("verdict") == "revise":
            explained = any(f.get("domain") == domain and f.get("status") in {"accepted-risk", "rejected", "resolved"} and _nonempty(f.get("response")) for f in active.values())
            if closed_out:  # at closing, a domain blocks only through an open must-fix finding in it
                explained = not any(f.get("domain") == domain and f["status"] == "open" and f["severity"] == "must-fix"
                                    and fid not in overridden for fid, f in active.items())
            if not explained:
                blockers.append(validation.issue("critic_revise", "Domain still requires revision", location=f"critic:{domain}"))
    return {"blockers": blockers, "findings": list(active.values()), "issue_dispositions": dispositions,
            "overridden": list(overridden.values())}


def check_round(ws: Workspace, path: Path) -> dict:
    data = read_json(path)
    if not isinstance(data, dict) or type(data.get("round")) is not int or data["round"] < 1:
        return {"ok": False, "problems": ["round must be an object with a positive integer round number"], "open_must_fix": []}
    evaluation = latest_evaluation(ws)
    rounds = [r for r in critic_rounds(ws) if r["round"] < data["round"]] + [data]
    result = review_gate(ws, evaluation, rounds=rounds)
    overridden = {f["id"] for f in result.get("overridden", [])}
    open_must_fix = [f for f in result["findings"] if f["status"] == "open" and f["severity"] == "must-fix" and f["id"] not in overridden]
    body = {"ok": not result["blockers"], "problems": [b["message"] for b in result["blockers"]],
            "blockers": result["blockers"], "open_must_fix": [f["id"] for f in open_must_fix]}
    overridable = [f["id"] for f in open_must_fix if data.get("closing") and f.get("kind") in OVERRIDABLE_KINDS]
    if overridable:
        body["overridable"] = overridable
        body["next"] = ("If you can fix a finding, fix it, psb eval, and take the verification round. If you disagree with "
                        "it on evidence, psb critic override <id> --reason \"...\"; the audit opens with the objection.")
    return body


def next_round(ws: Workspace, evaluation: dict, rounds: list[dict]) -> tuple[int, str]:
    """The number and kind (``revision``, ``closing`` or ``verification``) of the next critic round."""
    number = max((r["round"] for r in rounds), default=0) + 1
    epoch = current_epoch(ws)
    budget = epoch_budget(ws, epoch)
    rounds = [r for r in rounds if round_epoch(r) == epoch]
    closings = [r for r in rounds if r.get("closing")]
    if closings:
        if closings[-1].get("review_sha256") == evaluation["review_sha256"]:
            raise WorkspaceError("the closing round reviewed the current strategy; run psb report")
        if len(closings) >= MAX_CLOSING_ROUNDS:
            raise ReviewExhausted(
                "the verification round has been used; use report --diagnostic for the handoff"
                + ("; the review was already extended once for this build" if critic_extensions(ws) else
                   ", or explain why the build is stuck and ask the user whether to extend the review (psb critic extend)"))
        return number, "verification"
    return number, "closing" if sum(bool(r.get("review_sha256")) for r in rounds) >= budget else "revision"


def extend_review(ws: Workspace, reason: str) -> dict:
    """One more review period, granted by the user, after the verification round is used and the review
    is stale (for example, PubMed's translation or indexing drifted before psb report). It touches no
    held-out record; a later release for repair opens its own epoch."""
    if not _nonempty(reason):
        raise WorkspaceError("give the reason the user granted the extension")
    if critic_extensions(ws):
        raise WorkspaceError("the review budget was already extended once for this build; use psb report --diagnostic "
                             "for the handoff")
    evaluation = latest_evaluation(ws)
    rounds = critic_rounds(ws)
    try:
        number, kind = next_round(ws, evaluation, rounds)
    except ReviewExhausted:
        pass
    except WorkspaceError as exc:
        raise WorkspaceError(f"no extension is needed: {exc}") from None
    else:
        raise WorkspaceError(f"no extension is needed: round {number} ({kind}) is still available; run psb critic packet")
    entry = {"reason": reason.strip(), "after_round": rounds[-1]["round"], "epoch": current_epoch(ws) + 1, "created": now()}
    write_json(ws.root / "critic" / "extensions.json", [entry])
    return {"extended": True, "epoch": entry["epoch"], "after_round": entry["after_round"],
            "next": "run psb critic packet for the extension's revision round; the audit discloses the extension"}


def rounds_left(ws: Workspace) -> str:
    """The critic rounds left in the current review period, for psb status."""
    epoch = current_epoch(ws)
    budget = epoch_budget(ws, epoch)
    rounds = [r for r in critic_rounds(ws) if round_epoch(r) == epoch]
    used = sum(bool(r.get("review_sha256")) and not r.get("closing") for r in rounds)
    closings = sum(bool(r.get("closing")) for r in rounds)
    period = {"extension": "extension: ", "repair": "repair: "}.get(epoch_kind(ws, epoch), "")
    if closings >= MAX_CLOSING_ROUNDS:
        return period + ("none left — psb report if the last round reviewed the current evaluation; otherwise "
                         + ("report --diagnostic or a critic override (the review was already extended)"
                            if critic_extensions(ws) else
                            "report --diagnostic, a critic override, or a review extension the user grants"))
    if closings:
        left = "closing used · verification left"
    elif used >= budget:
        left = "closing and verification left"
    else:
        left = f"{budget - used} revision{'s' if budget - used != 1 else ''}, closing and verification left"
    return f"{period}revision {min(used, budget)}/{budget} used · {left}"


def _holdout_note(ws: Workspace) -> list[str]:
    """What the critic is told about held-out records: their count, never their identity or retrieval."""
    current = allocation.state(ws)
    if current is None or not current["held"]:
        return []
    if current["released"]:
        return ["**Repair review.** The held-out records were released into development to repair the search after "
                "the held-out test. They are now development records; review the revised strategy as usual.", ""]
    units = len(current["held"])
    return [f"**Held-out test.** {units} unit{'s are' if units != 1 else ' is'} reserved for one retrieval test that "
            "runs after this review. They are not in this packet and must not be requested or inferred.", ""]


def _last_rounds(ws: Workspace, rounds: list[dict], kind: str) -> bool:
    """Whether the next round is the last revision round, the closing round or the verification round."""
    if kind != "revision":
        return True
    epoch = current_epoch(ws)
    used = sum(bool(r.get("review_sha256")) and not r.get("closing") for r in rounds if round_epoch(r) == epoch)
    return used + 1 >= epoch_budget(ws, epoch)


def critic_packet(ws: Workspace, *, anyway: bool = False) -> Path:
    evaluation = latest_evaluation(ws)
    if not evaluation["validation"]["complete"]:
        raise WorkspaceError("run a complete psb eval before requesting critique")
    rounds = critic_rounds(ws)
    number, kind = next_round(ws, evaluation, rounds)
    # Technical blockers stop psb report whatever the critic says (review_gate never clears them; mandatory
    # issue reviews are answered in issue_dispositions and do not count here). Spending one of the last
    # rounds on a draft that cannot be delivered wastes it.
    blockers = sorted({str(b.get("code")) for b in evaluation["validation"]["blockers"]})
    if blockers and not anyway and _last_rounds(ws, rounds, kind):
        label = "last revision" if kind == "revision" else kind
        raise WorkspaceError(f"the latest evaluation has technical blockers no critic round can clear "
                             f"({', '.join(blockers)}): fix them and psb eval before using the {label} round, or pass "
                             "--anyway to use it now")
    epoch = current_epoch(ws)
    budget = epoch_budget(ws, epoch)
    verification = kind == "verification"
    closing = kind != "revision"
    template = {"round": number, **({"epoch": epoch} if epoch > 1 else {}), **({"closing": True} if closing else {}),
                "strategy_version": evaluation.get("version"), "review_sha256": evaluation["review_sha256"],
                "domains": {d: {"verdict": "pass | revise", "note": "explanation"} for d in DOMAINS}, "findings": [],
                "issue_dispositions": [{"issue_id": i["id"], "status": "accepted-risk | rejected", "response": "reason", "evidence": "observations", **({"query": i.get("query"), "translation": i.get("translation")} if i["code"] in validation.PHRASE_CODES else {})} for i in evaluation["validation"]["review_required"]]}
    closing_note = ([f"**Closing round.** The {budget} revision round(s) are used. Verify how each earlier finding was "
                     "handled in the current strategy: mark it resolved, rejected or accepted-risk with a response, or keep "
                     "it open and the domain at revise if it was not handled. Do not raise new must-fix or should-fix "
                     "findings; record any new concern as severity 'document'. Keep \"closing\": true in the response.", ""]
                    if closing else [])
    if verification:
        closing_note = ["**Verification round.** The draft changed after the closing round. This is the last review: "
                        "check that the change keeps every earlier finding's disposition true, and update a finding only "
                        "where the change affects it. Do not raise new must-fix or should-fix findings; record any new "
                        "concern as severity 'document'. Keep \"closing\": true in the response.", ""]
    title = " (verification)" if verification else " (closing)" if closing else ""
    extension = next((e for e in critic_extensions(ws) if e.get("epoch") == epoch), None)
    extension_note = ([f"**Review extension.** The user extended the review budget after round {extension.get('after_round')}: "
                       f"{str(extension.get('reason') or '').strip()}. This review period allows one revision round, then a "
                       "closing round and a verification round. Review the current draft as usual.", ""]
                      if extension else [])
    lines = [f"# Critic packet, round {number}{title}", "", *extension_note, *closing_note, *_holdout_note(ws),
             "Review this draft as an information specialist using the six PRESS domains. "
             "Use only the packet. Do not answer the evidence question. Technical errors cannot be waived. "
             "Carry earlier finding IDs forward with explicit dispositions. For each finding provide id, domain, severity "
             "(must-fix/should-fix/document), kind (lexical/structural/scope/filter/syntax/reporting), finding, "
             "recommendation, status (open/resolved/rejected/accepted-risk), and response for a closed finding.", "",
             "Phrase warnings require clause-specific interpretation review. ~0 allows any order; no wildcards in proximity. "
             "Prefer explicit tested expressions; do not delete terms merely because seeds are already covered. "
             "A retained warning needs a reason and evidence. Rewrites/removals require another complete evaluation.", "",
             *_scope_section(evaluation), *_line_table(evaluation), "", "## Complete evidence", "", "```json", json.dumps(evaluation, indent=2, ensure_ascii=False),
             "```", "", "## Earlier critic rounds", "", "```json", json.dumps(rounds, indent=2, ensure_ascii=False), "```", "",
             "## Response JSON", "", "```json", json.dumps(template, indent=2, ensure_ascii=False), "```"]
    path = ws.root / "critic" / f"packet-{number}.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


HOLDOUT_BLOCKERS = {
    "allocation_missing": "Freeze the allocation of the known records first (psb allocate)",
    "allocation_stale": "The reserved records no longer match the scope; re-screen them and psb allocate --rebind",
    "holdout_test_missing": "Run the held-out test (psb holdout-test) after the critic review",
    "holdout_test_incomplete": "The held-out test did not complete; run psb holdout-test again",
    "holdout_test_stale": "The held-out test ran on another interpretation of the query; run psb holdout-test again",
    "holdout_strategy_changed": ("The strategy changed after the held-out test: restore the tested strategy, or "
                                 "release the held-out records for repair (psb holdout-release)"),
}


def holdout_gate(ws: Workspace, evaluation: dict) -> tuple[dict | None, list[dict]]:
    """The held-out receipt a delivery rests on, or blockers when the allocation or the test is missing.
    Holdout misses never block: the tested query is delivered unchanged and a repair is offered."""
    from .progress import decisions
    state = allocation.state(ws)
    if state is None:
        known = bool(ws.sets()) or any(row["decision"] == "include" for row in decisions(ws).values())
        return None, [validation.issue("allocation_missing", HOLDOUT_BLOCKERS["allocation_missing"])] if known else []
    if not state["held"] or state["released"]:
        return None, []
    if state["stale"]:
        return None, [validation.issue("allocation_stale", HOLDOUT_BLOCKERS["allocation_stale"], evidence=state["stale"])]
    receipt, problem = holdout.matching(ws, evaluation, state)
    if problem:
        return None, [validation.issue(problem, HOLDOUT_BLOCKERS[problem])]
    return receipt, []


@contextmanager
def _publication_lock(ws: Workspace):
    path = ws.root / ".report.lock"
    try:
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise WorkspaceError("report already running or interrupted; inspect .report.lock before retrying") from exc
    try:
        os.write(fd, f"pid={os.getpid()} started={now()}".encode())
        os.close(fd)
        yield
    finally:
        path.unlink(missing_ok=True)


def _archive(ws: Workspace) -> None:
    existing = [ws.root / name for name in ARTIFACTS if (ws.root / name).exists()]
    if existing:
        target = ws.root / "history" / "deliveries" / str(time.time_ns())
        target.mkdir(parents=True)
        for path in existing:
            path.replace(target / path.name)


def _diagnostic(ws: Workspace, evaluation: dict, blockers: list[dict]) -> Path:
    path = ws.root / "diagnostic-audit.md"
    path.write_text("# Diagnostic audit - unfinished; not a protected final query\n\n```json\n" +
                    json.dumps({"blockers": blockers, "evaluation": evaluation}, indent=2, ensure_ascii=False) + "\n```\n", encoding="utf-8")
    return path


def report(ws: Workspace, *, diagnostic: bool = False, note: str = "") -> dict:
    with _publication_lock(ws):
        _archive(ws)
        cache = ws.pubmed.cache
        enabled = cache.enabled
        cache.enabled = False
        evaluation = {}
        rounds = []
        overrides = []
        extensions = []
        overridden = []
        receipt = None
        try:
            evaluation = evaluate(ws, term_counts=True)
            evaluation["fresh"] = True
            record_evaluation(ws, evaluation, note=note or "live finalization attempt")
            blockers = list(evaluation["validation"]["blockers"])
            if not evaluation["validation"]["complete"]:
                blockers.append(validation.issue("validation_incomplete", "All final validation checks must complete"))
            rounds = critic_rounds(ws)
            overrides = critic_overrides(ws)
            extensions = critic_extensions(ws)
            critic_hash = critic_digest(rounds, overrides, extensions)
            review = review_gate(ws, evaluation, rounds=rounds, overrides=overrides)
            blockers.extend(review["blockers"])
            overridden = review.get("overridden", [])
            receipt, held_blockers = holdout_gate(ws, evaluation)
            blockers.extend(held_blockers)
        except (ValueError, OSError, WorkspaceError) as exc:
            blockers = [validation.issue("finalization_failed", "Finalization could not complete", evidence=str(exc))]
        finally:
            cache.enabled = enabled
        evaluation["delivery_blockers"] = blockers
        attempt = ws.save_attempt(evaluation, purpose="diagnostic" if diagnostic else "report")
        if blockers or diagnostic:
            path = _diagnostic(ws, evaluation, blockers)
            return {"ok": False, "diagnostic": str(path), "attempt_id": attempt["attempt_id"], "blockers": blockers,
                    "message": "Diagnostic output only; no protected final query was issued"}
        stage = ws.root / "attempts" / (attempt["attempt_id"] + "-delivery")
        stage.mkdir()
        # One rendering of the held-out interpretation: the audit embeds it and the manifest carries it,
        # so the delivery message relays the same bytes.
        held = holdout.message(ws, receipt, evaluation)
        query_bytes = (evaluation["query"] + "\n").encode("utf-8")
        audit_bytes = _audit(ws, evaluation, rounds, overridden, held, receipt, extensions).encode("utf-8")
        import hashlib
        hashes = {"final-query.txt": hashlib.sha256(query_bytes).hexdigest(), "audit.md": hashlib.sha256(audit_bytes).hexdigest()}
        state = allocation.state(ws)
        manifest = {"status": "passed", "policy_version": validation.POLICY_VERSION, "attempt_id": attempt["attempt_id"],
                    "input_sha256": evaluation["input_sha256"], "review_sha256": evaluation["review_sha256"], "critic_sha256": critic_hash,
                    "created": now(), "query": evaluation["query"], "artifacts": hashes, "human_press_review": "pending",
                    "allocation_sha256": state["sha256"] if state else None,
                    "holdout": {"case": held["case"], "text": held["text"], "template_version": held["template_version"],
                                **({"receipt": receipt["number"], "receipt_sha256": holdout.receipt_digest(ws, receipt["number"])}
                                   if receipt else {})},
                    **({"overridden_findings": [f["id"] for f in overridden]} if overridden else {})}
        try:
            (stage / "final-query.txt").write_bytes(query_bytes)
            (stage / "audit.md").write_bytes(audit_bytes)
            write_json(stage / "validation-manifest.json", manifest)
            if validation.digest(validation.input_snapshot(ws)) != evaluation["input_sha256"] or critic_evidence(ws) != critic_hash:
                raise WorkspaceError("inputs or critic changed during finalization")
            for name in ("final-query.txt", "audit.md", "validation-manifest.json"):
                (stage / name).replace(ws.root / name)
        except (OSError, WorkspaceError) as exc:
            _archive(ws)
            blockers = [validation.issue("publication_failed", "Artifact publication failed", evidence=str(exc))]
            evaluation["delivery_blockers"] = blockers
            failure = ws.save_attempt(evaluation, purpose="publication-failed")
            path = _diagnostic(ws, evaluation, blockers)
            return {"ok": False, "blockers": blockers, "diagnostic": str(path), "attempt_id": failure["attempt_id"]}
        except BaseException:
            _archive(ws)
            raise
        ws.log({"type": "report", "attempt_id": attempt["attempt_id"], "status": "passed"})
        return {"ok": True, "report": str(ws.root / "audit.md"), "query_file": str(ws.root / "final-query.txt"),
                "manifest": str(ws.root / "validation-manifest.json"), "attempt_id": attempt["attempt_id"]}


def _changed_hint(ws: Workspace, manifest: dict, snapshot: dict) -> str:
    """Which inputs changed since the delivery, and whether a plain `psb report` re-run will do."""
    try:
        old = read_json(ws.root / "attempts" / f"{manifest.get('attempt_id')}.json")["evaluation"]["inputs"]
    except (OSError, ValueError, KeyError, TypeError):
        return "; run psb eval and psb report again"
    changed = validation.changed_inputs(old, snapshot)
    exempt = {f"protocol.{k}" for k in validation.REVIEW_EXEMPT_PROTOCOL_KEYS}
    advice = ("only conversation metadata changed: the critic is still current, so run psb report again"
              if changed and set(changed) <= exempt else "run psb eval, review the change with the critic, and psb report again")
    return f" ({', '.join(changed) or 'unknown'}); {advice}"


def verify_delivery(ws: Workspace) -> dict:
    """Read-only receipt check for consumers; never trust an orphaned or stale query file."""
    import hashlib
    try:
        manifest = read_json(ws.root / "validation-manifest.json")
        policy = manifest.get("policy_version") if isinstance(manifest, dict) else None
        legacy = policy in validation.LEGACY_POLICY_VERSIONS
        if not isinstance(manifest, dict) or manifest.get("status") != "passed" or not (policy == validation.POLICY_VERSION or legacy):
            raise WorkspaceError("missing current validation receipt")
        if (ws.root / ".report.lock").exists():
            raise WorkspaceError("publication is in progress or was interrupted")
        snapshot = validation.input_snapshot_v1(ws) if legacy else validation.input_snapshot(ws)
        if manifest.get("input_sha256") != validation.digest(snapshot):
            raise WorkspaceError("delivery inputs have changed" + _changed_hint(ws, manifest, snapshot))
        if manifest.get("critic_sha256") != critic_evidence(ws):
            raise WorkspaceError("critic evidence has changed")
        for name in ("final-query.txt", "audit.md"):
            expected = manifest.get("artifacts", {}).get(name)
            if hashlib.sha256((ws.root / name).read_bytes()).hexdigest() != expected:
                raise WorkspaceError(f"{name} is incomplete or changed")
        if (ws.root / "final-query.txt").read_text(encoding="utf-8").strip() != manifest.get("query"):
            raise WorkspaceError("query does not match the validated receipt")
        number = (manifest.get("holdout") or {}).get("receipt")
        if number is not None and holdout.receipt_digest(ws, number) != manifest["holdout"].get("receipt_sha256"):
            raise WorkspaceError("the held-out test receipt has changed")
        if legacy:
            return {"ok": True, "legacy": True, "query_file": str(ws.root / "final-query.txt"), "manifest": manifest,
                    "note": f"legacy delivery (policy {policy}): its recall labels predate held-out testing"}
        return {"ok": True, "query_file": str(ws.root / "final-query.txt"), "manifest": manifest}
    except (WorkspaceError, OSError, ValueError, TypeError, AttributeError) as exc:
        return {"ok": False, "error": str(exc)}


def _overridden_section(overridden: list[dict]) -> list[str]:
    """Must-fix findings the closing critic left open and the agent disagreed with: first thing a reviewer reads."""
    if not overridden:
        return []
    lines = ["## Delivered over an open critic objection", "",
             "The internal critic's closing round left these must-fix findings open. The query was delivered "
             "with them overridden; the peer reviewer should decide each one.", ""]
    for f in overridden:
        lines += [f"- **{f['id']}** ({f.get('domain')}, {f.get('kind')}{', block ' + str(f['block']) if f.get('block') else ''}): "
                  f"{f.get('finding')}",
                  f"  - Critic recommended: {f.get('recommendation') or 'not stated'}",
                  f"  - Reason for overriding: {f['override']}"]
    return lines + [""]


def _extension_section(extensions: list[dict]) -> list[str]:
    """A review period the user added after the verification round: disclosed beside any override."""
    if not extensions:
        return []
    lines = ["## Review budget extended", ""]
    for e in extensions:
        lines += [f"Review budget extended at the user's request: {str(e.get('reason') or '').strip()}", "",
                  f"The extension followed round {e.get('after_round')} and allowed one more revision round, then a "
                  "closing round and a verification round.", ""]
    return lines


def _audit(ws: Workspace, evaluation: dict, rounds: list[dict], overridden: list[dict] | None = None,
           held: dict | None = None, receipt: dict | None = None, extensions: list[dict] | None = None) -> str:
    protocol = evaluation["inputs"]["protocol"]
    strategy = Strategy.from_dict(evaluation["inputs"]["strategy"])
    versions = ws.versions()
    version = {"created": evaluation["run_date"], "strategy_sha256": validation.digest(strategy.to_dict())}
    log = ws.log_entries()
    ncbi = [e for e in log if e.get("type") == "ncbi"]
    concepts = protocol.get("concepts", [])
    lines = [
        "# PubMed search strategy: audit",
        "",
        f"Generated {now()} by `psb report` from workspace files. Draft for human PRESS peer review.",
        "",
        *_overridden_section(overridden or []),
        *_extension_section(extensions or []),
        "## Question and scope",
        "",
        f"- Question: {protocol.get('question')}",
        f"- Framework: {protocol.get('framework') or 'not recorded'}",
        f"- Scope confirmed by user: {'yes' if protocol.get('scope_confirmed') else 'no'}"
        + (f" ({protocol.get('notes')})" if protocol.get("notes") else ""),
        f"- Depth: {protocol.get('depth')}",
        "",
        "| Concept | Handling | Rationale |",
        "|---|---|---|",
        *[f"| {c.get('name') or c.get('id')} | {c.get('role')} | {c.get('rationale', '')} |" for c in concepts],
        "",
        "## Search details (PRISMA-S)",
        "",
        "- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)",
        f"- Date the final counts were run: {evaluation.get('run_date') or version['created'][:10]}",
        f"- Records added to PubMed up to: {evaluation.get('as_of') or 'search date (no as-of bound)'}",
        f"- Total records: {evaluation.get('count'):,}"
        + (f" ({evaluation.get('count_without_limits'):,} before limits)" if evaluation.get("count_without_limits") is not None else ""),
        "- Limits and filters: " + ("; ".join(f"`{l.clause}` ({l.rationale or 'no rationale recorded'})" for l in strategy.limits) or "none"),
        "",
        "### Strategy (line by line)",
        "",
        *_line_table(evaluation),
        "",
        "### Strategy (single line, for copying into PubMed)",
        "",
        "```text",
        evaluation["query"],
        "```",
        "",
        "## Known-record retrieval",
        "",
        "### Held-out test and interpretation",
        "",
        *(held or holdout.message(ws, receipt, evaluation))["text"].split("\n"),
        "",
    ]
    if receipt and receipt.get("status") in {"complete", "empty"}:
        lines += ["Held-out records (released to this audit after the test):", "", *holdout.records_section(ws, receipt), ""]
    lines += ["### Development checks", ""]
    if evaluation.get("sets"):
        lines += _recall_table(evaluation)
        lines += ["", "Development records were used to build the strategy; their retrieval is a development check, "
                  "not independent validation and not sensitivity. Comparison lists are reported separately.", ""]
        if evaluation.get("misses"):
            lines += ["Missed records:", ""]
            lines += [f"- PMID {m['pmid']} ({', '.join(m['sets'])}): not retrieved by {', '.join(m['failing_blocks']) or 'limits'}"
                      for m in evaluation["misses"]]
            lines.append("")
    else:
        lines += ["No development or comparison records were available.", ""]
    if isinstance(evaluation.get("ablation"), list):
        lines += ["### Leave-one-block-out", "", "| Block dropped | Records | Known records gained |", "|---|---:|---:|"]
        lines += [f"| {a['drop']} | {a['count']:,} | {a['known_gained']} |" for a in evaluation["ablation"]]
        lines.append("")
    lines += ["## Development history", "", "| Version | Records | Change | Known lost | Note |", "|---:|---:|---|---|---|"]
    for entry in versions:
        diff = entry["evaluation"].get("since_previous") or {}
        changes = "; ".join(
            f"{block}: +{len(c.get('terms_added', []))} / -{len(c.get('terms_removed', []))}" for block, c in (diff.get("changes") or {}).items()
            if not block.startswith("_")
        ) or ("initial" if entry["version"] == 1 else "limits/combination")
        lost = ", ".join(diff.get("known_lost", [])) or "none"
        lines.append(f"| {entry['version']} | {entry['evaluation'].get('count', 0):,} | {changes} | {lost} | {entry.get('note', '')} |")
    lines += ["", "## Internal critic (PRESS-informed, not PRESS peer review)", ""]
    if rounds:
        for r in rounds:
            findings = r.get("findings", [])
            note = f" ({r['note']})" if r.get("note") else ""
            lines.append(f"- Round {r.get('round')} on version {r.get('strategy_version')}{note}: {len(findings)} findings; "
                         + ", ".join(f"{f.get('id')} {f.get('severity')} {f.get('status')}" for f in findings))
        lines.append("")
    else:
        lines += ["No critic round was run.", ""]
    lines += [
        "## Limitations",
        "",
        "- This is a draft. It needs peer review by an information specialist (PRESS) before use.",
        "- The internal critic is automated quality assurance, not PRESS peer review.",
        "- PubMed only: records indexed only in other databases are out of reach of this strategy.",
        "",
        f"_Provenance: {len(ncbi)} NCBI requests logged ({sum(1 for e in ncbi if e.get('cache'))} from cache); "
        f"strategy sha256 {version['strategy_sha256'][:12]}._",
    ]
    lines += ["", "## Validation evidence and dispositions", "", "```json",
              json.dumps({"validation": evaluation["validation"], "vocabulary": evaluation["vocabulary"],
                          "translation": evaluation.get("translation"), "critic": rounds}, indent=2, ensure_ascii=False), "```", ""]
    return "\n".join(lines) + "\n"
