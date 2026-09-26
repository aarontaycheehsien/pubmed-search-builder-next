# Reporting

`psb report --fresh` re-runs every count live and writes `audit.md` with:

- question, framework, concept roles, and whether the user confirmed the scope
- PRISMA-S search details: database and platform, date the counts were run, `as_of` bound,
  total records, limits with rationale
- the strategy line by line with counts, and as one line for copying into PubMed
- recall on each known set with its role, missed records and the blocks that miss them
- leave-one-block-out results
- the development history (every evaluated version, its change, lost records, and note)
- critic rounds and finding status
- standard limitations and the provenance line (NCBI requests, cache use, strategy hash)

Do not edit the numbers in `audit.md`. If something is wrong, fix the workspace and run
`psb report` again.

## Add these sections by hand, below the generated ones

1. **Rationale.** Why each concept is searched or screened; key MeSH decisions (explosion,
   `:noexp`, supplementary concepts); notable text-word choices; why limits were used.
2. **How known records were found.** Sources, screening budget, how many screened and included,
   how the validation set was held out, and whether it later became part of development.
3. **Critic dispositions.** For each finding: what changed, or why it was rejected or accepted.
4. **Open risks for the peer reviewer.** Fragile concepts, records out of reach, noisy terms kept
   on purpose, anything you were unsure about.

## PRISMA-S items this covers (PubMed only)

Items 1 (database), 8 (full strategy), 9 (limits and restrictions), 10 (search filters with
source), 13 (date of search), 16 (records per database). State item 12 (peer review) as
"internal PRESS-structured critic only; PRESS peer review pending". Items about other databases,
registries, citation searching and deduplication are outside this skill.

## Wording to use

- "relative recall against <set>" — never "sensitivity"
- "development set (used to build the strategy)" versus "held-out validation set"
- "PRESS-structured internal critique", never "PRESS peer reviewed"
- If no known records existed: "Recall was not estimated; the strategy is empirically unvalidated."
