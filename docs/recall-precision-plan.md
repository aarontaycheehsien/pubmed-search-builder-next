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
3. **`evals/replay.py`** runs the diagnostics on a strategy an agent really delivered, with the
   answer key as the known records. Development topics only. No agent and no model.
4. **Known records no keyword search led to.** `psb eval` reports
   `known_without_keyword_search`: user seeds and review reference lists, how many are
   retrieved, and a 95% lower bound on recall from those also held out of the build. With none,
   it says the recall figures check the wording and do not estimate recall. To make such
   records easier to get, the prior-review sample marks reviews in PMC, `psb neighbors` names
   records that have no reference list, and `known-records.md` says to try further reviews.
5. **`psb eval --term-impact`** removes each term in turn and reports the records, and the
   known records, that only it retrieves, with a query file to sample what it alone finds.
6. **Mining gaps.** `terms rank` proposes substance names (`[nm]`) and folds singular and
   plural into one truncated candidate; `vocabulary.md` covers previous indexing, `[pa]`, and
   narrower headings as the family list for a word that only ends compounds.
7. **Study design is asked at intake**, so a validated filter can be tested as a limit.

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

**Term impact** (Welling_2021, the one-block card of 155,668 records, 39 terms): `pandemic*[tiab]`
alone adds 20,299 records (13.0%), `confinement[tiab]` 19,677 (12.6%) and
`"social isolation"[tiab]` 7,377 (4.7%). None is the only route to a gold record.

On van_de_Schoot the trajectory-label block retrieves 37 of 38 gold records on its own, more
than the delivered PTSD block (35 of 38), and all three current misses. With the first block
broadened to match (distress, acute stress, traumatic stress and two MeSH headings), the
two-block search returns 1,653 records at 97.4%, against 32,074 at 92.1% delivered.

## Agent runs on a cheaper model (development topics)

Claude Sonnet, no seeds, standard depth, scored with `harness.score` against the answer key.
`main` is 704317b.

### The whole branch against main, three runs a side

Each cell is records and recall. The branch arm is commit bf6943b (everything up to the
term-impact prompt).

| Topic | main | branch |
|---|---|---|
| van_de_Schoot_2018 | 35,263 · 35,405 · 67,383, all 94.7% | 10,004 · 9,255 · 9,964, all 94.7% |
| Bos_2018 | 9,885 · 12,691 · 52,766, all 100% | 9,229 · 7,454 · 7,702, all 100% |
| Welling_2021 | 152,755 · 130,810 · 139,917, all 100% | 23,866 · 31,440 · 26,130, all 98.1% |
| Kwok_2020 | 1,572 (94.8%) · 6,816 (96.6%) · 6,272 (96.6%) | 6,332 (96.6%) · 1,562 (97.4%) · 1,288 (94.8%) |

| Across the twelve runs of each arm | main | branch |
|---|---:|---:|
| Mean recall | 97.7% | 97.3% |
| Gold records missed, of 648 | 20 | 22 |
| Mean of the per-topic median record counts | 48,571 | 11,340 |
| Runs with known records no keyword search led to | 2 | 11 |
| Runs that measured an optional block with `psb eval` | not available | 11 |
| Runs that ran `--term-impact` | not available | 10 |

What this shows, and what it does not:

- **About a quarter of the records at about the same recall.** On van_de_Schoot, Bos and
  Welling every branch run returned fewer records than every `main` run. The branch is also
  far steadier: van_de_Schoot spans 9,255 to 10,004 on the branch and 35,263 to 67,383 on
  `main`; Bos 7,454 to 9,229 against 9,885 to 52,766. On `main` the size of the result depends
  on whether the agent happens to AND a second block on judgement.
- **Welling costs one gold record, the same one each time.** All three branch runs AND-ed an
  outcome block and missed 32242089, "Endocrine and metabolic link to coronavirus infection",
  whose record carries no lifestyle or well-being wording for any outcome block to match. That
  is 1 of 53 for a result one fifth the size. Each run reported the risk it had measured:
  bounds of 19.3%, 10.9% and 6.3% on 14, 26 and 46 independent records.
