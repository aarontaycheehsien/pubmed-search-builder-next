# PubMed search builder (next)

An agent skill (Claude Code, Codex) that builds high-sensitivity PubMed search strategies for
evidence syntheses, tests them against known relevant records, runs a PRESS-structured critique,
and writes a PRISMA-S style audit.

This is a fresh rebuild of
[pubmed-search-builder](https://github.com/aarontaycheehsien/pubmed-search-builder)
(`protocol-first-empirical-search-builder` branch). It retains the methodology of the earlier
project but replaces much of its excessively heavy bookkeeping machinery with a simpler, leaner
implementation. The aim is to preserve the parts that improve search quality while making the
code easier to understand, maintain, and modify.

This version has also been tested much more systematically with Luna-6 at high effort. A typical
run takes around 10–15 minutes. Any major code change is first tested on a development set of 10
questions, each with a gold-standard set of relevant records. Each question is run three times so
that improvements are not judged from a single favourable run. Once a change performs
satisfactorily on the development set, it is tested separately on a held-out set of 10 additional
questions that was not used to guide the change. The held-out set checks that the improvement
generalises beyond the questions used during development, rather than simply fitting the
development set.

## What it does

PubMed Search Builder is an agent skill for **Claude Code and Codex** that develops high-sensitivity PubMed search strategies for systematic reviews, scoping reviews, rapid reviews, and other evidence syntheses.

Instead of asking an LLM to produce a plausible-looking Boolean query in one shot, it treats search development as an **iterative, testable process**. The user provides the review question and can optionally supply seed papers. The agent then proposes which concepts should be searched and which are better handled during screening; the user approves or revises that decision **(human in the loop)**. The agent builds the MeSH and free-text vocabulary, then **pilots and tests candidate strategies directly in PubMed via its API**. It evaluates retrieval against the supplied or known relevant records, diagnoses misses, revises the strategy, runs a PRESS-structured internal critique, and produces an auditable final search for human review.

> **This is not just an LLM Boolean-query generator. It is an agentic search-development workflow.**

![PubMed Search Builder workflow](docs/pubmed-search-builder-workflow.svg)

## Why use it?

LLMs can write convincing search strings that still have serious retrieval problems. They may AND too many concepts, search outcomes or comparators unnecessarily, misuse controlled vocabulary, generate syntax that PubMed interprets differently from what was intended, or simply stop after producing the first plausible query.

PubMed Search Builder adds a search-development loop around the model:

- **Scope before vocabulary.** It decides which concepts need to be searched before using seed records, reducing overfitting and the common mistake of turning every PICO element into an AND block.
- **MeSH plus free text.** Each searched concept is represented explicitly with controlled vocabulary and title/abstract terms rather than relying on PubMed Automatic Term Mapping.
- **Empirical testing.** The strategy is actually run in PubMed. Counts, translations, known-record retrieval, failing blocks, and leave-one-block-out results are inspected.
- **Diagnose misses rather than explain them away.** When a known relevant record is missed, the workflow identifies which concept block failed and examines the record's vocabulary.
- **Revision is recorded.** Search versions, changes, lost records, counts, and rationales are retained rather than disappearing into a chat transcript.
- **Protected delivery.** The final query and audit are generated only after validation and critique requirements pass.

The guiding principle is simple: **the LLM can reason about the search, but claims about PubMed should come from PubMed.**

The workflow is recall-first. It does not try to produce the smallest possible result set if doing so risks missing relevant studies.

## Workflow

| Step | What happens |
|---|---|
| **1. Question / intake** | Start with the plain-language review question, optional known articles, search depth, and required limits. |
| **2. Scope** | Decide which concepts should be searched, handled at screening, or tested as optional blocks. |
| **3. Known records** | Collect seed or benchmark PMIDs when available so the strategy can be tested against known relevant studies. |
| **4. Vocabulary** | Build each searched concept using MeSH plus free-text title/abstract terminology. |
| **5. Test & revise** | Run the search, inspect PubMed translations and counts, measure relative recall, diagnose misses, and revise one change at a time. |
| **6. Critique** | Run a fresh-context PRESS-structured internal critique and resolve, reject, or explicitly document each finding. |
| **7. Deliver** | Revalidate the strategy and generate the final query, audit, and validation manifest for handoff. |

The core loop is:

**construct → execute → measure → diagnose → revise → critique → validate**

## What you get

A successful run produces:

- a copyable final PubMed search strategy;
- the strategy line by line with counts;
- relative recall against each known-record set, when such records are available;
- missed-record and failing-block diagnostics;
- the development and change history;
- scope and search-design decisions;
- an internal PRESS-structured critique and dispositions;
- a PRISMA-S-style audit for the PubMed search; and
- a validation manifest tying the delivered query to the evaluated workspace.

The output is a **draft ready for human PRESS peer review by an information specialist**, not a claim that the strategy has perfect recall or has itself undergone formal PRESS peer review.

## When to use it

Typical uses include:

- building a new PubMed strategy from a review question;
- building a strategy when you already have several known relevant articles to test against;
- reviewing an existing PubMed strategy for likely recall, structure, vocabulary, or syntax problems; and
- updating a previously completed PubMed search while documenting what changed.

It is designed for **search development**, not for answering the review question or summarising the retrieved literature. It covers PubMed/MEDLINE only; searches of other databases, registries, citation indexes, and grey-literature sources remain separate parts of an evidence-synthesis search.

## Design

- **One tool, one workspace.** `scripts/psb.py` does all PubMed and MeSH work. A run workspace
  holds `protocol.json` (scope), `strategy.json` (blocks), `sets/` (known PMIDs with roles),
  `history/` (strategy versions), `attempts/` (every evaluation), and `log.jsonl`.
- **Provenance as a side effect.** Every NCBI request is logged automatically. `psb report`
  builds the audit from workspace files, so reported numbers come from the tool, not from prose.
- **One key per concept.** A block `id` in the strategy is the concept `id` in the protocol and
  in every report.
- **Protected delivery.** `psb report` validates live and blocks technical defects and unfinished
  review. `psb status` verifies the current delivery manifest. Counts and recall are recomputed.
- **Standard library only.** Python 3.10+, no dependencies, no hooks.

## Quick start

```bash
cp .env.example .env            # add NCBI_EMAIL and optionally NCBI_API_KEY
python scripts/psb.py doctor
python scripts/psb.py init runs/demo --question "Accuracy of DMSA scan or ultrasound for vesicoureteral reflux in children with UTI"
python scripts/psb.py --workspace runs/demo mesh lookup vesicoureteral reflux
# edit runs/demo/protocol.json and runs/demo/strategy.json
python scripts/psb.py --workspace runs/demo set add seeds 12345678 23456789 --role seed
python scripts/psb.py --workspace runs/demo eval --note "first draft"
python scripts/psb.py --workspace runs/demo critic packet
# Save the reviewer's response as critic/round-1.json, then run critic check.
python scripts/psb.py --workspace runs/demo report
```

## Commands

| Command | Purpose |
|---|---|
| `init`, `status` | create a workspace; list what is done and what is missing |
| `count`, `sample`, `fetch` | count a query with PubMed's translation; look at records |
| `neighbors`, `resolve` | similar/citing/cited records; DOIs and PMCIDs to PMIDs |
| `mesh lookup`, `mesh show` | MeSH descriptors, entry terms, narrower headings, counts |
| `set add/remove/split/list` | known-record sets with roles (seed, relevant, validation, benchmark) |
| `lint` | offline syntax and design checks, numbered line set |
| `eval` | counts per line, recall per set, failing blocks, ablation, change since last version |
| `terms rank`, `terms miss` | objective term candidates; vocabulary of missed records |
| `critic packet`, `critic check`, `critic override` | PRESS critic input; validate a critic round; deliver over an open judgment finding after the closing round |
| `report` | live validation and protected query/audit/manifest; `--diagnostic` emits unfinished output |
| `log`, `cache`, `doctor` | provenance summary, cache, configuration check |

## Tests

```bash
uv run --with pytest python -m pytest
```

Tests run offline against a fake PubMed that evaluates Boolean queries over a small corpus.

## Status

- Done: core library and CLI, offline tests, `SKILL.md` and references, and the evaluation harness
  (`evals/`, see its README) with 20 fixtures, naive and reference baselines, and Claude/Codex drivers.
- First end-to-end runs (one run each, Claude, no seeds) are in `evals/RESULTS.md`. Both topics
  reached 100% recall; on CD011926 the lean `creating-high-sensitivity-pubmed-searches-optimal`
  skill did too, at similar workload and lower cost. Single runs on two topics prove the pipeline,
  not a difference between skills.
- Next: repeated runs across the suite (both skills, noseed and seeded) to find where they differ,
  then add components only where they help.

## Licence

MIT

Delivery policy and phrase-warning handling: [references/validation.md](references/validation.md).
Opt-in live smoke check: set `PSB_LIVE_TESTS=1` and run `python -m pytest tests/test_guardrails.py -q`.
