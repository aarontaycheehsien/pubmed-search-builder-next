# PubMed Search Builder (next)

**Develop, test and document high-sensitivity PubMed search strategies with an AI coding agent.**

> **Preview branch:** The skill is named `pubmed-search-builder-holdout-verbose` in `SKILL.md`. This branch introduces private candidate screening, development/held-out allocation, one final held-out retrieval test when feasible, and optional verbose progress messages.

PubMed Search Builder is an agent skill for **Codex and Claude Code**. Give it a systematic, scoping or rapid review question and, optionally, papers already known to be relevant. It develops a PubMed strategy, **executes candidate queries against PubMed**, checks their interpretation and results, examines which relevant records were missed, and revises the search. It then conducts a PRESS-structured *internal* critique and delivers a validated query with an audit trail.

**Why not just ask an LLM for a Boolean string?** A convincing-looking search can contain non-existent MeSH headings, over-restrictive AND blocks, unsuitable field tags or PubMed translations that differ from the intended search. This workflow tests the search against PubMed and records what happened; it does **not** establish that every relevant paper was found.

![PubMed Search Builder workflow: screening, allocation, development, and optional repair](docs/pubmed-search-builder-workflow-repair.webp)

The diagram separates **Step 3a (discover and screen known records)** from **Step 3b (allocate eligible records)**. These are two parts of the existing seven-stage workflow, not an additional numbered stage. **If the held-out test misses records**, the agent first delivers the original tested query unchanged, then offers an optional **Repair**: release the held-out records into development, revise and re-review the search, and deliver the revised query clearly labelled as *not independently tested* against those records. A [simpler editable SVG workflow](docs/pubmed-search-builder-workflow.svg) is also available.

## Quick start

You need **Python 3.10+**, internet access to NCBI E-utilities, and **Codex or Claude Code**. No additional Python packages are required for the core search tool.

1. Clone or download **this branch** and open the repository in your coding agent.
2. Copy `.env.example` to `.env`, then set `NCBI_EMAIL=your.email@example.com`. An `NCBI_API_KEY` is optional. Do not commit `.env`.
3. Ask the agent to read and follow `SKILL.md`, and supply your review question.

For example, send this to your agent:

> Read `SKILL.md` in this repository and build a high-sensitivity PubMed search for a systematic review of school-based food and nutrition education interventions and adolescent food consumption.

The agent runs the commands; **you do not need to operate the CLI yourself**. During intake, it asks for any **known relevant papers** (PMIDs, DOIs or PMCIDs; optional), your preferred **depth** (quick, standard or thorough), any required **date or language limits**, and whether you want **standard or verbose progress messages**. You do not need to specify these in the opening prompt. The agent also asks you to approve or revise the proposed search scope before building the strategy. You can provide inclusion/exclusion criteria at intake. The workflow supports reviewing or updating an existing strategy too.

To check local configuration:

```bash
cp .env.example .env
# Edit .env to set NCBI_EMAIL.
python scripts/psb.py doctor
```

**Important:** A clone of this branch does not automatically install the skill globally in your coding agent. The straightforward route is to open the repository and explicitly ask the agent to follow its `SKILL.md`. The skill is designed for a coding agent with terminal and network access, not the ordinary ChatGPT or Claude web chat.

## Example: from a review question to a tested strategy

Consider: **“Do school-based food and nutrition education interventions change food consumption among adolescents?”**

The workflow does not immediately concatenate every element of this question with AND. It first proposes concept roles for your approval. For example, an agent might propose a **school-based intervention** concept and a **food/nutrition education** concept for searching, while leaving **food consumption outcomes** for screening if they are inconsistently mentioned in abstracts. This is *illustrative*, not a tested strategy or a recommendation to omit the adolescent population: the actual scope decision depends on the eligibility criteria and must be confirmed.

After scope approval, it identifies MeSH and title/abstract terms, runs the candidate search in PubMed and checks known relevant records when available. If a relevant paper is missed, it can identify which required concept block prevented its retrieval, inspect the terminology used in that paper, revise the search and test again. It then completes the internal critique and runs live validation before delivery.

**What a complete run can show:**

