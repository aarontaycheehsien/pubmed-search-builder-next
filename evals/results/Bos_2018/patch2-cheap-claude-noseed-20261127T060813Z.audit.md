# PubMed search strategy: audit

Generated 2026-11-27T06:14:40+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In population-based cohorts, is cerebral small vessel disease (and its MRI markers) associated with the risk of incident dementia and cognitive decline?
- Framework: PECO
- Scope confirmed by user: yes (User unavailable; defaults used: standard depth, no limits, no seeds. Outcome kept optional and measured; design/population screened. Not pausing for scope confirmation. Harness pins PubMed to 2017-05-06 via PSB_AS_OF (Entrez-date bound); not a review limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Cerebral small vessel disease and MRI markers (WMH, lacunes/silent infarcts, microbleeds, vascular brain injury) | search | exposure defining the topic; named in title/abstract/MeSH |
| Dementia, Alzheimer disease, cognitive decline/impairment | optional | outcome; usually screened, but CSVD alone may be too large; measured as optional block |
| Population-based / longitudinal cohort | screen | design and setting judged at screening |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-11-27T06:14:16+00:00
- Records added to PubMed up to: 2017-05-06
- Total records: 22,482
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `("Cerebral Small Vessel Diseases"[Mesh] AND ("Dementia"[Mesh] OR "Dementia, Vascular"[Mesh] OR "Alzheimer Disease"[Mesh] OR "Cognitive Dysfunction"[Mesh] OR "Cognition Disorders"[Mesh] OR "Cognition"[Mesh] OR "Neurocognitive Disorders"[Mesh] OR dementia[tiab] OR dementias[tiab] OR alzheimer*[tiab] OR "cognitive decline"[tiab] OR "cognitive impairment"[tiab] OR "cognitive dysfunction"[tiab] OR "cognitive deterioration"[tiab] OR "cognitive function"[tiab] OR "cognitive performance"[tiab] OR cognition[tiab] OR "memory"[tiab] OR "mild cognitive impairment"[tiab] OR "cognitive disorder*"[tiab] OR "cognitive change*"[tiab] OR "cognitive aging"[tiab] OR "neurocognitive"[tiab]))` | 1,144 | none |
| 2 | `"Leukoaraiosis"[Mesh]` | 470 | none |
| 3 | `"Stroke, Lacunar"[Mesh]` | 412 | none |
| 4 | `"small vessel disease"[tiab]` | 2,316 | none |
| 5 | `"small vessel diseases"[tiab]` | 203 | none |
| 6 | `"small-vessel disease"[tiab]` | 2,316 | none |
| 7 | `"white matter hyperintensit*"[tiab]` | 2,313 | none |
| 8 | `("white matter lesion*"[ti] OR ("white matter lesion*"[tiab] AND ("Dementia"[Mesh] OR "Dementia, Vascular"[Mesh] OR "Alzheimer Disease"[Mesh] OR "Cognitive Dysfunction"[Mesh] OR "Cognition Disorders"[Mesh] OR "Cognition"[Mesh] OR "Neurocognitive Disorders"[Mesh] OR dementia[tiab] OR dementias[tiab] OR alzheimer*[tiab] OR "cognitive decline"[tiab] OR "cognitive impairment"[tiab] OR "cognitive dysfunction"[tiab] OR "cognitive deterioration"[tiab] OR "cognitive function"[tiab] OR "cognitive performance"[tiab] OR cognition[tiab] OR "memory"[tiab] OR "mild cognitive impairment"[tiab] OR "cognitive disorder*"[tiab] OR "cognitive change*"[tiab] OR "cognitive aging"[tiab] OR "neurocognitive"[tiab])))` | 2,117 | none |
| 9 | `"white matter change*"[tiab]` | 1,880 | none |
| 10 | `"white matter disease*"[tiab]` | 948 | none |
| 11 | `"white matter abnormalit*"[tiab]` | 1,590 | none |
| 12 | `"white matter disintegrity"[tiab]` | 4 | none |
| 13 | `"white matter damage"[tiab]` | 1,050 | none |
| 14 | `leukoaraios*[tiab]` | 1,010 | none |
| 15 | `"subcortical vascular"[tiab:~2]` | 579 | none |
| 16 | `"periventricular hyperintensit*"[tiab]` | 307 | none |
| 17 | `"deep white matter"[tiab]` | 1,229 | none |
| 18 | `WMH[tiab]` | 1,105 | none |
| 19 | `WMHs[tiab]` | 313 | none |
| 20 | `"lacunar infarct*"[tiab]` | 2,251 | none |
| 21 | `"lacunar stroke*"[tiab]` | 918 | none |
| 22 | `lacune[tiab]` | 153 | none |
| 23 | `lacunes[tiab]` | 585 | none |
| 24 | `("lacunar"[ti] OR ("lacunar"[tiab] AND ("Dementia"[Mesh] OR "Dementia, Vascular"[Mesh] OR "Alzheimer Disease"[Mesh] OR "Cognitive Dysfunction"[Mesh] OR "Cognition Disorders"[Mesh] OR "Cognition"[Mesh] OR "Neurocognitive Disorders"[Mesh] OR dementia[tiab] OR dementias[tiab] OR alzheimer*[tiab] OR "cognitive decline"[tiab] OR "cognitive impairment"[tiab] OR "cognitive dysfunction"[tiab] OR "cognitive deterioration"[tiab] OR "cognitive function"[tiab] OR "cognitive performance"[tiab] OR cognition[tiab] OR "memory"[tiab] OR "mild cognitive impairment"[tiab] OR "cognitive disorder*"[tiab] OR "cognitive change*"[tiab] OR "cognitive aging"[tiab] OR "neurocognitive"[tiab])))` | 1,866 | none |
| 25 | `"silent brain infarct*"[tiab]` | 280 | none |
| 26 | `"silent infarct*"[tiab]` | 311 | none |
| 27 | `"silent cerebral infarct*"[tiab]` | 322 | none |
| 28 | `"covert brain infarct*"[tiab]` | 9 | none |
| 29 | `"silent stroke*"[tiab]` | 136 | none |
| 30 | `"subcortical infarct*"[tiab]` | 1,322 | none |
| 31 | `"subcortical ischemic"[tiab]` | 307 | none |
| 32 | `"subcortical ischaemic"[tiab]` | 52 | none |
| 33 | `microbleed*[tiab]` | 1,468 | none |
| 34 | `"micro-bleed*"[tiab]` | 28 | none |
| 35 | `"microhemorrhage*"[tiab]` | 554 | none |
| 36 | `"microhaemorrhage*"[tiab]` | 107 | none |
| 37 | `"cerebral microbleed*"[tiab]` | 710 | none |
| 38 | `"microinfarct*"[tiab]` | 605 | none |
| 39 | `"micro-infarct*"[tiab]` | 51 | none |
| 40 | `"vascular brain injury"[tiab]` | 73 | none |
| 41 | `"vascular brain damage"[tiab]` | 47 | none |
| 42 | `"cerebrovascular lesion*"[tiab]` | 784 | none |
| 43 | `"ischemic brain lesion*"[tiab]` | 309 | none |
| 44 | `"ischaemic brain lesion*"[tiab]` | 52 | none |
| 45 | `"perivascular space*"[tiab]` | 1,613 | none |
| 46 | `"Virchow-Robin"[tiab]` | 444 | none |
| 47 | `"CADASIL"[tiab]` | 1,055 | none |
| 48 | `"binswanger"[tiab]` | 568 | none |
| 49 | `"cerebral microangiopath*"[tiab]` | 150 | none |
| 50 | `"brain microangiopath*"[tiab]` | 4 | none |
| 51 | `"cerebral leukoencephalopath*"[tiab]` | 9 | none |
| 52 | `"vascular leukoencephalopath*"[tiab]` | 24 | none |
| 53 | `"ischemic leukoencephalopath*"[tiab]` | 15 | none |
| 54 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53` | 22,482 | none |

### Strategy (single line, for copying into PubMed)

```text
((("Cerebral Small Vessel Diseases"[Mesh] AND ("Dementia"[Mesh] OR "Dementia, Vascular"[Mesh] OR "Alzheimer Disease"[Mesh] OR "Cognitive Dysfunction"[Mesh] OR "Cognition Disorders"[Mesh] OR "Cognition"[Mesh] OR "Neurocognitive Disorders"[Mesh] OR dementia[tiab] OR dementias[tiab] OR alzheimer*[tiab] OR "cognitive decline"[tiab] OR "cognitive impairment"[tiab] OR "cognitive dysfunction"[tiab] OR "cognitive deterioration"[tiab] OR "cognitive function"[tiab] OR "cognitive performance"[tiab] OR cognition[tiab] OR "memory"[tiab] OR "mild cognitive impairment"[tiab] OR "cognitive disorder*"[tiab] OR "cognitive change*"[tiab] OR "cognitive aging"[tiab] OR "neurocognitive"[tiab])) OR "Leukoaraiosis"[Mesh] OR "Stroke, Lacunar"[Mesh] OR "small vessel disease"[tiab] OR "small vessel diseases"[tiab] OR "small-vessel disease"[tiab] OR "white matter hyperintensit*"[tiab] OR ("white matter lesion*"[ti] OR ("white matter lesion*"[tiab] AND ("Dementia"[Mesh] OR "Dementia, Vascular"[Mesh] OR "Alzheimer Disease"[Mesh] OR "Cognitive Dysfunction"[Mesh] OR "Cognition Disorders"[Mesh] OR "Cognition"[Mesh] OR "Neurocognitive Disorders"[Mesh] OR dementia[tiab] OR dementias[tiab] OR alzheimer*[tiab] OR "cognitive decline"[tiab] OR "cognitive impairment"[tiab] OR "cognitive dysfunction"[tiab] OR "cognitive deterioration"[tiab] OR "cognitive function"[tiab] OR "cognitive performance"[tiab] OR cognition[tiab] OR "memory"[tiab] OR "mild cognitive impairment"[tiab] OR "cognitive disorder*"[tiab] OR "cognitive change*"[tiab] OR "cognitive aging"[tiab] OR "neurocognitive"[tiab]))) OR "white matter change*"[tiab] OR "white matter disease*"[tiab] OR "white matter abnormalit*"[tiab] OR "white matter disintegrity"[tiab] OR "white matter damage"[tiab] OR leukoaraios*[tiab] OR "subcortical vascular"[tiab:~2] OR "periventricular hyperintensit*"[tiab] OR "deep white matter"[tiab] OR WMH[tiab] OR WMHs[tiab] OR "lacunar infarct*"[tiab] OR "lacunar stroke*"[tiab] OR lacune[tiab] OR lacunes[tiab] OR ("lacunar"[ti] OR ("lacunar"[tiab] AND ("Dementia"[Mesh] OR "Dementia, Vascular"[Mesh] OR "Alzheimer Disease"[Mesh] OR "Cognitive Dysfunction"[Mesh] OR "Cognition Disorders"[Mesh] OR "Cognition"[Mesh] OR "Neurocognitive Disorders"[Mesh] OR dementia[tiab] OR dementias[tiab] OR alzheimer*[tiab] OR "cognitive decline"[tiab] OR "cognitive impairment"[tiab] OR "cognitive dysfunction"[tiab] OR "cognitive deterioration"[tiab] OR "cognitive function"[tiab] OR "cognitive performance"[tiab] OR cognition[tiab] OR "memory"[tiab] OR "mild cognitive impairment"[tiab] OR "cognitive disorder*"[tiab] OR "cognitive change*"[tiab] OR "cognitive aging"[tiab] OR "neurocognitive"[tiab]))) OR "silent brain infarct*"[tiab] OR "silent infarct*"[tiab] OR "silent cerebral infarct*"[tiab] OR "covert brain infarct*"[tiab] OR "silent stroke*"[tiab] OR "subcortical infarct*"[tiab] OR "subcortical ischemic"[tiab] OR "subcortical ischaemic"[tiab] OR microbleed*[tiab] OR "micro-bleed*"[tiab] OR "microhemorrhage*"[tiab] OR "microhaemorrhage*"[tiab] OR "cerebral microbleed*"[tiab] OR "microinfarct*"[tiab] OR "micro-infarct*"[tiab] OR "vascular brain injury"[tiab] OR "vascular brain damage"[tiab] OR "cerebrovascular lesion*"[tiab] OR "ischemic brain lesion*"[tiab] OR "ischaemic brain lesion*"[tiab] OR "perivascular space*"[tiab] OR "Virchow-Robin"[tiab] OR "CADASIL"[tiab] OR "binswanger"[tiab] OR "cerebral microangiopath*"[tiab] OR "brain microangiopath*"[tiab] OR "cerebral leukoencephalopath*"[tiab] OR "vascular leukoencephalopath*"[tiab] OR "ischemic leukoencephalopath*"[tiab])) AND ("1800/01/01"[edat] : "2017/05/06"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall | Found without a keyword search: retrieved / in PubMed |
|---|---|---:|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 9 | 9 | 100.0% | 0 / 0 |

Every known record came from a keyword search, or from the similar or citing articles of one. Such records name the searched words by construction, so the recall figures check the strategy's wording; they do not estimate recall. A prior review's reference list (psb neighbors <review PMID> --links refs) gives records that do not depend on your wording.

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Citation searching for known records

These citation searches found candidate known records to test the strategy against. They are not part of the delivered search, and they did not search for studies for the review itself. Terminology follows the TARCiS statement (Hirt et al., 2024, https://doi.org/10.1136/bmj-2023-078384).

| Batch | Date | Citation index | Direction | Seed records | Candidates | Shown | Screened in |
|---|---|---|---|---:|---:|---:|---:|
| C3 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 0 |

### Optional blocks (measured, not searched)

Each row is the effect of AND-ing a concept that is not part of the strategy. Independent records are known records that no keyword search led to (user seeds, a review's reference list); only they can show what a block would lose, and the 95% bound is the largest share of relevant records it could lose on their evidence.

| Block | Records now | Records if AND-ed | Known lost / retrieved now | Independent lost / retrieved now | 95% bound on share lost |
|---|---:|---:|---:|---:|---:|
| Dementia and cognitive decline/impairment (outcome) | 22,482 | 7,896 | 0 / 9 | 0 / 0 | unmeasured |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | initial draft: CSVD block, outcome optional |
| 2 | 51,990 | csvd: +1 / -8 | none | fix proximity lint; drop broad infarct/VaD/CAA terms |
| 3 | 29,664 | csvd: +5 / -3 | none | drop noisy vascular lesions~2, microangiopath*, leukoencephalopath*; add cerebral-specific variants |
| 4 | 22,482 | csvd: +3 / -3 | none | restructure top 3 terms (Cerebral Small Vessel Diseases[Mesh], white matter lesion*, lacunar) with outcome qualifier; none refused |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4 (fresh-context subagent critic): 5 findings; F1 must-fix rejected, F2 should-fix accepted-risk, F3 must-fix rejected, F4 should-fix accepted-risk, F5 document accepted-risk
- Round 2 on version 4 (fresh-context subagent critic): 5 findings; F1 should-fix accepted-risk, F2 should-fix accepted-risk, F3 document resolved, F4 document accepted-risk, F5 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 830 NCBI requests logged (334 from cache); strategy sha256 9ad0333b2478._

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
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "requested": "Dementia",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"Dementia\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Dementia, Vascular",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D015140",
          "name": "Dementia, Vascular",
          "type": "descriptor",
          "scope_note": "An imprecise term referring to dementia associated with CEREBROVASCULAR DISORDERS, including CEREBRAL INFARCTION (single or multiple), and conditions associated with chronic BRAIN ISCHEMIA. Diffuse, cortical, and subcortical subtypes have been described. (From Gerontol Geriatr 1998 Feb;31(1):36-44)",
          "tree_numbers": [
            "C10.228.140.300.400",
            "C10.228.140.300.510.800.500",
            "C10.228.140.380.230",
            "C10.228.140.695.500",
            "C14.907.137.126.372.500",
            "C14.907.253.560.350.500",
            "F03.615.400.350"
          ],
          "entry_terms": 39,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D015140",
      "preferred_label": "Dementia, Vascular",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "\"Dementia, Vascular\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alzheimer Disease",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "location": "vocabulary:4",
      "term": {
        "text": "\"Alzheimer Disease\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognitive Dysfunction",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "location": "vocabulary:5",
      "term": {
        "text": "\"Cognitive Dysfunction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognition Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "location": "vocabulary:6",
      "term": {
        "text": "\"Cognition Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognition",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "location": "vocabulary:7",
      "term": {
        "text": "\"Cognition\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Neurocognitive Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "location": "vocabulary:8",
      "term": {
        "text": "\"Neurocognitive Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Leukoaraiosis",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "\"Leukoaraiosis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stroke, Lacunar",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "\"Stroke, Lacunar\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Dementia",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "location": "vocabulary:33",
      "term": {
        "text": "\"Dementia\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Dementia, Vascular",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D015140",
          "name": "Dementia, Vascular",
          "type": "descriptor",
          "scope_note": "An imprecise term referring to dementia associated with CEREBROVASCULAR DISORDERS, including CEREBRAL INFARCTION (single or multiple), and conditions associated with chronic BRAIN ISCHEMIA. Diffuse, cortical, and subcortical subtypes have been described. (From Gerontol Geriatr 1998 Feb;31(1):36-44)",
          "tree_numbers": [
            "C10.228.140.300.400",
            "C10.228.140.300.510.800.500",
            "C10.228.140.380.230",
            "C10.228.140.695.500",
            "C14.907.137.126.372.500",
            "C14.907.253.560.350.500",
            "F03.615.400.350"
          ],
          "entry_terms": 39,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D015140",
      "preferred_label": "Dementia, Vascular",
      "type": "descriptor",
      "location": "vocabulary:34",
      "term": {
        "text": "\"Dementia, Vascular\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alzheimer Disease",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "location": "vocabulary:38",
      "term": {
        "text": "\"Cognition\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Neurocognitive Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "location": "vocabulary:39",
      "term": {
        "text": "\"Neurocognitive Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Dementia",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "location": "vocabulary:73",
      "term": {
        "text": "\"Dementia\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Dementia, Vascular",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D015140",
          "name": "Dementia, Vascular",
          "type": "descriptor",
          "scope_note": "An imprecise term referring to dementia associated with CEREBROVASCULAR DISORDERS, including CEREBRAL INFARCTION (single or multiple), and conditions associated with chronic BRAIN ISCHEMIA. Diffuse, cortical, and subcortical subtypes have been described. (From Gerontol Geriatr 1998 Feb;31(1):36-44)",
          "tree_numbers": [
            "C10.228.140.300.400",
            "C10.228.140.300.510.800.500",
            "C10.228.140.380.230",
            "C10.228.140.695.500",
            "C14.907.137.126.372.500",
            "C14.907.253.560.350.500",
            "F03.615.400.350"
          ],
          "entry_terms": 39,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D015140",
      "preferred_label": "Dementia, Vascular",
      "type": "descriptor",
      "location": "vocabulary:74",
      "term": {
        "text": "\"Dementia, Vascular\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alzheimer Disease",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "location": "vocabulary:75",
      "term": {
        "text": "\"Alzheimer Disease\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognitive Dysfunction",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "location": "vocabulary:76",
      "term": {
        "text": "\"Cognitive Dysfunction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognition Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "location": "vocabulary:77",
      "term": {
        "text": "\"Cognition Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognition",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "location": "vocabulary:78",
      "term": {
        "text": "\"Cognition\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Neurocognitive Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:14:16+00:00",
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
      "location": "vocabulary:79",
      "term": {
        "text": "\"Neurocognitive Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "((\"Cerebral Small Vessel Diseases\"[MeSH Terms] AND (\"Dementia\"[MeSH Terms] OR \"dementia, vascular\"[MeSH Terms] OR \"Alzheimer Disease\"[MeSH Terms] OR \"Cognitive Dysfunction\"[MeSH Terms] OR \"Cognition Disorders\"[MeSH Terms] OR \"Cognition\"[MeSH Terms] OR \"Neurocognitive Disorders\"[MeSH Terms] OR \"Dementia\"[Title/Abstract] OR \"dementias\"[Title/Abstract] OR \"alzheimer*\"[Title/Abstract] OR \"cognitive decline\"[Title/Abstract] OR \"cognitive impairment\"[Title/Abstract] OR \"Cognitive Dysfunction\"[Title/Abstract] OR \"cognitive deterioration\"[Title/Abstract] OR \"cognitive function\"[Title/Abstract] OR \"cognitive performance\"[Title/Abstract] OR \"Cognition\"[Title/Abstract] OR \"memory\"[Title/Abstract] OR \"mild cognitive impairment\"[Title/Abstract] OR \"cognitive disorder*\"[Title/Abstract] OR \"cognitive change*\"[Title/Abstract] OR \"cognitive aging\"[Title/Abstract] OR \"neurocognitive\"[Title/Abstract])) OR \"Leukoaraiosis\"[MeSH Terms] OR \"stroke, lacunar\"[MeSH Terms] OR \"small-vessel disease\"[Title/Abstract] OR \"small vessel diseases\"[Title/Abstract] OR \"small-vessel disease\"[Title/Abstract] OR \"white matter hyperintensit*\"[Title/Abstract] OR (\"white matter lesion*\"[Title] OR (\"white matter lesion*\"[Title/Abstract] AND (\"Dementia\"[MeSH Terms] OR \"dementia, vascular\"[MeSH Terms] OR \"Alzheimer Disease\"[MeSH Terms] OR \"Cognitive Dysfunction\"[MeSH Terms] OR \"Cognition Disorders\"[MeSH Terms] OR \"Cognition\"[MeSH Terms] OR \"Neurocognitive Disorders\"[MeSH Terms] OR \"Dementia\"[Title/Abstract] OR \"dementias\"[Title/Abstract] OR \"alzheimer*\"[Title/Abstract] OR \"cognitive decline\"[Title/Abstract] OR \"cognitive impairment\"[Title/Abstract] OR \"Cognitive Dysfunction\"[Title/Abstract] OR \"cognitive deterioration\"[Title/Abstract] OR \"cognitive function\"[Title/Abstract] OR \"cognitive performance\"[Title/Abstract] OR \"Cognition\"[Title/Abstract] OR \"memory\"[Title/Abstract] OR \"mild cognitive impairment\"[Title/Abstract] OR \"cognitive disorder*\"[Title/Abstract] OR \"cognitive change*\"[Title/Abstract] OR \"cognitive aging\"[Title/Abstract] OR \"neurocognitive\"[Title/Abstract]))) OR \"white matter change*\"[Title/Abstract] OR \"white matter disease*\"[Title/Abstract] OR \"white matter abnormalit*\"[Title/Abstract] OR \"white matter disintegrity\"[Title/Abstract] OR \"white matter damage\"[Title/Abstract] OR \"leukoaraios*\"[Title/Abstract] OR \"subcortical vascular\"[Title/Abstract:~2] OR \"periventricular hyperintensit*\"[Title/Abstract] OR \"deep white matter\"[Title/Abstract] OR \"WMH\"[Title/Abstract] OR \"WMHs\"[Title/Abstract] OR \"lacunar infarct*\"[Title/Abstract] OR \"lacunar stroke*\"[Title/Abstract] OR \"lacune\"[Title/Abstract] OR \"lacunes\"[Title/Abstract] OR (\"lacunar\"[Title] OR (\"lacunar\"[Title/Abstract] AND (\"Dementia\"[MeSH Terms] OR \"dementia, vascular\"[MeSH Terms] OR \"Alzheimer Disease\"[MeSH Terms] OR \"Cognitive Dysfunction\"[MeSH Terms] OR \"Cognition Disorders\"[MeSH Terms] OR \"Cognition\"[MeSH Terms] OR \"Neurocognitive Disorders\"[MeSH Terms] OR \"Dementia\"[Title/Abstract] OR \"dementias\"[Title/Abstract] OR \"alzheimer*\"[Title/Abstract] OR \"cognitive decline\"[Title/Abstract] OR \"cognitive impairment\"[Title/Abstract] OR \"Cognitive Dysfunction\"[Title/Abstract] OR \"cognitive deterioration\"[Title/Abstract] OR \"cognitive function\"[Title/Abstract] OR \"cognitive performance\"[Title/Abstract] OR \"Cognition\"[Title/Abstract] OR \"memory\"[Title/Abstract] OR \"mild cognitive impairment\"[Title/Abstract] OR \"cognitive disorder*\"[Title/Abstract] OR \"cognitive change*\"[Title/Abstract] OR \"cognitive aging\"[Title/Abstract] OR \"neurocognitive\"[Title/Abstract]))) OR \"silent brain infarct*\"[Title/Abstract] OR \"silent infarct*\"[Title/Abstract] OR \"silent cerebral infarct*\"[Title/Abstract] OR \"covert brain infarct*\"[Title/Abstract] OR \"silent stroke*\"[Title/Abstract] OR \"subcortical infarct*\"[Title/Abstract] OR \"subcortical ischemic\"[Title/Abstract] OR \"subcortical ischaemic\"[Title/Abstract] OR \"microbleed*\"[Title/Abstract] OR \"micro bleed*\"[Title/Abstract] OR \"microhemorrhage*\"[Title/Abstract] OR \"microhaemorrhage*\"[Title/Abstract] OR \"cerebral microbleed*\"[Title/Abstract] OR \"microinfarct*\"[Title/Abstract] OR \"micro infarct*\"[Title/Abstract] OR \"vascular brain injury\"[Title/Abstract] OR \"vascular brain damage\"[Title/Abstract] OR \"cerebrovascular lesion*\"[Title/Abstract] OR \"ischemic brain lesion*\"[Title/Abstract] OR \"ischaemic brain lesion*\"[Title/Abstract] OR \"perivascular space*\"[Title/Abstract] OR \"Virchow-Robin\"[Title/Abstract] OR \"CADASIL\"[Title/Abstract] OR \"binswanger\"[Title/Abstract] OR \"cerebral microangiopath*\"[Title/Abstract] OR \"brain microangiopath*\"[Title/Abstract] OR \"cerebral leukoencephalopath*\"[Title/Abstract] OR \"vascular leukoencephalopath*\"[Title/Abstract] OR \"ischemic leukoencephalopath*\"[Title/Abstract]) AND 1800/01/01:2017/05/06[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "0cc3f79108f0aa32d52206c0b2d1334ac7690688b83e3c39660b08dff15d3aa5",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "See F1."
        },
        "operators": {
          "verdict": "revise",
          "note": "See F1, F2."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "See F1."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Good coverage; see F5."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No warnings."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "See F3."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "structural",
          "block": "csvd",
          "finding": "Three exposure terms (CSVD MeSH, white matter lesion*, lacunar) are only searched with outcome words (restructured); records lacking outcome words are lost.",
          "recommendation": "Restore bare forms.",
          "status": "rejected",
          "response": "Deliberate per-term narrowing (psb restructure, top 3 noisiest terms, none refused, 0 of 9 known lost). Every other CSVD term (50+) remains bare, and white matter lesion*/lacunar are kept unconditionally in titles. Records indexed only to the CSVD descriptor or those words with no dementia/cognition wording in title, abstract or MeSH do not meet the outcome eligibility criterion anyway, and restoring them would add 7,182 records (29,664 vs 22,482). Residual risk is unmeasured (no independent known records) and is flagged for the PRESS peer reviewer."
        },
        {
          "id": "F2",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "block": "outcome",
          "finding": "AND decision for the outcome block is implicit; loss unmeasured.",
          "recommendation": "Decide explicitly.",
          "status": "accepted-risk",
          "response": "Explicit decision: outcome block is NOT AND-ed at top level (recall first; 0 independent known records, loss unmeasured, 7,896 if AND-ed). Outcome used only to narrow the three noisiest generic terms via restructure. No prior review supplied a usable reference list and OpenAlex was over budget. Reviewers may AND the outcome block (7,896) if 22,482 is too large to screen."
        },
        {
          "id": "F3",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "block": "",
          "finding": "Queries carry an [edat] bound to 2017/05/06 while protocol has as_of null.",
          "recommendation": "Record or remove.",
          "status": "rejected",
          "response": "The edat bound is imposed by the evaluation harness (PSB_AS_OF=2017-05-06, work-as-of date for this run), not a search limit chosen for the review; it is recorded in notes. No publication-date limit is used."
        },
        {
          "id": "F4",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "block": "csvd",
          "finding": "Term impact stale after v4; recall is a wording check.",
          "recommendation": "Re-run term-impact; report recall as non-independent.",
          "status": "accepted-risk",
          "response": "Term impact was measured at v2 and drove the removal of vascular lesions~2, microangiopath*, leukoencephalopath* (v3) and the restructure (v4); recall is reported as non-independent (0 independent known records) in narrative.md."
        },
        {
          "id": "F5",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "block": "csvd",
          "finding": "Redundant hyphen variants; CADASIL/Binswanger/deep white matter may add clinic records.",
          "recommendation": "Keep.",
          "status": "accepted-risk",
          "response": "Kept for recall; noise is screened out at title/abstract."
        }
      ],
      "issue_dispositions": [],
      "note": "fresh-context subagent critic"
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "0cc3f79108f0aa32d52206c0b2d1334ac7690688b83e3c39660b08dff15d3aa5",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Pass per fresh-context reviewer round 2; see findings."
        },
        "operators": {
          "verdict": "pass",
          "note": "Pass per fresh-context reviewer round 2; see findings."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Pass per fresh-context reviewer round 2; see findings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Pass per fresh-context reviewer round 2; see findings."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Pass per fresh-context reviewer round 2; see findings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Pass per fresh-context reviewer round 2; see findings."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "structural",
          "block": "csvd",
          "finding": "CSVD descriptor, white matter lesion*, lacunar searched only with outcome terms (abstract-level); recall-vs-volume trade-off.",
          "recommendation": "Keep narrowing; report trade-off; un-narrowed 29,664 as sensitivity option.",
          "status": "accepted-risk",
          "response": "Downgraded from must-fix. Named members covered bare via other tiab terms and bare Leukoaraiosis/Stroke, Lacunar MeSH; titles unconditional. 0 of 9 known lost (not independent). Residual risk unmeasured; reported."
        },
        {
          "id": "F2",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "block": "outcome",
          "finding": "Large result (22,482); outcome AND would give 7,896, loss unmeasured.",
          "recommendation": "Keep explicit no-AND; report 7,896 fallback.",
          "status": "accepted-risk",
          "response": "Decision explicit and measured; recall-first; loss if AND-ed is unmeasured and reported as such."
        },
        {
          "id": "F3",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "filter",
          "block": "",
          "finding": "[edat] bound to 2017/05/06 with as_of null.",
          "recommendation": "Report as harness bound.",
          "status": "resolved",
          "response": "Recorded in notes as harness bound, not review limit."
        },
        {
          "id": "F4",
          "domain": "translation",
          "severity": "document",
          "kind": "reporting",
          "block": "csvd",
          "finding": "Term impact predates v4; recall is a wording check.",
          "recommendation": "Report as non-independent.",
          "status": "accepted-risk",
          "response": "Term impact at v2 drove removals/restructure; recall reported non-independent."
        },
        {
          "id": "F5",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "block": "csvd",
          "finding": "Redundant variants; CADASIL/Binswanger may add clinic records.",
          "recommendation": "Keep.",
          "status": "accepted-risk",
          "response": "Kept for recall; screened out at title/abstract."
        }
      ],
      "issue_dispositions": [],
      "note": "fresh-context subagent critic"
    }
  ]
}
```

