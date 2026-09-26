---
name: pubmed-search-builder-next
description: "Build, review, or update a high-sensitivity PubMed/MEDLINE Boolean search strategy for a systematic review, scoping review, rapid review, or other evidence synthesis. Use when the user wants a recall-first PubMed search developed from a plain-language review question: concept analysis, MeSH and free-text vocabulary, testing against known relevant records, a PRESS-structured critique, and a PRISMA-S style audit. Also use to review an existing PubMed strategy or re-run one for a review update. Do not use it to answer the review question itself."
---

# PubMed search builder

You deliver a **draft PubMed search strategy and its audit**, ready for human PRESS peer review.
You never answer the review question, and you never search PubMed to summarise evidence.

All PubMed and MeSH work goes through one tool, run from the skill directory:

```bash
python scripts/psb.py --workspace <run-dir> <command> ...
```

Every command prints JSON. Every NCBI request is logged in the workspace automatically, and
`psb report` builds the audit from the workspace. **Only report counts, PMIDs, MeSH headings
and recall figures that a `psb` command returned.** If you did not run it, do not claim it.

## Workflow

Copy this checklist into your notes and work through it in order.

```
[ ] 1 Intake        question, seeds, depth, limits (one message to the user)
[ ] 2 Scope         protocol.json: concepts and roles; confirm with the user
[ ] 3 Known records sets of relevant PMIDs (seeds, screened discoveries, benchmark)
[ ] 4 Vocabulary    MeSH + free text for each searched concept -> strategy.json
[ ] 5 Test & revise psb eval, fix misses and noise, one change at a time
[ ] 6 Critic        fresh-context PRESS review; address every finding
[ ] 7 Deliver       psb report --fresh; hand off for PRESS peer review
```

### 1. Intake

You need a plain-language review question. If you do not have one, ask for it and stop.
If the user pasted a Boolean strategy, still ask for the question: the strategy is the object
under review, never evidence of scope.

In one message, also ask for: known relevant articles (PMIDs, DOIs, PMCIDs; optional), the
depth (`quick`, `standard` or `thorough`; default `standard`), and any required limits such as
dates or languages. When the user says to proceed without answers, use the defaults and record
the assumptions in `protocol.json` `notes`.

Create the workspace: `psb init <run-dir> --question "..."`. Keep all build files inside it.

### 2. Scope

Read `references/scope.md`. Fill `protocol.json`:

- `concepts`: each candidate concept with `id`, `name`, `role` and `rationale`.
  Roles: `search` (an AND-ed block), `screen` (handled at screening, not searched), `optional`
  (a possible block to test, not in the main strategy).
- `eligibility`: include and exclude criteria for screening.
- `limits`: only limits the question truly requires, each with a reason.

Only AND a concept that passes the admission test in `references/scope.md`; when in doubt, do
not AND it. Outcomes, comparators, settings and study designs are usually `screen`.
Decide roles from the question before reading any seed record.

Show the user a short table of concepts, roles and limits, and ask them to confirm. Set
`scope_confirmed` when they do. If they asked you not to pause, proceed and say so in `notes`.
Resolve high-impact ambiguity (population versus outcome, intervention versus exposure)
with the user; never pick one silently.

### 3. Known relevant records

Read `references/known-records.md`. Known relevant records are how you measure recall, so
build these sets before drafting (skip at `quick` depth when there are no seeds):

- `psb resolve` for DOIs or PMCIDs, then `psb set add seeds ... --role seed`.
- At `standard` or `thorough` depth with few seeds, find more: prior systematic reviews on the
  topic (their included studies make the best benchmark), precise pilot searches, and
  `psb neighbors`. Screen candidates against the eligibility criteria before they enter a set.
- With 10 or more development records, hold some out: `psb set split seeds --fraction 0.3`.

Seeds and screened records may change vocabulary and even which concepts are AND-ed. They may
never change eligibility. If a record looks relevant but falls outside the scope, ask the user.

