"""Objective vocabulary: rank candidate terms from known relevant records.

``rank`` scores each candidate by coverage (share of the relevant records that contain it) and
lift (coverage relative to its prevalence in PubMed), in the tradition of Hausner et al. 2012
and PubReMiner. Scores are discovery aids, not recall: every accepted term is still tested with
``psb eval``.
"""

from __future__ import annotations

import re
from collections import defaultdict

from .ncbi import PubMed
from .strategy import Strategy

PUBMED_TOTAL = 38_000_000
NOISE_BACKGROUND = 100_000
NOISE_COVERAGE = 0.5
GENERIC_LIFT = 10.0

TOKEN = re.compile(r"[A-Za-z0-9][A-Za-z0-9-]*")
ACRONYM = re.compile(r"\b[A-Z][A-Z0-9-]{1,9}s?\b")
STOPWORDS = set(
    """a about above after again against all also am an and any are as at be because been before
    being between both but by can could did do does doing during each few for from further had has
    have having he her here hers him his how i if in into is it its itself me more most my no nor
    not of off on once only or other our ours out over own same she should so some such than that
    the their theirs them then there these they this those through to too under until up very was
    we were what when where which while who whom why with would you your yours""".split()
)
SECTION_LABELS = set(
    """background objective objectives aim aims goal goals purpose introduction importance rationale
    context method methods methodology design setting settings participants subjects intervention
    interventions measurements outcome outcomes result results finding findings conclusion
    conclusions interpretation discussion limitation limitations registration funding keywords""".split()
)
BOUNDARY_LABELS = SECTION_LABELS - {"intervention", "interventions", "outcome", "outcomes", "design", "setting",
                                    "settings", "participants", "subjects", "context", "measurements"}
NON_TOPICAL = {
    "humans", "animals", "male", "female", "pregnancy", "infant", "infant newborn", "child",
    "child preschool", "adolescent", "adult", "young adult", "middle aged", "aged", "aged 80 and over",
    "retrospective studies", "prospective studies", "follow up studies", "cross sectional studies",
    "united states", "united kingdom", "china", "japan", "canada", "australia", "germany", "france",
    "italy", "spain", "netherlands", "india", "brazil", "europe", "asia", "africa",
}
STAT_WORDS = {"iqr", "sem", "aor"}


def normalize(text: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9]+", " ", text.lower()).split())


def record_text(record: dict) -> str:
    return " ".join([str(record.get("title", "")), str(record.get("abstract", "")), " ".join(record.get("keywords", []))])


def _phrases(record: dict) -> set[str]:
    tokens = [t.lower() for t in TOKEN.findall(record_text(record))]
    grams = set()
    for size in (1, 2, 3):
        for i in range(len(tokens) - size + 1):
            gram = tokens[i : i + size]
            if gram[0] in STOPWORDS or gram[-1] in STOPWORDS:
                continue
            if size == 1 and (len(gram[0]) < 4 or gram[0].isdigit()):
                continue
            if size > 1 and sum(t not in STOPWORDS for t in gram) < 2:
                continue
            grams.add(" ".join(gram))
    return grams


def _acronyms(record: dict) -> set[str]:
    return {m.group(0).strip("-") for m in ACRONYM.finditer(record_text(record)) if not m.group(0).isdigit() and len(m.group(0)) > 1}


def noise_reason(term: str, field: str) -> str | None:
    norm = normalize(term)
    if not norm:
        return "empty"
    if norm in NON_TOPICAL:
        return "non_topical"
    if norm in SECTION_LABELS:
        return "section_label"
    words = norm.split()
    if field == "tiab":
        tokens = term.split()
        # Only multi-word fragments: single symbols such as IL-6 or p53 are real vocabulary.
        if len(tokens) >= 2 and not any(sum(c.isalpha() for c in w) >= 3 and w.lower() not in STAT_WORDS for w in tokens):
            return "statistical"
        if words[0] in BOUNDARY_LABELS or words[-1] in BOUNDARY_LABELS:
            return "section_label"
    return None


# -- coverage by the current strategy -----------------------------------------------------------

def _term_patterns(strategy: Strategy) -> tuple[list[re.Pattern], set[str]]:
    """Regexes for the text terms of a strategy (truncation-aware) and its MeSH headings."""
    patterns: list[re.Pattern] = []
    mesh: set[str] = set()
    for block in strategy.blocks:
        for term in block.terms:
            for phrase, tag in re.findall(r'"?([^"\[\]()]+?)"?\s*\[([^\]]+)\]', term):
                tag = tag.lower()
                clean = re.split(r"\b(?:OR|AND|NOT)\b", phrase)[-1].strip()
                if tag.startswith(("mesh", "mh", "majr")):
                    mesh.add(normalize(clean))
                    continue
                words = [w for w in re.split(r"[\s-]+", clean.lower()) if w]
                if not words:
                    continue
                parts = [re.escape(w.replace("*", "")) + (r"[a-z0-9]*" if "*" in w else "") for w in words]
                patterns.append(re.compile(r"\b" + r"[\s-]+".join(parts) + r"\b"))
    return patterns, mesh


def covered(term: str, field: str, strategy: Strategy, cache: dict | None = None) -> bool:
    key = id(strategy)
    if cache is not None and key in cache:
        patterns, mesh = cache[key]
    else:
        patterns, mesh = _term_patterns(strategy)
        if cache is not None:
            cache[key] = (patterns, mesh)
    norm = normalize(term)
    if field == "mesh":
        return norm in mesh
    return any(p.search(norm) for p in patterns)


