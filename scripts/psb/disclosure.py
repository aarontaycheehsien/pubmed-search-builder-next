"""What builder-facing output may say about the separate screening context.

Three things are kept apart:

- the actual agent context: a separate screener can read papers; a flag never creates isolation;
- recorded exposure: each screening row's context and ``exposure.jsonl``; nothing here writes or
  defaults it, and private presentation never makes an exposed record unexposed;
- presentation restriction: what a progress message, or a replayable public row, may say. It can be
  stricter than a record's exposure.

An invocation is *restricted* when it serves the separate context. The policy is a pure function of
the parsed arguments, decided before a workspace is opened, anything is logged or any request is
made, and it lives on that invocation's ``args`` only. A restricted invocation's progress gives only
fixed operation labels, whether it completed, a processed-record count, the cumulative number of
screening decisions with the budget, and that allocation is pending. Its NCBI requests use the
private cache, and its ``log.jsonl`` rows keep accounting fields only: the full rows go to
``screening/log.jsonl``.

``psb progress list`` and ``psb log --tail`` return public projections: explicitly chosen fields only.
Rows written before this policy carry no ``disclosure_version`` and are classified by their fixed
event or type name, never by their text. The files themselves are never rewritten.
"""

from __future__ import annotations

DISCLOSURE_VERSION = 1
DISCOVERY_COMMANDS = ("count", "sample", "fetch", "neighbors", "resolve")
# Commands whose older log rows may carry a private query, seed or decisions file in their argv.
PRIVATE_COMMANDS = (*DISCOVERY_COMMANDS, "screen")
# The fields a restricted invocation leaves in log.jsonl: enough for request and cache accounting.
LOG_FIELDS = ("ts", "type", "command", "endpoint", "cache", "disclosure_version")
MESSAGE_FIELDS = ("seq", "event", "step", "text")
# Older progress rows that never described private discovery or screening.
SHOWN_EVENTS = frozenset({
    "intake-request", "stage:intake", "stage:scope", "stage:vocabulary", "stage:test", "stage:critic",
    "stage:deliver", "set", "eval", "terms-rank", "terms-miss", "report", "allocation", "allocation-preview",
    "holdout-test", "holdout-release"})
SHOWN_PREFIXES = ("critic-",)
OMITTED_NOTE = ("Earlier entries that may describe discovery or screening are not shown; they are counted in "
                "omitted.")
# Fixed labels for what a restricted invocation was doing; never built from its arguments.
OPERATIONS = {"count": "A search count", "sample": "A candidate search", "fetch": "Record retrieval",
              "neighbors": "A neighbour search", "resolve": "Identifier resolution", "screen": "Screening"}


def restricted(args) -> bool:
    """Whether this invocation's builder-facing output is restricted. ``screen`` is restricted for the
    separate context or any decisions file, decided before the file is read; its rows keep their own
    context."""
    command = getattr(args, "command", None)
    if command in DISCOVERY_COMMANDS:
        return bool(getattr(args, "screening", False))
    if command == "screen":
        return getattr(args, "context", None) == "separate" or bool(getattr(args, "file", None))
    return False


def operation(args) -> str:
    return OPERATIONS.get(getattr(args, "command", None), "A separate-context command")


def accounting(row: dict) -> dict:
    """A log row reduced to the accounting fields: no arguments, parameters, bodies or error text."""
    return {k: row[k] for k in LOG_FIELDS if k in row}


def command_tokens(argv) -> list[str]:
    """The non-option words of a logged argv, without the values of the global path options."""
    words, skip = [], False
    for token in argv or []:
        if skip:
            skip = False
        elif token in {"--workspace", "--env-file"}:
            skip = True
        elif not str(token).startswith("-"):
            words.append(str(token))
    return words


def legacy_command(argv, vocabulary: dict[str, frozenset]) -> list[str] | None:
    """The canonical words of an older command row: the command and its known subcommand or stage."""
    tokens = command_tokens(argv)
    if not tokens or tokens[0] not in vocabulary:
        return None
    words = tokens[:1]
    if len(tokens) > 1 and tokens[1] in vocabulary[tokens[0]]:
        words.append(tokens[1])
    return words


def _marked(row: dict) -> bool:
    return row.get("disclosure_version") == DISCLOSURE_VERSION


def public_message(row: dict, known: set[str] | frozenset) -> dict | None:
    """A progress row as ``psb progress list`` shows it, or None when it is omitted."""
    event, text = row.get("event"), row.get("text")
    if not isinstance(event, str) or not isinstance(text, str):
        return None
    shown = event in known if _marked(row) else event in SHOWN_EVENTS or event.startswith(SHOWN_PREFIXES)
    return {k: row[k] for k in MESSAGE_FIELDS if k in row} if shown else None


def public_messages(rows: list[dict], known: set[str] | frozenset) -> tuple[list[dict], int]:
    shown = [m for m in (public_message(r, known) for r in rows) if m is not None]
    return shown, len(rows) - len(shown)


def public_log_row(row: dict, vocabulary: dict[str, frozenset]) -> dict | None:
    """A log row as ``psb log --tail`` shows it, or None when it is omitted."""
    kind = row.get("type")
    if not isinstance(kind, str):
        return None
    base = {"ts": row.get("ts"), "type": kind}
    if kind == "ncbi":
        return {**base, "endpoint": row.get("endpoint"), "cache": bool(row.get("cache"))}
    if kind == "command":
        words = row.get("command")
        if _marked(row) and isinstance(words, list) and words and words[0] in vocabulary \
                and all(w in vocabulary[words[0]] for w in words[1:2]) and len(words) <= 2:
            return {**base, "command": list(words)}
        words = legacy_command(row.get("argv"), vocabulary)
        if words is None or words[0] in PRIVATE_COMMANDS:
            return None
        return {**base, "command": words}
    return {**base, **{k: v for k, v in row.items()
                       if k not in {"ts", "type", "disclosure_version"} and isinstance(v, (bool, int, float))}}


def public_log(rows: list[dict], vocabulary: dict[str, frozenset]) -> tuple[list[dict], int]:
    shown = [r for r in (public_log_row(row, vocabulary) for row in rows) if r is not None]
    return shown, len(rows) - len(shown)
