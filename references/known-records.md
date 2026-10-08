# Known relevant records

Recall can only be measured against records you already know are relevant. How you found them
decides what the number means, so each set has a role.

| Role | What it is | Use for mining? | What its recall means |
|---|---|---|---|
| `seed` | articles the user supplied | yes | development check; not independent |
| `relevant` | records you screened in during the build | yes | development check; not independent |
| `validation` | relevant records held out from mining | no | semi-independent (it is still consulted every eval) |
| `benchmark` | included studies of a prior review, screened for your scope | no | external relative recall |

`psb eval` reports recall for every set. Records not in PubMed (or added after `as_of`) are
excluded from the denominator and listed.

## Seeds

- Resolve DOIs and PMCIDs with `psb resolve`; add PMIDs with `psb set add seeds ... --role seed`.
- Fetch them (`psb fetch --set seeds`) after the concept roles are set. If a seed looks outside
  the scope, ask the user whether to keep it; do not widen the scope to fit it.

## Finding more records (standard and thorough depth)

Budget: screen at most about 150 candidates at `standard` and 400 at `thorough`.

1. **Prior reviews.** Search for systematic reviews on the topic with
   `psb sample --purpose prior-reviews "<precise topic query> AND systematic[sb]"`. If one
   matches your scope, its included studies are the strongest benchmark.
   Get them from the user, the review's reference list (`psb neighbors <review PMID> --links refs`),
   or its tables, and screen each against your eligibility criteria. Save them as `benchmark`.
   A review of a broader or parent topic (forward switching, when you want switching back) is
   still worth mining for candidates: its included studies may report your topic as a subgroup.
2. **Precise pilots.** Run two or three narrow, high-precision queries (the core concepts in
   titles, for example) with `psb sample --purpose pilot`, and screen what they return.
3. **Neighbours.** `psb neighbors --set seeds --links similar,citedin --exclude-known` ranks
   records linked to several known records first. Screen before use.

## Screening candidates

Screen each candidate's title and abstract (`psb fetch <pmids> --abstracts`) against the
`eligibility` criteria in `protocol.json`:

- include only when the record clearly meets every criterion you can judge from the abstract;
- mark uncertain records uncertain and leave them out of every set;
- keep a short reason for each include (it goes in the set's `note` or your working notes).

Record every decision, including excludes and uncertain records:
`psb screen --include ... --exclude ... --uncertain ... --reason "..."`. For a reason per
record, pass `--file decisions.json`, a list of `{pmid, decision, reason}`. The record only feeds
the progress messages: the screening counts, the source of each candidate and the budget used.
It never adds a record to a set.

Add includes with `psb set add relevant ... --role relevant --source "similar articles of seeds"`.
Never add unscreened pilot hits or neighbours to a set: they are candidates, not evidence.

## Holding records out

When development records reach about 10 or more, run `psb set split seeds --fraction 0.3` (or on
`relevant`) before mining. Do not mine the `validation` set. If you later add terms because of
a validation miss, report that the set became part of development.

## When you have nothing

With no seeds, no matching prior review, and nothing screened in, say so plainly: the strategy is
empirically unvalidated, recall is not estimated, and the audit must state it. Ask the user
whether they can supply known articles or name a related review before you continue, unless
this is a quick search without seeds or the user asked you to proceed with documented
assumptions. Those cases may proceed without recall measurement; record that limitation.
