"""A run workspace: the single source of truth for one search build.

    protocol.json    scope: question, concepts and their roles, eligibility, limits, as_of
    strategy.json    the current strategy (see strategy.py)
    sets/<name>.json PMID sets with a role
    records.jsonl    fetched PubMed records, one per line, keyed by PMID
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
from pathlib import Path

from .cache import Cache
from .config import read_env
from .ncbi import PubMed
from .strategy import Strategy

MARKER = "protocol.json"
ROLES = {
    "seed": "user-supplied known relevant records; used for development, not independent",
    "relevant": "records screened relevant during the build; used for development, not independent",
    "validation": "relevant records held out from term mining; semi-independent",
    "benchmark": "included studies of a prior review; external benchmark",
}
MINING_ROLES = {"seed", "relevant"}

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


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise WorkspaceError(f"missing {path.name}") from None
    except ValueError as exc:
        raise WorkspaceError(f"{path.name} is not valid JSON: {exc}") from None


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)


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
        (root / ".gitignore").write_text(".cache/\n", encoding="utf-8")
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

    def write_protocol(self, protocol: dict) -> None:
        write_json(self.root / MARKER, protocol)

    def write_strategy(self, strategy: Strategy) -> None:
        write_json(self.root / "strategy.json", strategy.to_dict())

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

    def save_set(self, name: str, role: str, pmids: list[str], *, source: str = "", note: str = "") -> dict:
        if role not in ROLES:
            raise WorkspaceError(f"role must be one of {', '.join(ROLES)}")
        overlap = {
            other: sorted(set(pmids) & set(data.get("pmids", [])))
            for other, data in self.sets().items()
            if other != name and data.get("role") != role
        }
        data = {"role": role, "pmids": pmids, "source": source, "note": note, "updated": now()}
        write_json(self.set_path(name), data)
        self.log({"type": "set", "name": name, "role": role, "size": len(pmids)})
        return {"name": name, **data, "overlap_with_other_roles": {k: v for k, v in overlap.items() if v}}

    def mining_pmids(self) -> list[str]:
        """Known relevant records that term mining may use (never validation or benchmark)."""
        held_out = {p for d in self.sets().values() if d.get("role") not in MINING_ROLES for p in d.get("pmids", [])}
        pmids = [p for d in self.sets().values() if d.get("role") in MINING_ROLES for p in d.get("pmids", [])]
        return sorted({p for p in pmids if p not in held_out}, key=int)

    # -- records -------------------------------------------------------------------------

    def records(self) -> dict[str, dict]:
        path = self.root / "records.jsonl"
        if not path.exists():
            return {}
        found = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                record = json.loads(line)
                found[str(record.get("pmid"))] = record
        return found

    def ensure_records(self, pmids: list[str]) -> dict[str, dict]:
        """Records for ``pmids``, fetching and storing any not yet in records.jsonl."""
        stored = self.records()
        missing = [p for p in pmids if p not in stored]
        if missing:
            fetched = self.pubmed.fetch(missing)
            with (self.root / "records.jsonl").open("a", encoding="utf-8") as handle:
                for record in fetched:
                    handle.write(json.dumps(record, ensure_ascii=False) + "\n")
                    stored[str(record["pmid"])] = record
        return {p: stored[p] for p in pmids if p in stored}

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
