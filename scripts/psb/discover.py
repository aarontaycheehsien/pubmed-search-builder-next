"""Known-record discovery through OpenAlex.

Every route here produces candidates, never known records: each one is screened against the
eligibility criteria before it enters a set, exactly as PubMed neighbours are. What a route
can show depends on how it found the record (see ``evaluate.INDEPENDENT_ROUTES``):

- ``openalex:refs``     a work's reference list: independent of the strategy's wording
- ``openalex:citedin``  works citing a known record: a separate tier, never in the recall bound
- ``openalex:prior-reviews`` reviews found by keyword: only their reference lists are independent
- ``openalex:frame``    a seeded random sample of a topic frame, screened before retrieval is checked
"""

from __future__ import annotations

import random

from . import progress
from .openalex import OpenAlexError, brief, doi_of, normalise_id, pmid_of, topic_of, work_id
from .strategy import full_query
from .workspace import Workspace, normalize_pmids

LINKS = ("refs", "citedin")
FRAME_MAX = 200
PROFILE_SLICES = 10
GAP_MIN_SHARE = 5.0
GAP_MIN_RECORDS = 3


def _label(work: dict) -> str:
    return pmid_of(work) or work_id(work)


def _to_pmids(ws: Workspace, works: list[dict]) -> tuple[dict[str, dict], list[dict]]:
    """PMIDs for works, through OpenAlex's own PMID and then the PMC ID converter on the DOI."""
    mapped: dict[str, dict] = {}
    unmapped: list[dict] = []
    for work in works:
        pmid = pmid_of(work)
        if pmid:
            mapped.setdefault(pmid, work)
        else:
            unmapped.append(work)
    dois = {doi_of(w): w for w in unmapped if doi_of(w)}
    if dois:
        converted: dict[str, str] = {}
        names = sorted(dois)
        for start in range(0, len(names), 200):
            converted.update({k.lower(): v for k, v in ws.pubmed.idconv(names[start:start + 200]).items()})
        still = []
        for work in unmapped:
            pmid = converted.get(doi_of(work) or "")
            if pmid and pmid.isdigit():
                mapped.setdefault(pmid.lstrip("0"), work)
            else:
                still.append(work)
        unmapped = still
    return mapped, unmapped


def _dated(ws: Workspace, pmids) -> set[str]:
    pmids = list(pmids)
    return ws.pubmed.existing(pmids) if ws.pubmed.as_of and pmids else set(pmids)


