"""The strategy model: concept blocks of OR-ed terms, combined into one PubMed query.

``strategy.json``::

    {"blocks": [{"id": "condition", "name": "Vesicoureteral reflux",
                 "terms": ["\\"Vesico-Ureteral Reflux\\"[Mesh]", "vesicoureteral reflux*[tiab]"]}],
     "combine": null,            # null = AND of all blocks; or e.g. "condition AND (test OR imaging)"
     "limits": [{"clause": "NOT (animals[mh] NOT humans[mh])", "rationale": "..."}]}

A block ``id`` is the one key for a concept everywhere: protocol, strategy, evaluation, report.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from . import wildcards, syntax

ID_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")
OPERATORS = {"AND", "OR", "NOT"}
_TAG = re.compile(r"\[([^\]]+)\]")


class StrategyError(ValueError):
    pass


@dataclass
class Block:
    id: str
    name: str
    terms: list[str]


@dataclass
class Limit:
    clause: str
    rationale: str = ""


@dataclass
class Strategy:
    blocks: list[Block]
    combine: str | None = None
    limits: list[Limit] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict) -> "Strategy":
        if not isinstance(data, dict):
            raise StrategyError("strategy must be a JSON object")
        blocks = []
        for raw in data.get("blocks") or []:
            if not isinstance(raw, dict):
                raise StrategyError("each block must be an object")
            terms = [str(t).strip() for t in raw.get("terms") or [] if str(t).strip()]
            blocks.append(Block(str(raw.get("id", "")).strip(), str(raw.get("name", "")).strip(), terms))
        limits = [
            Limit(str(item.get("clause", "")).strip(), str(item.get("rationale", "")).strip())
            for item in data.get("limits") or []
            if isinstance(item, dict) and str(item.get("clause", "")).strip()
        ]
        combine = data.get("combine")
        return cls(blocks, str(combine).strip() if combine else None, limits)

    def to_dict(self) -> dict:
        return {
            "blocks": [{"id": b.id, "name": b.name, "terms": list(b.terms)} for b in self.blocks],
            "combine": self.combine,
            "limits": [{"clause": l.clause, "rationale": l.rationale} for l in self.limits],
        }

    def block(self, block_id: str) -> Block:
        for block in self.blocks:
            if block.id == block_id:
                return block
        raise StrategyError(f"no block with id {block_id!r}")

    def structural_errors(self) -> list[str]:
        errors = []
        if not self.blocks:
            errors.append("strategy has no blocks")
        seen = set()
        for block in self.blocks:
            if not ID_PATTERN.fullmatch(block.id) or block.id.upper() in OPERATORS:
                errors.append(f"invalid block id {block.id!r} (letters, digits, underscore; not AND/OR/NOT)")
            if block.id in seen:
                errors.append(f"duplicate block id {block.id!r}")
            seen.add(block.id)
            if not block.terms:
                errors.append(f"block {block.id!r} has no terms")
        if self.combine:
            errors.extend(message for _, message in syntax.problems(self.combine, combination=True))
            words = set(re.findall(r"[A-Za-z][A-Za-z0-9_]*", self.combine)) - OPERATORS
            unknown = sorted(words - seen)
            if unknown:
                errors.append(f"combine references unknown block ids: {', '.join(unknown)}")
        return errors

    def validate(self) -> None:
        errors = self.structural_errors()
        if errors:
            raise StrategyError("; ".join(errors))


def _mask_quotes(text: str) -> str:
    return re.sub(r'"[^"]*"', lambda m: "_" * len(m.group(0)), text)


def wrap_term(term: str) -> str:
    """Parenthesise a term that has its own top-level operators, so OR-joining cannot rebind it."""
    stripped = term.strip()
    if re.search(r"\s(AND|OR|NOT)\s", _mask_groups(stripped)):
        return f"({stripped})"
    return stripped


def _mask_groups(text: str) -> str:
    """Blank out quoted phrases, field tags and parenthesised groups (keeps top level only)."""
    text = re.sub(r'"[^"]*"', lambda m: "_" * len(m.group(0)), text)
    text = re.sub(r"\[[^\]]*\]", lambda m: "_" * len(m.group(0)), text)
    out, depth = [], 0
    for char in text:
        if char == "(":
            depth += 1
        out.append("_" if depth else char)
        if char == ")" and depth:
            depth -= 1
    return "".join(out)


def block_query(block: Block) -> str:
    return "(" + " OR ".join(wrap_term(t) for t in block.terms) + ")"


def core_query(strategy: Strategy, *, exclude: str | None = None) -> str:
    """The topic query without limits; ``exclude`` drops one block (AND-combined strategies only)."""
    if strategy.combine and exclude is None:
        queries = {b.id: block_query(b) for b in strategy.blocks}
        return re.sub(r"\b[A-Za-z][A-Za-z0-9_]*\b", lambda m: queries.get(m.group(0), m.group(0)), strategy.combine)
    if strategy.combine and exclude is not None:
        raise StrategyError("block ablation needs the default AND combination")
    parts = [block_query(b) for b in strategy.blocks if b.id != exclude]
    return " AND ".join(parts)


def apply_limits(query: str, limits: list[Limit]) -> str:
    for limit in limits:
        clause = limit.clause.strip()
        if clause.upper().startswith("NOT "):
            query = f"({query}) NOT ({clause[4:].strip()})"
        else:
            query = f"({query}) AND ({clause})"
    return query


def full_query(strategy: Strategy) -> str:
    return apply_limits(core_query(strategy), strategy.limits)


def numbered_lines(strategy: Strategy) -> list[dict]:
    """PRISMA-S style line set: one line per term, an OR line per block, then combination and limits."""
    lines: list[dict] = []
    block_lines: dict[str, int] = {}
    for block in strategy.blocks:
        first = len(lines) + 1
        for term in block.terms:
            lines.append({"n": len(lines) + 1, "text": term, "query": term, "kind": "term", "block": block.id})
        refs = " OR ".join(f"#{n}" for n in range(first, len(lines) + 1))
        lines.append({"n": len(lines) + 1, "text": refs, "query": block_query(block), "kind": "block", "block": block.id})
        block_lines[block.id] = len(lines)
    if strategy.combine:
        text = re.sub(r"\b[A-Za-z][A-Za-z0-9_]*\b", lambda m: f"#{block_lines[m.group(0)]}" if m.group(0) in block_lines else m.group(0), strategy.combine)
    else:
        text = " AND ".join(f"#{block_lines[b.id]}" for b in strategy.blocks)
    if len(strategy.blocks) > 1 or strategy.combine:
        lines.append({"n": len(lines) + 1, "text": text, "query": core_query(strategy), "kind": "combine", "block": None})
    current = len(lines)
    for index, limit in enumerate(strategy.limits):
        clause = limit.clause.strip()
        is_not = clause.upper().startswith("NOT ")
        text = f"#{current} NOT {clause[4:].strip()}" if is_not else f"#{current} AND {clause}"
        query = apply_limits(core_query(strategy), strategy.limits[: index + 1])
        lines.append({"n": len(lines) + 1, "text": text, "query": query, "kind": "limit", "block": None})
        current = len(lines)
    return lines


# -- lint ------------------------------------------------------------------------------------

def untagged_segments(text: str) -> list[str]:
    """Compatibility entry point for the shared tokenizer's field-aware scan."""
    return syntax.untagged(text)


