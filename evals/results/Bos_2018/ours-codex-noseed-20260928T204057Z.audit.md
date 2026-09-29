# PubMed search strategy: audit

Generated 2026-09-28T21:00:24+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In population-based cohorts, is cerebral small vessel disease (and its MRI markers) associated with the risk of incident dementia and cognitive decline?
- Framework: PECO
- Scope confirmed by user: yes (User asked to proceed without clarification. Working scope: PECO; mandatory CSVD/MRI-marker exposure block; incident dementia/cognitive outcomes tested as optional; population setting and longitudinal follow-up screened rather than filtered. No known articles supplied. No language, date-publication, age, or study-design filters. Entrez cutoff is supplied by PSB_AS_OF=2017-05-06 for all commands; no [dp] limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Cerebral small vessel disease and MRI markers | search | The exposure is mandatory and searchable; relevant papers may name a specific MRI marker without using the umbrella term. |
| Incident dementia and cognitive decline or impairment | optional | Topic-defining outcome with searchable labels, but outcomes can be inconsistently represented in abstracts; test before deciding whether to AND. |
| Population-based or community-dwelling participants | screen | Setting labels are inconsistent and eligibility can be assessed during screening. |
| Prospective cohort or longitudinal observational follow-up | screen | Design filters can miss eligible studies; assess study design at screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T20:59:39+00:00
- Records added to PubMed up to: 2017-05-06
- Total records: 7,973
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Cerebral Small Vessel Diseases"[Mesh]` | 6,257 | none |
| 2 | `"Leukoaraiosis"[Mesh]` | 470 | none |
| 3 | `"Stroke, Lacunar"[Mesh]` | 412 | none |
| 4 | `"Cerebral Hemorrhage"[Mesh]` | 31,304 | none |
| 5 | `"Cerebral Infarction"[Mesh]` | 29,744 | none |
| 6 | `"cerebral small vessel disease"[tiab]` | 813 | none |
| 7 | `"small vessel disease"[tiab]` | 2,316 | none |
| 8 | `cerebral microangiopath*[tiab]` | 150 | none |
| 9 | `"white matter hyperintens*"[tiab]` | 2,354 | none |
| 10 | `"white matter lesion*"[tiab]` | 4,051 | none |
| 11 | `"white matter change*"[tiab]` | 1,880 | none |
| 12 | `leukoaraiosis[tiab]` | 1,008 | none |
| 13 | `"lacunar infarct*"[tiab]` | 2,251 | none |
| 14 | `"silent brain infarct*"[tiab]` | 280 | none |
| 15 | `"silent cerebral infarct*"[tiab]` | 322 | none |
| 16 | `"covert brain infarct*"[tiab]` | 9 | none |
| 17 | `lacune*[tiab]` | 686 | none |
| 18 | `microbleed*[tiab]` | 1,468 | none |
| 19 | `microhemorrhag*[tiab]` | 578 | none |
| 20 | `microhaemorrhag*[tiab]` | 113 | none |
| 21 | `"vascular brain injury"[tiab]` | 73 | none |
| 22 | `(subcortical[tiab] AND vascular[tiab] AND injur*[tiab])` | 114 | none |
| 23 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22` | 74,853 | none |
| 24 | `"Dementia"[Mesh]` | 145,526 | none |
| 25 | `"Alzheimer Disease"[Mesh]` | 82,140 | none |
| 26 | `"Cognitive Dysfunction"[Mesh]` | 8,211 | none |
| 27 | `"Cognition Disorders"[Mesh]` | 80,254 | none |
| 28 | `dementia*[tiab]` | 87,012 | none |
| 29 | `Alzheimer*[tiab]` | 116,181 | none |
| 30 | `"mild cognitive impairment"[tiab]` | 11,353 | none |
| 31 | `MCI[tiab]` | 13,462 | none |
| 32 | `cognitive impair*[tiab]` | 45,842 | none |
| 33 | `cognitive declin*[tiab]` | 15,221 | none |
| 34 | `cognitive dysfunction*[tiab]` | 10,778 | none |
| 35 | `"cognitive decline"[tiab]` | 15,036 | none |
| 36 | `"cognitive deterioration"[tiab]` | 1,471 | none |
| 37 | `"cognitive function"[tiab]` | 25,869 | none |
| 38 | `cognition[tiab]` | 54,533 | none |
| 39 | `#24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38` | 325,874 | none |
| 40 | `#23 AND #39` | 7,973 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Cerebral Small Vessel Diseases"[Mesh] OR "Leukoaraiosis"[Mesh] OR "Stroke, Lacunar"[Mesh] OR "Cerebral Hemorrhage"[Mesh] OR "Cerebral Infarction"[Mesh] OR "cerebral small vessel disease"[tiab] OR "small vessel disease"[tiab] OR cerebral microangiopath*[tiab] OR "white matter hyperintens*"[tiab] OR "white matter lesion*"[tiab] OR "white matter change*"[tiab] OR leukoaraiosis[tiab] OR "lacunar infarct*"[tiab] OR "silent brain infarct*"[tiab] OR "silent cerebral infarct*"[tiab] OR "covert brain infarct*"[tiab] OR lacune*[tiab] OR microbleed*[tiab] OR microhemorrhag*[tiab] OR microhaemorrhag*[tiab] OR "vascular brain injury"[tiab] OR (subcortical[tiab] AND vascular[tiab] AND injur*[tiab])) AND ("Dementia"[Mesh] OR "Alzheimer Disease"[Mesh] OR "Cognitive Dysfunction"[Mesh] OR "Cognition Disorders"[Mesh] OR dementia*[tiab] OR Alzheimer*[tiab] OR "mild cognitive impairment"[tiab] OR MCI[tiab] OR cognitive impair*[tiab] OR cognitive declin*[tiab] OR cognitive dysfunction*[tiab] OR "cognitive decline"[tiab] OR "cognitive deterioration"[tiab] OR "cognitive function"[tiab] OR cognition[tiab])) AND ("1800/01/01"[edat] : "2017/05/06"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Incident dementia and cognitive decline or impairment | AND-ed | 74,853 / 7,973 | 89.3% | none | 0/30 (up to 10% of removed records could be relevant) | Decision refreshed on the current query after the exposure vocabulary revision. The block reduces the retrieval set by 89.3%, loses none of the three development records, and none of the refreshed 30-record loss sample met eligibility. Outcome wording remains an inherent recall risk, but the measured reduction is substantial. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Cerebral small vessel disease and MRI markers | 1 | `(MRI[tiab] OR magnetic resonance imaging[tiab] OR neuroimaging[tiab])` | 19,409 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| csvid | 325,874 | 0 |
| cognitive_outcomes | 74,853 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 74,784 | initial | none | Initial exposure block includes the umbrella SVD heading and separately named MRI markers; incident dementia/cognitive outcomes added as optional candidate for empirical testing. |
| 2 | 7,973 | csvid: +1 / -1; cognitive_outcomes: +15 / -0 | none | AND the optional dementia/cognitive outcome block after a 30-record loss sample screened 0 relevant and the optional block reduced the marker-only set materially; replaced an unindexed quoted phrase with token co-occurrence because exact order is not required. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 1 findings; P1 must-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 610 NCBI requests logged (207 from cache); strategy sha256 87122fbe8eb4._

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
      "checked_at": "2026-09-28T20:59:39+00:00",
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
      "checked_at": "2026-09-28T20:59:39+00:00",
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
      "checked_at": "2026-09-28T20:59:39+00:00",
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
      "requested": "Cerebral Hemorrhage",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T20:59:39+00:00",
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
      "location": "vocabulary:4",
      "term": {
        "text": "\"Cerebral Hemorrhage\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cerebral Infarction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T20:59:39+00:00",
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
      "requested": "Dementia",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T20:59:39+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "\"Dementia\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Alzheimer Disease",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T20:59:39+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "\"Alzheimer Disease\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognitive Dysfunction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T20:59:39+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "\"Cognitive Dysfunction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognition Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T20:59:39+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "\"Cognition Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Cerebral Small Vessel Diseases\"[MeSH Terms] OR \"Leukoaraiosis\"[MeSH Terms] OR \"stroke, lacunar\"[MeSH Terms] OR \"Cerebral Hemorrhage\"[MeSH Terms] OR \"Cerebral Infarction\"[MeSH Terms] OR \"cerebral small vessel disease\"[Title/Abstract] OR \"small vessel disease\"[Title/Abstract] OR \"cerebral microangiopath*\"[Title/Abstract] OR \"white matter hyperintens*\"[Title/Abstract] OR \"white matter lesion*\"[Title/Abstract] OR \"white matter change*\"[Title/Abstract] OR \"Leukoaraiosis\"[Title/Abstract] OR \"lacunar infarct*\"[Title/Abstract] OR \"silent brain infarct*\"[Title/Abstract] OR \"silent cerebral infarct*\"[Title/Abstract] OR \"covert brain infarct*\"[Title/Abstract] OR \"lacune*\"[Title/Abstract] OR \"microbleed*\"[Title/Abstract] OR \"microhemorrhag*\"[Title/Abstract] OR \"microhaemorrhag*\"[Title/Abstract] OR \"vascular brain injury\"[Title/Abstract] OR (\"subcortical\"[Title/Abstract] AND \"vascular\"[Title/Abstract] AND \"injur*\"[Title/Abstract])) AND (\"Dementia\"[MeSH Terms] OR \"Alzheimer Disease\"[MeSH Terms] OR \"Cognitive Dysfunction\"[MeSH Terms] OR \"Cognition Disorders\"[MeSH Terms] OR \"dementia*\"[Title/Abstract] OR \"alzheimer*\"[Title/Abstract] OR \"mild cognitive impairment\"[Title/Abstract] OR \"MCI\"[Title/Abstract] OR \"cognitive impair*\"[Title/Abstract] OR \"cognitive declin*\"[Title/Abstract] OR \"cognitive dysfunction*\"[Title/Abstract] OR \"cognitive decline\"[Title/Abstract] OR \"cognitive deterioration\"[Title/Abstract] OR \"cognitive function\"[Title/Abstract] OR \"cognition\"[Title/Abstract]) AND 1800/01/01:2017/05/06[Date - Entry]",
  "critic": [
    {
      "domains": {
        "operators": {
          "verdict": "pass",
          "note": "The within-concept terms are ORed and the exposure and outcome blocks are ANDed. The outcome block has a documented optional-concept assessment, including reduction, known-record check, and loss sample."
        },
        "translation": {
          "verdict": "pass",
          "note": "The named exposure markers and cognitive outcomes have corresponding MeSH or title/abstract terms. The packet reports no translation warnings or errors."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The evaluated query includes an Entrez date-entry range ending 2017-05-06. The harness requires this bound to simulate the PubMed corpus as of the task date; it is not an optional publication-date or eligibility filter."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words cover the MRI markers and outcome labels named in the scope. The category probe found no eligible records outside the exposure block in its 30-record sample."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The expressions are fielded and parenthesized, and PubMed returned no syntax errors or translation issues."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The selected MeSH headings are verified in the packet. Broader Cerebral Hemorrhage and Cerebral Infarction headings may add noise, but the exposure block also includes the named MRI-marker terms."
        }
      },
      "review_sha256": "2ffddab35662f678cf61a0a9be591222ff4e14af76ee94fcdc80ee85c837182a",
      "findings": [
        {
          "id": "P1",
          "recommendation": "Remove the [edat] range from the final search, then rerun retrieval, optional-concept assessment, and validation on the unrestricted query. If the 2017-05-06 cutoff is intended, state it as an explicit scope restriction and explain its rationale.",
          "kind": "filter",
          "status": "rejected",
          "severity": "must-fix",
          "finding": "The executed query appends [edat] from 1800-01-01 through 2017-05-06. This omits records entered into PubMed after that date, although the protocol specifies no date limits and the question has no stated historical cutoff.",
          "domain": "limits_filters",
          "response": "Rejected because the harness explicitly requires PubMed to be simulated as of 2017-05-06 by setting PSB_AS_OF=2017-05-06 on every command. The resulting Entrez entry-date bound is essential to that constraint and excludes records added to PubMed after the pinned date; it does not impose a publication-date [dp] filter, which the harness expressly forbids. The protocol notes and final audit state the bound and rationale."
        }
      ],
      "round": 1,
      "strategy_version": 2,
      "issue_dispositions": []
    }
  ]
}
```

