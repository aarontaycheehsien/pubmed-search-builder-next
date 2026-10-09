---
name: pubmed-search-builder-holdout-verbose
description: "Preview of pubmed-search-builder-next with known-record allocation, a one-shot held-out test, private screening in a separate context and optional verbose progress messages. Use only when the user asks for pubmed-search-builder-holdout-verbose by name. Build, review, or update a high-sensitivity PubMed/MEDLINE Boolean search strategy for a systematic review, scoping review, rapid review, or other evidence synthesis. Use when the user wants a recall-first PubMed search developed from a plain-language review question: concept analysis, MeSH and free-text vocabulary, testing against known relevant records, a PRESS-structured critique, and a PRISMA-S style audit. Also use to review an existing PubMed strategy or re-run one for a review update. Do not use it to answer the review question itself."
---

# PubMed search builder

You deliver a **draft PubMed search strategy and its audit**, ready for human PRESS peer review.
You never answer the review question, and you never search PubMed to summarise evidence.

All PubMed and MeSH work goes through one tool, run from the skill directory:

```bash
python scripts/psb.py --workspace <run-dir> <command> ...
```

Every command prints JSON. Every NCBI request is logged in the workspace automatically, and
`psb report` validates live and generates the query, audit and validation manifest. **Only report counts, PMIDs, MeSH headings
and recall figures that a `psb` command returned.** If you did not run it, do not claim it.

## Progress messages

The user follows the build through standard messages that `psb` writes. You relay them; you do
not write your own status updates.

- When a `psb` result contains `progress`, send `progress.text` to the user **verbatim**, as its
  own message, before anything you add. Do not reword, shorten, merge, reorder or add numbers.
  Any comment of yours goes after it and must not restate its numbers differently.
- At the end of each step, run `psb progress <stage>` and relay its text the same way. The
  stages are `intake`, `scope`, `known-records`, `vocabulary`, `test`, `critic` and `deliver`.
- `psb status` lists any stage summary that is due and not yet sent.
- The separate screening context's messages reach the user through `psb progress list`: relay the
  new ones when it returns (see `references/known-records.md`).
- When the user asks for more detailed (verbose) progress, run `psb progress mode verbose` once,
  relay its message, and read `references/verbose.md`. `psb progress mode standard` switches back.
- `psb progress` and `psb screen` write only their own logs (`progress.jsonl`,
  `screening.jsonl`, `candidates.jsonl`). These sit outside every evaluation, critic and
  delivery hash.

## Workflow

Copy this checklist into your notes and work through it in order.

```
[ ] 1 Intake           question, seeds, depth, limits (one message)       -> psb progress intake
[ ] 2 Scope            protocol.json: concepts, roles, eligibility; confirm -> psb progress scope
[ ] 3 Known records    discover, screen, choose the allocation (psb allocate) -> psb progress known-records
[ ] 4 Vocabulary       MeSH + free text per searched concept               -> psb progress vocabulary
[ ] 5 Develop & revise psb eval, fix misses and noise, one at a time        -> psb progress test
[ ] 6 Critic           fresh-context PRESS review; answer every finding    -> psb progress critic
[ ] 7 Deliver          psb holdout-test (if held out), psb report, deliver unchanged, offer repair
                                                                           -> psb progress deliver
```

### 1. Intake

You need a plain-language review question. If you do not have one, ask for it and stop.
If the user pasted a Boolean strategy, still ask for the question: the strategy is the object
under review, never evidence of scope.

In one message, also ask for: known relevant articles (PMIDs, DOIs, PMCIDs; optional), the
depth (`quick`, `standard` or `thorough`; default `standard`), and any required limits such as
dates or languages. That message is the text of `psb progress intake-request`; add
`--have-question` when you already have the question. When the user says to proceed without
answers, use the defaults and record the assumptions in `protocol.json` `notes`.

Create the workspace: `psb init <run-dir> --question "..."`. Keep all build files inside it.
Record the depth, limits and notes in `protocol.json`, then run `psb progress intake`.

### 2. Scope

Read `references/scope.md`. Fill `protocol.json`:

- `concepts`: each candidate concept with `id`, `name`, `role` and `rationale`.
  Roles: `search` (an AND-ed block), `screen` (handled at screening, not searched), `optional`
  (a possible block to test, not in the main strategy).
- `eligibility`: include and exclude criteria for screening.
- `limits`: only limits the question truly requires, each with a reason.

Only AND a concept that passes the admission test in `references/scope.md`; when in doubt, do
not AND it. Outcomes, comparators, settings and study designs are usually `screen`.
A block that names one direction of a process (switching back) is fragile; search the process.
Every member the criteria list for a concept is searched by its own name.
Decide roles from the question before reading any seed record.

