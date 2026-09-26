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
  `history/` (every evaluated version) and `log.jsonl`.
- **Provenance as a side effect.** Every NCBI request is logged automatically. `psb report`
  builds the audit from workspace files, so reported numbers come from the tool, not from prose.
- **One key per concept.** A block `id` in the strategy is the concept `id` in the protocol and
  in every report.
- **Soft checklists, hard facts.** `psb status` lists what is missing but never blocks; counts
  and recall are recomputed each time.
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
python scripts/psb.py --workspace runs/demo report --fresh
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
| `critic packet`, `critic check` | PRESS critic input; validate a critic round |
| `report` | render `audit.md` (`--fresh` re-runs counts live) |
| `log`, `cache`, `doctor` | provenance summary, cache, configuration check |

## Tests

```bash
uv run --with pytest python -m pytest
```

Tests run offline against a fake PubMed that evaluates Boolean queries over a small corpus.

## Status

- Done: core library and CLI, offline tests, `SKILL.md` and references.
- Next: an evaluation harness that runs the skill end to end on gold-standard reviews (CLEF TAR,
  SYNERGY) with sealed gold sets and `as_of` dating, against naive, lean-skill and original-review
  baselines. New components are added only when they improve recall or workload there.

## Licence

MIT
