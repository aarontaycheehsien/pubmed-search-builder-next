"""Objective vocabulary: rank candidate terms from known relevant records.

``rank`` scores each candidate by coverage (share of the relevant records that contain it) and
lift (coverage relative to its prevalence in PubMed), in the tradition of Hausner et al. 2012
and PubReMiner. Scores are discovery aids, not recall: every accepted term is still tested with
``psb eval``.
"""

from __future__ import annotations

import re
from collections import defaultdict

from . import syntax
from .ncbi import PubMed
from .strategy import Block, Strategy

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


def _grams(text: str) -> set[str]:
    tokens = [t.lower() for t in TOKEN.findall(text)]
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


def _phrases(record: dict) -> set[str]:
    return _grams(record_text(record))


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


# -- why a block missed a record ----------------------------------------------------------------

TEXT_FIELDS = {"tiab", "ti", "ab", "tw", "ot"}
MAX_GAP = 3    # widest gap (words between a phrase's words) still reported as a near miss
MIN_EMBED = 5  # shorter stems sit inside too many unrelated words (rate: moderate, accurate)
CAUSES = {
    "phrase_gap": "The block has the phrase, but the record separates or reorders its words, or uses only part "
                  "of it. Test the suggested proximity or shorter phrase with psb eval.",
    "embedded_stem": "The block's word occurs only inside a longer word (virus: rotavirus). PubMed cannot "
                     "truncate on the left: name those words, or the family they belong to, in the block.",
    "no_abstract": "The record has no abstract, so only its title and MeSH can match. Check mesh_not_in_strategy.",
    "no_block_wording": "Nothing in the title, abstract or keywords matches or nearly matches the block. Read the "
                        "record. If it names the concept in other words, add them (text_not_in_strategy, "
                        "mesh_not_in_strategy). If it does not name the concept at all, no term can reach it while "
                        "this block is AND-ed: record it as out of reach instead of widening the block.",
}
_WORD = re.compile(r"[a-z0-9]+")
_DISTANCE = re.compile(r":~(\d+)$")


def _matcher(word: str):
    if "*" not in word:
        return lambda token: token == word
    pattern = re.compile("[a-z0-9]*".join(re.escape(part) for part in word.split("*")) + "$")
    return lambda token: bool(pattern.match(token))


def text_atoms(block: Block) -> list[dict]:
    """The block's free-text terms as word lists: ``"hip pain"[tiab:~2]`` -> hip, pain, distance 2."""
    found = []
    for term in block.terms:
        for atom in syntax.atoms(term):
            if atom["field"] not in TEXT_FIELDS:
                continue
            words = [w for w in (re.sub(r"[^a-z0-9*]", "", raw) for raw in re.split(r"[\s-]+", atom["text"].lower()))
                     if w.strip("*")]
            if not words:
                continue
            distance = _DISTANCE.search(atom["tag"].replace(" ", ""))
            found.append({"term": f"{atom['text']}[{atom['tag']}]", "words": words, "field": atom["field"],
                          "distance": int(distance[1]) if distance else None, "matchers": [_matcher(w) for w in words]})
    return found


def _segments(record: dict) -> list[list[str]]:
    """Title, abstract and each keyword as separate token runs: a phrase cannot span two of them."""
    parts = [str(record.get("title", "")), str(record.get("abstract", "")), *map(str, record.get("keywords", []))]
    return [tokens for tokens in (_WORD.findall(part.lower()) for part in parts) if tokens]


def _adjacent(tokens: list[str], matchers: list) -> int | None:
    size = len(matchers)
    return next((i for i in range(len(tokens) - size + 1) if all(m(tokens[i + k]) for k, m in enumerate(matchers))), None)


def _nearest(tokens: list[str], matchers: list) -> tuple[int, int] | None:
    """The smallest window that holds a different token for every word of the phrase, in any order."""
    positions = [[i for i, token in enumerate(tokens) if m(token)] for m in matchers]
    if not all(positions):
        return None
    best = None
    for left in sorted({p for plist in positions for p in plist}):
        used: set[int] = set()
        for plist in positions:
            pick = next((p for p in plist if p >= left and p not in used), None)
            if pick is None:
                break
            used.add(pick)
        else:
            if left in used and (best is None or max(used) - left < best[1] - best[0]):
                best = (left, max(used))
    return best


def _phrase_gap(segments: list[list[str]], atom: dict) -> dict | None:
    """The phrase's words all occur close together, but not the way the term requires."""
    matchers = atom["matchers"]
    if len(matchers) < 2:
        return None
    best = None
    for tokens in segments:
        if atom["distance"] is None and _adjacent(tokens, matchers) is not None:
            return None  # present as written: whatever failed, it was not the wording
        window = _nearest(tokens, matchers)
        if window:
            gap = window[1] - window[0] + 1 - len(matchers)
            if best is None or gap < best["words_between"]:
                best = {"term": atom["term"], "found": " ".join(tokens[window[0]: window[1] + 1]), "words_between": gap}
    if best is None or best["words_between"] > MAX_GAP or (atom["distance"] is not None and best["words_between"] <= atom["distance"]):
        return None
    if any("*" in word for word in atom["words"]):
        best["try"] = ("PubMed ignores proximity when a phrase has a wildcard: list the variants as proximity "
                       f"phrases ([tiab:~{best['words_between']}]), or search the distinctive word on its own")
    else:
        field = atom["field"] if atom["field"] in {"ti", "tiab"} else "tiab"
        best["try"] = f"\"{' '.join(atom['words'])}\"[{field}:~{best['words_between']}]"
    return best


