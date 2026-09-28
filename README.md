# PubMed search builder (next)

An agent skill (Claude Code, Codex) that builds high-sensitivity PubMed search strategies for
evidence syntheses, tests them against known relevant records, runs a PRESS-structured critique,
and writes a PRISMA-S style audit.

This is a fresh rebuild of
[pubmed-search-builder](https://github.com/aarontaycheehsien/pubmed-search-builder)
(`protocol-first-empirical-search-builder` branch). It keeps that project's methodology and
drops its bookkeeping machinery.

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
| `optional sample`, `optional decide` | loss sample of the records an optional block removes; record whether to AND it |
| `critic packet`, `critic check` | PRESS critic input; validate a critic round |
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
