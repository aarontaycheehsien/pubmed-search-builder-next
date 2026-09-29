# PubMed search strategy: audit

Generated 2026-09-29T19:14:25+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In population-based cohorts, is cerebral small vessel disease (and its MRI markers) associated with the risk of incident dementia and cognitive decline?
- Framework: PECO
- Scope confirmed by user: yes (User asked to proceed without clarification; scope and roles were set from the supplied question and criteria. Standard depth; no seeds supplied; no language or other search limits. The run is bounded to PubMed records present by Entrez date 2017-05-06 via PSB_AS_OF on every command; no publication-date limit is applied. No known articles or review were supplied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Cerebral small vessel disease and its MRI markers | search | The exposure is essential and has a named disease concept plus explicitly listed MRI-marker members; search both category wording and the named markers. |
| Incident dementia and cognitive decline | optional | This topic-defining outcome may reduce an otherwise broad imaging exposure set, but outcome reporting in abstracts is not reliable enough to require without testing. |
| Population-based or community-dwelling cohort | optional | Population setting is recognizable and may help control screening workload, but community status can be inconsistently named. |
| Prospective cohort or longitudinal follow-up design | optional | Cohort/follow-up labels are searchable but design can be incompletely described in abstracts; test before requiring. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T19:13:46+00:00
- Records added to PubMed up to: 2017-05-06
- Total records: 20,767
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Cerebral Small Vessel Diseases[Mesh]` | 6,257 | none |
| 2 | `Leukoaraiosis[Mesh]` | 470 | none |
| 3 | `Stroke, Lacunar[Mesh]` | 412 | none |
| 4 | `"cerebral small vessel disease"[tiab]` | 813 | none |
| 5 | `"cerebral small-vessel disease"[tiab]` | 813 | none |
| 6 | `"small vessel disease"[tiab]` | 2,316 | none |
| 7 | `"small-vessel disease"[tiab]` | 2,316 | none |
| 8 | `cerebral microangiopath*[tiab]` | 150 | none |
| 9 | `leukoaraios*[tiab]` | 1,010 | none |
| 10 | `"white matter hyperintens*"[tiab]` | 2,354 | none |
| 11 | `("white matter"[tiab:~2] AND hyperintens*[tiab])` | 3,883 | none |
| 12 | `"white matter lesion*"[tiab]` | 4,051 | none |
| 13 | `"white matter abnormalit*"[tiab]` | 1,590 | none |
| 14 | `"lacunar infarct*"[tiab]` | 2,251 | none |
| 15 | `"lacunar stroke*"[tiab]` | 918 | none |
| 16 | `"silent brain infarct*"[tiab]` | 280 | none |
| 17 | `"silent cerebral infarct*"[tiab]` | 322 | none |
| 18 | `"silent infarct*"[tiab]` | 311 | none |
| 19 | `"covert brain infarct*"[tiab]` | 9 | none |
| 20 | `"subcortical infarct*"[tiab]` | 1,322 | none |
| 21 | `cerebral microbleed*[tiab]` | 710 | none |
| 22 | `microbleed*[tiab]` | 1,468 | none |
| 23 | `cerebral microinfarct*[tiab]` | 43 | none |
| 24 | `"vascular brain injur*"[tiab]` | 77 | none |
| 25 | `"small vessel ischemic disease"[tiab]` | 15 | none |
| 26 | `"small vessel ischaemic disease"[tiab]` | 3 | none |
| 27 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26` | 20,767 | none |

### Strategy (single line, for copying into PubMed)

```text
((Cerebral Small Vessel Diseases[Mesh] OR Leukoaraiosis[Mesh] OR Stroke, Lacunar[Mesh] OR "cerebral small vessel disease"[tiab] OR "cerebral small-vessel disease"[tiab] OR "small vessel disease"[tiab] OR "small-vessel disease"[tiab] OR cerebral microangiopath*[tiab] OR leukoaraios*[tiab] OR "white matter hyperintens*"[tiab] OR ("white matter"[tiab:~2] AND hyperintens*[tiab]) OR "white matter lesion*"[tiab] OR "white matter abnormalit*"[tiab] OR "lacunar infarct*"[tiab] OR "lacunar stroke*"[tiab] OR "silent brain infarct*"[tiab] OR "silent cerebral infarct*"[tiab] OR "silent infarct*"[tiab] OR "covert brain infarct*"[tiab] OR "subcortical infarct*"[tiab] OR cerebral microbleed*[tiab] OR microbleed*[tiab] OR cerebral microinfarct*[tiab] OR "vascular brain injur*"[tiab] OR "small vessel ischemic disease"[tiab] OR "small vessel ischaemic disease"[tiab])) AND ("1800/01/01"[edat] : "2017/05/06"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Incident dementia and cognitive decline | left out | 20,767 / 5,909 | 71.5% | none | 0/30 (up to 10% of removed records could be relevant) | The required exposure block was widened per critic and the outcome loss sample was redrawn and screened (30 records, none eligible). Only three known development records remain, below the 15-record safety threshold, so outcome terms stay out of the required query. |
| Population-based or community-dwelling cohort | left out | 20,767 / 933 | 95.5% | none | 0/30 (up to 10% of removed records could be relevant) | The required exposure block was widened per critic and the population loss sample was redrawn and screened (30 records, none eligible). Only three known development records remain, below the 15-record safety threshold, so community/population terms stay out of the required query. |
| Prospective cohort or longitudinal follow-up design | left out | 20,767 / 6,693 | 67.8% | none | 0/30 (up to 10% of removed records could be relevant) | The required exposure block was widened per critic and the longitudinal-design loss sample was redrawn and screened (30 records, none eligible). Only three known development records remain, below the 15-record safety threshold, so design terms stay out of the required query. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Cerebral small vessel disease and its MRI markers | 1 | `(Cerebrovascular Disorders[Mesh] OR brain vascular lesion*[tiab] OR brain microvascular disease*[tiab]) AND (cognit*[tiab] OR dement*[tiab])` | 13,804 | 0/30 |
| Incident dementia and cognitive decline | 1 | `(memory[tiab] OR neuropsycholog*[tiab] OR mental status[tiab])` | 271 | 0/30 |
| Incident dementia and cognitive decline | 2 | `(memory[tiab] OR neuropsycholog*[tiab] OR mental status[tiab])` | 278 | 0/30 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial exposure block from question vocabulary; optional outcome, setting, and design retained for empirical testing. |
| 2 | 337,211 | svd: +0 / -1 | none | Initial exposure block after removing invalid one-word proximity phrase variant; added screened relevant pilot record. |
| 3 | 20,593 | svd: +0 / -2 | none | Removed very broad legacy Cerebrovascular Disorders and Cerebral Infarction MeSH headings whose counts overwhelmed the named small-vessel MRI marker concepts; retained the specific SVD, leukoaraiosis, lacunar-stroke headings and marker text terms. |
| 4 | 20,767 | svd: +2 / -0 | none | Added explicit bare-name title/abstract expressions for white matter hyperintensity and silent infarct per critic finding F2; no other changes. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 1 findings; F1 must-fix rejected
- Round 2 on version 3: 2 findings; F1 must-fix rejected, F2 must-fix open
- Round 3 on version 4: 2 findings; F1 must-fix rejected, F2 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 976 NCBI requests logged (351 from cache); strategy sha256 cd77939b0976._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "code": "over_workload_budget",
        "message": "20,767 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:outcome",
        "blocking": false,
        "requires_review": true,
        "id": "I-ecaf5eb32c2cc01a9487"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:population",
        "blocking": false,
        "requires_review": true,
        "id": "I-5334920505c6387f26fe"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:longitudinal",
        "blocking": false,
        "requires_review": true,
        "id": "I-c646ec15555b8ea769b6"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "20,767 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:outcome",
        "blocking": false,
        "requires_review": true,
        "id": "I-ecaf5eb32c2cc01a9487"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:population",
        "blocking": false,
        "requires_review": true,
        "id": "I-5334920505c6387f26fe"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:longitudinal",
        "blocking": false,
        "requires_review": true,
        "id": "I-c646ec15555b8ea769b6"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Cerebral Small Vessel Diseases",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:13:46+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D059345",
          "name": "Cerebral Small Vessel Diseases",
          "type": "descriptor",
          "scope_note": "Pathological processes or diseases where cerebral MICROVESSELS show abnormalities. They are often associated with aging, hypertension and risk factors for lacunar infarcts (see LACUNAR INFARCTION); LEUKOARAIOSIS; and CEREBRAL HEMORRHAGE.",
          "tree_numbers": [
            "C10.228.140.300.275",
            "C14.907.253.329"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D059345",
      "preferred_label": "Cerebral Small Vessel Diseases",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "Cerebral Small Vessel Diseases",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Leukoaraiosis",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:13:46+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D049292",
          "name": "Leukoaraiosis",
          "type": "descriptor",
          "scope_note": "Non-specific white matter changes in the BRAIN, often seen after age 65. Changes include loss of AXONS; MYELIN pallor, GLIOSIS, loss of ependymal cells, and enlarged perivascular spaces. Leukoaraiosis is a risk factor for DEMENTIA and CEREBROVASCULAR DISORDERS.",
          "tree_numbers": [
            "C23.550.522"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D049292",
      "preferred_label": "Leukoaraiosis",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "Leukoaraiosis",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stroke, Lacunar",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:13:46+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D059409",
          "name": "Stroke, Lacunar",
          "type": "descriptor",
          "scope_note": "Stroke caused by lacunar infarction or other small vessel diseases of the brain. It features hemiparesis (see PARESIS), hemisensory, or hemisensory motor loss.",
          "tree_numbers": [
            "C10.228.140.300.275.800",
            "C10.228.140.300.775.400.750.500",
            "C14.907.253.329.800",
            "C14.907.253.855.400.750.500",
            "C23.550.513.355.250.600",
            "C23.550.717.489.250.600"
          ],
          "entry_terms": 15,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D059409",
      "preferred_label": "Stroke, Lacunar",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "Stroke, Lacunar",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"cerebral small vessel diseases\"[MeSH Terms] OR \"leukoaraiosis\"[MeSH Terms] OR \"stroke, lacunar\"[MeSH Terms] OR \"cerebral small-vessel disease\"[Title/Abstract] OR \"cerebral small-vessel disease\"[Title/Abstract] OR \"small-vessel disease\"[Title/Abstract] OR \"small-vessel disease\"[Title/Abstract] OR \"cerebral microangiopath*\"[Title/Abstract] OR \"leukoaraios*\"[Title/Abstract] OR \"white matter hyperintens*\"[Title/Abstract] OR (\"white matter\"[Title/Abstract:~2] AND \"hyperintens*\"[Title/Abstract]) OR \"white matter lesion*\"[Title/Abstract] OR \"white matter abnormalit*\"[Title/Abstract] OR \"lacunar infarct*\"[Title/Abstract] OR \"lacunar stroke*\"[Title/Abstract] OR \"silent brain infarct*\"[Title/Abstract] OR \"silent cerebral infarct*\"[Title/Abstract] OR \"silent infarct*\"[Title/Abstract] OR \"covert brain infarct*\"[Title/Abstract] OR \"subcortical infarct*\"[Title/Abstract] OR \"cerebral microbleed*\"[Title/Abstract] OR \"microbleed*\"[Title/Abstract] OR \"cerebral microinfarct*\"[Title/Abstract] OR \"vascular brain injur*\"[Title/Abstract] OR \"small vessel ischemic disease\"[Title/Abstract] OR \"small vessel ischaemic disease\"[Title/Abstract]) AND 1800/01/01:2017/05/06[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "9047df42d20ac4e51e0b2f78dbc7215d3f9dc31e0d010d0538863d221e105222",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched SVD/MRI-marker block includes disease-category language and individual terms for the MRI markers named in eligibility. Outcome, setting, and longitudinal design remain optional and are not made mandatory."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within the single required concept, and the final strategy applies no untested mandatory outcome, population, or design conjunction. The white-matter/hyperintensity proximity expression uses no wildcard within proximity; ~2 does not impose word order."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Cerebral Small Vessel Diseases, Leukoaraiosis, and Stroke, Lacunar headings supplement the text-word coverage. The packet does not establish a missing heading that would constitute a technical error."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words cover the named disease and marker concepts, including spelling variants for small-vessel terminology, silent/covert infarcts, microbleeds, and vascular brain injury. Discovery of three known records via similar and citing candidates linked to a relevant 2013 review is documented; the small validation set remains a limitation rather than evidence of a specific missing term."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed PubMed query is parenthesized, uses field tags consistently, and its expressions have tested counts with no syntax diagnostics or phrase warnings in the packet."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez-date ceiling is explicitly required by the run instructions to simulate a 2017-05-06 search and exclude records added to PubMed later. It is recorded as an as-of bound, not an ad hoc publication-date filter."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query applies an Entrez-date ceiling of 2017-05-06. The review question and eligibility criteria give no temporal boundary, so the strategy excludes all records entered after that date and cannot represent an unrestricted search.",
          "recommendation": "Remove the Entrez-date restriction and rerun the complete term evaluation and validation, or document a scope-authorized date boundary and report it explicitly.",
          "status": "rejected",
          "response": "Rejected because this run has an explicit temporal scope from the harness: treat the database as of 2017-05-06 and exclude records entered afterward using PSB_AS_OF. The date bound is part of the requested simulation and must remain set on every PubMed command; it is an Entrez-date ceiling, not a [dp] publication-date limit."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The 20,593-record result set exceeds the stated 10,000-record workload budget. Each of the three searchable optional concepts was tested, and the loss samples contained no relevant records, but sample sizes of 30 do not establish safe sensitivity. With only three known development records, excluding optional blocks preserves recall at the cost of an over-budget screening workload.",
          "evidence": "The packet reports 20,593 results, a 10,000-record budget, tests for outcome, population, and longitudinal blocks, zero relevant records in each 30-record loss sample, and three known development records."
        },
        {
          "issue_id": "I-ecaf5eb32c2cc01a9487",
          "status": "accepted-risk",
          "response": "The low known-record count remains a limitation for deciding whether outcome terms can safely reduce workload. The packet documents a search of similar and citing records linked to a relevant 2013 review, which found three screened development records; the outcome block remains optional to protect recall.",
          "evidence": "The discovery source is recorded in the relevant-set metadata. The outcome block reduces results by 71.5%, with zero relevant records in a 30-record loss sample and no known records lost."
        },
        {
          "issue_id": "I-5334920505c6387f26fe",
          "status": "accepted-risk",
          "response": "The low known-record count limits confidence in the population block's workload benefit. Discovery through similar and citing candidates linked to the 2013 review is documented; the population block remains optional because community/population status can be inconsistently reported and the sample does not demonstrate safe exclusion.",
          "evidence": "The population block would reduce results by 95.5%; its 30-record loss sample contained zero eligible records and no known record was lost."
        },
        {
          "issue_id": "I-c646ec15555b8ea769b6",
          "status": "accepted-risk",
          "response": "The low known-record count limits confidence in the longitudinal block's workload benefit. Discovery through similar and citing candidates linked to the 2013 review is documented; the design block remains optional because follow-up wording can be inconsistently reported and the sample does not demonstrate safe exclusion.",
          "evidence": "The longitudinal block would reduce results by 67.9%; its 30-record loss sample contained zero eligible records and no known record was lost."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "9047df42d20ac4e51e0b2f78dbc7215d3f9dc31e0d010d0538863d221e105222",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The required exposure block lacks bare-name coverage for two MRI markers explicitly named in eligibility: white matter hyperintensity appears only as a proximity combination, and silent infarct appears only in narrower phrases such as silent brain/cerebral infarct. Add explicit tested bare-name expressions before accepting translation."
        },
        "operators": {
          "verdict": "pass",
          "note": "The final query ORs terms within the required exposure block and does not AND optional outcome, population, or design concepts. The ~2 proximity operator permits either order, and no wildcard occurs inside a proximity expression."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet tests Cerebral Small Vessel Diseases, Leukoaraiosis, and Stroke, Lacunar headings. It does not establish a specific missing heading as a technical error; the named-marker bare-name gaps are recorded under translation."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The marker vocabulary misses bare-name text expressions for white matter hyperintensity and silent infarct. Existing proximity and narrower phrases do not satisfy the packet's explicit member-by-member bare-name check."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed query is parenthesized and uses consistent field tags. Tested counts show no syntax diagnostics or phrase warnings; the proximity expression contains no wildcard and ~2 allows either order. Any vocabulary rewrite must be fully reevaluated."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez-date ceiling implements the packet's required 2017-05-06 as-of simulation, is applied as an entry-date bound rather than a publication-date limit, and has no other reported limits."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query applies an Entrez-date ceiling of 2017-05-06. The review question and eligibility criteria give no temporal boundary, so the strategy excludes records entered later and cannot represent an unrestricted search.",
          "recommendation": "Remove the Entrez-date restriction and rerun the complete term evaluation and validation, or document a scope-authorized date boundary and report it explicitly.",
          "status": "rejected",
          "response": "The packet specifies a PSB_AS_OF simulation through 2017-05-06 and requires that entry-date bound on every PubMed command. The date restriction is therefore authorized by the run scope, not an unsupported publication-date filter."
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility explicitly names white matter hyperintensity and lacunar/silent infarct as MRI markers. The strategy represents white matter hyperintensity only through a white matter/hyperintens* proximity combination and silent infarct only in narrower phrases (silent brain/cerebral infarct*); it lacks each marker's own bare-name expression under the packet's translation rule.",
          "recommendation": "Add explicit tested bare-name expressions such as \"white matter hyperintens*\"[tiab] and \"silent infarct*\"[tiab], then rerun the complete term evaluation, counts, category probes, and validation before accepting the rewrite.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The required exposure-only set remains above the workload budget. Optional outcome, population, and longitudinal blocks were individually tested, but their loss samples are too small and only three screened development records are known, so omitting them protects recall while leaving an over-budget workload.",
          "evidence": "The required set returns 20,593 records against a 10,000-record budget. The three optional block tests reduce results by 71.5%, 95.5%, and 67.9%, respectively; each 30-record loss sample contained zero eligible records, and the relevant set has three records."
        },
        {
          "issue_id": "I-ecaf5eb32c2cc01a9487",
          "status": "accepted-risk",
          "response": "The outcome block remains optional because only three development records are known and the loss sample does not establish that mandatory outcome terms are safe. The documented discovery attempt through similar and citing candidates linked to a relevant 2013 review supports retaining the recall-first choice.",
          "evidence": "The relevant-set metadata records that discovery source and identifies three screened records. The outcome block would reduce 20,593 records to 5,864; its 30-record loss sample contained no eligible record and no known relevant record was lost."
        },
        {
          "issue_id": "I-5334920505c6387f26fe",
          "status": "accepted-risk",
          "response": "The population/community block remains optional because its large workload reduction is not supported by enough known records or a sufficiently informative loss sample to establish safe mandatory use; community status may also be inconsistently reported.",
          "evidence": "The block would reduce 20,593 records to 919, with no known record lost and zero eligible records among 30 sampled losses. Only three screened development records are documented."
        },
        {
          "issue_id": "I-c646ec15555b8ea769b6",
          "status": "accepted-risk",
          "response": "The prospective/cohort/follow-up block remains optional because its loss sample and the three known records do not establish safe mandatory use, and design or follow-up wording may be absent from abstracts.",
          "evidence": "The block would reduce 20,593 records to 6,607, with no known record lost and zero eligible records among 30 sampled losses. Only three screened development records are documented."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "008818d1350af3d963768919454b90ada36458d0787d88f1cf3068c17246b2a0",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The v4 exposure block now includes the explicitly requested bare-name expressions \"white matter hyperintens*\"[tiab] and \"silent infarct*\"[tiab], in addition to category and other marker terms. Both terms have tested counts without diagnostics; the required exposure remains the only mandatory concept."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within the required exposure block; outcome, population, and design remain optional and are not AND-ed into the final query. The ~2 proximity expression permits either order and contains no wildcard."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy tests Cerebral Small Vessel Diseases, Leukoaraiosis, and Stroke, Lacunar headings. The packet does not establish a specific missing heading as a technical error."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The revised text-word set covers the named disease and MRI-marker members, including bare-name white matter hyperintensity and silent infarct expressions, and retains additional marker and spelling variants. Tested counts show no diagnostics."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed current query is parenthesized with consistent field tags. The proximity expression has no wildcard and allows either word order; tested expressions report no syntax diagnostics or phrase warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No strategy limits are configured. The required 2017-05-06 as-of simulation is implemented as an Entrez entry-date ceiling on PubMed commands, not a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query applies an Entrez-date ceiling of 2017-05-06. The review question and eligibility criteria give no temporal boundary, so the strategy excludes records entered later and cannot represent an unrestricted search.",
          "recommendation": "Remove the Entrez-date restriction and rerun the complete term evaluation and validation, or document a scope-authorized date boundary and report it explicitly.",
          "status": "rejected",
          "response": "The packet explicitly requires a PSB_AS_OF simulation through 2017-05-06 and that entry-date bound on every PubMed command. The restriction is authorized by the run scope, rather than an unsupported publication-date filter."
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility explicitly names white matter hyperintensity and lacunar/silent infarct as MRI markers. The strategy represents white matter hyperintensity only through a white matter/hyperintens* proximity combination and silent infarct only in narrower phrases (silent brain/cerebral infarct*); it lacks each marker's own bare-name expression under the packet's translation rule.",
          "recommendation": "Add explicit tested bare-name expressions such as \"white matter hyperintens*\"[tiab] and \"silent infarct*\"[tiab], then rerun the complete term evaluation, counts, category probes, and validation before accepting the rewrite.",
          "status": "resolved",
          "response": "The v4 strategy adds both requested bare-name terms to the required exposure block. The packet reports tested counts of 2,354 for \"white matter hyperintens*\"[tiab] and 311 for \"silent infarct*\"[tiab], no diagnostics, and a 20,767-record current exposure set; the outcome, population, and longitudinal loss samples were redrawn after widening the exposure block, and the current validation is complete with no known-record loss."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The required exposure-only set remains above the workload budget. The optional outcome, population, and longitudinal blocks were tested, but the small loss samples and only three known development records do not establish that requiring an optional block is safe; the recall-first strategy therefore retains a larger screening workload.",
          "evidence": "The current required set returns 20,767 records against a 10,000-record budget. The optional blocks reduce results by 71.5%, 95.5%, and 67.8%, respectively; each updated 30-record loss sample contains zero eligible records, and three known development records are documented."
        },
        {
          "issue_id": "I-ecaf5eb32c2cc01a9487",
          "status": "accepted-risk",
          "response": "The outcome block remains optional because the three known records and sampled losses do not establish that mandatory outcome terms are safe. The documented similar and citing candidate search linked to a relevant 2013 review provides a discovery attempt, while omitting the block protects recall.",
          "evidence": "The relevant-set metadata documents three screened records and the discovery source. The updated outcome test reduces 20,767 results to 5,909; none of the 30 sampled losses was eligible and no known record is reported lost."
        },
        {
          "issue_id": "I-5334920505c6387f26fe",
          "status": "accepted-risk",
          "response": "The population/community block remains optional because the small known set and loss sample do not establish that population-setting terms are safe as a mandatory requirement; the packet also notes that community status may be inconsistently reported.",
          "evidence": "The updated population test reduces 20,767 results to 933; none of the 30 sampled losses was eligible and no known record is reported lost. Three screened development records are documented."
        },
        {
          "issue_id": "I-c646ec15555b8ea769b6",
          "status": "accepted-risk",
          "response": "The prospective/cohort/follow-up block remains optional because neither the small known set nor the loss sample establishes safe mandatory use, and design or follow-up wording may be absent from abstracts.",
          "evidence": "The updated longitudinal-design test reduces 20,767 results to 6,693; none of the 30 sampled losses was eligible and no known record is reported lost. Three screened development records are documented."
        }
      ]
    }
  ]
}
```

