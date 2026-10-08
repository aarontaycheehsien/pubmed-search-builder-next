# Plan: known-record allocation, a one-shot held-out test, and fixed interpretation messages

Status: implemented on branch `worktree-holdout-allocation`. Baseline at `704317b`: 214 passed,
1 skipped; after the change: 303 passed, 1 skipped, and the skill validator passes.

## As built: differences from the text below

- **Held-out membership is never a set.** It lives only in `allocation.json` (with later events in
  `allocation-log.jsonl`). There is no `sets/holdout.json`, so no command that lists, mines or
  evaluates sets can reach a reserved record.
- **A user's designated test set is given as PMIDs** (`psb allocate --reserve <PMIDs>`), not as a set
  name.
- **The six interpretation lines are a Markdown list** (`- **Allocation:** …`). Plain consecutive lines
  collapse into one paragraph when Markdown is rendered.
- **`psb allocate --rebind`** is the command that re-binds a stale allocation after re-screening.
- **Exposure "after the reservation"** is ordered by position in `exposure.jsonl`, not by timestamp.
- **The manifest stores the delivered interpretation text** (`holdout.text`). The Step 7 message relays
  those bytes, which is how it matches the audit.

The plan resolves four decisions:

- (a) The comparison list holds records that never entered the allocation pool: legacy
  `validation`/`benchmark` sets and unscreened user lists.
- (b) A set the user designates replaces the automatic holdout.
- (c) The command is `psb holdout-test`.
- (d) `POLICY_VERSION` goes to `"2"`, with a read path for legacy receipts.

## 0. Ground rules

- **Work in a git worktree on its own branch.** `~/.claude/skills/pubmed-search-builder-next`
  and `~/.codex/skills/pubmed-search-builder-next` are symlinks to this checkout, so any edit
  here goes live immediately. Merge only when the whole suite passes.
- **Do not modify:**
  - `runs/`
  - `evals/results/`
  - the `history/` and `attempts/` folders inside any workspace
  - `~/.claude/skills/_backups` and `~/.codex/skills/_backups`
  - the older, separate skill at `~/.codex/skills/pubmed-search-builder`
  - `IMPLEMENTATION_PLAN.md`, which is the record of earlier work
- **Never rewrite legacy files.** Map legacy labels when they are read, so policy-1 hashes still
  verify.
- **Every phase in §8 ends with the full offline suite passing.**

## 1. Workflow and terminology

Keep the seven numbered steps. The progress messages, `psb status` reminders and the golden test
all depend on them.

| Step | Name | What changes |
|---|---|---|
| 1 | Intake | Unchanged. |
| 2 | Scope | Eligibility is fixed here, before any supplied paper is examined. |
| 3 | Known records | Discover → screen → **choose allocation** (`psb allocate`). |
| 4 | Vocabulary | Mining uses development records only. |
| 5 | **Develop & revise** (was "Test & revise") | Stage key stays `test` for legacy `progress.jsonl`. |
| 6 | Critic | Development evidence only. |
| 7 | Deliver | **`psb holdout-test`** when a holdout exists → `psb report` → deliver unchanged → offer repair. |

In short: scope → discover/screen → choose allocation → develop and check → critic → held-out
test when applicable → deliver unchanged → offer repairs.

### Terms

| Term | Meaning |
|---|---|
| Candidate records | Found by a discovery search; not yet assessed for eligibility |
| Eligible reference records | Screened as eligible for this question; together they form the allocation pool |
| Development set | Used for term mining, diagnosing misses and repeated retrieval checks |
| Held-out test set | Reserved and unseen by the builder; used for one retrieval test of the frozen query |
| Comparison list | Records outside the allocation pool whose eligibility or separation cannot be established under this workflow: legacy `validation`/`benchmark` sets and user-supplied lists that were not screened. They are checked and reported separately, are not mined by default, and are never a held-out test. |

### Wording rules

- A development retrieval result is a **check**. **Test** means only the held-out test.
- Say "held-out records" or "held-out test set". Never call anything the builder has seen
  "validation".
- "Seeds" stays an informal word for papers the user supplied.
- "Held-out topics" belongs to the evaluation harness (`evals/splits.json`) and is never used
  for workspace records.

### Origin

Origin is stored separately from purpose, and a record may have several:

