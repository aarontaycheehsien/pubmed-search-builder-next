# PubMed search strategy: audit

Generated 2026-09-29T03:17:52+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In population-based cohorts, is cerebral small vessel disease (and its MRI markers) associated with the risk of incident dementia and cognitive decline?
- Framework: PECO
- Scope confirmed by user: yes (User requested no follow-up questions and authorized reasonable assumptions. Standard depth; no user-supplied known articles. Scope roles are provisional but proceeding: exposure searched, outcome tested as optional, population and longitudinal follow-up screened. No language or publication-date limit. Harness PubMed entry-date cutoff is 2017-05-06; this is not a [dp] restriction. Community-dwelling population-based cohorts are interpreted broadly to include longitudinal observational cohorts sampling community populations. The outcome is a listed set of named endpoints rather than an open-ended member category, so category probing is not applicable.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Cerebral small vessel disease and MRI markers | search | The exposure defines the review and its disease and MRI-marker members are named in the eligibility criteria; search both the category and members. |
| Incident dementia, Alzheimer disease, cognitive decline or impairment | optional | A topic-defining outcome that authors often name but may omit from abstracts; test the outcome block before deciding whether to AND it. |
| Population-based or community-dwelling participants | screen | Population-based sampling and community-dwelling status are eligibility properties inconsistently named in titles/abstracts. |
| Prospective/longitudinal observational cohort with follow-up | screen | Design and follow-up eligibility are not reliably captured by a PubMed block; screen records. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T03:17:15+00:00
- Records added to PubMed up to: 2017-05-06
- Total records: 45,434
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Cerebral Small Vessel Diseases"[Mesh]` | 6,257 | none |
| 2 | `"Leukoaraiosis"[Mesh]` | 470 | none |
| 3 | `"Stroke, Lacunar"[Mesh]` | 412 | none |
| 4 | `"Cerebral Infarction"[Mesh]` | 29,744 | none |
| 5 | `"cerebral small vessel disease"[tiab]` | 813 | none |
| 6 | `"small vessel disease"[tiab]` | 2,316 | none |
| 7 | `"cerebral microangiopath*"[tiab]` | 150 | none |
| 8 | `"small vessel ischemic disease"[tiab]` | 15 | none |
| 9 | `"small vessel ischemic change*"[tiab]` | 2 | none |
| 10 | `"white matter hyperintensity"[tiab]` | 738 | none |
| 11 | `"white matter hyperintensities"[tiab]` | 1,776 | none |
| 12 | `"white matter lesion"[tiab]` | 615 | none |
| 13 | `"white matter lesions"[tiab]` | 3,662 | none |
| 14 | `"white matter change"[tiab]` | 112 | none |
| 15 | `"white matter changes"[tiab]` | 1,796 | none |
| 16 | `leukoaraiosis[tiab]` | 1,008 | none |
| 17 | `"lacunar infarct"[tiab]` | 396 | none |
| 18 | `"lacunar infarcts"[tiab]` | 968 | none |
| 19 | `"silent infarct"[tiab]` | 68 | none |
| 20 | `"silent infarcts"[tiab]` | 151 | none |
| 21 | `"silent brain infarct"[tiab]` | 24 | none |
| 22 | `"silent brain infarcts"[tiab]` | 115 | none |
| 23 | `"cerebral microbleed"[tiab]` | 65 | none |
| 24 | `"cerebral microbleeds"[tiab]` | 685 | none |
| 25 | `"brain microbleed"[tiab]` | 2 | none |
| 26 | `"brain microbleeds"[tiab]` | 59 | none |
| 27 | `microbleed*[tiab]` | 1,468 | none |
| 28 | `"vascular brain injury"[tiab]` | 73 | none |
| 29 | `"vascular brain damage"[tiab]` | 47 | none |
| 30 | `"subclinical brain infarct"[tiab]` | 1 | none |
| 31 | `"subclinical brain infarcts"[tiab]` | 9 | none |
| 32 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31` | 45,434 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Cerebral Small Vessel Diseases"[Mesh] OR "Leukoaraiosis"[Mesh] OR "Stroke, Lacunar"[Mesh] OR "Cerebral Infarction"[Mesh] OR "cerebral small vessel disease"[tiab] OR "small vessel disease"[tiab] OR "cerebral microangiopath*"[tiab] OR "small vessel ischemic disease"[tiab] OR "small vessel ischemic change*"[tiab] OR "white matter hyperintensity"[tiab] OR "white matter hyperintensities"[tiab] OR "white matter lesion"[tiab] OR "white matter lesions"[tiab] OR "white matter change"[tiab] OR "white matter changes"[tiab] OR leukoaraiosis[tiab] OR "lacunar infarct"[tiab] OR "lacunar infarcts"[tiab] OR "silent infarct"[tiab] OR "silent infarcts"[tiab] OR "silent brain infarct"[tiab] OR "silent brain infarcts"[tiab] OR "cerebral microbleed"[tiab] OR "cerebral microbleeds"[tiab] OR "brain microbleed"[tiab] OR "brain microbleeds"[tiab] OR microbleed*[tiab] OR "vascular brain injury"[tiab] OR "vascular brain damage"[tiab] OR "subclinical brain infarct"[tiab] OR "subclinical brain infarcts"[tiab])) AND ("1800/01/01"[edat] : "2017/05/06"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 8 | 8 | 100.0% |
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 2 | 2 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Incident dementia, Alzheimer disease, cognitive decline or impairment | left out | 45,434 / 7,030 | 84.5% | none | 0/30 (up to 10% of removed records could be relevant) | The 30-record loss sample contained no eligible study, and the block would cut the search by 84.5%; however, only 10 known eligible records were found, below the required 15 records needed to establish that AND-ing this topic-defining outcome block is safe. Leave it out to protect recall and screen outcomes manually. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Cerebral small vessel disease and MRI markers | 1 | `((Cerebrovascular Disorders[Mesh] OR Cerebral Infarction[Mesh] OR Brain Infarction[Mesh] OR White Matter[Mesh] OR white matter[tiab] OR infarct*[tiab] OR microangiopath*[tiab] OR perivascular space*[tiab] OR vascular brain injury[tiab]) AND (Dementia[Mesh] OR Alzheimer Disease[Mesh] OR Cognitive Dysfunction[Mesh] OR dementia*[tiab] OR Alzheimer*[tiab] OR cognitive decline[tiab] OR cognitive impairment[tiab]))` | 17,194 | 0/30 |
| Cerebral small vessel disease and MRI markers | 2 | `(Cerebrovascular Disorders[Mesh] OR White Matter[Mesh] OR white matter[tiab] OR infarct*[tiab] OR microangiopath*[tiab] OR microbleed*[tiab] OR perivascular space*[tiab] OR vascular brain injury[tiab])` | 531,174 | 0/30 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 335,819 | initial | none | Initial broad exposure block combines SVD and named MRI marker vocabulary with MeSH and title/abstract terms; outcome tested as optional because it is topic-defining but may be inconsistently reported. |
| 2 | 335,819 | svd: +0 / -1 | none | Revised outcome category classification (enumerated named endpoints) and removed the plural leukoaraioses clause after PubMed returned an unrecognized phrase/no hits; singular leukoaraiosis and its MeSH heading remain. |
| 3 | 17,406 | svd: +4 / -1 | none | Removed the overly broad legacy Cerebrovascular Disorders heading after its line retrieved 329,326 records, and added the user's vascular-brain-injury wording plus subclinical infarct variants; all retained marker terms still have MeSH and text layers. |
| 4 | 45,434 | svd: +1 / -0 | none | Added the MeSH heading Cerebral Infarction to cover indexed cerebral infarcts, including MRI-defined infarcts not named in the title/abstract; this addresses the single missed review-benchmark cohort. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 1 findings; R1-01 should-fix open
- Round 2 on version 4: 1 findings; R1-01 should-fix resolved
- Round 3 on version 4: 1 findings; R1-01 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 817 NCBI requests logged (303 from cache); strategy sha256 8bc42fa1fc6d._

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
        "message": "45,434 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "45,434 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Cerebral Small Vessel Diseases",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:17:15+00:00",
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
        "text": "\"Cerebral Small Vessel Diseases\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Leukoaraiosis",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:17:15+00:00",
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
        "text": "\"Leukoaraiosis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stroke, Lacunar",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:17:15+00:00",
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
        "text": "\"Stroke, Lacunar\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cerebral Infarction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:17:15+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D002544",
          "name": "Cerebral Infarction",
          "type": "descriptor",
          "scope_note": "The formation of an area of NECROSIS in the CEREBRUM caused by an insufficiency of arterial or venous blood flow. Infarcts of the cerebrum are generally classified by hemisphere (i.e., left vs. right), lobe (e.g., frontal lobe infarction), arterial distribution (e.g., INFARCTION, ANTERIOR CEREBRAL ARTERY), and etiology (e.g., embolic infarction).",
          "tree_numbers": [
            "C10.228.140.300.150.477.200",
            "C10.228.140.300.775.200.200",
            "C14.907.253.092.477.200",
            "C14.907.253.855.200.200",
            "C23.550.513.355.250.200",
            "C23.550.717.489.250.200"
          ],
          "entry_terms": 25,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D002544",
      "preferred_label": "Cerebral Infarction",
      "type": "descriptor",
      "location": "vocabulary:4",
      "term": {
        "text": "\"Cerebral Infarction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Cerebral Small Vessel Diseases\"[MeSH Terms] OR \"Leukoaraiosis\"[MeSH Terms] OR \"stroke, lacunar\"[MeSH Terms] OR \"Cerebral Infarction\"[MeSH Terms] OR \"cerebral small vessel disease\"[Title/Abstract] OR \"small vessel disease\"[Title/Abstract] OR \"cerebral microangiopath*\"[Title/Abstract] OR \"small vessel ischemic disease\"[Title/Abstract] OR \"small vessel ischemic change*\"[Title/Abstract] OR \"white matter hyperintensity\"[Title/Abstract] OR \"white matter hyperintensities\"[Title/Abstract] OR \"white matter lesion\"[Title/Abstract] OR \"white matter lesions\"[Title/Abstract] OR \"white matter change\"[Title/Abstract] OR \"white matter changes\"[Title/Abstract] OR \"Leukoaraiosis\"[Title/Abstract] OR \"lacunar infarct\"[Title/Abstract] OR \"lacunar infarcts\"[Title/Abstract] OR \"silent infarct\"[Title/Abstract] OR \"silent infarcts\"[Title/Abstract] OR \"silent brain infarct\"[Title/Abstract] OR \"silent brain infarcts\"[Title/Abstract] OR \"cerebral microbleed\"[Title/Abstract] OR \"cerebral microbleeds\"[Title/Abstract] OR \"brain microbleed\"[Title/Abstract] OR \"brain microbleeds\"[Title/Abstract] OR \"microbleed*\"[Title/Abstract] OR \"vascular brain injury\"[Title/Abstract] OR \"vascular brain damage\"[Title/Abstract] OR \"subclinical brain infarct\"[Title/Abstract] OR \"subclinical brain infarcts\"[Title/Abstract]) AND 1800/01/01:2017/05/06[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "d8ac79e81213253d82be5216998fd0d448b9b32bb3ef8bbc99fc05405565c167",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The category probe ANDs the optional outcome block even though the protocol says eligible studies may omit outcomes from abstracts. That can hide relevant records from the exposure-category check."
        },
        "operators": {
          "verdict": "pass",
          "note": "The searched exposure terms are combined with OR, with no required outcome or population block. The optional outcome block was tested and left out based on the stated evidence."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the four selected MeSH descriptors. It does not provide evidence to support adding other headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The exposure block covers the named disease and MRI-marker members with text words, including white matter changes, lacunar and silent infarcts, microbleeds, and vascular brain injury."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The search and term translations report no errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, publication-date, or design filters are applied. The entry-date cutoff is identified as a harness cutoff rather than a [dp] search limit."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The SVD category probe uses a broader query that requires dementia, Alzheimer disease, or cognitive terms. Because the outcome block was left out specifically to avoid missing studies that omit outcomes from abstracts, this probe may fail to sample otherwise relevant records and does not fully validate the exposure category.",
          "recommendation": "Repeat the category probe using a broader exposure query that does not require an outcome term, then screen the resulting outside-block sample against the eligibility criteria.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The result count exceeds the stated workload budget, but the outcome block's 84.5% reduction is not established as safe: only 10 known eligible records are available, below the stated 15-record threshold. The population and follow-up concepts are designated screen-only because they are inconsistently reported. The larger screening burden is therefore an acknowledged recall-preserving risk.",
          "evidence": "The search returns 45,434 records against a 10,000-record budget. The optional outcome block reduces this to 7,030, but only 10 known eligible records were found; the 30-record loss sample had 0 relevant records."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "319811d80739e001c0c698c0fa5cfc2feba2335a9e024dd15371fed73fcbec42",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The second category probe uses a broader exposure query without requiring outcome terms and screens records outside the exposure block against eligibility, addressing R1-01."
        },
        "operators": {
          "verdict": "pass",
          "note": "The exposure terms are combined with OR, and no outcome or population block is required. The optional outcome block was tested and left out based on the stated evidence."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the four selected MeSH descriptors and provides no evidence requiring additional headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The exposure block covers the named disease and MRI-marker members, including white matter changes, lacunar and silent infarcts, microbleeds, and vascular brain injury."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported search and term translations show no errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, publication-date, or design filters are applied. The entry-date cutoff is identified as a harness cutoff rather than a [dp] search limit."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The first SVD category probe required dementia, Alzheimer disease, or cognitive terms, which could miss otherwise relevant records that omit outcomes from abstracts.",
          "recommendation": "Repeat the category probe using a broader exposure query without an outcome term, then screen records outside the exposure block against eligibility.",
          "status": "resolved",
          "response": "The second probe used an exposure query without an outcome term and screened 30 records outside the block; none were relevant."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The result count exceeds the workload budget, but the optional outcome block is not established as safe: only 10 known eligible records are available, below the stated 15-record threshold. Population and follow-up remain screen-only because they are inconsistently reported. The larger screening burden is an acknowledged recall-preserving risk.",
          "evidence": "The search returns 45,434 records against a 10,000-record budget. The outcome block reduces this to 7,030, but only 10 known eligible records were found; the 30-record loss sample had 0 relevant records."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "319811d80739e001c0c698c0fa5cfc2feba2335a9e024dd15371fed73fcbec42",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The second category probe uses an exposure query without outcome terms and screens records outside the exposure block; 0 of 30 were relevant. This resolves the earlier concern that the first probe could miss eligible records omitting outcomes from abstracts."
        },
        "operators": {
          "verdict": "pass",
          "note": "The searched exposure terms are combined with OR. No outcome or population block is required; the optional outcome block was tested and left out because its safety was not established."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the four selected MeSH descriptors and provides no evidence requiring additional headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The exposure block includes the named disease and MRI-marker members, with text words for white matter changes, lacunar and silent infarcts, microbleeds, and vascular brain injury."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported search and term translations show no errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, publication-date, or design filters are applied. The entry-date cutoff is identified as a harness cutoff rather than a [dp] search limit."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The first SVD category probe required dementia, Alzheimer disease, or cognitive terms, which could miss otherwise relevant records that omit outcomes from abstracts.",
          "recommendation": "Repeat the category probe using a broader exposure query without an outcome term, then screen records outside the exposure block against eligibility.",
          "status": "resolved",
          "response": "The second probe used an exposure query without an outcome term and screened 30 records outside the block; none were relevant."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The result count exceeds the workload budget, but the optional outcome block is not established as safe: only 10 known eligible records are available, below the stated 15-record threshold. Population and follow-up remain screen-only because they are inconsistently reported. The larger screening burden is an acknowledged recall-preserving risk.",
          "evidence": "The search returns 45,434 records against a 10,000-record budget. The outcome block reduces this to 7,030, but only 10 known eligible records were found; the 30-record loss sample had 0 relevant records."
        }
      ]
    }
  ]
}
```