def _partial_phrase(segments: list[list[str]], atom: dict) -> dict | None:
    """Part of a three-word-or-longer phrase is present as written; the rest is nowhere near it."""
    words, matchers = atom["words"], atom["matchers"]
    for size in range(len(words) - 1, 1, -1):
        for start in range(len(words) - size + 1):
            if any(_adjacent(tokens, matchers[start: start + size]) is not None for tokens in segments):
                part = words[start: start + size]
                return {"term": atom["term"], "matched": " ".join(part), "absent": words[:start] + words[start + size:],
                        "try": f"\"{' '.join(part)}\"[tiab]"}
    return None


def _embedded_stem(segments: list[list[str]], atom: dict) -> dict | None:
    """A one-word term that occurs only inside longer words, which right truncation cannot reach."""
    if len(atom["words"]) != 1:
        return None
    stem = atom["words"][0].rstrip("*")
    if "*" in stem or len(stem) < MIN_EMBED:
        return None
    inside = sorted({token for tokens in segments for token in tokens if stem in token and not token.startswith(stem)})
    return {"term": atom["term"], "inside": inside[:8]} if inside else None


def diagnose_block(record: dict, block: Block) -> dict:
    """Why this block's free text did not match the record, from the record's own wording."""
    segments = _segments(record)
    atoms = text_atoms(block)
    gaps = [g for g in (_phrase_gap(segments, a) for a in atoms) if g]
    near = {g["term"] for g in gaps}
    partial = [p for p in (_partial_phrase(segments, a) for a in atoms if a["term"] not in near and len(a["words"]) >= 3) if p]
    embedded = [e for e in (_embedded_stem(segments, a) for a in atoms) if e]
    cause = ("phrase_gap" if gaps or partial else "embedded_stem" if embedded
             else "no_abstract" if not str(record.get("abstract", "")).strip() else "no_block_wording")
    found = {"block": block.id, "cause": cause}
    for key, rows in (("phrase_gaps", gaps), ("partial_phrases", partial), ("embedded_stems", embedded)):
        if rows:
            found[key] = sorted(rows, key=lambda r: (r.get("words_between", 0), r["term"]))[:5]
    return found


def _uncovered_text(record: dict, strategy: Strategy, memo: dict, limit: int) -> list[str]:
    """Wording the strategy lacks: author keywords and the title first, the abstract after them.

    A record yields hundreds of abstract n-grams; listed alphabetically they bury the few words
    that say what the paper is about.
    """
    def by_size(grams: set[str]) -> list[str]:
        return sorted(grams, key=lambda t: ({2: 0, 1: 1}.get(len(t.split()), 2), t))

    ordered = [" ".join(str(k).lower().split()) for k in record.get("keywords", [])]
    ordered += by_size(_grams(str(record.get("title", ""))))
    ordered += sorted(a.lower() for a in _acronyms(record))
    ordered += by_size(_grams(str(record.get("abstract", ""))))
    kept: list[str] = []
    for term in ordered:
        if term and term not in kept and not noise_reason(term, "tiab") and not covered(term, "tiab", strategy, memo):
            kept.append(term)
            if len(kept) >= limit:
                break
    return kept


def miss_report(records: list[dict], evaluation: dict, strategy: Strategy, *, per_record: int = 15) -> list[dict]:
    """For each missed known record: failing blocks, why each failed, and vocabulary the strategy lacks."""
    failing = {m["pmid"]: m for m in evaluation.get("misses", [])}
    blocks = {block.id: block for block in strategy.blocks}
    memo: dict = {}
    report = []
    for record in records:
        pmid = str(record.get("pmid"))
        miss = failing.get(pmid, {})
        mesh = [h["name"] for h in record.get("mesh", [])]
        report.append(
            {
                "pmid": pmid,
                "title": record.get("title", ""),
                "failing_blocks": miss.get("failing_blocks", []),
                "lost_to_limits": miss.get("lost_to_limits", False),
                "diagnosis": [diagnose_block(record, blocks[b]) for b in miss.get("failing_blocks", []) if b in blocks],
                "mesh_not_in_strategy": [m for m in mesh if not covered(m, "mesh", strategy, memo) and not noise_reason(m, "mesh")],
                "keywords": record.get("keywords", []),
                "text_not_in_strategy": _uncovered_text(record, strategy, memo, per_record),
                "has_abstract": bool(str(record.get("abstract", "")).strip()),
                "has_mesh": bool(mesh),
                "indexing_status": record.get("status", ""),
            }
        )
    return report