# -- ranking ------------------------------------------------------------------------------------

def candidates(records: list[dict], fields: list[str]) -> list[dict]:
    df: dict[tuple[str, str], set[str]] = defaultdict(set)
    display: dict[tuple[str, str], str] = {}
    sources: dict[tuple[str, str], set[str]] = defaultdict(set)
    for record in records:
        items: list[tuple[str, str, str]] = []
        if "tiab" in fields:
            items += [(t, "tiab", "phrase") for t in _phrases(record)]
            items += [(t, "tiab", "acronym") for t in _acronyms(record)]
            items += [(t, "tiab", "keyword") for t in record.get("keywords", [])]
        if "mesh" in fields:
            items += [(h["name"], "mesh", "mesh") for h in record.get("mesh", []) if h.get("name")]
        for term, field, source in items:
            term = " ".join(str(term).split())
            if noise_reason(term, field):
                continue
            key = (field, normalize(term))
            display.setdefault(key, term)
            sources[key].add(source)
            df[key].add(str(record.get("pmid", "")))
    total = max(len(records), 1)
    return [
        {"term": display[k], "field": k[0], "df": len(v), "coverage": round(len(v) / total, 3),
         "sources": sorted(sources[k]), "pmids": sorted(v)}
        for k, v in df.items()
    ]


def select_diverse(rows: list[dict], budget: int) -> list[dict]:
    """Spend the background-count budget round-robin across MeSH, keyword, acronym and phrase
    candidates, preferring terms that cover records not yet covered."""
    buckets: dict[str, list[dict]] = {"mesh": [], "keyword": [], "acronym": [], "phrase": []}
    for row in rows:
        name = "mesh" if row["field"] == "mesh" else next((s for s in ("keyword", "acronym", "phrase") if s in row["sources"]), "phrase")
        buckets[name].append(row)
    chosen: list[dict] = []
    covered_pmids: set[str] = set()
    active = [name for name, items in buckets.items() if items]
    while active and len(chosen) < budget:
        still = []
        for name in active:
            items = buckets[name]
            items.sort(key=lambda r: (-len(set(r["pmids"]) - covered_pmids), -r["df"], r["term"].lower()))
            row = items.pop(0)
            covered_pmids.update(row["pmids"])
            chosen.append(row)
            if items:
                still.append(name)
            if len(chosen) >= budget:
                break
        active = still
    return chosen


def background_query(term: str, field: str) -> str:
    clean = term.strip('"')
    if field == "mesh":
        return f'"{clean}"[Mesh]'
    return f'"{clean}"[tiab]' if " " in clean else f"{clean}[tiab]"


def rank(pm: PubMed, records: list[dict], strategy: Strategy, *, fields: list[str], budget: int = 40,
         min_df: int = 2, include_covered: bool = False) -> dict:
    rows = candidates(records, fields)
    memo: dict = {}
    for row in rows:
        row["in_strategy"] = covered(row["term"], row["field"], strategy, memo)
    pool = [r for r in rows if r["df"] >= min(min_df, len(records)) and (include_covered or not r["in_strategy"])]
    pool.sort(key=lambda r: (-r["df"], 0 if r["field"] == "mesh" else 1, r["term"].lower()))
    scored = select_diverse(pool, budget)
    for row in scored:
        query = background_query(row["term"], row["field"])
        background = pm.count(query)
        row["query"] = query
        row["background"] = background
        row["lift"] = round(row["coverage"] / (background / PUBMED_TOTAL), 1) if background else None
        row["noise_risk"] = background >= NOISE_BACKGROUND and row["coverage"] < NOISE_COVERAGE
        row["pmids"] = row["pmids"][:10]
        row["generic"] = row["lift"] is not None and row["lift"] < GENERIC_LIFT
    # Distinctive terms first; common words that merely co-occur (patients, study) go last.
    scored.sort(key=lambda r: (r["generic"], -r["coverage"], -(r["lift"] or 0), r["term"].lower()))
    return {
        "records": len(records),
        "candidates": len(rows),
        "already_covered": sum(r["in_strategy"] for r in rows),
        "scored": scored,
        "note": "coverage = share of the records containing the term; lift = coverage / PubMed prevalence "
                "(approximate corpus size, for ranking only); generic = lift below 10. "
                "Candidates, not additions: test each with psb eval.",
    }


def miss_report(records: list[dict], evaluation: dict, strategy: Strategy, *, per_record: int = 15) -> list[dict]:
    """For each missed known record: failing blocks, its indexing, and vocabulary the strategy lacks."""
    failing = {m["pmid"]: m for m in evaluation.get("misses", [])}
    memo: dict = {}
    report = []
    for record in records:
        pmid = str(record.get("pmid"))
        miss = failing.get(pmid, {})
        phrases = sorted(_phrases(record) | _acronyms(record), key=lambda t: (-len(t.split()), t))
        uncovered = [t for t in phrases if not noise_reason(t, "tiab") and not covered(t, "tiab", strategy, memo)]
        mesh = [h["name"] for h in record.get("mesh", [])]
        report.append(
            {
                "pmid": pmid,
                "title": record.get("title", ""),
                "failing_blocks": miss.get("failing_blocks", []),
                "lost_to_limits": miss.get("lost_to_limits", False),
                "mesh_not_in_strategy": [m for m in mesh if not covered(m, "mesh", strategy, memo) and not noise_reason(m, "mesh")],
                "keywords": record.get("keywords", []),
                "text_not_in_strategy": uncovered[:per_record],
                "indexing_status": record.get("status", ""),
            }
        )
    return report