- The scope table, including concepts deliberately left to screening rather than AND-ed into the query.
- An executable PubMed query and its line-by-line result counts.
- Which *development* records the query retrieved or missed, and which blocks contributed to misses.
- The successive revisions, decisions and unresolved limitations.
- A held-out retrieval result **only if** eligible unexposed records were reserved and a separate test was completed.
- A PRESS-structured internal critique and a PRISMA-S-style PubMed audit.

**This example is a walkthrough of the implemented workflow, not an empirical case report.** No query, record count or improvement is claimed for this review question here. A real end-to-end worked case with archived outputs should be added separately rather than inventing before/after performance numbers.

## How the seven-step workflow works

The workflow has **seven numbered stages**. Step 3 has two parts, **3a (discover and screen)** and **3b (allocate)**, which are shown separately in the workflow diagram.

| Step | What the agent does | What you do | Detailed instructions |
|---|---|---|---|
| **1. Intake** | Records the review question and asks for anything not already supplied: eligibility criteria, optional known relevant articles (PMIDs, DOIs or PMCIDs), search depth (**quick**, **standard** or **thorough**), genuine date/language limits and **standard or verbose** progress messages. Starts a workspace and records assumptions; standard depth and progress are the defaults. | Start with **just your review question** if you prefer; answer the follow-up questions as needed. You do not have to mention known papers or progress settings in the initial prompt. | [Intake procedure](SKILL.md#1-intake) · [Progress options](references/verbose.md) |
| **2. Scope** | Analyses the question, proposes the review framework and eligibility criteria, and classifies concepts as **searched** (AND-ed blocks), **screened** (assessed after retrieval) or **optional**. Explains why an outcome, comparator, setting or other fragile concept may be safer at screening rather than in the PubMed query. | **Approve the proposed scope** (reply `keep`) or request changes. This happens before the agent examines known records for search development, so they do not determine the review's scope. | [Scope and concept roles](references/scope.md) · [Scope procedure](SKILL.md#2-scope) |
| **3a. Known records: discover and screen** | Finds candidate studies from supplied identifiers, prior reviews and their included-study tables (when accessible), focused pilot searches, PubMed similar articles and citation links. Screens candidates against the agreed eligibility criteria, records their origins and groups reports of the same study. When available, a **separate agent context** keeps discovery and screening information out of the search-building context. | Optionally supply relevant papers or clarify uncertain eligibility. You do **not** need to find seed papers before starting. | [Discovery and screening](references/known-records.md#discovery-by-depth) · [Separate screening context](references/known-records.md#the-separate-screening-context) |
| **3b. Known records: allocate** | **Before term mining**, allocates eligible records to a **development set** (visible for vocabulary discovery and repeated checks) and, when feasible, an **unseen held-out set** for one final retrieval test. A holdout is proposed only with at least 10 eligible allocation units and some unexposed units; otherwise the records are used for development. Study reports are kept together when their grouping is recognised. | **Choose** whether to keep the proposed holdout or use all eligible records for development. If no holdout is possible, there is no allocation choice to make. | [Allocation rules and choices](references/known-records.md#allocation) · [Why exposure matters](references/known-records.md#exposure) |
| **4. Vocabulary** | For every searched concept, checks the actual **MeSH** vocabulary (including entry terms and narrower headings), constructs a corresponding **title/abstract** free-text layer, and considers synonyms, spelling variants, acronyms, truncation and proximity. May mine useful terms from **development records only**, never the reserved held-out set. | Usually no action is needed; inspect suggested terms if you want to check how the concepts are represented. | [MeSH and free-text methods](references/vocabulary.md) · [Vocabulary procedure](SKILL.md#4-vocabulary) |
| **5. Develop and revise** | Executes candidate queries directly in **PubMed**, checks translations and line-by-line result counts, measures retrieval of **development records**, and uses failed concept blocks, term analysis and leave-one-block-out checks to diagnose misses. Revises and retests, documenting changes and the effect on recall proxies and result-set size. Reviews phrase-index warnings instead of ignoring them. | Normally let the agent iterate. You can examine the interim search choices or clarify a substantive question; retrieval of development records is **not independent validation**. | [Testing and revision procedure](SKILL.md#5-develop-and-revise) · [Phrase and syntax checks](references/validation.md) · [Search anti-patterns](references/anti-patterns.md) |
| **6. Critique** | Sends a structured evidence packet to a **fresh-context PRESS-structured internal critic** when possible. Reviews syntax, concept coverage, vocabulary and other search-design risks; addresses each finding with a change, reasoned disposition or documented accepted risk, and performs further checks as required. Technical blockers cannot simply be waived. | Usually no action is needed, though the agent may ask about unresolved scope decisions or explain why it cannot finish. **This is not formal PRESS peer review.** | [Critique process and domains](references/critic.md) · [Critique procedure](SKILL.md#6-critic) |
| **7. Validate and deliver** | When a holdout was reserved, runs **one retrieval test of the frozen query** after critique. Revalidates PubMed syntax, headings, translations and counts; then generates `final-query.txt`, `audit.md` and `validation-manifest.json`. **Even if the holdout reveals misses, it delivers the tested query unchanged first**, with the result and limitations clearly stated. | Review the draft and arrange **human PRESS peer review** where appropriate. If held-out records were missed, you may choose **Repair**: release them for development, revise and re-review the search. The revised query is labelled **not independently tested** against those records. | [Delivery and Repair](references/reporting.md#order-at-delivery) · [After a repair](references/reporting.md#after-a-repair) · [Final validation](references/validation.md) |

**The essential loop:** construct → execute → measure → diagnose → revise. A final draft is delivered only if the required checks pass. If the held-out test reveals a miss, the tested query is reported **unchanged** first; a subsequent repair is explicitly labelled as no longer independently tested against those records.

![Human decisions and agent actions, including allocation and the option to repair a missed held-out record](docs/pubmed-search-builder-human-agent-workflow.svg)

The allocation decision is offered **only when an eligible holdout is possible**. After final delivery, **Repair** is offered only if the held-out test missed records. A repair uses the released records for further development, so it cannot count as a fresh independent test on those same records.

## What progress looks like

The tool generates consistent messages for each of the seven stages. For instance, the stage headings include `PSB · Step 2/7 Scope`, `PSB · Step 3/7 Known records`, and `PSB · Step 5/7 Develop & revise`. The messages identify what has happened and what comes next.

![Rendered screenshot of the PubMed Search Builder progress transcript showing the scope summary and known-record discovery](docs/progress-sequence-screenshot.webp)

*Example progress messages from [`tests/golden/progress_sequence.md`](tests/golden/progress_sequence.md), shown in a locally rendered GitHub-style excerpt. This is a **synthetic test fixture**, not a screenshot of a live PubMed search or a direct capture of GitHub's website. The displayed counts are illustrative.*

Choose **standard** messages for short updates or **verbose** messages for up to three additional detail lines on discovery, MeSH lookups, term mining and evaluation. Verbose mode changes what is *shown*, **not** what is searched or screened. Private screening messages never disclose their hidden records or queries, even in verbose mode. See [the progress-message specification](references/verbose.md) and [the complete example progress sequence](tests/golden/progress_sequence.md).

## Choose a search depth

| Depth | Candidate-screening budget | Internal critique | Held-out test |
|---|---:|---|---|
| **Quick** | Up to about 30 | 1 revision round, then closing | No automatic holdout |
| **Standard (default)** | Up to about 150 | 2 revision rounds, then closing | Proposed if eligible, unexposed records exist and allocation conditions are met |
| **Thorough** | Up to about 400 | 3 revision rounds, then closing | Same conditional allocation as standard |

These are **upper screening budgets**, not promises of how many eligible studies will be found or guarantees of greater recall. Further verification/closing rounds can be required by the critique rules. See [SKILL.md](SKILL.md).

## Development records versus held-out records

A search that retrieves papers already used to build it has passed a **development check**, not an independent test. This branch can use a separate agent context to discover and screen records without revealing their titles, abstracts, search queries or screening decisions to the search-building agent. Eligible records are then allocated:

- **Development records** can be inspected for terminology, used to diagnose missed records, and checked repeatedly during revisions.
- **Held-out records** remain unavailable to the builder and are checked **once** against the frozen final query, when a holdout is feasible and chosen.
- **Comparison lists** are reported separately; they are not treated as independent held-out tests.

An automatic holdout is proposed only when at least **10 eligible allocation units** exist and at least one is unexposed. It reserves approximately 30% of eligible units, capped by the unexposed units available, while keeping reports of the same study together where recognised. You can instead choose all-development allocation. A private, unexposed context is a **procedural safeguard**, not an access-control security boundary; without such a context, all records are development records.

**A held-out result is not a reliable estimate of overall recall by itself.** The pool may overrepresent papers similar to the queries, prior reviews or seed studies used to assemble it. Finding 6 of 6 held-out records establishes retrieval of those six records, not that the strategy retrieves nearly all eligible literature. The number of independent studies, study grouping and discovery sources matter as well. See [known-record methods](references/known-records.md) and [fixed interpretation rules](references/reporting.md).

## What you receive

When the delivery gate passes, the workspace contains:

| Output | What it contains |
|---|---|
| `final-query.txt` | The copyable, revalidated PubMed strategy |
| `audit.md` | Scope, search lines and counts, record-based checks, development history, critic findings, limitations and PubMed reporting details |
| `validation-manifest.json` | Evidence that the delivered artefacts correspond to the evaluated and validated query |

The final query is a **draft for human PRESS peer review by an information specialist**, not a formally peer-reviewed strategy. The audit follows relevant [PRISMA-S](https://doi.org/10.1186/s13643-020-01542-z) reporting principles for **PubMed only**; it is not a complete multi-database PRISMA-S report. See [reporting details](references/reporting.md).

## Evaluation: what is and is not established

The repository contains an [end-to-end evaluation harness](evals/README.md), [historical results](evals/RESULTS.md), development topics and separately frozen held-out **topics**. These topic-level held-out evaluations assess changes to the skill; they are **different** from the record-level held-out test within one user's search build.

**Version caveat:** `evals/RESULTS.md` was generated on **30 September 2026** and contains results from earlier staged skill versions. It must not be read as an end-to-end performance evaluation of the exact current `pubmed-clearerui` branch, which has introduced substantial subsequent changes. The repository also includes targeted automated tests of allocation, private disclosure, held-out receipts, progress messages and delivery checks; those tests establish intended software behaviour under test conditions, **not improved real-world retrieval recall**.

The historical evaluation covers recall against known published-review reference sets, unseen recall, search size and workload proxies. Comparisons must consider variation across repeated agent runs, uneven run completion and how much larger a result set becomes in exchange for higher recall. See the [evaluation methods](evals/README.md) before citing results.

## Limitations

- **No guarantee of complete recall.** Evaluation is against available reference records, not an exhaustive census of every eligible study.
- **Discovery bias remains possible.** A held-out set can be unseen yet unrepresentative of the literature.
- **Eligibility screening is fallible.** Agent screening and study-group identifiers need appropriate human checking; different identifiers for the same study are not automatically reconciled.
- **Full-text extraction is not built into `psb`.** When included-study tables or supplementary files from earlier reviews are required, an agent needs other permitted tools or user-supplied documents.
- **Recall-first searches can be large.** Additional retrieved records impose real screening workload.
- **Internal critique is not independent human PRESS peer review.**
- **Only PubMed/MEDLINE is covered.** Other databases, registers, citation searches and grey-literature searches need separate planning.

## For developers and auditors

Most users can stop here. The technical material is in:

- [`SKILL.md`](SKILL.md) — instructions followed by Codex or Claude Code.
- [Known-record discovery and allocation](references/known-records.md) — origins, exposure, screening, allocation and repair.
- [Scope and concept decisions](references/scope.md) — searched versus screened concepts.
- [Validation and phrase-warning handling](references/validation.md) — PubMed syntax and delivery blockers.
- [Reporting and protected outputs](references/reporting.md) — interpretation language and audit structure.
- [Progress messages](references/verbose.md) — verbose mode behaviour.
- [Evaluation harness](evals/README.md) and [results](evals/RESULTS.md).
- [Allocation implementation plan](ALLOCATION_PLAN.md) — historical design rationale, not the primary user instructions.

**CLI commands:** `python scripts/psb.py --workspace <run-dir> <command> ...`. Start with `python scripts/psb.py doctor` and `SKILL.md`; do not manually bypass the agent's required allocation, critique and reporting checks.

**Automated tests:**

```bash
uv run --with pytest python -m pytest
# Optional live NCBI smoke test:
PSB_LIVE_TESTS=1 python -m pytest tests/test_guardrails.py -q
```

## Licence

MIT
