# PubMed search strategy: audit

Generated 2026-09-28T14:47:57+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In population-based cohorts, is cerebral small vessel disease (and its MRI markers) associated with the risk of incident dementia and cognitive decline?
- Framework: PECO
- Scope confirmed by user: yes (User asked to proceed without clarification; scope roles and assumptions were set from the question. PSB_AS_OF pins the PubMed Entrez-entry-date upper bound at 2017-05-06 for every command, matching protocol as_of; this is an entry-date cutoff, not a publication-date limit. No [dp] limit is used. No known relevant articles were supplied. Standard-depth workload budget is 10,000 records. Population setting and longitudinal design were tested as optional concepts and retained in screening eligibility.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Cerebral small vessel disease and MRI markers | search | The exposure defines the question and must be named or indexed; include the listed MRI marker families by their own terms. |
| Incident dementia, Alzheimer disease, cognitive decline or impairment | optional | Topic-defining outcomes are searchable but may not be named in every abstract; test a broad outcome block before deciding whether to AND it. |
| Population-based/community cohort and longitudinal follow-up | optional | The setting and design are recognizable in some titles/abstracts but incompletely reported; test before considering AND-ing, with eligibility ultimately screened. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T14:46:46+00:00
- Records added to PubMed up to: 2017-05-06
- Total records: 6,837
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Cerebral Small Vessel Diseases[Mesh]` | 6,257 | none |
| 2 | `Cerebrovascular Disorders[Mesh]` | 329,326 | none |
| 3 | `Leukoaraiosis[Mesh]` | 470 | none |
| 4 | `Stroke, Lacunar[Mesh]` | 412 | none |
| 5 | `Brain Infarction[Mesh]` | 34,827 | none |
| 6 | `"cerebral small vessel disease"[tiab:~1]` | 858 | none |
| 7 | `"small-vessel disease"[tiab:~1]` | 2,481 | none |
| 8 | `"small vessel disease"[tiab:~1]` | 2,481 | none |
| 9 | `cerebral microangiopath*[tiab]` | 150 | none |
| 10 | `leukoaraiosis[tiab]` | 1,008 | none |
| 11 | `white matter[tiab] AND hyperintens*[tiab]` | 3,861 | none |
| 12 | `white matter[tiab] AND lesion*[tiab]` | 12,285 | none |
| 13 | `WMH[tiab]` | 1,105 | none |
| 14 | `lacunar infarct*[tiab]` | 2,251 | none |
| 15 | `lacune*[tiab]` | 686 | none |
| 16 | `silent[tiab] AND brain[tiab] AND infarct*[tiab]` | 701 | none |
| 17 | `covert[tiab] AND brain[tiab] AND infarct*[tiab]` | 26 | none |
| 18 | `brain infarct*[tiab]` | 3,534 | none |
| 19 | `cerebral infarct*[tiab]` | 15,197 | none |
| 20 | `cerebral microbleed*[tiab]` | 710 | none |
| 21 | `brain microbleed*[tiab]` | 59 | none |
| 22 | `microbleed*[tiab]` | 1,468 | none |
| 23 | `cerebral microhemorrhag*[tiab]` | 62 | none |
| 24 | `cerebral microhaemorrhag*[tiab]` | 4 | none |
| 25 | `"vascular brain injury"[tiab:~1]` | 129 | none |
| 26 | `"subcortical ischemic vascular disease"[tiab:~1]` | 76 | none |
| 27 | `"subcortical ischaemic vascular disease"[tiab:~1]` | 12 | none |
| 28 | `SIVD[tiab]` | 120 | none |
| 29 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28` | 345,435 | none |
| 30 | `Dementia[Mesh]` | 145,526 | none |
| 31 | `Alzheimer Disease[Mesh]` | 82,140 | none |
| 32 | `Cognition[Mesh]` | 138,866 | none |
| 33 | `Cognition Disorders[Mesh]` | 80,254 | none |
| 34 | `Cognitive Dysfunction[Mesh]` | 8,211 | none |
| 35 | `dementia*[tiab]` | 87,012 | none |
| 36 | `Alzheimer*[tiab]` | 116,181 | none |
| 37 | `cognit*[tiab]` | 298,961 | none |
| 38 | `neurocognit*[tiab]` | 15,280 | none |
| 39 | `"cognitive dysfunction"[tiab:~1]` | 10,427 | none |
| 40 | `"cognitive decline"[tiab:~1]` | 16,066 | none |
| 41 | `"cognitive impairment"[tiab:~1]` | 42,032 | none |
| 42 | `"cognitive deterioration"[tiab:~1]` | 1,933 | none |
| 43 | `"cognitive function"[tiab:~1]` | 26,673 | none |
| 44 | `"mental deterioration"[tiab:~1]` | 1,248 | none |
| 45 | `#30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44` | 544,172 | none |
| 46 | `Cohort Studies[Mesh]` | 1,725,846 | none |
| 47 | `Longitudinal Studies[Mesh]` | 114,265 | none |
| 48 | `Prospective Studies[Mesh]` | 468,312 | none |
| 49 | `Follow-Up Studies[Mesh]` | 586,948 | none |
| 50 | `cohort*[tiab]` | 405,084 | none |
| 51 | `prospective[tiab]` | 453,045 | none |
| 52 | `longitudinal[tiab]` | 189,054 | none |
| 53 | `follow-up[tiab]` | 772,149 | none |
| 54 | `followup[tiab]` | 735,741 | none |
| 55 | `population-based[tiab]` | 100,037 | none |
| 56 | `"population based"[tiab:~1]` | 104,903 | none |
| 57 | `community-based[tiab]` | 46,909 | none |
| 58 | `"community based"[tiab:~1]` | 49,134 | none |
| 59 | `community-dwelling[tiab]` | 16,741 | none |
| 60 | `"community dwelling"[tiab:~1]` | 16,769 | none |
| 61 | `"general population"[tiab:~1]` | 89,351 | none |
| 62 | `"population cohort"[tiab:~1]` | 14,803 | none |
| 63 | `#46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62` | 2,581,241 | none |
| 64 | `#29 AND #45 AND #63` | 6,837 | none |

### Strategy (single line, for copying into PubMed)

```text
((Cerebral Small Vessel Diseases[Mesh] OR Cerebrovascular Disorders[Mesh] OR Leukoaraiosis[Mesh] OR Stroke, Lacunar[Mesh] OR Brain Infarction[Mesh] OR "cerebral small vessel disease"[tiab:~1] OR "small-vessel disease"[tiab:~1] OR "small vessel disease"[tiab:~1] OR cerebral microangiopath*[tiab] OR leukoaraiosis[tiab] OR (white matter[tiab] AND hyperintens*[tiab]) OR (white matter[tiab] AND lesion*[tiab]) OR WMH[tiab] OR lacunar infarct*[tiab] OR lacune*[tiab] OR (silent[tiab] AND brain[tiab] AND infarct*[tiab]) OR (covert[tiab] AND brain[tiab] AND infarct*[tiab]) OR brain infarct*[tiab] OR cerebral infarct*[tiab] OR cerebral microbleed*[tiab] OR brain microbleed*[tiab] OR microbleed*[tiab] OR cerebral microhemorrhag*[tiab] OR cerebral microhaemorrhag*[tiab] OR "vascular brain injury"[tiab:~1] OR "subcortical ischemic vascular disease"[tiab:~1] OR "subcortical ischaemic vascular disease"[tiab:~1] OR SIVD[tiab]) AND (Dementia[Mesh] OR Alzheimer Disease[Mesh] OR Cognition[Mesh] OR Cognition Disorders[Mesh] OR Cognitive Dysfunction[Mesh] OR dementia*[tiab] OR Alzheimer*[tiab] OR cognit*[tiab] OR neurocognit*[tiab] OR "cognitive dysfunction"[tiab:~1] OR "cognitive decline"[tiab:~1] OR "cognitive impairment"[tiab:~1] OR "cognitive deterioration"[tiab:~1] OR "cognitive function"[tiab:~1] OR "mental deterioration"[tiab:~1]) AND (Cohort Studies[Mesh] OR Longitudinal Studies[Mesh] OR Prospective Studies[Mesh] OR Follow-Up Studies[Mesh] OR cohort*[tiab] OR prospective[tiab] OR longitudinal[tiab] OR follow-up[tiab] OR followup[tiab] OR population-based[tiab] OR "population based"[tiab:~1] OR community-based[tiab] OR "community based"[tiab:~1] OR community-dwelling[tiab] OR "community dwelling"[tiab:~1] OR "general population"[tiab:~1] OR "population cohort"[tiab:~1])) AND ("1800/01/01"[edat] : "2017/05/06"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 4 | 4 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Incident dementia, Alzheimer disease, cognitive decline or impairment | AND-ed | 77,683 / 6,837 | 91.2% | none | 0/30 (up to 10% of removed records could be relevant) | Refresh decision against the current query after cohort_setting was added. The outcome block reduces the current exposure-plus-cohort set by more than 90% (measured separately above), loses none of the four benchmark studies, and the refreshed 30-record loss sample contains no eligible record. Retain the block; its loss sample is only an approximate check on a large removed set, so records that omit outcome terms remain a residual risk. |
| Population-based/community cohort and longitudinal follow-up | AND-ed | 25,542 / 6,837 | 73.2% | none | 0/30 (up to 10% of removed records could be relevant) | AND the population/cohort/follow-up block because it cut the outcome-constrained set by 73.2%, lost none of the four screened population-based/community benchmark studies, and none of the 30 screened losses met eligibility. The measured set falls below the standard 10,000-record screening budget. Cohort and setting terms are inconsistent in abstracts, so residual risk remains that eligible community cohorts use none of these labels. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| csd | 88,447 | 0 |
| outcome | 77,683 | 0 |
| cohort_setting | 25,542 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 345,435 | initial | none | Initial recall-first CSVD exposure block with MeSH and MRI marker text terms; add outcome and cohort/setting as optional blocks for empirical testing. Four screened benchmark studies derived from references of a matching prospective WMH systematic review; no seed records. |
| 2 | 25,542 | outcome: +15 / -0 | none | AND outcome block after measured 92.6% reduction, no benchmark loss, and 0/30 eligible records in the loss sample; re-evaluate the remaining cohort-setting candidate against this updated base. |
| 3 | 6,837 | cohort_setting: +17 / -0 | none | AND cohort/setting optional block after updated 73.2% reduction, no benchmark loss, 0/30 eligible in loss sample, and reduction below workload budget; retain exposure/outcome terms unchanged. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 1 findings; F1 must-fix open
- Round 2 on version 3: 1 findings; F1 must-fix resolved
- Round 3 on version 3: 1 findings; F1 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1188 NCBI requests logged (452 from cache); strategy sha256 f848b2b0605b._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [],
    "issues": []
  },
  "vocabulary": [
    {
      "requested": "Cerebral Small Vessel Diseases",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:46:46+00:00",
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
      "checked_at": "2026-09-28T14:46:46+00:00",
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
      "requested": "Leukoaraiosis",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:46:46+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "Leukoaraiosis",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stroke, Lacunar",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:46:46+00:00",
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
      "requested": "Brain Infarction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:46:46+00:00",
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
      "location": "vocabulary:5",
      "term": {
        "text": "Brain Infarction",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Dementia",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:46:46+00:00",
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
      "location": "vocabulary:35",
      "term": {
        "text": "Dementia",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alzheimer Disease",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:46:46+00:00",
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
      "location": "vocabulary:36",
      "term": {
        "text": "Alzheimer Disease",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognition",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:46:46+00:00",
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
      "location": "vocabulary:37",
      "term": {
        "text": "Cognition",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognition Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:46:46+00:00",
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
      "location": "vocabulary:38",
      "term": {
        "text": "Cognition Disorders",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognitive Dysfunction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:46:46+00:00",
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
      "location": "vocabulary:39",
      "term": {
        "text": "Cognitive Dysfunction",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cohort Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:46:46+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D015331",
          "name": "Cohort Studies",
          "type": "descriptor",
          "scope_note": "Studies in which subsets of a defined population are identified. These groups may or may not be exposed to factors hypothesized to influence the probability of the occurrence of a particular disease or other outcome. Cohorts are defined populations which, as a whole, are followed in an attempt to determine distinguishing subgroup characteristics.",
          "tree_numbers": [
            "E05.318.372.500.750",
            "N05.715.360.330.500.750",
            "N06.850.520.450.500.750"
          ],
          "entry_terms": 33,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D015331",
      "preferred_label": "Cohort Studies",
      "type": "descriptor",
      "location": "vocabulary:50",
      "term": {
        "text": "Cohort Studies",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Longitudinal Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:46:46+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D008137",
          "name": "Longitudinal Studies",
          "type": "descriptor",
          "scope_note": "Studies in which variables relating to an individual or group of individuals are assessed over a period of time.",
          "tree_numbers": [
            "E05.318.372.500.750.500",
            "N05.715.360.330.500.750.500",
            "N06.850.520.450.500.750.500"
          ],
          "entry_terms": 32,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D008137",
      "preferred_label": "Longitudinal Studies",
      "type": "descriptor",
      "location": "vocabulary:51",
      "term": {
        "text": "Longitudinal Studies",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Prospective Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:46:46+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011446",
          "name": "Prospective Studies",
          "type": "descriptor",
          "scope_note": "Observation of a population for a sufficient number of persons over a sufficient number of years to generate incidence or mortality rates subsequent to the selection of the study group.",
          "tree_numbers": [
            "E05.318.372.500.750.625",
            "N05.715.360.330.500.750.650",
            "N06.850.520.450.500.750.650"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011446",
      "preferred_label": "Prospective Studies",
      "type": "descriptor",
      "location": "vocabulary:52",
      "term": {
        "text": "Prospective Studies",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Follow-Up Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:46:46+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D005500",
          "name": "Follow-Up Studies",
          "type": "descriptor",
          "scope_note": "Studies in which individuals or populations are followed to assess the outcome of exposures, procedures, or effects of a characteristic, e.g., occurrence of disease.",
          "tree_numbers": [
            "E05.318.372.500.750.249",
            "N05.715.360.330.500.750.350",
            "N06.850.520.450.500.750.350"
          ],
          "entry_terms": 8,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D005500",
      "preferred_label": "Follow-Up Studies",
      "type": "descriptor",
      "location": "vocabulary:53",
      "term": {
        "text": "Follow-Up Studies",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"cerebral small vessel diseases\"[MeSH Terms] OR \"cerebrovascular disorders\"[MeSH Terms] OR \"leukoaraiosis\"[MeSH Terms] OR \"stroke, lacunar\"[MeSH Terms] OR \"brain infarction\"[MeSH Terms] OR \"cerebral small vessel disease\"[Title/Abstract:~1] OR \"small-vessel disease\"[Title/Abstract:~1] OR \"small-vessel disease\"[Title/Abstract:~1] OR \"cerebral microangiopath*\"[Title/Abstract] OR \"leukoaraiosis\"[Title/Abstract] OR (\"white matter\"[Title/Abstract] AND \"hyperintens*\"[Title/Abstract]) OR (\"white matter\"[Title/Abstract] AND \"lesion*\"[Title/Abstract]) OR \"WMH\"[Title/Abstract] OR \"lacunar infarct*\"[Title/Abstract] OR \"lacune*\"[Title/Abstract] OR (\"silent\"[Title/Abstract] AND \"brain\"[Title/Abstract] AND \"infarct*\"[Title/Abstract]) OR (\"covert\"[Title/Abstract] AND \"brain\"[Title/Abstract] AND \"infarct*\"[Title/Abstract]) OR \"brain infarct*\"[Title/Abstract] OR \"cerebral infarct*\"[Title/Abstract] OR \"cerebral microbleed*\"[Title/Abstract] OR \"brain microbleed*\"[Title/Abstract] OR \"microbleed*\"[Title/Abstract] OR \"cerebral microhemorrhag*\"[Title/Abstract] OR \"cerebral microhaemorrhag*\"[Title/Abstract] OR \"vascular brain injury\"[Title/Abstract:~1] OR \"subcortical ischemic vascular disease\"[Title/Abstract:~1] OR \"subcortical ischaemic vascular disease\"[Title/Abstract:~1] OR \"SIVD\"[Title/Abstract]) AND (\"dementia\"[MeSH Terms] OR \"alzheimer disease\"[MeSH Terms] OR \"cognition\"[MeSH Terms] OR \"cognition disorders\"[MeSH Terms] OR \"cognitive dysfunction\"[MeSH Terms] OR \"dementia*\"[Title/Abstract] OR \"alzheimer*\"[Title/Abstract] OR \"cognit*\"[Title/Abstract] OR \"neurocognit*\"[Title/Abstract] OR \"cognitive dysfunction\"[Title/Abstract:~1] OR \"cognitive decline\"[Title/Abstract:~1] OR \"cognitive impairment\"[Title/Abstract:~1] OR \"cognitive deterioration\"[Title/Abstract:~1] OR \"cognitive function\"[Title/Abstract:~1] OR \"mental deterioration\"[Title/Abstract:~1]) AND (\"cohort studies\"[MeSH Terms] OR \"longitudinal studies\"[MeSH Terms] OR \"prospective studies\"[MeSH Terms] OR \"follow up studies\"[MeSH Terms] OR \"cohort*\"[Title/Abstract] OR \"prospective\"[Title/Abstract] OR \"longitudinal\"[Title/Abstract] OR \"follow-up\"[Title/Abstract] OR \"followup\"[Title/Abstract] OR \"population-based\"[Title/Abstract] OR \"population-based\"[Title/Abstract:~1] OR \"community-based\"[Title/Abstract] OR \"community-based\"[Title/Abstract:~1] OR \"community-dwelling\"[Title/Abstract] OR \"community-dwelling\"[Title/Abstract:~1] OR \"general population\"[Title/Abstract:~1] OR \"population cohort\"[Title/Abstract:~1]) AND 1800/01/01:2017/05/06[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "fe5b47e807a324684ece6f46aa9978011c1781610f4a4e2adcbce28029a22904",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure block includes the named small-vessel disease and MRI marker families. No phrase warnings are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three blocks are OR-combined internally and AND-ed consistently with the documented decisions. The optional-block loss samples and residual risks are reported."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes relevant disease, outcome, and study-design headings; the packet reports no heading diagnostics."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Title/abstract terms cover the listed exposure markers and outcomes, including spelling variants for microhemorrhage and ischemia."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported PubMed translation has no syntax errors or warnings. Proximity expressions contain no wildcards."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The executed query applies an entry-date range ending 2017-05-06, although the protocol specifies no date restriction and the strategy input lists no limits. This excludes later records from the stated search question."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The executed query ends with AND (\"1800/01/01\"[edat] : \"2017/05/06\"[edat]). No date cutoff appears in the question, eligibility criteria, or documented strategy limits. Records entered after 2017-05-06 are excluded.",
          "recommendation": "Remove the entry-date restriction unless a cutoff is part of the review protocol. If the cutoff is intentional, document its rationale and revise the question and protocol; then rerun the complete evaluation against the intended date range.",
          "status": "open",
          "response": ""
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "c326d86fba931250f36dacca78bcff8946ed75fb00efa00cfbdd7f6dac45a460",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure block covers cerebral small vessel disease and the named MRI marker families. Outcome terms cover dementia, Alzheimer disease, cognitive decline, and impairment; cohort, setting, and follow-up terms are also present."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are OR-combined within blocks, and the outcome and cohort-setting blocks are AND-ed as supported by the reported reductions, benchmark checks, and loss samples. Residual risk from records omitting those terms is documented."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Relevant disease, MRI marker, outcome, and study-design headings are included. The packet reports no heading diagnostics."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Title/abstract terms cover the named exposure markers and outcomes, including ischemia and microhemorrhage spelling variants."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no syntax errors or warnings. Proximity expressions contain no wildcards."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The executed entry-date range ends on 2017-05-06, matching the protocol as_of date recorded in the packet. The earlier concern that this cutoff was undocumented is resolved."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The executed query ends with an entry-date range ending 2017-05-06.",
          "recommendation": "Remove the entry-date restriction unless a cutoff is part of the review protocol; if intentional, document its rationale and rerun the complete evaluation against the intended date range.",
          "status": "resolved",
          "response": "The packet documents that PSB_AS_OF pins the PubMed Entrez-entry-date upper bound at 2017-05-06 for every command, matching the protocol as_of date. The cutoff is therefore part of the documented protocol, is required by the harness, and is not a publication-date limit."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "c326d86fba931250f36dacca78bcff8946ed75fb00efa00cfbdd7f6dac45a460",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure block includes the named small-vessel disease and MRI marker families, and the outcome block covers dementia, Alzheimer disease, cognitive decline, and impairment. Cohort, setting, and follow-up terms are included. The packet reports no phrase warnings."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are OR-combined within blocks, and the outcome and cohort-setting blocks are AND-ed based on the reported reductions, benchmark retrieval, and loss samples. Residual risk from eligible records omitting those terms is documented."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Relevant disease, MRI marker, outcome, and study-design headings are included. The packet reports no heading diagnostics."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Title and abstract terms cover the named exposure markers and outcomes, including ischemia and microhemorrhage spelling variants."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no syntax errors or warnings. Proximity expressions contain no wildcards."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez entry-date range ends on 2017-05-06, matching the documented protocol as_of date. The packet states this is an entry-date cutoff, not a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The executed query uses an Entrez entry-date range ending 2017-05-06.",
          "recommendation": "Remove the entry-date restriction unless it is part of the review protocol; if intentional, document its rationale and rerun the complete evaluation against the intended date range.",
          "status": "resolved",
          "response": "The current packet documents protocol as_of as 2017-05-06 and states that PSB_AS_OF applies this Entrez entry-date upper bound to every command. It also clarifies that this is not a publication-date limit. This resolves the earlier concern that the cutoff was undocumented."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

