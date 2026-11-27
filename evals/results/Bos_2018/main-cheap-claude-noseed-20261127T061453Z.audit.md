# PubMed search strategy: audit

Generated 2026-11-27T06:23:35+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In population-based cohorts, is cerebral small vessel disease (and its MRI markers) associated with the risk of incident dementia and cognitive decline?
- Framework: PECO
- Scope confirmed by user: yes (User unavailable; proceeded without answers. Assumptions: no known articles, standard depth, no limits. Exposure vs outcome interpreted as PECO per question wording (cSVD = exposure; dementia/cognition = outcome). Scope not paused for confirmation by user instruction. Outcome block AND-ed for workload (see concept rationale); recall loss unmeasured. No independent known records beyond one review's reference list; recall is a lower bound only on those 7.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Cerebral small vessel disease and MRI markers (WMH, lacunes/silent infarcts, microbleeds, vascular brain injury) | search | the exposure; defines the topic; every relevant record involves it; named in title/abstract and MeSH |
| Incident dementia, Alzheimer disease, cognitive decline/impairment | search | AND-ed FOR WORKLOAD, not on evidence. Without it the exposure-only result is 28,723 records (too large to screen; assumed >10,000). With it: 7,947 (v6). Independent evidence: 0 of 7 benchmark records (reference list of one review, 20660506) lost; 95% bound on share lost 34.8%. The 6 pilot-derived 'relevant' records are not independent and are not counted in the bound. Reference lists of 4 reviews examined (20660506, 25377475, 25827412, 29213989); only the first yielded eligible records. Block kept broad (bare cognitive/cognition, MeSH Dementia, Cognition Disorders, Cognitive Dysfunction, Alzheimer Disease). Reversible: drop block for 28,723. The 10,000-record threshold for 'too large to screen' is an assumption (user unavailable). |
| Population-based / longitudinal cohort | screen | design/setting; judged at screening; not reliably named in abstracts |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-11-27T06:23:01+00:00
- Records added to PubMed up to: 2017-05-06
- Total records: 7,947
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
| 7 | `"small vessel ischemic disease"[tiab]` | 15 | none |
| 8 | `"small vessel ischaemic disease"[tiab]` | 3 | none |
| 9 | `"small vessel disease burden"[tiab]` | 6 | none |
| 10 | `"cerebral microangiopath*"[tiab]` | 150 | none |
| 11 | `"white matter hyperintensit*"[tiab]` | 2,313 | none |
| 12 | `"white matter lesion*"[tiab]` | 4,051 | none |
| 13 | `"white matter change*"[tiab]` | 1,880 | none |
| 14 | `"white matter disease"[tiab]` | 813 | none |
| 15 | `"white matter abnormalit*"[tiab]` | 1,590 | none |
| 16 | `"white matter damage"[tiab]` | 1,050 | none |
| 17 | `"white matter hypodensit*"[tiab]` | 78 | none |
| 18 | `"white matter signal abnormalit*"[tiab]` | 78 | none |
| 19 | `WMH[tiab]` | 1,105 | none |
| 20 | `WMHs[tiab]` | 313 | none |
| 21 | `leukoaraiosis[tiab]` | 1,008 | none |
| 22 | `"leuko-araiosis"[tiab]` | 76 | none |
| 23 | `"subcortical hyperintensit*"[tiab]` | 85 | none |
| 24 | `"periventricular hyperintensit*"[tiab]` | 307 | none |
| 25 | `"deep white matter"[tiab]` | 1,229 | none |
| 26 | `"T2 hyperintensit*"[tiab]` | 565 | none |
| 27 | `"Binswanger*"[tiab]` | 570 | none |
| 28 | `"lacunar infarct*"[tiab]` | 2,251 | none |
| 29 | `"lacunar stroke*"[tiab]` | 918 | none |
| 30 | `lacune*[tiab]` | 686 | none |
| 31 | `"silent brain infarct*"[tiab]` | 280 | none |
| 32 | `"silent cerebral infarct*"[tiab]` | 322 | none |
| 33 | `"silent infarct*"[tiab]` | 311 | none |
| 34 | `"silent stroke*"[tiab]` | 136 | none |
| 35 | `"covert brain infarct*"[tiab]` | 9 | none |
| 36 | `"covert vascular"[tiab]` | 5 | none |
| 37 | `"subclinical brain infarct*"[tiab]` | 16 | none |
| 38 | `"subcortical infarct*"[tiab]` | 1,322 | none |
| 39 | `"small subcortical infarct*"[tiab]` | 84 | none |
| 40 | `microinfarct*[tiab]` | 605 | none |
| 41 | `microbleed*[tiab]` | 1,468 | none |
| 42 | `"micro-bleed*"[tiab]` | 28 | none |
| 43 | `"microhemorrhage*"[tiab]` | 554 | none |
| 44 | `"microhaemorrhage*"[tiab]` | 107 | none |
| 45 | `"micro-hemorrhage*"[tiab]` | 41 | none |
| 46 | `"cerebral microhemorrhage*"[tiab]` | 62 | none |
| 47 | `"brain microbleed*"[tiab]` | 59 | none |
| 48 | `"cerebral microbleed*"[tiab]` | 710 | none |
| 49 | `CMBs[tiab]` | 348 | none |
| 50 | `"vascular brain injury"[tiab]` | 73 | none |
| 51 | `"vascular brain lesion*"[tiab]` | 74 | none |
| 52 | `"cerebrovascular lesion*"[tiab]` | 784 | none |
| 53 | `"subclinical cerebrovascular"[tiab]` | 67 | none |
| 54 | `"silent cerebrovascular"[tiab]` | 84 | none |
| 55 | `"MRI marker*"[tiab]` | 301 | none |
| 56 | `"MRI-defined"[tiab]` | 284 | none |
| 57 | `"subcortical vascular"[tiab]` | 362 | none |
| 58 | `"subcortical ischemic vascular"[tiab]` | 162 | none |
| 59 | `"white matter hyperdensit*"[tiab]` | 2 | none |
| 60 | `Virchow-Robin[tiab]` | 444 | none |
| 61 | `"perivascular space*"[tiab]` | 1,613 | none |
| 62 | `"enlarged perivascular"[tiab]` | 89 | none |
| 63 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62` | 28,723 | none |
| 64 | `"Dementia"[Mesh]` | 145,526 | none |
| 65 | `"Cognition Disorders"[Mesh]` | 80,254 | none |
| 66 | `"Cognitive Dysfunction"[Mesh]` | 8,211 | none |
| 67 | `"Alzheimer Disease"[Mesh]` | 82,140 | none |
| 68 | `dementia[tiab]` | 85,597 | none |
| 69 | `dementias[tiab]` | 4,177 | none |
| 70 | `Alzheimer*[tiab]` | 116,176 | none |
| 71 | `"cognitive decline"[tiab]` | 15,036 | none |
| 72 | `"cognitive impairment"[tiab]` | 40,821 | none |
| 73 | `"cognitive dysfunction"[tiab]` | 9,910 | none |
| 74 | `"cognitive deterioration"[tiab]` | 1,471 | none |
| 75 | `"cognitive function"[tiab]` | 25,869 | none |
| 76 | `"cognitive performance"[tiab]` | 13,653 | none |
| 77 | `"mild cognitive impairment"[tiab]` | 11,353 | none |
| 78 | `"memory decline"[tiab]` | 1,116 | none |
| 79 | `neurocognitive[tiab]` | 14,643 | none |
| 80 | `cogniti*[tiab]` | 298,877 | none |
| 81 | `"Cognition"[Mesh]` | 138,866 | none |
| 82 | `#64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75 OR #76 OR #77 OR #78 OR #79 OR #80 OR #81` | 543,391 | none |
| 83 | `#63 AND #82` | 7,947 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Cerebral Small Vessel Diseases"[Mesh] OR "Leukoaraiosis"[Mesh] OR "Stroke, Lacunar"[Mesh] OR "small vessel disease"[tiab] OR "small vessel diseases"[tiab] OR "small-vessel disease"[tiab] OR "small vessel ischemic disease"[tiab] OR "small vessel ischaemic disease"[tiab] OR "small vessel disease burden"[tiab] OR "cerebral microangiopath*"[tiab] OR "white matter hyperintensit*"[tiab] OR "white matter lesion*"[tiab] OR "white matter change*"[tiab] OR "white matter disease"[tiab] OR "white matter abnormalit*"[tiab] OR "white matter damage"[tiab] OR "white matter hypodensit*"[tiab] OR "white matter signal abnormalit*"[tiab] OR WMH[tiab] OR WMHs[tiab] OR leukoaraiosis[tiab] OR "leuko-araiosis"[tiab] OR "subcortical hyperintensit*"[tiab] OR "periventricular hyperintensit*"[tiab] OR "deep white matter"[tiab] OR "T2 hyperintensit*"[tiab] OR "Binswanger*"[tiab] OR "lacunar infarct*"[tiab] OR "lacunar stroke*"[tiab] OR lacune*[tiab] OR "silent brain infarct*"[tiab] OR "silent cerebral infarct*"[tiab] OR "silent infarct*"[tiab] OR "silent stroke*"[tiab] OR "covert brain infarct*"[tiab] OR "covert vascular"[tiab] OR "subclinical brain infarct*"[tiab] OR "subcortical infarct*"[tiab] OR "small subcortical infarct*"[tiab] OR microinfarct*[tiab] OR microbleed*[tiab] OR "micro-bleed*"[tiab] OR "microhemorrhage*"[tiab] OR "microhaemorrhage*"[tiab] OR "micro-hemorrhage*"[tiab] OR "cerebral microhemorrhage*"[tiab] OR "brain microbleed*"[tiab] OR "cerebral microbleed*"[tiab] OR CMBs[tiab] OR "vascular brain injury"[tiab] OR "vascular brain lesion*"[tiab] OR "cerebrovascular lesion*"[tiab] OR "subclinical cerebrovascular"[tiab] OR "silent cerebrovascular"[tiab] OR "MRI marker*"[tiab] OR "MRI-defined"[tiab] OR "subcortical vascular"[tiab] OR "subcortical ischemic vascular"[tiab] OR "white matter hyperdensit*"[tiab] OR Virchow-Robin[tiab] OR "perivascular space*"[tiab] OR "enlarged perivascular"[tiab]) AND ("Dementia"[Mesh] OR "Cognition Disorders"[Mesh] OR "Cognitive Dysfunction"[Mesh] OR "Alzheimer Disease"[Mesh] OR dementia[tiab] OR dementias[tiab] OR Alzheimer*[tiab] OR "cognitive decline"[tiab] OR "cognitive impairment"[tiab] OR "cognitive dysfunction"[tiab] OR "cognitive deterioration"[tiab] OR "cognitive function"[tiab] OR "cognitive performance"[tiab] OR "mild cognitive impairment"[tiab] OR "memory decline"[tiab] OR neurocognitive[tiab] OR cogniti*[tiab] OR "Cognition"[Mesh])) AND ("1800/01/01"[edat] : "2017/05/06"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall | Found without a keyword search: retrieved / in PubMed |
|---|---|---:|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 7 | 7 | 100.0% | 7 / 7 |
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 6 | 6 | 100.0% | 0 / 0 |

7 of the 7 held-out known records found without a keyword search are retrieved: on their evidence recall is at least 65.2% (95% bound; it is as wide as the number of such records makes it). 7 of the 7 known records found through reference lists come from one review (20660506, 100.0%). A benchmark built on one review takes that review's scope: add the reference list of a second review that covers a different searched concept.

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Citation searching for known records

These citation searches found candidate known records to test the strategy against. They are not part of the delivered search, and they did not search for studies for the review itself. Terminology follows the TARCiS statement (Hirt et al., 2024, https://doi.org/10.1136/bmj-2023-078384).

| Batch | Date | Citation index | Direction | Seed records | Candidates | Shown | Screened in |
|---|---|---|---|---:|---:|---:|---:|
| C4 | 2026-11-27 | PubMed | backward | 1 | 29 | 29 | 0 |
| C5 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 0 |
| C6 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 0 |
| C7 | 2026-11-27 | PubMed | backward | 1 | 29 | 29 | 0 |
| C8 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 0 |
| C10 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 7 |
| C11 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 7 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| csvd | 543,391 | 0 |
| outcome | 28,723 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 49,079 | initial | none | initial draft: csvd block + optional outcome |
| 2 | 49,079 | csvd: +0 / -1 | none | remove cerebral CMB; term impact |
| 3 | 27,031 | csvd: +0 / -9 | none | drop noisy terms: microangiopath*, leukoencephalopath*, brain infarct*, cerebral white matter, bare lacunar, CAA, CADASIL, perivascular spaces, VCI (term-impact: no known records unique) |
| 4 | 7,788 | outcome: +18 / -0 | none | AND outcome block for workload (27,031 -> 7,788; 0 known lost) |
| 5 | 7,819 | csvd: +2 / -3 | none | remove 3 zero-hit terms (leukoaraioses, covert cerebral infarct*, vascular lesions of the brain); add white matter hyperdensit*, Virchow-Robin |
| 6 | 7,947 | csvd: +2 / -0; outcome: +2 / -2 | none | add perivascular space*, enlarged perivascular (F2); cogniti* + Cognition MeSH replace cognitive/cognition (F4) |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5 (fresh-context subagent): 4 findings; F1 should-fix open, F2 should-fix open, F3 should-fix open, F4 document open
- Round 2 on version 6 (fresh-context subagent): 6 findings; F1 should-fix resolved, F2 should-fix resolved, F3 should-fix resolved, F4 document resolved, N1 document accepted-risk, N2 document accepted-risk
- Round 3 on version 6 (fresh-context subagent): 7 findings; F1 should-fix resolved, F2 should-fix resolved, F3 should-fix resolved, F4 document resolved, N1 document accepted-risk, N2 document accepted-risk, N3 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1267 NCBI requests logged (838 from cache); strategy sha256 cad597872d58._

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
      "checked_at": "2026-11-27T06:23:01+00:00",
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
      "checked_at": "2026-11-27T06:23:01+00:00",
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
      "checked_at": "2026-11-27T06:23:01+00:00",
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
      "checked_at": "2026-11-27T06:23:01+00:00",
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
      "location": "vocabulary:63",
      "term": {
        "text": "\"Dementia\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognition Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:23:01+00:00",
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
      "location": "vocabulary:64",
      "term": {
        "text": "\"Cognition Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognitive Dysfunction",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:23:01+00:00",
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
      "location": "vocabulary:65",
      "term": {
        "text": "\"Cognitive Dysfunction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alzheimer Disease",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:23:01+00:00",
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
      "location": "vocabulary:66",
      "term": {
        "text": "\"Alzheimer Disease\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognition",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:23:01+00:00",
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
      "location": "vocabulary:80",
      "term": {
        "text": "\"Cognition\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Cerebral Small Vessel Diseases\"[MeSH Terms] OR \"Leukoaraiosis\"[MeSH Terms] OR \"stroke, lacunar\"[MeSH Terms] OR \"small-vessel disease\"[Title/Abstract] OR \"small vessel diseases\"[Title/Abstract] OR \"small-vessel disease\"[Title/Abstract] OR \"small vessel ischemic disease\"[Title/Abstract] OR \"small vessel ischaemic disease\"[Title/Abstract] OR \"small vessel disease burden\"[Title/Abstract] OR \"cerebral microangiopath*\"[Title/Abstract] OR \"white matter hyperintensit*\"[Title/Abstract] OR \"white matter lesion*\"[Title/Abstract] OR \"white matter change*\"[Title/Abstract] OR \"white matter disease\"[Title/Abstract] OR \"white matter abnormalit*\"[Title/Abstract] OR \"white matter damage\"[Title/Abstract] OR \"white matter hypodensit*\"[Title/Abstract] OR \"white matter signal abnormalit*\"[Title/Abstract] OR \"WMH\"[Title/Abstract] OR \"WMHs\"[Title/Abstract] OR \"Leukoaraiosis\"[Title/Abstract] OR \"leuko-araiosis\"[Title/Abstract] OR \"subcortical hyperintensit*\"[Title/Abstract] OR \"periventricular hyperintensit*\"[Title/Abstract] OR \"deep white matter\"[Title/Abstract] OR \"t2 hyperintensit*\"[Title/Abstract] OR \"binswanger*\"[Title/Abstract] OR \"lacunar infarct*\"[Title/Abstract] OR \"lacunar stroke*\"[Title/Abstract] OR \"lacune*\"[Title/Abstract] OR \"silent brain infarct*\"[Title/Abstract] OR \"silent cerebral infarct*\"[Title/Abstract] OR \"silent infarct*\"[Title/Abstract] OR \"silent stroke*\"[Title/Abstract] OR \"covert brain infarct*\"[Title/Abstract] OR \"covert vascular\"[Title/Abstract] OR \"subclinical brain infarct*\"[Title/Abstract] OR \"subcortical infarct*\"[Title/Abstract] OR \"small subcortical infarct*\"[Title/Abstract] OR \"microinfarct*\"[Title/Abstract] OR \"microbleed*\"[Title/Abstract] OR \"micro bleed*\"[Title/Abstract] OR \"microhemorrhage*\"[Title/Abstract] OR \"microhaemorrhage*\"[Title/Abstract] OR \"micro hemorrhage*\"[Title/Abstract] OR \"cerebral microhemorrhage*\"[Title/Abstract] OR \"brain microbleed*\"[Title/Abstract] OR \"cerebral microbleed*\"[Title/Abstract] OR \"CMBs\"[Title/Abstract] OR \"vascular brain injury\"[Title/Abstract] OR \"vascular brain lesion*\"[Title/Abstract] OR \"cerebrovascular lesion*\"[Title/Abstract] OR \"subclinical cerebrovascular\"[Title/Abstract] OR \"silent cerebrovascular\"[Title/Abstract] OR \"mri marker*\"[Title/Abstract] OR \"MRI-defined\"[Title/Abstract] OR \"subcortical vascular\"[Title/Abstract] OR \"subcortical ischemic vascular\"[Title/Abstract] OR \"white matter hyperdensit*\"[Title/Abstract] OR \"Virchow-Robin\"[Title/Abstract] OR \"perivascular space*\"[Title/Abstract] OR \"enlarged perivascular\"[Title/Abstract]) AND (\"Dementia\"[MeSH Terms] OR \"Cognition Disorders\"[MeSH Terms] OR \"Cognitive Dysfunction\"[MeSH Terms] OR \"Alzheimer Disease\"[MeSH Terms] OR \"Dementia\"[Title/Abstract] OR \"dementias\"[Title/Abstract] OR \"alzheimer*\"[Title/Abstract] OR \"cognitive decline\"[Title/Abstract] OR \"cognitive impairment\"[Title/Abstract] OR \"Cognitive Dysfunction\"[Title/Abstract] OR \"cognitive deterioration\"[Title/Abstract] OR \"cognitive function\"[Title/Abstract] OR \"cognitive performance\"[Title/Abstract] OR \"mild cognitive impairment\"[Title/Abstract] OR \"memory decline\"[Title/Abstract] OR \"neurocognitive\"[Title/Abstract] OR \"cogniti*\"[Title/Abstract] OR \"Cognition\"[MeSH Terms]) AND 1800/01/01:2017/05/06[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "a4e367a955329ebdedd1d8ce1544dc1edf12d22fcb9ce6448170ea46d341c4c1",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "No warnings; bare member names searched."
        },
        "operators": {
          "verdict": "revise",
          "note": "Outcome block AND-ed for workload; evidence thin; rationale counts stale."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Descriptors verified and exploded."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Removed zero-hit terms without recorded reason; perivascular spaces coverage narrow."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Correct."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Only harness as-of pin."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "csvd",
          "finding": "v5 removed leukoaraioses, covert cerebral infarct*, vascular lesions of the brain without stated reason.",
          "recommendation": "Restore or document.",
          "status": "open"
        },
        {
          "id": "F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "csvd",
          "finding": "Perivascular spaces covered only by Virchow-Robin.",
          "recommendation": "Add perivascular space* and enlarged perivascular.",
          "status": "open"
        },
        {
          "id": "F3",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "block": "outcome",
          "finding": "Outcome rationale quotes stale counts (7,788/27,031) vs v5 (7,819/27,394); thin recall evidence.",
          "recommendation": "Update rationale, state threshold assumption.",
          "status": "open"
        },
        {
          "id": "F4",
          "domain": "subject_headings",
          "severity": "document",
          "kind": "lexical",
          "block": "outcome",
          "finding": "Outcome block lacks cogniti* and Cognition MeSH.",
          "recommendation": "Consider or accept risk.",
          "status": "open"
        }
      ],
      "issue_dispositions": [],
      "note": "fresh-context subagent"
    },
    {
      "round": 2,
      "strategy_version": 6,
      "review_sha256": "3a9441a1b1fd24ce4a7cca200e7cb7d102143fdd8a5640fd128a71846c6313ba",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "No warnings; bare member names covered."
        },
        "operators": {
          "verdict": "pass",
          "note": "Outcome block AND-ed for workload; evidence weak and disclosed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Descriptors verified."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Variants covered."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Correct."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Only harness as-of pin."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "csvd",
          "finding": "v5 removed three terms without stated reason.",
          "recommendation": "Restore or document.",
          "status": "resolved",
          "response": "Removed terms returned 0 hits in PubMed; documented in narrative.md."
        },
        {
          "id": "F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "csvd",
          "finding": "Perivascular spaces covered only by Virchow-Robin.",
          "recommendation": "Add terms.",
          "status": "resolved",
          "response": "perivascular space* and enlarged perivascular added in v6."
        },
        {
          "id": "F3",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "block": "outcome",
          "finding": "Stale counts in rationale.",
          "recommendation": "Update.",
          "status": "resolved",
          "response": "Rationale updated to 28,723 and 7,947."
        },
        {
          "id": "F4",
          "domain": "subject_headings",
          "severity": "document",
          "kind": "lexical",
          "block": "outcome",
          "finding": "No cogniti* or Cognition MeSH.",
          "recommendation": "Add.",
          "status": "resolved",
          "response": "Both added in v6."
        },
        {
          "id": "N1",
          "domain": "operators",
          "severity": "document",
          "kind": "scope",
          "block": "outcome",
          "finding": "Outcome block AND-ed for workload; thin recall evidence.",
          "recommendation": "Disclose.",
          "status": "accepted-risk",
          "response": "Disclosed in rationale and narrative.md."
        },
        {
          "id": "N2",
          "domain": "text_words",
          "severity": "document",
          "kind": "reporting",
          "block": "csvd",
          "finding": "Zero-hit counts for removed terms not documented.",
          "recommendation": "Record in notes.",
          "status": "accepted-risk",
          "response": "Recorded in narrative.md."
        }
      ],
      "issue_dispositions": [],
      "note": "fresh-context subagent"
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 6,
      "review_sha256": "3a9441a1b1fd24ce4a7cca200e7cb7d102143fdd8a5640fd128a71846c6313ba",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "pass"
        },
        "operators": {
          "verdict": "pass",
          "note": "pass"
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "pass"
        },
        "text_words": {
          "verdict": "pass",
          "note": "pass"
        },
        "syntax": {
          "verdict": "pass",
          "note": "pass"
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "pass"
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "csvd",
          "finding": "v5 removed three terms without stated reason.",
          "recommendation": "Restore or document.",
          "status": "resolved",
          "response": "0 hits in PubMed; documented in narrative.md."
        },
        {
          "id": "F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "csvd",
          "finding": "Perivascular spaces covered only by Virchow-Robin.",
          "recommendation": "Add terms.",
          "status": "resolved",
          "response": "Added in v6."
        },
        {
          "id": "F3",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "block": "outcome",
          "finding": "Stale counts.",
          "recommendation": "Update.",
          "status": "resolved",
          "response": "Updated to 28,723 and 7,947."
        },
        {
          "id": "F4",
          "domain": "subject_headings",
          "severity": "document",
          "kind": "lexical",
          "block": "outcome",
          "finding": "No cogniti* / Cognition MeSH.",
          "recommendation": "Add.",
          "status": "resolved",
          "response": "Added."
        },
        {
          "id": "N1",
          "domain": "operators",
          "severity": "document",
          "kind": "scope",
          "block": "outcome",
          "finding": "Workload AND; thin recall evidence.",
          "recommendation": "Disclose.",
          "status": "accepted-risk",
          "response": "Disclosed in rationale and narrative.md."
        },
        {
          "id": "N2",
          "domain": "text_words",
          "severity": "document",
          "kind": "reporting",
          "block": "csvd",
          "finding": "Zero-hit counts undocumented.",
          "recommendation": "Record.",
          "status": "accepted-risk",
          "response": "In narrative.md."
        },
        {
          "id": "N3",
          "domain": "subject_headings",
          "severity": "document",
          "kind": "lexical",
          "block": "csvd",
          "finding": "No exposure-side MeSH for microbleeds/silent infarcts.",
          "recommendation": "Record as limitation.",
          "status": "accepted-risk",
          "response": "Recorded in narrative.md; no known record lost."
        }
      ],
      "issue_dispositions": [],
      "note": "fresh-context subagent"
    }
  ]
}
```