- `user-supplied`, including identifiers converted by `psb resolve`
- `prior-review`
- `pilot-search`
- `similar-articles`, which ranks by text and MeSH similarity and is not a citation search
- `citation-backward`
- `citation-forward`

Origin never establishes independence. The test-material line reports the mix of origins and
flags `similar-articles` and `pilot-search`, because both share vocabulary with development
records or with queries the builder wrote.

### Where content lives

| Content | Location |
|---|---|
| Workflow entrypoint | `SKILL.md`, kept concise |
| Allocation procedure | `references/known-records.md` |
| Message text | Rendered by `psb` (new `scripts/psb/interpret.py`, plus `progress.py`) and relayed verbatim |
| Copy of the message text | `references/reporting.md`, with a parity test asserting it matches the renderer |

## 2. Discovery and allocation by depth

### Quick

- Screen the supplied papers. The builder may screen them; they are then exposed and go to
  development.
- Targeted extra discovery is allowed, up to **30 screened candidates** (`SCREEN_BUDGET["quick"] = 30`).
- `psb allocate` freezes everything as development. There is no automatic holdout and no
  choice prompt.
- Report development retrieval only.
- **Papers the user reserves are never mined.** Ask once:

  > A held-out test is a standard-depth step. Switch to standard depth and keep these papers
  > reserved, or use them for development?

  If the user cannot be asked, switch to standard depth, keep the papers reserved, and record
  the assumption in `protocol.notes`.

### Standard and thorough

- **Discovery.** Use prior reviews, two or three complementary precise queries, and
  similar-article and citation searches. The screening budgets stay at about **150 / 400**.
- **Prior reviews.** Confirm inclusion from the included-studies table or a supplement. A
  reference list supplies candidates only. `psb` cannot read full text, so the table comes from
  the user or another tool; otherwise the records stay candidates.
- **Screening record.** For every candidate, store:
  - the decision and reason
  - the source reference (for example "Table 2 of PMID 123")
  - the evidence basis (title/abstract or full text)
  - the screening context (`separate` or `builder`)
  - the study group key
  - whether the record is available at the effective `as_of` date
- **Pool.** Leave uncertain, ineligible, unresolved and unavailable records out of the pool.
  Deduplicate PMIDs.
- **Study groups.** Keep known reports of the same study together. The group key is a
  registration ID or a note from the screener. Where grouping is unknown, each PMID is its own
  unit and the limitation is disclosed.

### Screening context and exposure

- When a separate screening context exists (a subagent or a separate session), it runs both
  discovery and screening for candidates, using `--screening`. Its outputs and reasons go to the
  private store, `screening/`. The builder sees only PMIDs, decisions, origins and groups.
  Reasons and source references are released to the audit after the held-out test; for
  development units, they are released at allocation.
- **Exposed.** A study group is exposed if the builder has seen any member's title, abstract,
  indexing, full text, search-relevant description, or retrieval feedback.
  - `psb` derives exposure from its own commands. It appends an event to `exposure.jsonl`
    whenever a builder-facing `fetch`, `sample`, `terms rank`, `terms miss`, or `eval` set
    membership shows content or feedback.
  - The agent declares any other exposure with `psb exposure declare`.
  - **Exposure is unknown unless** every member was screened in the separate context and no
    exposure event exists. Unknown exposure counts as exposed.
  - Handling a PMID alone, or a fetch by the screener into the private store, is not exposure.
- **Exposed groups go to development.** Moving a record out of a set after the builder has seen
  it does not restore independence, so `psb set split` is withdrawn (§3).
- **With no separate context,** every screened record is exposed. Then U = 0, no holdout is
  proposed, and the report says why.
- **Eligible records stay out of sets until allocation.** Running an evaluation with them in a
  set would expose them through retrieval feedback.
- **Exposure control is procedural.** `psb` refuses, redacts and records. The files are not a
  security boundary, and the builder must not read `screening/`.

### Automatic allocation

Let `N` be the number of eligible allocation units and `U` the number of unexposed units.

| Condition | Proposed allocation |
|---|---|
| `N = 0` | No record-based retrieval check |
| `N < 10` | All development |
| `N ≥ 10`, `U = 0` | All development |
| `N ≥ 10`, `U > 0` | Holdout `H = min((3N + 5) // 10, U)`; development `N − H` |

- **The draw.** A unit's ID is its lowest PMID. Order the unexposed units by
  `sha256(f"{seed}:{unit_id}")` and take the first `H`. The default seed is `1`. Record the seed
  and the method `sha256-order-v1`, which, unlike `random.sample`, is stable across Python
  versions.
