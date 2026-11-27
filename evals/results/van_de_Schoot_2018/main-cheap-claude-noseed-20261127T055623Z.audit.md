# PubMed search strategy: audit

Generated 2026-11-27T06:08:04+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: prognosis / course (condition + course pattern)
- Scope confirmed by user: yes (User unavailable; proceeded on defaults (standard depth, no seeds, no limits). Scope not paused for confirmation. Ambiguity: trajectories treated as course/pattern of PTSD symptoms after any trauma type; adults and children both included. Known misses 16400531 and 21234796 name no PTSD wording (general 'mental health problems'/'psychiatric disorders' after disaster): out of reach, not widened for. Date bound on every query is the harness's Entrez-date pin (as of 2016-01-24), not a strategy limit. Animal studies are excluded at screening, not in the search. Dropped bare posttraumatic[tiab]/post-traumatic[tiab] in v3: a noise-check sample (25 random of 12,479 records they alone retrieved) was all orthopaedic/neurosurgical/animal or post-traumatic growth in cancer; no PTSD.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| PTSD and post-traumatic stress symptoms | search | target condition, reliably named and MeSH-indexed |
| Symptom trajectories / course over time | search | ANDed for WORKLOAD, not on evidence. Without it the PTSD block alone returns 35,830 records, assumed too large to screen (user unavailable); with it 14,450 (59.7% fewer; generic outcome*/pattern* were dropped, course wording added). 28 benchmark records are in PubMed, 26 retrieved (2 missed by the PTSD block, none lost to this block); the 11 pilot-found records are keyword-dependent and not independent. Tested on 26 known records found without a keyword search (reference lists of reviews 23593134 and 23824234): 0 lost; the 95% upper bound on the share lost is 10.9% on those 26, so the loss is only partly measured. The benchmark is concentrated in two reviews (one child-disaster review supplies about half). Block deliberately broad (course/longitudinal/trajectory/persistence/recovery wording plus MeSH). Reversible: drop the block to return to 35,830. |
| Exposure to a traumatic event | optional | implicit in PTSD; population/context, not reliably named separately. Tested as optional: AND-ing loses 2 known records (18725431, 26764215) and saves only about 12% (14,450 to 12,753); left out. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-11-27T06:07:33+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 14,450
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 25,369 | none |
| 2 | `"Stress Disorders, Traumatic"[Mesh]` | 28,166 | none |
| 3 | `PTSD[tiab]` | 15,732 | none |
| 4 | `PTSS[tiab]` | 510 | none |
| 5 | `CPTSD[tiab]` | 45 | none |
| 6 | `"posttraumatic stress"[tiab]` | 14,174 | none |
| 7 | `"post-traumatic stress"[tiab]` | 8,160 | none |
| 8 | `"post traumatic stress"[tiab]` | 8,160 | none |
| 9 | `"traumatic stress"[tiab]` | 9,453 | none |
| 10 | `"acute stress disorder"[tiab]` | 469 | none |
| 11 | `"acute stress reaction*"[tiab]` | 201 | none |
| 12 | `"combat disorder*"[tiab]` | 19 | none |
| 13 | `"combat stress"[tiab]` | 293 | none |
| 14 | `"stress disorder*"[tiab]` | 20,149 | none |
| 15 | `"trauma symptom*"[tiab]` | 595 | none |
| 16 | `"trauma-related symptom*"[tiab]` | 200 | none |
| 17 | `"traumatic neuros*"[tiab]` | 198 | none |
| 18 | `"war neuros*"[tiab]` | 129 | none |
| 19 | `"shell shock"[tiab]` | 110 | none |
| 20 | `"posttraumatic stress"[tiab:~3]` | 14,699 | none |
| 21 | `"post-traumatic stress"[tiab:~3]` | 8,203 | none |
| 22 | `"posttraumatic symptom*"[tiab]` | 403 | none |
| 23 | `"post-traumatic symptom*"[tiab]` | 236 | none |
| 24 | `"posttraumatic reaction*"[tiab]` | 54 | none |
| 25 | `"post-traumatic reaction*"[tiab]` | 52 | none |
| 26 | `"posttraumatic disorder*"[tiab]` | 97 | none |
| 27 | `"post-traumatic disorder*"[tiab]` | 99 | none |
| 28 | `"posttraumatic response*"[tiab]` | 37 | none |
| 29 | `"posttraumatic stress disorder"[tiab:~3]` | 12,954 | none |
| 30 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29` | 35,830 | none |
| 31 | `"Disease Progression"[Mesh]` | 138,667 | none |
| 32 | `"Longitudinal Studies"[Mesh]` | 102,902 | none |
| 33 | `"Cohort Studies"[Mesh]` | 1,583,592 | none |
| 34 | `"Follow-Up Studies"[Mesh]` | 555,750 | none |
| 35 | `"Time Factors"[Mesh]` | 1,073,831 | none |
| 36 | `trajector*[tiab]` | 43,861 | none |
| 37 | `"growth mixture"[tiab]` | 576 | none |
| 38 | `"latent growth"[tiab]` | 1,343 | none |
| 39 | `"latent class"[tiab]` | 2,971 | none |
| 40 | `"growth curve*"[tiab]` | 8,981 | none |
| 41 | `"group-based"[tiab]` | 3,805 | none |
| 42 | `"mixture model*"[tiab]` | 3,628 | none |
| 43 | `longitudinal*[tiab]` | 180,653 | none |
| 44 | `prospective*[tiab]` | 506,544 | none |
| 45 | `"follow-up"[tiab]` | 702,978 | none |
| 46 | `"followed up"[tiab]` | 74,344 | none |
| 47 | `"time course"[tiab]` | 66,728 | none |
| 48 | `"natural course"[tiab]` | 6,566 | none |
| 49 | `"course of"[tiab]` | 276,070 | none |
| 50 | `chronic*[tiab]` | 944,225 | none |
| 51 | `persist*[tiab]` | 367,129 | none |
| 52 | `recover*[tiab]` | 513,902 | none |
| 53 | `resilien*[tiab]` | 15,494 | none |
| 54 | `remission[tiab]` | 92,395 | none |
| 55 | `"delayed onset"[tiab]` | 5,353 | none |
| 56 | `"delayed-onset"[tiab]` | 5,353 | none |
| 57 | `"over time"[tiab]` | 128,863 | none |
| 58 | `"long-term"[tiab]` | 596,468 | none |
| 59 | `"growth model*"[tiab]` | 3,528 | none |
| 60 | `"clinical course"[tiab]` | 51,128 | none |
| 61 | `"symptom course"[tiab]` | 86 | none |
| 62 | `"illness course"[tiab]` | 504 | none |
| 63 | `"latent transition"[tiab]` | 153 | none |
| 64 | `followup[tiab]` | 670,138 | none |
| 65 | `"months after"[tiab]` | 170,675 | none |
| 66 | `"years after"[tiab]` | 97,858 | none |
| 67 | `"Recovery of Function"[Mesh]` | 38,979 | none |
| 68 | `"Resilience, Psychological"[Mesh]` | 2,836 | none |
| 69 | `#31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68` | 5,153,718 | none |
| 70 | `#30 AND #69` | 14,450 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Stress Disorders, Post-Traumatic"[Mesh] OR "Stress Disorders, Traumatic"[Mesh] OR PTSD[tiab] OR PTSS[tiab] OR CPTSD[tiab] OR "posttraumatic stress"[tiab] OR "post-traumatic stress"[tiab] OR "post traumatic stress"[tiab] OR "traumatic stress"[tiab] OR "acute stress disorder"[tiab] OR "acute stress reaction*"[tiab] OR "combat disorder*"[tiab] OR "combat stress"[tiab] OR "stress disorder*"[tiab] OR "trauma symptom*"[tiab] OR "trauma-related symptom*"[tiab] OR "traumatic neuros*"[tiab] OR "war neuros*"[tiab] OR "shell shock"[tiab] OR "posttraumatic stress"[tiab:~3] OR "post-traumatic stress"[tiab:~3] OR "posttraumatic symptom*"[tiab] OR "post-traumatic symptom*"[tiab] OR "posttraumatic reaction*"[tiab] OR "post-traumatic reaction*"[tiab] OR "posttraumatic disorder*"[tiab] OR "post-traumatic disorder*"[tiab] OR "posttraumatic response*"[tiab] OR "posttraumatic stress disorder"[tiab:~3]) AND ("Disease Progression"[Mesh] OR "Longitudinal Studies"[Mesh] OR "Cohort Studies"[Mesh] OR "Follow-Up Studies"[Mesh] OR "Time Factors"[Mesh] OR trajector*[tiab] OR "growth mixture"[tiab] OR "latent growth"[tiab] OR "latent class"[tiab] OR "growth curve*"[tiab] OR "group-based"[tiab] OR "mixture model*"[tiab] OR longitudinal*[tiab] OR prospective*[tiab] OR "follow-up"[tiab] OR "followed up"[tiab] OR "time course"[tiab] OR "natural course"[tiab] OR "course of"[tiab] OR chronic*[tiab] OR persist*[tiab] OR recover*[tiab] OR resilien*[tiab] OR remission[tiab] OR "delayed onset"[tiab] OR "delayed-onset"[tiab] OR "over time"[tiab] OR "long-term"[tiab] OR "growth model*"[tiab] OR "clinical course"[tiab] OR "symptom course"[tiab] OR "illness course"[tiab] OR "latent transition"[tiab] OR followup[tiab] OR "months after"[tiab] OR "years after"[tiab] OR "Recovery of Function"[Mesh] OR "Resilience, Psychological"[Mesh])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall | Found without a keyword search: retrieved / in PubMed |
|---|---|---:|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 28 | 26 | 92.9% | 26 / 28 |
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 11 | 11 | 100.0% | 0 / 0 |

26 of the 28 held-out known records found without a keyword search are retrieved: on their evidence recall is at least 79.2% (95% bound; it is as wide as the number of such records makes it).

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Citation searching for known records

These citation searches found candidate known records to test the strategy against. They are not part of the delivered search, and they did not search for studies for the review itself. Terminology follows the TARCiS statement (Hirt et al., 2024, https://doi.org/10.1136/bmj-2023-078384).

| Batch | Date | Citation index | Direction | Seed records | Candidates | Shown | Screened in |
|---|---|---|---|---:|---:|---:|---:|
| C3 | 2026-11-27 | PubMed | backward | 1 | 29 | 29 | 13 |
| C4 | 2026-11-27 | PubMed | backward | 1 | 29 | 29 | 13 |
| C11 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 15 |
| C12 | 2026-11-27 | PubMed | backward | 1 | 50 | 50 | 15 |

Missed records:

- PMID 16400531 (benchmark): not retrieved by ptsd
- PMID 21234796 (benchmark): not retrieved by ptsd

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| ptsd | 5,153,718 | 2 |
| trajectory | 35,830 | 0 |

### Optional blocks (measured, not searched)

Each row is the effect of AND-ing a concept that is not part of the strategy. Independent records are known records that no keyword search led to (user seeds, a review's reference list); only they can show what a block would lose, and the 95% bound is the largest share of relevant records it could lose on their evidence.

| Block | Records now | Records if AND-ed | Known lost / retrieved now | Independent lost / retrieved now | 95% bound on share lost |
|---|---:|---:|---:|---:|---:|
| Exposure to a traumatic event (trauma) | 14,450 | 12,753 | 2 / 37 | 1 / 26 | 17.0% |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 60,559 | initial | none | first draft: PTSD block only, trajectory/trauma optional |
| 2 | 29,144 | trajectory: +30 / -0 | none | AND trajectory block for workload |
| 3 | 16,666 | ptsd: +10 / -2 | none | replace bare posttraumatic/post-traumatic (6,022 sole records, orthopaedic/neuro noise) with stress/symptom/reaction/disorder phrase and proximity forms |
| 4 | 13,810 | trajectory: +0 / -2 | none | drop generic outcome* and pattern* from trajectory block (term impact: 1,932 and 835 sole records, no known; sample off-topic treatment/cross-sectional) |
| 5 | 14,450 | trajectory: +10 / -0 | none | critic F3: add growth model*, clinical/symptom/illness course, latent transition, followup, months/years after, Recovery of Function and Resilience MeSH |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5: 4 findings; F1 should-fix accepted-risk, F2 document accepted-risk, F3 document accepted-risk, F4 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1401 NCBI requests logged (668 from cache); 1 OpenAlex requests for known-record discovery (0 from cache); strategy sha256 b3c44a90da93._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "code": "known_records_missed",
        "message": "Investigate missed known records and explain any retained misses",
        "severity": "warning",
        "location": "final",
        "evidence": [
          {
            "pmid": "16400531",
            "failing_blocks": [
              "ptsd"
            ],
            "lost_to_limits": false,
            "sets": [
              "benchmark"
            ]
          },
          {
            "pmid": "21234796",
            "failing_blocks": [
              "ptsd"
            ],
            "lost_to_limits": false,
            "sets": [
              "benchmark"
            ]
          }
        ],
        "blocking": false,
        "requires_review": true,
        "id": "I-aca96d0cd318a2bc54b8"
      }
    ],
    "issues": [
      {
        "code": "known_records_missed",
        "message": "Investigate missed known records and explain any retained misses",
        "severity": "warning",
        "location": "final",
        "evidence": [
          {
            "pmid": "16400531",
            "failing_blocks": [
              "ptsd"
            ],
            "lost_to_limits": false,
            "sets": [
              "benchmark"
            ]
          },
          {
            "pmid": "21234796",
            "failing_blocks": [
              "ptsd"
            ],
            "lost_to_limits": false,
            "sets": [
              "benchmark"
            ]
          }
        ],
        "blocking": false,
        "requires_review": true,
        "id": "I-aca96d0cd318a2bc54b8"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:07:33+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D013313",
          "name": "Stress Disorders, Post-Traumatic",
          "type": "descriptor",
          "scope_note": "A class of traumatic stress disorders with symptoms that last more than one month.",
          "tree_numbers": [
            "F03.950.750.500"
          ],
          "entry_terms": 25,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D013313",
      "preferred_label": "Stress Disorders, Post-Traumatic",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"Stress Disorders, Post-Traumatic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress Disorders, Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:07:33+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D040921",
          "name": "Stress Disorders, Traumatic",
          "type": "descriptor",
          "scope_note": "Anxiety disorders manifested by the development of characteristic symptoms following a psychologically traumatic event that is outside the normal range of usual human experience. Symptoms include re-experiencing the traumatic event, increased arousal, and numbing of responsiveness to or reduced involvement with the external world. Traumatic stress disorders can be further classified by the time...",
          "tree_numbers": [
            "F03.950.750"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D040921",
      "preferred_label": "Stress Disorders, Traumatic",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Stress Disorders, Traumatic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Disease Progression",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:07:33+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D018450",
          "name": "Disease Progression",
          "type": "descriptor",
          "scope_note": "The worsening and general progression of a disease over time. This concept is most often used for chronic and incurable diseases where the stage of the disease is an important determinant of therapy and prognosis.",
          "tree_numbers": [
            "C23.550.291.656"
          ],
          "entry_terms": 6,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D018450",
      "preferred_label": "Disease Progression",
      "type": "descriptor",
      "location": "vocabulary:30",
      "term": {
        "text": "\"Disease Progression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Longitudinal Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:07:33+00:00",
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
      "location": "vocabulary:31",
      "term": {
        "text": "\"Longitudinal Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cohort Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:07:33+00:00",
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
      "location": "vocabulary:32",
      "term": {
        "text": "\"Cohort Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Follow-Up Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:07:33+00:00",
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
      "location": "vocabulary:33",
      "term": {
        "text": "\"Follow-Up Studies\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Time Factors",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:07:33+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D013997",
          "name": "Time Factors",
          "type": "descriptor",
          "scope_note": "Elements of limited time intervals, contributing to particular results or situations.",
          "tree_numbers": [
            "G01.910.857"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D013997",
      "preferred_label": "Time Factors",
      "type": "descriptor",
      "location": "vocabulary:34",
      "term": {
        "text": "\"Time Factors\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Recovery of Function",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:07:33+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D020127",
          "name": "Recovery of Function",
          "type": "descriptor",
          "scope_note": "A partial or complete return to the normal or proper physiologic activity of an organ or part following disease or trauma.",
          "tree_numbers": [
            "G16.757"
          ],
          "entry_terms": 2,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D020127",
      "preferred_label": "Recovery of Function",
      "type": "descriptor",
      "location": "vocabulary:66",
      "term": {
        "text": "\"Recovery of Function\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Resilience, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T06:07:33+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D055500",
          "name": "Resilience, Psychological",
          "type": "descriptor",
          "scope_note": "The human ability to adapt in the face of tragedy, trauma, adversity, hardship, and ongoing significant life stressors.",
          "tree_numbers": [
            "F02.940"
          ],
          "entry_terms": 15,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D055500",
      "preferred_label": "Resilience, Psychological",
      "type": "descriptor",
      "location": "vocabulary:67",
      "term": {
        "text": "\"Resilience, Psychological\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"stress disorders, traumatic\"[MeSH Terms] OR \"PTSD\"[Title/Abstract] OR \"PTSS\"[Title/Abstract] OR \"CPTSD\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"traumatic stress\"[Title/Abstract] OR \"acute stress disorder\"[Title/Abstract] OR \"acute stress reaction*\"[Title/Abstract] OR \"combat disorder*\"[Title/Abstract] OR \"combat stress\"[Title/Abstract] OR \"stress disorder*\"[Title/Abstract] OR \"trauma symptom*\"[Title/Abstract] OR \"trauma related symptom*\"[Title/Abstract] OR \"traumatic neuros*\"[Title/Abstract] OR \"war neuros*\"[Title/Abstract] OR \"shell shock\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract:~3] OR \"post-traumatic stress\"[Title/Abstract:~3] OR \"posttraumatic symptom*\"[Title/Abstract] OR \"post traumatic symptom*\"[Title/Abstract] OR \"posttraumatic reaction*\"[Title/Abstract] OR \"post traumatic reaction*\"[Title/Abstract] OR \"posttraumatic disorder*\"[Title/Abstract] OR \"post traumatic disorder*\"[Title/Abstract] OR \"posttraumatic response*\"[Title/Abstract] OR \"posttraumatic stress disorder\"[Title/Abstract:~3]) AND (\"Disease Progression\"[MeSH Terms] OR \"Longitudinal Studies\"[MeSH Terms] OR \"Cohort Studies\"[MeSH Terms] OR \"Follow-Up Studies\"[MeSH Terms] OR \"Time Factors\"[MeSH Terms] OR \"trajector*\"[Title/Abstract] OR \"growth mixture\"[Title/Abstract] OR \"latent growth\"[Title/Abstract] OR \"latent class\"[Title/Abstract] OR \"growth curve*\"[Title/Abstract] OR \"group-based\"[Title/Abstract] OR \"mixture model*\"[Title/Abstract] OR \"longitudinal*\"[Title/Abstract] OR \"prospective*\"[Title/Abstract] OR \"follow-up\"[Title/Abstract] OR \"followed up\"[Title/Abstract] OR \"time course\"[Title/Abstract] OR \"natural course\"[Title/Abstract] OR \"course of\"[Title/Abstract] OR \"chronic*\"[Title/Abstract] OR \"persist*\"[Title/Abstract] OR \"recover*\"[Title/Abstract] OR \"resilien*\"[Title/Abstract] OR \"remission\"[Title/Abstract] OR \"delayed-onset\"[Title/Abstract] OR \"delayed-onset\"[Title/Abstract] OR \"over time\"[Title/Abstract] OR \"long-term\"[Title/Abstract] OR \"growth model*\"[Title/Abstract] OR \"clinical course\"[Title/Abstract] OR \"symptom course\"[Title/Abstract] OR \"illness course\"[Title/Abstract] OR \"latent transition\"[Title/Abstract] OR \"followup\"[Title/Abstract] OR \"months after\"[Title/Abstract] OR \"years after\"[Title/Abstract] OR \"Recovery of Function\"[MeSH Terms] OR \"resilience, psychological\"[MeSH Terms]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "1d7a3bf1248ffa2c0ef754ee5157869681a81e6ee19bdd94887c4f43d72de454",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "Result 14,450 above 10,000 threshold; trajectory block ANDed for workload and broad."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within, AND between; trauma optional block correctly left out."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Both PTSD headings and course MeSH present."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Variants, acronyms, legacy terms covered; dropped bare posttraumatic documented."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No warnings on 70 lines."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No limits; date bound is harness pin."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "structural",
          "block": "trajectory",
          "finding": "Result 14,450 above 10,000; trajectory block ANDed for workload with generic terms; term impact measured on an earlier version.",
          "recommendation": "Re-run term impact; test narrower trajectory wording; state that the whole result is to be screened.",
          "status": "accepted-risk",
          "response": "Term impact was measured on v3 (35,830 PTSD-only; 16,666 with block): outcome* (1,932 sole records) and pattern* (835) were sampled as off-topic and dropped in v4 with no known record lost; the remaining generic terms (chronic*, Cohort Studies, long-term, recover*) each carry no known record alone but are kept on purpose because the course concept is fragile and only 26 independent known records exist (95% loss bound 10.9%), so further narrowing would trade unmeasured recall for workload. v5 adds course wording (+640 records). The user must screen about 14,450 records; this is stated as an open risk, and removing or narrowing the block is the reversible lever."
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "document",
          "kind": "reporting",
          "block": "trajectory",
          "finding": "Evidence for the trajectory block is partly independent and concentrated.",
          "recommendation": "State provenance and the 10.9% bound; do not call the block validated.",
          "status": "accepted-risk",
          "response": "Documented in narrative.md and the trajectory rationale: 26 independent records from reference lists of 23593134 (13) and 23824234 (15 added), bound 10.9%, pilot records not independent. The block is not described as validated."
        },
        {
          "id": "F3",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "block": "ptsd",
          "finding": "Two known records miss the PTSD block.",
          "recommendation": "Retain and list.",
          "status": "accepted-risk",
          "response": "Records name no PTSD wording; out of reach without dropping the PTSD concept. Listed in narrative.md."
        },
        {
          "id": "F4",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "block": "ptsd",
          "finding": "Duplicate lines #7/#8, #55/#56; #29 overlaps #20.",
          "recommendation": "Keep with reason or remove and re-evaluate.",
          "status": "accepted-risk",
          "response": "Retained as explicit hyphen/space and proximity variants; they add no records and no coverage; stated in narrative.md."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-aca96d0cd318a2bc54b8",
          "status": "accepted-risk",
          "response": "Two missed known records (16400531, 21234796) fail only the PTSD block; they name no PTSD or traumatic stress wording, so no PTSD term can retrieve them. Block recall 37 of 39. Retained and listed in the final report.",
          "evidence": "misses: both failing_blocks=[ptsd], lost_to_limits=false; ablation: dropping ptsd gains these two but returns about 5.15 million records; dropping trajectory gains 0 known records (35,830 results)."
        }
      ]
    }
  ]
}
```

