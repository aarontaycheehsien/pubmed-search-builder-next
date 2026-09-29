# PubMed search strategy: audit

Generated 2026-09-29T03:40:58+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Long-term outcomes of cognitive behavioral therapy for anxiety-related disorders
- Framework: PICO (intervention effectiveness)
- Scope confirmed by user: yes (User asked to proceed without questions. Assumed intervention-effectiveness framing; CBT and anxiety-related disorders are the required search concepts, while long-term follow-up is tested as optional and duration is screened. Used a broad clinical anxiety-spectrum interpretation including OCD and PTSD where treated as anxiety-related. Long-term means at least 6 months after treatment or authors explicitly label the follow-up long-term. No language, age, study-design, or publication-date restrictions. Search cutoff is PubMed Entrez date 2017-08-24, enforced by PSB_AS_OF for every command and protocol as_of; no [dp] cutoff. No known relevant articles supplied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Anxiety-related disorders | search | Target clinical population; disorder names are searchable, but records may name a particular disorder rather than the umbrella category. |
| Cognitive behavioral therapy | search | Intervention of interest; intervention names and CBT variants are searchable, with relevant reports sometimes using a named component or delivery form. |
| Long-term outcomes or follow-up | optional | Topic-defining duration/outcome property that may be named in abstracts but is not certain to be indexed or described consistently; test as an optional AND block. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T03:40:01+00:00
- Records added to PubMed up to: 2017-08-24
- Total records: 19,587
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Anxiety Disorders"[Mesh]` | 75,155 | none |
| 2 | `"Obsessive-Compulsive Disorder"[Mesh]` | 14,139 | none |
| 3 | `"Phobic Disorders"[Mesh]` | 12,282 | none |
| 4 | `"Panic Disorder"[Mesh]` | 6,597 | none |
| 5 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 28,555 | none |
| 6 | `"Agoraphobia"[Mesh]` | 2,516 | none |
| 7 | `"Anxiety, Separation"[Mesh]` | 2,050 | none |
| 8 | `anxiety[tiab]` | 151,430 | none |
| 9 | `anxious[tiab]` | 14,019 | none |
| 10 | `"generalized anxiety"[tiab]` | 5,844 | none |
| 11 | `GAD[tiab]` | 7,728 | none |
| 12 | `"panic disorder"[tiab]` | 8,365 | none |
| 13 | `agoraphobi*[tiab]` | 3,183 | none |
| 14 | `"separation anxi*"[tiab]` | 1,376 | none |
| 15 | `phobi*[tiab]` | 10,712 | none |
| 16 | `"social anxi*"[tiab]` | 4,818 | none |
| 17 | `"social phobi*"[tiab]` | 3,768 | none |
| 18 | `sociophob*[tiab]` | 17 | none |
| 19 | `obsessive-compulsive[tiab]` | 15,107 | none |
| 20 | `"obsessive compulsive"[tiab]` | 15,107 | none |
| 21 | `OCD[tiab]` | 7,878 | none |
| 22 | `posttraumatic[tiab]` | 52,009 | none |
| 23 | `"post-traumatic"[tiab]` | 24,958 | none |
| 24 | `PTSD[tiab]` | 18,640 | none |
| 25 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24` | 266,412 | none |
| 26 | `"Cognitive Behavioral Therapy"[Mesh]` | 24,064 | none |
| 27 | `"Behavior Therapy"[Mesh]` | 66,990 | none |
| 28 | `"cognitive behavioral therapy"[tiab]` | 6,806 | none |
| 29 | `"cognitive behaviour therapy"[tiab]` | 1,404 | none |
| 30 | `"cognitive behavioral treatment"[tiab]` | 1,140 | none |
| 31 | `"cognitive behaviour treatment"[tiab]` | 11 | none |
| 32 | `"cognitive therapy"[tiab]` | 2,592 | none |
| 33 | `"behavior therapy"[tiab]` | 4,182 | none |
| 34 | `"behaviour therapy"[tiab]` | 2,129 | none |
| 35 | `CBT[tiab]` | 8,158 | none |
| 36 | `"exposure therapy"[tiab]` | 1,242 | none |
| 37 | `"exposure treatment"[tiab]` | 703 | none |
| 38 | `"exposure and response prevention"[tiab]` | 274 | none |
| 39 | `"exposure and ritual prevention"[tiab]` | 51 | none |
| 40 | `ERP[tiab]` | 13,251 | none |
| 41 | `(cogniti*[tiab] AND behavio*[tiab] AND therap*[tiab])` | 23,260 | none |
| 42 | `(cogniti*[tiab] AND behavio*[tiab] AND treatment*[tiab])` | 28,599 | none |
| 43 | `#26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42` | 105,548 | none |
| 44 | `#25 AND #43` | 19,587 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Anxiety Disorders"[Mesh] OR "Obsessive-Compulsive Disorder"[Mesh] OR "Phobic Disorders"[Mesh] OR "Panic Disorder"[Mesh] OR "Stress Disorders, Post-Traumatic"[Mesh] OR "Agoraphobia"[Mesh] OR "Anxiety, Separation"[Mesh] OR anxiety[tiab] OR anxious[tiab] OR "generalized anxiety"[tiab] OR GAD[tiab] OR "panic disorder"[tiab] OR agoraphobi*[tiab] OR "separation anxi*"[tiab] OR phobi*[tiab] OR "social anxi*"[tiab] OR "social phobi*"[tiab] OR sociophob*[tiab] OR obsessive-compulsive[tiab] OR "obsessive compulsive"[tiab] OR OCD[tiab] OR posttraumatic[tiab] OR "post-traumatic"[tiab] OR PTSD[tiab]) AND ("Cognitive Behavioral Therapy"[Mesh] OR "Behavior Therapy"[Mesh] OR "cognitive behavioral therapy"[tiab] OR "cognitive behaviour therapy"[tiab] OR "cognitive behavioral treatment"[tiab] OR "cognitive behaviour treatment"[tiab] OR "cognitive therapy"[tiab] OR "behavior therapy"[tiab] OR "behaviour therapy"[tiab] OR CBT[tiab] OR "exposure therapy"[tiab] OR "exposure treatment"[tiab] OR "exposure and response prevention"[tiab] OR "exposure and ritual prevention"[tiab] OR ERP[tiab] OR (cogniti*[tiab] AND behavio*[tiab] AND therap*[tiab]) OR (cogniti*[tiab] AND behavio*[tiab] AND treatment*[tiab]))) AND ("1800/01/01"[edat] : "2017/08/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 4 | 4 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Long-term outcomes or follow-up | left out | 19,587 / 6,027 | 69.2% | none | 0/30 (up to 10% of removed records could be relevant) | The current required-concept strategy has only four screened long-term benchmark records, fewer than the 15-record evidence threshold. The current 30-record loss sample was screened; it contained no record clearly meeting the long-term outcome criterion. Leave the optional block out to protect recall; screen duration at full text. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Anxiety-related disorders | 1 | `disorder*[tiab] OR "mental disorders"[Mesh]` | 37,170 | 0/30 |
| Anxiety-related disorders | 2 | `disorder*[tiab] OR "mental disorders"[Mesh]` | 36,852 | not screened |
| Anxiety-related disorders | 3 | `disorder*[tiab] OR "mental disorders"[Mesh]` | 36,852 | 0/30 |
| Cognitive behavioral therapy | 1 | `psychotherapy[Mesh] OR exposure[tiab] OR "cognitive restructur*"[tiab] OR "behavioral activation"[tiab] OR "behavioural activation"[tiab]` | 23,151 | 0/30 |
| Cognitive behavioral therapy | 2 | `psychotherapy[Mesh] OR exposure[tiab] OR "cognitive restructur*"[tiab] OR "behavioral activation"[tiab] OR "behavioural activation"[tiab]` | 24,847 | not screened |
| Cognitive behavioral therapy | 3 | `psychotherapy[Mesh] OR exposure[tiab] OR "cognitive restructur*"[tiab] OR "behavioral activation"[tiab] OR "behavioural activation"[tiab]` | 24,847 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| anxiety_disorders | 105,548 | 0 |
| cognitive_behavioral_therapy | 266,412 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial question-led two-block search; long-term follow-up held as an optional candidate. Cutoff enforced by Entrez date. No known records supplied; begin review and pilot discovery. |
| 2 | 19,268 | anxiety_disorders: +20 / -0; cognitive_behavioral_therapy: +18 / -0 | none | Structured OR terms with explicit MeSH and title/abstract coverage for required concepts; optional long-term follow-up block added for empirical assessment. |
| 3 | 19,587 | anxiety_disorders: +5 / -1; cognitive_behavioral_therapy: +0 / -1 | none | Corrected MeSH labels to canonical authority headings, removed a duplicate noncanonical therapy heading, and expanded named anxiety-spectrum members (agoraphobia and separation anxiety). |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 0 findings; 
- Round 2 on version 3: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 827 NCBI requests logged (317 from cache); strategy sha256 86f892451b29._

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
        "message": "19,587 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "message": "19,587 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
      "checked_at": "2026-09-29T03:40:01+00:00",
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
        "text": "\"Anxiety Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Obsessive-Compulsive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:40:01+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"Obsessive-Compulsive Disorder\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Phobic Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:40:01+00:00",
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
        "text": "\"Phobic Disorders\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Panic Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:40:01+00:00",
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
        "text": "\"Panic Disorder\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:40:01+00:00",
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
      "location": "vocabulary:5",
      "term": {
        "text": "\"Stress Disorders, Post-Traumatic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Agoraphobia",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:40:01+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000379",
          "name": "Agoraphobia",
          "type": "descriptor",
          "scope_note": "Obsessive, persistent, intense fear of places or situations from which escape might be difficult or embarrassing.",
          "tree_numbers": [
            "F03.080.725.250"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000379",
      "preferred_label": "Agoraphobia",
      "type": "descriptor",
      "location": "vocabulary:6",
      "term": {
        "text": "\"Agoraphobia\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Anxiety, Separation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:40:01+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001010",
          "name": "Anxiety, Separation",
          "type": "descriptor",
          "scope_note": "Anxiety experienced by an individual upon separation from a person or object of particular significance to the individual.",
          "tree_numbers": [
            "F03.080.300",
            "F03.625.047"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001010",
      "preferred_label": "Anxiety, Separation",
      "type": "descriptor",
      "location": "vocabulary:7",
      "term": {
        "text": "\"Anxiety, Separation\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognitive Behavioral Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:40:01+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "\"Cognitive Behavioral Therapy\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Behavior Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:40:01+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "\"Behavior Therapy\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Anxiety Disorders\"[MeSH Terms] OR \"Obsessive-Compulsive Disorder\"[MeSH Terms] OR \"Phobic Disorders\"[MeSH Terms] OR \"Panic Disorder\"[MeSH Terms] OR \"stress disorders, post traumatic\"[MeSH Terms] OR \"Agoraphobia\"[MeSH Terms] OR \"anxiety, separation\"[MeSH Terms] OR \"anxiety\"[Title/Abstract] OR \"anxious\"[Title/Abstract] OR \"generalized anxiety\"[Title/Abstract] OR \"GAD\"[Title/Abstract] OR \"Panic Disorder\"[Title/Abstract] OR \"agoraphobi*\"[Title/Abstract] OR \"separation anxi*\"[Title/Abstract] OR \"phobi*\"[Title/Abstract] OR \"social anxi*\"[Title/Abstract] OR \"social phobi*\"[Title/Abstract] OR \"sociophob*\"[Title/Abstract] OR \"obsessive-compulsive\"[Title/Abstract] OR \"obsessive-compulsive\"[Title/Abstract] OR \"OCD\"[Title/Abstract] OR \"posttraumatic\"[Title/Abstract] OR \"post-traumatic\"[Title/Abstract] OR \"PTSD\"[Title/Abstract]) AND (\"Cognitive Behavioral Therapy\"[MeSH Terms] OR \"Behavior Therapy\"[MeSH Terms] OR \"Cognitive Behavioral Therapy\"[Title/Abstract] OR \"cognitive behaviour therapy\"[Title/Abstract] OR \"cognitive behavioral treatment\"[Title/Abstract] OR \"cognitive behaviour treatment\"[Title/Abstract] OR \"cognitive therapy\"[Title/Abstract] OR \"Behavior Therapy\"[Title/Abstract] OR \"behaviour therapy\"[Title/Abstract] OR \"CBT\"[Title/Abstract] OR \"exposure therapy\"[Title/Abstract] OR \"exposure treatment\"[Title/Abstract] OR \"exposure and response prevention\"[Title/Abstract] OR \"exposure and ritual prevention\"[Title/Abstract] OR \"ERP\"[Title/Abstract] OR (\"cogniti*\"[Title/Abstract] AND \"behavio*\"[Title/Abstract] AND \"therap*\"[Title/Abstract]) OR (\"cogniti*\"[Title/Abstract] AND \"behavio*\"[Title/Abstract] AND \"treatment*\"[Title/Abstract])) AND 1800/01/01:2017/08/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "1c60e6fd3ea174038100980a04cf78c45b5806b2683b31a99544bb0a458f3947",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no translation issues. The translated query retains the anxiety and CBT blocks, and all four benchmark records are retrieved. This benchmark is small, so it supports translation checking but does not establish broad sensitivity."
        },
        "operators": {
          "verdict": "pass",
          "note": "The strategy ORs synonyms within each concept and ANDs the two required concepts. The long-term follow-up block was tested and left out with a recall rationale; duration remains an eligibility criterion for screening."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes the listed anxiety and CBT MeSH headings. The packet reports that the headings were verified and that both required blocks retrieve all four benchmark records."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words cover the disorder names and CBT terms named in the scope, including OCD, PTSD, panic, phobic/social anxiety, exposure, and response prevention. The broad anxiety term and other variants supplement the specific names."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no query errors or translation issues, and provides a translated final query with the entry-date cutoff applied."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, study-design, or publication-date restrictions are applied. The entry-date cutoff is documented as 2017-08-24. Long-term follow-up is screened rather than imposed as a required search filter."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "Accept the screening workload as a documented recall tradeoff. The optional follow-up block was tested, but the evidence for using it to narrow the required-concept set is limited; retain the broad strategy and assess follow-up duration during screening.",
          "evidence": "The final strategy returns 19,587 records against a 10,000-record workload budget. The optional block reduces the set to 6,027 records (69.2%), but only four benchmark records were available and the 30-record loss sample contained no clearly eligible long-term record. All four benchmark records are retrieved by the required-concept strategy."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "1c60e6fd3ea174038100980a04cf78c45b5806b2683b31a99544bb0a458f3947",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Round 1 had no translation findings. The strategy is unchanged at version 3, and the prior translation assessment remains applicable."
        },
        "operators": {
          "verdict": "pass",
          "note": "Round 1 had no operator findings. The required blocks and tested optional follow-up block are unchanged."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Round 1 had no subject-heading findings. The strategy is unchanged."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Round 1 had no text-word findings. The strategy is unchanged."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Round 1 had no syntax findings. The packet reports the same strategy version and review hash."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Round 1 had no limits or filter findings. The documented cutoff and screening approach are unchanged."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The prior accepted-risk disposition is carried forward. The strategy is unchanged, and the packet retains the rationale for accepting the screening workload while assessing follow-up duration during screening.",
          "evidence": "The packet reports 19,587 results against a 10,000-record budget, the optional follow-up block's 69.2% reduction, four retrieved benchmark records, and a 30-record loss sample with no clearly eligible long-term record."
        }
      ]
    }
  ]
}
```

