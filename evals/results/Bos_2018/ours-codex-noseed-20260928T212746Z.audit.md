# PubMed search strategy: audit

Generated 2026-09-28T21:54:12+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In population-based cohorts, is cerebral small vessel disease (and its MRI markers) associated with the risk of incident dementia and cognitive decline?
- Framework: PECO
- Scope confirmed by user: yes (User requested proceeding without clarification. Assumed PECO; searched the core exposure and tested topic-defining outcome and population-setting blocks as optional. Design and community dwelling are screened. No known relevant records supplied. Standard depth, 10,000-record default workload budget, no language/date limits; PubMed is bounded by Entrez date 2017-05-06 via PSB_AS_OF, with no publication-date limit. Round-1 critique added Cognition[Mesh] and cognition[tiab]. Outcome labels are enumerated, so the outcome concept is no longer treated as a category; the exposure remains a category.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Cerebral small vessel disease and MRI markers | search | Core exposure defining every eligible record; marker members are frequently named individually, so this is a category concept. |
| Incident dementia, Alzheimer disease, cognitive decline or impairment | optional | Topic-defining outcome block tested and AND-ed; dementia, Alzheimer disease, and cognitive decline/impairment are individually named and searched as separate endpoint labels, so this is not treated as a parent category. |
| Population-based/community-dwelling cohort setting | optional | Topic-defining population setting may be searchable but inconsistently named; test its retrieval reduction and loss sample. |
| Prospective cohort or longitudinal observational follow-up | screen | Eligibility property; do not require ad hoc design terms in the search. |
| Community-dwelling participants | screen | Community dwelling can be implicit or described only in full text. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T21:53:13+00:00
- Records added to PubMed up to: 2017-05-06
- Total records: 7,952
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Cerebral Small Vessel Diseases"[Mesh]` | 6,257 | none |
| 2 | `"Leukoaraiosis"[Mesh]` | 470 | none |
| 3 | `"Stroke, Lacunar"[Mesh]` | 412 | none |
| 4 | `"Cerebral Infarction"[Mesh]` | 29,744 | none |
| 5 | `"cerebral small vessel disease"[tiab]` | 813 | none |
| 6 | `"cerebral small vessel diseases"[tiab]` | 105 | none |
| 7 | `"small vessel disease"[tiab]` | 2,316 | none |
| 8 | `"small vessel diseases"[tiab]` | 203 | none |
| 9 | `"cerebral microangiopath*"[tiab]` | 150 | none |
| 10 | `CSVD[tiab]` | 127 | none |
| 11 | `leukoaraiosis[tiab]` | 1,008 | none |
| 12 | `"white matter hyperintens*"[tiab]` | 2,354 | none |
| 13 | `"white matter lesion*"[tiab]` | 4,051 | none |
| 14 | `"white matter change*"[tiab]` | 1,880 | none |
| 15 | `"white matter abnormalit*"[tiab]` | 1,590 | none |
| 16 | `"white matter signal"[tiab:~2]` | 611 | none |
| 17 | `"periventricular hyperintens*"[tiab]` | 316 | none |
| 18 | `"lacunar infarct*"[tiab]` | 2,251 | none |
| 19 | `"lacunar stroke*"[tiab]` | 918 | none |
| 20 | `"silent infarct*"[tiab]` | 311 | none |
| 21 | `"silent brain infarct*"[tiab]` | 280 | none |
| 22 | `"silent cerebral infarct*"[tiab]` | 322 | none |
| 23 | `"covert brain infarct*"[tiab]` | 9 | none |
| 24 | `"asymptomatic brain infarct*"[tiab]` | 15 | none |
| 25 | `"cerebral microbleed*"[tiab]` | 710 | none |
| 26 | `"brain microbleed*"[tiab]` | 59 | none |
| 27 | `"cerebral microhemorrhag*"[tiab]` | 62 | none |
| 28 | `"brain microhemorrhag*"[tiab]` | 15 | none |
| 29 | `"vascular brain injur*"[tiab]` | 77 | none |
| 30 | `"vascular brain lesion*"[tiab]` | 74 | none |
| 31 | `"subcortical vascular disease"[tiab]` | 35 | none |
| 32 | `"small vessel ischemic"[tiab]` | 37 | none |
| 33 | `"small vessel ischaemic"[tiab]` | 9 | none |
| 34 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33` | 48,108 | none |
| 35 | `"Dementia"[Mesh]` | 145,526 | none |
| 36 | `"Alzheimer Disease"[Mesh]` | 82,140 | none |
| 37 | `"Cognitive Dysfunction"[Mesh]` | 8,211 | none |
| 38 | `"Cognition Disorders"[Mesh]` | 80,254 | none |
| 39 | `dementia*[tiab]` | 87,012 | none |
| 40 | `Alzheimer*[tiab]` | 116,181 | none |
| 41 | `"cognitive decline"[tiab]` | 15,036 | none |
| 42 | `"cognitive deteriorat*"[tiab]` | 1,480 | none |
| 43 | `"cognitive impair*"[tiab]` | 45,842 | none |
| 44 | `"cognitive dysfunction"[tiab]` | 9,912 | none |
| 45 | `"cognitive function"[tiab]` | 25,869 | none |
| 46 | `"cognitive change*"[tiab]` | 3,310 | none |
| 47 | `"cognitive performance"[tiab]` | 13,653 | none |
| 48 | `"memory decline"[tiab]` | 1,116 | none |
| 49 | `"memory impair*"[tiab]` | 10,485 | none |
| 50 | `"Cognition"[Mesh]` | 138,866 | none |
| 51 | `cognition[tiab]` | 54,533 | none |
| 52 | `#35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51` | 430,993 | none |
| 53 | `#34 AND #52` | 7,952 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Cerebral Small Vessel Diseases"[Mesh] OR "Leukoaraiosis"[Mesh] OR "Stroke, Lacunar"[Mesh] OR "Cerebral Infarction"[Mesh] OR "cerebral small vessel disease"[tiab] OR "cerebral small vessel diseases"[tiab] OR "small vessel disease"[tiab] OR "small vessel diseases"[tiab] OR "cerebral microangiopath*"[tiab] OR CSVD[tiab] OR leukoaraiosis[tiab] OR "white matter hyperintens*"[tiab] OR "white matter lesion*"[tiab] OR "white matter change*"[tiab] OR "white matter abnormalit*"[tiab] OR "white matter signal"[tiab:~2] OR "periventricular hyperintens*"[tiab] OR "lacunar infarct*"[tiab] OR "lacunar stroke*"[tiab] OR "silent infarct*"[tiab] OR "silent brain infarct*"[tiab] OR "silent cerebral infarct*"[tiab] OR "covert brain infarct*"[tiab] OR "asymptomatic brain infarct*"[tiab] OR "cerebral microbleed*"[tiab] OR "brain microbleed*"[tiab] OR "cerebral microhemorrhag*"[tiab] OR "brain microhemorrhag*"[tiab] OR "vascular brain injur*"[tiab] OR "vascular brain lesion*"[tiab] OR "subcortical vascular disease"[tiab] OR "small vessel ischemic"[tiab] OR "small vessel ischaemic"[tiab]) AND ("Dementia"[Mesh] OR "Alzheimer Disease"[Mesh] OR "Cognitive Dysfunction"[Mesh] OR "Cognition Disorders"[Mesh] OR dementia*[tiab] OR Alzheimer*[tiab] OR "cognitive decline"[tiab] OR "cognitive deteriorat*"[tiab] OR "cognitive impair*"[tiab] OR "cognitive dysfunction"[tiab] OR "cognitive function"[tiab] OR "cognitive change*"[tiab] OR "cognitive performance"[tiab] OR "memory decline"[tiab] OR "memory impair*"[tiab] OR "Cognition"[Mesh] OR cognition[tiab])) AND ("1800/01/01"[edat] : "2017/05/06"[edat])
```

## Validation against known relevant records

No known relevant records were available, so recall was not estimated.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Incident dementia, Alzheimer disease, cognitive decline or impairment | AND-ed | 48,108 / 7,952 | 83.5% | none | 0/30 (up to 10% of removed records could be relevant) | The refreshed outcome block including Cognition[Mesh] and cognition[tiab] reduces the exposure-only set from 48,108 to 7,952 (83.5%). The refreshed 30-record loss sample contained no eligible cohort study; no known seeds or benchmark records were lost. Because this remains a high-impact outcome AND with no known-record validation, recall risk is documented for PRESS review. |
| Population-based/community-dwelling cohort setting | left out | 7,952 / 2,280 | 71.3% | none | 0/30 (up to 10% of removed records could be relevant) | On the current query, this setting candidate reduces results from 7,952 to 2,280. The 30-record loss sample had no confirmed eligible studies; one abstract (PMID 27709107) described an autopsy cohort with vascular neuropathology and cognitive trajectories, but the abstract did not establish an eligible MRI/SVD exposure or a community-dwelling cohort, so it remains uncertain and was not added as relevant. Keep the block out because cohort/community labels remain unreliable and the current search is within the 10,000 budget. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Cerebral small vessel disease and MRI markers | 1 | `white matter[tiab] OR infarct*[tiab] OR microbleed*[tiab] OR microhemorrhag*[tiab] OR cerebrovascular[tiab] OR " Cerebrovascular Disorders\[Mesh]` | 0 | 0/0 |
| Cerebral small vessel disease and MRI markers | 2 | `white matter[tiab] OR infarct*[tiab] OR microbleed*[tiab] OR microhemorrhag*[tiab] OR cerebrovascular[tiab] OR Cerebrovascular Disorders[Mesh]` | 538,315 | not screened |
| Cerebral small vessel disease and MRI markers | 3 | `white matter[tiab] OR infarct*[tiab] OR microbleed*[tiab] OR microhemorrhag*[tiab] OR cerebrovascular[tiab] OR Cerebrovascular Disorders[Mesh]` | 538,315 | 0/30 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 48,108 | initial | none | Initial broad exposure block with named SVD MRI-marker members; test outcome and population setting as optional blocks. No seed records were supplied. |
| 2 | 7,555 | outcome: +15 / -0 | none | After screening the outcome-block loss sample (0 relevant of 30), promoted the topic-defining outcome block to the query. Re-measure the setting candidate against the updated query. |
| 3 | 7,952 | outcome: +2 / -0 | none | Critic round 1 identified that cognition may be named without cognitive decline or impairment. Added Cognition[Mesh] and cognition[tiab] to the outcome block; these are supported by the outcome category probe broader query and MeSH entry terms. Reevaluate count and known-record effects. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2 (same-context critic; no separate reviewer context was available): 1 findings; outcome-cognition-vocabulary should-fix open
- Round 2 on version 3 (same-context critic; no separate reviewer context was available): 1 findings; outcome-cognition-vocabulary should-fix resolved
- Round 3 on version 3 (same-context closing critic; no separate reviewer context was available): 1 findings; outcome-cognition-vocabulary should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 953 NCBI requests logged (382 from cache); strategy sha256 331fca04fc1b._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:svd",
        "blocking": false,
        "requires_review": true,
        "id": "I-59f75d45dd32eaf35a89"
      }
    ],
    "issues": [
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:svd",
        "blocking": false,
        "requires_review": true,
        "id": "I-59f75d45dd32eaf35a89"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Cerebral Small Vessel Diseases",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:53:13+00:00",
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
      "checked_at": "2026-09-28T21:53:13+00:00",
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
      "checked_at": "2026-09-28T21:53:13+00:00",
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
      "checked_at": "2026-09-28T21:53:13+00:00",
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
      "requested": "Dementia",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:53:13+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003704",
          "name": "Dementia",
          "type": "descriptor",
          "scope_note": "An acquired organic mental disorder with loss of intellectual abilities of sufficient severity to interfere with social or occupational functioning. The dysfunction is multifaceted and involves memory, behavior, personality, judgment, attention, spatial relations, language, abstract thought, and other executive functions. The intellectual decline is usually progressive, and initially spares the...",
          "tree_numbers": [
            "C10.228.140.380",
            "F03.615.400"
          ],
          "entry_terms": 12,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003704",
      "preferred_label": "Dementia",
      "type": "descriptor",
      "location": "vocabulary:34",
      "term": {
        "text": "\"Dementia\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alzheimer Disease",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:53:13+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000544",
          "name": "Alzheimer Disease",
          "type": "descriptor",
          "scope_note": "A degenerative disease of the BRAIN characterized by the insidious onset of DEMENTIA. Impairment of MEMORY, judgment, attention span, and problem solving skills are followed by severe APRAXIAS and a global loss of cognitive abilities. The condition primarily occurs after age 60, and is marked pathologically by severe cortical atrophy and the triad of SENILE PLAQUES; NEUROFIBRILLARY TANGLES; and...",
          "tree_numbers": [
            "C10.228.140.380.100",
            "C10.574.945.249",
            "F03.615.400.100"
          ],
          "entry_terms": 35,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000544",
      "preferred_label": "Alzheimer Disease",
      "type": "descriptor",
      "location": "vocabulary:35",
      "term": {
        "text": "\"Alzheimer Disease\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognitive Dysfunction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:53:13+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D060825",
          "name": "Cognitive Dysfunction",
          "type": "descriptor",
          "scope_note": "Diminished or impaired mental and/or intellectual function.",
          "tree_numbers": [
            "F03.615.250.700"
          ],
          "entry_terms": 25,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D060825",
      "preferred_label": "Cognitive Dysfunction",
      "type": "descriptor",
      "location": "vocabulary:36",
      "term": {
        "text": "\"Cognitive Dysfunction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognition Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:53:13+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003072",
          "name": "Cognition Disorders",
          "type": "descriptor",
          "scope_note": "Disorders characterized by disturbances in mental processes related to learning, thinking, reasoning, and judgment.",
          "tree_numbers": [
            "F03.615.250"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003072",
      "preferred_label": "Cognition Disorders",
      "type": "descriptor",
      "location": "vocabulary:37",
      "term": {
        "text": "\"Cognition Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognition",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:53:13+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003071",
          "name": "Cognition",
          "type": "descriptor",
          "scope_note": "Intellectual or mental process whereby an organism obtains knowledge.",
          "tree_numbers": [
            "F02.463.188"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003071",
      "preferred_label": "Cognition",
      "type": "descriptor",
      "location": "vocabulary:49",
      "term": {
        "text": "\"Cognition\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Cerebral Small Vessel Diseases\"[MeSH Terms] OR \"Leukoaraiosis\"[MeSH Terms] OR \"stroke, lacunar\"[MeSH Terms] OR \"Cerebral Infarction\"[MeSH Terms] OR \"cerebral small vessel disease\"[Title/Abstract] OR \"Cerebral Small Vessel Diseases\"[Title/Abstract] OR \"small vessel disease\"[Title/Abstract] OR \"small vessel diseases\"[Title/Abstract] OR \"cerebral microangiopath*\"[Title/Abstract] OR \"CSVD\"[Title/Abstract] OR \"Leukoaraiosis\"[Title/Abstract] OR \"white matter hyperintens*\"[Title/Abstract] OR \"white matter lesion*\"[Title/Abstract] OR \"white matter change*\"[Title/Abstract] OR \"white matter abnormalit*\"[Title/Abstract] OR \"white matter signal\"[Title/Abstract:~2] OR \"periventricular hyperintens*\"[Title/Abstract] OR \"lacunar infarct*\"[Title/Abstract] OR \"lacunar stroke*\"[Title/Abstract] OR \"silent infarct*\"[Title/Abstract] OR \"silent brain infarct*\"[Title/Abstract] OR \"silent cerebral infarct*\"[Title/Abstract] OR \"covert brain infarct*\"[Title/Abstract] OR \"asymptomatic brain infarct*\"[Title/Abstract] OR \"cerebral microbleed*\"[Title/Abstract] OR \"brain microbleed*\"[Title/Abstract] OR \"cerebral microhemorrhag*\"[Title/Abstract] OR \"brain microhemorrhag*\"[Title/Abstract] OR \"vascular brain injur*\"[Title/Abstract] OR \"vascular brain lesion*\"[Title/Abstract] OR \"subcortical vascular disease\"[Title/Abstract] OR \"small vessel ischemic\"[Title/Abstract] OR \"small vessel ischaemic\"[Title/Abstract]) AND (\"Dementia\"[MeSH Terms] OR \"Alzheimer Disease\"[MeSH Terms] OR \"Cognitive Dysfunction\"[MeSH Terms] OR \"Cognition Disorders\"[MeSH Terms] OR \"dementia*\"[Title/Abstract] OR \"alzheimer*\"[Title/Abstract] OR \"cognitive decline\"[Title/Abstract] OR \"cognitive deteriorat*\"[Title/Abstract] OR \"cognitive impair*\"[Title/Abstract] OR \"Cognitive Dysfunction\"[Title/Abstract] OR \"cognitive function\"[Title/Abstract] OR \"cognitive change*\"[Title/Abstract] OR \"cognitive performance\"[Title/Abstract] OR \"memory decline\"[Title/Abstract] OR \"memory impair*\"[Title/Abstract] OR \"Cognition\"[MeSH Terms] OR \"Cognition\"[Title/Abstract]) AND 1800/01/01:2017/05/06[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "a1e5f81fb788a8b9ef4fc0194ea5d3f0a84767bd0d1e27f0d82ec6b4c65ee202",
      "note": "same-context critic; no separate reviewer context was available",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two AND-ed blocks match the core exposure and topic-defining outcome. Setting and follow-up design remain for screening. The stale exposure category probe is dispositioned below."
        },
        "operators": {
          "verdict": "pass",
          "note": "The blocks are OR-ed internally and AND-ed together; no NOT or untested operator constructions are present."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The core headings are explicit, exploded by default, and the bound validation confirms them. Leukoaraiosis is a direct marker heading; lacunar stroke and cerebral infarction cover infarct terminology."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The outcome vocabulary has cognitive* formulations but not the bare word cognition, which appears in records describing cognitive test outcomes. Add cognition[tiab] and the Cognition MeSH descriptor; then reevaluate."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All terms have explicit fields, truncations meet minimum stem length, and proximity is used without wildcards."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, publication-date, age, or design filter is applied. The Entrez-date bound is 2017-05-06 as requested."
        }
      },
      "findings": [
        {
          "id": "outcome-cognition-vocabulary",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "outcome",
          "finding": "The outcome block lacks the bare free-text term cognition and the Cognition MeSH heading; a record may describe change in cognition or test performance without saying cognitive decline or impairment.",
          "recommendation": "Add cognition[tiab] and \"Cognition\"[Mesh], run psb eval, and review any resulting probe status or count change.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-59f75d45dd32eaf35a89",
          "status": "accepted-risk",
          "response": "The exposure-category probe is stale because the outcome block was promoted after its draw, and the standard probe allowance was consumed by duplicate draws. The remaining probe cannot be refreshed within the configured budget; this is retained as a limitation for human PRESS review.",
          "evidence": "The corrected broader exposure query retrieved 538,315 records outside the block and a screened 30-record sample contained 0 eligible records, but this sample was drawn before the final outcome block was added. The first malformed probe had zero outside records; a duplicate draw was also left unscreened. The final exposure block explicitly searches cerebral small vessel disease, white matter hyperintensities/lesions, lacunar and silent infarcts, cerebral microbleeds/microhemorrhages, and vascular brain injury."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "6857d1a6f8686b74ce6200ad7ffacb283361236867e8f64de34fd481e0b7d994",
      "note": "same-context critic; no separate reviewer context was available",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two AND-ed blocks reflect the cerebral SVD exposure and the review-defined cognitive/dementia outcomes. The population setting and longitudinal design remain screening criteria; both searchable optional concepts were measured."
        },
        "operators": {
          "verdict": "pass",
          "note": "Correct OR within concepts and AND across concepts; no NOT, untested operators, or fragile directional terms."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Cerebral Small Vessel Diseases, Leukoaraiosis, Stroke, Lacunar, Cerebral Infarction, Dementia, Alzheimer Disease, Cognition Disorders, Cognitive Dysfunction, and Cognition are explicit verified headings; explosion is retained."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The previous gap is fixed with Cognition[Mesh] and cognition[tiab]. They increased the final count by 397 (7,555 to 7,952), with no known records lost; both have field tags and the MeSH heading is verified."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The bound evaluation reports no lint or translation issues. Phrase proximity and truncation are syntactically valid."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No population, age, language, or publication-date filters are used. The entry-date bound matches the requested cutoff."
        }
      },
      "findings": [
        {
          "id": "outcome-cognition-vocabulary",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "outcome",
          "finding": "The outcome block lacked the bare free-text term cognition and the Cognition MeSH heading.",
          "recommendation": "Add cognition[tiab] and \"Cognition\"[Mesh], run psb eval, and review any resulting probe status or count change.",
          "status": "resolved",
          "response": "Added \"Cognition\"[Mesh] and cognition[tiab] to the outcome block, confirmed the descriptor is Cognition (D003071), and reevaluated. The final count rose from 7,555 to 7,952; no known records were lost or gained. The updated optional loss sample had 0 eligible records among 30 screened."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-59f75d45dd32eaf35a89",
          "status": "accepted-risk",
          "response": "The exposure-category probe is stale because the outcome block was promoted after its draw, and the standard probe allowance was consumed by duplicate draws. The remaining probe cannot be refreshed within the configured budget; this is retained as a limitation for human PRESS review.",
          "evidence": "The corrected broader exposure query retrieved 538,315 records outside the block and a screened 30-record sample contained 0 eligible records, but this sample was drawn before the final outcome block was added. The first malformed probe had zero outside records; a duplicate draw was also left unscreened. The final exposure block explicitly searches cerebral small vessel disease, white matter hyperintensities/lesions, lacunar and silent infarcts, cerebral microbleeds/microhemorrhages, and vascular brain injury."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "6857d1a6f8686b74ce6200ad7ffacb283361236867e8f64de34fd481e0b7d994",
      "note": "same-context closing critic; no separate reviewer context was available",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The query roles remain consistent with the question and eligibility: SVD exposure AND the topic-defining dementia/cognition outcome, with cohort setting and longitudinal design screened."
        },
        "operators": {
          "verdict": "pass",
          "note": "Boolean structure and field tags are valid; no disallowed operators."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The headings are explicit, verified, and exploded."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The missing cognition wording has been added and reevaluated with no technical issues."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No lint or PubMed translation issues remain."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The only bound is the requested Entrez entry-date cutoff; there is no publication-date limit."
        }
      },
      "findings": [
        {
          "id": "outcome-cognition-vocabulary",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "outcome",
          "finding": "The outcome block lacked the bare free-text term cognition and the Cognition MeSH heading.",
          "recommendation": "Add cognition[tiab] and \"Cognition\"[Mesh], run psb eval, and review any resulting probe status or count change.",
          "status": "resolved",
          "response": "Round 2 added both terms and reevaluated the strategy; the resulting count is 7,952 and the optional outcome decision was refreshed."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-59f75d45dd32eaf35a89",
          "status": "accepted-risk",
          "response": "The exposure-category probe is stale because the outcome block was promoted after its draw, and the standard probe allowance was consumed by duplicate draws. The remaining probe cannot be refreshed within the configured budget; this limitation is closed for delivery and retained for human PRESS review.",
          "evidence": "The corrected broader exposure query yielded 538,315 records outside the block and the screened 30-record sample contained 0 eligible records, but it was drawn before the final outcome block was added. The first malformed draw yielded no records and one duplicate draw remained unscreened. The exposure block itself explicitly contains SVD and each named MRI-marker member."
        }
      ]
    }
  ]
}
```

