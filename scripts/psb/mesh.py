"""MeSH through E-utilities (db=mesh): the same client, cache and log as PubMed searches."""

from __future__ import annotations

from .ncbi import PubMed, NcbiError
from . import syntax
from .validation import issue

SCOPE_NOTE_LIMIT = 400


def _kind(summary: dict) -> str:
    ui = str(summary.get("ds_meshui", ""))
    return {"D": "descriptor", "C": "supplementary", "Q": "qualifier"}.get(ui[:1], summary.get("ds_recordtype", ""))


def _brief(summary: dict) -> dict:
    terms = summary.get("ds_meshterms") or []
    note = str(summary.get("ds_scopenote", "")).strip()
    return {
        "ui": summary.get("ds_meshui", ""),
        "name": terms[0] if terms else "",
        "type": _kind(summary),
        "scope_note": note if len(note) <= SCOPE_NOTE_LIMIT else note[: SCOPE_NOTE_LIMIT - 3] + "...",
        "tree_numbers": [link.get("treenum") for link in summary.get("ds_idxlinks") or [] if link.get("treenum")],
        "entry_terms": len(terms) - 1 if terms else 0,
        "mapped_to": summary.get("ds_headingmappedto") or None,
    }


def lookup(pm: PubMed, term: str, *, limit: int = 8) -> dict:
    uids = pm.mesh_search(term, retmax=limit)
    return {"query": term, "matches": [_brief(s) for s in pm.mesh_summary(uids)]}


def _resolve(pm: PubMed, identifier: str) -> dict:
    ident = identifier.strip()
    query = f"{ident}[mhui]" if ident[:1] in "DCQ" and ident[1:].isdigit() else f'"{ident}"[mh]'
    uids = pm.mesh_search(query, retmax=1) or pm.mesh_search(ident, retmax=1)
    summaries = pm.mesh_summary(uids)
    if not summaries:
        raise ValueError(f"no MeSH record found for {identifier!r}")
    return summaries[0]


def show(pm: PubMed, identifier: str, *, counts: bool = True, children: bool = True) -> dict:
    summary = _resolve(pm, identifier)
    brief = _brief(summary)
    terms = summary.get("ds_meshterms") or []
    brief["scope_note"] = str(summary.get("ds_scopenote", "")).strip()
    brief["entry_terms"] = terms[1:]
    brief["year_introduced"] = summary.get("ds_yearintroduced") or None
    brief["previous_indexing"] = summary.get("ds_previousindexing") or []
    brief["see_related"] = summary.get("ds_seerelated") or []
    if children:
        child_uids = sorted({str(c) for link in summary.get("ds_idxlinks") or [] for c in link.get("children") or [] if str(c).startswith("68")})
        brief["narrower"] = [
            {"ui": s.get("ds_meshui"), "name": (s.get("ds_meshterms") or [""])[0]}
            for s in pm.mesh_summary(child_uids[:100])
        ]
    if counts and brief["name"]:
        name = brief["name"]
        if brief["type"] == "supplementary":
            brief["pubmed_count"] = {"[nm]": pm.count(f'"{name}"[nm]')}
        else:
            brief["pubmed_count"] = {
                "[Mesh]": pm.count(f'"{name}"[Mesh]'),
                "[Mesh:noexp]": pm.count(f'"{name}"[Mesh:noexp]'),
            }
    return brief


def validate_query(pm: PubMed, query: str, checked_at: str) -> tuple[list[dict], list[dict]]:
    """Validate every vocabulary atom without treating retrieval counts as authority evidence."""
    evidence, problems = [], []
    memo = {}

    def resolve(name: str, kind: str) -> dict:
        key = (" ".join(name.casefold().split()), kind)
        if key in memo:
            return memo[key]
        search_field = "Substance Name" if kind == "supplementary" else "mh"
        uids = pm.mesh_search(f'"{name}"[{search_field}]', retmax=100)
        if len(uids) >= 100:
            raise NcbiError("MeSH candidates truncated; narrow or use the canonical heading")
        summaries = pm.mesh_summary(uids)
        candidates = [_brief(s) for s in summaries]
        matches = [s for s in candidates if " ".join(s["name"].casefold().split()) == key[0]]
        compatible = [s for s in matches if s["type"] == kind]
        row = {"requested": name, "expected_type": kind, "checked_at": checked_at,
               "source": "NCBI MeSH ESearch/ESummary", "candidates": candidates}
        if len(compatible) == 1:
            row.update(status="verified", ui=compatible[0]["ui"], preferred_label=compatible[0]["name"], type=kind)
        else:
            row["status"] = "ambiguous" if len(compatible) > 1 else "wrong_type" if matches else "not_canonical" if candidates else "not_found"
        memo[key] = row
        return row

    for index, atom in enumerate(syntax.atoms(query)):
        if atom["field"] not in {"mh", "majr", "nm", "sh"}:
            continue
        location = f"vocabulary:{index + 1}"
        name = atom["text"].replace('"', '').strip()
        parts = [p.strip() for p in name.split("/")]
        kind = {"mh": "descriptor", "majr": "descriptor", "nm": "supplementary", "sh": "qualifier"}[atom["field"]]
        try:
            if len(parts) > 2 or (len(parts) == 2 and kind != "descriptor") or "*" in name:
                problems.append(issue("vocabulary_syntax", "Use explicit canonical vocabulary labels; unsupported vocabulary expression", location=location, term=atom))
                continue
            row = dict(resolve(parts[0], kind), location=location, term=atom)
            evidence.append(row)
            if row["status"] != "verified":
                problems.append(issue("vocabulary_" + row["status"], "Vocabulary label is not an unambiguous canonical record of the required type", location=location, evidence=row))
                continue
            if len(parts) == 2:
                qualifier = dict(resolve(parts[1], "qualifier"))
                row["qualifier"] = qualifier
                if qualifier["status"] != "verified":
                    problems.append(issue("qualifier_invalid", "Qualifier needs canonical authority verification", location=location, evidence=qualifier))
                    continue
                descriptor = pm.mesh_descriptor(row["ui"])
                allowed = descriptor.get("allowableQualifier", [])
                if isinstance(allowed, str):
                    allowed = [allowed]
                if not isinstance(allowed, list) or not all(isinstance(x, str) for x in allowed):
                    raise NcbiError("malformed allowable-qualifier evidence")
                row["allowable_qualifiers"] = allowed
                if not any(url.rsplit("/", 1)[-1] == qualifier["ui"] for url in allowed):
                    problems.append(issue("qualifier_incompatible", "Qualifier is not allowed for this descriptor", location=location, evidence=row))
        except NcbiError as exc:
            row = {"location": location, "term": atom, "checked_at": checked_at, "status": "unverified", "error": str(exc)}
            evidence.append(row)
            problems.append(issue("vocabulary_unverified", "Authority verification could not complete", location=location, evidence=str(exc)))
    return evidence, problems
