"""One policy for technical validity and evidence-bound mandatory review."""
from __future__ import annotations

import hashlib
import json
from . import syntax

POLICY_VERSION = "1"
BLOCKING_CODES = {"field_not_found", "truncation_dropped", "all_fields_fallback", "unknown_tag"}
PHRASE_CODES = {"phrase_not_found", "quoted_phrase_not_found"}


def stable(value):
    if isinstance(value, dict):
        return {k: stable(v) for k, v in value.items() if k != "checked_at"}
    if isinstance(value, list):
        return [stable(v) for v in value]
    return value


def digest(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def issue(code: str, message: str, *, severity: str = "error", location: str = "final", **evidence) -> dict:
    item = dict(code=code, message=message, severity=severity, location=location, **evidence)
    return identify(item)


def identify(item: dict, location: str | None = None) -> dict:
    item = dict(item)
    item["location"] = location or item.get("location", "final")
    item["blocking"] = item.get("severity") == "error" or item["code"] in BLOCKING_CODES
    item["requires_review"] = not item["blocking"] and item.get("severity") == "warning"
    if item["code"] in PHRASE_CODES:
        atoms = syntax.atoms(item.get("query", ""))
        controlled = any(a["field"] in {"mh", "majr", "nm", "sh"} for a in atoms)
        item["review_guidance"] = {
            "controlled_vocabulary": "Verify authority record and field compatibility separately" if controlled else None,
            "outcomes": ["rewrite and re-evaluate", "remove with justification and re-evaluate", "accept the observed interpretation with clause-specific evidence"],
            "candidates": ["If adjacency matters, test ~0 (any order, not exact ordered matching)",
                           "If separation is acceptable, choose and test ~N",
                           "If adjacency is unnecessary, test individually tagged words joined with AND",
                           "For morphology, test an ordinary wildcard phrase or enumerated proximity variants"],
            "constraints": ["Never put wildcards inside proximity", "Never silently select a repair",
                            "Compare clause/final counts, translation and known-record losses",
                            "Zero hits and seed coverage alone do not establish redundancy"],
        }
    key = {k: v for k, v in item.items() if k not in {"id", "message", "disposition", "checked_at"}}
    item["id"] = "I-" + digest(stable(key))[:20]
    return item


def summarize(issues: list[dict], *, complete: bool) -> dict:
    indexed = {i["id"]: i for i in issues}
    rows = list(indexed.values())
    return {"policy_version": POLICY_VERSION, "complete": complete,
            "blockers": [i for i in rows if i["blocking"]],
            "review_required": [i for i in rows if i["requires_review"]],
            "issues": rows}


def input_snapshot(ws) -> dict:
    return {"strategy": ws.strategy().to_dict(), "protocol": ws.protocol(), "sets": ws.sets(),
            "as_of": ws.pubmed.as_of, "policy_version": POLICY_VERSION}


# Protocol fields that record the conversation, not what is searched. Editing them after a review
# (correcting scope_confirmed, adding a note) needs a fresh `psb report`, never a fresh critic.
REVIEW_EXEMPT_PROTOCOL_KEYS = ("notes", "scope_confirmed")


def review_inputs(inputs: dict) -> dict:
    """The inputs a critic reviews: everything but conversation metadata in the protocol."""
    protocol = {k: v for k, v in (inputs.get("protocol") or {}).items() if k not in REVIEW_EXEMPT_PROTOCOL_KEYS}
    return {**inputs, "protocol": protocol}


def changed_inputs(old: dict, new: dict) -> list[str]:
    """Top-level input sections, and protocol fields, that differ between two snapshots."""
    changed = []
    for key in sorted(set(old) | set(new)):
        if key == "protocol":
            a, b = old.get(key) or {}, new.get(key) or {}
            changed += [f"protocol.{k}" for k in sorted(set(a) | set(b)) if a.get(k) != b.get(k)]
        elif old.get(key) != new.get(key):
            changed.append(key)
    return changed


def review_fingerprint(evaluation: dict) -> str:
    """Counts and clocks may change; query interpretation and known hits may not."""
    authorities = [{k: v for k, v in row.items() if k != "checked_at"}
                   for row in evaluation.get("vocabulary", [])]
    return digest({"inputs": digest(review_inputs(evaluation.get("inputs") or {})), "query": evaluation.get("query"),
                   "issues": sorted(i["id"] for i in evaluation["validation"]["issues"]),
                   "translations": [(x.get("query"), x.get("translation")) for x in evaluation.get("lines", [])],
                   "translation": evaluation.get("translation"), "vocabulary": stable(authorities),
                   "retrieved": evaluation.get("retrieved_known", []),
                   "present": evaluation.get("known_in_pubmed", [])})
