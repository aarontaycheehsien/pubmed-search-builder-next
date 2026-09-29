# PubMed search strategy: audit

Generated 2026-09-29T03:14:39+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Long-term outcomes of cognitive behavioral therapy for anxiety-related disorders
- Framework: PICO (intervention effectiveness)
- Scope confirmed by user: yes (User asked to proceed without questions. Assumption: 'anxiety-related disorders' includes anxiety disorders and disorders commonly grouped with them in older clinical classifications, including OCD and PTSD; other stressor-related conditions are screened for scope. 'Long-term' has no supplied minimum duration and will be operationalized at screening as an outcome after treatment or a later follow-up. No known relevant records supplied. PubMed retrieval is bounded by Entrez date 2017-08-24 via PSB_AS_OF on every command; no publication-date limit. Standard depth defaults used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Anxiety and anxiety-related disorders | search | The target condition is required. Broadly include anxiety disorders and closely related disorders that have been grouped with anxiety across changing taxonomies; test member-only disorder terminology. |
| Cognitive behavioral and behavior therapies | search | The intervention is required, but studies may name a CBT component or modality (such as cognitive therapy, exposure, or behavior therapy) instead of the umbrella label; test member-only terminology. |
| Long-term follow-up or durability of outcomes | optional | This defines the review topic but may be reported inconsistently. Test as an extra AND block before deciding whether to require it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T03:13:36+00:00
- Records added to PubMed up to: 2017-08-24
- Total records: 24,486
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Anxiety Disorders[Mesh]` | 75,155 | none |
| 2 | `Anxiety[Mesh]` | 74,592 | none |
| 3 | `Phobic Disorders[Mesh]` | 12,282 | none |
| 4 | `Panic Disorder[Mesh]` | 6,597 | none |
| 5 | `Obsessive-Compulsive Disorder[Mesh]` | 14,139 | none |
| 6 | `Stress Disorders, Post-Traumatic[Mesh]` | 28,555 | none |
| 7 | `anxiet*[tiab]` | 153,037 | none |
| 8 | `anxiety[tiab] AND disorder*[tiab]` | 55,789 | none |
| 9 | `anxious[tiab]` | 14,019 | none |
| 10 | `generalized[tiab] AND anxiety[tiab]` | 7,287 | none |
| 11 | `generalised[tiab] AND anxiety[tiab]` | 822 | none |
| 12 | `GAD[tiab]` | 7,728 | none |
| 13 | `panic[tiab]` | 13,408 | none |
| 14 | `agoraphobi*[tiab]` | 3,183 | none |
| 15 | `phobi*[tiab]` | 10,712 | none |
| 16 | `social[tiab] AND anxi*[tiab]` | 26,058 | none |
| 17 | `"social phobia"[tiab:~1]` | 3,643 | none |
| 18 | `"separation anxiety"[tiab:~1]` | 1,430 | none |
| 19 | `obsessive-compulsive[tiab]` | 15,107 | none |
| 20 | `"obsessive compulsive"[tiab:~1]` | 15,168 | none |
| 21 | `OCD[tiab]` | 7,878 | none |
| 22 | `PTSD[tiab]` | 18,640 | none |
| 23 | `"posttraumatic stress"[tiab:~1]` | 17,530 | none |
| 24 | `"post-traumatic stress"[tiab:~1]` | 9,655 | none |
| 25 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24` | 262,969 | none |
| 26 | `Behavior Therapy[Mesh]` | 66,990 | none |
| 27 | `Cognitive Behavioral Therapy[Mesh]` | 24,064 | none |
| 28 | `Desensitization, Psychologic[Mesh]` | 3,088 | none |
| 29 | `Implosive Therapy[Mesh]` | 1,036 | none |
| 30 | `"cognitive behavioral therapy"[tiab:~2]` | 7,264 | none |
| 31 | `"cognitive behaviour therapy"[tiab:~2]` | 1,439 | none |
| 32 | `"cognitive behavioral treatment"[tiab:~2]` | 1,890 | none |
| 33 | `"cognitive behaviour treatment"[tiab:~2]` | 69 | none |
| 34 | `"cognitive therapy"[tiab:~1]` | 15,763 | none |
| 35 | `"behavior therapy"[tiab:~1]` | 4,464 | none |
| 36 | `"behaviour therapy"[tiab:~1]` | 2,213 | none |
| 37 | `CBT[tiab]` | 8,158 | none |
| 38 | `cognitiv*[tiab] AND therap*[tiab]` | 46,483 | none |
| 39 | `exposure[tiab] AND therap*[tiab]` | 61,364 | none |
| 40 | `exposure-based[tiab]` | 1,163 | none |
| 41 | `"exposure and response prevention"[tiab:~1]` | 308 | none |
| 42 | `"response prevention"[tiab:~1]` | 886 | none |
| 43 | `systematic desensiti*[tiab]` | 391 | none |
| 44 | `behavior*[tiab] AND therap*[tiab]` | 69,586 | none |
| 45 | `behaviour*[tiab] AND therap*[tiab]` | 22,244 | none |
| 46 | `#26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45` | 221,591 | none |
| 47 | `#25 AND #46` | 24,486 | none |

### Strategy (single line, for copying into PubMed)

```text
((Anxiety Disorders[Mesh] OR Anxiety[Mesh] OR Phobic Disorders[Mesh] OR Panic Disorder[Mesh] OR Obsessive-Compulsive Disorder[Mesh] OR Stress Disorders, Post-Traumatic[Mesh] OR anxiet*[tiab] OR (anxiety[tiab] AND disorder*[tiab]) OR anxious[tiab] OR (generalized[tiab] AND anxiety[tiab]) OR (generalised[tiab] AND anxiety[tiab]) OR GAD[tiab] OR panic[tiab] OR agoraphobi*[tiab] OR phobi*[tiab] OR (social[tiab] AND anxi*[tiab]) OR "social phobia"[tiab:~1] OR "separation anxiety"[tiab:~1] OR obsessive-compulsive[tiab] OR "obsessive compulsive"[tiab:~1] OR OCD[tiab] OR PTSD[tiab] OR "posttraumatic stress"[tiab:~1] OR "post-traumatic stress"[tiab:~1]) AND (Behavior Therapy[Mesh] OR Cognitive Behavioral Therapy[Mesh] OR Desensitization, Psychologic[Mesh] OR Implosive Therapy[Mesh] OR "cognitive behavioral therapy"[tiab:~2] OR "cognitive behaviour therapy"[tiab:~2] OR "cognitive behavioral treatment"[tiab:~2] OR "cognitive behaviour treatment"[tiab:~2] OR "cognitive therapy"[tiab:~1] OR "behavior therapy"[tiab:~1] OR "behaviour therapy"[tiab:~1] OR CBT[tiab] OR (cognitiv*[tiab] AND therap*[tiab]) OR (exposure[tiab] AND therap*[tiab]) OR exposure-based[tiab] OR "exposure and response prevention"[tiab:~1] OR "response prevention"[tiab:~1] OR systematic desensiti*[tiab] OR (behavior*[tiab] AND therap*[tiab]) OR (behaviour*[tiab] AND therap*[tiab]))) AND ("1800/01/01"[edat] : "2017/08/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 9 | 9 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Long-term follow-up or durability of outcomes | left out | 24,486 / 10,190 | 58.4% | none | 0/30 (up to 10% of removed records could be relevant) | Only nine known in-scope studies remain below the 15-record evidence threshold required to AND an optional concept. The second random 30-record loss sample was screened and contained no clearly eligible study; the long-term terms still reduce retrieval by roughly 58%, so follow-up duration stays for screening. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Anxiety and anxiety-related disorders | 1 | `(mental disorders[Mesh] OR mental[tiab] AND disorder*[tiab] OR psychological disorders[tiab] OR psychiatric[tiab] AND disorder*[tiab])` | 12,679 | 0/30 |
| Anxiety and anxiety-related disorders | 2 | `(mental disorders[Mesh] OR (mental[tiab] AND disorder*[tiab]) OR psychological disorders[tiab] OR (psychiatric[tiab] AND disorder*[tiab]))` | 49,322 | 0/30 |
| Cognitive behavioral and behavior therapies | 1 | `(Psychotherapy[Mesh] OR psychotherap*[tiab] OR therapy[tiab])` | 26,423 | not screened |
| Cognitive behavioral and behavior therapies | 2 | `(Psychotherapy[Mesh] OR psychotherap*[tiab] OR therapy[tiab])` | 26,423 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| anxiety | 221,591 | 0 |
| cbt | 262,969 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | First broad strategy with condition and intervention blocks plus a separately tested long-term follow-up candidate; terms include member disorders and CBT modalities to reduce category-word dependence. |
| 2 | 20,763 | anxiety: +5 / -5; cbt: +9 / -9 | none | Corrected quoted proximity syntax after lint flagged unquoted phrases; retained unordered proximity where word order varies. |
| 3 | 24,486 | cbt: +2 / -0 | none | Added explicit US and UK behavioral/behavioural therapy free-text coverage in response to internal critic R1-1; rerunning the optional follow-up evaluation against the revised query. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 1 findings; R1-1 should-fix open
- Round 2 on version 3: 1 findings; R1-1 should-fix resolved
- Round 3 on version 3: 1 findings; R1-1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1467 NCBI requests logged (793 from cache); strategy sha256 089d6eeea222._

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
        "message": "24,486 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "24,486 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-29T03:13:36+00:00",
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
      "requested": "Anxiety",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:13:36+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001007",
          "name": "Anxiety",
          "type": "descriptor",
          "scope_note": "Feelings or emotions of dread, apprehension, and impending disaster but not disabling as with ANXIETY DISORDERS.",
          "tree_numbers": [
            "F01.470.132"
          ],
          "entry_terms": 8,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001007",
      "preferred_label": "Anxiety",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "Anxiety",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Phobic Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:13:36+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D010698",
          "name": "Phobic Disorders",
          "type": "descriptor",
          "scope_note": "Anxiety disorders in which the essential feature is persistent and irrational fear of a specific object, activity, or situation that the individual feels compelled to avoid.",
          "tree_numbers": [
            "F03.080.725"
          ],
          "entry_terms": 6,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D010698",
      "preferred_label": "Phobic Disorders",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "Phobic Disorders",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Panic Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:13:36+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D016584",
          "name": "Panic Disorder",
          "type": "descriptor",
          "scope_note": "A type of anxiety disorder characterized by unexpected panic attacks that last minutes or, rarely, hours. Panic attacks begin with intense apprehension, fear or terror and, often, a feeling of impending doom. Symptoms experienced during a panic attack include dyspnea or sensations of being smothered; dizziness, loss of balance or faintness; choking sensations; palpitations or accelerated heart ...",
          "tree_numbers": [
            "F03.080.700"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D016584",
      "preferred_label": "Panic Disorder",
      "type": "descriptor",
      "location": "vocabulary:4",
      "term": {
        "text": "Panic Disorder",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Obsessive-Compulsive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:13:36+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D009771",
          "name": "Obsessive-Compulsive Disorder",
          "type": "descriptor",
          "scope_note": "An anxiety disorder characterized by recurrent, persistent obsessions or compulsions. Obsessions are the intrusive ideas, thoughts, or images that are experienced as senseless or repugnant. Compulsions are repetitive and seemingly purposeful behavior which the individual generally recognizes as senseless and from which the individual does not derive pleasure although it may provide a release fr...",
          "tree_numbers": [
            "F03.080.600"
          ],
          "entry_terms": 13,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D009771",
      "preferred_label": "Obsessive-Compulsive Disorder",
      "type": "descriptor",
      "location": "vocabulary:5",
      "term": {
        "text": "Obsessive-Compulsive Disorder",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:13:36+00:00",
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
      "location": "vocabulary:6",
      "term": {
        "text": "Stress Disorders, Post-Traumatic",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Behavior Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:13:36+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "Behavior Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognitive Behavioral Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:13:36+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "Cognitive Behavioral Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Desensitization, Psychologic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:13:36+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003887",
          "name": "Desensitization, Psychologic",
          "type": "descriptor",
          "scope_note": "A behavior therapy technique in which deep muscle relaxation is used to inhibit the effects of graded anxiety-evoking stimuli.",
          "tree_numbers": [
            "F04.754.137.506"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003887",
      "preferred_label": "Desensitization, Psychologic",
      "type": "descriptor",
      "location": "vocabulary:31",
      "term": {
        "text": "Desensitization, Psychologic",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Implosive Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:13:36+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D007171",
          "name": "Implosive Therapy",
          "type": "descriptor",
          "scope_note": "A method for extinguishing anxiety by a saturation exposure to the feared stimulus situation or its substitute.",
          "tree_numbers": [
            "F04.754.137.506.325"
          ],
          "entry_terms": 15,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D007171",
      "preferred_label": "Implosive Therapy",
      "type": "descriptor",
      "location": "vocabulary:32",
      "term": {
        "text": "Implosive Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"anxiety disorders\"[MeSH Terms] OR \"anxiety\"[MeSH Terms] OR \"phobic disorders\"[MeSH Terms] OR \"panic disorder\"[MeSH Terms] OR \"obsessive compulsive disorder\"[MeSH Terms] OR \"stress disorders, post traumatic\"[MeSH Terms] OR \"anxiet*\"[Title/Abstract] OR (\"anxiety\"[Title/Abstract] AND \"disorder*\"[Title/Abstract]) OR \"anxious\"[Title/Abstract] OR (\"generalized\"[Title/Abstract] AND \"anxiety\"[Title/Abstract]) OR (\"generalised\"[Title/Abstract] AND \"anxiety\"[Title/Abstract]) OR \"GAD\"[Title/Abstract] OR \"panic\"[Title/Abstract] OR \"agoraphobi*\"[Title/Abstract] OR \"phobi*\"[Title/Abstract] OR (\"social\"[Title/Abstract] AND \"anxi*\"[Title/Abstract]) OR \"social phobia\"[Title/Abstract:~1] OR \"separation anxiety\"[Title/Abstract:~1] OR \"obsessive-compulsive\"[Title/Abstract] OR \"obsessive-compulsive\"[Title/Abstract:~1] OR \"OCD\"[Title/Abstract] OR \"PTSD\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract:~1] OR \"post-traumatic stress\"[Title/Abstract:~1]) AND (\"behavior therapy\"[MeSH Terms] OR \"cognitive behavioral therapy\"[MeSH Terms] OR \"desensitization, psychologic\"[MeSH Terms] OR \"implosive therapy\"[MeSH Terms] OR \"cognitive behavioral therapy\"[Title/Abstract:~2] OR \"cognitive behaviour therapy\"[Title/Abstract:~2] OR \"cognitive behavioral treatment\"[Title/Abstract:~2] OR \"cognitive behaviour treatment\"[Title/Abstract:~2] OR \"cognitive therapy\"[Title/Abstract:~1] OR \"behavior therapy\"[Title/Abstract:~1] OR \"behaviour therapy\"[Title/Abstract:~1] OR \"CBT\"[Title/Abstract] OR (\"cognitiv*\"[Title/Abstract] AND \"therap*\"[Title/Abstract]) OR (\"exposure\"[Title/Abstract] AND \"therap*\"[Title/Abstract]) OR \"exposure-based\"[Title/Abstract] OR \"exposure and response prevention\"[Title/Abstract:~1] OR \"response prevention\"[Title/Abstract:~1] OR \"systematic desensiti*\"[Title/Abstract] OR (\"behavior*\"[Title/Abstract] AND \"therap*\"[Title/Abstract]) OR (\"behaviour*\"[Title/Abstract] AND \"therap*\"[Title/Abstract])) AND 1800/01/01:2017/08/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "592aa9e3da9aab8558e5f80c0be61728d71ce481c0f130c79bb55ab2bd50aca1",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no translation issues, and the combined-query translation reflects the listed MeSH, Title/Abstract, and date-entry clauses."
        },
        "operators": {
          "verdict": "pass",
          "note": "The anxiety and CBT synonym sets are OR-combined and then AND-combined; the optional follow-up block was evaluated separately."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed anxiety and therapy headings are reported as verified MeSH descriptors."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The intervention block lacks explicit free-text coverage for behavioral/behavioural therapy; the 0/30 category probe does not establish their absence among eligible records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no query errors or translation issues. Proximity clauses contain no truncation wildcards."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The query applies the stated Entrez date-entry bound and no unsupported follow-up or population filter."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Free-text intervention coverage does not explicitly include behavioral/behavioural therapy. The query has behavior/behaviour therapy phrases, while the CBT phrases cover cognitive behavioral/behaviour therapy; the separate adjective forms are not listed.",
          "recommendation": "Add tested free-text coverage such as behavior* AND therap* and behaviour* AND therap*, or equivalent explicit expressions, then run a complete evaluation.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The only optional concept identified in the packet, long-term follow-up or durability, was tested as an AND block. It would reduce retrieval by 55.1% to 9,317, but only nine known in-scope records are available, below the stated 15-record threshold for safely requiring it; the 0/30 loss sample cannot establish safety. Retaining the broad base retrieval for screening is justified despite exceeding the 10,000-record workload budget.",
          "evidence": "The packet reports a base count of 20,763, 9,317 with the optional block, nine known in-scope records, and a random loss sample with 0/30 relevant records. The decision leaves the optional block out because the evidence threshold is unmet."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "809592e4d3e7277d1f2e697b1590f47c592474cae4072d88dd6e33522d152a6f",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The current combined query reflects the listed anxiety and therapy clauses. The added behavioral/behavioural expressions are included in the translated intervention block."
        },
        "operators": {
          "verdict": "pass",
          "note": "The anxiety and therapy synonyms are OR-combined within their blocks, and the required blocks are AND-combined. The long-term block was evaluated separately as an optional AND block."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the listed anxiety and therapy headings as verified MeSH descriptors, with no heading translation errors."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The intervention block now explicitly includes behavior*[tiab] AND therap*[tiab] and behaviour*[tiab] AND therap*[tiab], addressing R1-1."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no query errors. Proximity clauses contain no truncation wildcards."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The stated Entrez date-entry bound is applied, and the strategy does not require the optional follow-up block or apply a population filter."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Free-text intervention coverage did not explicitly include behavioral/behavioural therapy.",
          "recommendation": "Add tested free-text coverage such as behavior* AND therap* and behaviour* AND therap*, or equivalent explicit expressions, then run a complete evaluation.",
          "status": "resolved",
          "response": "Resolved in version 3: both expressions appear as intervention terms #44 and #45, with reported counts of 69,586 and 22,244; the current strategy evaluation reports 24,486 results."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The only optional searchable concept named in the scope is long-term follow-up or durability, and it was tested as an extra AND block. I accept retaining the broader strategy for screening because the packet reports only nine known in-scope studies, below its 15-record threshold for requiring an optional block, and the loss sample does not establish that the block is safe. This leaves retrieval above the 10,000-record budget, even with the block.",
          "evidence": "The current base query (#47) returns 24,486 records. The optional long-term block reduces this to 10,190 (58.4%); the packet reports no known records lost and 0/30 relevant in the second random loss sample, while noting that up to 10% of removed records could still be relevant. The block therefore leaves retrieval 190 records over budget, and its loss evidence is insufficient to justify requiring it."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "809592e4d3e7277d1f2e697b1590f47c592474cae4072d88dd6e33522d152a6f",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The combined query reflects the listed anxiety and intervention terms. The added behavioral and behavioural therapy expressions appear in the translated intervention block."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are OR-combined within the required anxiety and intervention blocks, which are AND-combined. The optional follow-up block was evaluated separately."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the listed anxiety and therapy MeSH headings as verified, with no heading translation errors."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Behavior*[tiab] AND therap*[tiab] and behaviour*[tiab] AND therap*[tiab] address the prior intervention coverage finding."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no query errors. Proximity clauses contain no truncation wildcards."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The stated Entrez date-entry bound is applied. Follow-up timing remains for screening, consistent with the stated eligibility and the decision to leave out the optional follow-up block."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Free-text intervention coverage did not explicitly include behavioral/behavioural therapy.",
          "recommendation": "Add tested free-text coverage such as behavior* AND therap* and behaviour* AND therap*, or equivalent explicit expressions, then run a complete evaluation.",
          "status": "resolved",
          "response": "Version 3 includes both expressions as terms #44 and #45, with reported counts of 69,586 and 22,244. The current strategy evaluation reports 24,486 results."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The only optional searchable concept named in scope, long-term follow-up or durability of outcomes, was tested as an extra AND block and left out. Accept retaining the broader query for screening: the packet reports only nine known in-scope studies, below its 15-record threshold for requiring an optional block, and the loss sample does not establish that the block is safe. The current retrieval remains above the 10,000-record workload budget.",
          "evidence": "The current base query (#47) returns 24,486 records. The optional block, comprising Follow-Up Studies[Mesh], Treatment Outcome[Mesh], and follow-up, long-term, maintenance, durability, sustained, post-treatment, and related title/abstract terms, reduces retrieval to 10,190 (58.4%), still 190 above budget. The packet reports no known records lost and 0/30 relevant in the second random loss sample, while noting that up to 10% of removed records could be relevant."
        }
      ]
    }
  ]
}
```

