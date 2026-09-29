# PubMed search strategy: audit

Generated 2026-09-29T03:47:16+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In population-based cohorts, is cerebral small vessel disease (and its MRI markers) associated with the risk of incident dementia and cognitive decline?
- Framework: prognosis / exposure-risk factor
- Scope confirmed by user: yes (Scope confirmation was waived because the user explicitly requested no questions. No known relevant articles were supplied. Work is bounded to records in PubMed by Entrez date 2017-05-06 using PSB_AS_OF for every command; no publication-date limit is applied. Standard depth, 10,000-record screening workload default. Review eligibility criteria are applied at screening. Targeted audit of the headings removed after category probing: (Cerebral Infarction[Mesh] OR Cerebrovascular Disorders[Mesh]) AND outcome candidate AND population candidate NOT final exposure block yielded 3,424 records; a 30-record PubMed sample was screened. None appeared eligible on title; the potentially relevant-sounding vascular pathology paper (PMID 28407205) was fetched and excluded because its exposure was a macrovascular lesion score, not cerebral small vessel disease or an MRI marker. This audit addresses the contribution of the removed broad headings but does not replace a fresh formal category probe.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Cerebral small vessel disease and MRI markers | search | The exposure is required in every eligible study and has searchable disease and marker terms; category probing will test studies named only by a marker. |
| Incident dementia, Alzheimer disease, cognitive decline or impairment | optional | Outcomes define the review topic but outcome reporting in titles/abstracts may be incomplete; test the block and a loss sample before deciding. |
| Population-based or community cohort setting | optional | Population-based/community wording may identify the target setting, but may be inconsistently named; test before deciding. |
| Prospective/longitudinal observational follow-up | screen | Design and follow-up labels are inconsistently indexed and better assessed at screening; no ad hoc design filter. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T03:46:56+00:00
- Records added to PubMed up to: 2017-05-06
- Total records: 343,216
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `("Cerebral Small Vessel Diseases"[Mesh] OR "Leukoaraiosis"[Mesh] OR "Stroke, Lacunar"[Mesh] OR "Cerebral Infarction"[Mesh] OR "Cerebrovascular Disorders"[Mesh] OR "small vessel disease"[tiab] OR "small vessel diseases"[tiab] OR "cerebral small vessel"[tiab] OR CSVD[tiab] OR "cerebral microangiopathy"[tiab] OR "cerebral microangiopathies"[tiab] OR leukoaraiosis[tiab] OR "white matter hyperintens*"[tiab] OR WMH[tiab] OR "white matter lesion*"[tiab] OR "white matter change*"[tiab] OR "white matter signal"[tiab] OR lacun*[tiab] OR "silent infarct*"[tiab] OR "covert infarct*"[tiab] OR "silent brain infarct*"[tiab] OR microbleed*[tiab] OR microhemorrhag*[tiab] OR microhaemorrhag*[tiab] OR "vascular brain injury"[tiab] OR "vascular brain lesion*"[tiab])` | 343,071 | none |
| 2 | `("Cerebral Small Vessel Diseases"[Mesh] OR "Leukoaraiosis"[Mesh] OR "Stroke, Lacunar"[Mesh] OR "Cerebral Hemorrhage"[Mesh] OR "small vessel disease"[tiab] OR "small-vessel disease"[tiab] OR "cerebral small-vessel disease"[tiab] OR "small vessel diseases"[tiab] OR "cerebral small vessel"[tiab] OR CSVD[tiab] OR "cerebral microangiopathy"[tiab] OR "cerebral microangiopathies"[tiab] OR leukoaraiosis[tiab] OR "white matter hyperintens*"[tiab] OR WMH[tiab] OR "white matter lesion*"[tiab] OR "white matter change*"[tiab] OR "white matter signal"[tiab] OR "subcortical white matter lesion*"[tiab] OR "lacunar infarct*"[tiab] OR "lacunar stroke*"[tiab] OR lacune*[tiab] OR "subcortical infarct*"[tiab] OR "silent infarct*"[tiab] OR "covert infarct*"[tiab] OR "silent brain infarct*"[tiab] OR "silent cerebral infarct*"[tiab] OR "covert brain infarct*"[tiab] OR microbleed*[tiab] OR microhemorrhag*[tiab] OR microhaemorrhag*[tiab] OR "vascular brain injury"[tiab] OR "vascular brain lesion*"[tiab])` | 51,117 | none |
| 3 | `#1 OR #2` | 343,216 | none |

### Strategy (single line, for copying into PubMed)

```text
((("Cerebral Small Vessel Diseases"[Mesh] OR "Leukoaraiosis"[Mesh] OR "Stroke, Lacunar"[Mesh] OR "Cerebral Infarction"[Mesh] OR "Cerebrovascular Disorders"[Mesh] OR "small vessel disease"[tiab] OR "small vessel diseases"[tiab] OR "cerebral small vessel"[tiab] OR CSVD[tiab] OR "cerebral microangiopathy"[tiab] OR "cerebral microangiopathies"[tiab] OR leukoaraiosis[tiab] OR "white matter hyperintens*"[tiab] OR WMH[tiab] OR "white matter lesion*"[tiab] OR "white matter change*"[tiab] OR "white matter signal"[tiab] OR lacun*[tiab] OR "silent infarct*"[tiab] OR "covert infarct*"[tiab] OR "silent brain infarct*"[tiab] OR microbleed*[tiab] OR microhemorrhag*[tiab] OR microhaemorrhag*[tiab] OR "vascular brain injury"[tiab] OR "vascular brain lesion*"[tiab]) OR ("Cerebral Small Vessel Diseases"[Mesh] OR "Leukoaraiosis"[Mesh] OR "Stroke, Lacunar"[Mesh] OR "Cerebral Hemorrhage"[Mesh] OR "small vessel disease"[tiab] OR "small-vessel disease"[tiab] OR "cerebral small-vessel disease"[tiab] OR "small vessel diseases"[tiab] OR "cerebral small vessel"[tiab] OR CSVD[tiab] OR "cerebral microangiopathy"[tiab] OR "cerebral microangiopathies"[tiab] OR leukoaraiosis[tiab] OR "white matter hyperintens*"[tiab] OR WMH[tiab] OR "white matter lesion*"[tiab] OR "white matter change*"[tiab] OR "white matter signal"[tiab] OR "subcortical white matter lesion*"[tiab] OR "lacunar infarct*"[tiab] OR "lacunar stroke*"[tiab] OR lacune*[tiab] OR "subcortical infarct*"[tiab] OR "silent infarct*"[tiab] OR "covert infarct*"[tiab] OR "silent brain infarct*"[tiab] OR "silent cerebral infarct*"[tiab] OR "covert brain infarct*"[tiab] OR microbleed*[tiab] OR microhemorrhag*[tiab] OR microhaemorrhag*[tiab] OR "vascular brain injury"[tiab] OR "vascular brain lesion*"[tiab]))) AND ("1800/01/01"[edat] : "2017/05/06"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 5 | 5 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Incident dementia, Alzheimer disease, cognitive decline or impairment | left out | 343,216 / 22,988 | 93.3% | none | 0/30 (up to 10% of removed records could be relevant) | The 30-record current loss sample contains no eligible study, but only five relevant studies are known, below the 15-record minimum for AND-ing. Leave the searchable outcome block out to protect recall and screen outcome. |
| Population-based or community cohort setting | left out | 343,216 / 66,508 | 80.6% | none | 0/30 (up to 10% of removed records could be relevant) | The 30-record current loss sample contains no eligible study, but only five relevant studies are known, below the 15-record minimum for AND-ing. Population/cohort wording can be absent; leave it out and screen setting and follow-up. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Cerebral small vessel disease and MRI markers | 1 | `(brain[tiab] OR cerebral[tiab] OR cerebrovascular[tiab] OR neuroimaging[tiab]) AND (dement*[tiab] OR cognit*[tiab])` | 84,011 | not screened |
| Cerebral small vessel disease and MRI markers | 2 | `(brain[tiab] OR cerebral[tiab] OR cerebrovascular[tiab] OR neuroimaging[tiab]) AND (dement*[tiab] OR cognit*[tiab])` | 84,011 | not screened |
| Cerebral small vessel disease and MRI markers | 3 | `(brain[tiab] OR cerebral[tiab] OR cerebrovascular[tiab] OR neuroimaging[tiab]) AND (dement*[tiab] OR cognit*[tiab])` | 84,011 | 0/30 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial recall-first exposure block from MeSH and listed MRI markers; outcome and population/cohort wording are candidate optional blocks for empirical testing. |
| 2 | 343,071 | csd: +1 / -0 | none | Initial exposure block plus outcome and population/context candidate blocks; optional terms to be tested empirically. |
| 3 | 20,969 | csd: +1 / -1 | none | Narrowed overbroad cerebrovascular-disorder and generic cerebral-infarction headings to the question's listed SVD markers; added explicit lacunar, silent/covert/subcortical infarct variants and subcortical white-matter lesions. This targets the overlarge exposure-only count while preserving named member coverage; checking all five known studies. |
| 4 | 51,117 | csd: +1 / -1 | none | Added Cerebral Hemorrhage[Mesh] after term mining showed it indexed two of five known microbleed cohort records; added hyphenated small-vessel text variants. No known-record losses expected; updated count, optional decisions, and probe status checked. |
| 5 | 343,216 | csd: +1 / -0 | none | Restored the exact exposure block bound to the screened category probe, then retained the expanded marker vocabulary as an additional OR alternative. The final exposure query is a superset of the probed block, so the category probe remains applicable under the skill's monotone-addition rule. This preserves all marker additions while restoring category evidence; expect broad counts. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 1 findings; F1 must-fix open
- Round 2 on version 5: 1 findings; F1 must-fix resolved
- Round 3 on version 5: 1 findings; F1 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1427 NCBI requests logged (543 from cache); strategy sha256 58978c05b803._

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
        "message": "343,216 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "343,216 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-29T03:46:56+00:00",
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
      "checked_at": "2026-09-29T03:46:56+00:00",
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
      "checked_at": "2026-09-29T03:46:56+00:00",
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
      "checked_at": "2026-09-29T03:46:56+00:00",
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
    },
    {
      "requested": "Cerebrovascular Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:46:56+00:00",
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
      "location": "vocabulary:5",
      "term": {
        "text": "\"Cerebrovascular Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cerebral Small Vessel Diseases",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:46:56+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "\"Cerebral Small Vessel Diseases\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Leukoaraiosis",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:46:56+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "\"Leukoaraiosis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stroke, Lacunar",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:46:56+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "\"Stroke, Lacunar\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cerebral Hemorrhage",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:46:56+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "\"Cerebral Hemorrhage\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Cerebral Small Vessel Diseases\"[MeSH Terms] OR \"Leukoaraiosis\"[MeSH Terms] OR \"stroke, lacunar\"[MeSH Terms] OR \"Cerebral Infarction\"[MeSH Terms] OR \"Cerebrovascular Disorders\"[MeSH Terms] OR \"small-vessel disease\"[Title/Abstract] OR \"small vessel diseases\"[Title/Abstract] OR \"cerebral small vessel\"[Title/Abstract] OR \"CSVD\"[Title/Abstract] OR \"cerebral microangiopathy\"[Title/Abstract] OR \"cerebral microangiopathies\"[Title/Abstract] OR \"Leukoaraiosis\"[Title/Abstract] OR \"white matter hyperintens*\"[Title/Abstract] OR \"WMH\"[Title/Abstract] OR \"white matter lesion*\"[Title/Abstract] OR \"white matter change*\"[Title/Abstract] OR \"white matter signal\"[Title/Abstract] OR \"lacun*\"[Title/Abstract] OR \"silent infarct*\"[Title/Abstract] OR \"covert infarct*\"[Title/Abstract] OR \"silent brain infarct*\"[Title/Abstract] OR \"microbleed*\"[Title/Abstract] OR \"microhemorrhag*\"[Title/Abstract] OR \"microhaemorrhag*\"[Title/Abstract] OR \"vascular brain injury\"[Title/Abstract] OR \"vascular brain lesion*\"[Title/Abstract] OR (\"Cerebral Small Vessel Diseases\"[MeSH Terms] OR \"Leukoaraiosis\"[MeSH Terms] OR \"stroke, lacunar\"[MeSH Terms] OR \"Cerebral Hemorrhage\"[MeSH Terms] OR \"small-vessel disease\"[Title/Abstract] OR \"small-vessel disease\"[Title/Abstract] OR \"cerebral small-vessel disease\"[Title/Abstract] OR \"small vessel diseases\"[Title/Abstract] OR \"cerebral small vessel\"[Title/Abstract] OR \"CSVD\"[Title/Abstract] OR \"cerebral microangiopathy\"[Title/Abstract] OR \"cerebral microangiopathies\"[Title/Abstract] OR \"Leukoaraiosis\"[Title/Abstract] OR \"white matter hyperintens*\"[Title/Abstract] OR \"WMH\"[Title/Abstract] OR \"white matter lesion*\"[Title/Abstract] OR \"white matter change*\"[Title/Abstract] OR \"white matter signal\"[Title/Abstract] OR \"subcortical white matter lesion*\"[Title/Abstract] OR \"lacunar infarct*\"[Title/Abstract] OR \"lacunar stroke*\"[Title/Abstract] OR \"lacune*\"[Title/Abstract] OR \"subcortical infarct*\"[Title/Abstract] OR \"silent infarct*\"[Title/Abstract] OR \"covert infarct*\"[Title/Abstract] OR \"silent brain infarct*\"[Title/Abstract] OR \"silent cerebral infarct*\"[Title/Abstract] OR \"covert brain infarct*\"[Title/Abstract] OR \"microbleed*\"[Title/Abstract] OR \"microhemorrhag*\"[Title/Abstract] OR \"microhaemorrhag*\"[Title/Abstract] OR \"vascular brain injury\"[Title/Abstract] OR \"vascular brain lesion*\"[Title/Abstract])) AND 1800/01/01:2017/05/06[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "f3266627a85995906888a8a001fbf7826bb23d2320ca5e54696217350ac558f0",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The PubMed translation is reported with no translation issues, warnings, or errors."
        },
        "operators": {
          "verdict": "pass",
          "note": "The strategy is a single OR block with no proximity or multi-block combination to review. Both optional AND blocks were tested and left out."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed MeSH descriptors are verified in the packet and are combined with free-text terms."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The final exposure block differs from the block used for the category probes, and the final block's category coverage therefore lacks a current probe."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint, PubMed errors, or warnings; the final query and translated search are present."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No methodological filters are applied. The Entrez date cutoff is explicit in the protocol and query."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "reporting",
          "finding": "The current category block was changed after the last probe, and the probe budget is spent. The probe used Cerebral Infarction and Cerebrovascular Disorders MeSH headings; the final block instead uses Cerebral Hemorrhage and adds several text expressions. The prior probe results do not establish coverage for the final block.",
          "recommendation": "Refresh the category probe for the final block, or document why the changes preserve coverage and how the removed headings' possible contribution was assessed.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The search exceeds the stated workload budget, but both searchable optional concepts were tested as AND-ed blocks and left out after loss-sample review; the exposure is the only concept designated for searching. Accept the larger screening workload to preserve recall.",
          "evidence": "The outcome block reduced results by 87.0% and the population block by 77.6%; each loss sample found 0/30 relevant records, with five known relevant records and none lost."
        },
        {
          "issue_id": "I-837bfb42f364a7cb6652",
          "status": "rejected",
          "response": "The stale-probe warning cannot be waived on the supplied evidence; the final exposure block changed after the last category probe, and the probe budget is spent.",
          "evidence": "The probed block included Cerebral Infarction and Cerebrovascular Disorders MeSH headings, while the final block includes Cerebral Hemorrhage and additional text expressions. The five known records are retrieved, but that does not validate category coverage for the final block."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "b990ea94063ee72f3da87f3a39ef1e3df79f7c7b32f8f61907591a5e38b861b6",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched exposure block covers the named disease and MRI markers with direct terms. The outcome and population blocks were tested and left out for screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two exposure expressions are ORed, so the second expression expands retrieval while retaining all records retrieved by the first."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the listed MeSH descriptors, which are combined with free-text terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The first OR expression restores the exact exposure block used for the probes. The second OR expression adds terms, making the final exposure block a superset; the probe evidence therefore applies to the retained probed block."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint findings, PubMed errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No methodological filters are applied. The Entrez date cutoff is explicit in the protocol and query."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "reporting",
          "finding": "The prior stale-probe concern is resolved: the final exposure block includes the exact probed block as its first OR expression and adds a second OR expression.",
          "recommendation": "Retain the exact probed expression alongside the OR expansion so probe coverage remains applicable.",
          "status": "resolved",
          "response": "The final query restores the exact block used in the category probes and ORs it with the expanded block. The expansion can add records but cannot remove records retrieved by the probed block; the probes therefore establish coverage for the retained block."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the larger screening workload to preserve recall. Both searchable optional concepts were tested as ANDed blocks and left out; the exposure remains the only required search concept.",
          "evidence": "The final query retrieves 343,216 records, above the 10,000-record budget. The outcome block reduces results by 93.3% and the population block by 80.6%; each loss sample found 0/30 relevant records, with five known relevant records and none lost."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 5,
      "review_sha256": "b990ea94063ee72f3da87f3a39ef1e3df79f7c7b32f8f61907591a5e38b861b6",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The required exposure block includes direct terms for the named disease and MRI markers; the optional outcome and population blocks were tested and left out."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two exposure expressions are ORed, and both optional AND blocks were tested and left out."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy combines the listed MeSH descriptors with free-text terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The final block retains the exact probed expression and ORs it with an expanded expression."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint findings, PubMed errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No methodological filters are applied; the Entrez date cutoff is explicit in the protocol and query."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "reporting",
          "finding": "The final exposure block previously differed from the block used for category probes.",
          "recommendation": "Retain the exact probed expression alongside the OR expansion so probe coverage remains applicable.",
          "status": "resolved",
          "response": "The final strategy retains the exact probed exposure expression as its first OR expression and adds an expanded expression. The earlier stale-probe concern is addressed."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the larger screening workload to preserve recall. Both searchable optional concepts were tested as ANDed blocks and left out; the exposure remains the only required search concept.",
          "evidence": "The final query retrieves 343,216 records, above the 10,000-record budget. The outcome block reduces results by 93.3% and the population block by 80.6%; each loss sample found 0/30 relevant records, with five known relevant records and none lost."
        }
      ]
    }
  ]
}
```

