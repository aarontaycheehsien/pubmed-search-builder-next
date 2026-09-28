# Evaluation harness

Measures the skill end to end: an agent gets only what a user would bring, builds a strategy,
and the harness scores it against the included studies of a published review.

```bash
python evals/run.py baselines                     # naive and reference strategies, all topics
python evals/run.py generate CD011926 --driver claude --condition noseed
python evals/run.py generate CD011926 --driver codex --condition seeded --runs 3
python evals/run.py generate Bos_2018 --skill <path to another skill> --skill-name lean
python evals/run.py score CD011926 --strategy-file my_strategy.txt
python evals/run.py report                        # writes evals/RESULTS.md
```

## Fixtures

`fixtures/<suite>/<id>.json`:

| Field | Seen by the agent? | Meaning |
|---|---|---|
| `question` | yes | plain-language review question |
| `eligibility` | yes | inclusion criteria, when the fixture has refined ones |
| `seeds` | seeded condition only | three gold PMIDs, chosen deterministically; excluded from scoring |
| `as_of` | as a date only | the review's search date, or the day after the latest Entrez date among the gold records (a lower bound) |
| `gold_pmids` | never | the review's included studies |
| `naive_blocks`, `reference_strategy` | never | baselines |

## Isolation

- Each generated run happens in a new directory outside the repository (default
  `<temp>/psb-evals/<topic>/<label>/`) that holds only a copy of the skill (`skill/`), the
  prompt, and the agent's work (`work/`). The fixtures and answer keys are never copied.
- `PSB_AS_OF` pins every `psb` PubMed search and neighbour lookup to `as_of`, so the source review
  (published after its own search) and later literature are out of reach whatever the agent does.
  Other skills do not read `PSB_AS_OF`; for them the date is only an instruction in the prompt.
- Claude runs use `--setting-sources project`, no MCP servers, and no web tools. Codex runs use
  a workspace-write sandbox with network access for NCBI.
- The scorecard lists leakage signs: the transcript naming the fixture or answer key, or `psb`
  PubMed searches that ran without the date bound. A run with leakage is kept but marked invalid.

## What is reported

- **Recall** over gold records in PubMed on or before `as_of`. Seeds are excluded in the seeded
  condition.
- **Unseen recall** leaves out gold records the agent itself screened into its sets during the
  build. Those records were used to develop the strategy, so recall on them flatters it.
- **Results** (the count on or before `as_of`) and **NNR** (results per gold record retrieved), a
  workload proxy rather than precision.
- **Cost and time** from the driver.

## Baselines

- `naive`: each concept's terms OR-ed as `[tiab]` phrases, concepts AND-ed. The concept lists
  come from the old project's fixture protocols, some of which were tightened while looking at
  the gold set, so treat this floor as optimistic.
- `reference`: the hand-authored strategies that two fixtures carry.
- Another skill (for example the lean `creating-high-sensitivity-pubmed-searches-optimal`) can be
  run through `generate --skill`, since the prompt only asks the agent to follow `skill/SKILL.md`
  and finish its final delivery. For protected-delivery versions of this skill, the harness
  verifies `work/validation-manifest.json` and consumes `work/final-query.txt`; it does not fall
  back to a handwritten query. Other skills can continue to write `final_strategy.txt`.

## Reading results

Gold sets are small (6-116 records), so one missed record can move recall by several points, and
agent runs vary. Compare sources with several runs per topic and look at per-topic wins and
losses rather than one mean. A component earns its place in the skill only when it improves
recall or workload across topics at an acceptable cost.
