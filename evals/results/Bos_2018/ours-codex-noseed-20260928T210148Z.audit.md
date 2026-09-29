# PubMed search strategy: audit

Generated 2026-09-28T21:25:11+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In population-based cohorts, is cerebral small vessel disease (and its MRI markers) associated with the risk of incident dementia and cognitive decline?
- Framework: PECO / prognosis
- Scope confirmed by user: yes (User has no known relevant articles and cannot answer questions during this run; proceeded with standard depth and no further clarification. Scope roles were set from the question before record discovery. No language, publication-date, age, or study-design limit. PSB_AS_OF=2017-05-06 is an Entrez-date bound; no [dp] cutoff. With no known records, recall cannot be estimated and the strategy will be empirically unvalidated unless screened discoveries support a limited development check.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Cerebral small vessel disease and MRI markers | search | Required exposure. Eligible studies may name only individual imaging manifestations such as white matter lesions, lacunes, silent infarcts, or microbleeds rather than the umbrella term. |
| Incident dementia, Alzheimer disease, cognitive decline or impairment | optional | Topic-defining outcomes are searchable but may be reported inconsistently; test whether requiring them materially reduces screening while retaining known relevant records. |
| Population-based/community-dwelling longitudinal cohort | screen | Population source, community dwelling status, and follow-up are eligibility properties often incompletely named or indexed; screen at full text. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T21:23:59+00:00
- Records added to PubMed up to: 2017-05-06
- Total records: 9,534
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Cerebral Small Vessel Diseases[Mesh]` | 6,257 | none |
| 2 | `Leukoaraiosis[Mesh]` | 470 | none |
| 3 | `Stroke, Lacunar[Mesh]` | 412 | none |
| 4 | `Cerebral Infarction[Mesh]` | 29,744 | none |
| 5 | `Cerebral Hemorrhage[Mesh]` | 31,304 | none |
| 6 | `"cerebral small vessel disease"[tiab]` | 813 | none |
| 7 | `"cerebral small vessel diseases"[tiab]` | 105 | none |
| 8 | `"small vessel disease"[tiab]` | 2,316 | none |
| 9 | `"small vessel diseases"[tiab]` | 203 | none |
| 10 | `"small vessel ischemic disease"[tiab]` | 15 | none |
| 11 | `"cerebral microangiopathy"[tiab]` | 136 | none |
| 12 | `"cerebral microangiopathies"[tiab]` | 14 | none |
| 13 | `leukoaraios*[tiab]` | 1,010 | none |
| 14 | `"white matter hyperintensit*"[tiab]` | 2,313 | none |
| 15 | `"white-matter hyperintensit*"[tiab]` | 2,313 | none |
| 16 | `"white matter lesion*"[tiab]` | 4,051 | none |
| 17 | `"white-matter lesion*"[tiab]` | 4,051 | none |
| 18 | `"white matter change*"[tiab]` | 1,880 | none |
| 19 | `"white-matter change*"[tiab]` | 1,880 | none |
| 20 | `"white matter signal"[tiab:~2]` | 611 | none |
| 21 | `"white matter abnormalit*"[tiab]` | 1,590 | none |
| 22 | `"periventricular hyperintensit*"[tiab]` | 307 | none |
| 23 | `"lacunar infarct*"[tiab]` | 2,251 | none |
| 24 | `"lacunar stroke*"[tiab]` | 918 | none |
| 25 | `lacune*[tiab]` | 686 | none |
| 26 | `"silent brain infarct*"[tiab]` | 280 | none |
| 27 | `"silent cerebral infarct*"[tiab]` | 322 | none |
| 28 | `"covert brain infarct*"[tiab]` | 9 | none |
| 29 | `"silent infarct*"[tiab]` | 311 | none |
| 30 | `"cerebral microbleed*"[tiab]` | 710 | none |
| 31 | `"brain microbleed*"[tiab]` | 59 | none |
| 32 | `"microbleed*"[tiab]` | 1,468 | none |
| 33 | `"microhemorrhag*"[tiab]` | 578 | none |
| 34 | `"micro-haemorrhag*"[tiab]` | 23 | none |
| 35 | `"microhaemorrhag*"[tiab]` | 113 | none |
| 36 | `"hemosiderin deposit*"[tiab]` | 695 | none |
| 37 | `"haemosiderin deposit*"[tiab]` | 116 | none |
| 38 | `"vascular brain injur*"[tiab]` | 77 | none |
| 39 | `"vascular cognitive impairment"[tiab]` | 781 | none |
| 40 | `"subcortical vascular disease"[tiab]` | 35 | none |
| 41 | `"subcortical ischemic vascular disease"[tiab]` | 60 | none |
| 42 | `"subcortical ischaemic vascular disease"[tiab]` | 12 | none |
| 43 | `"Binswanger disease"[tiab]` | 317 | none |
| 44 | `"Binswanger's disease"[tiab]` | 276 | none |
| 45 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44` | 78,446 | none |
| 46 | `Dementia[Mesh]` | 145,526 | none |
| 47 | `Alzheimer Disease[Mesh]` | 82,140 | none |
| 48 | `Neurocognitive Disorders[Mesh]` | 222,273 | none |
| 49 | `Cognitive Dysfunction[Mesh]` | 8,211 | none |
| 50 | `"cognitive impairment"[tiab]` | 40,821 | none |
| 51 | `"cognitive impairments"[tiab]` | 6,267 | none |
| 52 | `"cognitive decline"[tiab]` | 15,036 | none |
| 53 | `"cognitive declines"[tiab]` | 239 | none |
| 54 | `"cognitive deterioration"[tiab]` | 1,471 | none |
| 55 | `"cognitive deteriorat*"[tiab]` | 1,480 | none |
| 56 | `"cognitive function"[tiab]` | 25,869 | none |
| 57 | `"cognitive functioning"[tiab]` | 10,032 | none |
| 58 | `"cognitive change"[tiab]` | 1,183 | none |
| 59 | `"cognitive changes"[tiab]` | 2,220 | none |
| 60 | `"cognitive performance"[tiab]` | 13,653 | none |
| 61 | `"cognitive trajectory"[tiab]` | 58 | none |
| 62 | `"cognitive trajectories"[tiab]` | 129 | none |
| 63 | `dementia[tiab]` | 85,598 | none |
| 64 | `dementias[tiab]` | 4,177 | none |
| 65 | `Alzheimer*[tiab]` | 116,181 | none |
| 66 | `"mild cognitive impairment"[tiab]` | 11,353 | none |
| 67 | `"mild cognitive impairments"[tiab]` | 112 | none |
| 68 | `"memory decline"[tiab]` | 1,116 | none |
| 69 | `"memory impairment"[tiab]` | 8,038 | none |
| 70 | `"incident dementia"[tiab]` | 749 | none |
| 71 | `"new-onset dementia"[tiab]` | 24 | none |
| 72 | `"onset of dementia"[tiab]` | 652 | none |
| 73 | `"cognitive outcome"[tiab]` | 1,353 | none |
| 74 | `"cognitive outcomes"[tiab]` | 1,670 | none |
| 75 | `#46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74` | 321,574 | none |
| 76 | `#45 AND #75` | 9,534 | none |

### Strategy (single line, for copying into PubMed)

```text
((Cerebral Small Vessel Diseases[Mesh] OR Leukoaraiosis[Mesh] OR Stroke, Lacunar[Mesh] OR Cerebral Infarction[Mesh] OR Cerebral Hemorrhage[Mesh] OR "cerebral small vessel disease"[tiab] OR "cerebral small vessel diseases"[tiab] OR "small vessel disease"[tiab] OR "small vessel diseases"[tiab] OR "small vessel ischemic disease"[tiab] OR "cerebral microangiopathy"[tiab] OR "cerebral microangiopathies"[tiab] OR leukoaraios*[tiab] OR "white matter hyperintensit*"[tiab] OR "white-matter hyperintensit*"[tiab] OR "white matter lesion*"[tiab] OR "white-matter lesion*"[tiab] OR "white matter change*"[tiab] OR "white-matter change*"[tiab] OR "white matter signal"[tiab:~2] OR "white matter abnormalit*"[tiab] OR "periventricular hyperintensit*"[tiab] OR "lacunar infarct*"[tiab] OR "lacunar stroke*"[tiab] OR lacune*[tiab] OR "silent brain infarct*"[tiab] OR "silent cerebral infarct*"[tiab] OR "covert brain infarct*"[tiab] OR "silent infarct*"[tiab] OR "cerebral microbleed*"[tiab] OR "brain microbleed*"[tiab] OR "microbleed*"[tiab] OR "microhemorrhag*"[tiab] OR "micro-haemorrhag*"[tiab] OR "microhaemorrhag*"[tiab] OR "hemosiderin deposit*"[tiab] OR "haemosiderin deposit*"[tiab] OR "vascular brain injur*"[tiab] OR "vascular cognitive impairment"[tiab] OR "subcortical vascular disease"[tiab] OR "subcortical ischemic vascular disease"[tiab] OR "subcortical ischaemic vascular disease"[tiab] OR "Binswanger disease"[tiab] OR "Binswanger's disease"[tiab]) AND (Dementia[Mesh] OR Alzheimer Disease[Mesh] OR Neurocognitive Disorders[Mesh] OR Cognitive Dysfunction[Mesh] OR "cognitive impairment"[tiab] OR "cognitive impairments"[tiab] OR "cognitive decline"[tiab] OR "cognitive declines"[tiab] OR "cognitive deterioration"[tiab] OR "cognitive deteriorat*"[tiab] OR "cognitive function"[tiab] OR "cognitive functioning"[tiab] OR "cognitive change"[tiab] OR "cognitive changes"[tiab] OR "cognitive performance"[tiab] OR "cognitive trajectory"[tiab] OR "cognitive trajectories"[tiab] OR dementia[tiab] OR dementias[tiab] OR Alzheimer*[tiab] OR "mild cognitive impairment"[tiab] OR "mild cognitive impairments"[tiab] OR "memory decline"[tiab] OR "memory impairment"[tiab] OR "incident dementia"[tiab] OR "new-onset dementia"[tiab] OR "onset of dementia"[tiab] OR "cognitive outcome"[tiab] OR "cognitive outcomes"[tiab])) AND ("1800/01/01"[edat] : "2017/05/06"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 2 | 2 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Incident dementia, Alzheimer disease, cognitive decline or impairment | AND-ed | 78,446 / 9,534 | 87.8% | none | 0/30 (up to 10% of removed records could be relevant) | The final exposure expansion adds 'silent infarct*' and increases the candidate exposure-only count to 78,446. The refreshed sample of 30 records removed by the outcome block was screened in title/abstract; none met the full population-based/community cohort, SVD marker, outcome, and follow-up criteria. The block reduces retrieval to 9,534 (87.8%), under the 10,000 budget; both known relevant records remain retrieved. Residual sampling uncertainty is retained. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Cerebral small vessel disease and MRI markers | 1 | `white[tiab] OR lacun*[tiab] OR microbleed*[tiab] OR infarct*[tiab] OR microangiopath*[tiab] OR ischem*[tiab] OR ischaem*[tiab] OR leukoencephalopath*[tiab] OR vascular[tiab]` | 22,847 | 0/30 |
| Cerebral small vessel disease and MRI markers | 2 | `white[tiab] OR lacun*[tiab] OR microbleed*[tiab] OR infarct*[tiab] OR microangiopath*[tiab] OR ischem*[tiab] OR ischaem*[tiab] OR leukoencephalopath*[tiab] OR vascular[tiab]` | 22,846 | 0/30 |
| Incident dementia, Alzheimer disease, cognitive decline or impairment | 1 | `cognition[tiab] OR cognitive[tiab] OR memory[tiab] OR neuropsycholog*[tiab] OR mental[tiab] OR forgetfulness[tiab]` | 2,283 | 0/30 |
| Incident dementia, Alzheimer disease, cognitive decline or impairment | 2 | `cognition[tiab] OR cognitive[tiab] OR memory[tiab] OR neuropsycholog*[tiab] OR mental[tiab] OR forgetfulness[tiab]` | 2,283 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| svd | 321,574 | 0 |
| cognitive_outcome | 78,446 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 78,326 | initial | none | Initial recall-first SVD exposure block with optional cognitive outcome block. Scope and terms derived before discovery; no seeds supplied. |
| 2 | 9,511 | cognitive_outcome: +29 / -0 | none | Moved the outcome candidate into the required strategy after an 87.9% count reduction and 0/30 eligible records in the loss sample; now evaluate the two-block strategy. |
| 3 | 9,513 | svd: +1 / -2 | none | Replaced separate exact leukoaraiosis singular/plural title-abstract clauses after PubMed warned the plural phrase was absent and zero-hit; tested leukoaraios*[tiab] (1,010 vs 1,008 singular), preserving the singular and adding morphological coverage without the warning. |
| 4 | 9,534 | svd: +1 / -0 | none | Added the exact eligible marker's bare name, silent infarct*, in response to critic finding R1-01. It is a new exposure synonym; remeasure count, development retrieval and probe/optional freshness. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 1 findings; R1-01 must-fix resolved
- Round 2 on version 4: 1 findings; R1-01 must-fix resolved
- Round 3 on version 4: 1 findings; R1-01 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1326 NCBI requests logged (657 from cache); strategy sha256 8696c43e0512._

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
        "location": "concept:cognitive_outcome",
        "blocking": false,
        "requires_review": true,
        "id": "I-d4984a6bbd20fc448176"
      }
    ],
    "issues": [
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:cognitive_outcome",
        "blocking": false,
        "requires_review": true,
        "id": "I-d4984a6bbd20fc448176"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Cerebral Small Vessel Diseases",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:23:59+00:00",
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
      "checked_at": "2026-09-28T21:23:59+00:00",
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
      "checked_at": "2026-09-28T21:23:59+00:00",
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
    },
    {
      "requested": "Cerebral Infarction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:23:59+00:00",
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
        "text": "Cerebral Infarction",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cerebral Hemorrhage",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:23:59+00:00",
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
      "requested": "Dementia",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:23:59+00:00",
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
      "location": "vocabulary:45",
      "term": {
        "text": "Dementia",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alzheimer Disease",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:23:59+00:00",
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
      "location": "vocabulary:46",
      "term": {
        "text": "Alzheimer Disease",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Neurocognitive Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:23:59+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D019965",
          "name": "Neurocognitive Disorders",
          "type": "descriptor",
          "scope_note": "Diagnoses of DEMENTIA and AMNESTIC DISORDER are subsumed here. (DSM-5)",
          "tree_numbers": [
            "F03.615"
          ],
          "entry_terms": 22,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D019965",
      "preferred_label": "Neurocognitive Disorders",
      "type": "descriptor",
      "location": "vocabulary:47",
      "term": {
        "text": "Neurocognitive Disorders",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognitive Dysfunction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:23:59+00:00",
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
      "location": "vocabulary:48",
      "term": {
        "text": "Cognitive Dysfunction",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"cerebral small vessel diseases\"[MeSH Terms] OR \"leukoaraiosis\"[MeSH Terms] OR \"stroke, lacunar\"[MeSH Terms] OR \"cerebral infarction\"[MeSH Terms] OR \"cerebral hemorrhage\"[MeSH Terms] OR \"cerebral small vessel disease\"[Title/Abstract] OR \"cerebral small vessel diseases\"[Title/Abstract] OR \"small vessel disease\"[Title/Abstract] OR \"small vessel diseases\"[Title/Abstract] OR \"small vessel ischemic disease\"[Title/Abstract] OR \"cerebral microangiopathy\"[Title/Abstract] OR \"cerebral microangiopathies\"[Title/Abstract] OR \"leukoaraios*\"[Title/Abstract] OR \"white matter hyperintensit*\"[Title/Abstract] OR \"white matter hyperintensit*\"[Title/Abstract] OR \"white matter lesion*\"[Title/Abstract] OR \"white matter lesion*\"[Title/Abstract] OR \"white matter change*\"[Title/Abstract] OR \"white matter change*\"[Title/Abstract] OR \"white matter signal\"[Title/Abstract:~2] OR \"white matter abnormalit*\"[Title/Abstract] OR \"periventricular hyperintensit*\"[Title/Abstract] OR \"lacunar infarct*\"[Title/Abstract] OR \"lacunar stroke*\"[Title/Abstract] OR \"lacune*\"[Title/Abstract] OR \"silent brain infarct*\"[Title/Abstract] OR \"silent cerebral infarct*\"[Title/Abstract] OR \"covert brain infarct*\"[Title/Abstract] OR \"silent infarct*\"[Title/Abstract] OR \"cerebral microbleed*\"[Title/Abstract] OR \"brain microbleed*\"[Title/Abstract] OR \"microbleed*\"[Title/Abstract] OR \"microhemorrhag*\"[Title/Abstract] OR \"micro haemorrhag*\"[Title/Abstract] OR \"microhaemorrhag*\"[Title/Abstract] OR \"hemosiderin deposit*\"[Title/Abstract] OR \"haemosiderin deposit*\"[Title/Abstract] OR \"vascular brain injur*\"[Title/Abstract] OR \"vascular cognitive impairment\"[Title/Abstract] OR \"subcortical vascular disease\"[Title/Abstract] OR \"subcortical ischemic vascular disease\"[Title/Abstract] OR \"subcortical ischaemic vascular disease\"[Title/Abstract] OR \"Binswanger disease\"[Title/Abstract] OR \"Binswanger's disease\"[Title/Abstract]) AND (\"dementia\"[MeSH Terms] OR \"alzheimer disease\"[MeSH Terms] OR \"neurocognitive disorders\"[MeSH Terms] OR \"cognitive dysfunction\"[MeSH Terms] OR \"cognitive impairment\"[Title/Abstract] OR \"cognitive impairments\"[Title/Abstract] OR \"cognitive decline\"[Title/Abstract] OR \"cognitive declines\"[Title/Abstract] OR \"cognitive deterioration\"[Title/Abstract] OR \"cognitive deteriorat*\"[Title/Abstract] OR \"cognitive function\"[Title/Abstract] OR \"cognitive functioning\"[Title/Abstract] OR \"cognitive change\"[Title/Abstract] OR \"cognitive changes\"[Title/Abstract] OR \"cognitive performance\"[Title/Abstract] OR \"cognitive trajectory\"[Title/Abstract] OR \"cognitive trajectories\"[Title/Abstract] OR \"dementia\"[Title/Abstract] OR \"dementias\"[Title/Abstract] OR \"alzheimer*\"[Title/Abstract] OR \"mild cognitive impairment\"[Title/Abstract] OR \"mild cognitive impairments\"[Title/Abstract] OR \"memory decline\"[Title/Abstract] OR \"memory impairment\"[Title/Abstract] OR \"incident dementia\"[Title/Abstract] OR \"new-onset dementia\"[Title/Abstract] OR \"onset of dementia\"[Title/Abstract] OR \"cognitive outcome\"[Title/Abstract] OR \"cognitive outcomes\"[Title/Abstract]) AND 1800/01/01:2017/05/06[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "05aab285cf91d8f968c168df57e9428a539006cce8c02c50775f67700f661ba2",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "Added the bare-name silent infarct* synonym identified by the critic; the term was tested in PubMed before re-evaluation."
        },
        "operators": {
          "verdict": "pass",
          "note": "The exposure and outcome blocks are OR-combined internally and AND-combined; population source and follow-up remain screening criteria."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The MeSH layer retains the small-vessel, lacunar, infarction, hemorrhage, dementia, Alzheimer disease, and cognitive dysfunction headings."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Added and tested the specific silent infarct* wording requested by the critic. The proximity clause remains unchanged and has no reported parser warning."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current evaluation reports no query translation issues or technical blockers."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age, language, or design filter is applied; the 2017-05-06 Entrez cutoff is not a publication-date restriction."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility names silent infarct as an eligible MRI marker, but the exposure block searches only silent brain, silent cerebral and covert brain variants.",
          "recommendation": "Add and test silent infarct*[tiab], then run a complete evaluation including count, known-record, category-probe and optional-block checks.",
          "status": "resolved",
          "response": "Added \"silent infarct*\"[tiab]. Its tested PubMed count was 311 through the Entrez cutoff; the final count changed from 9,513 to 9,534 and both known relevant development records remained retrieved. The optional sample was refreshed and re-screened, and the SVD category probe remains clean. The outcome category probe is stale because this exposure edit changed the overall probe base after the two-probe budget was spent; that remaining review item is explicitly passed to the next critic round for evidence-bound disposition."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "4f7616c0f62672fc38aad92b7e59db3df35b72188d1fd7a4414020f87e34841b",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The current exposure block covers the named MRI markers, including the bare-name silent infarct* term added after round 1. The outcome block covers dementia, Alzheimer disease and cognitive impairment/decline."
        },
        "operators": {
          "verdict": "pass",
          "note": "Exposure and outcome terms are OR-combined within blocks; blocks are AND-combined. Population source and follow-up remain screening criteria. The outcome block retains both known development records and reduces the workload to 9,534."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "MeSH headings cover cerebral small vessel disease, leukoaraiosis, lacunar stroke, infarction, hemorrhage, dementia, Alzheimer disease, neurocognitive disorders and cognitive dysfunction."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Bare-name MRI marker wording is present. The white matter signal proximity expression has no wildcard and is translated without a warning."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Current evaluation has no translation issues or parser warnings; count and final query syntax are valid."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age, language or study-design restriction is applied. 2017-05-06 is an Entrez-date cutoff, not a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility names silent infarct as an eligible MRI marker, but the earlier exposure block searched only silent brain, silent cerebral and covert brain variants.",
          "recommendation": "Add and test silent infarct*[tiab], then run a complete evaluation.",
          "status": "resolved",
          "response": "The current block includes \"silent infarct*\"[tiab] (311 results through the Entrez cutoff). Final retrieval is 9,534; both known relevant development records remain retrieved, and the optional sample was refreshed and re-screened."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-d4984a6bbd20fc448176",
          "status": "accepted-risk",
          "response": "The outcome category probe is genuinely stale: its second 30-record sample predates the final addition of \"silent infarct*\"[tiab]. The probe budget for this concept is spent, so no fresh draw can be made within the standard workflow. Accept this as a bounded residual sampling risk after review: both outcome probes screened 0/30 eligible records, the new exposed term was independently tested (311 records through the cutoff), the final result increased from 9,513 to 9,534, both eligible development records remain retrieved, and the optional loss sample was refreshed at the final strategy. This does not establish that no outside eligible studies exist; community cohort and follow-up criteria remain for screening.",
          "evidence": "Validation issue I-d4984a6bbd20fc448176 states category_probe_stale_budget_spent. The stored cognitive_outcome-2 probe query does not contain silent infarct*. Its screen found 0/30 relevant; current evaluation counts are 9,534 final and 78,446 exposure-only; the added term count is 311; relevant set recall is 2/2; refreshed optional loss sample is 0/30 relevant."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "4f7616c0f62672fc38aad92b7e59db3df35b72188d1fd7a4414020f87e34841b",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure block includes the requested bare-name silent infarct* term alongside the other named MRI markers. The outcome block covers dementia, Alzheimer disease, and cognitive decline or impairment."
        },
        "operators": {
          "verdict": "pass",
          "note": "Exposure and outcome terms are OR-combined within blocks, and blocks are AND-combined. Population source and follow-up remain screening criteria. The outcome block reduces retrieval to 9,534, within the 10,000-record budget."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The MeSH layer includes cerebral small vessel disease, leukoaraiosis, lacunar stroke, infarction, hemorrhage, dementia, Alzheimer disease, neurocognitive disorders, and cognitive dysfunction."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Named MRI markers have corresponding text-word coverage, including silent infarct. The white matter signal proximity clause has no wildcard and the packet reports no parser warning."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current evaluation reports no translation issues or parser warnings and includes the final query count."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age, language, or study-design filter is applied. The 2017-05-06 bound is an Entrez-date cutoff, not a publication-date restriction."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility names silent infarct as an eligible MRI marker, but the earlier exposure block searched only silent brain, silent cerebral, and covert brain variants.",
          "recommendation": "Add and test silent infarct*[tiab], then run a complete evaluation.",
          "status": "resolved",
          "response": "The current block includes \"silent infarct*\"[tiab], tested at 311 records through the Entrez cutoff. Final retrieval is 9,534; both eligible development records remain retrieved, and the optional loss sample was refreshed and screened."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-d4984a6bbd20fc448176",
          "status": "accepted-risk",
          "response": "Accept this as a bounded residual sampling risk. The outcome category probe is stale because its second 30-record sample predates the final exposure edit, and the probe budget is spent. The evidence supports retaining the disposition: both outcome probes screened 0/30 eligible records; the added exposure term was independently tested; both eligible development records remain retrieved; and the optional loss sample was refreshed at the final strategy. These checks do not prove that no eligible studies were missed, so population source and follow-up remain screening criteria.",
          "evidence": "The packet identifies the stored cognitive_outcome-2 probe as stale because it does not contain \"silent infarct*\". Its screen found 0/30 relevant. The added term returned 311 records through the cutoff; final retrieval is 9,534 versus 9,513 before the edit, exposure-only retrieval is 78,446, both eligible development records remain retrieved, and the refreshed optional loss sample found 0/30 relevant."
        }
      ]
    }
  ]
}
```

