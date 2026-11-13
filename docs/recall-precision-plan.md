# Recall and precision: findings, what this patch changes, and what to fix next

Everything here was motivated by development topics only. The held-out table in
`evals/RESULTS.md` was read in aggregate; no held-out strategy, audit or miss was inspected.

## What the development runs show

Two patterns account for most of the avoidable loss.

**1. A concept's role is decided by judgement, and only one direction is measured.**
Ablation shows what a searched block costs. Nothing showed what an unsearched concept would
save, so "when in doubt, do not AND it" had no counterweight.

| Topic | Delivered | Records | Recall | Note |
|---|---|---:|---:|---|
| van_de_Schoot_2018 | one PTSD block | 31,980 | 92.1% | lean-optimal: same recall at 7,025 |
| Bos_2018 | one small-vessel-disease block | 54,277 to 91,025 | 100% (9 gold) | lean-optimal: 100% at 5,313 |
| Welling_2021 | one COVID block | 151,652 | 98.1% | second run added a block: 13,793 at 90.6% |

On van_de_Schoot the three missed records call the condition "distress" or "acute stress"; all
three name trajectories or growth mixture modelling. The screened concept was the reliably
named one.

**2. A miss was reported without its cause.**
`psb terms miss` listed 15 n-grams the strategy lacks, in alphabetical order, so for a record
with an abstract they were arbitrary trigrams. Looking up the missed records of Kwok_2020,
van_Dis_2020, Brouwer_2019, van_de_Schoot_2018 and Smid_2020 in PubMed gave four causes:

| Cause | Example (PMID) | Fixable by a term? |
|---|---|---|
| Phrase split or reordered | "high-throughput DNA sequencing" against `"high throughput sequencing"[tiab]` (22821184) | yes: proximity |
| Long phrase, part present | "cognitive-behavioral and psychodynamic approaches" against `cognitive behavio* therap*[tiab]` (10838679) | yes: shorter phrase |
| Word inside a longer word | "rotavirus", "polyomavirus" against `virus*[tiab]`, record not MeSH-indexed (29677111, 29700160) | yes: name the words |
| Concept absent from title and abstract | no sequencing method named (25918239, 28495761, 28653486) | no |

The last row matters for precision: "fix every miss" otherwise rewards widening a block for a
record no term can reach.

## In this patch

1. **`psb terms miss` gives a cause for every failing block** (`phrase_gap`, `embedded_stem`,
   `no_abstract`, `no_block_wording`), the form to test, and the record's keywords and title
   wording ahead of its abstract. `SKILL.md`, `vocabulary.md` and `anti-patterns.md` say what to
   do with each cause, including recording a record as out of reach.
2. **`psb eval` measures optional blocks.** `strategy.json` takes an `optional` list of blocks
   that are never part of the query. For each, `optional_blocks` reports the count if it were
   AND-ed, the known records lost (by set and by discovery route), how many known records name
   the concept, and which current misses the block would have matched. An exact 95% upper bound
   on the share lost is computed only on known records that no keyword search led to; without
   any, the loss is reported as unmeasured (see the Welling_2021 run below for why). `scope.md`
   has the decision rule; the critic packet and the audit carry the evidence.
3. **`evals/replay.py`** runs both diagnostics on a strategy an agent really delivered, with the
   answer key as the known records. Development topics only. No agent and no model.

## Replay on development topics (live PubMed, as-of dates from the fixtures)

These show what the tools would have told an agent. They use the answer key, so the fixes in
the last column are hindsight; they bound what the diagnostics can recover, they are not a
result an agent achieved.

**Miss diagnosis**

| Topic (card) | Misses | phrase gap | word inside a word | no wording | Suggested fixes applied |
|---|---:|---:|---:|---:|---|
| Kwok_2020 (lean-fixes, 1,060 records, 94.8%) | 6 | 1 | 2 | 3 | `[tiab:~1]` and two named words: 1,074 records, 97.4% |
| van_Dis_2020 (ours, 16,407 records, 93.4%) | 4 | 1 | 0 | 3 | not run |