def term_issues(term: str) -> list[dict]:
    issues = []

    def add(severity: str, code: str, message: str) -> None:
        issues.append({"severity": severity, "code": code, "message": message, "term": term})

    for code, message in syntax.problems(term):
        add("error", code, message)
    tags = [tag.strip().lower() for tag in _TAG.findall(term)]
    for tag in tags:
        base = tag.split(":")[0]
        modifier = tag[len(base):]
        if base not in syntax.ALIASES:
            add("warning", "unknown_tag", f"field tag [{tag}] needs authoritative verification")
        if modifier and not modifier.startswith(":~") and not (
            modifier == ":noexp" and syntax.field(base) in {"mh", "majr", "sh", "pt"}
        ):
            add("error", "field_modifier", f"unsupported modifier in [{tag}]")
    masked = " ".join(t for t in syntax.tokens(term) if not t.startswith(('"', '[')))
    if syntax.untagged(term):
        add("warning", "untagged", "untagged text relies on Automatic Term Mapping; add a field tag")
    for short in wildcards.short_truncations(term):
        add("error", "short_truncation", f"'{short}': PubMed ignores truncation with fewer than 4 leading characters")
    if any(tag.startswith("majr") for tag in tags):
        add("warning", "major_topic", "[majr] restricts to major-topic indexing and lowers recall")
    if any(tag.endswith(":noexp") for tag in tags):
        add("info", "noexp", "unexploded MeSH: confirm the narrower descriptors are meant to be excluded")
    if re.search(r'"[^"]*/[^"]*"\s*\[(mesh|mh)', term, re.I):
        add("warning", "subheading", "MeSH/subheading combinations lower recall; prefer the unqualified heading")
    if re.search(r"\bNOT\b", masked):
        add("warning", "not_operator", "NOT inside a block can remove relevant records")
    return issues