def neighbors(ws: Workspace, identifiers: list[str], *, links: list[str], max_per_seed: int, limit: int,
              exclude_known: bool, set_names: list[str]) -> dict:
    """Reference lists and citing works in OpenAlex, mapped to PMIDs and ranked by how many origins link to them."""
    unknown = [l for l in links if l not in LINKS]
    if unknown:
        raise OpenAlexError(f"unknown OpenAlex link {unknown[0]!r}; use {', '.join(LINKS)}")
    oa = ws.openalex
    until = ws.as_of()
    known = {p for d in ws.sets().values() for p in d.get("pmids", [])}
    scores: dict[str, dict] = {}
    origins, not_found, no_refs, after = [], [], [], []
    outside: dict[str, dict] = {}
    for ident in identifiers:
        work = oa.work(ident)
        if work is None:
            not_found.append(ident)
            continue
        label = _label(work)
        published = str(work.get("publication_date") or work.get("publication_year") or "")
        if until and published and published[:len(until)] > until[:len(published)]:
            # A review published after the as-of date may be the very review being reproduced.
            after.append(label)
            continue
        origins.append(label)
        for link in links:
            if link == "refs":
                refs = [str(r).rsplit("/", 1)[-1] for r in work.get("referenced_works") or []]
                if not refs:
                    no_refs.append(label)
                    continue
                linked = oa.by_ids(refs)
            else:
                linked, _ = oa.citing(work_id(work), limit=max_per_seed, until=until)
            mapped, unmapped = _to_pmids(ws, linked)
            for work_row in unmapped:
                outside.setdefault(work_id(work_row), brief(work_row))
            for pmid, row in mapped.items():
                entry = scores.setdefault(pmid, {"pmid": pmid, "from": [], "links": set(), "title": row.get("display_name") or "",
                                                 "year": row.get("publication_year"), "work": work_id(row)})
                entry["from"].append(label)
                entry["links"].add(link)
    own = set(origins)
    candidates = [e for p, e in scores.items() if p not in own and not (exclude_known and p in known)]
    dated = _dated(ws, [e["pmid"] for e in candidates])
    candidates = [e for e in candidates if e["pmid"] in dated]
    candidates.sort(key=lambda e: (-len(set(e["from"])), e["pmid"]))
    rows = [{**e, "links": sorted(e["links"]), "from": sorted(set(e["from"]))} for e in candidates[:limit]]
    body = {"ok": True, "source": "openalex", "seeds": len(origins), "candidates": len(candidates), "shown": len(rows),
            "rows": rows, "not_in_pubmed": {"count": len(outside), "works": list(outside.values())[:25]},
            "note": "Neighbours are candidates, not relevant records: screen them before using them for mining. "
                    "Linked works with no PMID are outside PubMed and cannot be scored; they are listed, not candidates."}
    if no_refs:
        body["no_reference_list"] = no_refs
        body["note"] += (" OpenAlex holds no reference list for " + ", ".join(no_refs) + ". That means no list was "
                         "deposited, not that the work has no references: try PubMed (psb neighbors <PMID> --links refs), "
                         "another review, or ask the user for the included studies.")
    if not_found:
        body["not_found"] = not_found
    if after:
        body["after_as_of"] = after
        body["note"] += (" Not followed, because they were published after the as-of date " + str(until) + ": "
                         + ", ".join(after) + ".")
    if "citedin" in links:
        body["tier_note"] = ("Forward citations are reported as their own tier: they count towards the recall bound only "
                             "through a held-out set, never as records found without a keyword search.")

    def data() -> dict:
        in_sets = {p for d in ws.sets().values() for p in d.get("pmids", [])}
        found = {"links": links, "from": origins, "sets": sorted(set(set_names or [])), "candidates": len(candidates),
                 "shown": len(rows), "exclude_known": exclude_known, "index": "openalex",
                 "per_link": {link: sum(1 for e in candidates if link in e["links"]) for link in links},
                 "known": sum(1 for p in scores if p in in_sets and p not in own),
                 "not_in_pubmed": len(outside), "no_reference_list": no_refs, "not_found": not_found}
        if rows:
            found["batch"] = progress.record_batch(
                ws, "openalex:" + ",".join(links), progress.neighbors_label(links, origins, found["sets"], "openalex"),
                [r["pmid"] for r in rows], total=len(candidates), origin=origins,
                origins={r["pmid"]: r["from"] for r in rows})["batch"]
        return found
    return progress.attach(body, ws, "neighbors", data)


def reference_counts(ws: Workspace, pmids: list[str]) -> dict:
    """How many references OpenAlex holds for each PMID (one request per 50 PMIDs)."""
    try:
        works = ws.openalex.by_pmids(pmids, select="id,ids,referenced_works_count")
    except OpenAlexError as exc:
        return {"error": str(exc)}
    return {"counts": {p: (works[p].get("referenced_works_count") or 0) if p in works else None for p in pmids}}


