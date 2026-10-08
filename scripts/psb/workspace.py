"""A run workspace: the single source of truth for one search build.

    protocol.json    scope: question, concepts and their roles, eligibility, limits, as_of
    strategy.json    the current strategy (see strategy.py)
    sets/<name>.json PMID sets with a purpose (development or comparison)
    records.jsonl    fetched PubMed records, one per line, keyed by PMID
    allocation.json  the frozen split of the eligible pool into development and held-out units
    allocation-log.jsonl  late companions, re-binding and release after the freeze
    exposure.jsonl   records whose content or retrieval the builder has seen
    screening/       the separate screening context's private store (records, cache, reasons)
    holdout/         held-out test receipts
    history/         each evaluated strategy version with its evaluation
    critic/          critic packets and rounds
    log.jsonl        every command and NCBI request, appended automatically
    .cache/          NCBI responses for this workspace only

Everything else (reports, audits) is derived from these files and never read back as input.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import time
import uuid
from contextlib import contextmanager
from pathlib import Path

from .cache import Cache
from .config import read_env
from .ncbi import PubMed
from .strategy import Strategy

MARKER = "protocol.json"
# What a set of known records is for. Held-out records are never a set: allocation.json holds them,
# so no command that lists, mines or evaluates sets can reach them.
PURPOSES = {
    "development": "used for term mining, diagnosing misses and repeated retrieval checks; not independent",
    "comparison": "outside the allocation pool; checked and reported separately, not mined by default, "
                  "never a held-out test",
}
# Sets written before held-out testing carry a role. They are mapped when read and never rewritten,
# so a legacy delivery still verifies. A legacy validation set was scored at every evaluation, so it
# is a comparison list, never an independent test.
LEGACY_ROLES = {"seed": "development", "relevant": "development", "validation": "comparison", "benchmark": "comparison"}
LEGACY_NOTE = "legacy: consulted during development"
ORIGINS = ("user-supplied", "prior-review", "pilot-search", "similar-articles", "citation-backward", "citation-forward")

PROTOCOL_TEMPLATE = {
    "question": "",
    "framework": "",
    "concepts": [],
    "eligibility": {"include": [], "exclude": []},
    "limits": [],
    "as_of": None,
    "depth": "standard",
    "scope_confirmed": False,
    "notes": "",
}
STRATEGY_TEMPLATE = {"blocks": [], "combine": None, "limits": []}


class WorkspaceError(RuntimeError):
    pass


def purpose_of(data: dict) -> str:
    """A set's purpose, mapping a legacy role; ``unknown`` when neither is recognised."""
    purpose = data.get("purpose")
    if isinstance(purpose, str) and purpose in PURPOSES:
        return purpose
    role = data.get("role")
    return LEGACY_ROLES.get(role, "unknown") if isinstance(role, str) else "unknown"


def purpose_label(data: dict) -> str:
    """How a set's use is described in messages and the audit."""
    purpose = purpose_of(data)
    role = None if data.get("purpose") else data.get("role")
    if isinstance(role, str) and role in LEGACY_ROLES:
        return f"{purpose} ({LEGACY_NOTE} as a {role} set)"
    return purpose


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except FileNotFoundError:
        raise WorkspaceError(f"missing {path.name}") from None
    except ValueError as exc:
        raise WorkspaceError(f"{path.name} is not valid JSON: {exc}") from None


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                row = json.loads(line)
            except ValueError:
                continue  # a line torn by a concurrent write
            if isinstance(row, dict):
                rows.append(row)
    return rows


def append_jsonl(path: Path, entry: dict) -> None:
    """One os.write to an O_APPEND descriptor, so concurrent writers cannot interleave a line."""
    path.parent.mkdir(parents=True, exist_ok=True)
    line = (json.dumps(entry, ensure_ascii=False) + "\n").encode("utf-8")
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
    try:
        os.write(fd, line)
    finally:
        os.close(fd)


read_jsonl = _read_jsonl


def find_root(start: str | Path | None = None) -> Path:
    explicit = start or os.environ.get("PSB_WORKSPACE")
    if explicit:
        root = Path(explicit).expanduser().resolve()
        if not (root / MARKER).is_file():
            raise WorkspaceError(f"{root} is not a workspace (no {MARKER}); run `psb init` first")
        return root
    here = Path.cwd().resolve()
    for candidate in (here, *here.parents):
        if (candidate / MARKER).is_file():
            return candidate
    raise WorkspaceError("no workspace found; run `psb init <dir>` or pass --workspace")


def normalize_pmids(values) -> list[str]:
    pmids: list[str] = []
    for value in values:
        for piece in str(value).replace(",", " ").split():
            piece = piece.strip()
            if not piece.isdigit() or not piece.strip("0"):
                raise WorkspaceError(f"not a PMID: {piece!r}")
            piece = piece.lstrip("0")
            if piece not in pmids:
                pmids.append(piece)
    return pmids