- **Examples.**

  | Units | Unexposed | Development / held-out |
  |---|---|---|
  | 10 | all | 7/3 |
  | 15 | all | 10/5 (halves round up) |
  | 20 | all | 14/6 |
  | 20 | 2 | 18/2 |
  | 8 | any | 8/0 |

- The ten-unit trigger and the 30% fraction are operational defaults, not adequacy thresholds.
  There is no minimum of three.
- **A user-designated test set replaces the automatic holdout.** It is held out as given after
  its eligibility is screened in the separate context. Ineligible papers are removed and listed,
  and any prior exposure is disclosed. Every other eligible unit goes to development, and the
  choice prompt is not shown.

### Allocation-choice message

`psb allocate --preview` renders this message as a Step 3 progress event, only when a holdout
is proposed. It is shown once, before any mining or release of reserved content.

> **Choose how to use the eligible reference records**
>
> Eligible pool: **{records} records representing {studies, or "an unverified number of studies"}.**
>
> - **Development: {units} units ({records} records)** — used for term mining, diagnosing misses, and improving the search.
> - **Held-out test: {units} units ({records} records)** — reserved for one retrieval check after the query is finalised.
>
> **Separation:** {exposure status}.
>
> A held-out check can reveal retrieval gaps. Retrieving every reserved record would show that the query found those records; it would not establish that all relevant literature was found. The reassurance depends on the test's size, coverage, and separation from development.
>
> **Keep the proposed holdout**, or **use everything for development**?
>
> Using everything provides more development material but leaves no independent final test.

How the reply is recorded:

- `--keep-holdout` records "keep".
- `--all-development` records "use everything".
- An earlier explicit choice is honoured without asking again.
- If the user asked not to be questioned, `--proceed-default` keeps the holdout and records the
  assumption.
- When no holdout is proposed, the user is not asked, and the frozen summary states the reason.

### After the freeze

- **`allocation.json` is immutable.** It binds the units, purposes, N, U, H, seed, method,
  choice, and the hashes of eligibility, `as_of` and the policy.
- **Later discoveries go to development**, with one exception. A report whose screening group
  matches a reserved group is refused by `set add`. It is kept as a *late companion*: never
  mined and outside the frozen denominators. If the builder saw its content, that group is
  recorded as exposed, and the exposure qualification applies.
- **No redraw based on retrieval results.** Accidental exposure is recorded. Records are never
  replaced, and denominators never change because of an outcome.
- **A change to eligibility or `as_of` makes the allocation stale.** `holdout-test` then
  refuses until the reserved records are re-screened in the separate context, or their
  availability is checked again. Removals are disclosed; nothing is added.

## 3. Helper changes

### Data

| File | Change |
|---|---|
| `sets/<name>.json` | `purpose` ∈ `development \| holdout \| comparison`. Legacy roles are mapped on read: `seed`, `relevant` → development; `validation`, `benchmark` → comparison, labelled "legacy: consulted during development". The file is not rewritten. |
| `screening.jsonl` | Adds `context`, `group`, `origin`, `evidence_basis`, `available`. Reasons and source references for separate-context decisions move to `screening/decisions.jsonl`. |
| `screening/` (new) | Private store: `records.jsonl`, `.cache/`, `decisions.jsonl`. |
| `exposure.jsonl` (new) | Automatic and declared exposure events. |
| `allocation.json` (new) | The frozen allocation. `sets/development.json` and `sets/holdout.json` are created from it. |
| `holdout/receipt-N.json` (new) | Held-out test receipts. They are never deleted. |

### Commands

- **`set add`**
  - `set add NAME PMIDS --purpose development|comparison --origin ...`. `--role` still accepts
    the legacy names.
  - `--purpose holdout` is refused, because only `allocate` creates a holdout.
  - Before allocation, adding a record to a development set records it as exposed.
- **`psb screen`** gains `--context separate|builder`, `--group`, `--evidence`, `--source-ref`
  and `--origin`. The same fields are accepted in `--file`.
- **`--screening`** is added to `fetch` and `sample`. Results go to the private store, and no
  exposure event is recorded. Only the separate screening context may pass this flag, and its
  use is reported as *declared*.