For comparison, dropping Kwok's virus block (the only other way to reach the two embedded
records) gives 5,516 records at 96.6%.

**Optional blocks**

| Topic (card) | Delivered | Optional block | If AND-ed | Known lost | 95% bound | Reading |
|---|---:|---|---:|---:|---:|---|
| van_de_Schoot_2018 (ours) | 32,074 | trajectory labels | 415 | 1 of 35 | 12.9% | loses one: broaden |
| van_de_Schoot_2018 (ours) | 32,074 | course over time, broad | 11,679 | 0 of 35 | 8.2% | candidate to AND |
| Bos_2018 (one block) | 91,189 | dementia or cognition | 11,981 | 0 of 9 | 28.3% | too few known records to rely on |
| Welling_2021 (run 1) | 155,668 | lifestyle block of run 2 | 32,005 | 5 of 53 | 18.8% | keep out |

On van_de_Schoot the trajectory-label block retrieves 37 of 38 gold records on its own, more
than the delivered PTSD block (35 of 38), and all three current misses. With the first block
broadened to match (distress, acute stress, traumatic stress and two MeSH headings), the
two-block search returns 1,653 records at 97.4%, against 32,074 at 92.1% delivered.

## Agent runs on a cheaper model (development topics, one run a side)

Unpatched `main` (704317b) against this patch, no seeds, standard depth, scored with
`harness.score` against the answer key. The model was Claude Sonnet unless marked.

