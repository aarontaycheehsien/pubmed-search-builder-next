"""MeSH through E-utilities (db=mesh): the same client, cache and log as PubMed searches."""

from __future__ import annotations

from .ncbi import PubMed

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