Run `psb progress scope` and relay its text verbatim. It shows every concept in a fixed table of
searched, screened and optional concepts, then the limits and eligibility criteria, explains
what each role means, and asks the user to keep the scope or say what to change. Do not restate
the table or explain the roles in your own words; put any ambiguity question after the message.
Then wait for the reply:

- **keep** (or another clear approval): set `scope_confirmed` and run `psb progress scope` again.
- **a change**: update `protocol.json` and run `psb progress scope` again; it shows the revised
  scope and asks again.

If the user told you not to pause, relay the message, say that you are continuing, and record
that in `notes`.
Resolve high-impact ambiguity (population versus outcome, intervention versus exposure)
with the user; never pick one silently.

### 3. Known records

Read `references/known-records.md` and follow it. In short, with eligibility already fixed:

- Discover candidates: `psb resolve` for the user's identifiers; at `standard`/`thorough` depth
  prior reviews, precise pilots and neighbours (budget ~150/400); at `quick` depth targeted
  discovery up to ~30. A prior review's included studies come from its tables or supplements; its
  reference list gives candidates only.
- Screen every candidate and record every decision with `psb screen`, including a study `group`
  key for reports of one study. When your host can start a fresh context, let it discover and
  screen with `--screening` / `--context separate` (held-out records must never be shown to you).
  Its whole reply is one fixed sentence; you relay its messages from `psb progress list`, and you
  never read its files.
- Do not put eligible records into a set yet. Run `psb allocate --preview`: when it proposes a
  holdout, relay its message verbatim and record the user's choice (`psb allocate --keep-holdout`
  or `--all-development`; `--proceed-default` if they asked you not to wait). Otherwise
  `psb allocate` freezes everything for development. A user's designated test set:
  `psb allocate --reserve <PMIDs>`.
- Records that cannot be screened into the pool go on a comparison list (`--purpose comparison`).

Screened records may change vocabulary and even which concepts are AND-ed. They may never change
eligibility. If a record looks relevant but falls outside the scope, ask the user.

### 4. Vocabulary

Read `references/vocabulary.md`. For each `search` concept, build one block in `strategy.json`
whose `id` equals the concept `id`:

- MeSH: `psb mesh lookup`, then `psb mesh show` for entry terms, tree position, narrower
  headings, and exploded versus unexploded counts. Tag headings explicitly with `[Mesh]`.
- Free text in `[tiab]`: synonyms, entry terms, spelling variants, acronyms, plurals, safe
  truncation (at least four letters before `*`), and proximity where word order varies.
- Objective terms from development records: `psb terms rank` (held-out records are never mined).

Every block needs both a MeSH layer and a text-word layer, because records not yet indexed
have no MeSH.

### 5. Develop and revise

Run `psb eval --note "<what changed and why>"` after every meaningful change. It reports lint
and translation problems, a count for every line, development (and comparison) retrieval per set,
which blocks miss which records, leave-one-block-out ablation, and what changed since the previous
version. Held-out records are never evaluated here.

- For every missed development record, run `psb terms miss`, then fix the failing block or record
  why the record is out of reach. Never explain a miss away without looking.
- Never silently lose a previously retrieved known record (`since_previous.known_lost`).
  Either revert, or say in the note why the loss is acceptable.
- Cut noise only when the count justifies it and no known record is lost. Use line counts
  and `psb sample --purpose noise-check` to find noisy terms. Recall comes first.
- A block whose removal gains known records (ablation) is a sign of over-structuring:
  reconsider its role in `protocol.json`.
- `psb` refuses to show, fetch, sample, mine or probe reserved records. Never try to learn
  which records are held out or whether the strategy retrieves them.

A phrase-index warning is a mandatory review, not proof of zero hits. Read the phrase decision
tree in `references/validation.md`. Inspect the individual clause's translation; test a justified
rewrite or removal, or record a clause-specific acceptance. Never silently change word-order,
proximity, or morphology requirements to make a warning disappear.

### 6. Critic

Read `references/critic.md`. Run `psb critic packet` and give only that packet to a
fresh-context reviewer (a subagent, if your host has one). Save its JSON as
`critic/round-N.json`, then run `psb critic check`. Answer every finding: change the strategy
and re-run `psb eval`, or set `status` to `rejected` or `accepted-risk` with a `response`.
Every depth requires a current critic: up to one revision round at `quick`, two at `standard`,
three at `thorough`, then one closing round. Before the last revision round, make every change
you plan and run `psb report --diagnostic` to see what still blocks delivery: that round should
review the strategy you mean to deliver. If it asks for changes, make them, `psb eval`, and run
`psb critic packet` once more: the closing round only verifies how each earlier finding was
handled and cannot raise new must-fix findings. Close substantive findings with explanations and
supply the packet's evidence-bound issue dispositions. Technical blockers cannot be accepted as
risks. If the closing round still asks for revision:

