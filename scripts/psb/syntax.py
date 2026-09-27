"""Lossless query tokens shared by lint, translation diagnostics and vocabulary checks.

This checks the supported search grammar, not PubMed's semantic interpretation.
Adjacent free-text words remain valid; custom block combinations require explicit operators.
"""
from __future__ import annotations

import re

TOKEN = re.compile(r'"[^"\n]*"|\[[^\[\]\n]*\]|[()]|[^\s()"\[\]]+|[^\s]')
OPERATORS = {"AND", "OR", "NOT"}
PROX_FIELDS = {"ti", "tiab", "ad", "title", "title/abstract", "affiliation"}

# Documented PubMed abbreviations and display names. EInfo supplies additional names.
FIELD_GROUPS = (
    "mh|mesh|mesh terms", "majr|mesh major topic", "sh|subheading|subheadings|mesh subheading|mesh subheadings",
    "nm|supplementary concept", "ti|title", "tiab|title/abstract", "ab|abstract",
    "ad|affiliation", "all|all fields", "tw|text word|text words", "ot|other term",
    "pt|publication type", "dp|pdat|date - publication|publication date", "edat|entrez date|entry date",
    "crdt|create date|date - create", "mhda|mesh date", "lr|date - modification|modification date",
    "la|lang|language", "au|author", "auid|author identifier", "1au|first author", "lastau|last author",
    "fau|full author", "cn|corporate author", "ir|investigator", "fir|full investigator",
    "ta|jour|journal", "jid|nlm unique id", "aid|article identifier", "doi", "uid|pmid",
    "rn|ec/rn number", "sb|filter|subset", "tt|transliterated title", "ps|personal name as subject",
    "pa|pharmacological action", "si|secondary source id", "gr|grant number|grants and funding",
    "dcom|date - completion|completion date", "cois|conflict of interest statement", "book",
    "ed|editor", "isbn", "ip|issue", "lid|location id", "own|owner", "pg|pagination",
    "pl|place of publication", "pubn|publisher", "vi|volume", "pmc|pmcid", "mid",
    "epdat", "ppdat", "pubstatus", "hasabstract", "kw",
)
ALIASES = {alias: group.split("|")[0] for group in FIELD_GROUPS for alias in group.split("|")}

# Word-processor and LLM output substitutes these for plain ASCII. PubMed quietly normalises some of
# them, but the tokeniser here does not treat curly quotes as quotes, other interfaces may not
# normalise at all, and the delivered query must be the text that was actually validated.
TYPOGRAPHIC = {
    "“": '"', "”": '"', "„": '"', "‟": '"', "«": '"', "»": '"',
    "‘": "'", "’": "'", "‚": "'", "‛": "'",
    "‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-", "−": "-",
    " ": " ", " ": " ", " ": " ", "​": "",
}


def tokens(text: str) -> list[str]:
    return TOKEN.findall(text)


def field(tag: str) -> str:
    base = tag.strip("[]").strip().casefold().split(":")[0]
    return ALIASES.get(base, base)


def atoms(text: str) -> list[dict]:
    """Return individually tagged runs, including those nested inside filters."""
    result, run = [], []
    for token in tokens(text):
        if token in {"(", ")"} or token.upper() in OPERATORS:
            run = []
        elif token.startswith("["):
            if run:
                result.append({"text": " ".join(run), "tag": token[1:-1], "field": field(token)})
            run = []
        else:
            run.append(token)
    return result


def untagged(text: str) -> list[str]:
    result, run = [], []
    for token in tokens(text):
        if token == ":":
            continue
        if token.startswith("["):
            run = []
        elif token in {"(", ")"} or token.upper() in OPERATORS:
            result.extend(run)
            run = []
        elif token.startswith('"'):
            result.extend(run)
            run = [token]
        else:
            if run and run[-1].startswith('"') and token != ":" and not token.startswith("/"):
                result.extend(run)
                run = []
            run.append(token)
    return result + run


def problems(text: str, *, combination: bool = False) -> list[tuple[str, str]]:
    found = []
    for char in dict.fromkeys(c for c in text if c in TYPOGRAPHIC):
        plain = TYPOGRAPHIC[char]
        found.append(("typographic_character",
                      f"replace typographic character U+{ord(char):04X} with "
                      + (f"plain {plain!r}" if plain.strip() else "a plain space" if plain else "nothing")))
    need_operand, depth, previous = True, 0, None
    for token in tokens(text):
        if token in {'"', "[", "]"}:
            found.append(("syntax", "unbalanced quotes or field brackets"))
        elif token == "(":
            if combination and not need_operand:
                found.append(("syntax", "missing operator before group"))
            depth += 1
            need_operand = True
        elif token == ")":
            if depth == 0 or need_operand:
                found.append(("syntax", "unmatched or empty parenthesised expression"))
            depth -= 1
            need_operand = False
        elif token.upper() in OPERATORS:
            if token not in OPERATORS:
                found.append(("lowercase_operator", "Boolean operators must be uppercase outside quoted phrases"))
            if need_operand:
                found.append(("syntax", "Boolean operator has no left operand"))
            need_operand = True
        elif token.startswith("["):
            if previous == ")" and not need_operand:
                # PubMed does not distribute a tag over a group: it drops the tag and sends the
                # group's words through Automatic Term Mapping into All Fields.
                found.append(("group_field_tag", "PubMed ignores a field tag after a parenthesised group; tag each term"))
            elif need_operand or (previous and previous.startswith("[")):
                found.append(("syntax", "field tag has no operand or repeats another tag"))
            tag = token[1:-1].strip().lower()
            if not tag:
                found.append(("syntax", "empty field tag"))
            if "~" in tag:
                match = re.fullmatch(r"([^:]+):~(\d+)", tag)
                if not match or not previous or not previous.startswith('"'):
                    found.append(("proximity_syntax", "proximity requires a quoted phrase and a nonnegative integer distance"))
                else:
                    if match[1] not in PROX_FIELDS:
                        found.append(("proximity_field", "proximity requires Title, Title/Abstract or Affiliation"))
                    if "*" in previous:
                        found.append(("proximity_wildcard", "wildcards cause PubMed to ignore proximity"))
                    if len(previous.strip('"').split()) < 2:
                        found.append(("proximity_single_word", "proximity requires at least two words"))
        else:
            if combination and (not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", token) or not need_operand):
                found.append(("syntax", "combine requires block IDs separated by Boolean operators"))
            if token == '""':
                found.append(("syntax", "empty quoted phrase"))
            need_operand = False
        previous = token
    if depth or need_operand:
        found.append(("syntax", "unbalanced parentheses or missing final operand"))
    return list(dict.fromkeys(found))
