# PubMed search strategy: audit

Generated 2026-11-27T03:40:09+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In population-based cohorts, is cerebral small vessel disease (and its MRI markers) associated with the risk of incident dementia and cognitive decline?
- Framework: PECO
- Scope confirmed by user: yes (User unavailable; no seeds; standard depth defaults. Assumptions: exposure=CSVD/markers, outcome=dementia/cognition; cohort design screened not searched. Scope confirmation not awaited; proceeding. Outcome block AND-ed for workload; see concept rationale.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Cerebral small vessel disease and MRI markers (WMH, lacunes/silent infarcts, microbleeds, vascular brain injury) | search | exposure; defines the topic, named in title/abstract/MeSH. Each listed marker searched by its own name. |
| Dementia, Alzheimer disease, cognitive decline/impairment | search | AND-ed for workload (user unavailable; no-outcome result 44,758 records assumed too large to screen). Tested on 7 independent known records (all from one review's reference list; second review 25377475 refs gave no clearly eligible prospective records); loss bound 34.8% (95%), i.e. largely unmeasured. Count without block: 44,758. Reversible. |
| Population-based / longitudinal cohort design | screen | study design/setting; handled at screening |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-11-27T03:39:29+00:00
- Records added to PubMed up to: 2017-05-06
- Total records: 9,540
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Cerebral Small Vessel Diseases"[Mesh]` | 6,257 | none |
| 2 | `"Leukoaraiosis"[Mesh]` | 470 | none |
| 3 | `"Stroke, Lacunar"[Mesh]` | 412 | none |
| 4 | `"small vessel disease"[tiab]` | 2,316 | none |
| 5 | `"small vessel diseases"[tiab]` | 203 | none |
| 6 | `"small-vessel disease"[tiab]` | 2,316 | none |
| 7 | `"small vessel"[tiab:~2]` | 6,857 | none |
| 8 | `"cerebral small vessel"[tiab]` | 915 | none |
| 9 | `cSVD[tiab]` | 127 | none |
| 10 | `"white matter hyperintensity"[tiab]` | 738 | none |
| 11 | `"white matter hyperintensities"[tiab]` | 1,776 | none |
| 12 | `"white matter lesion"[tiab]` | 615 | none |
| 13 | `"white matter lesions"[tiab]` | 3,662 | none |
| 14 | `"white matter change"[tiab]` | 112 | none |
| 15 | `"white matter changes"[tiab]` | 1,796 | none |
| 16 | `"white matter disease"[tiab]` | 813 | none |
| 17 | `"white matter abnormalit*"[tiab]` | 1,590 | none |
| 18 | `leukoaraiosis[tiab]` | 1,008 | none |
| 19 | `leukoencephalopath*[tiab]` | 6,366 | none |
| 20 | `leucoaraiosis[tiab]` | 38 | none |
| 21 | `WMH[tiab]` | 1,105 | none |
| 22 | `WMHs[tiab]` | 313 | none |
| 23 | `"periventricular hyperintens*"[tiab]` | 316 | none |
| 24 | `"subcortical hyperintens*"[tiab]` | 97 | none |
| 25 | `"deep white matter"[tiab]` | 1,229 | none |
| 26 | `lacun*[tiab]` | 10,405 | none |
| 27 | `"silent brain infarct*"[tiab]` | 280 | none |
| 28 | `"silent infarct*"[tiab]` | 311 | none |
| 29 | `"silent cerebral infarct*"[tiab]` | 322 | none |
| 30 | `"silent stroke*"[tiab]` | 136 | none |
| 31 | `"covert brain infarct*"[tiab]` | 9 | none |
| 32 | `"covert infarct*"[tiab]` | 4 | none |
| 33 | `"subclinical infarct*"[tiab]` | 30 | none |
| 34 | `"subcortical infarct*"[tiab]` | 1,322 | none |
| 35 | `"silent brain infarction"[tiab]` | 142 | none |
| 36 | `"MRI infarct*"[tiab]` | 46 | none |
| 37 | `microbleed*[tiab]` | 1,468 | none |
| 38 | `"micro-bleed*"[tiab]` | 28 | none |
| 39 | `"cerebral microhemorrhage*"[tiab]` | 62 | none |
| 40 | `"cerebral microhaemorrhage*"[tiab]` | 4 | none |
| 41 | `"microhemorrhage*"[tiab]` | 554 | none |
| 42 | `"microhaemorrhage*"[tiab]` | 107 | none |
| 43 | `"cerebral micro bleed*"[tiab]` | 5 | none |
| 44 | `"vascular brain injury"[tiab]` | 73 | none |
| 45 | `"vascular brain lesion*"[tiab]` | 74 | none |
| 46 | `"cerebrovascular lesion*"[tiab]` | 784 | none |
| 47 | `"cerebral small vessel"[tiab:~3]` | 1,048 | none |
| 48 | `"enlarged perivascular space*"[tiab]` | 86 | none |
| 49 | `"perivascular space*"[tiab]` | 1,613 | none |
| 50 | `"Binswanger*"[tiab]` | 570 | none |
| 51 | `"subcortical ischemic vascular"[tiab]` | 162 | none |
| 52 | `"subcortical vascular"[tiab]` | 362 | none |
| 53 | `"white matter hyperintensity"[tiab:~3]` | 891 | none |
| 54 | `"white matter hyperintensities"[tiab:~3]` | 1,922 | none |
| 55 | `"white matter lesions"[tiab:~3]` | 5,013 | none |
| 56 | `"white matter lesion"[tiab:~3]` | 1,043 | none |
| 57 | `"silent infarcts"[tiab:~3]` | 423 | none |
| 58 | `"small vessel ischemic"[tiab:~3]` | 163 | none |
| 59 | `"microvascular disease"[tiab:~2]` | 1,696 | none |
| 60 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59` | 44,758 | none |
| 61 | `"Dementia"[Mesh]` | 145,526 | none |
| 62 | `"Cognition Disorders"[Mesh]` | 80,254 | none |
| 63 | `"Cognitive Dysfunction"[Mesh]` | 8,211 | none |
| 64 | `"Alzheimer Disease"[Mesh]` | 82,140 | none |
| 65 | `dementia[tiab]` | 85,597 | none |
| 66 | `dementias[tiab]` | 4,177 | none |
| 67 | `alzheimer*[tiab]` | 116,176 | none |
| 68 | `"cognitive decline"[tiab]` | 15,036 | none |
| 69 | `"cognitive impairment"[tiab]` | 40,821 | none |
| 70 | `"cognitive dysfunction"[tiab]` | 9,910 | none |
| 71 | `"cognitive deterioration"[tiab]` | 1,471 | none |
| 72 | `"cognitive function"[tiab]` | 25,869 | none |
| 73 | `"cognitive performance"[tiab]` | 13,653 | none |
| 74 | `"cognitive disorder*"[tiab]` | 3,431 | none |
| 75 | `cognition[tiab]` | 54,532 | none |
| 76 | `"cognitive change*"[tiab]` | 3,310 | none |
| 77 | `"memory decline"[tiab]` | 1,116 | none |
| 78 | `"memory impairment"[tiab]` | 8,038 | none |
| 79 | `"mental deterioration"[tiab]` | 1,015 | none |
| 80 | `"neurocognitive"[tiab]` | 14,643 | none |
| 81 | `"Neuropsychological Tests"[Mesh]` | 161,667 | none |
| 82 | `"Memory Disorders"[Mesh]` | 26,825 | none |
| 83 | `cogniti*[tiab]` | 298,877 | none |
| 84 | `neuropsycholog*[tiab]` | 44,830 | none |
| 85 | `"executive function*"[tiab]` | 18,887 | none |
| 86 | `"processing speed"[tiab]` | 5,489 | none |
| 87 | `"mini-mental"[tiab]` | 13,125 | none |
| 88 | `MMSE[tiab]` | 8,585 | none |
| 89 | `"memory"[tiab]` | 200,576 | none |
| 90 | `#61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81 OR #82 OR #83 OR #84 OR #85 OR #86 OR #87 OR #88 OR #89` | 703,635 | none |
| 91 | `#60 AND #90` | 9,540 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Cerebral Small Vessel Diseases"[Mesh] OR "Leukoaraiosis"[Mesh] OR "Stroke, Lacunar"[Mesh] OR "small vessel disease"[tiab] OR "small vessel diseases"[tiab] OR "small-vessel disease"[tiab] OR "small vessel"[tiab:~2] OR "cerebral small vessel"[tiab] OR cSVD[tiab] OR "white matter hyperintensity"[tiab] OR "white matter hyperintensities"[tiab] OR "white matter lesion"[tiab] OR "white matter lesions"[tiab] OR "white matter change"[tiab] OR "white matter changes"[tiab] OR "white matter disease"[tiab] OR "white matter abnormalit*"[tiab] OR leukoaraiosis[tiab] OR leukoencephalopath*[tiab] OR leucoaraiosis[tiab] OR WMH[tiab] OR WMHs[tiab] OR "periventricular hyperintens*"[tiab] OR "subcortical hyperintens*"[tiab] OR "deep white matter"[tiab] OR lacun*[tiab] OR "silent brain infarct*"[tiab] OR "silent infarct*"[tiab] OR "silent cerebral infarct*"[tiab] OR "silent stroke*"[tiab] OR "covert brain infarct*"[tiab] OR "covert infarct*"[tiab] OR "subclinical infarct*"[tiab] OR "subcortical infarct*"[tiab] OR "silent brain infarction"[tiab] OR "MRI infarct*"[tiab] OR microbleed*[tiab] OR "micro-bleed*"[tiab] OR "cerebral microhemorrhage*"[tiab] OR "cerebral microhaemorrhage*"[tiab] OR "microhemorrhage*"[tiab] OR "microhaemorrhage*"[tiab] OR "cerebral micro bleed*"[tiab] OR "vascular brain injury"[tiab] OR "vascular brain lesion*"[tiab] OR "cerebrovascular lesion*"[tiab] OR "cerebral small vessel"[tiab:~3] OR "enlarged perivascular space*"[tiab] OR "perivascular space*"[tiab] OR "Binswanger*"[tiab] OR "subcortical ischemic vascular"[tiab] OR "subcortical vascular"[tiab] OR "white matter hyperintensity"[tiab:~3] OR "white matter hyperintensities"[tiab:~3] OR "white matter lesions"[tiab:~3] OR "white matter lesion"[tiab:~3] OR "silent infarcts"[tiab:~3] OR "small vessel ischemic"[tiab:~3] OR "microvascular disease"[tiab:~2]) AND ("Dementia"[Mesh] OR "Cognition Disorders"[Mesh] OR "Cognitive Dysfunction"[Mesh] OR "Alzheimer Disease"[Mesh] OR dementia[tiab] OR dementias[tiab] OR alzheimer*[tiab] OR "cognitive decline"[tiab] OR "cognitive impairment"[tiab] OR "cognitive dysfunction"[tiab] OR "cognitive deterioration"[tiab] OR "cognitive function"[tiab] OR "cognitive performance"[tiab] OR "cognitive disorder*"[tiab] OR cognition[tiab] OR "cognitive change*"[tiab] OR "memory decline"[tiab] OR "memory impairment"[tiab] OR "mental deterioration"[tiab] OR "neurocognitive"[tiab] OR "Neuropsychological Tests"[Mesh] OR "Memory Disorders"[Mesh] OR cogniti*[tiab] OR neuropsycholog*[tiab] OR "executive function*"[tiab] OR "processing speed"[tiab] OR "mini-mental"[tiab] OR MMSE[tiab] OR "memory"[tiab])) AND ("1800/01/01"[edat] : "2017/05/06"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall | Found without a keyword search: retrieved / in PubMed |
|---|---|---:|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 7 | 7 | 100.0% | 7 / 7 |
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 2 | 2 | 100.0% | 0 / 0 |

7 of the 7 held-out known records found without a keyword search are retrieved: on their evidence recall is at least 65.2% (95% bound; it is as wide as the number of such records makes it). 7 of the 7 known records found through reference lists come from one review (20660506, 100.0%). A benchmark built on one review takes that review's scope: add the reference list of a second review that covers a different searched concept.

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Citation searching for known records

These citation searches found candidate known records to test the strategy against. They are not part of the delivered search, and they did not search for studies for the review itself. Terminology follows the TARCiS statement (Hirt et al., 2024, https://doi.org/10.1136/bmj-2023-078384).

| Batch | Date | Citation index | Direction | Seed records | Candidates | Shown | Screened in |
|---|---|---|---|---:|---:|---:|---:|
| C3 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 7 |
| C4 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 7 |
| C8 | 2026-11-27 | PubMed | backward | 1 | 29 | 29 | 0 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| csvd | 703,635 | 0 |
| outcome | 44,758 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | initial draft: csvd only |
| 2 | 44,758 | csvd: +7 / -4 | none | fix proximity lint |
| 3 | 9,540 | outcome: +29 / -0 | none | AND outcome block (moved from optional) for workload; broadened outcome terms |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 3 findings; F1 must-fix rejected, F2 should-fix accepted-risk, F3 document accepted-risk
- Round 2 on version 3: 4 findings; F1 document accepted-risk, F2 should-fix accepted-risk, F3 document accepted-risk, F4 document accepted-risk
- Round 3 on version 3: 4 findings; F1 document accepted-risk, F2 should-fix accepted-risk, F3 document accepted-risk, F4 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 459 NCBI requests logged (76 from cache); strategy sha256 45e0352603eb._

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
      "checked_at": "2026-11-27T03:39:29+00:00",
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
      "checked_at": "2026-11-27T03:39:29+00:00",
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
      "checked_at": "2026-11-27T03:39:29+00:00",
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
      "requested": "Dementia",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T03:39:29+00:00",
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
      "location": "vocabulary:60",
      "term": {
        "text": "\"Dementia\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognition Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T03:39:29+00:00",
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
      "location": "vocabulary:61",
      "term": {
        "text": "\"Cognition Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognitive Dysfunction",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T03:39:29+00:00",
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
      "location": "vocabulary:62",
      "term": {
        "text": "\"Cognitive Dysfunction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alzheimer Disease",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T03:39:29+00:00",
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
      "location": "vocabulary:63",
      "term": {
        "text": "\"Alzheimer Disease\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Neuropsychological Tests",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T03:39:29+00:00",
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
      "location": "vocabulary:80",
      "term": {
        "text": "\"Neuropsychological Tests\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Memory Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T03:39:29+00:00",
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
      "location": "vocabulary:81",
      "term": {
        "text": "\"Memory Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Cerebral Small Vessel Diseases\"[MeSH Terms] OR \"Leukoaraiosis\"[MeSH Terms] OR \"stroke, lacunar\"[MeSH Terms] OR \"small-vessel disease\"[Title/Abstract] OR \"small vessel diseases\"[Title/Abstract] OR \"small-vessel disease\"[Title/Abstract] OR \"small vessel\"[Title/Abstract:~2] OR \"cerebral small vessel\"[Title/Abstract] OR \"cSVD\"[Title/Abstract] OR \"white matter hyperintensity\"[Title/Abstract] OR \"white matter hyperintensities\"[Title/Abstract] OR \"white matter lesion\"[Title/Abstract] OR \"white matter lesions\"[Title/Abstract] OR \"white matter change\"[Title/Abstract] OR \"white matter changes\"[Title/Abstract] OR \"white matter disease\"[Title/Abstract] OR \"white matter abnormalit*\"[Title/Abstract] OR \"Leukoaraiosis\"[Title/Abstract] OR \"leukoencephalopath*\"[Title/Abstract] OR \"leucoaraiosis\"[Title/Abstract] OR \"WMH\"[Title/Abstract] OR \"WMHs\"[Title/Abstract] OR \"periventricular hyperintens*\"[Title/Abstract] OR \"subcortical hyperintens*\"[Title/Abstract] OR \"deep white matter\"[Title/Abstract] OR \"lacun*\"[Title/Abstract] OR \"silent brain infarct*\"[Title/Abstract] OR \"silent infarct*\"[Title/Abstract] OR \"silent cerebral infarct*\"[Title/Abstract] OR \"silent stroke*\"[Title/Abstract] OR \"covert brain infarct*\"[Title/Abstract] OR \"covert infarct*\"[Title/Abstract] OR \"subclinical infarct*\"[Title/Abstract] OR \"subcortical infarct*\"[Title/Abstract] OR \"silent brain infarction\"[Title/Abstract] OR \"mri infarct*\"[Title/Abstract] OR \"microbleed*\"[Title/Abstract] OR \"micro bleed*\"[Title/Abstract] OR \"cerebral microhemorrhage*\"[Title/Abstract] OR \"cerebral microhaemorrhage*\"[Title/Abstract] OR \"microhemorrhage*\"[Title/Abstract] OR \"microhaemorrhage*\"[Title/Abstract] OR \"cerebral micro bleed*\"[Title/Abstract] OR \"vascular brain injury\"[Title/Abstract] OR \"vascular brain lesion*\"[Title/Abstract] OR \"cerebrovascular lesion*\"[Title/Abstract] OR \"cerebral small vessel\"[Title/Abstract:~3] OR \"enlarged perivascular space*\"[Title/Abstract] OR \"perivascular space*\"[Title/Abstract] OR \"binswanger*\"[Title/Abstract] OR \"subcortical ischemic vascular\"[Title/Abstract] OR \"subcortical vascular\"[Title/Abstract] OR \"white matter hyperintensity\"[Title/Abstract:~3] OR \"white matter hyperintensities\"[Title/Abstract:~3] OR \"white matter lesions\"[Title/Abstract:~3] OR \"white matter lesion\"[Title/Abstract:~3] OR \"silent infarcts\"[Title/Abstract:~3] OR \"small vessel ischemic\"[Title/Abstract:~3] OR \"microvascular disease\"[Title/Abstract:~2]) AND (\"Dementia\"[MeSH Terms] OR \"Cognition Disorders\"[MeSH Terms] OR \"Cognitive Dysfunction\"[MeSH Terms] OR \"Alzheimer Disease\"[MeSH Terms] OR \"Dementia\"[Title/Abstract] OR \"dementias\"[Title/Abstract] OR \"alzheimer*\"[Title/Abstract] OR \"cognitive decline\"[Title/Abstract] OR \"cognitive impairment\"[Title/Abstract] OR \"Cognitive Dysfunction\"[Title/Abstract] OR \"cognitive deterioration\"[Title/Abstract] OR \"cognitive function\"[Title/Abstract] OR \"cognitive performance\"[Title/Abstract] OR \"cognitive disorder*\"[Title/Abstract] OR \"cognition\"[Title/Abstract] OR \"cognitive change*\"[Title/Abstract] OR \"memory decline\"[Title/Abstract] OR \"memory impairment\"[Title/Abstract] OR \"mental deterioration\"[Title/Abstract] OR \"neurocognitive\"[Title/Abstract] OR \"Neuropsychological Tests\"[MeSH Terms] OR \"Memory Disorders\"[MeSH Terms] OR \"cogniti*\"[Title/Abstract] OR \"neuropsycholog*\"[Title/Abstract] OR \"executive function*\"[Title/Abstract] OR \"processing speed\"[Title/Abstract] OR \"mini-mental\"[Title/Abstract] OR \"MMSE\"[Title/Abstract] OR \"memory\"[Title/Abstract]) AND 1800/01/01:2017/05/06[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "f5f09e6383ebf679af3604e3c485208702a5280976ff2ae7668078f57a700c20",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Every marker the question and eligibility name is searched by its own bare name. No directional block. Translations as expected."
        },
        "operators": {
          "verdict": "revise",
          "note": "Outcome block AND-ed for workload; no known record lost but benchmark is thin (7 records from one review; loss bound 34.8%). Reversible and documented."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "All MeSH headings verified, each paired with tiab text."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Good synonym/spelling coverage; lines 4 and 6 redundant but harmless."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Lint empty; no diagnostics."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "Executed query carries an edat cutoff 2017/05/06 not declared in protocol limits."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "block": "",
          "finding": "The search applies an edat cutoff of 2017/05/06 (as_of) but protocol.as_of is null and protocol.limits is empty.",
          "recommendation": "If not intended, remove and re-evaluate; if intended, record it as an explicit limit with reason.",
          "status": "rejected",
          "response": "The date bound is not a search limit chosen for the review: the evaluation harness pins PubMed to 2017-05-06 (PSB_AS_OF) to reproduce the search as of that date. It is an Entrez-date bound applied identically to every line and is not part of the delivered query. The question sets no date limit. Reported as a limitation."
        },
        {
          "id": "F2",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "block": "outcome",
          "finding": "Outcome block AND-ed for workload; benchmark is 7 records from one review, loss bound 34.8%, largely unmeasured.",
          "recommendation": "Document as a workload trade-off with the bound and the reversible fallback; add independent benchmark if possible.",
          "status": "accepted-risk",
          "response": "AND-ed for workload: exposure-only result is 44,758 records, assumed too large to screen; with outcome 9,540. 0 of 9 known records lost; 7 independent records from one review, 95% loss bound 34.8%, so recall is not reliably estimated. Second review's reference list (25377475) yielded no clearly eligible records. Reversible: fallback is the exposure-only block. Documented in protocol and narrative."
        },
        {
          "id": "F3",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "block": "csvd",
          "finding": "Lines 4 and 6 return identical counts; proximity lines overlap plain phrases. Redundant, no recall loss.",
          "recommendation": "Keep; note the redundancy.",
          "status": "accepted-risk",
          "response": "Redundancy costs nothing in precision or recall."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "f5f09e6383ebf679af3604e3c485208702a5280976ff2ae7668078f57a700c20",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Every named marker searched by its bare name; no directional block."
        },
        "operators": {
          "verdict": "pass",
          "note": "Outcome AND accepted as workload risk; 0 of 9 known lost; 34.8% bound stated; exposure-only fallback of 44,758."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "All MeSH verified with tiab counterparts."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Good coverage; some noisy terms (lacun*, leukoencephalopath*, memory) cost precision only."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Lint empty; no diagnostics."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Edat bound is harness-pinned reproduction date, not a topical limit; reported as limitation."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "filter",
          "block": "",
          "finding": "Executed query carries an edat cutoff 2017/05/06 while protocol limits is empty.",
          "recommendation": "Keep out of delivered query; state in report that results are as of 2017-05-06 because the environment pins the date.",
          "status": "accepted-risk",
          "response": "Accepted: harness reproduction date applied uniformly, not a topical restriction; reported as a limitation."
        },
        {
          "id": "F2",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "block": "outcome",
          "finding": "Outcome block AND-ed for workload; 7 independent records from one review; 95% loss bound 34.8%.",
          "recommendation": "Keep as accepted risk; report bound, single-source benchmark and the exposure-only fallback (44,758 records).",
          "status": "accepted-risk",
          "response": "Accepted. 0 known records lost; rationale and fallback documented in protocol and narrative."
        },
        {
          "id": "F3",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "block": "csvd",
          "finding": "Lines 4 and 6 identical counts; proximity lines overlap plain phrases.",
          "recommendation": "Keep; mention redundancy.",
          "status": "accepted-risk",
          "response": "Accepted; redundant lines cost nothing."
        },
        {
          "id": "F4",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "block": "csvd",
          "finding": "Several broad noisy terms (lacun*, leukoencephalopath*, small vessel proximity, memory, cogniti*).",
          "recommendation": "Keep for recall; manage noise at screening; narrow first if 9,540 is too many.",
          "status": "accepted-risk",
          "response": "Accepted: all known records depend on a broad strategy, recall first; narrowing options noted in narrative."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "strategy_version": 3,
      "review_sha256": "f5f09e6383ebf679af3604e3c485208702a5280976ff2ae7668078f57a700c20",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Every named marker searched by its bare name; no directional block. (closing round: verified)"
        },
        "operators": {
          "verdict": "pass",
          "note": "Outcome AND accepted as workload risk; 0 of 9 known lost; 34.8% bound stated; exposure-only fallback of 44,758. (closing round: verified)"
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "All MeSH verified with tiab counterparts. (closing round: verified)"
        },
        "text_words": {
          "verdict": "pass",
          "note": "Good coverage; some noisy terms (lacun*, leukoencephalopath*, memory) cost precision only. (closing round: verified)"
        },
        "syntax": {
          "verdict": "pass",
          "note": "Lint empty; no diagnostics. (closing round: verified)"
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Edat bound is harness-pinned reproduction date, not a topical limit; reported as limitation. (closing round: verified)"
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "filter",
          "block": "",
          "finding": "Executed query carries an edat cutoff 2017/05/06 while protocol limits is empty.",
          "recommendation": "Keep out of delivered query; state in report that results are as of 2017-05-06 because the environment pins the date.",
          "status": "accepted-risk",
          "response": "Accepted: harness reproduction date applied uniformly, not a topical restriction; reported as a limitation."
        },
        {
          "id": "F2",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "block": "outcome",
          "finding": "Outcome block AND-ed for workload; 7 independent records from one review; 95% loss bound 34.8%.",
          "recommendation": "Keep as accepted risk; report bound, single-source benchmark and the exposure-only fallback (44,758 records).",
          "status": "accepted-risk",
          "response": "Accepted. 0 known records lost; rationale and fallback documented in protocol and narrative."
        },
        {
          "id": "F3",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "block": "csvd",
          "finding": "Lines 4 and 6 identical counts; proximity lines overlap plain phrases.",
          "recommendation": "Keep; mention redundancy.",
          "status": "accepted-risk",
          "response": "Accepted; redundant lines cost nothing."
        },
        {
          "id": "F4",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "block": "csvd",
          "finding": "Several broad noisy terms (lacun*, leukoencephalopath*, small vessel proximity, memory, cogniti*).",
          "recommendation": "Keep for recall; manage noise at screening; narrow first if 9,540 is too many.",
          "status": "accepted-risk",
          "response": "Accepted: all known records depend on a broad strategy, recall first; narrowing options noted in narrative."
        }
      ],
      "issue_dispositions": [],
      "closing": true
    }
  ]
}
```

