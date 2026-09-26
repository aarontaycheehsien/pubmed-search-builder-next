"""Read PubMed's own account of a query: translation, warnings, and not-found terms.

A count is only evidence when PubMed searched what the strategy says. These checks turn the
ESearch translation into short, coded issues so silent reinterpretation gets noticed.
"""

from __future__ import annotations

import re

from . import wildcards

MAX_ISSUES = 8
EVIDENCE_LIMIT = 240
ATM_EXPANSION_RATIO = 4.0


def _items(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    if isinstance(value, dict):
        return [f"{key}: {item}" for key, nested in value.items() for item in _items(nested)]
    text = str(value).strip()
    return [text] if text else []


def _pairs(translations: object) -> list[tuple[str, str]]:
    pairs = []
    for item in translations if isinstance(translations, list) else []:
        if isinstance(item, dict):
            pairs.append((str(item.get("from", "")).strip(), str(item.get("to", "")).strip()))
    return [pair for pair in pairs if pair[0] or pair[1]]


def _untagged_words(query: str) -> list[str]:
    text = re.sub(r'"[^"]+"\s*\[[^\]]+\]', " ", query)
    text = re.sub(r"[\w*.'-]+\s*\[[^\]]+\]", " ", text)
    text = re.sub(r"\[[^\]]+\]", " ", text)
    words = re.findall(r"\b[A-Za-z][A-Za-z0-9-]+\b", text)
    return [word for word in words if word.upper() not in {"AND", "OR", "NOT"}]


def translation_issues(
    query: str,
    translation: str,
    translations: object = None,
    warnings: object = None,
    errors: object = None,
) -> list[dict[str, str]]:
    issues: list[dict[str, str]] = []

    def add(severity: str, code: str, message: str, evidence: object = "") -> None:
        if len(issues) < MAX_ISSUES:
            issue = {"severity": severity, "code": code, "message": message}
            text = str(evidence)
            if text:
                issue["evidence"] = text if len(text) <= EVIDENCE_LIMIT else text[: EVIDENCE_LIMIT - 3] + "..."
            issues.append(issue)

    for item in _items(warnings):
        add("warning", "pubmed_warning", "PubMed reported a warning; check the translation.", item)

    phrases, fields = [], []
    if isinstance(errors, dict):
        phrases = _items(errors.get("phrasesnotfound"))
        fields = _items(errors.get("fieldsnotfound"))
    elif errors:
        phrases = _items(errors)
    if phrases:
        add(
            "warning",
            "phrase_not_found",
            "PubMed found no records for these terms. Check spelling, hyphenation and spacing "
            "before deciding they are genuinely absent; a zero-hit term is recall-neutral.",
            ", ".join(dict.fromkeys(phrases)),
        )
    if fields:
        add("error", "field_not_found", "PubMed did not recognise these field tags.", ", ".join(dict.fromkeys(fields)))

    lower = (translation or "").lower()
    pairs = _pairs(translations)
    untagged = [source for source, _ in pairs] or _untagged_words(query)
    tagged = bool(re.search(r"\[[^\]]+\]", query))

    if untagged and pairs:
        add(
            "warning",
            "automatic_term_mapping",
            "Untagged text went through Automatic Term Mapping; tag it explicitly so the "
            "search does not depend on ATM behaviour.",
            "; ".join(f"{a} -> {b}" for a, b in pairs[:3]),
        )
    if untagged and "[all fields]" in lower:
        add("warning", "all_fields", "Untagged text was searched in All Fields.", ", ".join(untagged[:8]))
    acronyms = [token for word in untagged for token in re.findall(r"\b[A-Z0-9]{2,6}\b", word)]
    if acronyms and translation:
        add("warning", "untagged_acronym", "Untagged acronyms may map ambiguously.", ", ".join(acronyms))
    if untagged and len(" ".join(lower.split())) > max(200, int(len(" ".join(query.split())) * ATM_EXPANSION_RATIO)):
        add("warning", "large_expansion", "PubMed expanded the query substantially.", translation)
    if tagged and not untagged and "[all fields]" in lower and "[all fields]" not in query.lower():
        add("warning", "all_fields_fallback", "A field-tagged query translated to All Fields.", translation)

    dropped = wildcards.dropped_truncations(query, translation) if translation else []
    if dropped:
        add(
            "warning",
            "truncation_dropped",
            "PubMed searched the bare word instead of the truncation; a word-final asterisk "
            "needs at least four preceding characters.",
            ", ".join(dropped),
        )
    return issues
