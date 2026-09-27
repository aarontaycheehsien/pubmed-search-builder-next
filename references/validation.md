# Final-query validation and phrase review

`psb eval` separates `validation.blockers` (non-waivable technical defects) from
`validation.review_required` (substantive judgments needing evidence). `complete: false` means
some required checks were not performed. `eval --no-term-counts` is development-only. Evaluation
success is not final-delivery authorization: only `psb report` can issue the protected artifacts.

## Technical defects

Fix syntax, field, proximity, truncation, confirmed unintended field fallback, and controlled
vocabulary errors. Unknown local tags are checked against NCBI field metadata before final
classification. A successful PubMed count alone does not establish field correctness.
Authority lookup checks preferred labels and types (descriptor, supplementary concept, qualifier),
plus allowable qualifiers for descriptor/subheading combinations. Entry terms produce canonical
heading suggestions. An authority outage means unverified; a valid heading with zero retrieval
is not an invalid heading. `mesh lookup/show` remain discovery tools, not delivery certificates.

No override, critic rejection, or accepted-risk label can waive a technical blocker. Diagnostics
preserve original queries, full evidence and translations; final checks include filters and limits.

## Phrase decision tree

1. Inspect the individual clause, its field, PubMed translation, original warning/error, and count.
   Phrase-index absence, zero retrieval, and invalid controlled vocabulary are distinct conditions.
2. For `[Mesh]`, `[mh]`, `[majr]`, `[nm]` or qualifiers, inspect authority verification first.
3. For free text, decide what the review question requires:
   - Adjacency: test `"school food environment"[tiab:~0]`. This permits **any order**; it is not
     an equivalent replacement when exact word order matters. Document any accepted order change.
   - Some separation: choose and test a justified distance, such as `[tiab:~2]`.
   - Co-occurrence: test `(school[tiab] AND food[tiab] AND environment[tiab])` explicitly.
   - Morphology: test a supported ordinary wildcard phrase, or enumerate variants inside an OR
     of proximity clauses. Never put `*` inside proximity; PubMed ignores proximity in that case.
4. Compare the original and candidate translations, clause counts, final counts and known-record
   retrieval. Diagnose every known loss. Counts are evidence, not proof of conceptual equivalence.
   Do not delete a term merely because it adds no seeds or has zero hits today. Its Boolean role
   matters: an OR alternative and a required condition have different effects.
5. End in one of these states:
   - **Rewritten:** retain before/after evidence in the evaluation history; re-evaluate and obtain
     current critique. Do not silently pick a repair or weaken the intended search.
   - **Removed:** record the rationale and measured effect; re-evaluate and obtain current critique.
   - **Accepted:** explain why the observed interpretation fits the intended search and retain its
     risk in the audit. Prefer an explicit expression when it faithfully expresses that interpretation.

A phrase warning is not automatically a technical failure, but its **unresolved review blocks
delivery**. For a retained warning, copy its issue ID, query and translation into the current
critic response's `issue_dispositions`, with `status: accepted-risk` (or `rejected` for an evidenced
false positive), a substantive `response`, and observed `evidence`. The packet supplies the schema.
Changed translation or inputs invalidate the disposition; "the complete query works" is insufficient.

## Evidence and publication

Every evaluation attempt is saved separately from strategy versions. Critic bindings include scope,
sets, effective dates, diagnostics, vocabulary and known hits. Count/timestamp changes alone do not
require another critique. Every depth requires a critic; quick/standard/thorough permit 1/2/3 rounds.
Unresolved findings cannot disappear by omission from a later round. On budget exhaustion use an
unfinished diagnostic handoff instead of issuing a final query.

`psb report` always validates live and runs all checks. `--fresh` is a compatible alias. On success,
deliver `final-query.txt` verbatim alongside `audit.md` and `validation-manifest.json`. The query
includes effective entry-date restrictions so it matches the tested search. Put additional prose
in `narrative.md`; editing generated artifacts invalidates their hashes. Counts reflect today's
index with the specified date bound, not a reconstruction of historical indexing.

On failure, inspect `diagnostic-audit.md`; it is unfinished output and no current protected query
is issued. Previous artifacts are archived, not discarded. `psb status` verifies the receipt;
an orphaned file, altered artifact or stale receipt is not a valid delivery. Technical checks and
automated critique do not establish complete recall or constitute human PRESS peer review.

Source: [NLM PubMed User Guide: phrases, wildcards, and proximity](https://pubmed.ncbi.nlm.nih.gov/help/).