- **`psb exposure declare PMIDS --kind title|abstract|indexing|full-text|description|feedback --note`.**
- **`psb allocate`**
  - Options: `--preview`, `--keep-holdout`, `--all-development`, `--proceed-default`,
    `--reserved-set NAME`, `--seed N`.
  - Required whenever the workspace has known records, at every depth. With N = 0 it records an
    empty allocation, so the "no records" message is based on recorded state.
- **`psb holdout-test`** (§3, *Held-out test*) and **`psb holdout-release --reason "..."`** (§3, *Repair*).
- **`psb set split`** now fails, with a message that it cannot create an independent test and a
  pointer to `psb allocate`.
- **`terms rank`.** `--allow-held-out` becomes `--include-comparison`. A holdout can never be mined.

### Central guard (new `scripts/psb/reserved.py`)

- `ws.reserved()` reads the holdout. `ws.sets()` and `mining_pmids()`, the builder's view,
  exclude it.
- One function, `guard(pmids, action)`, handles every builder-facing path:
  - `fetch`, `terms rank/miss` and `neighbors --set` refuse reserved PMIDs.
  - `sample` and `neighbors` output show `[reserved]` in place of reserved rows. This includes
    noise checks of the developing query, which will return reserved records.
  - `count` and `sample` refuse queries that probe reserved PMIDs through `[uid]` or `[pmid]`.
- Development and comparison evidence only, in:
  - `evaluate` (sets, misses, ablation, block recall)
  - `compare`
  - `known_records_missed`
  - `review_fingerprint`
  - the critic packet, which shows only "H units reserved"
  - `psb status`
  - progress recall lines
  - `diagnostic-audit.md`
- `input_snapshot` carries `allocation_sha256` rather than the members of the holdout.
- An exposure that is blocked or detected after the freeze is appended to `exposure.jsonl`.

### Held-out test (`psb holdout-test`)

- **Preconditions:**
  - the allocation is frozen with H > 0 and is not stale
  - the latest evaluation is complete
  - `review_gate` shows no blockers, the same critic check that `report` applies
- **Binding:**
  - the effective query
  - `review_sha256`
  - inputs, excluding `notes` and `scope_confirmed`
  - `as_of`
  - `allocation_sha256`
  - the eligibility hash
  - `POLICY_VERSION`
  - `TEMPLATE_VERSION`
- **One receipt per binding.** A repeat run returns the stored receipt.
- **A new receipt only when the binding changes for a reason other than a strategy edit.** This
  covers drift in PubMed's translation or the vocabulary. Every receipt is kept and listed in
  the audit.
- **Changing the strategy after a receipt** is refused by `holdout-test` and `report` until
  `holdout-release`.
- **Receipt contents:**
  - records retrieved / eligible and, when grouping is verified, studies retrieved / eligible
    (a study counts as found if any of its reports is found)
  - missed PMIDs
  - origin mix
  - screening contexts and evidence basis
  - grouping status
  - exposure events
  - dates
- **Status `complete`, `empty` or `incomplete`.**
  - `empty` means no reserved record is available at `as_of`.
  - `incomplete` means a service failure. No partial counts are stored or shown, and the run may
    be repeated.

### Report

- With a holdout, `psb report` requires a `complete` or `empty` receipt that matches. An
  `incomplete` receipt blocks the report like any other incomplete check. Without a holdout,
  the report uses the allocation's reason.
- The report never re-scores the holdout. Holdout misses never create `review_required` issues,
  so they cannot start a revision cycle.
- The audit's "Held-out test" section, the `holdout-test` progress message and the
  `progress deliver` message are all rendered by `interpret()` from the stored receipt.
- The manifest records `holdout_receipt_sha256`.
- Technical delivery checks are unchanged.

### Repair (`psb holdout-release --reason`)

- The release:
  - marks the allocation as released
  - moves the held-out units to development
  - keeps the receipt (`released: true`)
  - opens critic **epoch** n+1
- Critic rounds carry `epoch`. `next_round`, `review_gate` and `_closing_problems` count each
  epoch separately. A repair epoch allows one revision round, then a closing round and a
  verification round, at every depth. A repair is targeted, and the strategy has already been
  reviewed once.
- The audit of a repaired delivery shows the original receipt as history and uses the
  repaired-delivery wording (§4). It never makes an x/x claim for the revised query.

### Legacy

