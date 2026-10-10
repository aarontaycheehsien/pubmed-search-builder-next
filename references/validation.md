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

Also technical: a `[pt]`, `[sb]`, `[la]` or `[pa]` value PubMed reports as not found
(`filter_value_not_found`; e.g. `"Randomised Controlled Trial"[pt]`), a tag after a group such as
`(a OR b)[tiab]` (`group_field_tag`; PubMed drops it and searches All Fields), and typographic
quotes, dashes or spaces (`typographic_character`); use plain ASCII and tag each term.

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
development and comparison sets, the frozen allocation (as a digest), effective dates, diagnostics,
vocabulary and known hits. Held-out records are not sets: no evaluation, critic packet or binding
contains them, and their retrieval never moves the critic binding. Count/timestamp changes alone do
not require another critique. Every depth requires a critic; quick/standard/thorough permit 1/2/3
rounds. Unresolved findings cannot disappear by omission from a later round. On budget exhaustion use
an unfinished diagnostic handoff instead of issuing a final query.

## The held-out receipt

`psb holdout-test` runs after a complete evaluation and a current critic review. It stores
`holdout/receipt-N.json`, bound to the query, strategy, `review_sha256`, `as_of`, the allocation and
held-out membership, eligibility, policy version and template version. A repeat with the same binding
returns the stored receipt; a new receipt is allowed only when the binding changed for a reason other
than a strategy edit. A changed strategy after a receipt is refused until `psb holdout-release`.
`psb report` requires the matching complete or empty receipt (blockers `allocation_missing`,
`allocation_stale`, `holdout_test_missing`, `holdout_test_incomplete`, `holdout_test_stale`,
`holdout_strategy_changed`), never scores the held-out records again, and never turns holdout misses
into a review: the tested query is delivered unchanged. The manifest records the receipt's hash and the
delivered interpretation text.

`psb report` always validates live and runs all checks. `--fresh` is a compatible alias. On success,
deliver `final-query.txt` verbatim alongside `audit.md` and `validation-manifest.json`. The query
includes the effective `as_of` restriction (Create Date `[crdt]`; Entry Date `[edat]` in workspaces made
before `cutoff.json`) so it matches the tested search. Put additional prose
in `narrative.md`; editing generated artifacts invalidates their hashes. Counts reflect today's
index with the specified date bound, not a reconstruction of historical indexing. A policy-1
delivery (from before held-out testing) still verifies and is labelled legacy.

On failure, inspect `diagnostic-audit.md`; it is unfinished output and no current protected query
is issued. Previous artifacts are archived, not discarded. `psb status` verifies the receipt;
an orphaned file, altered artifact or stale receipt is not a valid delivery. Technical checks and
automated critique do not establish complete recall or constitute human PRESS peer review.

Source: [NLM PubMed User Guide: phrases, wildcards, and proximity](https://pubmed.ncbi.nlm.nih.gov/help/).