- **Kwok shows no effect, and one caution.** Both arms vary fourfold between runs and their
  recall overlaps. The third branch run wrote a narrower method block than the other two and
  missed two gold records they kept. It also dropped `pyrosequencing`, `"novel virus*"` and
  `"viral diversity"` after `--term-impact` showed no known record depending on them and its
  samples looked off-topic. Restoring the three (checked against the answer key) recovers one
  gold record, 25918239, for 383 more records. A term-impact cut is only as safe as the known
  set is wide.
- **The mechanisms were used.** Eleven of twelve branch runs built a benchmark from a review's
  reference list (two of twelve on `main`) and measured an optional block; three reached the
  20 independent records the rule asked for, eight AND-ed for workload with 8 to 14. Ten ran
  `--term-impact` and cut what its samples showed: bare `posttraumatic[tiab]` (orthopaedic and
  surgical records), `leukoencephalopath*` (18.5% of one result), `epidemic*` and `outbreak*`
  (48% of one COVID result), `confinement`.
- **The two records every run missed on van_de_Schoot** (20061839, 20836603) call the
  condition "distress" or "acute stress". No run had them among its known records, so no
  diagnostic could point at them. Known-record discovery still bounds recall.
- **This is not the harness, and not the usual model.** The agents were subagents sharing one
  machine, with the as-of date pinned in the staged launcher and a same-context critic. Three
  runs a side on four development topics supports the direction and rough size of the effect
  on record counts; it does not support small differences in recall, and it says nothing about
  held-out topics. Two commits made after these runs (the shorter `--brief` output and the
  restated rule in `scope.md`) have not been run by any agent.

### Earlier versions of the branch (one run each)

Claude Sonnet, no seeds, standard depth, scored with `harness.score` against the answer key.
`main` is 704317b. "First version" is commits 1 to 3 of this patch as first written (the loss
bound counted every known record). "Commits 1 to 9" is the branch before the term-impact prompt. Each cell is records and recall.

| Topic | main, run 1 | main, run 2 | first version | commits 1 to 9 |
|---|---:|---:|---:|---:|
| van_de_Schoot_2018 | 35,263 · 94.7% | 35,405 · 94.7% | 10,554 · 94.7% | 32,266 · 94.7% |
| Bos_2018 | 9,885 · 100% | 12,691 · 100% | 7,976 · 100% | 14,369 · 100% |
| Welling_2021 | 152,755 · 100% | 130,810 · 100% | 22,729 · 92.5% | 126,454 · 100% |
| Kwok_2020 | 1,572 · 94.8% | 6,816 · 96.6% | 1,519 · 98.3% | 5,932 · 98.3% |

Known records found without a keyword search, per run (the only ones that can test anything):

| Topic | main, run 1 | main, run 2 | first version | commits 1 to 9 |
|---|---:|---:|---:|---:|
| van_de_Schoot_2018 | 0 of 11 | 9 of 27 | 12 of 31 | 13 of 30 |
| Bos_2018 | 0 of 13 | 0 of 13 | 2 of 17 | 6 of 18 |
| Welling_2021 | 0 of 10 | 0 of 23 | 0 of 95 | 16 of 28 |
| Kwok_2020 | 0 of 19 | 0 of 16 | 0 of 31 | 0 of 28 |

One further pair on Haiku, van_de_Schoot only: `main` 8,404 records at 89.5%, first version
32,440 at 94.7%.

What these earlier runs showed, and why the branch changed after them:

- **The first version bought precision with an unmeasured loss.** It cut records on all four
  topics, and on Welling it lost 4 of 53 gold records after its measurement had reported none
  of 95 known records lost. All 95 came from pilot searches and their similar articles.