| Topic | main: records | main: recall | patch: records | patch: recall | What the patch run did |
|---|---:|---:|---:|---:|---|
| van_de_Schoot_2018 | 35,263 | 94.7% (36/38) | 10,554 | 94.7% (36/38) | measured the trajectory block (0 of 30 lost, 11 of them from a review's reference list), AND-ed it |
| Bos_2018 | 9,885 | 100% (9/9) | 7,976 | 100% (9/9) | measured the outcome block (0 of 17 lost, 7 of them not from a pilot search), AND-ed it |
| Kwok_2020 | 1,572 | 94.8% (110/116) | 1,519 | 98.3% (114/116) | proximity phrases and named virus families, from the new `vocabulary.md` text |
| Welling_2021 | 152,755 | 100% (53/53) | 22,729 | 92.5% (49/53) | measured the outcome block (0 of 95 lost, none independent), AND-ed it |
| van_de_Schoot_2018 (Haiku) | 8,404 | 89.5% (34/38) | 32,440 | 94.7% (36/38) | measured two blocks, each lost known records, kept both out |

What this does and does not show:

- Every patch run used the optional-block measurement without being told to beyond the skill
  text, and decided by it. On `main`, the Sonnet run on van_de_Schoot left the trajectory block
  out, reporting that its known records were too few to check it and that the skill did not say
  how to test an optional block; it used `psb count`.
- On Kwok the gain came from the instructions, not the diagnosis command: no known record was
  missed during the build, so `psb terms miss` never ran. The two records still missed are the
  ones replay labels `no_block_wording`.
- **Welling is a failure of the first version of this patch.** The measurement said none of 95
  known records would be lost, with a 95% bound of 3.1%; the block lost 4 of 53 gold records
  (7.5%). All 95 came from pilot searches and their similar articles, so they named the outcome
  words by construction. The bound now counts only records no keyword search led to, and the
  same evidence reads "loss unmeasured". That makes the report honest; it does not make the
  block safe. A run with no independent known records still has to choose between a result too
  large to screen and an unmeasured loss.
- Haiku on `main` AND-ed the trajectory block on judgement and lost two more gold records than
  any other run on that topic; with the patch it measured, saw a loss, and kept the block out.
- One run a side cannot separate the patch from run-to-run variance, which
  `evals/RESULTS.md` shows is large. These runs were also not made by `evals/run.py`: the
  agents were subagents sharing one machine, with the as-of date pinned in the staged launcher
  and a same-context critic. Treat them as a smoke test and repeat them with the harness
  (below) before believing the size of any difference.

## Plan: what to fix next, in order

0. **Independent known records in no-seed runs (both).** Welling shows the limit is the known
   set, not the measurement. Two of the four Sonnet patch runs found a review reference list;
   two had none, and `psb neighbors --links refs` returned nothing for a relevant review in two
   other runs. Until a run has records no keyword search led to, recall figures and optional
   blocks alike rest on circular evidence. Where: `known-records.md` (search for reviews on
   overlapping topics when none matches; say plainly that pilot-found records do not validate
   anything), and report the independent count beside every recall figure (item 2). Test: the
   share of no-seed development runs that end with ten or more independent records.

Each item states where it goes and how to tell whether it earned its place.

1. **Marginal contribution of each term (precision).** `lines` reports stand-alone counts;
   `vocabulary.md` already says the final result is the thing to manage. Add, behind
   `psb eval --term-impact`, for each term: the final count without it, and the known records
   only it retrieves (two requests per term). A term with a large marginal count and no unique
   known record is the noise candidate to sample. Where: `evaluate._measure`, one entry per
   term line. Test: replay on Welling_2021 and Brouwer_2019 should name the few terms that
   carry most of the result.
2. **Recall by discovery route, with bounds, for every set (recall estimate).** Pilot searches
   find records that use the searched words, so recall on them is circular. `by_route` exists
   for optional blocks; extend it to the recall table and add the exact bound on independent
   records, so "100% of 9" reads as "at least 72%" and "100% of 95 pilot-found records" reads
   as unmeasured. Where: `evaluate._measure`, `deliver._recall_table`,
   `progress._recall`. Test: unit tests; no agent run needed.
3. **Mining gaps (recall on drug topics).** `ncbi.parse_article` drops `ChemicalList` and
   supplementary concept names, so `terms rank` cannot propose `[nm]`; `terms.candidates` counts
   singular and plural separately against `min_df`; `mesh show` returns `year_introduced` and
   `previous_indexing` but `vocabulary.md` never says to add the earlier heading. Also document
   `[pa]` for drug classes. Test: `terms rank` on a drug topic's seeds proposes substance names.
4. **Members of a concept whose name is a word-ending.** The `embedded_stem` cause says what is
   missing; the fix is a family list. `mesh show` already lists narrower headings: say in
   `vocabulary.md` to use their names as text words when the stem embeds. Test: replay on
   Kwok_2020.
5. **Study design at intake (precision).** The intake message asks for dates and languages.
   Add study design, so a review of trials can test a validated filter as a limit; `psb eval`
   already reports what a limit removes. Test: agent runs on the Cohen topics are held out, so
   use a development trial topic (van_Dis_2020).

## How to test, cheapest first

1. `python -m pytest` (offline, seconds).
2. `python evals/replay.py ...` on the development cards (NCBI requests only, under a minute
   each). A diagnostic that says nothing useful here is not worth an agent run.
3. Agent runs on a cheaper model, baseline against patch, development topics, three runs a
   side. `report` groups by source, driver and skill version, not by model, so give
   cheaper-model runs their own `--skill-name`:

   ```bash
   git worktree add ../psb-main main
   for t in van_de_Schoot_2018 Bos_2018 Welling_2021 Kwok_2020 van_Dis_2020; do
     python evals/run.py generate $t --driver claude --model haiku --skill ../psb-main --skill-name main-haiku --runs 3
     python evals/run.py generate $t --driver claude --model haiku --skill . --skill-name patch-haiku --runs 3
   done
   python evals/run.py report --pair generated:patch-haiku generated:main-haiku
   ```

   With Codex, pass a cheaper `--model` and `--effort low`. A cheaper model ranks the two arms;
   it does not show what the usual model would deliver.
4. Only for a change that survives step 3: the usual model on the held-out topics, once, three
   runs a side, as `evals/README.md` requires.

Keep or revert each commit on its own: the two code changes are separate commits so their
effect can be attributed.