def lint(strategy: Strategy, *, concepts: list[dict] | None = None) -> list[dict]:
    issues: list[dict] = [{"severity": "error", "code": "structure", "message": m} for m in strategy.structural_errors()]
    for block in strategy.blocks:
        seen: set[str] = set()
        mesh = text = False
        for term in block.terms:
            normalized = " ".join(term.lower().split())
            if normalized in seen:
                issues.append({"severity": "warning", "code": "duplicate", "message": "duplicate term", "term": term, "block": block.id})
            seen.add(normalized)
            for issue in term_issues(term):
                issue["block"] = block.id
                issues.append(issue)
            tags = {syntax.field(tag) for tag in _TAG.findall(term)}
            mesh = mesh or bool(tags & {"mh", "majr", "nm"})
            text = text or bool(tags & {"tiab", "ti", "ab", "tw", "ot", "kw"})
        compound = [t for t in block.terms if re.search(r"\sAND\s", _mask_quotes(t))]
        if len(block.terms) >= 2 and 2 * len(compound) >= len(block.terms):
            issues.append({"severity": "warning", "code": "compound_block", "block": block.id,
                           "message": "most terms AND two ideas inside one block: split them into separate concept "
                                      "blocks so each gets its full vocabulary (synonyms, MeSH, spelling variants)"})
        if block.terms and not text:
            issues.append({"severity": "warning", "code": "no_text_layer", "block": block.id,
                           "message": "no title/abstract layer: records not yet MeSH-indexed will be missed"})
        if block.terms and not mesh:
            issues.append({"severity": "info", "code": "no_mesh_layer", "block": block.id,
                           "message": "no MeSH layer: confirm with `psb mesh lookup` that no fitting descriptor exists"})
    full = full_query(strategy) if not strategy.structural_errors() else ""
    if full.count("*") > wildcards.MAX_WILDCARDS:
        issues.append({"severity": "error", "code": "too_many_wildcards",
                       "message": f"{full.count('*')} wildcards; PubMed rejects more than {wildcards.MAX_WILDCARDS}"})
    if full:
        for code, message in syntax.problems(full):
            issues.append({"severity": "error", "code": code, "message": message, "location": "final"})
    for index, limit in enumerate(strategy.limits):
        clause = limit.clause[4:] if limit.clause.startswith("NOT ") else limit.clause
        for item in term_issues(clause):
            issues.append({**item, "location": f"limit:{index + 1}"})
        if not limit.rationale:
            issues.append({"severity": "warning", "code": "limit_without_rationale", "message": f"limit has no rationale: {limit.clause}"})
    if concepts is not None:
        block_ids = {b.id for b in strategy.blocks}
        searched = {str(c.get("id")) for c in concepts if c.get("role") == "search"}
        for missing in sorted(searched - block_ids):
            issues.append({"severity": "warning", "code": "concept_without_block",
                           "message": f"protocol concept {missing!r} has role 'search' but no block"})
        known = {str(c.get("id")) for c in concepts}
        for extra in sorted(block_ids - known):
            issues.append({"severity": "warning", "code": "block_without_concept",
                           "message": f"block {extra!r} is not a protocol concept; add it to protocol.json with a role"})
        for concept in concepts:
            if concept.get("role") in {"screen", "optional"} and concept.get("id") in block_ids and not strategy.combine:
                issues.append({"severity": "warning", "code": "screen_concept_searched",
                               "message": f"concept {concept.get('id')!r} is role {concept.get('role')!r} but is AND-ed as a block"})
    return issues
