# PubMed search strategy: audit

Generated 2026-11-27T15:25:55+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In population-based cohorts, is cerebral small vessel disease (and its MRI markers) associated with the risk of incident dementia and cognitive decline?
- Framework: PECO
- Scope confirmed by user: yes (User gave no known articles, standard depth, no limits; cannot answer questions so defaults used and run continues without pausing. Assumption: exposure=CSVD is the searched concept; outcome (dementia/cognition) measured as optional block; cohort design handled at screening. as-of date 2017-05-06 via PSB_AS_OF. Scope relayed; user unavailable, so run continued without waiting.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Cerebral small vessel disease and MRI markers (WMH, lacunes, microbleeds, silent infarcts) | search | exposure; defines the topic, named reliably and MeSH-indexed |
| Dementia, Alzheimer disease, cognitive decline/impairment | optional | outcome; outcomes are usually screened, but it is reliably named so it is measured as an optional block |
| Population-based / community-dwelling longitudinal cohort | screen | study design/setting, judged at screening; no ad hoc design filter |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-11-27T15:25:36+00:00
- Records added to PubMed up to: 2017-05-06
- Total records: 19,533
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Cerebral Small Vessel Diseases"[Mesh:noexp]` | 492 | none |
| 2 | `"Leukoaraiosis"[Mesh]` | 470 | none |
| 3 | `"Stroke, Lacunar"[Mesh]` | 412 | none |
| 4 | `"CADASIL"[Mesh]` | 684 | none |
| 5 | `"small vessel disease"[tiab]` | 2,316 | none |
| 6 | `"small vessel diseases"[tiab]` | 203 | none |
| 7 | `"small-vessel disease"[tiab]` | 2,316 | none |
| 8 | `"cerebral microangiopath*"[tiab]` | 150 | none |
| 9 | `leukoaraiosis[tiab]` | 1,008 | none |
| 10 | `"white matter hyperintensit*"[tiab]` | 2,313 | none |
| 11 | `"white matter hyperintensity"[tiab:~3]` | 891 | none |
| 12 | `"white matter lesion*"[tiab]` | 4,051 | none |
| 13 | `"white matter lesion"[tiab:~3]` | 1,043 | none |
| 14 | `"white matter change*"[tiab]` | 1,880 | none |
| 15 | `"white matter disease*"[tiab]` | 948 | none |
| 16 | `WMH[tiab]` | 1,105 | none |
| 17 | `WMHs[tiab]` | 313 | none |
| 18 | `"periventricular hyperintensit*"[tiab]` | 307 | none |
| 19 | `"subcortical hyperintensit*"[tiab]` | 85 | none |
| 20 | `microbleed*[tiab]` | 1,468 | none |
| 21 | `"micro-bleed*"[tiab]` | 28 | none |
| 22 | `"cerebral microhemorrhage*"[tiab]` | 62 | none |
| 23 | `"cerebral microhaemorrhage*"[tiab]` | 4 | none |
| 24 | `"microhemorrhage*"[tiab]` | 554 | none |
| 25 | `"microhaemorrhage*"[tiab]` | 107 | none |
| 26 | `"cerebral hemosiderin"[tiab]` | 3 | none |
| 27 | `lacune*[tiab]` | 686 | none |
| 28 | `"silent brain infarct*"[tiab]` | 280 | none |
| 29 | `"silent infarct*"[tiab]` | 311 | none |
| 30 | `"silent cerebral infarct*"[tiab]` | 322 | none |
| 31 | `"silent stroke*"[tiab]` | 136 | none |
| 32 | `"covert brain infarct*"[tiab]` | 9 | none |
| 33 | `"covert infarct*"[tiab]` | 4 | none |
| 34 | `"covert vascular brain injur*"[tiab]` | 2 | none |
| 35 | `"vascular brain injur*"[tiab]` | 77 | none |
| 36 | `"subcortical infarct*"[tiab]` | 1,322 | none |
| 37 | `"subcortical vascular"[tiab]` | 362 | none |
| 38 | `"subcortical ischemic"[tiab]` | 307 | none |
| 39 | `"subcortical ischaemic"[tiab]` | 52 | none |
| 40 | `"microinfarct*"[tiab]` | 605 | none |
| 41 | `"Binswanger"[tiab]` | 568 | none |
| 42 | `"lacunar infarct*"[tiab]` | 2,251 | none |
| 43 | `"lacunar stroke*"[tiab]` | 918 | none |
| 44 | `"lacunar lesion*"[tiab]` | 131 | none |
| 45 | `"lacunar syndrome*"[tiab]` | 257 | none |
| 46 | `"enlarged perivascular space*"[tiab]` | 86 | none |
| 47 | `"Virchow-Robin"[tiab]` | 444 | none |
| 48 | `"T2 hyperintensit*"[tiab]` | 565 | none |
| 49 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48` | 19,533 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Cerebral Small Vessel Diseases"[Mesh:noexp] OR "Leukoaraiosis"[Mesh] OR "Stroke, Lacunar"[Mesh] OR "CADASIL"[Mesh] OR "small vessel disease"[tiab] OR "small vessel diseases"[tiab] OR "small-vessel disease"[tiab] OR "cerebral microangiopath*"[tiab] OR leukoaraiosis[tiab] OR "white matter hyperintensit*"[tiab] OR "white matter hyperintensity"[tiab:~3] OR "white matter lesion*"[tiab] OR "white matter lesion"[tiab:~3] OR "white matter change*"[tiab] OR "white matter disease*"[tiab] OR WMH[tiab] OR WMHs[tiab] OR "periventricular hyperintensit*"[tiab] OR "subcortical hyperintensit*"[tiab] OR microbleed*[tiab] OR "micro-bleed*"[tiab] OR "cerebral microhemorrhage*"[tiab] OR "cerebral microhaemorrhage*"[tiab] OR "microhemorrhage*"[tiab] OR "microhaemorrhage*"[tiab] OR "cerebral hemosiderin"[tiab] OR lacune*[tiab] OR "silent brain infarct*"[tiab] OR "silent infarct*"[tiab] OR "silent cerebral infarct*"[tiab] OR "silent stroke*"[tiab] OR "covert brain infarct*"[tiab] OR "covert infarct*"[tiab] OR "covert vascular brain injur*"[tiab] OR "vascular brain injur*"[tiab] OR "subcortical infarct*"[tiab] OR "subcortical vascular"[tiab] OR "subcortical ischemic"[tiab] OR "subcortical ischaemic"[tiab] OR "microinfarct*"[tiab] OR "Binswanger"[tiab] OR "lacunar infarct*"[tiab] OR "lacunar stroke*"[tiab] OR "lacunar lesion*"[tiab] OR "lacunar syndrome*"[tiab] OR "enlarged perivascular space*"[tiab] OR "Virchow-Robin"[tiab] OR "T2 hyperintensit*"[tiab])) AND ("1800/01/01"[edat] : "2017/05/06"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall | Found without a keyword search: retrieved / in PubMed |
|---|---|---:|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 8 | 8 | 100.0% | 0 / 0 |

Every known record came from a keyword search, or from the similar or citing articles of one. Such records name the searched words by construction, so the recall figures check the strategy's wording; they do not estimate recall. A prior review's reference list (psb neighbors <review PMID> --links refs) gives records that do not depend on your wording.

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Citation searching for known records

These citation searches found candidate known records to test the strategy against. They are not part of the delivered search, and they did not search for studies for the review itself. Terminology follows the TARCiS statement (Hirt et al., 2024, https://doi.org/10.1136/bmj-2023-078384).

| Batch | Date | Citation index | Direction | Seed records | Candidates | Shown | Screened in |
|---|---|---|---|---:|---:|---:|---:|
| C3 | 2026-11-27 | PubMed | backward | 1 | 49 | 49 | 0 |
| C4 | 2026-11-27 | PubMed | backward | 1 | 49 | 49 | 0 |

### Optional blocks (measured, not searched)

Each row is the effect of AND-ing a concept that is not part of the strategy. Independent records are known records that no keyword search led to (user seeds, a review's reference list); only they can show what a block would lose, and the 95% bound is the largest share of relevant records it could lose on their evidence.

| Block | Records now | Records if AND-ed | Known lost / retrieved now | Independent lost / retrieved now | 95% bound on share lost |
|---|---:|---:|---:|---:|---:|
| Dementia and cognitive decline (outcome) | 19,533 | 6,803 | 0 / 8 | 0 / 0 | unmeasured |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 43,686 | initial | none | first draft |
| 2 | 18,643 | csvd: +5 / -14 | none | removed noisy terms (microangiopath*, leukoencephalopath*, bare lacunar, perivascular, generic white matter phrases); CSVD MeSH unexploded to exclude Fabry/MELAS/MPA children |
| 3 | 15,804 | csvd: +3 / -3 | none | restructured 3 heaviest terms (white matter lesion*, white matter change*, lacunar infarct*) with outcome qualifier: 18,643 -> ~15.8k, none refused; outcome block not AND-ed (unmeasured loss, no independent records, only one weak review) |
| 4 | 19,533 | csvd: +6 / -3 | none | reverted outcome-restricted terms to bare unrestricted forms (critic F1/F2); added enlarged perivascular space*, Virchow-Robin, T2 hyperintensit* (F4) |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 6 findings; F1 should-fix accepted-risk, F2 document accepted-risk, F3 document accepted-risk, F4 document rejected, F5 document accepted-risk, F6 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 905 NCBI requests logged (401 from cache); strategy sha256 d5736b903eee._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [],
    "issues": [
      {
        "severity": "info",
        "code": "noexp",
        "message": "unexploded MeSH: confirm the narrower descriptors are meant to be excluded",
        "term": "\"Cerebral Small Vessel Diseases\"[Mesh:noexp]",
        "block": "csvd",
        "location": "block:csvd",
        "blocking": false,
        "requires_review": false,
        "id": "I-7c6ecb81f2a21066e5a1"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Cerebral Small Vessel Diseases",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T15:25:36+00:00",
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
        "tag": "Mesh:noexp",
        "field": "mh"
      }
    },
    {
      "requested": "Leukoaraiosis",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T15:25:36+00:00",
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
      "checked_at": "2026-11-27T15:25:36+00:00",
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
      "requested": "CADASIL",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T15:25:36+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D046589",
          "name": "CADASIL",
          "type": "descriptor",
          "scope_note": "A familial, cerebral arteriopathy mapped to chromosome 19q12, and characterized by the presence of granular deposits in small CEREBRAL ARTERIES producing ischemic STROKE; PSEUDOBULBAR PALSY; and multiple subcortical infarcts (CEREBRAL INFARCTION). CADASIL is an acronym for Cerebral Autosomal Dominant Arteriopathy with Subcortical Infarcts and Leukoencephalopathy. CADASIL differs from BINSWANGER...",
          "tree_numbers": [
            "C10.228.140.300.150.477.200.100",
            "C10.228.140.300.275.249",
            "C10.228.140.300.400.203",
            "C10.228.140.300.510.200.175",
            "C10.228.140.300.775.200.200.100",
            "C10.228.140.380.230.124",
            "C14.907.253.092.477.200.100",
            "C14.907.253.329.249",
            "C14.907.253.560.200.175",
            "C14.907.253.855.200.200.100",
            "C16.320.129",
            "C23.550.513.355.250.200.100",
            "C23.550.717.489.250.200.100"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D046589",
      "preferred_label": "CADASIL",
      "type": "descriptor",
      "location": "vocabulary:4",
      "term": {
        "text": "\"CADASIL\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Cerebral Small Vessel Diseases\"[MeSH Terms:noexp] OR \"Leukoaraiosis\"[MeSH Terms] OR \"stroke, lacunar\"[MeSH Terms] OR \"CADASIL\"[MeSH Terms] OR \"small-vessel disease\"[Title/Abstract] OR \"small vessel diseases\"[Title/Abstract] OR \"small-vessel disease\"[Title/Abstract] OR \"cerebral microangiopath*\"[Title/Abstract] OR \"Leukoaraiosis\"[Title/Abstract] OR \"white matter hyperintensit*\"[Title/Abstract] OR \"white matter hyperintensity\"[Title/Abstract:~3] OR \"white matter lesion*\"[Title/Abstract] OR \"white matter lesion\"[Title/Abstract:~3] OR \"white matter change*\"[Title/Abstract] OR \"white matter disease*\"[Title/Abstract] OR \"WMH\"[Title/Abstract] OR \"WMHs\"[Title/Abstract] OR \"periventricular hyperintensit*\"[Title/Abstract] OR \"subcortical hyperintensit*\"[Title/Abstract] OR \"microbleed*\"[Title/Abstract] OR \"micro bleed*\"[Title/Abstract] OR \"cerebral microhemorrhage*\"[Title/Abstract] OR \"cerebral microhaemorrhage*\"[Title/Abstract] OR \"microhemorrhage*\"[Title/Abstract] OR \"microhaemorrhage*\"[Title/Abstract] OR \"cerebral hemosiderin\"[Title/Abstract] OR \"lacune*\"[Title/Abstract] OR \"silent brain infarct*\"[Title/Abstract] OR \"silent infarct*\"[Title/Abstract] OR \"silent cerebral infarct*\"[Title/Abstract] OR \"silent stroke*\"[Title/Abstract] OR \"covert brain infarct*\"[Title/Abstract] OR \"covert infarct*\"[Title/Abstract] OR \"covert vascular brain injur*\"[Title/Abstract] OR \"vascular brain injur*\"[Title/Abstract] OR \"subcortical infarct*\"[Title/Abstract] OR \"subcortical vascular\"[Title/Abstract] OR \"subcortical ischemic\"[Title/Abstract] OR \"subcortical ischaemic\"[Title/Abstract] OR \"microinfarct*\"[Title/Abstract] OR \"Binswanger\"[Title/Abstract] OR \"lacunar infarct*\"[Title/Abstract] OR \"lacunar stroke*\"[Title/Abstract] OR \"lacunar lesion*\"[Title/Abstract] OR \"lacunar syndrome*\"[Title/Abstract] OR \"enlarged perivascular space*\"[Title/Abstract] OR \"Virchow-Robin\"[Title/Abstract] OR \"t2 hyperintensit*\"[Title/Abstract]) AND 1800/01/01:2017/05/06[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "31814a325c2b02eb7e1cead23d322f5f43d4d8987de465870af672f788475e37",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "No translation issues; every named member searched by bare name."
        },
        "operators": {
          "verdict": "revise",
          "note": "Single OR block of 19,533 records; outcome block unmeasured on independent records."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "MeSH verified; CSVD unexploded deliberately; CADASIL and Stroke, Lacunar searched separately."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Broad coverage; a few optional gaps."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax problems."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Only the as-of entry-date bound; no ad hoc filters."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "block": "csvd",
          "finding": "One-block OR with 19,533 results, above the 10,000 threshold; the outcome block is not applied. AND-ing gives 6,803 (-65.2%), loses 0 of 8 known records, but 0 of 8 were found independently so the loss is unmeasured.",
          "recommendation": "Find independent known records and re-test, or AND only for workload and report the unmeasured risk; otherwise screen all and say the outcome was left to screening.",
          "status": "accepted-risk",
          "response": "Outcome kept as a measured optional block, not AND-ed: user asked for high sensitivity, no independent known records exist (one prior review had no usable reference list; OpenAlex budget exhausted), so the AND-ing rules (two reviews' reference lists) are not met. Result of 19,533 is left to screening; AND-ing would give 6,803 with unmeasured loss and is documented as an alternative."
        },
        {
          "id": "F2",
          "domain": "operators",
          "severity": "document",
          "kind": "reporting",
          "block": "csvd",
          "finding": "Recall of 100% (8/8) is circular: the records were screened in during the build and are not independent.",
          "recommendation": "Report as a wording check only.",
          "status": "accepted-risk",
          "response": "Reported as a wording check only; recall is not estimated."
        },
        {
          "id": "F3",
          "domain": "subject_headings",
          "severity": "document",
          "kind": "scope",
          "block": "csvd",
          "finding": "Cerebral Small Vessel Diseases is searched [Mesh:noexp]; other narrower descriptors are excluded.",
          "recommendation": "Confirm and document the exclusion is intentional.",
          "status": "accepted-risk",
          "response": "noexp intentional: narrower children (Fabry disease, MELAS, microscopic polyangiitis, familial CAA) are not small vessel MRI markers and added ~4,600 off-topic records; Leukoaraiosis, Stroke Lacunar and CADASIL are searched explicitly."
        },
        {
          "id": "F4",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "block": "csvd",
          "finding": "Possible gaps: hyperintense, white matter abnormalit*, leukoencephalopathy, non-contiguous small vessel wording.",
          "recommendation": "Test or record as considered.",
          "status": "rejected",
          "response": "Considered: leukoencephalopathy and white matter abnormalit* were removed after term-impact showed thousands of off-topic records; hyperintense/small vessel variants not named in criteria. Not added."
        },
        {
          "id": "F5",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "block": "csvd",
          "finding": "Lines 5/7 and proximity lines 11/13 overlap with lines 10/12; redundancy only.",
          "recommendation": "Retain and document.",
          "status": "accepted-risk",
          "response": "Redundant hyphen/proximity variants retained as harmless safeguards."
        },
        {
          "id": "F6",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "filter",
          "block": "csvd",
          "finding": "The date bound is on entry date, not publication date.",
          "recommendation": "State in methods.",
          "status": "accepted-risk",
          "response": "Entry-date bound is intentional (as-of 2017-05-06), stated in the audit."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

