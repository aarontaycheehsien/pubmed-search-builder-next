"""PubMed wildcard rules that fail silently or look like an outage.

Both were confirmed against live ESearch:

* A word-final asterisk truncates only when at least four characters precede it, counted from
  the start of its term or quoted phrase. Otherwise PubMed drops the asterisk and searches the
  bare word with no warning: ``cat*[tiab]`` runs as ``"cat"[Title/Abstract]`` and
  ``"cat* scratch"[tiab]`` as ``"cat scratch"``, while ``"scratch cat*"[tiab]`` keeps it.
* A query with more than 256 asterisks is rejected with an HTTP 200 "Search Backend failed ...
  temporarily unavailable" body, which reads like an outage rather than a query problem.
"""

from __future__ import annotations

import re
from typing import Any

MIN_TRUNCATION_PREFIX = 4
MAX_WILDCARDS = 256

_TOKEN = re.compile(r'"[^"]*"|\[[^\]]*\]|[()]|[^\s()"\[\]]+')
_OPERATORS = frozenset({"AND", "OR", "NOT"})
_WORD_BEFORE = re.compile(r"([A-Za-z0-9][A-Za-z0-9'-]*)$")


def search_terms(query: str) -> list[str]:
    """Units PubMed searches: quoted phrases, tagged word runs (``smith j*[au]``), single words."""
    terms: list[str] = []
    run: list[str] = []
    for token in _TOKEN.findall(query or ""):
        if token.startswith("["):
            if run:
                terms.append(" ".join(run))
                run = []
            continue
        if token.startswith('"') or token in "()" or token.upper() in _OPERATORS:
            terms.extend(run)
            run = []
            if token.startswith('"'):
                terms.append(token[1:-1])
            continue
        run.append(token)
    terms.extend(run)
    return terms


def wildcard_terms(query: str) -> list[dict[str, Any]]:
    found: list[dict[str, Any]] = []
    for segment in search_terms(query):
        for position, character in enumerate(segment):
            if character != "*":
                continue
            prefix = segment[:position]
            word = _WORD_BEFORE.search(prefix)
            found.append(
                {
                    "term": segment.strip(),
                    "word": word.group(1) if word else "",
                    "word_final": not segment[position + 1 : position + 2].isalnum(),
                    "prefix_length": len(re.sub(r"[\s*]", "", prefix)),
                }
            )
    return found


def short_truncations(query: str) -> list[str]:
    """Terms whose word-final truncation PubMed silently ignores."""
    return sorted(
        {
            item["term"]
            for item in wildcard_terms(query)
            if item["word_final"] and item["prefix_length"] < MIN_TRUNCATION_PREFIX
        }
    )


def dropped_truncations(query: str, translation: str) -> list[str]:
    """Words whose truncation is missing from PubMed's translation of the query."""
    translated = (translation or "").casefold()
    if not translated.strip():
        return []
    return sorted(
        {
            f"{item['word']}*"
            for item in wildcard_terms(query)
            if item["word_final"] and item["word"] and f"{item['word']}*".casefold() not in translated
        }
    )