### 4. Vocabulary

Read `references/vocabulary.md`. For each `search` concept, build one block in `strategy.json`
whose `id` equals the concept `id`:

- MeSH: `psb mesh lookup`, then `psb mesh show` for entry terms, tree position, narrower
  headings, and exploded versus unexploded counts. Tag headings explicitly with `[Mesh]`.
- Free text in `[tiab]`: synonyms, entry terms, spelling variants, acronyms, plurals, safe
  truncation (at least four letters before `*`), and proximity where word order varies.
- Objective terms from known records: `psb terms rank` (never from held-out sets).

Every block needs both a MeSH layer and a text-word layer, because records not yet indexed
have no MeSH.

### 5. Test and revise

Run `psb eval --note "<what changed and why>"` after every meaningful change. It reports lint
and translation problems, a count for every line, recall per set, which blocks miss which
records, leave-one-block-out ablation, and what changed since the previous version.

- For every missed known record, run `psb terms miss`, then fix the failing block or record
  why the record is out of reach. Never explain a miss away without looking.
- Never silently lose a previously retrieved known record (`since_previous.known_lost`).
  Either revert, or say in the note why the loss is acceptable.
- Cut noise only when the count justifies it and no known record is lost. Use line counts
  and `psb sample` to find noisy terms. Recall comes first.
- A block whose removal gains known records (ablation) is a sign of over-structuring:
  reconsider its role in `protocol.json`.
- Recovering a held-out validation miss makes that set part of development. Say so.

### 6. Critic

Read `references/critic.md`. Run `psb critic packet` and give only that packet to a
fresh-context reviewer (a subagent, if your host has one). Save its JSON as
`critic/round-N.json`, then run `psb critic check`. Answer every finding: change the strategy
and re-run `psb eval`, or set `status` to `rejected` or `accepted-risk` with a `response`.
Stop when no `must-fix` finding is open (at most two rounds at `standard`, three at `thorough`).
If no fresh context is available, review the packet yourself and say so in the audit.

### 7. Deliver

Run `psb report --fresh`. It re-runs the counts live and writes `audit.md`. Read
`references/reporting.md`, add the narrative sections it lists, and give the user:

- the strategy (single line and line by line with counts),
- recall on each known set, with how independent each set is,
- open risks, limitations, and the statement that this draft needs PRESS peer review by an
  information specialist before use.

## Rules

1. The question defines scope. Seeds, discovered records and existing strategies never do.
2. Report only numbers, headings and PMIDs that `psb` returned in this workspace.
3. Every searched concept has MeSH plus `[tiab]` terms. Do not rely on Automatic Term Mapping.
4. No limits, filters, `NOT`, `[majr]`, subheadings or `:noexp` without a stated reason.
   Use validated filters (`references/filters.md`), never ad hoc study-design blocks.
5. Mine terms only from `seed` and `relevant` sets, never from `validation` or `benchmark`.
6. Label evidence honestly: development recall is not independent validation, relative recall
   is not sensitivity, and the internal critic is not PRESS peer review.
7. Read `references/anti-patterns.md` before you finalise the scope and again before you deliver.

## Other modes

- **Review an existing strategy:** get the question first (step 1), write the concepts, then
  transcribe the strategy into `strategy.json` blocks and run steps 5 and 6. Report findings;
  do not rewrite it unless asked.
- **Update a finished search:** set `as_of` in `protocol.json` to the previous search date to
  reproduce the original count, then clear it and re-run `psb eval` to see the growth. Report
  changes in PubMed's translation (`translation_issues`) before trusting the new numbers.

## Depth

| | quick | standard (default) | thorough |
|---|---|---|---|
| Known records | seeds if given | seeds + discovery or a prior-review benchmark | both, larger screening budget |
| Term mining | if seeds | yes | yes, plus `psb terms miss` on every miss |
| Critic rounds | 0-1 | 1-2 | up to 3 |