- `POLICY_VERSION = "2"`.
- `verify_delivery` checks a policy-1 manifest with the preserved policy-1 snapshot function,
  `input_snapshot_v1`. It reports "legacy delivery (policy 1): its recall labels predate
  held-out testing", not "not current".
- A legacy `validation` set is never presented as a held-out test.

## 4. Fixed interpretation messages

`interpret(state) -> str` in `scripts/psb/interpret.py` picks the case and fills the template.
The agent relays the text verbatim and never writes its own interpretation of a result such as
`x/x`.

The message always has six labelled lines:

> **Allocation:** {development units/records}; {held-out units/records}; {choice}.
> **Result:** {result, or unavailable status}.
> **Test material and separation:** {origins; screening context and evidence basis; grouping; exposure; reserved and tested dates; `as_of`}.
> **Interpretation:** {case text below, plus the exposure qualification when it applies}.
> **Size context:** {calculation or limitation}.
> **Delivery and next step:** {delivery text}.

The `{choice}` value is one of:

- you kept the proposed holdout
- you chose to use every record for development
- the proposed holdout was kept by default (you asked me not to wait for answers)
- your designated test set
- no holdout was proposed: {fewer than 10 eligible units | no unexposed units | quick depth}

The case is chosen by record-level results, which is conservative: a missed report counts as a
gap even when another report of the same study was retrieved. When grouping is verified, the
Result line also shows the study-level figure.

### Every held-out record retrieved: `x/x`, x > 0

> The frozen query retrieved all **{x} eligible held-out records**. This check exposed no retrieval failures. It establishes successful retrieval of these records, not complete retrieval of all relevant literature. A result of **{x}/{x}** does not by itself establish high overall recall.

Size context, when every held-out unit is one record with an explicit group key from the
screener and all keys are distinct:

> For scale only: a search that misses **5%** of relevant studies would still retrieve all **{x}** test studies about **{p}%** of the time, assuming independent, representative sampling. This is an illustration of the test's ability to detect misses, not an estimate of this search's actual recall.

Otherwise:

> A numerical sample-size illustration is omitted because these records cannot be treated as verified independent study observations. Multiple reports of one study do not provide the same information as the same number of distinct studies.

Then always:

> The test may also underrepresent terminology or study types missing from the sources used to assemble it. Increasing its size does not by itself remove that selection limitation.

How `{p}` is computed:

- `Decimal("0.95") ** x * 100`, rounded half-up to one decimal place.
- `<0.1%` when the unrounded value is below 0.1.
- Required examples:

  | x | p |
  |---|---|
  | 2 | 90.3% |
  | 3 | 85.7% |
  | 6 | 73.5% |
  | 134 | 0.1% |
  | 135 | <0.1% |

Never report only "100% recall" or "validation passed".

### Some or all missed: `r/x`, r < x (including r = 0)

> The frozen query retrieved **{r}/{x} eligible held-out records** and missed **{x−r}**. This demonstrates a retrieval gap among these test records. The observed proportion describes this reference set; it is not a reliable estimate of recall across all relevant literature without suitable sampling and independence.

Size context: the selection-limitation sentence above.

### No held-out test, N > 0

> These records were available for developing or improving the search. Their retrieval is a development check, not independent validation. No held-out retrieval test was performed.

The Test material line gives the reason. Size context and Delivery are "Not applicable: no
held-out test was performed."

### No eligible records, N = 0

> No eligible reference records were available, so no record-based retrieval check was performed. Recall was not estimated; the strategy is empirically unvalidated.

### Incomplete test or empty denominator

> No interpretable held-out retrieval result is available because **{reason}**. Do not interpret this as zero recall or a successful test.

Only `empty` reaches delivery. `incomplete` blocks the report (§3, *Report*).

### Exposure qualification

Appended whenever any held-out unit has an exposure event, whether it was there before the
designation or happened by accident later:

> **Independence limitation:** {specific exposure or uncertainty}. These results must not be described as an unexposed independent test.

### Comparison lists

One line per list, shown outside the six-line block:

> **{name}:** {r}/{x} retrieved. These records were not screened into the allocation pool for this question (or were consulted throughout development in an earlier version of this skill), so this is a comparison, not a development check or an independent test.

### Delivery wording

After a completed test:

> The delivered query is the query that was tested and has not been revised using these results.

When records were missed, add:

> Investigating the missed records and repairing the search is available as a next step. Such a revision would use this test set for development and would require new unexposed records for another independent test.