- **Commits 1 to 9 were recall-safe, without a demonstrated precision gain.** With
  the bound restricted to records no keyword search led to, the Welling run found a review's
  reference list (16 records), saw that the two outcome blocks would lose 13 and 6 of 28 known
  records, and kept both out: 100% recall, and a result as large as `main`. On Kwok the run had
  no such records, read the virus block's loss as unmeasured, and left it out: recall as high
  as the first version, with four times its records. Recall equals or exceeds `main` on every
  topic; the result is smaller than both `main` runs on two topics, larger on one, between
  them on one.
- **Independent known records became common:** three of four runs of commits 1 to 9 had them,
  against one of eight on `main`. None reached the 20 that `scope.md` asks for before AND-ing
  a block on evidence, so the two runs that did AND one used the "otherwise too large to
  screen" clause and recorded an unmeasured risk.
- **`--term-impact` was never run by an agent**, so its only evidence is the replay above. Two
  runs cut noise by hand instead. After these runs, `psb eval` was changed to return
  `large_result` above 10,000 records until term impact has been measured, with a line in the
  progress message, and `SKILL.md` to require it once before the critic step. No agent run has
  tested that prompt.
- On Kwok the recall gain came from the `vocabulary.md` text on proximity and families; no
  known record was missed during those builds, so `psb terms miss` never ran there.
- One run a side, two for `main`, cannot separate the patch from run-to-run variance: the two
  `main` runs on Kwok differ by a factor of four in records. These runs were not made by
  `evals/run.py`: the agents were subagents sharing one machine, with the as-of date pinned in
  the staged launcher and a same-context critic. The planned third `main` run and further runs
  of that version were stopped by an account usage limit.

## What is still open

1. **Known-record discovery.** The records every arm missed were never in a known set. Review
   reference lists help (eleven of twelve runs), but a review of a neighbouring topic gives a
   benchmark skewed toward that topic, which several runs flagged.
2. **Term-impact cuts on a narrow known set.** One Kwok run cut a term that was the only
   route to a gold record no run had among its known records. A firmer rule (keep a term that
   names a method or member the criteria name, whatever its impact) might have kept it; it has
   not been written or tested.
3. **AND-ing for workload.** Eight of eleven AND decisions rested on 8 to 14 independent
   records. `scope.md` now names this as its own ground with conditions; whether the user
   should be asked at intake how many records they can screen is undecided.
4. **Closing critic round.** Several runs noted that the depth table suggests a closing round
   at standard depth while `psb report` accepts one revision round. That predates this branch.

## How to test, cheapest first

1. `python -m pytest` (offline, seconds).
2. `python evals/replay.py ...` on the development cards (NCBI requests only, about a minute
   each). A diagnostic that says nothing useful here is not worth an agent run.
3. Agent runs on a cheaper model, baseline against patch, development topics, three runs a
   side. `report` groups by source, driver and skill version, not by model, so give
   cheaper-model runs their own `--skill-name`:

   ```bash
   git worktree add ../psb-main main
   for t in van_de_Schoot_2018 Bos_2018 Welling_2021 Kwok_2020 van_Dis_2020; do
     python evals/run.py generate $t --driver claude --model sonnet --skill ../psb-main --skill-name main-sonnet --runs 3
     python evals/run.py generate $t --driver claude --model sonnet --skill . --skill-name patch-sonnet --runs 3
   done
   python evals/run.py report --pair generated:patch-sonnet generated:main-sonnet
   ```

   Sonnet followed the skill to a protected delivery in every run here; Haiku did too, in two
   runs, with more erratic structural choices. With Codex, pass a cheaper `--model` and
   `--effort low`. A cheaper model ranks the two arms; it does not show what the usual model
   would deliver.
4. Only for a change that survives step 3: the usual model on the held-out topics, once, three
   runs a side, as `evals/README.md` requires.

Keep or revert each commit on its own: every change is a separate commit so its effect can be
attributed. To test the first three commits against the rest, check out the commit before
"known records: count the ones no keyword search led to".