class Workspace:
    def __init__(self, root: Path, *, use_cache: bool = True) -> None:
        self.root = root
        self.use_cache = use_cache and read_env("PSB_CACHE", "on").lower() not in {"off", "0", "false"}
        self._pubmed: PubMed | None = None

    # -- creation ------------------------------------------------------------------------

    @classmethod
    def create(cls, root: Path, question: str) -> "Workspace":
        root = root.expanduser().resolve()
        if (root / MARKER).exists():
            raise WorkspaceError(f"{root} already has a {MARKER}")
        root.mkdir(parents=True, exist_ok=True)
        protocol = dict(PROTOCOL_TEMPLATE, question=question.strip())
        write_json(root / MARKER, protocol)
        write_json(root / "strategy.json", STRATEGY_TEMPLATE)
        for name in ("sets", "history", "critic"):
            (root / name).mkdir(exist_ok=True)
        (root / ".gitignore").write_text(".cache/\nscreening/.cache/\n", encoding="utf-8")
        workspace = cls(root)
        workspace.log({"type": "init", "question": question.strip()})
        return workspace

    # -- files ---------------------------------------------------------------------------

    def protocol(self) -> dict:
        data = read_json(self.root / MARKER)
        if not isinstance(data, dict):
            raise WorkspaceError("protocol.json must be an object")
        return data

    def strategy_text(self) -> str:
        return (self.root / "strategy.json").read_text(encoding="utf-8")

    def strategy(self) -> Strategy:
        return Strategy.from_dict(read_json(self.root / "strategy.json"))

    def log(self, entry: dict) -> None:
        # A buffered text-mode append can split into more than one underlying write, so two
        # `psb` processes running at once (the agent backgrounding commands, or a second
        # terminal) can interleave and corrupt a line. A single os.write of the encoded bytes to
        # an O_APPEND descriptor is one kernel call, which the OS does not interleave with
        # another process's own single call to the same file.
        line = (json.dumps({"ts": now(), **entry}, ensure_ascii=False) + "\n").encode("utf-8")
        fd = os.open(self.root / "log.jsonl", os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
        try:
            os.write(fd, line)
        finally:
            os.close(fd)

    def log_entries(self) -> list[dict]:
        path = self.root / "log.jsonl"
        if not path.exists():
            return []
        entries = []
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                entries.append(json.loads(line))
            except ValueError:
                continue  # a line torn by a concurrent write; skip rather than fail the reader
        return entries

    @property
    def pubmed(self) -> PubMed:
        if self._pubmed is None:
            # PSB_AS_OF (set by the eval harness) overrides the protocol, so a run cannot see
            # literature added after the source review's search, whatever the agent writes.
            as_of = os.environ.get("PSB_AS_OF") or self.protocol().get("as_of") or None
            cache = Cache(self.root / ".cache", enabled=self.use_cache)
            self._pubmed = PubMed(cache=cache, log=self.log, as_of=as_of)
        self._pubmed.as_of = os.environ.get("PSB_AS_OF") or self.protocol().get("as_of") or None
        return self._pubmed

    @pubmed.setter
    def pubmed(self, client: PubMed) -> None:
        self._pubmed = client

    # -- sets ----------------------------------------------------------------------------

    def set_path(self, name: str) -> Path:
        if not name.replace("-", "_").isidentifier():
            raise WorkspaceError(f"invalid set name {name!r}")
        return self.root / "sets" / f"{name}.json"

    def sets(self) -> dict[str, dict]:
        found = {}
        for path in sorted((self.root / "sets").glob("*.json")):
            data = read_json(path)
            if isinstance(data, dict):
                found[path.stem] = data
        return found

    def get_set(self, name: str) -> dict:
        path = self.set_path(name)
        if not path.exists():
            raise WorkspaceError(f"no set named {name!r}")
        return read_json(path)  # type: ignore[return-value]

    def save_set(self, name: str, purpose: str, pmids: list[str], *, source: str = "", note: str = "",
                 origin: list[str] | None = None) -> dict:
        """Write a set. A legacy role name (seed, relevant, validation, benchmark) is accepted and
        stored as its purpose. No set can be held out: only ``psb allocate`` reserves records."""
        purpose = LEGACY_ROLES.get(purpose, purpose)
        if purpose == "holdout":
            raise WorkspaceError("held-out records are reserved only by psb allocate, never by a set")
        if purpose not in PURPOSES:
            raise WorkspaceError(f"purpose must be one of {', '.join(PURPOSES)}")
        bad = [o for o in origin or [] if o not in ORIGINS]
        if bad:
            raise WorkspaceError(f"origin must be one of {', '.join(ORIGINS)}")
        overlap = {
            other: sorted(set(pmids) & set(data.get("pmids", [])))
            for other, data in self.sets().items()
            if other != name and purpose_of(data) != purpose
        }
        data = {"purpose": purpose, "pmids": pmids, "source": source, "note": note,
                "origin": sorted(set(origin or [])), "updated": now()}
        write_json(self.set_path(name), data)
        self.log({"type": "set", "name": name, "purpose": purpose, "size": len(pmids)})
        return {"name": name, **data, "overlap_with_other_purposes": {k: v for k, v in overlap.items() if v}}

    def set_pmids(self, *purposes: str) -> set[str]:
        return {p for d in self.sets().values() if purpose_of(d) in purposes for p in d.get("pmids", [])}

    def mining_pmids(self, *, include_comparison: bool = False) -> list[str]:
        """Known records that term mining may use: development sets, plus comparison lists only when
        asked. Held-out records are never in a set, so they can never be mined."""
        purposes = ("development", "comparison") if include_comparison else ("development",)
        return sorted(self.set_pmids(*purposes) - self.reserved_pmids(), key=int)

    # -- allocation ----------------------------------------------------------------------

    def allocation(self) -> dict | None:
        """The frozen allocation, or None before ``psb allocate``. The file never changes once written."""
        path = self.root / "allocation.json"
        if not path.exists():
            return None
        data = read_json(path)
        if not isinstance(data, dict) or not isinstance(data.get("units"), list):
            raise WorkspaceError("allocation.json must be an object with a units list")
        return data

    def allocation_events(self) -> list[dict]:
        """Events after the freeze: late companions, re-binding and release."""
        return _read_jsonl(self.root / "allocation-log.jsonl")

    def released(self) -> dict | None:
        """The release that returned the held-out records to development, if any."""
        return next((e for e in reversed(self.allocation_events()) if e.get("type") == "release"), None)

    def reserved_pmids(self) -> set[str]:
        """Records the builder may not see: held-out members and late companions, until released."""
        allocation = self.allocation()
        if not allocation or self.released():
            return set()
        events = self.allocation_events()
        removed = {str(p) for e in events if e.get("type") == "rebind" for p in e.get("removed", [])}
        held = {str(p) for u in allocation["units"] if isinstance(u, dict) and u.get("purpose") == "holdout"
                for p in u.get("members", [])}
        late = {str(e.get("pmid")) for e in events if e.get("type") == "late-companion"}
        return (held - removed) | late

    # -- records -------------------------------------------------------------------------

    def _records_path(self, private: bool) -> Path:
        return self.root / "screening" / "records.jsonl" if private else self.root / "records.jsonl"

    def records(self, *, private: bool = False) -> dict[str, dict]:
        path = self._records_path(private)
        if not path.exists():
            return {}
        found = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                record = json.loads(line)
                found[str(record.get("pmid"))] = record
        return found

    def ensure_records(self, pmids: list[str], *, private: bool = False) -> dict[str, dict]:
        """Records for ``pmids``, fetching and storing any not yet stored.

        ``private`` is the separate screening context's store (screening/records.jsonl with its own
        NCBI cache). The builder's commands never read it, so screening there exposes nothing."""
        stored = self.records(private=private)
        missing = [p for p in pmids if p not in stored]
        if missing:
            with self.private_cache(private):
                fetched = self.pubmed.fetch(missing)
            path = self._records_path(private)
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("a", encoding="utf-8") as handle:
                for record in fetched:
                    handle.write(json.dumps(record, ensure_ascii=False) + "\n")
                    stored[str(record["pmid"])] = record
        return {p: stored[p] for p in pmids if p in stored}

    @contextmanager
    def private_cache(self, private: bool = True):
        """Route NCBI responses to the screening store's own cache while ``private``."""
        if not private:
            yield
            return
        client = self.pubmed
        shared = client.cache
        client.cache = Cache(self.root / "screening" / ".cache", enabled=self.use_cache)
        try:
            yield
        finally:
            client.cache = shared

    # -- history -------------------------------------------------------------------------

    def versions(self) -> list[dict]:
        return [read_json(p) for p in sorted((self.root / "history").glob("v*.json"))]  # type: ignore[misc]

    def save_version(self, evaluation: dict, note: str) -> dict:
        versions = self.versions()
        number = len(versions) + 1
        entry = {
            "version": number,
            "created": now(),
            "note": note,
            "strategy_sha256": sha256_text(json.dumps(self.strategy().to_dict(), sort_keys=True)),
            "protocol_sha256": sha256_text(json.dumps(self.protocol(), sort_keys=True)),
            "strategy": self.strategy().to_dict(),
            "evaluation": evaluation,
        }
        write_json(self.root / "history" / f"v{number:03d}.json", entry)
        self.log({"type": "version", "version": number, "note": note})
        return entry


    def save_attempt(self, evaluation: dict, *, purpose: str = "eval") -> dict:
        attempt_id = f"{time.time_ns()}-{uuid.uuid4().hex[:8]}"
        entry = {"attempt_id": attempt_id, "created": now(), "purpose": purpose, "evaluation": evaluation}
        write_json(self.root / "attempts" / f"{attempt_id}.json", entry)
        self.log({"type": "evaluation_attempt", "attempt_id": attempt_id, "ok": evaluation.get("ok")})
        return entry

    def attempts(self) -> list[dict]:
        return [read_json(p) for p in sorted((self.root / "attempts").glob("*.json"))]