After a repair:

> This query was revised after the held-out test, using the held-out records for development. The earlier result ({r}/{x}, receipt {id}) applies to the earlier query, not this one. No independent held-out test of this query was performed.

### Reporting-only escape hatch

- **Scope.** The escape hatch applies only to the agent's own prose: an additional chat message,
  or `narrative.md`. It never applies to relayed `psb` text, which stays verbatim, or to
  `audit.md`, which is hash-bound.
- **Allowed.** For a format the user requested, or an unusual case, the agent may shorten,
  combine or extend the templates there. It must preserve:
  - the observed result
  - the separation qualifications
  - the significance statement
  - the limitations
  - the next-step status

  Record the reason in a `narrative.md` section titled "Reporting format".
- **Never allowed:**
  - an unexplained `x/x` success claim
  - "validated" wording
  - suppressed exposure
  - altered denominators
  - bypassed checks

## 5. Documentation

| File | Change |
|---|---|
| `SKILL.md` | Seven-step checklist: Step 3 includes `allocate`, Step 5 is renamed, Step 7 adds `holdout-test` and the repair offer. Rules 5 and 6 use the new terms. Depth table: quick discovery up to 30, no automatic holdout. One line on relaying held-out messages verbatim, pointing to the escape hatch. Stays concise. |
| `references/known-records.md` | Rewrite: terms, origins, discovery by depth, verifying prior-review inclusion, the screening record, the separate-context procedure with a ready prompt for a screener subagent, exposure, pool rules, grouping, allocation, the choice, the freeze, late companions, user-designated sets, reserved papers at quick depth, comparison lists, the legacy mapping, and "when you have nothing". |
| `references/reporting.md` | Copy of the §4 texts (parity-tested), formatting rules, the order `holdout-test` → `report` → offer repair, the escape hatch, updated wording list, and `narrative.md` section 2 (how records were found and allocated). |
| `references/validation.md` | Receipt binding. `report` uses the stored receipt and never re-scores. Critic bindings cover development evidence only. Policy 2 and legacy receipts. |
| `references/critic.md` | The packet holds development evidence only. The critic is never shown holdout content. Repair-epoch budget. |
| `references/vocabulary.md` | Mine development records only. |
| `references/anti-patterns.md` | Mistake 5 ("Seed PMIDs are validation aids") becomes development aids. Mistake 6 covers development records. New mistakes: "Reading x/x as validation" and "Peeking at held-out records" (noise-check samples, `[uid]` probes, mining). |
| `README.md` | Purpose table instead of the role table (lines 118–127), the known-records steps, and the command table (`allocate`, `holdout-test`, `holdout-release`; `set split` withdrawn). Separate "held-out topics" in the harness from the workspace "held-out test set". |
| `evals/README.md` | Terminology note, and the new `gold_seen` / `gold_reserved` fields. |

## 6. Evaluation harness

- `gold_seen` counts members of development and comparison sets. A new field, `gold_reserved`,
  reports held-out members separately.
- The scorecard records, from `screening.jsonl`, whether a separate screening context was used,
  together with the allocation summary. A U = 0 run is then explained rather than counted as a
  skill failure.
- The existing harness prompt says the user cannot answer questions, which triggers
  `--proceed-default`. No prompt change is needed.

## 7. Verification

### New and updated tests

