# PubMed search strategy: audit

Generated 2026-09-28T14:11:41+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In population-based cohorts, is cerebral small vessel disease (and its MRI markers) associated with the risk of incident dementia and cognitive decline?
- Framework: PECO
- Scope confirmed by user: yes (User asked not to pause for questions. Scope roles proceeded on the stated question: PECO; CSVD/MRI markers searched; dementia/cognitive outcome and population/community setting tested as optional searchable concepts; longitudinal follow-up screened. Both optional blocks were moved into the query after their current versions retained all five benchmark articles, reduced counts materially, and had no eligible records in their 30-record random loss samples. No known articles supplied. Standard depth defaults used; PubMed constrained by Entrez date as_of 2017-05-06 per harness, without a publication-date limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Cerebral small vessel disease and MRI markers | search | The exposure defines the question and its named MRI markers are searchable, central terms. |
| Incident dementia, Alzheimer disease, cognitive decline or impairment | optional | The outcome defines the review topic and is searchable, but abstract reporting can be inconsistent; test the retrieval reduction and loss sample before deciding whether to AND it. |
| Population-based, community-dwelling cohorts | optional | The target population/setting is a named and searchable concept, often stated in abstracts, so test it against the outcome-filtered set and a loss sample before deciding whether to require it. |
| Prospective cohort / longitudinal observational follow-up | screen | Follow-up design is an eligibility property; avoid an ad hoc design filter that risks missing eligible studies. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T14:10:09+00:00
- Records added to PubMed up to: 2017-05-06
- Total records: 8,199
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Cerebral Small Vessel Diseases"[Mesh]` | 6,257 | none |
| 2 | `"Cerebrovascular Disorders"[Mesh]` | 329,326 | none |
| 3 | `"Leukoaraiosis"[Mesh]` | 470 | none |
| 4 | `"Stroke, Lacunar"[Mesh]` | 412 | none |
| 5 | `"Cerebral Infarction"[Mesh]` | 29,744 | none |
| 6 | `"Cerebral Hemorrhage"[Mesh]` | 31,304 | none |
| 7 | `"cerebral small vessel disease"[tiab]` | 813 | none |
| 8 | `"cerebral small vessel diseases"[tiab]` | 105 | none |
| 9 | `"small vessel disease"[tiab]` | 2,316 | none |
| 10 | `"small vessel diseases"[tiab]` | 203 | none |
| 11 | `"small vessel ischemic disease"[tiab]` | 15 | none |
| 12 | `"small vessel ischaemic disease"[tiab]` | 3 | none |
| 13 | `microangiopath*[tiab]` | 8,590 | none |
| 14 | `"subcortical ischemic vascular disease"[tiab]` | 60 | none |
| 15 | `"subcortical ischaemic vascular disease"[tiab]` | 12 | none |
| 16 | `Binswanger*[tiab]` | 570 | none |
| 17 | `leukoaraiosis[tiab]` | 1,008 | none |
| 18 | `leukoencephalopath*[tiab]` | 6,366 | none |
| 19 | `"white matter hyperintens*"[tiab]` | 2,354 | none |
| 20 | `hyperintens*[tiab]` | 12,104 | none |
| 21 | `"white matter lesion*"[tiab]` | 4,051 | none |
| 22 | `"white matter change*"[tiab]` | 1,880 | none |
| 23 | `"white matter abnormalit*"[tiab]` | 1,590 | none |
| 24 | `"white matter disease"[tiab]` | 813 | none |
| 25 | `"white matter diseases"[tiab]` | 153 | none |
| 26 | `"silent brain infarct*"[tiab]` | 280 | none |
| 27 | `"silent cerebral infarct*"[tiab]` | 322 | none |
| 28 | `"asymptomatic brain infarct*"[tiab]` | 15 | none |
| 29 | `"asymptomatic cerebral infarct*"[tiab]` | 63 | none |
| 30 | `"lacunar infarct*"[tiab]` | 2,251 | none |
| 31 | `lacune*[tiab]` | 686 | none |
| 32 | `"cerebral microbleed*"[tiab]` | 710 | none |
| 33 | `"brain microbleed*"[tiab]` | 59 | none |
| 34 | `"cerebral microhemorrhag*"[tiab]` | 62 | none |
| 35 | `"cerebral microhaemorrhag*"[tiab]` | 4 | none |
| 36 | `"vascular brain injur*"[tiab]` | 77 | none |
| 37 | `injur*[tiab]` | 687,100 | none |
| 38 | `"vascular brain lesion*"[tiab]` | 74 | none |
| 39 | `"cerebral small vessel"[tiab:~2]` | 1,011 | none |
| 40 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39` | 1,013,074 | none |
| 41 | `"Dementia"[Mesh]` | 145,526 | none |
| 42 | `"Alzheimer Disease"[Mesh]` | 82,140 | none |
| 43 | `"Cognitive Dysfunction"[Mesh]` | 8,211 | none |
| 44 | `"Cognition Disorders"[Mesh]` | 80,254 | none |
| 45 | `"Neuropsychological Tests"[Mesh]` | 161,667 | none |
| 46 | `dementia[tiab]` | 85,598 | none |
| 47 | `dementias[tiab]` | 4,177 | none |
| 48 | `"Alzheimer disease"[tiab]` | 102,114 | none |
| 49 | `"Alzheimer's disease"[tiab]` | 92,248 | none |
| 50 | `"Alzheimer dementia"[tiab]` | 1,886 | none |
| 51 | `"vascular dementia"[tiab]` | 5,404 | none |
| 52 | `"cognitive decline"[tiab]` | 15,036 | none |
| 53 | `"cognitive deterioration"[tiab]` | 1,471 | none |
| 54 | `"cognitive impairment"[tiab]` | 40,821 | none |
| 55 | `"cognitive dysfunction"[tiab]` | 9,912 | none |
| 56 | `"cognitive disorder"[tiab]` | 561 | none |
| 57 | `"cognitive disorders"[tiab]` | 2,955 | none |
| 58 | `"cognitive function"[tiab]` | 25,869 | none |
| 59 | `"cognitive functioning"[tiab]` | 10,032 | none |
| 60 | `"cognitive performance"[tiab]` | 13,653 | none |
| 61 | `"cognitive change"[tiab]` | 1,183 | none |
| 62 | `"cognitive changes"[tiab]` | 2,220 | none |
| 63 | `"cognitive trajectory"[tiab]` | 58 | none |
| 64 | `"cognitive trajectories"[tiab]` | 129 | none |
| 65 | `"mild cognitive impairment"[tiab]` | 11,353 | none |
| 66 | `"neurocognitive decline"[tiab]` | 248 | none |
| 67 | `"neurocognitive disorder"[tiab]` | 451 | none |
| 68 | `"cognitive test"[tiab]` | 1,983 | none |
| 69 | `"cognitive tests"[tiab]` | 3,669 | none |
| 70 | `"cognitive testing"[tiab]` | 1,915 | none |
| 71 | `"neuropsychological test"[tiab]` | 4,059 | none |
| 72 | `"neuropsychological tests"[tiab]` | 7,068 | none |
| 73 | `#41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72` | 407,114 | none |
| 74 | `"Cohort Studies"[Mesh]` | 1,725,846 | none |
| 75 | `"Longitudinal Studies"[Mesh]` | 114,265 | none |
| 76 | `"Prospective Studies"[Mesh]` | 468,312 | none |
| 77 | `"community-based"[tiab]` | 46,909 | none |
| 78 | `"community based"[tiab]` | 46,909 | none |
| 79 | `"community-dwelling"[tiab]` | 16,741 | none |
| 80 | `"community dwelling"[tiab]` | 16,741 | none |
| 81 | `"population-based"[tiab]` | 100,037 | none |
| 82 | `"population based"[tiab]` | 100,037 | none |
| 83 | `"population-based study"[tiab]` | 23,007 | none |
| 84 | `"general population"[tiab]` | 80,605 | none |
| 85 | `"population cohort"[tiab]` | 1,176 | none |
| 86 | `"community cohort"[tiab]` | 682 | none |
| 87 | `"community cohorts"[tiab]` | 62 | none |
| 88 | `"population cohorts"[tiab]` | 316 | none |
| 89 | `#74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81 OR #82 OR #83 OR #84 OR #85 OR #86 OR #87 OR #88` | 1,895,416 | none |
| 90 | `#40 AND #73 AND #89` | 8,199 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Cerebral Small Vessel Diseases"[Mesh] OR "Cerebrovascular Disorders"[Mesh] OR "Leukoaraiosis"[Mesh] OR "Stroke, Lacunar"[Mesh] OR "Cerebral Infarction"[Mesh] OR "Cerebral Hemorrhage"[Mesh] OR "cerebral small vessel disease"[tiab] OR "cerebral small vessel diseases"[tiab] OR "small vessel disease"[tiab] OR "small vessel diseases"[tiab] OR "small vessel ischemic disease"[tiab] OR "small vessel ischaemic disease"[tiab] OR microangiopath*[tiab] OR "subcortical ischemic vascular disease"[tiab] OR "subcortical ischaemic vascular disease"[tiab] OR Binswanger*[tiab] OR leukoaraiosis[tiab] OR leukoencephalopath*[tiab] OR "white matter hyperintens*"[tiab] OR hyperintens*[tiab] OR "white matter lesion*"[tiab] OR "white matter change*"[tiab] OR "white matter abnormalit*"[tiab] OR "white matter disease"[tiab] OR "white matter diseases"[tiab] OR "silent brain infarct*"[tiab] OR "silent cerebral infarct*"[tiab] OR "asymptomatic brain infarct*"[tiab] OR "asymptomatic cerebral infarct*"[tiab] OR "lacunar infarct*"[tiab] OR lacune*[tiab] OR "cerebral microbleed*"[tiab] OR "brain microbleed*"[tiab] OR "cerebral microhemorrhag*"[tiab] OR "cerebral microhaemorrhag*"[tiab] OR "vascular brain injur*"[tiab] OR injur*[tiab] OR "vascular brain lesion*"[tiab] OR "cerebral small vessel"[tiab:~2]) AND ("Dementia"[Mesh] OR "Alzheimer Disease"[Mesh] OR "Cognitive Dysfunction"[Mesh] OR "Cognition Disorders"[Mesh] OR "Neuropsychological Tests"[Mesh] OR dementia[tiab] OR dementias[tiab] OR "Alzheimer disease"[tiab] OR "Alzheimer's disease"[tiab] OR "Alzheimer dementia"[tiab] OR "vascular dementia"[tiab] OR "cognitive decline"[tiab] OR "cognitive deterioration"[tiab] OR "cognitive impairment"[tiab] OR "cognitive dysfunction"[tiab] OR "cognitive disorder"[tiab] OR "cognitive disorders"[tiab] OR "cognitive function"[tiab] OR "cognitive functioning"[tiab] OR "cognitive performance"[tiab] OR "cognitive change"[tiab] OR "cognitive changes"[tiab] OR "cognitive trajectory"[tiab] OR "cognitive trajectories"[tiab] OR "mild cognitive impairment"[tiab] OR "neurocognitive decline"[tiab] OR "neurocognitive disorder"[tiab] OR "cognitive test"[tiab] OR "cognitive tests"[tiab] OR "cognitive testing"[tiab] OR "neuropsychological test"[tiab] OR "neuropsychological tests"[tiab]) AND ("Cohort Studies"[Mesh] OR "Longitudinal Studies"[Mesh] OR "Prospective Studies"[Mesh] OR "community-based"[tiab] OR "community based"[tiab] OR "community-dwelling"[tiab] OR "community dwelling"[tiab] OR "population-based"[tiab] OR "population based"[tiab] OR "population-based study"[tiab] OR "general population"[tiab] OR "population cohort"[tiab] OR "community cohort"[tiab] OR "community cohorts"[tiab] OR "population cohorts"[tiab])) AND ("1800/01/01"[edat] : "2017/05/06"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 5 | 5 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Incident dementia, Alzheimer disease, cognitive decline or impairment | AND-ed | 151,287 / 8,199 | 94.6% | none | 0/30 (up to 10% of removed records could be relevant) | Reaffirm the outcome block on the current query: the base without outcomes is 151,287 records and the block yields 8,199 (94.6% reduction); all 5 benchmark cohorts remain retrieved and none of the 30 updated random losses met eligibility on title/abstract screening. |
| Population-based, community-dwelling cohorts | AND-ed | 40,408 / 8,199 | 79.7% | none | 0/30 (up to 10% of removed records could be relevant) | Reaffirm the population/cohort block on the current query: it reduces 40,408 to 8,199 records (79.7%), retains all 5 benchmark cohorts, and none of the updated 30 random losses met eligibility on title/abstract screening. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| csvd | 60,655 | 0 |
| cognitive_outcomes | 151,287 | 0 |
| population | 40,408 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 350,580 | initial | none | Initial recall-first exposure block with explicit MeSH plus marker terminology; dementia/cognitive outcome included as an optional candidate block for empirical loss testing. Added a five-record benchmark screened from an in-scope prior longitudinal WMH review. |
| 2 | 350,580 | limits/combination | none | Removed a duplicate microbleed text term flagged by lint; retained broad exposure indexing pending measured optional-outcome decision. |
| 3 | 21,296 | cognitive_outcomes: +28 / -0 | none | Accepted the tested outcome block based on 93.9% reduction, full benchmark retention, and 0 eligible studies among 30 sampled losses; added population/community setting as a second optional concept for testing because authors often name it. |
| 4 | 25,081 | cognitive_outcomes: +6 / -2 | none | Corrected a noncanonical MeSH label for mild cognitive impairment; replaced a quoted truncation phrase with exact singular/plural cognitive and neuropsychological test phrases. Added cohort/prospective/longitudinal study MeSH to the optional population-setting candidate for testing. |
| 5 | 5,269 | population: +15 / -0 | none | Current population-setting optional block passed the sample/no-loss/material-reduction criteria after adding the relevant cohort/longitudinal/prospective MeSH layer; moved it into the query alongside outcomes. |
| 6 | 8,199 | csvd: +2 / -0 | none | Addressed critic R1-F1 by testing bare-name hyperintens*[tiab] and injur*[tiab] terms while retaining the existing marker phrases; checked current benchmark retrieval and optional-block status. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5: 2 findings; R1-F1 should-fix open, R1-F2 should-fix open
- Round 2 on version 6: 2 findings; R1-F1 should-fix resolved, R1-F2 should-fix resolved
- Round 3 on version 6: 2 findings; R1-F1 should-fix resolved, R1-F2 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1487 NCBI requests logged (699 from cache); strategy sha256 c0a86b32d794._

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
      "checked_at": "2026-09-28T14:10:09+00:00",
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
      "requested": "Cerebrovascular Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:10:09+00:00",
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
        "text": "\"Cerebrovascular Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Leukoaraiosis",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:10:09+00:00",
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
        "text": "\"Leukoaraiosis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stroke, Lacunar",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:10:09+00:00",
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
        "text": "\"Stroke, Lacunar\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cerebral Infarction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:10:09+00:00",
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
      "location": "vocabulary:5",
      "term": {
        "text": "\"Cerebral Infarction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cerebral Hemorrhage",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:10:09+00:00",
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
      "location": "vocabulary:6",
      "term": {
        "text": "\"Cerebral Hemorrhage\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Dementia",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:10:09+00:00",
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
      "location": "vocabulary:40",
      "term": {
        "text": "\"Dementia\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alzheimer Disease",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:10:09+00:00",
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
      "location": "vocabulary:41",
      "term": {
        "text": "\"Alzheimer Disease\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognitive Dysfunction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:10:09+00:00",
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
      "location": "vocabulary:42",
      "term": {
        "text": "\"Cognitive Dysfunction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognition Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:10:09+00:00",
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
      "location": "vocabulary:43",
      "term": {
        "text": "\"Cognition Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Neuropsychological Tests",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:10:09+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D009483",
          "name": "Neuropsychological Tests",
          "type": "descriptor",
          "scope_note": "Tests designed to assess neurological function associated with certain behaviors. They are used in diagnosing brain dysfunction or damage and central nervous system disorders or injury.",
          "tree_numbers": [
            "F04.711.513"
          ],
          "entry_terms": 33,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D009483",
      "preferred_label": "Neuropsychological Tests",
      "type": "descriptor",
      "location": "vocabulary:44",
      "term": {
        "text": "\"Neuropsychological Tests\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cohort Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:10:09+00:00",
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
      "location": "vocabulary:72",
      "term": {
        "text": "\"Cohort Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Longitudinal Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:10:09+00:00",
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
      "location": "vocabulary:73",
      "term": {
        "text": "\"Longitudinal Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Prospective Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T14:10:09+00:00",
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
      "location": "vocabulary:74",
      "term": {
        "text": "\"Prospective Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Cerebral Small Vessel Diseases\"[MeSH Terms] OR \"Cerebrovascular Disorders\"[MeSH Terms] OR \"Leukoaraiosis\"[MeSH Terms] OR \"stroke, lacunar\"[MeSH Terms] OR \"Cerebral Infarction\"[MeSH Terms] OR \"Cerebral Hemorrhage\"[MeSH Terms] OR \"cerebral small vessel disease\"[Title/Abstract] OR \"Cerebral Small Vessel Diseases\"[Title/Abstract] OR \"small vessel disease\"[Title/Abstract] OR \"small vessel diseases\"[Title/Abstract] OR \"small vessel ischemic disease\"[Title/Abstract] OR \"small vessel ischaemic disease\"[Title/Abstract] OR \"microangiopath*\"[Title/Abstract] OR \"subcortical ischemic vascular disease\"[Title/Abstract] OR \"subcortical ischaemic vascular disease\"[Title/Abstract] OR \"binswanger*\"[Title/Abstract] OR \"Leukoaraiosis\"[Title/Abstract] OR \"leukoencephalopath*\"[Title/Abstract] OR \"white matter hyperintens*\"[Title/Abstract] OR \"hyperintens*\"[Title/Abstract] OR \"white matter lesion*\"[Title/Abstract] OR \"white matter change*\"[Title/Abstract] OR \"white matter abnormalit*\"[Title/Abstract] OR \"white matter disease\"[Title/Abstract] OR \"white matter diseases\"[Title/Abstract] OR \"silent brain infarct*\"[Title/Abstract] OR \"silent cerebral infarct*\"[Title/Abstract] OR \"asymptomatic brain infarct*\"[Title/Abstract] OR \"asymptomatic cerebral infarct*\"[Title/Abstract] OR \"lacunar infarct*\"[Title/Abstract] OR \"lacune*\"[Title/Abstract] OR \"cerebral microbleed*\"[Title/Abstract] OR \"brain microbleed*\"[Title/Abstract] OR \"cerebral microhemorrhag*\"[Title/Abstract] OR \"cerebral microhaemorrhag*\"[Title/Abstract] OR \"vascular brain injur*\"[Title/Abstract] OR \"injur*\"[Title/Abstract] OR \"vascular brain lesion*\"[Title/Abstract] OR \"cerebral small vessel\"[Title/Abstract:~2]) AND (\"Dementia\"[MeSH Terms] OR \"alzheimer disease\"[MeSH Terms] OR \"Cognitive Dysfunction\"[MeSH Terms] OR \"Cognition Disorders\"[MeSH Terms] OR \"Neuropsychological Tests\"[MeSH Terms] OR \"Dementia\"[Title/Abstract] OR \"dementias\"[Title/Abstract] OR \"alzheimer disease\"[Title/Abstract] OR \"Alzheimer's disease\"[Title/Abstract] OR \"Alzheimer dementia\"[Title/Abstract] OR \"vascular dementia\"[Title/Abstract] OR \"cognitive decline\"[Title/Abstract] OR \"cognitive deterioration\"[Title/Abstract] OR \"cognitive impairment\"[Title/Abstract] OR \"Cognitive Dysfunction\"[Title/Abstract] OR \"cognitive disorder\"[Title/Abstract] OR \"cognitive disorders\"[Title/Abstract] OR \"cognitive function\"[Title/Abstract] OR \"cognitive functioning\"[Title/Abstract] OR \"cognitive performance\"[Title/Abstract] OR \"cognitive change\"[Title/Abstract] OR \"cognitive changes\"[Title/Abstract] OR \"cognitive trajectory\"[Title/Abstract] OR \"cognitive trajectories\"[Title/Abstract] OR \"mild cognitive impairment\"[Title/Abstract] OR \"neurocognitive decline\"[Title/Abstract] OR \"neurocognitive disorder\"[Title/Abstract] OR \"cognitive test\"[Title/Abstract] OR \"cognitive tests\"[Title/Abstract] OR \"cognitive testing\"[Title/Abstract] OR \"neuropsychological test\"[Title/Abstract] OR \"Neuropsychological Tests\"[Title/Abstract]) AND (\"Cohort Studies\"[MeSH Terms] OR \"Longitudinal Studies\"[MeSH Terms] OR \"Prospective Studies\"[MeSH Terms] OR \"community-based\"[Title/Abstract] OR \"community-based\"[Title/Abstract] OR \"community-dwelling\"[Title/Abstract] OR \"community-dwelling\"[Title/Abstract] OR \"population-based\"[Title/Abstract] OR \"population-based\"[Title/Abstract] OR \"population-based study\"[Title/Abstract] OR \"general population\"[Title/Abstract] OR \"population cohort\"[Title/Abstract] OR \"community cohort\"[Title/Abstract] OR \"community cohorts\"[Title/Abstract] OR \"population cohorts\"[Title/Abstract]) AND 1800/01/01:2017/05/06[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "f1a6e2c90386f8302b15ecea1a2b69936684aa939b1710bb5612c86921ce71e9",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The instructions require each named member of a searched concept to be covered by its own bare name. The exposure block uses parent-qualified phrases such as white matter hyperintens* and vascular brain injur*; it does not test bare hyperintens* or injur* terms. Test appropriate bare-name variants while retaining the existing phrases."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three blocks are combined with AND, consistent with the stated PECO scope and optional-concept testing."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet includes relevant CSVD, cerebrovascular, dementia, cognitive, and cohort or longitudinal MeSH headings. No heading translation errors are reported."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add and test bare-name variants for the explicitly named MRI markers that currently appear only in parent-qualified phrases; preserve the current phrase terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed query and field syntax have no reported errors; the proximity term has no wildcard, and its warning is explicitly documented."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The outcome block is marked stale, and its rationale says the reduction is about 94% while the reported counts show 91.4%. Reconcile the status and rationale with the current evaluation before relying on the optional-block decision."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The eligibility names white matter hyperintensity and vascular brain injury as exposure markers, but the corresponding text-word terms are parent-qualified phrases. The packet's translation check requires a named member to be covered by its own bare name, not solely through a phrase containing the parent's wording.",
          "recommendation": "Test bare-name variants such as hyperintens*[tiab] and injur*[tiab], retain the existing phrases, and document retrieval and relevance before deciding whether to include them.",
          "status": "open"
        },
        {
          "id": "R1-F2",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The outcome optional concept is labeled stale. Its reason says the block reduces results by about 94%, whereas the table and evidence report 61,128 without the block and 5,269 with it, a 91.4% reduction.",
          "recommendation": "Reconcile the stale status and correct the reduction rationale against the current tested counts and loss-sample evidence before treating the outcome block decision as current.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 6,
      "review_sha256": "2875f4f7359d2a4ae9ca8dac22eddc1601665e8a778742033935aa98a2ae559f",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure block now includes the bare-name terms hyperintens*[tiab] and injur*[tiab], while retaining the more specific phrases. The named exposure markers and cognitive outcomes are represented."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three concept blocks are combined with AND. The outcome and population blocks were tested as optional concepts before being retained."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes relevant headings for CSVD and cerebrovascular conditions, dementia and cognition, and cohort and longitudinal study designs. No heading translation errors are reported."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word block covers the named MRI markers and cognitive outcomes, including the bare-name variants required by the translation check."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax errors or PubMed warnings are reported. The proximity expression has no wildcard."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The current evidence reports the outcome block reducing 151,287 records to 8,199 (94.6%) and the population block reducing 40,408 to 8,199 (79.7%). Both retain all five benchmarks, and neither updated 30-record loss sample contained a relevant record."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier review found that named MRI markers appeared only in parent-qualified phrases, without bare-name terms.",
          "recommendation": "Add and test bare-name variants while retaining the existing phrases.",
          "status": "resolved",
          "response": "Resolved in the current strategy: hyperintens*[tiab] and injur*[tiab] were added, and the complete strategy was evaluated with those terms."
        },
        {
          "id": "R1-F2",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The earlier review found a stale outcome-block status and a reduction rationale inconsistent with the reported counts.",
          "recommendation": "Reconcile the status and rationale with current counts and loss-sample evidence.",
          "status": "resolved",
          "response": "Resolved in the current packet: the outcome block is reaffirmed using current counts of 151,287 without the block and 8,199 with it, a 94.6% reduction, with all five benchmarks retained and 0/30 relevant records in the updated loss sample."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 6,
      "review_sha256": "2875f4f7359d2a4ae9ca8dac22eddc1601665e8a778742033935aa98a2ae559f",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure block now includes the bare-name terms hyperintens*[tiab] and injur*[tiab], retaining the more specific phrases. All five benchmark cohorts are retrieved."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three concept blocks are combined with AND; the outcome and population blocks were tested as optional concepts before being retained."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes headings for CSVD and cerebrovascular conditions, dementia and cognition, and cohort and longitudinal designs. No heading translation errors are reported."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word terms cover the named MRI markers and cognitive outcomes, including the required bare-name exposure terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax errors, PubMed warnings, or translation issues are reported. The proximity expression has no wildcard."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Current evidence reports the outcome block reducing 151,287 records to 8,199 (94.6%) and the population block reducing 40,408 to 8,199 (79.7%). Both retain all five benchmarks, and neither updated 30-record loss sample contained an eligible record."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier review found that named MRI markers appeared only in parent-qualified phrases, without bare-name terms.",
          "recommendation": "Add and test bare-name variants while retaining the existing phrases.",
          "status": "resolved",
          "response": "Resolved in the current strategy: hyperintens*[tiab] and injur*[tiab] are present alongside the existing phrases, and the complete strategy was evaluated with those terms."
        },
        {
          "id": "R1-F2",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The earlier review found a stale outcome-block status and a reduction rationale inconsistent with the reported counts.",
          "recommendation": "Reconcile the status and rationale with current counts and loss-sample evidence.",
          "status": "resolved",
          "response": "Resolved in the current packet: the outcome block is reaffirmed at 151,287 records without the block and 8,199 with it, a 94.6% reduction; all five benchmarks remain retrieved and the updated loss sample contains 0/30 relevant records."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

