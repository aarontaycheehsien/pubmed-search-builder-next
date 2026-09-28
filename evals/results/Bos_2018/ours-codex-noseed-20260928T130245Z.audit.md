# PubMed search strategy: audit

Generated 2026-09-28T13:39:18+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In population-based cohorts, is cerebral small vessel disease (and its MRI markers) associated with the risk of incident dementia and cognitive decline?
- Framework: PECO
- Scope confirmed by user: no (User asked to proceed without clarification; roles are provisional assumptions. No known relevant articles were supplied. Standard-depth discovery attempted within PubMed as of 2017-05-06. No publication-date limit; the Entrez date bound is applied via as_of/PSB_AS_OF. The cohort/population setting was changed from screen to optional after the evaluated count exceeded 10,000; test as an AND-ed candidate before deciding. Following the internal critique, enlarged perivascular spaces (including Virchow-Robin spaces) are treated as an eligible MRI marker under the broad CSVD marker wording and added to the exposure vocabulary.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Cerebral small vessel disease and MRI markers | search | The exposure defines the question and includes named MRI markers; authors and indexers commonly name these concepts. |
| Incident dementia, Alzheimer disease, and cognitive decline or impairment | optional | Topic-defining outcomes may reduce screening burden, but some cohort studies do not name outcomes consistently in searchable fields; test a complete outcome block before deciding. |
| Community-dwelling population-based longitudinal cohorts | optional | Cohort, prospective, longitudinal, and community or population-based labels are searchable, but their absence is not reliable enough to require; test this block because the current count exceeds the workload budget. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T13:37:41+00:00
- Records added to PubMed up to: 2017-05-06
- Total records: 6,946
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Cerebral Small Vessel Diseases[Mesh]` | 6,257 | none |
| 2 | `Cerebrovascular Disorders[Mesh]` | 329,326 | none |
| 3 | `Leukoaraiosis[Mesh]` | 470 | none |
| 4 | `Stroke, Lacunar[Mesh]` | 412 | none |
| 5 | `Cerebral Infarction[Mesh]` | 29,744 | none |
| 6 | `Brain Infarction[Mesh]` | 34,827 | none |
| 7 | `White Matter[Mesh]` | 4,280 | none |
| 8 | `Cerebral Hemorrhage[Mesh]` | 31,304 | none |
| 9 | `"cerebral small vessel disease"[tiab]` | 813 | none |
| 10 | `"small vessel disease"[tiab]` | 2,316 | none |
| 11 | `CSVD[tiab]` | 127 | none |
| 12 | `"cerebral microangiopath*"[tiab]` | 150 | none |
| 13 | `"white matter hyperintens*"[tiab]` | 2,354 | none |
| 14 | `"white matter lesion*"[tiab]` | 4,051 | none |
| 15 | `"white matter change*"[tiab]` | 1,880 | none |
| 16 | `"white matter abnormalit*"[tiab]` | 1,590 | none |
| 17 | `"white matter disease"[tiab]` | 813 | none |
| 18 | `leukoaraios*[tiab]` | 1,010 | none |
| 19 | `leucoaraios*[tiab]` | 38 | none |
| 20 | `"lacunar infarct*"[tiab]` | 2,251 | none |
| 21 | `"lacunar stroke*"[tiab]` | 918 | none |
| 22 | `"silent brain infarct*"[tiab]` | 280 | none |
| 23 | `"silent cerebral infarct*"[tiab]` | 322 | none |
| 24 | `"covert brain infarct*"[tiab]` | 9 | none |
| 25 | `"asymptomatic brain infarct*"[tiab]` | 15 | none |
| 26 | `"brain infarct*"[tiab]` | 3,534 | none |
| 27 | `"cerebral microbleed*"[tiab]` | 710 | none |
| 28 | `"brain microbleed*"[tiab]` | 59 | none |
| 29 | `"cerebral microhemorrhag*"[tiab]` | 62 | none |
| 30 | `"brain microhemorrhag*"[tiab]` | 15 | none |
| 31 | `"vascular brain injury"[tiab]` | 73 | none |
| 32 | `"vascular brain injur*"[tiab]` | 77 | none |
| 33 | `"subcortical ischemic vascular disease"[tiab]` | 60 | none |
| 34 | `"subcortical ischaemic vascular disease"[tiab]` | 12 | none |
| 35 | `perivascular space*[tiab]` | 1,613 | none |
| 36 | `"enlarged perivascular space*"[tiab]` | 86 | none |
| 37 | `"dilated perivascular space*"[tiab]` | 75 | none |
| 38 | `"Virchow-Robin space*"[tiab]` | 410 | none |
| 39 | `"Virchow Robin space*"[tiab]` | 410 | none |
| 40 | `"silent infarct*"[tiab]` | 311 | none |
| 41 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40` | 342,602 | none |
| 42 | `Dementia[Mesh]` | 145,526 | none |
| 43 | `Alzheimer Disease[Mesh]` | 82,140 | none |
| 44 | `Cognition Disorders[Mesh]` | 80,254 | none |
| 45 | `Cognitive Dysfunction[Mesh]` | 8,211 | none |
| 46 | `Memory Disorders[Mesh]` | 26,825 | none |
| 47 | `dementia*[tiab]` | 87,012 | none |
| 48 | `Alzheimer*[tiab]` | 116,181 | none |
| 49 | `"mild cognitive impairment"[tiab]` | 11,353 | none |
| 50 | `"cognitive impairment"[tiab]` | 40,821 | none |
| 51 | `"cognitive decline"[tiab]` | 15,036 | none |
| 52 | `"cognitive deterioration"[tiab]` | 1,471 | none |
| 53 | `"cognitive dysfunction"[tiab]` | 9,912 | none |
| 54 | `"cognitive function"[tiab]` | 25,869 | none |
| 55 | `"cognitive performance"[tiab]` | 13,653 | none |
| 56 | `"cognitive change"[tiab]` | 1,183 | none |
| 57 | `"mental decline"[tiab]` | 214 | none |
| 58 | `"memory decline"[tiab]` | 1,116 | none |
| 59 | `"executive function"[tiab]` | 10,410 | none |
| 60 | `"processing speed"[tiab]` | 5,489 | none |
| 61 | `cognition[tiab]` | 54,533 | none |
| 62 | `cognitive[tiab]` | 268,718 | none |
| 63 | `"incident dementia"[tiab]` | 749 | none |
| 64 | `"conversion to dementia"[tiab]` | 254 | none |
| 65 | `#42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64` | 480,162 | none |
| 66 | `Cohort Studies[Mesh]` | 1,725,846 | none |
| 67 | `Longitudinal Studies[Mesh]` | 114,265 | none |
| 68 | `Follow-Up Studies[Mesh]` | 586,948 | none |
| 69 | `Prospective Studies[Mesh]` | 468,312 | none |
| 70 | `cohort*[tiab]` | 405,084 | none |
| 71 | `longitudinal[tiab]` | 189,054 | none |
| 72 | `prospective[tiab]` | 453,045 | none |
| 73 | `follow-up[tiab]` | 772,149 | none |
| 74 | `follow up[tiab]` | 772,149 | none |
| 75 | `population-based[tiab]` | 100,037 | none |
| 76 | `population based[tiab]` | 100,037 | none |
| 77 | `community-based[tiab]` | 46,909 | none |
| 78 | `community based[tiab]` | 46,909 | none |
| 79 | `community-dwelling[tiab]` | 16,741 | none |
| 80 | `community dwelling[tiab]` | 16,741 | none |
| 81 | `general population[tiab]` | 80,605 | none |
| 82 | `#66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81` | 2,564,539 | none |
| 83 | `#41 AND #65 AND #82` | 6,946 | none |

### Strategy (single line, for copying into PubMed)

```text
((Cerebral Small Vessel Diseases[Mesh] OR Cerebrovascular Disorders[Mesh] OR Leukoaraiosis[Mesh] OR Stroke, Lacunar[Mesh] OR Cerebral Infarction[Mesh] OR Brain Infarction[Mesh] OR White Matter[Mesh] OR Cerebral Hemorrhage[Mesh] OR "cerebral small vessel disease"[tiab] OR "small vessel disease"[tiab] OR CSVD[tiab] OR "cerebral microangiopath*"[tiab] OR "white matter hyperintens*"[tiab] OR "white matter lesion*"[tiab] OR "white matter change*"[tiab] OR "white matter abnormalit*"[tiab] OR "white matter disease"[tiab] OR leukoaraios*[tiab] OR leucoaraios*[tiab] OR "lacunar infarct*"[tiab] OR "lacunar stroke*"[tiab] OR "silent brain infarct*"[tiab] OR "silent cerebral infarct*"[tiab] OR "covert brain infarct*"[tiab] OR "asymptomatic brain infarct*"[tiab] OR "brain infarct*"[tiab] OR "cerebral microbleed*"[tiab] OR "brain microbleed*"[tiab] OR "cerebral microhemorrhag*"[tiab] OR "brain microhemorrhag*"[tiab] OR "vascular brain injury"[tiab] OR "vascular brain injur*"[tiab] OR "subcortical ischemic vascular disease"[tiab] OR "subcortical ischaemic vascular disease"[tiab] OR perivascular space*[tiab] OR "enlarged perivascular space*"[tiab] OR "dilated perivascular space*"[tiab] OR "Virchow-Robin space*"[tiab] OR "Virchow Robin space*"[tiab] OR "silent infarct*"[tiab]) AND (Dementia[Mesh] OR Alzheimer Disease[Mesh] OR Cognition Disorders[Mesh] OR Cognitive Dysfunction[Mesh] OR Memory Disorders[Mesh] OR dementia*[tiab] OR Alzheimer*[tiab] OR "mild cognitive impairment"[tiab] OR "cognitive impairment"[tiab] OR "cognitive decline"[tiab] OR "cognitive deterioration"[tiab] OR "cognitive dysfunction"[tiab] OR "cognitive function"[tiab] OR "cognitive performance"[tiab] OR "cognitive change"[tiab] OR "mental decline"[tiab] OR "memory decline"[tiab] OR "executive function"[tiab] OR "processing speed"[tiab] OR cognition[tiab] OR cognitive[tiab] OR "incident dementia"[tiab] OR "conversion to dementia"[tiab]) AND (Cohort Studies[Mesh] OR Longitudinal Studies[Mesh] OR Follow-Up Studies[Mesh] OR Prospective Studies[Mesh] OR cohort*[tiab] OR longitudinal[tiab] OR prospective[tiab] OR follow-up[tiab] OR follow up[tiab] OR population-based[tiab] OR population based[tiab] OR community-based[tiab] OR community based[tiab] OR community-dwelling[tiab] OR community dwelling[tiab] OR general population[tiab])) AND ("1800/01/01"[edat] : "2017/05/06"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 10 | 10 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Incident dementia, Alzheimer disease, and cognitive decline or impairment | AND-ed | 77,092 / 6,946 | 91.0% | none | 0/30 (up to 10% of removed records could be relevant) | Re-tested after adding the bare silent infarct* term: 30 excluded records were screened by title and abstract, with none meeting all criteria; none of the 10 benchmark records is lost. On the current base query the outcome block reduces 77,092 records to 6,946 (91.0%). Retain for a material reduction; 0/30 does not prove the excluded pool contains no eligible records. |
| Community-dwelling population-based longitudinal cohorts | AND-ed | 25,936 / 6,946 | 73.2% | none | 0/30 (up to 10% of removed records could be relevant) | Re-tested after adding the bare silent infarct* term: 30 excluded records were screened by title and abstract, with none meeting population/community cohort and longitudinal follow-up criteria; none of the 10 benchmark records is lost. The block reduces 25,936 records to 6,946 (73.2%) and keeps screening under the standard 10,000 budget. Retain it while recognizing that eligible studies omitting cohort/population labels may be missed. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| csd | 82,076 | 0 |
| cognitive_outcome | 77,092 | 0 |
| population_design | 25,936 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 340,969 | initial | none | Initial recall-first exposure block with a comprehensive optional cognitive-outcome block; MeSH and title/abstract terms cover specified CSVD MRI markers. Benchmark records screened from included studies of the longitudinal WMH review. |
| 2 | 25,848 | cognitive_outcome: +23 / -0 | none | AND-ed cognitive outcome block after optional loss-sample decision: 0/30 sampled losses relevant and no benchmark loss; expected substantial reduction. |
| 3 | 25,848 | limits/combination | none | Added population_design as an optional candidate because the evaluated strategy exceeded workload budget; test cohort, follow-up, prospective and community/population labels. |
| 4 | 6,939 | population_design: +16 / -0 | none | Cohort/population setting block AND-ed after optional sample: 0/30 sampled losses relevant, no benchmark losses, and count now below the 10,000 budget. |
| 5 | 6,944 | csd: +5 / -0 | none | Added enlarged/dilated perivascular spaces and Virchow-Robin variants to the eligible exposure block following internal critique; scope expanded under broad CSVD MRI marker wording, requiring refreshed optional decisions. |
| 6 | 6,946 | csd: +1 / -0 | none | Added the bare title/abstract term silent infarct* following the second critic; this covers the named silent-infarct concept without requiring brain/cerebral wording. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 2 findings; R1-1 must-fix resolved, R1-2 should-fix resolved
- Round 2 on version 5: 3 findings; R1-1 must-fix resolved, R1-2 should-fix resolved, R2-1 should-fix resolved
- Round 3 on version 6: 3 findings; R1-1 must-fix resolved, R1-2 should-fix resolved, R2-1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 2192 NCBI requests logged (1171 from cache); strategy sha256 6966a67c69f7._

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
      "checked_at": "2026-09-28T13:37:41+00:00",
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
      "checked_at": "2026-09-28T13:37:41+00:00",
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
      "checked_at": "2026-09-28T13:37:41+00:00",
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
      "checked_at": "2026-09-28T13:37:41+00:00",
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
      "requested": "Cerebral Infarction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:37:41+00:00",
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
        "text": "Cerebral Infarction",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Brain Infarction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:37:41+00:00",
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
      "location": "vocabulary:6",
      "term": {
        "text": "Brain Infarction",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "White Matter",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:37:41+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D066127",
          "name": "White Matter",
          "type": "descriptor",
          "scope_note": "The region of CENTRAL NERVOUS SYSTEM that appears lighter in color than the other type, GRAY MATTER. It mainly consists of MYELINATED NERVE FIBERS and contains few neuronal cell bodies or DENDRITES.",
          "tree_numbers": [
            "A08.186.211.204",
            "A08.186.854.880"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D066127",
      "preferred_label": "White Matter",
      "type": "descriptor",
      "location": "vocabulary:7",
      "term": {
        "text": "White Matter",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cerebral Hemorrhage",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:37:41+00:00",
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
      "location": "vocabulary:8",
      "term": {
        "text": "Cerebral Hemorrhage",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Dementia",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:37:41+00:00",
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
      "location": "vocabulary:41",
      "term": {
        "text": "Dementia",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alzheimer Disease",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:37:41+00:00",
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
      "location": "vocabulary:42",
      "term": {
        "text": "Alzheimer Disease",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognition Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:37:41+00:00",
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
        "text": "Cognition Disorders",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognitive Dysfunction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:37:41+00:00",
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
      "location": "vocabulary:44",
      "term": {
        "text": "Cognitive Dysfunction",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Memory Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:37:41+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D008569",
          "name": "Memory Disorders",
          "type": "descriptor",
          "scope_note": "Disturbances in registering an impression, in the retention of an acquired impression, or in the recall of an impression. Memory impairments are associated with DEMENTIA; CRANIOCEREBRAL TRAUMA; ENCEPHALITIS; ALCOHOLISM (see also ALCOHOL AMNESTIC DISORDER); SCHIZOPHRENIA; and other conditions.",
          "tree_numbers": [
            "C10.597.606.525",
            "C23.888.592.604.529",
            "F01.700.625"
          ],
          "entry_terms": 25,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D008569",
      "preferred_label": "Memory Disorders",
      "type": "descriptor",
      "location": "vocabulary:45",
      "term": {
        "text": "Memory Disorders",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cohort Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:37:41+00:00",
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
      "location": "vocabulary:64",
      "term": {
        "text": "Cohort Studies",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Longitudinal Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:37:41+00:00",
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
      "location": "vocabulary:65",
      "term": {
        "text": "Longitudinal Studies",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Follow-Up Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:37:41+00:00",
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
      "location": "vocabulary:66",
      "term": {
        "text": "Follow-Up Studies",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Prospective Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T13:37:41+00:00",
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
      "location": "vocabulary:67",
      "term": {
        "text": "Prospective Studies",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"cerebral small vessel diseases\"[MeSH Terms] OR \"cerebrovascular disorders\"[MeSH Terms] OR \"leukoaraiosis\"[MeSH Terms] OR \"stroke, lacunar\"[MeSH Terms] OR \"cerebral infarction\"[MeSH Terms] OR \"brain infarction\"[MeSH Terms] OR \"white matter\"[MeSH Terms] OR \"cerebral hemorrhage\"[MeSH Terms] OR \"cerebral small vessel disease\"[Title/Abstract] OR \"small vessel disease\"[Title/Abstract] OR \"CSVD\"[Title/Abstract] OR \"cerebral microangiopath*\"[Title/Abstract] OR \"white matter hyperintens*\"[Title/Abstract] OR \"white matter lesion*\"[Title/Abstract] OR \"white matter change*\"[Title/Abstract] OR \"white matter abnormalit*\"[Title/Abstract] OR \"white matter disease\"[Title/Abstract] OR \"leukoaraios*\"[Title/Abstract] OR \"leucoaraios*\"[Title/Abstract] OR \"lacunar infarct*\"[Title/Abstract] OR \"lacunar stroke*\"[Title/Abstract] OR \"silent brain infarct*\"[Title/Abstract] OR \"silent cerebral infarct*\"[Title/Abstract] OR \"covert brain infarct*\"[Title/Abstract] OR \"asymptomatic brain infarct*\"[Title/Abstract] OR \"brain infarct*\"[Title/Abstract] OR \"cerebral microbleed*\"[Title/Abstract] OR \"brain microbleed*\"[Title/Abstract] OR \"cerebral microhemorrhag*\"[Title/Abstract] OR \"brain microhemorrhag*\"[Title/Abstract] OR \"vascular brain injury\"[Title/Abstract] OR \"vascular brain injur*\"[Title/Abstract] OR \"subcortical ischemic vascular disease\"[Title/Abstract] OR \"subcortical ischaemic vascular disease\"[Title/Abstract] OR \"perivascular space*\"[Title/Abstract] OR \"enlarged perivascular space*\"[Title/Abstract] OR \"dilated perivascular space*\"[Title/Abstract] OR \"virchow robin space*\"[Title/Abstract] OR \"virchow robin space*\"[Title/Abstract] OR \"silent infarct*\"[Title/Abstract]) AND (\"dementia\"[MeSH Terms] OR \"alzheimer disease\"[MeSH Terms] OR \"cognition disorders\"[MeSH Terms] OR \"cognitive dysfunction\"[MeSH Terms] OR \"memory disorders\"[MeSH Terms] OR \"dementia*\"[Title/Abstract] OR \"alzheimer*\"[Title/Abstract] OR \"mild cognitive impairment\"[Title/Abstract] OR \"cognitive impairment\"[Title/Abstract] OR \"cognitive decline\"[Title/Abstract] OR \"cognitive deterioration\"[Title/Abstract] OR \"cognitive dysfunction\"[Title/Abstract] OR \"cognitive function\"[Title/Abstract] OR \"cognitive performance\"[Title/Abstract] OR \"cognitive change\"[Title/Abstract] OR \"mental decline\"[Title/Abstract] OR \"memory decline\"[Title/Abstract] OR \"executive function\"[Title/Abstract] OR \"processing speed\"[Title/Abstract] OR \"cognition\"[Title/Abstract] OR \"cognitive\"[Title/Abstract] OR \"incident dementia\"[Title/Abstract] OR \"conversion to dementia\"[Title/Abstract]) AND (\"cohort studies\"[MeSH Terms] OR \"longitudinal studies\"[MeSH Terms] OR \"follow up studies\"[MeSH Terms] OR \"prospective studies\"[MeSH Terms] OR \"cohort*\"[Title/Abstract] OR \"longitudinal\"[Title/Abstract] OR \"prospective\"[Title/Abstract] OR \"follow-up\"[Title/Abstract] OR \"follow-up\"[Title/Abstract] OR \"population-based\"[Title/Abstract] OR \"population-based\"[Title/Abstract] OR \"community-based\"[Title/Abstract] OR \"community-based\"[Title/Abstract] OR \"community-dwelling\"[Title/Abstract] OR \"community-dwelling\"[Title/Abstract] OR \"general population\"[Title/Abstract]) AND 1800/01/01:2017/05/06[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "1eb0fd18803d2dd4231022a3f211322b1a7251fdaf5aa5365687934c655b84d1",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The required exposure, tested outcome, and tested cohort/population concepts correspond to the question; the later expansion adds a named CSVD MRI marker."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within concept blocks and AND across measured concepts; no NOT operators."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The reviewed MeSH headings were verified; the perivascular-space vocabulary is covered with text terms because the MeSH lookup returned no specific descriptor."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The exposure block and eligibility criteria were expanded to include enlarged/dilated perivascular spaces and Virchow-Robin spaces, with current-query evaluation and optional blocks re-tested."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No technical syntax or translation issue was reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2017-05-06 Entry Date bound is an explicit run constraint, not a publication-date filter; no [dp] limit is used."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "block": null,
          "finding": "The Entrez Entry Date ceiling needs to be identified as a deliberate 2017-05-06 cutoff rather than an unexplained publication-date limit.",
          "recommendation": "Document the cutoff and distinguish Entry Date from publication date.",
          "status": "resolved",
          "response": "Resolved by recording as_of=2017-05-06 in protocol.json, retaining the required Entry Date [edat] ceiling for the harness snapshot, and explicitly stating that no publication-date [dp] limit is applied. The packet's PubMed translation identifies the limit as Date - Entry."
        },
        {
          "id": "R1-2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "block": "csd",
          "finding": "Enlarged perivascular spaces were not included among eligible CSVD MRI markers.",
          "recommendation": "Include enlarged perivascular spaces if within the intended broad CSVD marker scope, and add common text variants.",
          "status": "resolved",
          "response": "Resolved using the user's instruction to proceed with reasonable assumptions: enlarged/dilated perivascular spaces and Virchow-Robin spaces are included as CSVD MRI markers in the eligibility wording and searched with perivascular space*, enlarged/dilated perivascular space*, and Virchow-Robin variants. MeSH lookup returned no dedicated perivascular-space descriptor. The full strategy was re-evaluated; 10/10 benchmark records remained retrieved. Both optional blocks were sampled and re-decided against the updated query."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "9c2744868586597f04481a0b569cf08b43c3ca8fbc840c35459b6ebee3d5e181",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The exposure block and eligibility were expanded as recommended; round 2 identified one remaining text-word omission, now addressed."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are OR-ed within blocks; tested optional concepts are AND-ed; no NOT is used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Verified MeSH headings and text terms for perivascular spaces are retained."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Added the bare silent infarct* expression recommended by this round and re-evaluated the full strategy; benchmark retrieval remains complete."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax or PubMed translation issue was reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The as-of Entry Date bound is explicitly documented and no publication-date filter is used."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The Entrez Entry Date ceiling needs to be identified as a deliberate 2017-05-06 cutoff rather than an unexplained publication-date limit.",
          "recommendation": "Document the cutoff and distinguish Entry Date from publication date.",
          "status": "resolved",
          "response": "The 2017-05-06 as-of limit is an explicit harness requirement recorded in protocol.json and encoded as [edat]. No [dp] publication-date limit is applied."
        },
        {
          "id": "R1-2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Enlarged perivascular spaces were not included among eligible CSVD MRI markers.",
          "recommendation": "Include enlarged perivascular spaces if within the intended broad CSVD marker scope, and add common text variants.",
          "status": "resolved",
          "response": "Enlarged/dilated perivascular spaces and Virchow-Robin spaces were added to eligibility and the exposure text-word block; current evaluation and optional-block checks were rerun."
        },
        {
          "id": "R2-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Eligibility names lacunar/silent infarct, but the silent-infarct text terms require brain or cerebral wording, or use covert/asymptomatic wording. The bare phrase silent infarct* is missing.",
          "recommendation": "Add silent infarct*[tiab], then perform another complete evaluation, including benchmark and optional-block rechecks.",
          "status": "resolved",
          "response": "Added \"silent infarct*\"[tiab] to the CSVD exposure block, then reran complete evaluation and refreshed both optional block samples and decisions. The 10-study benchmark remains fully retrieved; no translation issues or blockers are reported."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 6,
      "review_sha256": "db815c8a4c3965a7e1541a92513df1c9be7c667dd21691fcc40edb3f91115dfb",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The exposure block includes the named markers, including perivascular spaces and the bare silent infarct* term. Outcome and cohort/population blocks were tested; both retain 10/10 benchmark records. Their remaining risk of missing studies that omit those labels is documented."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are OR-ed within blocks and the selected outcome and population/design blocks are AND-ed with the exposure. No NOT operators are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The reviewed MeSH headings are retained; perivascular spaces are represented by text terms because the lookup found no specific descriptor."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The prior marker omissions are addressed with perivascular-space variants and the bare silent infarct* term. The complete evaluation and optional-block checks were rerun."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no translation errors or blockers; the translated query preserves the intended block structure and Entry Date bound."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2017-05-06 as-of cutoff is documented and applied as an Entrez Entry Date bound. No publication-date limit is applied."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The Entrez Entry Date ceiling needs to be identified as a deliberate 2017-05-06 cutoff rather than an unexplained publication-date limit.",
          "recommendation": "Document the cutoff and distinguish Entry Date from publication date.",
          "status": "resolved",
          "response": "The protocol records as_of=2017-05-06, and the translated query applies the bound as Date - Entry. The notes explicitly state that no publication-date limit is used."
        },
        {
          "id": "R1-2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Enlarged perivascular spaces were not included among eligible CSVD MRI markers.",
          "recommendation": "Include enlarged perivascular spaces if within the intended broad CSVD marker scope, and add common text variants.",
          "status": "resolved",
          "response": "Eligibility and the exposure block now include enlarged/dilated perivascular spaces and Virchow-Robin variants. The packet records a full re-evaluation and refreshed optional-block checks."
        },
        {
          "id": "R2-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Eligibility names lacunar/silent infarct, but the silent-infarct text terms require brain or cerebral wording, or use covert/asymptomatic wording. The bare phrase silent infarct* is missing.",
          "recommendation": "Add silent infarct*[tiab], then perform another complete evaluation, including benchmark and optional-block rechecks.",
          "status": "resolved",
          "response": "The CSVD exposure block includes \"silent infarct*\"[tiab]. The packet records a complete re-evaluation, full benchmark retrieval, and refreshed optional-block samples and decisions."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