| Test file | What it checks |
|---|---|
| `test_allocation.py` | All N/U cases. Splits at N = 10, 15, 20 and 35. 18/2 and 8/0. A golden list of PMIDs selected by the hash draw for a fixed pool. Grouped units stay together. Reproducibility. Reserved papers at quick depth. A user-designated set replacing the automatic holdout. `--keep-holdout`, `--all-development`, `--proceed-default`. An earlier choice honoured. No prompt when no holdout is proposed. Stale allocation after an eligibility or `as_of` change. Late companions. |
| `test_reserved_guard.py` | Reserved PMIDs refused by `fetch` and `terms`. Redaction in `sample` and `neighbors`, including noise checks. `[uid]` probes refused. Exposure events recorded. Holdout absent from evaluation, `compare`, ablation, `known_records_missed`, `review_fingerprint`, the critic packet, `status` and progress. `set split` refused. Protection holds both before the choice and throughout development. |
| `test_holdout_test.py` | Preconditions (complete evaluation, current critic). Binding. One receipt per binding. Strategy edits after a receipt refused. A new receipt after translation drift. `incomplete` blocks the report with no partial counts; `empty` delivers. The report does not re-score and does not start a revision cycle on misses. The query is delivered unchanged when records were missed. |
| `test_interpret.py` | Fixed text for 3/3 (85.7%), 14/14, 4/6, 0/6, no holdout (each reason), N = 0, incomplete, empty, and compromised exposure. The illustration omitted for grouped or unverified units. Rounding at x = 2, 3, 6, 134 and 135. The audit section, `holdout-test` message and `deliver` message are byte-identical. `reporting.md` matches the renderer. |
| `test_repair_epoch.py` | Release moves units and keeps the receipt. The critic budget resets per epoch. The repaired-delivery wording. No x/x claim for the revised query. |
| `test_legacy.py` | Legacy roles mapped on read and files not rewritten. Policy-1 deliveries verify as legacy. Legacy `validation` reported as a comparison list, never as a held-out test. |
| Updated | `tests/golden/progress_sequence.md` (Step 5 name, Step 3 allocation), `test_progress.py`, `test_workspace.py`, `test_guardrails.py`. |

### Commands

```bash
uv run --with pytest pytest -q
```

```bash
uv run python ~/.claude/plugins/marketplaces/claude-plugins-official/plugins/skill-creator/skills/skill-creator/scripts/quick_validate.py .
```

### Walkthroughs

- **Scripted, with the fake PubMed in `tests/conftest.py`:**
  - no records
  - quick depth with seeds
  - standard depth with no separate context (U = 0)
  - standard depth with a separate context: preview, keep holdout, 3/3, deliver
  - the same with 4/6, then release, repair and the repaired delivery
- **Live, through the harness:** two or three **dev** topics only, with the Claude driver (which
  has subagents) and the Codex driver (U = 0 is expected). Check that the receipt, the audit and
  the final message agree.

## 8. Implementation order

Each phase is one commit, and the suite passes after each.

1. **Terminology and data model.** Purposes, origins, screening fields, the exposure log, the
   private store, the legacy mapping on read, policy 2 and the policy-1 verification path.
2. **Guard.** `reserved.py`, development-only evidence everywhere, and `set split` withdrawn.
3. **Allocation.** `psb allocate`, the preview and choice messages, the freeze, stale
   detection, and quick-depth handling.
4. **Held-out test.** `psb holdout-test`, `interpret.py`, and report and progress integration.
5. **Repair.** `holdout-release` and critic epochs.
6. **Documentation.** `SKILL.md`, the references, `README.md`, and the parity test.
7. **Harness and walkthroughs.**

Done when all of these hold:

- the suite and the skill validator pass;
- the scripted walkthroughs produce the §4 texts exactly;
- one live dev-topic run ends with a receipt, an audit and a final message that agree.

## Appendix: changes from the draft plan

- **Installed copies.** These are symlinks to the repository, so the work happens in a worktree
  rather than avoiding a separate copy.
- **Terminology.** The draft's target, "held-out seeds", does not exist in the repo. The terms
  actually replaced are `validation`/`benchmark` and the README role table.
- **Comparison list.** It is now outside the pool by construction, so it no longer contradicts
  the rule that unknown exposure counts as exposed.
- **Origins.** Similar articles are separated from citation searches.
- **Rounding.** Half-up through `Decimal`, and integer `(3N+5)//10`.
- **The draw.** Hash ordering replaces `random.sample` for reproducibility.
- **Message text.** `psb` renders it and `reporting.md` mirrors it, rather than the agent choosing
  wording from a reference.
- **Escape hatch.** Limited to `narrative.md` and extra chat prose.
- **Command and step names.** The command is `psb holdout-test`, and Step 5 is renamed
  "Develop & revise", which removes the double meaning of "test".
- **Repair.** Gets its own critic epoch; without one the existing round limits block delivery.
- **Exposure.** Derived from `psb`'s own logs, with a private screener store. Noise-check
  samples and `[uid]` probes are redacted or refused.
- **Units.** Results are reported per record and per study.
- **Late companions.** A later report of a reserved study records exposure rather than joining
  the group quietly.
- **New messages.** Added: N = 0, comparison lists and repaired delivery.
- **Incomplete test.** Blocks the report; an empty denominator delivers with its fixed wording.
- **Legacy.** Policy 2, with policy-1 receipts verified as legacy deliveries.
