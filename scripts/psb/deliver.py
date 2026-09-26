"""Critic packets, critic-round checks, and the audit report, all rendered from the workspace.

The report reads only workspace files (protocol, the latest evaluated version, sets, critic
rounds, log), so every number in it comes from a `psb` command rather than from prose.
"""

from __future__ import annotations

import json
from pathlib import Path

from .strategy import full_query
from .workspace import ROLES, Workspace, WorkspaceError, now, read_json, sha256_text

DOMAINS = [
    "translation",       # PRESS 1: translation of the research question
    "operators",         # PRESS 2: Boolean and proximity operators
    "subject_headings",  # PRESS 3
    "text_words",        # PRESS 4
    "syntax",            # PRESS 5: spelling, syntax, line numbers
    "limits_filters",    # PRESS 6
]
SEVERITIES = {"must-fix", "should-fix", "document"}
KINDS = {"lexical", "structural", "scope", "filter", "syntax", "reporting"}
STATUSES = {"open", "resolved", "rejected", "accepted-risk"}


def latest_version(ws: Workspace) -> dict:
    versions = ws.versions()
    if not versions:
        raise WorkspaceError("run psb eval first")
    current = sha256_text(json.dumps(ws.strategy().to_dict(), sort_keys=True))
    if versions[-1]["strategy_sha256"] != current:
        raise WorkspaceError("strategy.json changed since the last psb eval; run psb eval first")
    return versions[-1]


def critic_rounds(ws: Workspace) -> list[dict]:
    return [read_json(p) for p in sorted((ws.root / "critic").glob("round-*.json"))]  # type: ignore[misc]


def _line_table(evaluation: dict) -> list[str]:
    rows = ["| # | Search | Results |", "|---:|---|---:|"]
    for line in evaluation.get("lines", []):
        text = line["text"].replace("|", "\\|")
        rows.append(f"| {line['n']} | `{text}` | {line['count']:,} |")
    return rows


def _recall_table(evaluation: dict) -> list[str]:
    rows = ["| Set | Role (independence) | In PubMed | Retrieved | Recall |", "|---|---|---:|---:|---:|"]
    for name, data in (evaluation.get("sets") or {}).items():
        recall = "n/a" if data["recall_percent"] is None else f"{data['recall_percent']}%"
        rows.append(f"| {name} | {data['role']} ({ROLES.get(data['role'], '')}) | {data['in_pubmed']} | {data['retrieved']} | {recall} |")
    return rows


def critic_packet(ws: Workspace) -> Path:
    version = latest_version(ws)
    evaluation = version["evaluation"]
    protocol = ws.protocol()
    rounds = critic_rounds(ws)
    open_findings = [f for r in rounds for f in r.get("findings", []) if f.get("status") == "open"]
    number = len(rounds) + 1
    lines = [
        f"# Critic packet, round {number}",
        "",
        "You are an experienced information specialist doing a PRESS 2015 review of a draft PubMed "
        "search for an evidence synthesis. Use only this packet. Judge whether the strategy will find "
        "the relevant records; do not answer the review question.",
        "",
        "## Review question and scope",
        "",
        f"Question: {protocol.get('question')}",
        "",
        "| Concept | Role | Rationale |",
        "|---|---|---|",
        *[f"| {c.get('name') or c.get('id')} (`{c.get('id')}`) | {c.get('role')} | {c.get('rationale', '')} |" for c in protocol.get("concepts", [])],
        "",
        f"Eligibility (screening, not searched): include {protocol.get('eligibility', {}).get('include')}; "
        f"exclude {protocol.get('eligibility', {}).get('exclude')}",
        f"Limits: {protocol.get('limits') or 'none'}",
        "",
        f"## Strategy (version {version['version']}, total {evaluation.get('count'):,})",
        "",
        *_line_table(evaluation),
        "",
        "PubMed translation issues: " + (", ".join(i["code"] for i in evaluation.get("translation_issues", [])) or "none"),
        "",
        "## Known relevant records",
        "",
        *_recall_table(evaluation),
        "",
        "Missed records and the blocks that fail them: "
        + (json.dumps(evaluation.get("misses", []), ensure_ascii=False) if evaluation.get("misses") else "none"),
        "",
        "Leave-one-block-out: " + json.dumps(evaluation.get("ablation"), ensure_ascii=False),
        "",
    ]
    if open_findings:
        lines += ["## Findings still open from earlier rounds", "", "```json", json.dumps(open_findings, indent=2, ensure_ascii=False), "```", ""]
    lines += [
        "## What to return",
        "",
        f"Return only JSON saved as `critic/round-{number}.json`:",
        "",
        "```json",
        json.dumps(
            {
                "round": number,
                "strategy_version": version["version"],
                "domains": {d: {"verdict": "pass | revise", "note": "..."} for d in DOMAINS},
                "findings": [
                    {"id": "F1", "domain": "text_words", "severity": "must-fix | should-fix | document",
                     "kind": "lexical | structural | scope | filter | syntax | reporting",
                     "block": "block id or null", "finding": "...", "recommendation": "...", "status": "open"}
                ],
            },
            indent=2,
        ),
        "```",
        "",
        "Keep IDs of earlier findings. Every domain needs a verdict. Only raise findings you can tie to "
        "something in this packet.",
    ]
    path = ws.root / "critic" / f"packet-{number}.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    ws.log({"type": "critic_packet", "round": number, "version": version["version"]})
    return path


