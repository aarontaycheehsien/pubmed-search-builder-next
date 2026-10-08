"""The fixed interpretation of known-record retrieval: one renderer, used by every message and the audit.

The agent relays this text verbatim and never words its own reading of a result such as ``x/x``.
``references/reporting.md`` quotes every template in ``TEXT``; a test keeps the two identical.

The message always has six labelled lines, as a Markdown list:

    - **Allocation:** development and held-out counts, and how the allocation was chosen
    - **Result:** the held-out result, or why there is none
    - **Test material and separation:** sources, screening, grouping, exposure, dates
    - **Interpretation:** the fixed wording for the case, plus any independence limitation
    - **Size context:** the illustration of what the test could detect, or its limitation
    - **Delivery and next step:** what was delivered and what may follow

Comparison lists follow as further list items.

The case is chosen by record-level results, which is conservative: a missed report is a gap even when
another report of the same study was retrieved.
"""

from __future__ import annotations

from decimal import ROUND_HALF_UP, Decimal

from .workspace import ORIGINS

TEMPLATE_VERSION = "1"
LABELS = ("Allocation", "Result", "Test material and separation", "Interpretation", "Size context",
          "Delivery and next step")
TEXT = {
    "all": ("The frozen query retrieved all **{x} eligible held-out records**. This check exposed no retrieval "
            "failures. It establishes successful retrieval of these records, not complete retrieval of all relevant "
            "literature. A result of **{x}/{x}** does not by itself establish high overall recall."),
    "illustration": ("For scale only: a search that misses **5%** of relevant studies would still retrieve all "
                     "**{x}** test studies about **{p}** of the time, assuming independent, representative sampling. "
                     "This is an illustration of the test's ability to detect misses, not an estimate of this "
                     "search's actual recall."),
    "omitted": ("A numerical sample-size illustration is omitted because these records cannot be treated as verified "
                "independent study observations. Multiple reports of one study do not provide the same information "
                "as the same number of distinct studies."),
    "selection": ("The test may also underrepresent terminology or study types missing from the sources used to "
                  "assemble it. Increasing its size does not by itself remove that selection limitation."),
    "partial": ("The frozen query retrieved **{r}/{x} eligible held-out records** and missed **{m}**. This "
                "demonstrates a retrieval gap among these test records. The observed proportion describes this "
                "reference set; it is not a reliable estimate of recall across all relevant literature without "
                "suitable sampling and independence."),
    "none": ("These records were available for developing or improving the search. Their retrieval is a development "
             "check, not independent validation. No held-out retrieval test was performed."),
    "no_records": ("No eligible reference records were available, so no record-based retrieval check was performed. "
                   "Recall was not estimated; the strategy is empirically unvalidated."),
    "unavailable": ("No interpretable held-out retrieval result is available because **{reason}**. Do not interpret "
                    "this as zero recall or a successful test."),
    "exposure": ("**Independence limitation:** {detail}. These results must not be described as an unexposed "
                 "independent test."),
    "comparison": ("**{name}:** {r}/{x} retrieved. These records were not screened into the allocation pool for this "
                   "question (or were consulted throughout development in an earlier version of this skill), so this "
                   "is a comparison, not a development check or an independent test."),
    "delivered": "The delivered query is the query that was tested and has not been revised using these results.",
    "repair_offer": ("Investigating the missed records and repairing the search is available as a next step. Such a "
                     "revision would use this test set for development and would require new unexposed records for "
                     "another independent test."),
    "repaired": ("This query was revised after the held-out test, using the held-out records for development. The "
                 "earlier result ({r}/{x}, receipt {id}) applies to the earlier query, not this one. No independent "
                 "held-out test of this query was performed."),
    "released_untested": ("The held-out records were released to development before any held-out test. No independent "
                          "held-out test of this query was performed."),
    "not_applicable": "Not applicable: no held-out test was performed.",
    "no_result": "Not applicable: there is no interpretable held-out result.",
    "pending": "Not delivered yet: the held-out test must complete before psb report.",
}
NO_HOLDOUT = {
    "empty": "no eligible reference records",
    "small": "fewer than 10 eligible units",
    "exposed": "no unexposed units: every eligible record was seen by the builder",
    "quick": "quick depth",
    "designated-none": "none of the designated records was eligible and available",
}
CHOICES = {
    "keep-holdout": "you kept the proposed holdout",
    "all-development": "you chose to use every record for development",
    "proceed-default": "the proposed holdout was kept by default (you asked me not to wait for answers)",
    "designated": "your designated test set",
}
SHARED_VOCABULARY = {"similar-articles", "pilot-search"}


