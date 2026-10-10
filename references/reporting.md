# Reporting

`psb report` always runs complete live validation, including vocabulary and the current critic.
`--fresh` remains a compatible alias. On success it publishes `final-query.txt`, `audit.md`, and
`validation-manifest.json` from the same evaluated snapshot. The exported query includes any
explicit effective `as_of` create-date (`[crdt]`) restriction; a workspace made before `cutoff.json`
keeps its entry-date (`[edat]`) restriction.

## Order at delivery

1. The critic review of the strategy you mean to deliver is complete (`psb critic check` passes).
2. If records are held out, run `psb holdout-test` once. Relay its message verbatim.
3. `psb report`. It uses the matching receipt and never scores the held-out records again.
4. Deliver the tested query **unchanged**, even when held-out records were missed. Then offer the
   repair (below). Do not revise the strategy because of the result before delivering.

A changed strategy after the test is refused (`holdout_strategy_changed`). An incomplete test
(a PubMed service failure) blocks the report until `psb holdout-test` completes; an empty
denominator (no held-out record in PubMed by the effective date) is delivered with its fixed text.

## The fixed interpretation

`psb` chooses and fills the wording; you relay it verbatim. Never write your own reading of a
result such as `x/x`. The holdout-test message, the audit and the `psb progress deliver` message
carry the same bytes (the manifest stores the delivered text).

The interpretation is a list of six labelled lines, then one line per comparison list:

- **Allocation:** development and held-out counts (units and records), and how the allocation was
  chosen
- **Result:** the held-out result, or why there is none
- **Test material and separation:** sources by origin, screening context and evidence basis,
  grouping, exposure, and dates
- **Interpretation:** the case text below, plus the independence limitation when it applies
- **Size context:** the illustration or the limitation
- **Delivery and next step:** what was delivered and what may follow

The case is chosen by records, which is conservative: a missed report is a gap even when another
report of the same study was found. When grouping is verified, the Result line also gives the
study-level figure (a study is found if any of its reports is found).

### Every held-out record retrieved: `x/x`, x > 0

> The frozen query retrieved all **{x} eligible held-out records**. This check exposed no retrieval failures. It establishes successful retrieval of these records, not complete retrieval of all relevant literature. A result of **{x}/{x}** does not by itself establish high overall recall.

Size context, when every held-out unit is one record with an explicit study key from the screener
and all keys differ (one record per verified distinct study):

> For scale only: a search that misses **5%** of relevant studies would still retrieve all **{x}** test studies about **{p}** of the time, assuming independent, representative sampling. This is an illustration of the test's ability to detect misses, not an estimate of this search's actual recall.

`{p}` is `100 × 0.95^x`, rounded half-up to one decimal place, with `%`; it is `<0.1%` when the
unrounded value is below 0.1 (x ≥ 135). Examples: x = 2 → 90.3%, 3 → 85.7%, 6 → 73.5%,
14 → 48.8%, 134 → 0.1%.

Otherwise (several reports of one study, or grouping not verified):

> A numerical sample-size illustration is omitted because these records cannot be treated as verified independent study observations. Multiple reports of one study do not provide the same information as the same number of distinct studies.

Then always:

> The test may also underrepresent terminology or study types missing from the sources used to assemble it. Increasing its size does not by itself remove that selection limitation.

Delivery and next step:

> The delivered query is the query that was tested and has not been revised using these results.

Never report only "100% recall" or "validation passed".

### Some or all missed: `r/x`, r < x (including 0/x)

> The frozen query retrieved **{r}/{x} eligible held-out records** and missed **{m}**. This demonstrates a retrieval gap among these test records. The observed proportion describes this reference set; it is not a reliable estimate of recall across all relevant literature without suitable sampling and independence.

Size context is the selection-limitation sentence. Delivery and next step is the delivered sentence,
then:

> Investigating the missed records and repairing the search is available as a next step. Such a revision would use this test set for development and would require new unexposed records for another independent test.

### No held-out test (eligible records exist)

> These records were available for developing or improving the search. Their retrieval is a development check, not independent validation. No held-out retrieval test was performed.

The Test material line gives the reason (fewer than 10 eligible units, no unexposed units, quick
depth, or your choice to use everything for development). Size context and Delivery:

> Not applicable: no held-out test was performed.

### No eligible records

> No eligible reference records were available, so no record-based retrieval check was performed. Recall was not estimated; the strategy is empirically unvalidated.

### Incomplete test, empty denominator, or not yet run

> No interpretable held-out retrieval result is available because **{reason}**. Do not interpret this as zero recall or a successful test.

Size context:

