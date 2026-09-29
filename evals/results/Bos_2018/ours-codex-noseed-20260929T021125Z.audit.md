# PubMed search strategy: audit

Generated 2026-09-29T02:47:38+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In population-based cohorts, is cerebral small vessel disease (and its MRI markers) associated with the risk of incident dementia and cognitive decline?
- Framework: PECO
- Scope confirmed by user: yes (Scope decisions are provisional assumptions because the user requested no questions during this run. No known relevant articles were supplied. Work is evaluated against PubMed records present by 2017-05-06 using PSB_AS_OF; no publication-date limit is applied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Cerebral small vessel disease and MRI markers | search | The exposure defines the review and relevant studies name the disease or an individual imaging marker; members include white matter hyperintensity, lacunar/silent infarction, cerebral microbleed, and vascular brain injury. |
| Dementia and cognitive outcomes | optional | Outcomes define the topic and are searchable, but outcome terms may be absent from titles/abstracts of otherwise eligible exposure cohorts; test before deciding whether to AND. |
| Population-based community-dwelling cohort | optional | Population-based or community-based setting is topic-defining and searchable but may not be named consistently; test this block as optional and screen setting eligibility. |
| Prospective/longitudinal observational follow-up | optional | Cohort and follow-up labels are searchable and may reduce screening, but design reporting is inconsistent; test the block as optional and screen prospective longitudinal eligibility. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T02:46:45+00:00
- Records added to PubMed up to: 2017-05-06
- Total records: 384,953
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Cerebral Small Vessel Diseases[Mesh]` | 6,257 | none |
| 2 | `Cerebrovascular Disorders[Mesh]` | 329,326 | none |
| 3 | `Brain Infarction[Mesh]` | 34,827 | none |
| 4 | `Stroke, Lacunar[Mesh]` | 412 | none |
| 5 | `Cerebral Hemorrhage[Mesh]` | 31,304 | none |
| 6 | `Microvessels[Mesh]` | 47,087 | none |
| 7 | `cerebral small vessel disease[tiab]` | 813 | none |
| 8 | `small vessel disease[tiab]` | 2,316 | none |
| 9 | `small-vessel disease[tiab]` | 2,316 | none |
| 10 | `cerebral microangiopath*[tiab]` | 150 | none |
| 11 | `cerebral small vessel ischem*[tiab]` | 6 | none |
| 12 | `CSVD[tiab]` | 127 | none |
| 13 | `leukoaraiosis[tiab]` | 1,008 | none |
| 14 | `white matter hyperintens*[tiab]` | 2,354 | none |
| 15 | `white matter lesion*[tiab]` | 4,051 | none |
| 16 | `white matter change*[tiab]` | 1,880 | none |
| 17 | `white matter abnormalit*[tiab]` | 1,590 | none |
| 18 | `WMH[tiab]` | 1,105 | none |
| 19 | `silent brain infarct*[tiab]` | 280 | none |
| 20 | `silent infarct*[tiab]` | 311 | none |
| 21 | `silent cerebral infarct*[tiab]` | 322 | none |
| 22 | `lacunar infarct*[tiab]` | 2,251 | none |
| 23 | `lacunar stroke[tiab]` | 750 | none |
| 24 | `lacune*[tiab]` | 686 | none |
| 25 | `cerebral microbleed*[tiab]` | 710 | none |
| 26 | `brain microbleed*[tiab]` | 59 | none |
| 27 | `microbleed*[tiab]` | 1,468 | none |
| 28 | `microhemorrhag*[tiab]` | 578 | none |
| 29 | `vascular brain injur*[tiab]` | 77 | none |
| 30 | `vascular brain disease[tiab]` | 36 | none |
| 31 | `white matter hyperintensit*[tiab]` | 2,313 | none |
| 32 | `perivascular space*[tiab]` | 1,613 | none |
| 33 | `enlarged perivascular space*[tiab]` | 86 | none |
| 34 | `Virchow-Robin space*[tiab]` | 410 | none |
| 35 | `subcortical infarct*[tiab]` | 1,322 | none |
| 36 | `subcortical white matter lesion*[tiab]` | 165 | none |
| 37 | `white matter signal abnormalit*[tiab]` | 78 | none |
| 38 | `vascular white matter lesion*[tiab]` | 6 | none |
| 39 | `cerebral microinfarct*[tiab]` | 43 | none |
| 40 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39` | 384,953 | none |

### Strategy (single line, for copying into PubMed)

```text
((Cerebral Small Vessel Diseases[Mesh] OR Cerebrovascular Disorders[Mesh] OR Brain Infarction[Mesh] OR Stroke, Lacunar[Mesh] OR Cerebral Hemorrhage[Mesh] OR Microvessels[Mesh] OR cerebral small vessel disease[tiab] OR small vessel disease[tiab] OR small-vessel disease[tiab] OR cerebral microangiopath*[tiab] OR cerebral small vessel ischem*[tiab] OR CSVD[tiab] OR leukoaraiosis[tiab] OR white matter hyperintens*[tiab] OR white matter lesion*[tiab] OR white matter change*[tiab] OR white matter abnormalit*[tiab] OR WMH[tiab] OR silent brain infarct*[tiab] OR silent infarct*[tiab] OR silent cerebral infarct*[tiab] OR lacunar infarct*[tiab] OR lacunar stroke[tiab] OR lacune*[tiab] OR cerebral microbleed*[tiab] OR brain microbleed*[tiab] OR microbleed*[tiab] OR microhemorrhag*[tiab] OR vascular brain injur*[tiab] OR vascular brain disease[tiab] OR white matter hyperintensit*[tiab] OR perivascular space*[tiab] OR enlarged perivascular space*[tiab] OR Virchow-Robin space*[tiab] OR subcortical infarct*[tiab] OR subcortical white matter lesion*[tiab] OR white matter signal abnormalit*[tiab] OR vascular white matter lesion*[tiab] OR cerebral microinfarct*[tiab])) AND ("1800/01/01"[edat] : "2017/05/06"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 9 | 9 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Dementia and cognitive outcomes | left out | 384,953 / 28,321 | 92.6% | none | 0/30 (up to 10% of removed records could be relevant) | Nine externally benchmarked eligible studies are below the required 15-record threshold for ANDing. The outcome block removes most base-query records; the refreshed random loss sample of 30 titles was unrelated, but this small review-derived set cannot establish safe outcome capture. Leave it out to preserve recall and screen outcomes. |
| Population-based community-dwelling cohort | left out | 384,953 / 7,599 | 98.0% | 15883315, 18195145, 18635849 | 0/30 (up to 10% of removed records could be relevant) | Nine externally benchmarked eligible studies are below the required 15-record threshold for ANDing. The population-setting block loses known eligible studies in the benchmark and setting language is inconsistently indexed or reported. Leave it out and screen for community/population setting. |
| Prospective/longitudinal observational follow-up | left out | 384,953 / 76,023 | 80.3% | none | 0/30 (up to 10% of removed records could be relevant) | Nine externally benchmarked eligible studies are below the required 15-record threshold for ANDing. The design block materially reduces the base query and these nine records are too few to establish safe capture. Leave it out and screen for prospective longitudinal follow-up. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Cerebral small vessel disease and MRI markers | 1 | `Magnetic Resonance Imaging[Mesh] OR MRI[tiab] OR neuroimaging[tiab] OR brain imaging[tiab]` | 424,297 | not screened |
| Cerebral small vessel disease and MRI markers | 2 | `Magnetic Resonance Imaging[Mesh] OR MRI[tiab] OR neuroimaging[tiab] OR brain imaging[tiab]` | 424,297 | 0/30 |
| Dementia and cognitive outcomes | 1 | `executive function[tiab] OR processing speed[tiab] OR memory[tiab] OR Mini-Mental[tiab] OR neuropsycholog*[tiab]` | 173 | 0/30 |
| Dementia and cognitive outcomes | 2 | `executive function[tiab] OR processing speed[tiab] OR memory[tiab] OR Mini-Mental[tiab] OR neuropsycholog*[tiab]` | 175 | 0/30 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 383,344 | initial | none | Initial PECO strategy: broad exposure/MRI-marker block with a separately measured optional dementia/cognition outcome block; no population or design filter. |
| 2 | 384,953 | svd: +8 / -0 | none | Expanded the exposure category with perivascular-space, subcortical infarct/lesion, white matter signal abnormality, and microinfarct terminology to cover additional named MRI markers; remeasure optional outcome decision after the query change. |
| 3 | 384,953 | limits/combination | none | Following the first critic, tested searchable population/community-setting and prospective/cohort-follow-up concepts as optional blocks. The topic outcomes block remains optional. These are measurement candidates only; none is ANDed pending loss tests and the known-record threshold. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 3 findings; R1-LF-01 must-fix rejected, R1-SH-01 should-fix open, R1-LF-02 should-fix open
- Round 2 on version 3: 3 findings; R1-LF-01 must-fix rejected, R1-SH-01 should-fix accepted-risk, R1-LF-02 should-fix resolved
- Round 3 on version 3: 3 findings; R1-LF-01 must-fix rejected, R1-SH-01 should-fix accepted-risk, R1-LF-02 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1879 NCBI requests logged (1028 from cache); strategy sha256 7c9ef5da471b._

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
        "message": "384,953 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "384,953 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-29T02:46:45+00:00",
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
      "requested": "Cerebrovascular Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:46:45+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D002561",
          "name": "Cerebrovascular Disorders",
          "type": "descriptor",
          "scope_note": "A spectrum of pathological conditions of impaired blood flow in the brain. They can involve vessels (ARTERIES or VEINS) in the CEREBRUM, the CEREBELLUM, and the BRAIN STEM. Major categories include INTRACRANIAL ARTERIOVENOUS MALFORMATIONS; BRAIN ISCHEMIA; CEREBRAL HEMORRHAGE; and others.",
          "tree_numbers": [
            "C10.228.140.300",
            "C14.907.253"
          ],
          "entry_terms": 25,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D002561",
      "preferred_label": "Cerebrovascular Disorders",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "Cerebrovascular Disorders",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Brain Infarction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:46:45+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D020520",
          "name": "Brain Infarction",
          "type": "descriptor",
          "scope_note": "Tissue NECROSIS in any area of the brain, including the CEREBRAL HEMISPHERES, the CEREBELLUM, and the BRAIN STEM. Brain infarction is the result of a cascade of events initiated by inadequate blood flow through the brain that is followed by HYPOXIA and HYPOGLYCEMIA in brain tissue. Damage may be temporary, permanent, selective or pan-necrosis.",
          "tree_numbers": [
            "C10.228.140.300.150.477",
            "C10.228.140.300.775.200",
            "C14.907.253.092.477",
            "C14.907.253.855.200",
            "C23.550.513.355.250",
            "C23.550.717.489.250"
          ],
          "entry_terms": 31,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D020520",
      "preferred_label": "Brain Infarction",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "Brain Infarction",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stroke, Lacunar",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:46:45+00:00",
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
      "location": "vocabulary:4",
      "term": {
        "text": "Stroke, Lacunar",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cerebral Hemorrhage",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:46:45+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D002543",
          "name": "Cerebral Hemorrhage",
          "type": "descriptor",
          "scope_note": "Bleeding into one or both CEREBRAL HEMISPHERES including the BASAL GANGLIA and the CEREBRAL CORTEX. It is often associated with HYPERTENSION and CRANIOCEREBRAL TRAUMA.",
          "tree_numbers": [
            "C10.228.140.300.535.200",
            "C14.907.253.573.200",
            "C23.550.414.913.100"
          ],
          "entry_terms": 23,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D002543",
      "preferred_label": "Cerebral Hemorrhage",
      "type": "descriptor",
      "location": "vocabulary:5",
      "term": {
        "text": "Cerebral Hemorrhage",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Microvessels",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:46:45+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D055806",
          "name": "Microvessels",
          "type": "descriptor",
          "scope_note": "The finer blood vessels of the vasculature that are generally less than 100 microns in internal diameter.",
          "tree_numbers": [
            "A07.015.461"
          ],
          "entry_terms": 6,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D055806",
      "preferred_label": "Microvessels",
      "type": "descriptor",
      "location": "vocabulary:6",
      "term": {
        "text": "Microvessels",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"cerebral small vessel diseases\"[MeSH Terms] OR \"cerebrovascular disorders\"[MeSH Terms] OR \"brain infarction\"[MeSH Terms] OR \"stroke, lacunar\"[MeSH Terms] OR \"cerebral hemorrhage\"[MeSH Terms] OR \"microvessels\"[MeSH Terms] OR \"cerebral small vessel disease\"[Title/Abstract] OR \"small vessel disease\"[Title/Abstract] OR \"small vessel disease\"[Title/Abstract] OR \"cerebral microangiopath*\"[Title/Abstract] OR \"cerebral small vessel ischem*\"[Title/Abstract] OR \"CSVD\"[Title/Abstract] OR \"leukoaraiosis\"[Title/Abstract] OR \"white matter hyperintens*\"[Title/Abstract] OR \"white matter lesion*\"[Title/Abstract] OR \"white matter change*\"[Title/Abstract] OR \"white matter abnormalit*\"[Title/Abstract] OR \"WMH\"[Title/Abstract] OR \"silent brain infarct*\"[Title/Abstract] OR \"silent infarct*\"[Title/Abstract] OR \"silent cerebral infarct*\"[Title/Abstract] OR \"lacunar infarct*\"[Title/Abstract] OR \"lacunar stroke\"[Title/Abstract] OR \"lacune*\"[Title/Abstract] OR \"cerebral microbleed*\"[Title/Abstract] OR \"brain microbleed*\"[Title/Abstract] OR \"microbleed*\"[Title/Abstract] OR \"microhemorrhag*\"[Title/Abstract] OR \"vascular brain injur*\"[Title/Abstract] OR \"vascular brain disease\"[Title/Abstract] OR \"white matter hyperintensit*\"[Title/Abstract] OR \"perivascular space*\"[Title/Abstract] OR \"enlarged perivascular space*\"[Title/Abstract] OR \"virchow robin space*\"[Title/Abstract] OR \"subcortical infarct*\"[Title/Abstract] OR \"subcortical white matter lesion*\"[Title/Abstract] OR \"white matter signal abnormalit*\"[Title/Abstract] OR \"vascular white matter lesion*\"[Title/Abstract] OR \"cerebral microinfarct*\"[Title/Abstract]) AND 1800/01/01:2017/05/06[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "043e0a3d0eca8a1ec142f244a8d62a7c36f39fc830a2c3399922775a4300574e",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The eligibility named markers have their own text-word coverage, including white matter hyperintensity, lacunar and silent infarction, cerebral microbleed, and vascular brain injury."
        },
        "operators": {
          "verdict": "pass",
          "note": "The exposure terms are ORed within one block and combined with the date range using AND; the optional outcome block is left out."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "Several verified headings are much broader than the exposure, especially Cerebrovascular Disorders and Microvessels. Their inclusion needs a scope and retrieval rationale."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The named exposure markers are represented by explicit text words. No unsupported outcome block is required because the outcome concept was tested and left out."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query has balanced grouping and no reported PubMed syntax diagnostics. No proximity operators or phrase warnings require interpretation."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The displayed query includes an EDAT cutoff of 2017-05-06. The packet says no publication-date limit is intended, but this entry-date bound excludes records entered later. The 10,000-record workload warning remains because population and design concepts were not tested as optional blocks."
        }
      },
      "findings": [
        {
          "id": "R1-LF-01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The displayed query is restricted to records entered in PubMed by 2017-05-06. That bound excludes records added after the cutoff, despite the stated absence of a publication-date limit.",
          "recommendation": "For a current review search, remove the EDAT upper bound. If this is only a historical evaluation snapshot, label it clearly and provide the unbounded query for use.",
          "status": "rejected",
          "response": "The user-facing review protocol has no publication-date eligibility limit, but this run is explicitly required to evaluate PubMed as of 2017-05-06 and the harness requires PSB_AS_OF on every command. The generated EDAT restriction enforces that historical database snapshot; it is not a [dp] restriction. An unbounded query would violate the run conditions and would not be the validated deliverable."
        },
        {
          "id": "R1-SH-01",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The verified headings Cerebrovascular Disorders and Microvessels cover broad subject areas beyond cerebral small vessel disease and its MRI markers; Cerebral Hemorrhage is also broader than the named exposure.",
          "recommendation": "Document the intended retrieval contribution of each broad heading or test its contribution against the exposure scope before retaining it. Re-evaluate the full query after any change.",
          "status": "open",
          "response": ""
        },
        {
          "id": "R1-LF-02",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The query returns 384,953 records against a 10,000-record workload budget. The outcome block was tested and left out, but the searchable population and longitudinal-design concepts marked for screening were not tested as optional blocks.",
          "recommendation": "Test optional population and design blocks with loss samples, or document why they should remain screening criteria despite the workload. Re-evaluate the full query after any change.",
          "status": "open",
          "response": ""
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "rejected",
          "response": "At this evaluation, the outcome concept had been tested but the searchable population and cohort/follow-up concepts had not yet been tested as optional blocks. The workload disposition therefore remains unresolved pending those tests.",
          "evidence": "The base count was 384,953 against a 10,000-record budget; outcome reduced it by 92.6% with 0/30 sampled relevant, and six benchmark studies were in the base query. Population and design optional tests had not been run in this bound review."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "ba478cf29c10c13032383ebcdcab4febe7d1e22e48170aa74b0b4419be30abb7",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The eligibility-named exposure markers have text-word coverage, including white matter hyperintensity, lacunar and silent infarction, cerebral microbleed, and vascular brain injury. No process-direction terms are involved."
        },
        "operators": {
          "verdict": "pass",
          "note": "Exposure terms are ORed in one block. Outcome, population, and design blocks were tested and left out with documented recall rationale."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Broad-heading contribution was separately checked: Cerebrovascular Disorders contributes 256,108 records beyond other exposure terms; Microvessels contributes 45,292 and a 10-record recent-title sample was unrelated. Cerebral Hemorrhage could not be reliably counted because PubMed returned a no-items diagnostic for the complex exclusion query. These broad routes remain a documented noise risk; the markers also have explicit text words."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The named exposure markers are represented by explicit text words. Outcome terms were tested as an optional block and left out to preserve recall."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint or PubMed syntax diagnostics. The exposure terms are grouped with OR; no phrase or proximity warnings require interpretation."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Population and longitudinal-design concepts were tested as optional blocks. The final count remains above budget, but every searchable screening concept was considered. EDAT implements the required 2017-05-06 PubMed snapshot, not a publication-date eligibility limit."
        }
      },
      "findings": [
        {
          "id": "R1-LF-01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The displayed query is restricted to records entered in PubMed by 2017-05-06, despite no publication-date eligibility limit.",
          "recommendation": "For a current review search, remove the EDAT upper bound; for this historical snapshot evaluation, label the bound as such.",
          "status": "rejected",
          "response": "The packet specifies evaluation of PubMed as of 2017-05-06 using PSB_AS_OF on every command. The EDAT bound implements that required historical snapshot and is not a publication-date eligibility restriction."
        },
        {
          "id": "R1-SH-01",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The verified headings Cerebrovascular Disorders and Microvessels cover broad subject areas beyond cerebral small vessel disease and its MRI markers; Cerebral Hemorrhage is also broader than the named exposure.",
          "recommendation": "Document the intended retrieval contribution of each broad heading or test its contribution against the exposure scope before retaining it. Re-evaluate the full query after any change.",
          "status": "accepted-risk",
          "response": "The heading-specific checks show substantial noise: Cerebrovascular Disorders retrieved 256,108 records exclusive of all other exposure terms; Microvessels retrieved 45,292 exclusive records, and the 10-record sample was unrelated to the review. Brain Infarction had zero exclusive records because its results overlap other exposure terms. A Cerebral Hemorrhage exclusive query returned a PubMed no-items diagnostic, so its contribution could not be estimated reliably. I retained Cerebrovascular Disorders because it is the historical parent used for records before the 2012 Cerebral Small Vessel Diseases descriptor and appears on eligible benchmark records; Brain Infarction and Cerebral Hemorrhage retain plausible indexing routes for infarct and hemorrhagic markers. Microvessels is the least specific; it remains as a broad route for small-vessel indexing, with substantial noise acknowledged. Exact text-word marker terms independently cover the named exposures. A reviewer may remove a broad heading if precision is preferred, but this strategy prioritizes recall."
        },
        {
          "id": "R1-LF-02",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The query exceeds the 10,000-record workload budget.",
          "recommendation": "Test searchable concepts used only for screening as optional blocks and document whether any can be safely ANDed.",
          "status": "resolved",
          "response": "The outcome, population, and design blocks were all tested. The outcome block reduces results by 92.6%; the population block by 98.0% and loses three known eligible benchmark records; the design block by 80.3%. Given those losses and the small nine-study benchmark, the packet leaves the blocks out to preserve recall and screens those criteria."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The final query remains above the workload budget, but every searchable concept identified for screening was tested as an optional block. The documented reductions and benchmark losses do not establish that ANDing any block is safe, so the blocks remain screening criteria.",
          "evidence": "The base query returns 384,953 records against a 10,000-record budget. Outcome reduces it to 28,321 (92.6%); population to 7,599 (98.0%) while losing benchmark PMIDs 15883315, 18195145, and 18635849; design to 76,023 (80.3%). Each test has only nine benchmark studies, below the stated 15-record threshold for ANDing."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "ba478cf29c10c13032383ebcdcab4febe7d1e22e48170aa74b0b4419be30abb7",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The eligibility-named exposure markers have explicit text-word coverage, including white matter hyperintensity, lacunar and silent infarction, cerebral microbleed, and vascular brain injury."
        },
        "operators": {
          "verdict": "pass",
          "note": "Exposure terms are ORed in one block. Outcome, population, and design blocks were tested and left out with documented recall rationale."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The broad-heading concern is addressed as an accepted recall-versus-noise risk: the packet documents each heading's contribution or its measurement limitation, and the named markers have independent text-word coverage."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The named exposure markers have explicit text-word coverage. Optional outcome terms were tested and left out to preserve recall."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint or PubMed syntax diagnostics. No phrase or proximity warnings require interpretation."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Population and design blocks were tested alongside the outcome block. The strategy remains above the workload budget, with reductions, benchmark losses, and reasons for leaving blocks out documented. EDAT implements the required 2017-05-06 snapshot."
        }
      },
      "findings": [
        {
          "id": "R1-LF-01",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query is restricted to records entered in PubMed by 2017-05-06, despite no publication-date eligibility limit.",
          "recommendation": "For a current review search, remove the EDAT upper bound; for this historical snapshot evaluation, label the bound as such.",
          "status": "rejected",
          "response": "The packet requires evaluation of PubMed as of 2017-05-06 using PSB_AS_OF on every command. EDAT implements that historical database snapshot and is not a publication-date eligibility restriction."
        },
        {
          "id": "R1-SH-01",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Cerebrovascular Disorders, Microvessels, and Cerebral Hemorrhage cover areas broader than the named exposure.",
          "recommendation": "Document the intended retrieval contribution of each broad heading or test its contribution against the exposure scope before retaining it.",
          "status": "accepted-risk",
          "response": "The packet documents substantial noise for Cerebrovascular Disorders and Microvessels, a 10-record unrelated sample for Microvessels, and a failed PubMed exclusion query that prevented reliable estimation for Cerebral Hemorrhage. Cerebrovascular Disorders is retained as a historical parent heading; Brain Infarction and Cerebral Hemorrhage as plausible marker-indexing routes; and Microvessels as a broad small-vessel route. Exact text-word marker terms independently cover the named exposures, and the strategy prioritizes recall."
        },
        {
          "id": "R1-LF-02",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The query exceeds the 10,000-record workload budget.",
          "recommendation": "Test searchable concepts used only for screening as optional blocks and document whether any can be safely ANDed.",
          "status": "resolved",
          "response": "Outcome, population, and design blocks were all tested. Their reductions and loss samples are documented; the population block loses three known eligible benchmark records, and the nine-study benchmark is below the stated 15-record threshold for ANDing. The blocks remain screening criteria to preserve recall."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The final query remains above the workload budget, but each searchable screening concept was tested as an optional block. The documented results do not establish that ANDing any block is safe, so the blocks remain screening criteria.",
          "evidence": "The base query returns 384,953 records against a 10,000-record budget. Outcome reduces results to 28,321 (92.6%); population to 7,599 (98.0%) while losing benchmark PMIDs 15883315, 18195145, and 18635849; design to 76,023 (80.3%). The benchmark has nine studies, below the stated 15-record threshold for ANDing."
        }
      ]
    }
  ]
}
```