def percent(x: int) -> str:
    """100 × 0.95^x, half-up to one decimal place; below 0.1 (unrounded) it is ``<0.1%``."""
    value = Decimal("0.95") ** x * 100
    if value < Decimal("0.1"):
        return "<0.1%"
    return f"{value.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)}%"


def _n(count: int, word: str) -> str:
    return f"{count:,} {word if count == 1 else word + 's'}"


def _units(counts: dict) -> str:
    return f"{_n(counts.get('units', 0), 'unit')} ({_n(counts.get('records', 0), 'record')})"


def _pmids(values) -> str:
    items = sorted({str(v) for v in values}, key=int)
    return ", ".join(items[:20]) + (f" and {len(items) - 20} more" if len(items) > 20 else "")


def _allocation_line(state: dict | None) -> str:
    if state is None:
        return "No allocation was recorded."
    allocation = state["allocation"]
    if not allocation.get("N"):
        return "No eligible reference records."
    development = {"units": len(state["development"]), "records": sum(len(u["members"]) for u in state["development"])}
    held = {"units": len(state["held"]), "records": sum(len(u["members"]) for u in state["held"])}
    if state.get("released"):
        total = {k: development[k] + held[k] for k in development}
        return (f"Development: {_units(total)}, including the {_n(held['units'], 'unit')} formerly held out "
                f"({CHOICES.get(allocation.get('choice'), 'held out')}; released for repair: "
                f"{state['released'].get('reason')}).")
    if held["units"]:
        return f"Development: {_units(development)}; held-out test: {_units(held)}; {CHOICES[allocation['choice']]}."
    if allocation.get("choice") in CHOICES:
        return f"Development: {_units(development)}; held-out test: none; {CHOICES[allocation['choice']]}."
    return (f"Development: {_units(development)}; held-out test: none; no holdout was proposed: "
            f"{NO_HOLDOUT.get(allocation.get('reason'), 'not recorded')}.")


def _material(state: dict, receipt: dict | None) -> str:
    """Sources, screening, grouping, exposure and dates of the held-out units."""
    held = state["held"]
    counts = {o: sum(1 for u in held if o in (u.get("origins") or [])) for o in ORIGINS}
    unrecorded = sum(1 for u in held if not u.get("origins"))
    parts = [f"{o} {n}" for o, n in counts.items() if n] + ([f"unrecorded {unrecorded}"] if unrecorded else [])
    sources = "Sources (units): " + (", ".join(parts) or "none recorded")
    shared = sum(1 for u in held if SHARED_VOCABULARY & set(u.get("origins") or []))
    if shared:
        sources += (f" ({_n(shared, 'unit')} found by similar-articles or pilot searches, which share vocabulary with "
                    "development records or the builder's queries)")
    contexts = {c for u in held for c in u.get("contexts") or []}
    screening = ("screened only in the separate context" if contexts == {"separate"}
                 else "screened in the separate context and by the builder" if "separate" in contexts
                 else "screened by the builder")
    evidence = sorted({e for u in held for e in u.get("evidence") or []})
    screening += f" (evidence basis: {', '.join(evidence)})" if evidence else " (evidence basis not recorded)"
    if all(u.get("grouping") == "verified" for u in held):
        grouping = ("one record per study, verified" if all(len(u["members"]) == 1 for u in held)
                    else "verified, with several reports for some studies")
    else:
        grouping = "not verified"
    exposed = len(exposure_details(state, receipt))
    dates = f"reserved {str(state['allocation'].get('created') or '')[:10]}"
    if receipt:
        dates += f"; tested {str(receipt.get('created') or '')[:10]}"
        dates += f" against PubMed records added up to {receipt['binding'].get('as_of') or 'the test date'}"
    return (f"{sources}. Screening: {screening}. Grouping: {grouping}. Exposure: "
            f"{'none recorded' if not exposed else _n(exposed, 'unit') + ' with recorded exposure'}. Dates: {dates}.")


def exposure_details(state: dict, receipt: dict | None) -> list[str]:
    """One sentence per held-out unit whose separation was compromised or is uncertain."""
    source = (receipt or {}).get("exposure")
    if source is None:
        source = [{"unit": u["id"], "reasons": [f"PMID {e['pmid']}: {', '.join(e['reasons'])}" for e in u.get("exposure") or []]}
                  for u in state["held"] if u.get("exposure")]
    return [f"unit {row['unit']} ({'; '.join(row['reasons'])})" for row in source if row.get("reasons")]


