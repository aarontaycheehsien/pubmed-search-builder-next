# PubMed search strategy: audit

Generated 2026-09-28T23:58:27+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Long-term outcomes of cognitive behavioral therapy for anxiety-related disorders
- Framework: PICO
- Scope confirmed by user: yes (Proceeding without clarification as requested. No known relevant articles were supplied. Assumed anxiety-related disorders includes core anxiety disorders and commonly grouped related disorders OCD and PTSD. No minimum long-term duration was specified; screen duration rather than impose a cutoff. No age, language, date, or study-design limit. Scope is operationally confirmed by the agent because user asked not to pause. PubMed requests are bounded to Entrez date 2017-08-24 through PSB_AS_OF; do not add a publication-date limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Anxiety-related disorders | search | Target clinical population; common member disorders may be named without the umbrella term, so include members and probe the category block. |
| Cognitive behavioral therapy | search | Intervention defining the review; require CBT concepts with the anxiety disorder block. |
| Long-term outcomes or follow-up | optional | Defines the topic but follow-up duration and sustained effects may be reported inconsistently; measure whether this block materially reduces screening without losing relevant records. |
| Comparators | screen | Comparator is not central to retrieval and is inconsistently named. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T23:57:41+00:00
- Records added to PubMed up to: 2017-08-24
- Total records: 12,822
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Anxiety Disorders[Mesh]` | 75,155 | none |
| 2 | `Stress Disorders, Post-Traumatic[Mesh]` | 28,555 | none |
| 3 | `anxiety disorder*[tiab]` | 24,830 | none |
| 4 | `anxiety neuros*[tiab]` | 477 | none |
| 5 | `anxiety state*[tiab]` | 1,659 | none |
| 6 | `generalized anxiety[tiab]` | 5,844 | none |
| 7 | `generalised anxiety[tiab]` | 673 | none |
| 8 | `panic disorder*[tiab]` | 8,745 | none |
| 9 | `phobia*[tiab]` | 8,273 | none |
| 10 | `social anxiety[tiab]` | 4,792 | none |
| 11 | `social phobia*[tiab]` | 3,690 | none |
| 12 | `agoraphobia*[tiab]` | 2,868 | none |
| 13 | `separation anxiety[tiab]` | 1,365 | none |
| 14 | `obsessive-compulsive[tiab]` | 15,107 | none |
| 15 | `obsessive compulsive[tiab]` | 15,107 | none |
| 16 | `OCD[tiab]` | 7,878 | none |
| 17 | `posttraumatic stress[tiab]` | 16,639 | none |
| 18 | `post-traumatic stress[tiab]` | 9,637 | none |
| 19 | `PTSD[tiab]` | 18,640 | none |
| 20 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19` | 128,712 | none |
| 21 | `Cognitive Behavioral Therapy[Mesh]` | 24,064 | none |
| 22 | `Behavior Therapy[Mesh]` | 66,990 | none |
| 23 | `cognitive behavio*[tiab]` | 22,079 | none |
| 24 | `cognitive behaviour*[tiab]` | 6,490 | none |
| 25 | `cognitive therap*[tiab]` | 2,812 | none |
| 26 | `cognitive psychotherap*[tiab]` | 117 | none |
| 27 | `cognitive restructuring[tiab]` | 736 | none |
| 28 | `CBT[tiab]` | 8,158 | none |
| 29 | `behavio* therap*[tiab]` | 18,154 | none |
| 30 | `behaviour* therap*[tiab]` | 5,585 | none |
| 31 | `exposure therap*[tiab]` | 1,294 | none |
| 32 | `"exposure and response prevention"[tiab]` | 274 | none |
| 33 | `exposure-response prevention[tiab]` | 36 | none |
| 34 | `applied relaxation[tiab]` | 116 | none |
| 35 | `#21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34` | 81,360 | none |
| 36 | `#20 AND #35` | 12,822 | none |

### Strategy (single line, for copying into PubMed)

```text
((Anxiety Disorders[Mesh] OR Stress Disorders, Post-Traumatic[Mesh] OR anxiety disorder*[tiab] OR anxiety neuros*[tiab] OR anxiety state*[tiab] OR generalized anxiety[tiab] OR generalised anxiety[tiab] OR panic disorder*[tiab] OR phobia*[tiab] OR social anxiety[tiab] OR social phobia*[tiab] OR agoraphobia*[tiab] OR separation anxiety[tiab] OR obsessive-compulsive[tiab] OR obsessive compulsive[tiab] OR OCD[tiab] OR posttraumatic stress[tiab] OR post-traumatic stress[tiab] OR PTSD[tiab]) AND (Cognitive Behavioral Therapy[Mesh] OR Behavior Therapy[Mesh] OR cognitive behavio*[tiab] OR cognitive behaviour*[tiab] OR cognitive therap*[tiab] OR cognitive psychotherap*[tiab] OR cognitive restructuring[tiab] OR CBT[tiab] OR behavio* therap*[tiab] OR behaviour* therap*[tiab] OR exposure therap*[tiab] OR "exposure and response prevention"[tiab] OR exposure-response prevention[tiab] OR applied relaxation[tiab])) AND ("1800/01/01"[edat] : "2017/08/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 16 | 16 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 5 | 5 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Long-term outcomes or follow-up | left out | 12,822 / 5,770 | 55.0% | 28191034 | 1/30 | Leave out: a clearly eligible multi-component CBT trial reported outcomes at 3, 6, and 9 months but was removed because its abstract did not use any tested long-term/follow-up term. The 55% count reduction is not worth the measured recall loss; screen follow-up duration instead. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Anxiety-related disorders | 1 | `Anxiety[Mesh] OR anxiety[tiab] OR fear*[tiab] OR worry[tiab]` | 6,606 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| anxiety | 81,360 | 0 |
| cbt | 128,712 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial broad two-concept PICO search with long-term follow-up treated as a measured optional block; no supplied known records. |
| 2 | 12,822 | cbt: +1 / -1 | none | Quoted the multiword exposure and response prevention term after lint identified the unquoted conjunction as a Boolean operator. |
| 3 | 12,822 | anxiety: +1 / -1 | none | Used the verified preferred MeSH label Stress Disorders, Post-Traumatic for PTSD; the prior noncanonical label was a validation blocker. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3 (same-context critic: no fresh-context reviewer was available under the environment's delegation restriction; I reviewed only critic/packet-1.md against the six PRESS domains.): 0 findings; 
- Round 2 on version 3 (same-context critic: second revision-round check after the validation-set correction; reviewed critic/packet-2.md only. No fresh-context reviewer was available under the environment's delegation restriction.): 0 findings; 
- Round 3 on version 3 (same-context closing critic: verified both prior rounds, current evaluation, and treatment of the workload review issue from critic/packet-3.md. No fresh-context reviewer was available under the environment's delegation restriction.): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 510 NCBI requests logged (256 from cache); strategy sha256 faf451a1ef35._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "code": "over_workload_budget",
        "message": "12,822 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "12,822 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Anxiety Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:57:41+00:00",
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
      "checked_at": "2026-09-28T23:57:41+00:00",
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
      "requested": "Cognitive Behavioral Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:57:41+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D015928",
          "name": "Cognitive Behavioral Therapy",
          "type": "descriptor",
          "scope_note": "A directive form of psychotherapy based on the interpretation of situations (cognitive structure of experiences) that determine how an individual feels and behaves. It is based on the premise that cognition, the process of acquiring knowledge and forming beliefs, is a primary determinant of mood and behavior. The therapy uses behavioral and verbal techniques to identify and correct negative thi...",
          "tree_numbers": [
            "F04.754.137.350"
          ],
          "entry_terms": 29,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D015928",
      "preferred_label": "Cognitive Behavioral Therapy",
      "type": "descriptor",
      "location": "vocabulary:20",
      "term": {
        "text": "Cognitive Behavioral Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Behavior Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:57:41+00:00",
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
      "location": "vocabulary:21",
      "term": {
        "text": "Behavior Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"anxiety disorders\"[MeSH Terms] OR \"stress disorders, post traumatic\"[MeSH Terms] OR \"anxiety disorder*\"[Title/Abstract] OR \"anxiety neuros*\"[Title/Abstract] OR \"anxiety state*\"[Title/Abstract] OR \"generalized anxiety\"[Title/Abstract] OR \"generalised anxiety\"[Title/Abstract] OR \"panic disorder*\"[Title/Abstract] OR \"phobia*\"[Title/Abstract] OR \"social anxiety\"[Title/Abstract] OR \"social phobia*\"[Title/Abstract] OR \"agoraphobia*\"[Title/Abstract] OR \"separation anxiety\"[Title/Abstract] OR \"obsessive-compulsive\"[Title/Abstract] OR \"obsessive-compulsive\"[Title/Abstract] OR \"OCD\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"PTSD\"[Title/Abstract]) AND (\"cognitive behavioral therapy\"[MeSH Terms] OR \"behavior therapy\"[MeSH Terms] OR \"cognitive behavio*\"[Title/Abstract] OR \"cognitive behaviour*\"[Title/Abstract] OR \"cognitive therap*\"[Title/Abstract] OR \"cognitive psychotherap*\"[Title/Abstract] OR \"cognitive restructuring\"[Title/Abstract] OR \"CBT\"[Title/Abstract] OR \"behavio* therap*\"[Title/Abstract] OR \"behaviour* therap*\"[Title/Abstract] OR \"exposure therap*\"[Title/Abstract] OR \"exposure and response prevention\"[Title/Abstract] OR \"exposure response prevention\"[Title/Abstract] OR \"applied relaxation\"[Title/Abstract]) AND 1800/01/01:2017/08/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "22fcac4773c77af14d177c81ebbebe32d3ec2a631bb77b9ff1f7fb9fa8d6c8e9",
      "note": "same-context critic: no fresh-context reviewer was available under the environment's delegation restriction; I reviewed only critic/packet-1.md against the six PRESS domains.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The strategy requires the defining anxiety-related disorder and CBT concepts. Long-term follow-up was tested as optional and left out after a screened loss sample found an eligible study missed by its wording; follow-up duration stays at screening. Comparators stay at screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two broad OR blocks are ANDed. No Boolean exclusion is used in the final query."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The Anxiety Disorders, Stress Disorders, Post-Traumatic, Cognitive Behavioral Therapy, and Behavior Therapy headings were verified as descriptors. The condition concept includes explicit text for named members and a screened category probe."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Title/abstract vocabulary covers spelling variants, anxiety disorder members, CBT wording, and broad behavioral/exposure forms. Acronyms occur within separate ANDed topic blocks."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current evaluation reports no lint errors, translation issues, or unresolved phrase warnings; every term has an explicit field tag."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age, language, publication-date, or study-design restriction is imposed. PubMed is bounded by Entrez date through PSB_AS_OF 2017-08-24."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the screening workload risk. The broad two-block search returns 12,822 records, above the standard 10,000-record budget. The only topic-defining optional block tested reduced the count by 55% but was left out because it removed a clearly eligible study with follow-up through nine months; no safe outcome/follow-up restriction was supported. Comparator is not a searchable required topic and should not be added as an AND block.",
          "evidence": "Current PSB evaluation: 12,822 without the optional block and 5,770 with it; the 30-record loss sample included relevant PMID 28191034 (1/30), which the abstract reports assessed outcomes at 3, 6, and 9 months. The anxiety category probe screened 30 broader-query records with 0 relevant. The optional decision is current and the remaining workload excess is explicitly flagged for the human reviewer."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "22fcac4773c77af14d177c81ebbebe32d3ec2a631bb77b9ff1f7fb9fa8d6c8e9",
      "note": "same-context critic: second revision-round check after the validation-set correction; reviewed critic/packet-2.md only. No fresh-context reviewer was available under the environment's delegation restriction.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The population and intervention blocks reflect the question; the optional follow-up block remains excluded based on its measured recall loss. The screen-only comparator is not required in the Boolean query."
        },
        "operators": {
          "verdict": "pass",
          "note": "The final query uses two OR blocks joined by AND and has no NOT clause or untested proximity operator."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports canonical verified descriptors and no MeSH translation issue. The Anxiety Disorders block was probed for member-only records."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The blocks use tagged text terms with spelling variants and disorder/intervention variants; no held-out records were used for mining."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Lint is clear and every clause has a field tag. The final PubMed translation has no reported warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date or other protocol-extraneous filter is used. The entry-date bound is from PSB_AS_OF. The over-budget issue is separately accepted as a measured workload risk."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the risk that the 12,822-record search exceeds the default 10,000-record workload. The tested 55% reduction would remove a relevant study, so a follow-up block is not a defensible required limiter. Human screening workload should be planned accordingly.",
          "evidence": "The measured optional block retained 5,770 records but excluded the eligible PMID 28191034, and 1 of 30 screened records removed by that block was relevant. No other searchable screen concept was identified; comparators remain a screening criterion."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "22fcac4773c77af14d177c81ebbebe32d3ec2a631bb77b9ff1f7fb9fa8d6c8e9",
      "note": "same-context closing critic: verified both prior rounds, current evaluation, and treatment of the workload review issue from critic/packet-3.md. No fresh-context reviewer was available under the environment's delegation restriction.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two required concepts and the screened comparator match the stated PICO scope. The optional long-term block was left out in response to a relevant loss."
        },
        "operators": {
          "verdict": "pass",
          "note": "The final query retains the evaluated OR and AND structure without NOT."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "All searched MeSH descriptors are verified, and the condition category probe is complete with no relevant sampled record outside the block."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes broad tagged wording for CBT and the named anxiety-related disorders. Development and held-out records are all retrieved, with the held-out set kept out of term mining."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current evaluation has no syntax, lint, field-tag, phrase, or translation issue."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No unnecessary filters are present; the entry-date cutoff is applied from PSB_AS_OF and no publication-date limit was added."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload excess remains an accepted risk for the delivered draft. The tested optional follow-up block has an observed eligible loss, and no safer searchable concept remains untested. The reviewer should plan screening for the measured count.",
          "evidence": "The current query returns 12,822 records. Requiring the optional block would reduce the count to 5,770 but lose eligible PMID 28191034; the loss sample was 1/30 relevant. The current category probe screened 30 records and found none relevant."
        }
      ]
    }
  ]
}
```

