# PubMed search strategy: audit

Generated 2026-09-29T02:40:26+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Long-term outcomes of cognitive behavioral therapy for anxiety-related disorders
- Framework: PICO
- Scope confirmed by user: no (User asked to proceed without questions. Assumptions: 'anxiety-related disorders' includes core anxiety disorders plus OCD and PTSD; long-term is >=6 months after CBT ends; no comparator, age, language, or study-design restrictions. Outcomes may include symptoms, sustained response/remission, relapse/recurrence, functioning, and quality of life. PSB_AS_OF is set to 2017-08-24 for every command; no publication-date limit is applied. No user-supplied known records. Eligibility assumes primary clinical studies rather than secondary reviews.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Anxiety-related disorders | search | The target clinical population is central and searchable; include named anxiety disorder members plus OCD and PTSD under the broad phrase anxiety-related disorders. |
| Cognitive behavioral therapy | search | The intervention is central and usually named; include cognitive, behavioral, and combined CBT terminology. |
| Long-term outcomes and follow-up | optional | The time horizon defines the review but may be missing from titles and abstracts; test rather than require it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T02:39:35+00:00
- Records added to PubMed up to: 2017-08-24
- Total records: 7,653
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Anxiety Disorders[Mesh]` | 75,155 | none |
| 2 | `Stress Disorders, Post-Traumatic[Mesh]` | 28,555 | none |
| 3 | `anxiety[tiab]` | 151,430 | none |
| 4 | `"anxiety disorder"[tiab:~1]` | 13,518 | none |
| 5 | `panic[tiab]` | 13,408 | none |
| 6 | `agoraphobia[tiab]` | 2,865 | none |
| 7 | `phobia*[tiab]` | 8,273 | none |
| 8 | `"social anxiety"[tiab]` | 4,792 | none |
| 9 | `"social phobia"[tiab]` | 3,620 | none |
| 10 | `"generalized anxiety"[tiab]` | 5,844 | none |
| 11 | `"generalised anxiety"[tiab]` | 673 | none |
| 12 | `"separation anxiety"[tiab]` | 1,365 | none |
| 13 | `obsessive-compulsive[tiab]` | 15,107 | none |
| 14 | `obsessive compulsive[tiab]` | 15,107 | none |
| 15 | `OCD[tiab]` | 7,878 | none |
| 16 | `PTSD[tiab]` | 18,640 | none |
| 17 | `post-traumatic stress[tiab]` | 9,637 | none |
| 18 | `posttraumatic stress[tiab]` | 16,639 | none |
| 19 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18` | 231,044 | none |
| 20 | `Behavior Therapy[Mesh]` | 66,990 | none |
| 21 | `"cognitive behavioral therapy"[tiab]` | 6,806 | none |
| 22 | `"cognitive behaviour therapy"[tiab]` | 1,404 | none |
| 23 | `"cognitive behavioral treatment"[tiab]` | 1,140 | none |
| 24 | `"cognitive behavioural treatment"[tiab]` | 336 | none |
| 25 | `"cognitive therapy"[tiab]` | 2,592 | none |
| 26 | `"behavior therapy"[tiab]` | 4,182 | none |
| 27 | `"behaviour therapy"[tiab]` | 2,129 | none |
| 28 | `CBT[tiab]` | 8,158 | none |
| 29 | `"exposure therapy"[tiab]` | 1,242 | none |
| 30 | `"exposure-based"[tiab]` | 1,163 | none |
| 31 | `"systematic desensitization"[tiab]` | 377 | none |
| 32 | `"systematic desensitisation"[tiab]` | 14 | none |
| 33 | `#20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32` | 74,473 | none |
| 34 | `Follow-Up Studies[Mesh]` | 594,219 | none |
| 35 | `Treatment Outcome[Mesh]` | 919,163 | none |
| 36 | `"long-term"[tiab]` | 661,989 | none |
| 37 | `"long term"[tiab]` | 661,989 | none |
| 38 | `follow-up[tiab]` | 788,429 | none |
| 39 | `followup[tiab]` | 751,136 | none |
| 40 | `posttreatment[tiab]` | 42,650 | none |
| 41 | `"post-treatment"[tiab]` | 30,453 | none |
| 42 | `relapse[tiab]` | 100,555 | none |
| 43 | `recurrence[tiab]` | 236,123 | none |
| 44 | `maintenance[tiab]` | 234,429 | none |
| 45 | `durability[tiab]` | 14,752 | none |
| 46 | `"sustained response"[tiab]` | 2,534 | none |
| 47 | `#34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46` | 2,603,375 | none |
| 48 | `#19 AND #33 AND #47` | 7,653 | none |

### Strategy (single line, for copying into PubMed)

```text
((Anxiety Disorders[Mesh] OR Stress Disorders, Post-Traumatic[Mesh] OR anxiety[tiab] OR "anxiety disorder"[tiab:~1] OR panic[tiab] OR agoraphobia[tiab] OR phobia*[tiab] OR "social anxiety"[tiab] OR "social phobia"[tiab] OR "generalized anxiety"[tiab] OR "generalised anxiety"[tiab] OR "separation anxiety"[tiab] OR obsessive-compulsive[tiab] OR obsessive compulsive[tiab] OR OCD[tiab] OR PTSD[tiab] OR post-traumatic stress[tiab] OR posttraumatic stress[tiab]) AND (Behavior Therapy[Mesh] OR "cognitive behavioral therapy"[tiab] OR "cognitive behaviour therapy"[tiab] OR "cognitive behavioral treatment"[tiab] OR "cognitive behavioural treatment"[tiab] OR "cognitive therapy"[tiab] OR "behavior therapy"[tiab] OR "behaviour therapy"[tiab] OR CBT[tiab] OR "exposure therapy"[tiab] OR "exposure-based"[tiab] OR "systematic desensitization"[tiab] OR "systematic desensitisation"[tiab]) AND (Follow-Up Studies[Mesh] OR Treatment Outcome[Mesh] OR "long-term"[tiab] OR "long term"[tiab] OR follow-up[tiab] OR followup[tiab] OR posttreatment[tiab] OR "post-treatment"[tiab] OR relapse[tiab] OR recurrence[tiab] OR maintenance[tiab] OR durability[tiab] OR "sustained response"[tiab])) AND ("1800/01/01"[edat] : "2017/08/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 34 | 34 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Long-term outcomes and follow-up | AND-ed | 16,174 / 7,653 | 52.7% | none | 0/30 (up to 10% of removed records could be relevant) | There are now 34 screened eligible development records in the base; the candidate retrieves all 34. The 30-record sample of removed records contained no eligible study, and the block reduces screening count by 52.7%, meeting the admission criteria. AND it while retaining >=6-month follow-up as a topic-defining concept; keep the six-month criterion for full-text screening. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Anxiety-related disorders | 1 | `Mental Disorders[Mesh] OR anxiety[tiab] OR disorder*[tiab] OR panic[tiab] OR phobia*[tiab] OR obsessive[tiab] OR posttraumatic[tiab] OR PTSD[tiab]` | 25,164 | 0/30 |
| Anxiety-related disorders | 2 | `Mental Disorders[Mesh] OR anxiety[tiab] OR disorder*[tiab] OR panic[tiab] OR phobia*[tiab] OR obsessive[tiab] OR posttraumatic[tiab] OR PTSD[tiab]` | 10,743 | 0/30 |
| Cognitive behavioral therapy | 1 | `Psychotherapy[Mesh] OR psychotherap*[tiab] OR exposure[tiab] OR cognitive[tiab] OR behavior*[tiab] OR behaviour*[tiab] OR desensiti*[tiab]` | 72,380 | 0/30 |
| Cognitive behavioral therapy | 2 | `Psychotherapy[Mesh] OR psychotherap*[tiab] OR exposure[tiab] OR cognitive[tiab] OR behavior*[tiab] OR behaviour*[tiab] OR desensiti*[tiab]` | 12,807 | not screened |
| Cognitive behavioral therapy | 3 | `Psychotherapy[Mesh] OR psychotherap*[tiab] OR exposure[tiab] OR cognitive[tiab] OR behavior*[tiab] OR behaviour*[tiab] OR desensiti*[tiab]` | 12,807 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| anxiety_disorders | 27,535 | 0 |
| cbt | 43,120 | 0 |
| long_term | 16,174 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 16,174 | initial | none | Initial draft from scope assumptions, MeSH and free-text vocabulary; screened reference candidates added as relevant development records |
| 2 | 7,653 | long_term: +13 / -0 | none | With 34 screened relevant records, the optional long-term block meets the specified test: no known losses, 0/30 eligible in the loss sample, and 52.7% reduction. Added it as an AND-ed block. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 1 findings; R1-LF-1 must-fix accepted-risk
- Round 2 on version 2: 1 findings; R1-LF-1 must-fix accepted-risk
- Round 3 on version 2: 1 findings; R1-LF-1 must-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1073 NCBI requests logged (462 from cache); strategy sha256 989f1432dc64._

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
      "requested": "Anxiety Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:39:35+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001008",
          "name": "Anxiety Disorders",
          "type": "descriptor",
          "scope_note": "Persistent and disabling ANXIETY.",
          "tree_numbers": [
            "F03.080"
          ],
          "entry_terms": 11,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001008",
      "preferred_label": "Anxiety Disorders",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "Anxiety Disorders",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:39:35+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "Stress Disorders, Post-Traumatic",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Behavior Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:39:35+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001521",
          "name": "Behavior Therapy",
          "type": "descriptor",
          "scope_note": "The application of modern theories of learning and conditioning in the treatment of behavior disorders.",
          "tree_numbers": [
            "F04.754.137"
          ],
          "entry_terms": 30,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001521",
      "preferred_label": "Behavior Therapy",
      "type": "descriptor",
      "location": "vocabulary:19",
      "term": {
        "text": "Behavior Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Follow-Up Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:39:35+00:00",
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
      "location": "vocabulary:32",
      "term": {
        "text": "Follow-Up Studies",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Treatment Outcome",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:39:35+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D016896",
          "name": "Treatment Outcome",
          "type": "descriptor",
          "scope_note": "Evaluation undertaken to assess the results or consequences of management and procedures used in combating disease in order to determine the efficacy, effectiveness, safety, and practicability of these interventions in individual cases or series.",
          "tree_numbers": [
            "E01.789.800",
            "N04.761.559.590.800",
            "N05.715.360.575.575.800"
          ],
          "entry_terms": 16,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D016896",
      "preferred_label": "Treatment Outcome",
      "type": "descriptor",
      "location": "vocabulary:33",
      "term": {
        "text": "Treatment Outcome",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"anxiety disorders\"[MeSH Terms] OR \"stress disorders, post traumatic\"[MeSH Terms] OR \"anxiety\"[Title/Abstract] OR \"anxiety disorder\"[Title/Abstract:~1] OR \"panic\"[Title/Abstract] OR \"agoraphobia\"[Title/Abstract] OR \"phobia*\"[Title/Abstract] OR \"social anxiety\"[Title/Abstract] OR \"social phobia\"[Title/Abstract] OR \"generalized anxiety\"[Title/Abstract] OR \"generalised anxiety\"[Title/Abstract] OR \"separation anxiety\"[Title/Abstract] OR \"obsessive-compulsive\"[Title/Abstract] OR \"obsessive-compulsive\"[Title/Abstract] OR \"OCD\"[Title/Abstract] OR \"PTSD\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract]) AND (\"behavior therapy\"[MeSH Terms] OR \"cognitive behavioral therapy\"[Title/Abstract] OR \"cognitive behaviour therapy\"[Title/Abstract] OR \"cognitive behavioral treatment\"[Title/Abstract] OR \"cognitive behavioural treatment\"[Title/Abstract] OR \"cognitive therapy\"[Title/Abstract] OR \"behavior therapy\"[Title/Abstract] OR \"behaviour therapy\"[Title/Abstract] OR \"CBT\"[Title/Abstract] OR \"exposure therapy\"[Title/Abstract] OR \"exposure-based\"[Title/Abstract] OR \"systematic desensitization\"[Title/Abstract] OR \"systematic desensitisation\"[Title/Abstract]) AND (\"follow up studies\"[MeSH Terms] OR \"treatment outcome\"[MeSH Terms] OR \"long-term\"[Title/Abstract] OR \"long-term\"[Title/Abstract] OR \"follow-up\"[Title/Abstract] OR \"followup\"[Title/Abstract] OR \"posttreatment\"[Title/Abstract] OR \"post-treatment\"[Title/Abstract] OR \"relapse\"[Title/Abstract] OR \"recurrence\"[Title/Abstract] OR \"maintenance\"[Title/Abstract] OR \"durability\"[Title/Abstract] OR \"sustained response\"[Title/Abstract]) AND 1800/01/01:2017/08/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "a62b8d9a1c1c0380956483e6169ab7a4115cd77a8a05d7c366af7fafaafffeb9",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The named disorder members and CBT terms in the scope are represented in the blocks."
        },
        "operators": {
          "verdict": "pass",
          "note": "The concept blocks are OR-combined and AND-combined as required by the stated search roles."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy uses relevant disorder, behavior therapy, follow-up, and treatment outcome headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words cover the named disorders, CBT forms, and follow-up concepts in the scope."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed syntax errors or warnings."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The evaluated query includes an entry-date cutoff of 2017-08-24, although the scope states no date restriction. If this is the search to run, it excludes later records."
        }
      },
      "findings": [
        {
          "id": "R1-LF-1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The evaluated query appends 1800/01/01:2017/08/24[Date - Entry]. The scope specifies no date limit, so this cutoff would exclude records entered after 2017-08-24.",
          "recommendation": "Remove the entry-date cutoff from the search intended for the review, or clearly identify it as a historical evaluation snapshot and rerun the strategy without it for the current search.",
          "status": "accepted-risk",
          "response": "The cutoff is required by this run's explicit historical-snapshot instruction: PubMed is pinned to records entered by 2017-08-24 via PSB_AS_OF for every command. It is an Entrez entry-date bound, not a publication-date limit; no [dp] restriction is used. The deliverable is therefore explicitly a strategy snapshot evaluated as of 2017-08-24, rather than a current live search. Removing it would violate the user's harness instruction and change the requested time basis. The audit narrative documents this bound."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "a62b8d9a1c1c0380956483e6169ab7a4115cd77a8a05d7c366af7fafaafffeb9",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched disorder members named in scope, including OCD and PTSD, have bare-name terms. The CBT block includes cognitive, behavioral, combined CBT, exposure, and desensitization terminology."
        },
        "operators": {
          "verdict": "pass",
          "note": "The terms are OR-combined within each concept block, and the three blocks are AND-combined in line with the stated search roles and optional-block decision."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes headings for anxiety disorders, post-traumatic stress, behavior therapy, follow-up studies, and treatment outcome."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words represent the named disorder members, CBT forms, and long-term outcome and follow-up concepts. The proximity expression has no wildcard, and the packet reports no phrase or translation warnings."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed errors or warnings, and the block combination is explicitly parenthesized."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "R1-LF-1 is carried forward as accepted-risk: the entry-date cutoff is part of the stated historical snapshot through 2017-08-24, not a publication-date limit. The response and audit narrative document that time basis."
        }
      },
      "findings": [
        {
          "id": "R1-LF-1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The evaluated query includes an entry-date cutoff through 2017-08-24, which excludes later-entered records.",
          "recommendation": "For this explicitly requested historical snapshot, retain the cutoff and identify the strategy as evaluated through 2017-08-24; remove it and rerun if the intended deliverable is a current search.",
          "status": "accepted-risk",
          "response": "Accepted for this run because the packet identifies the cutoff as required by the historical-snapshot instruction and documents it as an Entrez entry-date bound, rather than a publication-date restriction. This disposition applies to the historical snapshot only."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "a62b8d9a1c1c0380956483e6169ab7a4115cd77a8a05d7c366af7fafaafffeb9",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The named disorder members and CBT forms are represented; the packet reports no changes to the strategy."
        },
        "operators": {
          "verdict": "pass",
          "note": "The concept blocks are OR-combined and AND-combined according to their roles and the documented optional-block decision."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes relevant headings for anxiety disorders, PTSD, behavior therapy, follow-up studies, and treatment outcome."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words cover the named disorders, CBT forms, and follow-up concepts; the proximity expression has no wildcard."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed syntax errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "R1-LF-1 remains accepted-risk for the explicitly documented historical snapshot through 2017-08-24. The packet identifies this as an Entrez entry-date bound, not a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-LF-1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The evaluation uses an entry-date cutoff through 2017-08-24, excluding records entered later.",
          "recommendation": "Retain and label the cutoff for the requested historical snapshot; remove it and rerun if the intended search is current.",
          "status": "accepted-risk",
          "response": "Accepted for this run because the packet documents the 2017-08-24 historical snapshot instruction and identifies the bound as Entrez entry date rather than publication date. This disposition applies to that snapshot."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