def prior_reviews(ws: Workspace, text: str, *, n: int) -> dict:
    """Reviews in OpenAlex, including those outside PubMed. Only their reference lists are independent."""
    filters = ["type:review"]
    if ws.as_of():
        filters.append(f"to_publication_date:{ws.as_of()}")
    works, total = ws.openalex.search(text, filters=filters, n=n)
    rows = [brief(w) for w in works]
    pmids = sorted({r["pmid"] for r in rows if r["pmid"]}, key=int)
    body = {"ok": True, "source": "openalex", "count": total, "records": rows,
            "note": ("references is the number of references OpenAlex holds for each review. A review's reference list "
                     "is the main source of known records that do not depend on your wording: follow it with "
                     "psb neighbors <PMID, DOI or OpenAlex ID> --links refs --source openalex, then screen. Reviews with "
                     "no PMID are outside PubMed, but their reference lists are still usable.")}

    def data() -> dict:
        found = {"query": f"OpenAlex: {text} ({', '.join(filters)})", "count": total, "shown": len(rows), "retstart": 0}
        if rows:
            found["batch"] = progress.record_batch(ws, "openalex:prior-reviews",
                                                   f"{progress.PURPOSES['prior-reviews']} (OpenAlex) {progress.code(progress.clean(text, 80))}",
                                                   pmids, total=total, query=found["query"])["batch"]
        return found
    return progress.attach(body, ws, "search:prior-reviews", data)


def frame_sample(ws: Workspace, topics: list[str], *, n: int, seed: int) -> dict:
    """A seeded random sample of PubMed records in one or two OpenAlex topics."""
    if not topics:
        raise OpenAlexError("a frame sample needs --topic (an OpenAlex topic ID such as T10102)")
    if not 1 <= n <= FRAME_MAX:
        raise OpenAlexError(f"--n must be between 1 and {FRAME_MAX} for a frame sample")
    ids = [t.strip().rsplit("/", 1)[-1].upper() for t in topics]
    filters = [f"primary_topic.id:{'|'.join(ids)}", "has_pmid:true"]
    if ws.as_of():
        filters.append(f"to_publication_date:{ws.as_of()}")
    works, total = ws.openalex.sample(filters=filters, n=n, seed=seed)
    mapped = {pmid_of(w): w for w in works if pmid_of(w)}
    dated = _dated(ws, mapped)
    rows = [{"pmid": p, "year": w.get("publication_year"), "title": w.get("display_name") or ""}
            for p, w in sorted(mapped.items(), key=lambda kv: int(kv[0])) if p in dated]
    query = f"OpenAlex frame: {','.join(filters)} (sample {n}, seed {seed})"
    body = {"ok": True, "source": "openalex", "count": total, "records": rows,
            "note": ("Screen every record here against the eligibility criteria, and add every include to a held-out "
                     "set (psb set add frame ... --role validation --source \"OpenAlex frame sample\") before you look "
                     "at whether the strategy retrieves it. psb eval reports recall within the frame only when every "
                     "sampled record is screened and every include is in a set. Retrieval is deliberately not shown here.")}
    if ws.protocol().get("depth") != "thorough":
        body["note"] += " A frame sample costs screening time; it is meant for thorough depth."

    def data() -> dict:
        found = {"query": query, "count": total, "shown": len(rows), "retstart": 0}
        if rows:
            found["batch"] = progress.record_batch(ws, "openalex:frame", f"{progress.PURPOSES['frame']} {progress.code(progress.clean(query, 80))}",
                                                   [r["pmid"] for r in rows], total=total, query=query)["batch"]
        return found
    return progress.attach(body, ws, "search:frame", data)


def _share(count: int, total: int) -> float:
    return round(100 * count / total, 1) if total else 0.0


