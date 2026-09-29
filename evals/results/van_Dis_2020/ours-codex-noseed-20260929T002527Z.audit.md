# PubMed search strategy: audit

Generated 2026-09-29T01:02:10+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Long-term outcomes of cognitive behavioral therapy for anxiety-related disorders
- Framework: PICO
- Scope confirmed by user: yes (User requested no follow-up questions and standard depth. Scope proceeded without user confirmation. Assumed anxiety-related disorders includes classic anxiety disorders plus OCD and PTSD, reflecting historical anxiety-related grouping. No seed records supplied. Cutoff fixed to PubMed Entrez date 2017-08-24 via PSB_AS_OF and protocol as_of; no publication-date limit. Long-term is an eligibility property to assess during screening; optional searchable follow-up concept will be tested. Operational definition assumed for long-term: at least 6 months after treatment ends. Three primary studies screened in from similar-article candidates linked to a relevant Cochrane review; these are development records, not independent validation.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Anxiety-related disorders | search | Population concept defining the review; include classic anxiety disorders and closely related OCD/PTSD because the question says anxiety-related. |
| Cognitive behavioral therapy | search | Intervention specified by the question; include cognitive, behavioral and combined CBT labels. |
| Long-term outcomes/follow-up | optional | Topic-defining outcome horizon, but duration and outcome labels may be inconsistently reported; test its retrieval cost and losses. |
| Comparators | screen | Not specified and not required in the search. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T01:01:06+00:00
- Records added to PubMed up to: 2017-08-24
- Total records: 6,812
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Anxiety Disorders[Mesh]` | 75,155 | none |
| 2 | `Phobic Disorders[Mesh]` | 12,282 | none |
| 3 | `Panic Disorder[Mesh]` | 6,597 | none |
| 4 | `Anxiety, Separation[Mesh]` | 2,050 | none |
| 5 | `Obsessive-Compulsive Disorder[Mesh]` | 14,139 | none |
| 6 | `Stress Disorders, Post-Traumatic[Mesh]` | 28,555 | none |
| 7 | `anxiety[tiab]` | 151,430 | none |
| 8 | `anxiet*[tiab]` | 153,037 | none |
| 9 | `generalized anxiety disorder[tiab]` | 4,859 | none |
| 10 | `social anxiety[tiab]` | 4,792 | none |
| 11 | `social phobia[tiab]` | 3,620 | none |
| 12 | `panic[tiab]` | 13,408 | none |
| 13 | `agoraphob*[tiab]` | 3,183 | none |
| 14 | `phobi*[tiab]` | 10,712 | none |
| 15 | `obsessive-compulsive[tiab]` | 15,107 | none |
| 16 | `obsessive compulsive[tiab]` | 15,107 | none |
| 17 | `OCD[tiab]` | 7,878 | none |
| 18 | `PTSD[tiab]` | 18,640 | none |
| 19 | `posttraumatic stress[tiab]` | 16,639 | none |
| 20 | `post-traumatic stress[tiab]` | 9,637 | none |
| 21 | `separation anxiety[tiab]` | 1,365 | none |
| 22 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21` | 233,077 | none |
| 23 | `Behavior Therapy[Mesh]` | 66,990 | none |
| 24 | `cognitive behavio* therap*[tiab]` | 12,875 | none |
| 25 | `cognitive therap*[tiab]` | 2,812 | none |
| 26 | `behavior therap*[tiab]` | 4,378 | none |
| 27 | `behaviour therap*[tiab]` | 2,193 | none |
| 28 | `cognitive behavio* treatment*[tiab]` | 1,786 | none |
| 29 | `CBT[tiab]` | 8,158 | none |
| 30 | `exposure therap*[tiab]` | 1,294 | none |
| 31 | `#23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30` | 74,708 | none |
| 32 | `Follow-Up Studies[Mesh]` | 594,219 | none |
| 33 | `long-term[tiab]` | 661,989 | none |
| 34 | `long term[tiab]` | 661,989 | none |
| 35 | `follow-up[tiab]` | 788,429 | none |
| 36 | `followup[tiab]` | 751,136 | none |
| 37 | `longitudinal[tiab]` | 194,058 | none |
| 38 | `maintenance[tiab]` | 234,429 | none |
| 39 | `sustained[tiab]` | 189,388 | none |
| 40 | `durability[tiab]` | 14,752 | none |
| 41 | `month*[tiab]` | 1,370,657 | none |
| 42 | `year*[tiab]` | 3,027,986 | none |
| 43 | `#32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42` | 4,864,862 | none |
| 44 | `#22 AND #31 AND #43` | 6,812 | none |

### Strategy (single line, for copying into PubMed)

```text
((Anxiety Disorders[Mesh] OR Phobic Disorders[Mesh] OR Panic Disorder[Mesh] OR Anxiety, Separation[Mesh] OR Obsessive-Compulsive Disorder[Mesh] OR Stress Disorders, Post-Traumatic[Mesh] OR anxiety[tiab] OR anxiet*[tiab] OR generalized anxiety disorder[tiab] OR social anxiety[tiab] OR social phobia[tiab] OR panic[tiab] OR agoraphob*[tiab] OR phobi*[tiab] OR obsessive-compulsive[tiab] OR obsessive compulsive[tiab] OR OCD[tiab] OR PTSD[tiab] OR posttraumatic stress[tiab] OR post-traumatic stress[tiab] OR separation anxiety[tiab]) AND (Behavior Therapy[Mesh] OR cognitive behavio* therap*[tiab] OR cognitive therap*[tiab] OR behavior therap*[tiab] OR behaviour therap*[tiab] OR cognitive behavio* treatment*[tiab] OR CBT[tiab] OR exposure therap*[tiab]) AND (Follow-Up Studies[Mesh] OR long-term[tiab] OR long term[tiab] OR follow-up[tiab] OR followup[tiab] OR longitudinal[tiab] OR maintenance[tiab] OR sustained[tiab] OR durability[tiab] OR month*[tiab] OR year*[tiab])) AND ("1800/01/01"[edat] : "2017/08/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 4 | 4 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Long-term outcomes/follow-up | AND-ed | 16,411 / 6,812 | 58.5% | none | 0/30 (up to 10% of removed records could be relevant) | After expanding the follow-up block to include month* and year*, the re-tested 30-record loss sample contained no study meeting the anxiety-related CBT and >=6-month post-treatment criteria. The block reduces results by 58.5% (16,411 to 6,812); AND-ing is justified for this specifically long-term review, with risk of follow-up reported only in full text documented. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Anxiety-related disorders | 1 | `(Mental Disorders[Mesh] OR mental[tiab] OR psychiatric[tiab] OR disorder*[tiab])` | 27,286 | 0/30 |
| Anxiety-related disorders | 2 | `(Mental Disorders[Mesh] OR mental[tiab] OR psychiatric[tiab] OR disorder*[tiab])` | 7,074 | 0/30 |
| Cognitive behavioral therapy | 1 | `(Psychotherapy[Mesh] OR psychotherap*[tiab] OR exposure[tiab] OR behavior*[tiab] OR behaviour*[tiab] OR cognitive[tiab])` | 72,545 | not screened |
| Cognitive behavioral therapy | 2 | `(Psychotherapy[Mesh] OR psychotherap*[tiab] OR exposure[tiab] OR behavior*[tiab] OR behaviour*[tiab] OR cognitive[tiab])` | 72,545 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| anxiety | 27,185 | 0 |
| cbt | 77,264 | 0 |
| long_term | 16,411 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | First full draft: broad anxiety-related disorder and CBT blocks with MeSH and title/abstract terms; long-term follow-up is an optional block for empirical testing. |
| 2 | 16,411 | anxiety: +21 / -0; cbt: +8 / -0 | none | First full draft: broad anxiety-related disorder and CBT blocks with MeSH and title/abstract terms; long-term follow-up is an optional block for empirical testing. |
| 3 | 4,709 | long_term: +9 / -0 | none | Applied the optional long-term follow-up block after the required loss sample found no eligible records and the reduction exceeded 30%; category probes screened with zero relevant records. |
| 4 | 6,812 | long_term: +2 / -0 | none | Recovered missed relevant PMID 28527657 by adding month*/year* time expressions to the long-term block; the abstract reports assessment 6 months after treatment completion without a follow-up label. |
| 5 | 16,411 | long_term: +0 / -11 | none | Temporarily leave long_term out to remeasure its revised block and refresh the decision-bound loss sample. |
| 6 | 6,812 | long_term: +11 / -0 | none | Re-decided the revised long-term block after screening its fresh 30-record loss sample; retains all four relevant development records. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 6: 1 findings; P1-01 document accepted-risk
- Round 2 on version 6: 1 findings; P1-01 document accepted-risk
- Round 3 on version 6: 1 findings; P1-01 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1176 NCBI requests logged (582 from cache); strategy sha256 7bb99df43555._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:anxiety",
        "blocking": false,
        "requires_review": true,
        "id": "I-504095d42e9d201c2368"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:cbt",
        "blocking": false,
        "requires_review": true,
        "id": "I-55bac4b0c1a86e93826e"
      }
    ],
    "issues": [
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:anxiety",
        "blocking": false,
        "requires_review": true,
        "id": "I-504095d42e9d201c2368"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:cbt",
        "blocking": false,
        "requires_review": true,
        "id": "I-55bac4b0c1a86e93826e"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Anxiety Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:01:06+00:00",
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
      "requested": "Phobic Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:01:06+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "Phobic Disorders",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Panic Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:01:06+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "Panic Disorder",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Anxiety, Separation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:01:06+00:00",
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
      "location": "vocabulary:4",
      "term": {
        "text": "Anxiety, Separation",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Obsessive-Compulsive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:01:06+00:00",
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
      "checked_at": "2026-09-29T01:01:06+00:00",
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
      "checked_at": "2026-09-29T01:01:06+00:00",
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
      "location": "vocabulary:22",
      "term": {
        "text": "Behavior Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Follow-Up Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T01:01:06+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "Follow-Up Studies",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"anxiety disorders\"[MeSH Terms] OR \"phobic disorders\"[MeSH Terms] OR \"panic disorder\"[MeSH Terms] OR \"anxiety, separation\"[MeSH Terms] OR \"obsessive compulsive disorder\"[MeSH Terms] OR \"stress disorders, post traumatic\"[MeSH Terms] OR \"anxiety\"[Title/Abstract] OR \"anxiet*\"[Title/Abstract] OR \"generalized anxiety disorder\"[Title/Abstract] OR \"social anxiety\"[Title/Abstract] OR \"social phobia\"[Title/Abstract] OR \"panic\"[Title/Abstract] OR \"agoraphob*\"[Title/Abstract] OR \"phobi*\"[Title/Abstract] OR \"obsessive-compulsive\"[Title/Abstract] OR \"obsessive-compulsive\"[Title/Abstract] OR \"OCD\"[Title/Abstract] OR \"PTSD\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"post traumatic stress\"[Title/Abstract] OR \"separation anxiety\"[Title/Abstract]) AND (\"behavior therapy\"[MeSH Terms] OR \"cognitive behavio* therap*\"[Title/Abstract] OR \"cognitive therap*\"[Title/Abstract] OR \"behavior therap*\"[Title/Abstract] OR \"behaviour therap*\"[Title/Abstract] OR \"cognitive behavio* treatment*\"[Title/Abstract] OR \"CBT\"[Title/Abstract] OR \"exposure therap*\"[Title/Abstract]) AND (\"follow up studies\"[MeSH Terms] OR \"long-term\"[Title/Abstract] OR \"long-term\"[Title/Abstract] OR \"follow-up\"[Title/Abstract] OR \"followup\"[Title/Abstract] OR \"longitudinal\"[Title/Abstract] OR \"maintenance\"[Title/Abstract] OR \"sustained\"[Title/Abstract] OR \"durability\"[Title/Abstract] OR \"month*\"[Title/Abstract] OR \"year*\"[Title/Abstract]) AND 1800/01/01:2017/08/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 6,
      "review_sha256": "452070fba763727fddd9f15172b22a02a7c57f3ed6111ca4c30111b9e25e9827",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The blocks cover the stated anxiety-related scope, including the named OCD/PTSD extensions, and the CBT block includes cognitive, behavioral, combined, and exposure therapy wording. The optional follow-up block includes month* and year*. No translation issues or warning diagnostics are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The final query ORs synonyms within each block and ANDs anxiety, CBT, and the chosen optional follow-up block. The optional block reduces 16,411 records to 6,812; its 30-record loss sample found no eligible records and no known relevant records were lost. The residual risk of follow-up being reported only in full text is documented."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet records verification of the selected MeSH descriptors: Anxiety Disorders, Phobic Disorders, Panic Disorder, Anxiety, Separation, Obsessive-Compulsive Disorder, Stress Disorders, Post-Traumatic, Behavior Therapy, and Follow-Up Studies. Each is entered with [Mesh], and text words supplement the headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes disorder names and common abbreviations, cognitive and behavioral therapy variants, and follow-up, duration, and maintenance wording. Anxiety probes screened 30 records each with no relevant records; the CBT evidence is weaker because its first probe was unscreened and the second draw repeated the same 30-record sample."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query is parenthesized by block, uses valid-looking PubMed field tags and Boolean operators, and includes an explicit Entrez date range through 2017-08-24. The packet reports no raw query errors or warnings and no translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No human-only or other eligibility filter is applied; human eligibility and animal exclusion remain for screening. The fixed Entrez-date cutoff is stated in the protocol and final query. The optional follow-up block's retrieval loss and full-text reporting risk are documented."
        }
      },
      "findings": [
        {
          "id": "P1-01",
          "domain": "text_words",
          "severity": "document",
          "kind": "reporting",
          "finding": "Category-probe evidence is stale for both searched blocks. The anxiety category has two screened samples with 0/30 relevant each, while the CBT category has one unscreened probe and one screened sample of 30; the packet says the second CBT draw duplicated the first. Validation marks both category probes stale and says the probe budget is spent.",
          "recommendation": "Retain the warnings as a documented limitation. If further probe budget becomes available, draw fresh samples against the current strategy before treating the category probes as current sensitivity evidence.",
          "status": "accepted-risk",
          "response": "The stale status and limited independent CBT probing are explicitly disclosed. The available probes found no eligible records outside the blocks, and the known relevant records are retrieved, but these observations do not establish current category sensitivity."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-504095d42e9d201c2368",
          "status": "accepted-risk",
          "response": "Accept the stale anxiety-probe warning as a documented limitation; the probe budget is spent, so the packet cannot supply a fresh current-version sample.",
          "evidence": "The packet records two screened anxiety probes of 30 records each, both with zero relevant records, and marks the category status stale. The current strategy retrieves all four known relevant records, but those are development records, not independent validation."
        },
        {
          "issue_id": "I-55bac4b0c1a86e93826e",
          "status": "accepted-risk",
          "response": "Accept the stale CBT-probe warning as a documented limitation; the available evidence is only one unique screened sample, with no remaining probe budget.",
          "evidence": "The first CBT probe is listed as not screened; the second screened 30 records and found zero relevant, and the packet says the second draw duplicated the same sample. The category status is stale, and all four known relevant records are retrieved."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 6,
      "review_sha256": "452070fba763727fddd9f15172b22a02a7c57f3ed6111ca4c30111b9e25e9827",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The anxiety block covers the stated disorders, including the named OCD and PTSD extensions. The CBT block covers cognitive, behavioral, combined, and exposure therapy wording, and the follow-up block includes the six-month horizon's month and year terms. The packet reports no translation issues."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within blocks and the selected blocks are ANDed. The optional follow-up block reduces results from 16,411 to 6,812; its 30-record loss sample found no eligible records and no known relevant records were lost. The documented risk of duration being reported only in full text remains."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verification of the selected MeSH descriptors for anxiety-related disorders, CBT, and follow-up. The headings are supplemented with title and abstract terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The terms cover disorder names and abbreviations, therapy variants, and follow-up, duration, and maintenance wording. Category-probe evidence remains limited and stale: anxiety has two screened samples with 0/30 relevant each; CBT has one unscreened probe and one screened sample, with the packet reporting that the screened draw duplicated the first."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query is grouped by concept, uses PubMed field tags and Boolean operators, and applies the stated Entrez date range through 2017-08-24. The packet reports no raw query errors or warnings and no translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No human-only or animal filter is applied; those eligibility criteria remain for screening. The Entrez-date cutoff is stated in the protocol and query. The follow-up block's retrieval loss and full-text reporting risk are documented."
        }
      },
      "findings": [
        {
          "id": "P1-01",
          "domain": "text_words",
          "severity": "document",
          "kind": "reporting",
          "finding": "Category-probe evidence is stale for both searched blocks. The anxiety category has two screened samples with 0/30 relevant each. The CBT category has one unscreened probe and one screened sample of 30; the packet reports that the second draw duplicated the first. Validation marks both probes stale and says their budgets are spent.",
          "recommendation": "Retain the warnings as a documented limitation. If probe budget becomes available, draw fresh samples against the current strategy before treating the probes as current sensitivity evidence.",
          "status": "accepted-risk",
          "response": "The stale status and limited independent CBT probing are disclosed. The available probes found no eligible records outside the blocks, and all four known relevant development records are retrieved; neither observation establishes current category sensitivity."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-504095d42e9d201c2368",
          "status": "accepted-risk",
          "response": "Accept the stale anxiety-probe warning as a documented limitation. The packet says the probe budget is spent, so it provides no fresh current-version sample.",
          "evidence": "The packet records two screened anxiety probes of 30 records each, both with zero relevant records, and marks the category status stale. The strategy retrieves all four known relevant records, but these are development records rather than independent validation."
        },
        {
          "issue_id": "I-55bac4b0c1a86e93826e",
          "status": "accepted-risk",
          "response": "Accept the stale CBT-probe warning as a documented limitation. The available evidence includes only one unique screened sample, with no remaining probe budget.",
          "evidence": "The first CBT probe is listed as unscreened; the second screened 30 records and found zero relevant, and the packet reports that the second draw duplicated the first sample. The category status is stale, and all four known relevant development records are retrieved."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 6,
      "review_sha256": "452070fba763727fddd9f15172b22a02a7c57f3ed6111ca4c30111b9e25e9827",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched blocks cover the named anxiety-related conditions, including the OCD and PTSD extensions, and include cognitive, behavioral, combined, and exposure therapy wording. The follow-up block includes month* and year*. No translation issues are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within blocks, and the anxiety, CBT, and selected follow-up blocks are ANDed. The follow-up block reduces results from 16,411 to 6,812; its loss sample found no eligible records, and the risk of follow-up being reported only in full text is documented."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verification of the selected MeSH descriptors for anxiety-related disorders, behavior therapy, and follow-up studies. The headings are supplemented with title and abstract terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The terms cover disorder names and abbreviations, therapy variants, and follow-up and duration wording. Category-probe evidence remains stale: anxiety has two screened samples with 0/30 relevant each; CBT has one unscreened probe and one screened sample, which duplicated the first draw. This limitation is carried forward."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query groups terms by concept, uses PubMed field tags and Boolean operators, and applies the stated Entrez date range through 2017-08-24. The packet reports no raw query errors, warnings, or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No human-only or animal filter is applied; those criteria remain for screening. The date cutoff is stated in the protocol and query. The follow-up block's retrieval loss and risk of duration being reported only in full text are documented."
        }
      },
      "findings": [
        {
          "id": "P1-01",
          "domain": "text_words",
          "severity": "document",
          "kind": "reporting",
          "finding": "Category-probe evidence is stale for both searched blocks. Anxiety has two screened samples with 0/30 relevant each. CBT has one unscreened probe and one screened sample of 30; the packet reports that the second draw duplicated the first. Validation marks both probes stale and says their budgets are spent.",
          "recommendation": "Retain the warnings as a documented limitation. If probe budget becomes available, draw fresh samples against the current strategy before treating the probes as current sensitivity evidence.",
          "status": "accepted-risk",
          "response": "The stale status and limited independent CBT probing are disclosed. The available probes found no eligible records outside the blocks, and all four known relevant development records are retrieved; neither observation establishes current category sensitivity."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-504095d42e9d201c2368",
          "status": "accepted-risk",
          "response": "Accept the stale anxiety-probe warning as a documented limitation. The probe budget is spent, so the packet provides no fresh current-version sample.",
          "evidence": "The packet records two screened anxiety probes of 30 records each, both with zero eligible records, and marks the category status stale. The strategy retrieves all four known relevant development records, but these are not independent validation."
        },
        {
          "issue_id": "I-55bac4b0c1a86e93826e",
          "status": "accepted-risk",
          "response": "Accept the stale CBT-probe warning as a documented limitation. The available evidence includes only one unique screened sample, with no remaining probe budget.",
          "evidence": "The first CBT probe is listed as unscreened; the second screened 30 records and found zero eligible, and the packet reports that the second draw duplicated the first sample. The category status is stale, and all four known relevant development records are retrieved."
        }
      ]
    }
  ]
}
```