def render(state: dict | None, receipt: dict | None = None, *, comparison: list[dict] | None = None) -> dict:
    """The six lines for the current allocation state and the receipt it rests on."""
    lines = {label: "" for label in LABELS}
    lines["Allocation"] = _allocation_line(state)
    case = "none"
    if state is None or not state["allocation"].get("N"):
        case = "no_records" if state is not None else "none"
        lines["Result"] = "No record-based retrieval check was performed."
        lines["Test material and separation"] = "Not applicable: no eligible reference records."
        lines["Interpretation"] = TEXT["no_records"] if state is not None else TEXT["none"]
        lines["Size context"] = lines["Delivery and next step"] = TEXT["not_applicable"]
    elif state.get("released"):
        case = "released"
        lines["Interpretation"] = TEXT["none"]
        lines["Size context"] = TEXT["not_applicable"]
        if receipt and receipt.get("status") == "complete":
            records = receipt["records"]
            lines["Result"] = (f"The earlier query retrieved {records['retrieved']}/{records['eligible']} held-out records "
                               f"(receipt {receipt['number']}); this query has no held-out test.")
            lines["Test material and separation"] = _material(state, receipt) + f" Released for repair: {state['released'].get('reason')}."
            lines["Delivery and next step"] = TEXT["repaired"].format(r=records["retrieved"], x=records["eligible"],
                                                                      id=receipt["number"])
        else:
            lines["Result"] = "No held-out test was performed; the held-out records were released before testing."
            lines["Test material and separation"] = f"Released before testing: {state['released'].get('reason')}."
            lines["Delivery and next step"] = TEXT["released_untested"]
    elif not state["held"]:
        lines["Result"] = "No held-out test was performed."
        allocation = state["allocation"]
        lines["Test material and separation"] = (
            f"{CHOICES[allocation['choice']][0].upper()}{CHOICES[allocation['choice']][1:]}."
            if allocation.get("choice") in CHOICES and allocation.get("choice") != "designated"
            else f"No holdout was proposed: {NO_HOLDOUT.get(allocation.get('reason'), 'not recorded')}.")
        lines["Interpretation"] = TEXT["none"]
        lines["Size context"] = lines["Delivery and next step"] = TEXT["not_applicable"]
    else:
        lines["Test material and separation"] = _material(state, receipt)
        status = (receipt or {}).get("status")
        if status == "complete":
            records = receipt["records"]
            x, r = records["eligible"], records["retrieved"]
            studies = receipt.get("studies")
            study_text = f"; studies {studies['retrieved']}/{studies['eligible']}" if studies else ""
            if r == x:
                case = "all"
                lines["Result"] = f"{r}/{x} eligible held-out records retrieved; 0 missed{study_text}."
                lines["Interpretation"] = TEXT["all"].format(x=x)
                size = (TEXT["illustration"].format(x=x, p=percent(x)) if receipt.get("distinct_studies")
                        else TEXT["omitted"])
                lines["Size context"] = f"{size} {TEXT['selection']}"
                lines["Delivery and next step"] = TEXT["delivered"]
            else:
                case = "partial"
                lines["Result"] = (f"{r}/{x} eligible held-out records retrieved; {x - r} missed{study_text} "
                                   f"(missed: PMIDs {_pmids(records['missed'])}).")
                lines["Interpretation"] = TEXT["partial"].format(r=r, x=x, m=x - r)
                lines["Size context"] = TEXT["selection"]
                lines["Delivery and next step"] = f"{TEXT['delivered']} {TEXT['repair_offer']}"
            details = exposure_details(state, receipt)
            if details:
                lines["Interpretation"] += " " + TEXT["exposure"].format(detail="; ".join(details))
        else:
            case = status or "pending"
            reason = {"empty": "none of the held-out records is in PubMed by the effective date",
                      "incomplete": (receipt or {}).get("reason") or "the held-out test did not complete",
                      None: "the held-out test has not been run yet"}[status]
            lines["Result"] = f"Not available: {reason}."
            lines["Interpretation"] = TEXT["unavailable"].format(reason=reason)
            lines["Size context"] = TEXT["no_result"]
            lines["Delivery and next step"] = TEXT["pending"] if status != "empty" else TEXT["no_result"]
    # A list, so each labelled line stays on its own line wherever the Markdown is rendered.
    body = [f"- **{label}:** {lines[label]}" for label in LABELS]
    extra = [f"- {TEXT['comparison'].format(name=c['name'], r=c['retrieved'], x=c['in_pubmed'])}" for c in comparison or []]
    return {"case": case, "lines": lines, "text": "\n".join(body + extra), "template_version": TEMPLATE_VERSION}


def comparison_rows(evaluation: dict) -> list[dict]:
    """Comparison lists in an evaluation, for the lines after the six."""
    from .workspace import purpose_of
    return [{"name": name, "retrieved": data.get("retrieved", 0), "in_pubmed": data.get("in_pubmed", 0)}
            for name, data in sorted((evaluation.get("sets") or {}).items()) if purpose_of(data) == "comparison"]
