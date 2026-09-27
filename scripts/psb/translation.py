"""Read PubMed's own account of a query: translation, warnings, and not-found terms.

A count is only evidence when PubMed searched what the strategy says. These checks turn the
ESearch translation into short, coded issues so silent reinterpretation gets noticed.
"""

from __future__ import annotations

import re

from . import wildcards, syntax

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


# Fields whose values come from a closed NLM list. A value PubMed cannot find in one of these is a
# misspelt or invented value, not a rare word: it silently drops out of an OR, or empties an AND.
FILTER_FIELDS = {"pt", "sb", "la", "pa"}
FILTER_VALUE_MESSAGE = ("PubMed does not recognise this publication type, subset, language or pharmacological "
                        "action value; use the exact NLM value.")


def _filter_value(query: str, phrase: str) -> bool:
    """True when a not-found phrase is a value of a closed-list field in ``query``.

    Quoted not-found phrases come back with their tag (``"X"[pt]``); unquoted ones come back bare
    (``systematicx``) and are matched against the query's tagged terms.
    """
    tagged = syntax.atoms(phrase)
    if tagged:
        return any(a["field"] in FILTER_FIELDS for a in tagged)
    text = phrase.strip().strip('"').casefold()
    return any(a["field"] in FILTER_FIELDS and a["text"].strip('"').casefold() == text for a in syntax.atoms(query))


def translation_issues(
    query: str,
    translation: str,
    translations: object = None,
    warnings: object = None,
    errors: object = None,
) -> list[dict[str, str]]:
    issues: list[dict[str, str]] = []

    def add(severity: str, code: str, message: str, evidence: object = "") -> None:
        issues.append({"severity": severity, "code": code, "message": message,
                       "evidence": evidence, "query": query, "translation": translation})

    for item in _items(warnings):
        phrase_warning = "phrase" in item.casefold() and ("not found" in item.casefold() or "notfound" in item.casefold())
        if phrase_warning and _filter_value(query, item.split(": ", 1)[-1]):
            add("error", "filter_value_not_found", FILTER_VALUE_MESSAGE, item)
            continue
        add("warning", "quoted_phrase_not_found" if phrase_warning else "pubmed_warning",
            "Review the clause translation; phrase-index absence does not establish zero retrieval."
            if phrase_warning else "PubMed reported a warning; review the translation.", item)
    if isinstance(errors, dict):
        for phrase in _items(errors.get("phrasesnotfound")):
            if _filter_value(query, phrase):
                add("error", "filter_value_not_found", FILTER_VALUE_MESSAGE, phrase)
                continue
            add("warning", "phrase_not_found",
                "Review this clause and its translation. Distinguish an unrecognised phrase, a zero-hit clause, "
                "and an invalid controlled-vocabulary term; no automatic rewrite or deletion.", phrase)
        for name in _items(errors.get("fieldsnotfound")):
            add("error", "field_not_found", "PubMed did not recognise a field tag.", name)
        other = {k: v for k, v in errors.items() if k not in {"phrasesnotfound", "fieldsnotfound"}}
        if other:
            add("error", "pubmed_error", "Unclassified PubMed error requires investigation.", other)
    elif errors:
        add("error", "pubmed_error", "Unexpected PubMed error response.", errors)

    lower = (translation or "").lower()
    pairs = _pairs(translations)
    pairs = [(a, b) for a, b in pairs if syntax.untagged(a)]
    untagged = syntax.untagged(query)
    tagged = bool(re.search(r"\[[^\]]+\]", query))

    if untagged and pairs:
        add(
            "warning",
            "automatic_term_mapping",
            "Untagged text went through Automatic Term Mapping; tag it explicitly so the "
            "search does not depend on ATM behaviour.",
            "; ".join(f"{a} -> {b}" for a, b in pairs),
        )
    if untagged and "[all fields]" in lower:
        add("warning", "all_fields", "Untagged text was searched in All Fields.", ", ".join(untagged))
    acronyms = [token for word in untagged for token in re.findall(r"\b[A-Z0-9]{2,6}\b", word)]
    if acronyms and translation:
        add("warning", "untagged_acronym", "Untagged acronyms may map ambiguously.", ", ".join(acronyms))
    if untagged and len(" ".join(lower.split())) > max(200, int(len(" ".join(query.split())) * ATM_EXPANSION_RATIO)):
        add("warning", "large_expansion", "PubMed expanded the query substantially.", translation)
    if tagged and not untagged and "[all fields]" in lower and not any(a["field"] == "all" for a in syntax.atoms(query)):
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
