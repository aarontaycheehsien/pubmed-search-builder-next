# Anti-Patterns

Recurring failure modes in LLM-built PubMed strategies. Read this when you set the concept
roles and again before you deliver. If a draft shows one of these, revise it.

## Mistake 1: Treating PICO as a Boolean template

Forcing all four PICO elements into `AND` blocks reduces recall. Each added `AND` block compounds retrieval loss.

Bad:

```text
Population AND Intervention AND Comparator AND Outcome
```

Better, in most cases:

```text
Population AND Intervention
```

with Comparator and Outcome handled at screening unless central to the topic.

Evidence: PICO elements C and O have lower retrieval potential in PubMed and Embase ([Frandsen et al. 2020](https://doi.org/10.1016/j.jclinepi.2020.07.005)). Two-block searches retrieved more relevant systematic reviews than four-block searches ([Ho et al. 2016](https://doi.org/10.1371/journal.pone.0167170)).

## Mistake 2: Searching outcomes by default

Broad outcome terms such as:

```text
mortality OR survival OR safety OR effectiveness OR complications
```

are inconsistently reported and indexed. Requiring them as an `AND` block typically reduces recall.

Use outcome terms only when the outcome defines the topic (e.g., a review of mortality from a specific cause) and when seed evidence or pilot testing confirms reliable indexing.

Evidence: [Frandsen et al. 2020](https://doi.org/10.1016/j.jclinepi.2020.07.005) found outcome retrieval was the weakest of the four PICO elements across both Embase and PubMed.

## Mistake 3: Searching comparators by default

Terms such as:

```text
placebo OR usual care OR control group OR standard treatment
```

are usually implicit in study design and inconsistently reported. Do not require them as `AND` blocks unless the comparator defines the topic.

Evidence: [Frandsen et al. 2020](https://doi.org/10.1016/j.jclinepi.2020.07.005).

## Mistake 4: Adding unnecessary limits

Avoid default limits for:

- age
- sex
- language
- geography
- publication date
- setting
- study design

Use limits only when essential and justified. Each limit is a potential source of bias and missed records. When a methodological filter (study design, age group, etc.) is required, use a validated filter from `filters.md` rather than an ad hoc block.

A search cutoff ("what PubMed held on date X", an update's previous search date) belongs in `protocol.json` `as_of`, which bounds on Entrez date. Do not add a `[dp]` or `[Date - Publication]` limit for it: an article in PubMed before the cutoff can carry a later publication date (epub ahead of print, a later issue), and a publication-date limit drops it.

## Mistake 5: Overfitting to seed studies

Seed PMIDs are validation aids, not the whole target set. Do not narrow the strategy to retrieve only the wording used in a small seed set. Maintain breadth so the search retrieves unknown relevant studies.

Use seeds to:

- discover candidate vocabulary
- test whether proposed required concepts would retrieve the seeds
- diagnose missed seeds

Do not use seeds to:

- bound the strategy to seed-only language
- exclude broader synonyms because no seed used them
- treat seed retrieval as sufficient validation

Evidence: [Bramer et al. 2018](https://doi.org/10.5195/jmla.2018.283).

## Mistake 6: Ignoring failed seed retrieval

If a proposed strategy misses an in-scope seed, do not explain it away without analysis. Identify which concept block fails to retrieve the seed and revise unless the seed is documented as out of scope.

`psb eval` lists the blocks that fail each missed record, and `psb terms miss` shows the
record's MeSH headings and the wording your strategy lacks. Revise the failing block, or record
why the record is out of reach.

## Mistake 7: Being overconfident about ambiguous questions

If the question allows plausible alternative interpretations (e.g., "is X the Population or the Outcome?", "is this an intervention or an exposure?", "is this diagnostic accuracy or screening effectiveness?"), the LLM default is to silently pick one interpretation. State the alternatives and resolve the choice with the user before building the strategy. See the ambiguity check in `scope.md`.

Evidence: LLM-generated Boolean queries show median sensitivity of 85% with IQR 40-100% across reviews — much of the variance is attributed to silent committal on ambiguous questions ([Adam et al. 2024](https://doi.org/10.1093/jamiaopen/ooae098)).

## Mistake 8: One-shot Boolean without iteration

Emitting a final Boolean strategy without testing it against seed PMIDs (where supplied) or against PubMed count checks is a documented LLM failure mode. A draft is not a final strategy.

Test with `psb eval`, revise, and run the critic before delivery. Do not skip these steps to deliver a "complete" answer faster.

Evidence: [Adam et al. 2024](https://doi.org/10.1093/jamiaopen/ooae098); [Park, Shin & Kim 2025](https://doi.org/10.69528/jkmla.2025.52.1.28) showed that even with PRESS-style prompting, LLM-generated strategies require human refinement on controlled vocabulary and syntax. [De Cassai et al. 2025](https://doi.org/10.1136/rapm-2024-106231) found ChatGPT-4o retrieved only 6% of the records that expert search strings retrieved across 85 anesthesiology systematic reviews.

## Mistake 9: Over-specific workflow block

For methodological or automation topics, do not require a narrow term family such as Boolean query formulation when relevant papers may describe the broader workflow: searching, screening, study selection, evidence synthesis, systematic-review conduct, or other evidence-synthesis tasks.

Bad:

```text
(large language models) AND (Boolean OR query formulation OR search string)
```

when the review question plausibly includes LLM support across search strategy/query generation, literature/database searching, title/abstract screening, full-text screening, study selection, data extraction, risk of bias, synthesis, or review drafting.

Better: use a broader workflow block for the main recall-first strategy, and keep the narrow action terms as a focused/reserve variant or within-block vocabulary when the protocol does not explicitly narrow the scope.

## Mistake 10: Standalone ambiguous model or acronym terms

Avoid standalone model names or acronyms when they have common non-LLM meanings. A term like `LLaMA[tiab]` can retrieve animal, antibody, or construct records unrelated to large language models. Prefer phrase variants tied to the model family, such as `"Llama 2"[tiab]`, `"Llama-2"[tiab]`, `"Llama 3"[tiab]`, and `"Llama-3"[tiab]`, and document any broader acronym only when testing shows it is useful and tolerable.

## Mistake 11: Treating low count as precision

A final topic-only count below 500 is not proof that the strategy is precise. It may indicate an over-specific concept block, too many `AND` blocks, narrow workflow/action language, missing MeSH or title/abstract variants, PubMed translation drift, or an unnecessary filter or limit.

Do not expand automatically just to exceed 500 records. Diagnose the low count. If the topic is rare, new, tightly scoped, or protocol-limited, document why a count under 500 is plausible. If the count reflects avoidable narrowing, revise/expand the bottleneck block, rerun the final topic-only count, and document before/after counts.

## Mistake 12: Letting seeds define scope

Reading seeds before setting the concept roles lets a small or biased set decide which elements become search blocks. Set the roles in `protocol.json` from the question first. Afterwards, records may change vocabulary and search structure, never eligibility; record any role change in `protocol.json` with its reason.

## Mistake 13: Mining unscreened pilot or related records

High-precision pilot hits, similar articles, citations, and high-overlap neighbours are candidates, not relevant studies. Screen each against the eligibility criteria before adding it to a set; only screened sets feed `psb terms rank`.

## Mistake 14: Calling automated QA PRESS peer review

Mapping a draft to PRESS elements or asking another model pass to criticize it is PRESS-informed internal QA. It does not become PRESS peer review without an independent information specialist. Preserve the human handoff and report the automated critic rounds separately.

## Mistake 15: A block for one direction of a process

Bad, for "patients switched from a biosimilar back to the originator":

```text
Biosimilar AND ("switching back"[tiab] OR "reverse switch"[tiab] OR "back to originator"[tiab:~2])
```

Most studies that report a switch back are cohorts of the forward switch, and say so in one sentence ("19 patients switched back") or only in the full text. A phrase list also misses inflections ("switched back"). Better:

```text
Biosimilar AND ("Drug Substitution"[Mesh] OR switch*[tiab] OR transition*[tiab] OR substitut*[tiab])
```

with the direction screened. See "Direction, sequence and events in a subset" in `scope.md`.

## Mistake 16: Narrowing the members the criteria name

Bad, when eligibility says "SEM-family models (CFA, latent growth, multilevel, mediation)":

```text
"multilevel structural equation"[tiab] OR "mediation model*"[tiab]
```

Better: `multilevel[tiab] OR "Multilevel Analysis"[Mesh] OR mediation[tiab] OR "indirect effect*"[tiab]`. A paper on Bayesian multilevel models seldom says "structural equation"; that is why the criteria list multilevel models separately. See "Named members of a concept" in `scope.md`.

## References

- Adam GP, et al. Literature search sandbox: a large language model that generates search queries for systematic reviews. *JAMIA Open* 2024. [doi:10.1093/jamiaopen/ooae098](https://doi.org/10.1093/jamiaopen/ooae098).
- Bramer WM, et al. A systematic approach to searching: an efficient and complete method to develop literature searches. *JMLA* 2018. [doi:10.5195/jmla.2018.283](https://doi.org/10.5195/jmla.2018.283).
- De Cassai A, et al. Evaluating the utility of large language models in generating search strings for systematic reviews in anesthesiology. *Regional Anesthesia & Pain Medicine* 2025. [doi:10.1136/rapm-2024-106231](https://doi.org/10.1136/rapm-2024-106231).
- Frandsen TF, et al. Using the full PICO model as a search tool for systematic reviews resulted in lower recall for some PICO elements. *J Clin Epidemiol* 2020. [doi:10.1016/j.jclinepi.2020.07.005](https://doi.org/10.1016/j.jclinepi.2020.07.005).
- Ho GJ, et al. Development of a Search Strategy for an Evidence Based Retrieval Service. *PLoS ONE* 2016. [doi:10.1371/journal.pone.0167170](https://doi.org/10.1371/journal.pone.0167170).
- Park H, Shin DW, Kim NJ. Quality Evaluation of Generative AI-Based Search Strategies in Systematic Reviews and Comparison of Search Performance with Human Expert (Medical Librarian). *J Korean Med Library Assoc* 2025. [doi:10.69528/jkmla.2025.52.1.28](https://doi.org/10.69528/jkmla.2025.52.1.28).