- fix what you can, `psb eval`, and run `psb critic packet` for the one verification round that
  may follow a closing round (it also covers any change you make after the closing round);
- for an open must-fix judgment you disagree with on evidence (kinds lexical, structural, scope,
  reporting), `psb critic override <id> --reason "..."`; the audit opens with the objection and
  your reason for the peer reviewer. Syntax and filter findings cannot be overridden;
- if nothing changed but `psb report` finds the review stale after the verification round (PubMed's
  translation or indexing drifted), explain this to the user. Only if they explicitly ask,
  `psb critic extend --reason "..."` opens one more review period, once per build; the audit discloses
  it. Never run it on your own initiative;
- otherwise produce diagnostic output.

`psb status` shows the critic rounds left. `psb critic packet` refuses the last revision, closing or
verification round while technical blockers remain (fix them and `psb eval`; `--anyway` overrides).

If no fresh context is available, review the packet yourself and say so in the audit.

### 7. Deliver

Read `references/reporting.md` and `references/validation.md`. If records are held out, run
`psb holdout-test` once, after the critic review of the strategy you mean to deliver, and relay
its message verbatim. Then run `psb report` (`--fresh` is an equivalent spelling). It
revalidates every line and heading live, checks the current critic and the matching held-out
receipt, and writes `final-query.txt`, `audit.md`, and `validation-manifest.json` only if the
gate passes. Deliver the tested query **unchanged**, even when held-out records were missed; then
offer the repair. If the user wants it, `psb holdout-release --reason "..."` returns the held-out
records to development, the revised query gets a repair critic round, and it is delivered with the
fixed wording that it was not independently tested.
Deliver the generated query verbatim; do not reconstruct or edit it. Set `scope_confirmed` and
`notes` truthfully before the report. After `psb report` succeeds, change nothing in the
workspace. If you must, run `psb status`: it names what changed. A change to `notes` or
`scope_confirmed` needs only `psb report` again; any other change needs `psb eval`, the critic's
verification round, and `psb report`. Deliver only from this workspace; never copy it to start over. Keep narrative additions
in `narrative.md`, because changing the generated audit invalidates its manifest. Give the user:

- the text of `psb progress deliver`. It includes the strategy (single line, and line by line
  with counts), the fixed interpretation of the held-out test and development checks, and the
  statement that this draft needs PRESS peer review by an information specialist before use;
- after it, the open risks and limitations from `narrative.md`.

Never write your own interpretation of a retrieval result such as `x/x`. For a format the user
asked for, the escape hatch in `references/reporting.md` applies to your own prose only.

## Rules

1. The question defines scope. Seeds, discovered records and existing strategies never do.
2. Report only numbers, headings and PMIDs that `psb` returned in this workspace.
3. Every searched concept has MeSH plus `[tiab]` terms. Do not rely on Automatic Term Mapping.
4. No limits, filters, `NOT`, `[majr]`, subheadings or `:noexp` without a stated reason.
   Use validated filters (`references/filters.md`), never ad hoc study-design blocks.
5. Mine terms only from development records. Held-out records are never mined, shown or probed;
   comparison lists are not mined.
6. Label evidence honestly: a development check is not independent validation, a held-out `x/x`
   does not establish high recall, relative recall is not sensitivity, and the internal critic is
   not PRESS peer review. Relay `psb`'s fixed interpretation instead of writing your own.
7. Read `references/anti-patterns.md` before you finalise the scope and again before you deliver.
8. Deliver a final query only after `psb report` returns `ok: true`. Otherwise fix the named
   blockers and re-evaluate, or give `psb report --diagnostic` output explicitly labelled unfinished.
   Do not hand-author a final query file or bypass the gate because retrieval counts look plausible.

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
| Known records | seeds, targeted discovery up to ~30 screened | seeds + discovery, ~150 screened | seeds + discovery, ~400 screened |
| Held-out test | never automatic; a user's test set means switching to standard | proposed when N ≥ 10 and U > 0 | as standard |
| Term mining | development records, if any | yes | yes, plus `psb terms miss` on every miss |
| Critic rounds | 1 + closing (+ verification) | 1-2 + closing (+ verification) | 1-3 + closing (+ verification) |
| Repair after the held-out test | — | 1 + closing (+ verification) | 1 + closing (+ verification) |
