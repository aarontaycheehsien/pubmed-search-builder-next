# PubMed search strategy: audit

Generated 2026-09-29T20:15:56+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In population-based cohorts, is cerebral small vessel disease (and its MRI markers) associated with the risk of incident dementia and cognitive decline?
- Framework: PECO
- Scope confirmed by user: no (User asked not to be questioned during this run. Scope proceeded on the supplied criteria: required exposure block; outcome and cohort setting/design treated as optional and to be tested. Cutoff is the PubMed Entrez record date 2017-05-06 via PSB_AS_OF; no publication-date limit. No known relevant articles were supplied. To find validation records, screened references of PubMed review PMID 25899293 (identified by a broad exposure-and-outcome pilot search); screened citation-neighbour candidates for that review and for cohort PMID 28468844; ran pilot samples and category probes. The cohort-context probe found Austrian Stroke Prevention Study PMID 11901238. Eleven eligible records were screened; eight development and three held-out validation records were split from these, so validation is semi-independent rather than external. MeSH checks: lookup for white matter lesions returned no descriptor; white matter hyperintensity mapped only to White Matter (anatomical) and broad Leukoencephalopathies, neither specific to SVD lesions. Lookup for microbleeds and cerebral microhemorrhage returned no descriptor; Cerebral Hemorrhage is too broad to represent microbleeds and was not added. Brain Infarction was added as a broader indexed heading; its narrower terms include Stroke, Lacunar.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Cerebral small vessel disease and MRI markers | search | The exposure is required; records may name individual MRI-marker members without the umbrella term, so member headings and terms must be probed. |
| Incident dementia, Alzheimer disease, cognitive decline or impairment | optional | Topic-defining outcomes may reduce a broad exposure search, but outcomes can be inconsistently named; test before deciding whether to AND. |
| Population-based or community-dwelling cohort setting | optional | Community and population-based cohorts are searchable setting labels, but studies may use cohort names without those labels; test before deciding whether to AND. |
| Prospective or longitudinal observational cohort follow-up | optional | Recognisable design and follow-up labels may lower screening burden, but design labels are not reliable enough to require without empirical testing. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T20:15:20+00:00
- Records added to PubMed up to: 2017-05-06
- Total records: 52,262
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Cerebral Small Vessel Diseases"[Mesh]` | 6,257 | none |
| 2 | `"Leukoaraiosis"[Mesh]` | 470 | none |
| 3 | `"Stroke, Lacunar"[Mesh]` | 412 | none |
| 4 | `"Brain Infarction"[Mesh]` | 34,827 | none |
| 5 | `"cerebral small vessel disease"[tiab]` | 813 | none |
| 6 | `"cerebral small vessel diseases"[tiab]` | 105 | none |
| 7 | `"small vessel disease"[tiab]` | 2,316 | none |
| 8 | `"small vessel diseases"[tiab]` | 203 | none |
| 9 | `cerebral microangiopath*[tiab]` | 150 | none |
| 10 | `leukoaraiosis[tiab]` | 1,008 | none |
| 11 | `"white matter hyperintens*"[tiab]` | 2,354 | none |
| 12 | `"white matter lesion*"[tiab]` | 4,051 | none |
| 13 | `"white matter change*"[tiab]` | 1,880 | none |
| 14 | `"white matter abnormalit*"[tiab]` | 1,590 | none |
| 15 | `"lacunar infarct*"[tiab]` | 2,251 | none |
| 16 | `lacune*[tiab]` | 686 | none |
| 17 | `"silent brain infarct*"[tiab]` | 280 | none |
| 18 | `"silent cerebral infarct*"[tiab]` | 322 | none |
| 19 | `"silent infarct*"[tiab]` | 311 | none |
| 20 | `"covert brain infarct*"[tiab]` | 9 | none |
| 21 | `microbleed*[tiab]` | 1,468 | none |
| 22 | `microhemorrhag*[tiab]` | 578 | none |
| 23 | `microhaemorrhag*[tiab]` | 113 | none |
| 24 | `"vascular brain injury"[tiab]` | 73 | none |
| 25 | `"vascular brain injur*"[tiab]` | 77 | none |
| 26 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25` | 52,262 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Cerebral Small Vessel Diseases"[Mesh] OR "Leukoaraiosis"[Mesh] OR "Stroke, Lacunar"[Mesh] OR "Brain Infarction"[Mesh] OR "cerebral small vessel disease"[tiab] OR "cerebral small vessel diseases"[tiab] OR "small vessel disease"[tiab] OR "small vessel diseases"[tiab] OR cerebral microangiopath*[tiab] OR leukoaraiosis[tiab] OR "white matter hyperintens*"[tiab] OR "white matter lesion*"[tiab] OR "white matter change*"[tiab] OR "white matter abnormalit*"[tiab] OR "lacunar infarct*"[tiab] OR lacune*[tiab] OR "silent brain infarct*"[tiab] OR "silent cerebral infarct*"[tiab] OR "silent infarct*"[tiab] OR "covert brain infarct*"[tiab] OR microbleed*[tiab] OR microhemorrhag*[tiab] OR microhaemorrhag*[tiab] OR "vascular brain injury"[tiab] OR "vascular brain injur*"[tiab])) AND ("1800/01/01"[edat] : "2017/05/06"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 8 | 8 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Incident dementia, Alzheimer disease, cognitive decline or impairment | left out | 52,262 / 7,700 | 85.3% | none | 0/30 (up to 10% of removed records could be relevant) | After adding Brain Infarction MeSH, re-tested the 30-record loss sample against current strategy; no eligible population/community longitudinal study was found. The outcome block is retained as a screening criterion because only 11 known records are available and outcomes may be described inconsistently. |
| Population-based or community-dwelling cohort setting | left out | 52,262 / 1,169 | 97.8% | 21543730, 22879094, 23423951 | 0/30 (up to 10% of removed records could be relevant) | After adding Brain Infarction MeSH, re-tested the 30-record loss sample against current strategy; no eligible population/community longitudinal study was found. Setting block still demonstrably loses known eligible cohort records, so setting remains a screening criterion. |
| Prospective or longitudinal observational cohort follow-up | left out | 52,262 / 12,313 | 76.4% | none | 0/30 (up to 10% of removed records could be relevant) | After adding Brain Infarction MeSH, re-tested the 30-record loss sample against current strategy; no eligible population/community longitudinal study was found. Only 11 known records are available, so the design block remains screening-only because follow-up labels can be absent. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Cerebral small vessel disease and MRI markers | 1 | `Magnetic Resonance Imaging[Mesh] AND (cognit*[tiab] OR dementia[tiab] OR alzheimer*[tiab])` | 25,537 | 0/30 |
| Cerebral small vessel disease and MRI markers | 2 | `Magnetic Resonance Imaging[Mesh] AND (cogniti*[tiab] OR dementia[tiab] OR alzheimer*[tiab])` | 25,196 | not screened |
| Population-based or community-dwelling cohort setting | 1 | `cohort*[tiab] OR participant*[tiab] OR population*[tiab]` | 2,930 | 1/30 |
| Population-based or community-dwelling cohort setting | 2 | `cohort*[tiab] OR participant*[tiab] OR population*[tiab]` | 2,913 | 0/30 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial broad exposure strategy with MeSH and title/abstract terms for every eligibility-listed marker; outcome, community setting, and longitudinal cohort design included as optional blocks for empirical testing. No known records were supplied; Entrez cutoff is 2017/05/06. |
| 2 | 20,717 | limits/combination | none | Added the named Austrian Stroke Prevention Study cohort to the optional setting vocabulary after the cohort-context probe identified eligible PMID 11901238 outside the setting block; re-evaluate counts and known-record retrieval. |
| 3 | 52,262 | small_vessel_disease: +1 / -0 | none | Added Brain Infarction MeSH after PRESS critic heading probes; text terms retain marker-specific recall and all previously screened seed records rechecked. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 2 findings; R1-01 should-fix open, R1-02 should-fix open
- Round 2 on version 3: 2 findings; R1-01 should-fix open, R1-02 should-fix accepted-risk
- Round 3 on version 3: 2 findings; R1-01 should-fix resolved, R1-02 should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1961 NCBI requests logged (1028 from cache); strategy sha256 c99a60a9c23b._

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
        "message": "52,262 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:cognitive_outcomes",
        "blocking": false,
        "requires_review": true,
        "id": "I-4fcb453370238f655c69"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:cohort_context",
        "blocking": false,
        "requires_review": true,
        "id": "I-2c8192cec20ca0f79657"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:longitudinal_design",
        "blocking": false,
        "requires_review": true,
        "id": "I-b7755748839d8cb71b56"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:cohort_context",
        "blocking": false,
        "requires_review": true,
        "id": "I-46e1f9a1b014406b5d91"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "52,262 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:cognitive_outcomes",
        "blocking": false,
        "requires_review": true,
        "id": "I-4fcb453370238f655c69"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:cohort_context",
        "blocking": false,
        "requires_review": true,
        "id": "I-2c8192cec20ca0f79657"
      },
      {
        "code": "optional_left_out_underpowered",
        "message": "Left out over the workload budget with fewer than 15 known records: the critic checks that finding more known records was tried (prior review, neighbours, pilot searches)",
        "severity": "warning",
        "location": "concept:longitudinal_design",
        "blocking": false,
        "requires_review": true,
        "id": "I-b7755748839d8cb71b56"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:cohort_context",
        "blocking": false,
        "requires_review": true,
        "id": "I-46e1f9a1b014406b5d91"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Cerebral Small Vessel Diseases",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:15:20+00:00",
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
      "checked_at": "2026-09-29T20:15:20+00:00",
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
      "checked_at": "2026-09-29T20:15:20+00:00",
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
      "requested": "Brain Infarction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T20:15:20+00:00",
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
      "location": "vocabulary:4",
      "term": {
        "text": "\"Brain Infarction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Cerebral Small Vessel Diseases\"[MeSH Terms] OR \"Leukoaraiosis\"[MeSH Terms] OR \"stroke, lacunar\"[MeSH Terms] OR \"Brain Infarction\"[MeSH Terms] OR \"cerebral small vessel disease\"[Title/Abstract] OR \"Cerebral Small Vessel Diseases\"[Title/Abstract] OR \"small vessel disease\"[Title/Abstract] OR \"small vessel diseases\"[Title/Abstract] OR \"cerebral microangiopath*\"[Title/Abstract] OR \"Leukoaraiosis\"[Title/Abstract] OR \"white matter hyperintens*\"[Title/Abstract] OR \"white matter lesion*\"[Title/Abstract] OR \"white matter change*\"[Title/Abstract] OR \"white matter abnormalit*\"[Title/Abstract] OR \"lacunar infarct*\"[Title/Abstract] OR \"lacune*\"[Title/Abstract] OR \"silent brain infarct*\"[Title/Abstract] OR \"silent cerebral infarct*\"[Title/Abstract] OR \"silent infarct*\"[Title/Abstract] OR \"covert brain infarct*\"[Title/Abstract] OR \"microbleed*\"[Title/Abstract] OR \"microhemorrhag*\"[Title/Abstract] OR \"microhaemorrhag*\"[Title/Abstract] OR \"vascular brain injury\"[Title/Abstract] OR \"vascular brain injur*\"[Title/Abstract]) AND 1800/01/01:2017/05/06[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "f50b4ea5fb2535f37bf42df46daf16bdec6abf10652719497ce7fe2e1eebeacb",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The required exposure terms cover each named marker through its own text-word expression; the optional outcome, setting, and design concepts remain available for screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "The exposure terms are OR-combined as one required concept. The tested optional blocks are left out of the final search."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "The heading set includes cerebral small vessel disease, leukoaraiosis, and lacunar stroke, but the packet does not show probes for headings representing other named MRI-marker members, such as white matter lesions, brain infarction, and cerebral microbleeds."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text terms explicitly cover the named white matter, lacunar or silent infarct, microbleed, and vascular brain injury markers. No proximity expressions or clause-specific phrase warnings appear in the supplied strategy."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The supplied PubMed expressions use valid field tags and Boolean structure; no proximity operators or syntax diagnostics are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No search limits are applied. The optional outcome, setting, and design blocks were tested and left out with recall concerns documented."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The required exposure includes several MRI-marker members, but the tested heading set does not document member-heading probes beyond Leukoaraiosis and Stroke, Lacunar. The text-word coverage and one 30-record category sample do not establish that heading-based retrieval for the other marker members was considered.",
          "recommendation": "Probe relevant PubMed headings for white matter lesions, brain infarction, and cerebral microbleeds, record their results, and add useful headings to the exposure block. Then run a complete evaluation of the revised strategy.",
          "status": "open"
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The search returns 20,717 records against a 10,000-record workload budget. The optional blocks were tested, but the packet documents only 11 known relevant records and does not show an attempt to discover additional known records through a prior review, citation neighbours, or pilot searches, as requested by the underpowered warnings.",
          "recommendation": "Document attempts to identify additional known relevant records, especially for the outcome and design concepts. Reassess the optional-block decisions with any records found; retain recall-sensitive blocks as screening criteria where evidence remains insufficient.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The mandatory exposure block returns more records than the workload budget. Each optional concept was tested, and the available evidence does not justify adding a block without risking missed eligible studies.",
          "evidence": "The outcome block removes 73.2% of records; the setting block removes 95.6% and loses three known relevant records; the design block removes 68.6%."
        },
        {
          "issue_id": "I-4fcb453370238f655c69",
          "status": "accepted-risk",
          "response": "The outcome block remains excluded because evidence is underpowered and outcomes may be inconsistently named. The packet does not document attempts to find more known relevant records, so this warning remains a risk to address.",
          "evidence": "There are 11 known relevant records, below the 15-record threshold; the sampled loss set contained 0/30 eligible studies."
        },
        {
          "issue_id": "I-2c8192cec20ca0f79657",
          "status": "accepted-risk",
          "response": "The setting block remains excluded because it demonstrably misses known relevant records. The packet does not document attempts to find more known records, so the underpowered warning remains a risk to address.",
          "evidence": "The block loses PMIDs 21543730, 22879094, and 23423951; a category probe also identified PMID 11901238 without the setting phrases."
        },
        {
          "issue_id": "I-b7755748839d8cb71b56",
          "status": "accepted-risk",
          "response": "The design block remains excluded because its safety is not established with only 11 known records, and design terms may be absent from abstracts. The packet does not document attempts to find more known relevant records.",
          "evidence": "The sampled loss set contained 0/30 eligible population or community cohort studies, but the known-record count is below the stated 15-record threshold."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "7fdbeec122d09d42cdad9f217c1cb66f44033000649a312bc51dea8adee0843d",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Each MRI marker named in eligibility has a corresponding text-word expression, including white matter hyperintensities, lacunar or silent infarcts, microbleeds, and vascular brain injury. Outcome, setting, and design remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "The exposure terms are OR-combined as the required concept. The optional blocks were tested and left out; no operator problem is evident in the supplied strategy."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "Brain Infarction[Mesh] has now been added and its result count recorded, partly addressing R1-01. The packet still does not document heading probes for white matter lesions or cerebral microbleeds."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text words cover the named MRI-marker members. No proximity expressions or clause-specific phrase warnings appear."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The supplied PubMed expressions use valid field tags and Boolean structure; no syntax diagnostics are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No search limits are applied. The exposure search exceeds the workload budget, but the optional outcome, setting, and design blocks were tested, with their recall risks documented. The packet now records use of a prior review, citation neighbours, and pilot searches to identify known records; the remaining evidence base is still small."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The required exposure includes multiple MRI-marker members. Brain Infarction[Mesh] was added and tested, but the packet still does not document heading probes for white matter lesions or cerebral microbleeds.",
          "recommendation": "Probe relevant PubMed headings for white matter lesions and cerebral microbleeds, record the results, add useful headings to the exposure block, and run a complete evaluation of the revised strategy.",
          "status": "open"
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The exposure search exceeds the 10,000-record workload budget, and only 11 eligible records are known, leaving the optional-block decisions underpowered. The current packet now documents attempts to find additional records through a prior review, citation neighbours, and pilot searches.",
          "recommendation": "Retain the optional concepts as screening criteria given the documented search and recall concerns; revisit the decision if additional eligible records are identified.",
          "status": "accepted-risk",
          "response": "The packet documents the requested discovery attempts. The optional blocks have been tested, and the available evidence does not support requiring them without risking missed eligible studies.",
          "evidence": "The notes report screening references of review PMID 25899293, citation-neighbour candidates, pilot searches, and a cohort-setting probe. Eleven eligible records were identified; the loss samples found 0/30 relevant records for each optional block, while the setting block loses known eligible records."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The mandatory exposure block remains over budget after the optional blocks were tested. Requiring an optional block would risk missing eligible studies, so the broad exposure search is retained for screening.",
          "evidence": "The exposure query returns 52,262 records. The outcome block removes 85.3% of records, the setting block removes 97.8% and loses three known eligible records, and the design block removes 76.4%."
        },
        {
          "issue_id": "I-4fcb453370238f655c69",
          "status": "accepted-risk",
          "response": "The outcome block remains excluded and outcome eligibility remains a screening criterion because the evidence base is small and outcome descriptions may vary.",
          "evidence": "The packet documents prior-review, citation-neighbour, and pilot-search efforts, but only 11 eligible records are known. The outcome block's loss sample contained 0/30 relevant studies."
        },
        {
          "issue_id": "I-2c8192cec20ca0f79657",
          "status": "accepted-risk",
          "response": "The setting block remains excluded because it loses known eligible records; setting remains a screening criterion.",
          "evidence": "The block loses PMIDs 21543730, 22879094, and 23423951. A category probe also identified PMID 11901238 outside the block. The packet documents efforts to find additional records, but only 11 eligible records are known."
        },
        {
          "issue_id": "I-b7755748839d8cb71b56",
          "status": "accepted-risk",
          "response": "The design block remains excluded because follow-up labels may be absent and the evidence base remains small; design remains a screening criterion.",
          "evidence": "The packet documents prior-review, citation-neighbour, and pilot-search efforts. Only 11 eligible records are known, and the design block's loss sample contained 0/30 relevant studies."
        },
        {
          "issue_id": "I-46e1f9a1b014406b5d91",
          "status": "accepted-risk",
          "response": "The setting category probe is stale and its probe budget is spent, so the latest setting-block change has not received a fresh probe. The setting block remains excluded, and the documented known-record losses support retaining setting as a screening criterion.",
          "evidence": "The packet reports the stale-probe warning; the setting block loses three known eligible records, and its probe history identified PMID 11901238 outside the block."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "d64bd1f7c5f519f9bf63d5348edbba67049eaadfdc8fe6d3036a1474c5f97be1",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The required exposure terms cover the named MRI markers. Outcome, setting, and design remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "The required exposure terms are combined as one concept; optional blocks were tested and left out."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes Brain Infarction[Mesh]. The packet documents checks for white matter lesions and microbleeds; no specific suitable headings were found."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text words cover the named MRI marker members. No proximity expressions or clause-specific phrase warnings appear."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The supplied expressions use valid PubMed field tags and Boolean structure; no syntax diagnostics are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No limits are applied. The search remains over budget, and the optional-block decisions retain documented recall risks after testing and attempts to identify more known records."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The packet initially lacked documented heading probes for the named MRI-marker members.",
          "recommendation": "Probe headings for white matter lesions, brain infarction, and cerebral microbleeds; add useful headings and evaluate the revised strategy.",
          "status": "resolved",
          "response": "Brain Infarction[Mesh] was added and tested. The notes document that white matter hyperintensity mapped only to broad or nonspecific headings, and no descriptor was found for microbleeds or cerebral microhemorrhage; Cerebral Hemorrhage was judged too broad to add."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The search exceeds the workload budget, with only 11 known eligible records available to assess the optional-block decisions.",
          "recommendation": "Document attempts to find additional known records and reassess optional blocks, retaining recall-sensitive concepts for screening where evidence remains insufficient.",
          "status": "accepted-risk",
          "response": "The packet documents prior-review references, citation-neighbour screening, and pilot searches. The optional blocks remain excluded because the available evidence does not justify requiring them without risking missed eligible studies.",
          "evidence": "Eleven eligible records were identified; each optional-block loss sample found 0/30 relevant records, while the setting block loses known eligible records."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The required exposure search remains over budget after optional concepts were tested; adding an optional block could miss eligible studies, so those concepts remain screening criteria.",
          "evidence": "The exposure query returns 52,262 records. The outcome block removes 85.3%, the setting block removes 97.8% and loses three known eligible records, and the design block removes 76.4%."
        },
        {
          "issue_id": "I-4fcb453370238f655c69",
          "status": "accepted-risk",
          "response": "The outcome block remains excluded because only 11 known eligible records are available and outcome descriptions may vary; the documented discovery efforts and loss sample do not establish that requiring it is safe.",
          "evidence": "The outcome block's loss sample contained 0/30 relevant studies. The packet documents screening references of a prior review, citation neighbours, and pilot searches."
        },
        {
          "issue_id": "I-2c8192cec20ca0f79657",
          "status": "accepted-risk",
          "response": "The setting block remains excluded because it loses known eligible records; setting remains a screening criterion.",
          "evidence": "The block loses PMIDs 21543730, 22879094, and 23423951. The setting probe history also identified PMID 11901238 outside the block."
        },
        {
          "issue_id": "I-b7755748839d8cb71b56",
          "status": "accepted-risk",
          "response": "The design block remains excluded because follow-up labels may be absent and the limited evidence does not establish that requiring the block is safe.",
          "evidence": "Only 11 eligible records are known; the design-block loss sample contained 0/30 relevant studies. The packet documents prior-review, citation-neighbour, and pilot-search efforts."
        },
        {
          "issue_id": "I-46e1f9a1b014406b5d91",
          "status": "accepted-risk",
          "response": "The setting probe is stale and its budget is spent, so the latest setting-block change has no fresh probe. The setting block remains excluded, with known-record losses supporting its use as a screening criterion.",
          "evidence": "The probe history identifies PMID 11901238 outside the setting block, and the block loses three known eligible records."
        }
      ]
    }
  ]
}
```

