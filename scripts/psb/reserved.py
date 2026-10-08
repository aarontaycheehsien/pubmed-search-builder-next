"""What the builder has seen, and the guard that keeps held-out records out of its view.

    exposure.jsonl  one event per PMID whose content or retrieval feedback a builder-facing
                    command showed, or that the agent declared with ``psb exposure declare``

A record screened only in the separate screening context (``psb screen --context separate``, with
``fetch``/``sample --screening`` writing to the private store) and never shown by a builder-facing
command is unexposed. Everything else counts as exposed: unknown exposure is exposure. Handling a
PMID alone (resolving it, listing it as a neighbour, counting it) shows no content.

Exposure control is procedural. psb refuses, redacts and records; the files are not a security
boundary, and the builder must not read ``screening/``.
"""

from __future__ import annotations

import re
from typing import Iterable

from .workspace import Workspace, WorkspaceError, append_jsonl, now, read_jsonl

KINDS = ("title", "abstract", "indexing", "full-text", "description", "feedback", "screened")
_NUMBER = re.compile(r"(?<![\w.])0*(\d+)(?![\w.])")


def record(ws: Workspace, pmids: Iterable[str], kind: str, via: str, *, note: str = "",
           declared: bool = False) -> list[dict]:
    """Append one exposure event per PMID."""
    if kind not in KINDS:
        raise WorkspaceError(f"exposure kind must be one of {', '.join(KINDS)}")
    entries = []
    for pmid in dict.fromkeys(str(p) for p in pmids):
        entry = {"pmid": pmid, "kind": kind, "via": via, "declared": declared, "note": note.strip(), "at": now()}
        append_jsonl(ws.root / "exposure.jsonl", entry)
        entries.append(entry)
    return entries


def events(ws: Workspace) -> list[dict]:
    return [e for e in read_jsonl(ws.root / "exposure.jsonl") if str(e.get("pmid", "")).isdigit()]


def by_pmid(ws: Workspace) -> dict[str, list[dict]]:
    found: dict[str, list[dict]] = {}
    for event in events(ws):
        found.setdefault(str(event["pmid"]), []).append(event)
    return found


# -- guard ------------------------------------------------------------------------------------

def refuse(ws: Workspace, pmids: Iterable[str], action: str) -> None:
    """Stop a builder-facing command before it shows a reserved record."""
    reserved = ws.reserved_pmids()
    hit = [p for p in pmids if str(p) in reserved]
    if hit:
        one = len(hit) == 1
        raise WorkspaceError(
            f"{len(hit)} of the requested records {'is' if one else 'are'} reserved for the held-out test, and "
            f"{action} would expose {'it' if one else 'them'}. Reserved records are released only by psb holdout-release.")


def check_query(ws: Workspace, query: str) -> None:
    """A query that names a reserved PMID reveals whether the strategy retrieves that record."""
    reserved = ws.reserved_pmids()
    if reserved and any(m.group(1) in reserved for m in _NUMBER.finditer(query)):
        raise WorkspaceError("this query names a record reserved for the held-out test; searching for it by "
                             "PMID would reveal whether the strategy retrieves it")


def visible(ws: Workspace, pmids: Iterable[str]) -> list[str]:
    """``pmids`` without reserved records, in order."""
    reserved = ws.reserved_pmids()
    return [p for p in pmids if str(p) not in reserved]
