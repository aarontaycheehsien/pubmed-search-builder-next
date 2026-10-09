"""Evaluation harness: fixtures, scoring, baselines, and leakage checks.

A fixture is what a user would bring (a question, sometimes eligibility criteria and a few known
articles) plus a sealed answer key: the included studies of a published review. Every count is
bounded by ``as_of`` (the review's search date, or a lower bound on it), so a strategy is judged
against the PubMed that existed when the review searched.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

EVALS = Path(__file__).resolve().parent
REPO = EVALS.parent
sys.path.insert(0, str(REPO / "scripts"))

from psb.cache import Cache  # noqa: E402
from psb.ncbi import PubMed  # noqa: E402

FIXTURES = EVALS / "fixtures"
RESULTS = EVALS / "results"
SPLITS = EVALS / "splits.json"
HELDOUT_LEDGER = EVALS / "heldout-ledger.jsonl"

# Scorecard fields that would show which gold records a held-out strategy missed (or, through
# the agent's own words and audit, which records it found). Studying them is how a held-out set
# turns into a development set, so held-out scorecards never keep them.
HELDOUT_REDACTED = ("missed", "final_message")


class HarnessError(RuntimeError):
    pass


def fixture_paths() -> list[Path]:
    return sorted(FIXTURES.glob("*/*.json"))


def fixture_hash(data: dict) -> str:
    """Content hash of a fixture, independent of key order, whitespace and line endings."""
    clean = {k: v for k, v in data.items() if not k.startswith("_")}
    return hashlib.sha256(json.dumps(clean, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()


def load_splits(path: Path | None = None) -> dict:
    path = path or SPLITS
    if not path.exists():
        return {"dev": [], "heldout": {}, "retired": {}}
    data = json.loads(path.read_text(encoding="utf-8"))
    data.setdefault("dev", [])
    data.setdefault("heldout", {})
    data.setdefault("retired", {})
    return data


def split_of(topic: str, splits: dict | None = None) -> str:
    """``dev``, ``heldout``, ``retired`` or ``unassigned``."""
    splits = splits if splits is not None else load_splits()
    if topic in splits["heldout"]:
        return "heldout"
    if topic in splits["retired"]:
        return "retired"
    if topic in splits["dev"]:
        return "dev"
    return "unassigned"


def check_frozen(fixture: dict, splits: dict | None = None) -> None:
    """A held-out fixture must be byte-for-byte (canonically) what was frozen."""
    splits = splits if splits is not None else load_splits()
    frozen = splits["heldout"].get(fixture["id"])
    if frozen is None:
        return
    expected = frozen["sha256"] if isinstance(frozen, dict) else frozen
    if fixture_hash(fixture) != expected:
        raise HarnessError(f"held-out fixture {fixture['id']} changed after it was frozen; "
                           "restore it or retire it and freeze a new topic")


def load_fixture(ref: str) -> dict:
    path = Path(ref)
    if not path.is_file():
        matches = [p for p in fixture_paths() if p.stem == ref]
        if len(matches) != 1:
            raise HarnessError(f"no unique fixture named {ref!r}")
        path = matches[0]
    data = json.loads(path.read_text(encoding="utf-8"))
    check_frozen(data)
    data["_path"] = str(path)
    return data


def redact_heldout(card: dict) -> dict:
    return {k: v for k, v in card.items() if k not in HELDOUT_REDACTED}


def record_heldout_look(entry: dict, path: Path | None = None) -> None:
    """Append one line per use of a held-out topic, so every look at it is on the record."""
    path = path or HELDOUT_LEDGER
    entry = {"at": dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ"), **entry}
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False) + "\n")


# -- provenance ---------------------------------------------------------------------------------

HASH_SKIP_DIRS = {"__pycache__", ".cache", ".git", ".pytest_cache", ".venv"}


def tree_hash(root: Path) -> str:
    """Hash of every file under ``root`` (paths and contents), skipping caches and ``.env``.

    Applied to the skill as staged into a run, it identifies the exact version an agent used,
    whether or not that skill lives in git. ``.env`` holds per-machine credentials, not the skill.
    """
    digest = hashlib.sha256()
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if path.is_dir() or path.name == ".env" or path.suffix == ".pyc" or HASH_SKIP_DIRS & set(rel.parts):
            continue
        digest.update(rel.as_posix().encode("utf-8") + b"\0")
        digest.update(path.read_bytes().replace(b"\r\n", b"\n") + b"\0")
    return digest.hexdigest()


EVAL_OUTPUTS = ("results", "RESULTS.md", "heldout-ledger.jsonl", ".cache")


def git_state(path: Path) -> dict:
    """Commit and dirty flag of the git checkout containing ``path`` (scoped to ``path``).

    The eval harness's own directories are left out: runs write scorecards and the held-out ledger
    there, which says nothing about whether the skill had uncommitted edits.
    """
    def git(*args: str) -> str | None:
        try:
            done = subprocess.run(["git", "-C", str(path), *args], capture_output=True, text=True, timeout=30)
        except (OSError, subprocess.SubprocessError):
            return None
        return done.stdout.strip() if done.returncode == 0 else None

    commit = git("rev-parse", "HEAD")
    if not commit:
        return {"commit": None, "dirty": None}
    top = git("rev-parse", "--show-toplevel")
    excluded = [":(exclude,top)evals/" + name for name in EVAL_OUTPUTS] if top else []
    if top and Path(top).resolve() == path.resolve():  # a skill at the repository root
        excluded += [":(exclude,top)evals", ":(exclude,top)tests"]
    status = git("status", "--porcelain", "--", ".", *excluded)
    return {"commit": commit, "dirty": bool(status)}


# -- run status -----------------------------------------------------------------------------------

INFRA_PATTERNS = re.compile(r"usage limit|rate limit|rate_limit|quota|\b429\b|overloaded|credit balance",
                            re.IGNORECASE)
INFRA_FAST_SECONDS = 60
# A full disk stops the agent mid-run; it says so in its final message, or the run leaves little room.
DISK_PATTERNS = re.compile(r"no space left on device|not enough space on the disk|ENOSPC|disk (?:is |was )?full|disk filled",
                           re.IGNORECASE)
MIN_FREE_BYTES = 5 * 1024 ** 3   # refuse to start a run with less free space than this
LOW_DISK_BYTES = 1024 ** 3       # an undelivered run that ended with less than this counts as infra


def free_bytes(path: Path) -> int:
    path = Path(path)
    while not path.exists() and path != path.parent:
        path = path.parent
    return shutil.disk_usage(path).free
STATUSES = ("ok", "leakage", "no-delivery", "timeout", "infra")


def run_status(card: dict, errors_text: str = "", *, low_disk: bool = False) -> str:
    """Why a generated run counts (``ok``) or not.

    ``infra`` is a failure of the account or service, not of the skill: the agent exited non-zero
    within a minute, or the transcript/stderr reports a quota or rate limit and nothing was
    delivered, or the disk filled up. Infra runs are retried and left out of a skill's run count. Scorecards written
    before this field existed are classified from what they recorded.
    """
    if card.get("status") in STATUSES:
        return card["status"]
    run = card.get("run") or {}
    delivered = card.get("recall_percent") is not None
    if run.get("timed_out") and not delivered:
        return "timeout"
    crashed_before_work = run.get("returncode") not in (0, None) and card.get("workspace_started") is False
    if not delivered and ((run.get("returncode") not in (0, None) and (run.get("seconds") or 0) < INFRA_FAST_SECONDS)
                          or crashed_before_work or INFRA_PATTERNS.search(errors_text or "") or low_disk
                          or DISK_PATTERNS.search((errors_text or "") + "\n" + (card.get("final_message") or ""))):
        return "infra"
    if card.get("leakage"):
        return "leakage"
    if not delivered or card.get("valid") is False:
        return "no-delivery"
    return "ok"


def client(fixture: dict, *, use_cache: bool = True) -> PubMed:
    cache = Cache(EVALS / ".cache" / re.sub(r"[^A-Za-z0-9_.-]", "_", fixture["id"]), enabled=use_cache)
    return PubMed(cache=cache, as_of=fixture.get("as_of"))


def score(fixture: dict, query: str, *, exclude: set[str] | None = None, seen: set[str] | None = None,
          pm: PubMed | None = None) -> dict:
    """Recall of ``query`` on the fixture's gold set, within the fixture's ``as_of`` window.

    ``exclude``: gold records given to the agent (seeds), left out of the denominator.
    ``seen``: gold records the agent screened into its own sets; recall is also reported without
    them, because a build that found a record while developing is partly measuring itself.
    """
    pm = pm or client(fixture)
    query = " ".join(query.split())
    if not query:
        raise HarnessError("empty strategy")
    exclude = exclude or set()
    gold = [p for p in fixture["gold_pmids"] if p not in exclude]
    reachable = pm.existing(gold)
    found = pm.among(query, reachable)
    search = pm.search(query)
    result = {
        "as_of": fixture.get("as_of"),
        "count": search["count"],
        "gold_scored": len(gold),
        "gold_reachable": len(reachable),
        "retrieved": len(found),
        "recall_percent": round(100 * len(found) / len(reachable), 1) if reachable else None,
        "missed": sorted(reachable - found, key=int),
        "nnr": round(search["count"] / len(found), 1) if found else None,
        "translation_issues": [i["code"] for i in search["issues"]],
    }
    if seen is not None:
        unseen = reachable - seen
        result["gold_seen_by_agent"] = len(reachable & seen)
        result["unseen_retrieved"] = len(found & unseen)
        result["unseen_recall_percent"] = round(100 * len(found & unseen) / len(unseen), 1) if unseen else None
    return result


def tiab(term: str) -> str:
    clean = " ".join(str(term).split())
    return f'"{clean}"[tiab]' if (" " in clean or "-" in clean) else f"{clean}[tiab]"


def naive_query(fixture: dict) -> str:
    """The floor: each concept's terms OR-ed as [tiab] phrases, concepts AND-ed. No MeSH, no
    expansion, no testing."""
    blocks = fixture.get("naive_blocks")
    if not blocks:
        raise HarnessError(f"{fixture['id']} has no naive_blocks")
    return " AND ".join("(" + " OR ".join(tiab(t) for t in b["terms"]) + ")" for b in blocks)


def baseline_queries(fixture: dict) -> dict[str, str]:
    queries = {}
    if fixture.get("naive_blocks"):
        queries["naive"] = naive_query(fixture)
    if fixture.get("reference_strategy"):
        queries["reference"] = fixture["reference_strategy"]
    return queries


# -- leakage and provenance checks on a generated run -----------------------------------------

def _run_dir_pattern(run_dir: Path) -> re.Pattern:
    """Match the run directory's path at any JSON escaping depth: a JSON transcript that nests a
    JSON blob as a string value re-escapes each ``\\`` again, so ``\\`` may appear doubled,
    quadrupled, and so on. A run of one-or-more ``\\``/``/`` between path segments matches all of
    those depths, since escaping only ever multiplies backslash characters, never other symbols.
    """
    segments = [s for s in re.split(r"[\\/]+", str(run_dir).rstrip("\\/")) if s]
    return re.compile(r"[\\/]+".join(re.escape(s) for s in segments), re.IGNORECASE)


_INLINE_BOUND = re.compile(r'\s+AND\s+\(\s*"\d{4}/\d{2}/\d{2}"\[edat\]\s*:\s*"(\d{4})/(\d{2})/(\d{2})"\[edat\]\s*\)\s*$',
                           re.IGNORECASE)


def inline_bounded(term: str, as_of: str) -> bool:
    """True when ``term`` is ``(query) AND (".."[edat] : "<date>"[edat])`` with date <= ``as_of``.

    ``psb eval`` writes the as-of bound into the query text (``evaluate.effective_query``) rather
    than the ``maxdate`` parameter, so the delivered query carries it. That only bounds the search
    when the date range is AND-ed onto the whole query, so the prefix must be a single group.
    """
    match = _INLINE_BOUND.search(term)
    if not match or "-".join(match.groups()) > as_of:
        return False
    prefix = term[: match.start()].strip()
    if not (prefix.startswith("(") and prefix.endswith(")")):
        return False
    depth, quoted = 0, False
    for index, char in enumerate(prefix):
        if char == '"':
            quoted = not quoted
        elif not quoted and char in "()":
            depth += 1 if char == "(" else -1
            if depth == 0 and index != len(prefix) - 1:
                return False
    return depth == 0


def leakage(fixture: dict, run_dir: Path, transcript: str) -> list[str]:
    """Signs that a run saw the answer key or the literature after ``as_of``.

    The run directory is named after the fixture id (``<runs_root>/<id>/<label>``) so every tool
    call that echoes its own working directory trivially "mentions" the id. Strip the run
    directory's own path before scanning, whatever form it takes in the transcript.
    """
    problems = []
    cleaned = _run_dir_pattern(run_dir).sub("", transcript)
    lowered = cleaned.lower()
    for marker in (fixture["id"].lower(), "clef tar", "synergy dataset", "qrels", "gold_pmids", "evals/fixtures"):
        if marker and marker in lowered:
            problems.append(f"transcript mentions {marker!r}")
    # The separate screening context's request rows keep their parameters only in its private log;
    # log.jsonl holds their accounting rows, which have no params and so are never counted twice.
    logs = [path for path in (run_dir / "work" / "log.jsonl", run_dir / "work" / "screening" / "log.jsonl")
            if path.exists()]
    if logs and fixture.get("as_of"):
        undated = 0
        for line in (row for path in logs for row in path.read_text(encoding="utf-8").splitlines()):
            if not line.strip():
                continue
            try:
                entry = json.loads(line)
            except ValueError:
                continue  # a line torn by a concurrent writer in the agent's own session; skip it
            params = entry.get("params") or {}
            term = str(params.get("term", ""))
            if entry.get("endpoint") == "esearch.fcgi" and params.get("db") == "pubmed" and "maxdate" not in params \
                    and "[doi]" not in term and not inline_bounded(term, fixture["as_of"]):
                undated += 1
        if undated:
            problems.append(f"{undated} PubMed searches ran without the as_of bound")
    return problems


def gold_seen(fixture: dict, run_dir: Path) -> set[str]:
    """Gold records the agent put into its own known-record sets (development and comparison).
    Held-out records are not sets, so they are never counted here: see ``gold_reserved``."""
    seen: set[str] = set()
    for path in (run_dir / "work" / "sets").glob("*.json"):
        try:
            seen.update(json.loads(path.read_text(encoding="utf-8")).get("pmids", []))
        except ValueError:
            continue
    return seen & set(fixture["gold_pmids"])


def gold_reserved(fixture: dict, run_dir: Path) -> set[str]:
    """Gold records the run held out for its one held-out test (none once released for repair)."""
    work = run_dir / "work"
    try:
        allocation = json.loads((work / "allocation.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return set()
    log = work / "allocation-log.jsonl"
    if log.exists() and '"type": "release"' in log.read_text(encoding="utf-8"):
        return set()
    held = {str(p) for u in allocation.get("units") or [] if isinstance(u, dict) and u.get("purpose") == "holdout"
            for p in u.get("members") or []}
    return held & set(fixture["gold_pmids"])


def screening_contexts(run_dir: Path) -> dict[str, int]:
    """How many screening decisions were made in the separate context and by the builder; a run with
    no separate context cannot hold anything out, which explains an all-development allocation."""
    counts = {"separate": 0, "builder": 0}
    path = run_dir / "work" / "screening.jsonl"
    if not path.exists():
        return counts
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            row = json.loads(line)
        except ValueError:
            continue
        if isinstance(row, dict):
            counts["separate" if row.get("context") == "separate" else "builder"] += 1
    return counts


def diagnostic_handoff(run_dir: Path) -> dict | None:
    """The query and blocker codes of an undelivered run's ``diagnostic-audit.md`` (psb report
    --diagnostic, or a gate refusal). None when there is no parseable handoff."""
    path = run_dir / "work" / "diagnostic-audit.md"
    delivered = run_dir / "work" / "final-query.txt"
    manifest = run_dir / "work" / "validation-manifest.json"
    # A delivery made after the last diagnostic and then invalidated by a later edit: its query is the
    # latest one, and the old diagnostic's blockers no longer describe the run.
    if delivered.exists() and manifest.exists() and (not path.exists() or manifest.stat().st_mtime > path.stat().st_mtime):
        query = delivered.read_text(encoding="utf-8").strip()
        return {"query": query, "blockers": ["delivery_stale"]} if query else None
    try:
        text = path.read_text(encoding="utf-8")
        data = json.loads(text[text.index("```json") + len("```json"):text.rindex("```")])
    except (OSError, ValueError):
        return None
    query = (data.get("evaluation") or {}).get("query") if isinstance(data, dict) else None
    if not isinstance(query, str) or not query.strip():
        return None
    return {"query": query, "blockers": sorted({str(b.get("code")) for b in data.get("blockers") or [] if isinstance(b, dict)})}