def profile(ws: Workspace, *, n: int, seed: int) -> dict:
    """OpenAlex topics and decades of the known set against a spread sample of the current result."""
    known = sorted({p for d in ws.sets().values() for p in d.get("pmids", [])}, key=int)
    if not known:
        raise OpenAlexError("no known records: add sets before profiling them")
    strategy = ws.strategy()
    if not strategy.blocks:
        raise OpenAlexError("strategy.json has no blocks: draft the strategy before comparing the known set with its result")
    query = full_query(strategy)
    total = ws.pubmed.search(query, retmax=0)["count"]
    sample: list[str] = []
    if total:
        per = max(1, n // PROFILE_SLICES)
        rng = random.Random(seed)
        # Several small slices at random offsets: one contiguous slice would come from a few years only.
        starts = sorted({rng.randrange(max(1, min(total, 9999) - per + 1)) for _ in range(PROFILE_SLICES)})
        for start in starts:
            sample += [p for p in ws.pubmed.search(query, retmax=per, retstart=start)["pmids"] if p not in sample]
    works = ws.openalex.by_pmids(known + [p for p in sample if p not in known])

    def tally(pmids):
        topics: dict[str, dict] = {}
        decades: dict[str, int] = {}
        for pmid in pmids:
            work = works.get(pmid)
            if not work:
                continue
            topic = topic_of(work) or {"id": "none", "name": "no OpenAlex topic"}
            row = topics.setdefault(topic["id"], {**topic, "records": 0})
            row["records"] += 1
            year = work.get("publication_year")
            if isinstance(year, int):
                decade = f"{year // 10 * 10}s"
                decades[decade] = decades.get(decade, 0) + 1
        return topics, decades

    known_topics, known_decades = tally(known)
    result_topics, result_decades = tally(sample)
    mapped_sample = sum(1 for p in sample if p in works)
    mapped_known = sum(1 for p in known if p in works)
    rows = []
    for topic_id, row in sorted(result_topics.items(), key=lambda kv: -kv[1]["records"]):
        share = _share(row["records"], mapped_sample)
        have = known_topics.get(topic_id, {}).get("records", 0)
        rows.append({"topic": topic_id, "name": row["name"], "result_sample": row["records"], "result_share_percent": share,
                     "known": have, "known_share_percent": _share(have, mapped_known),
                     "gap": have == 0 and share >= GAP_MIN_SHARE and row["records"] >= GAP_MIN_RECORDS})
    decades = []
    for decade in sorted(set(result_decades) | set(known_decades)):
        share = _share(result_decades.get(decade, 0), mapped_sample)
        decades.append({"decade": decade, "result_sample": result_decades.get(decade, 0), "result_share_percent": share,
                        "known": known_decades.get(decade, 0),
                        "gap": not known_decades.get(decade) and share >= 10.0 and result_decades.get(decade, 0) >= GAP_MIN_RECORDS})
    gaps = [r for r in rows if r["gap"]]
    old = [d for d in decades if d["gap"]]
    reading = ("This shows where the known set is thin, to decide where to look for more known records. It is not "
               "evidence of recall and must not be reported as such.")
    if gaps:
        reading += (" No known record falls in " + "; ".join(f"{g['name']} ({g['topic']}, {g['result_share_percent']}% of the "
                    "result sample)" for g in gaps[:5]) + ": look for a review or known records there.")
    if old:
        reading += (" No known record comes from " + ", ".join(d["decade"] for d in old) + ", which hold a sizeable share of "
                    "the result: older records may use earlier terminology.")
    return {"ok": True, "query": query, "result_count": total, "result_sample": len(sample), "result_sample_in_openalex": mapped_sample,
            "known": len(known), "known_in_openalex": mapped_known, "topics": rows[:20], "decades": decades,
            "gaps": [g["topic"] for g in gaps], "reading": reading}


def identifiers(ws: Workspace, values: list[str], set_names: list[str] | None) -> list[str]:
    """Origins for OpenAlex neighbours: PMIDs from sets, plus any PMID, DOI, PMCID or OpenAlex ID given."""
    found: list[str] = []
    for value in values or []:
        normalise_id(value)  # fail early on something that is not an identifier
        found.append(value.strip())
    for name in set_names or []:
        found += [p for p in ws.get_set(name).get("pmids", []) if p not in found]
    if not found:
        raise OpenAlexError("no identifiers given")
    digits = [v for v in found if v.isdigit()]
    normalize_pmids(digits)
    return found