> Not applicable: there is no interpretable held-out result.

Before a completed test the Delivery line is:

> Not delivered yet: the held-out test must complete before psb report.

### Independence limitation

Appended to the Interpretation whenever any held-out unit has recorded exposure, before the
designation or after the reservation (including a later report of the study that the builder saw):

> **Independence limitation:** {detail}. These results must not be described as an unexposed independent test.

### Comparison lists

One line per list, after the six:

> **{name}:** {r}/{x} retrieved. These records were not screened into the allocation pool for this question (or were consulted throughout development in an earlier version of this skill), so this is a comparison, not a development check or an independent test.

### After a repair

If the user asks for the repair, `psb holdout-release --reason "..."` returns the held-out records to
development and keeps the receipt. The revised query is reviewed in a repair epoch (one revision
round, then the closing round) and delivered with:

> This query was revised after the held-out test, using the held-out records for development. The earlier result ({r}/{x}, receipt {id}) applies to the earlier query, not this one. No independent held-out test of this query was performed.

If the records were released before any test:

> The held-out records were released to development before any held-out test. No independent held-out test of this query was performed.

## Reporting-only escape hatch

For a format the user asked for, or an unusual case, you may shorten, combine or extend these texts
**in your own prose only**: an additional chat message, or `narrative.md`. Relayed `psb` text stays
verbatim, and `audit.md` is hash-bound. Keep the observed result, the separation qualifications, the
significance statement, the limitations and the next-step status. Record why the format changed in a
`narrative.md` section titled "Reporting format".

Never: an unexplained `x/x` success claim, "validated" wording, suppressed exposure, altered
denominators, or a bypassed check.

## What the audit contains

- first, any must-fix finding delivered over an open critic objection (`psb critic override`), and
  any review extension the user granted ("Review budget extended at the user's request: <reason>",
  from `psb critic extend`)
- question, framework, concept roles, and whether the user confirmed the scope
- PRISMA-S search details: database and platform, date the counts were run, `as_of` bound, total
  records, limits with rationale
- the strategy line by line with counts, and as one line for copying into PubMed
- the fixed interpretation, then (after a held-out test) each held-out record with its screening
  reason and source, released from the private screening store
- development checks per set with purpose, missed development records and the blocks that miss them
- leave-one-block-out results and the development history
- critic rounds and finding status
- standard limitations and the provenance line

Do not edit `audit.md` or `final-query.txt`; their bytes are verified by the manifest. If something
is wrong, fix the workspace and run `psb report` again.

## Add these sections separately in `narrative.md`

1. **Rationale.** Why each concept is searched or screened; key MeSH decisions; notable text-word
   choices; why limits were used.
2. **How known records were found and allocated.** Sources, screening budget, how many screened and
   included, whether a separate screening context was used, the allocation (relay the numbers from
   `psb progress known-records`), and any release for repair.
3. **Critic dispositions.** For each finding: what changed, or why it was rejected or accepted.
4. **Open risks for the peer reviewer.** Fragile concepts, records out of reach, noisy terms kept on
   purpose, anything you were unsure about.
5. **Reporting format** (only when you used the escape hatch).

## PRISMA-S items this covers (PubMed only)

Items 1 (database), 8 (full strategy), 9 (limits and restrictions), 10 (search filters with
source), 13 (date of search), 16 (records per database). State item 12 (peer review) as
"internal PRESS-structured critic only; PRESS peer review pending". Items about other databases,
registries, citation searching and deduplication are outside this skill.

## Wording to use

- "development check" for retrieval of development records; "held-out test" only for
  `psb holdout-test`; "held-out records", never "held-out seeds" or "validation set"
- "relative recall against <set>" — never "sensitivity"
- "PRESS-structured internal critique", never "PRESS peer reviewed"
- If no known records existed, the fixed no-records text above.

## Failed or interrupted finalization

Read `validation.md`. Any technical blocker, incomplete check, missing/stale critic, missing
allocation or held-out receipt, or mandatory review without a disposition prevents final delivery.
`report --diagnostic` writes `diagnostic-audit.md`, returns `ok: false`, and does not issue a
protected query. Prior delivery files are preserved under `history/deliveries/`; every attempt is
kept under `attempts/`, and every held-out receipt under `holdout/`.

The manifest is published last. `psb status` checks its input, critic, receipt and artifact hashes;
missing, stale or interrupted receipts are not valid delivery. After a process crash, inspect
`.report.lock` and confirm the recorded process has stopped before removing that lock. A delivery
made under policy 1 (before held-out testing) still verifies and is labelled legacy; its recall
labels predate held-out testing and are never reported as an independent test.