def check_round(ws: Workspace, path: Path) -> dict:
    data = read_json(path)
    problems = []
    if not isinstance(data, dict):
        return {"ok": False, "problems": ["round must be a JSON object"]}
    domains = data.get("domains") or {}
    for domain in DOMAINS:
        verdict = (domains.get(domain) or {}).get("verdict")
        if verdict not in {"pass", "revise"}:
            problems.append(f"domain {domain!r} needs a verdict of pass or revise")
    ids = set()
    for finding in data.get("findings") or []:
        fid = finding.get("id")
        if not fid or fid in ids:
            problems.append(f"finding id missing or duplicated: {fid!r}")
        ids.add(fid)
        if finding.get("severity") not in SEVERITIES:
            problems.append(f"{fid}: severity must be one of {sorted(SEVERITIES)}")
        if finding.get("kind") not in KINDS:
            problems.append(f"{fid}: kind must be one of {sorted(KINDS)}")
        if finding.get("status") not in STATUSES:
            problems.append(f"{fid}: status must be one of {sorted(STATUSES)}")
        if finding.get("status") in {"rejected", "accepted-risk"} and not finding.get("response"):
            problems.append(f"{fid}: a {finding.get('status')} finding needs a response explaining why")
    earlier = {f.get("id") for r in critic_rounds(ws) if r.get("round", 0) < data.get("round", 0)
               for f in r.get("findings", []) if f.get("status") == "open"}
    dropped = sorted(i for i in earlier - ids if i)
    if dropped:
        problems.append(f"earlier open findings are missing from this round: {', '.join(dropped)}")
    open_must = [f.get("id") for f in data.get("findings") or [] if f.get("status") == "open" and f.get("severity") == "must-fix"]
    return {"ok": not problems, "problems": problems, "open_must_fix": open_must}


def report(ws: Workspace) -> Path:
    version = latest_version(ws)
    evaluation = version["evaluation"]
    protocol = ws.protocol()
    strategy = ws.strategy()
    versions = ws.versions()
    rounds = critic_rounds(ws)
    log = ws.log_entries()
    ncbi = [e for e in log if e.get("type") == "ncbi"]
    concepts = protocol.get("concepts", [])
    lines = [
        "# PubMed search strategy: audit",
        "",
        f"Generated {now()} by `psb report` from workspace files. Draft for human PRESS peer review.",
        "",
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
        "- Database and platform: MEDLINE via PubMed (NCBI E-utilities)",
        f"- Date the final counts were run: {evaluation.get('run_date') or version['created'][:10]}",
        f"- Records added to PubMed up to: {protocol.get('as_of') or 'search date (no as-of bound)'}",
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
        full_query(strategy),
        "```",
        "",
        "## Validation against known relevant records",
        "",
    ]
    if evaluation.get("sets"):
        lines += _recall_table(evaluation)
        lines += ["", "Relative recall against these sets is not absolute sensitivity. Development sets were used to "
                  "build the strategy and cannot show how it performs on unseen records.", ""]
        if evaluation.get("misses"):
            lines += ["Missed records:", ""]
            lines += [f"- PMID {m['pmid']} ({', '.join(m['sets'])}): not retrieved by {', '.join(m['failing_blocks']) or 'limits'}"
                      for m in evaluation["misses"]]
            lines.append("")
    else:
        lines += ["No known relevant records were available, so recall was not estimated.", ""]
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
    path = ws.root / "audit.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    ws.log({"type": "report", "version": version["version"]})
    return path
