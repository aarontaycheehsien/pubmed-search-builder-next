# PubMed search strategy: audit

Generated 2026-09-29T00:23:40+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Long-term outcomes of cognitive behavioral therapy for anxiety-related disorders
- Framework: PICO (intervention effectiveness)
- Scope confirmed by user: no (User asked to proceed without questions. Scope decisions are provisional assumptions. Interpret anxiety-related disorders broadly to include anxiety disorders and historically associated OCD and PTSD; screen for a defined anxiety-related clinical target. Long-term means outcomes measured at follow-up beyond acute treatment, with no minimum duration imposed because none was specified. No age, language, publication-date, or study-design limits. PSB_AS_OF is set to 2017-08-24 for every command as an Entrez-date cutoff; do not add a publication-date limit. No seeds were supplied; standard-depth discovery and screening will be attempted. The Generalized Anxiety Disorder MeSH heading was checked but returned zero records under the cutoff; it was removed after testing, while the Anxiety Disorders MeSH tree and generalized/generalised anxiety text wording remain.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Anxiety and anxiety-related disorders | search | The disorder family defines the target population and is expected to be named or indexed; individual member diagnoses must also be searched. |
| Cognitive behavioral therapy and named CBT variants | search | The intervention defines eligibility; CBT terminology and common named variants are searchable, with generic psychotherapy reserved for a category probe. |
| Long-term follow-up or persistence of outcomes after CBT | optional | Long-term outcome is topic-defining but follow-up duration and persistence may be inconsistently named; test its retrieval effect before deciding whether to AND it. |
| Comparators | screen | Comparators vary and are not needed to identify CBT studies. |
| Specific clinical outcomes | screen | Include symptom, diagnostic, functioning, relapse, and related outcomes at screening; no single outcome is required. |
| Eligible study designs | screen | No design restriction was specified and an ad hoc design block could reduce recall. |
| Age groups | screen | No age restriction was specified. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T00:22:25+00:00
- Records added to PubMed up to: 2017-08-24
- Total records: 8,541
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Anxiety Disorders[Mesh]` | 75,155 | none |
| 2 | `Phobic Disorders[Mesh]` | 12,282 | none |
| 3 | `Phobia, Social[Mesh]` | 388 | none |
| 4 | `Panic Disorder[Mesh]` | 6,597 | none |
| 5 | `Obsessive-Compulsive Disorder[Mesh]` | 14,139 | none |
| 6 | `Stress Disorders, Post-Traumatic[Mesh]` | 28,555 | none |
| 7 | `Anxiety, Separation[Mesh]` | 2,050 | none |
| 8 | `anxiety[tiab]` | 151,430 | none |
| 9 | `anxiety disorder*[tiab]` | 24,830 | none |
| 10 | `anxiety-related[tiab]` | 3,987 | none |
| 11 | `panic disorder*[tiab]` | 8,745 | none |
| 12 | `panic attack*[tiab]` | 3,419 | none |
| 13 | `agoraphobi*[tiab]` | 3,183 | none |
| 14 | `phobi*[tiab]` | 10,712 | none |
| 15 | `social anxi*[tiab]` | 4,818 | none |
| 16 | `social phobi*[tiab]` | 3,768 | none |
| 17 | `generalized anxiety[tiab]` | 5,844 | none |
| 18 | `generalised anxiety[tiab]` | 673 | none |
| 19 | `GAD[tiab]` | 7,728 | none |
| 20 | `obsessive-compulsive disorder*[tiab]` | 11,295 | none |
| 21 | `obsessive compulsive disorder*[tiab]` | 11,295 | none |
| 22 | `OCD[tiab]` | 7,878 | none |
| 23 | `post-traumatic stress disorder*[tiab]` | 8,583 | none |
| 24 | `posttraumatic stress disorder*[tiab]` | 14,806 | none |
| 25 | `PTSD[tiab]` | 18,640 | none |
| 26 | `separation anxiety[tiab]` | 1,365 | none |
| 27 | `Mutism[Mesh]` | 1,023 | none |
| 28 | `selective mutism[tiab]` | 179 | none |
| 29 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28` | 234,523 | none |
| 30 | `Cognitive Behavioral Therapy[Mesh]` | 24,064 | none |
| 31 | `Behavior Therapy[Mesh]` | 66,990 | none |
| 32 | `cognitive behavioral therap*[tiab]` | 7,078 | none |
| 33 | `cognitive behaviour therap*[tiab]` | 1,423 | none |
| 34 | `cognitive behavior therap*[tiab]` | 1,987 | none |
| 35 | `cognitive behavioural therap*[tiab]` | 3,048 | none |
| 36 | `CBT[tiab]` | 8,158 | none |
| 37 | `cognitive therap*[tiab]` | 2,812 | none |
| 38 | `behavior therap*[tiab]` | 4,378 | none |
| 39 | `behaviour therap*[tiab]` | 2,193 | none |
| 40 | `exposure therap*[tiab]` | 1,294 | none |
| 41 | `cognitive behavio*[tiab]` | 22,079 | none |
| 42 | `(exposure[tiab] AND response[tiab] AND prevention[tiab])` | 2,591 | none |
| 43 | `ERP[tiab]` | 13,251 | none |
| 44 | `cognitive processing therap*[tiab]` | 182 | none |
| 45 | `CPT[tiab]` | 10,989 | none |
| 46 | `((trauma-focused[tiab] OR "trauma focused"[tiab]) AND (CBT[tiab] OR (cognitive[tiab] AND behavio*[tiab] AND therap*[tiab])))` | 282 | none |
| 47 | `#30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46` | 105,727 | none |
| 48 | `Follow-Up Studies[Mesh]` | 594,219 | none |
| 49 | `Treatment Outcome[Mesh]` | 919,163 | none |
| 50 | `follow-up[tiab]` | 788,429 | none |
| 51 | `follow up[tiab]` | 788,429 | none |
| 52 | `followup[tiab]` | 751,136 | none |
| 53 | `long-term[tiab]` | 661,989 | none |
| 54 | `long term[tiab]` | 661,989 | none |
| 55 | `longitudinal[tiab]` | 194,058 | none |
| 56 | `maintenance[tiab]` | 234,429 | none |
| 57 | `durability[tiab]` | 14,752 | none |
| 58 | `sustain*[tiab]` | 277,245 | none |
| 59 | `persist*[tiab]` | 402,701 | none |
| 60 | `post-treatment[tiab]` | 30,453 | none |
| 61 | `posttreatment[tiab]` | 42,650 | none |
| 62 | `relapse[tiab]` | 100,555 | none |
| 63 | `remission[tiab]` | 100,780 | none |
| 64 | `#48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63` | 3,176,192 | none |
| 65 | `#29 AND #47 AND #64` | 8,541 | none |

### Strategy (single line, for copying into PubMed)

```text
((Anxiety Disorders[Mesh] OR Phobic Disorders[Mesh] OR Phobia, Social[Mesh] OR Panic Disorder[Mesh] OR Obsessive-Compulsive Disorder[Mesh] OR Stress Disorders, Post-Traumatic[Mesh] OR Anxiety, Separation[Mesh] OR anxiety[tiab] OR anxiety disorder*[tiab] OR anxiety-related[tiab] OR panic disorder*[tiab] OR panic attack*[tiab] OR agoraphobi*[tiab] OR phobi*[tiab] OR social anxi*[tiab] OR social phobi*[tiab] OR generalized anxiety[tiab] OR generalised anxiety[tiab] OR GAD[tiab] OR obsessive-compulsive disorder*[tiab] OR obsessive compulsive disorder*[tiab] OR OCD[tiab] OR post-traumatic stress disorder*[tiab] OR posttraumatic stress disorder*[tiab] OR PTSD[tiab] OR separation anxiety[tiab] OR Mutism[Mesh] OR selective mutism[tiab]) AND (Cognitive Behavioral Therapy[Mesh] OR Behavior Therapy[Mesh] OR cognitive behavioral therap*[tiab] OR cognitive behaviour therap*[tiab] OR cognitive behavior therap*[tiab] OR cognitive behavioural therap*[tiab] OR CBT[tiab] OR cognitive therap*[tiab] OR behavior therap*[tiab] OR behaviour therap*[tiab] OR exposure therap*[tiab] OR cognitive behavio*[tiab] OR (exposure[tiab] AND response[tiab] AND prevention[tiab]) OR ERP[tiab] OR cognitive processing therap*[tiab] OR CPT[tiab] OR ((trauma-focused[tiab] OR "trauma focused"[tiab]) AND (CBT[tiab] OR (cognitive[tiab] AND behavio*[tiab] AND therap*[tiab])))) AND (Follow-Up Studies[Mesh] OR Treatment Outcome[Mesh] OR follow-up[tiab] OR follow up[tiab] OR followup[tiab] OR long-term[tiab] OR long term[tiab] OR longitudinal[tiab] OR maintenance[tiab] OR durability[tiab] OR sustain*[tiab] OR persist*[tiab] OR post-treatment[tiab] OR posttreatment[tiab] OR relapse[tiab] OR remission[tiab])) AND ("1800/01/01"[edat] : "2017/08/24"[edat])
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
| Long-term follow-up or persistence of outcomes after CBT | AND-ed | 17,874 / 8,541 | 52.2% | none | 0/30 (up to 10% of removed records could be relevant) | Refreshed for the current base query after critic-requested condition and intervention additions. The block retrieves all 3 screened relevant publications, removes 9,333 records (52.2% of the base set), and no clearly eligible long-term CBT anxiety-disorder outcome appeared in the 30-record loss sample; sampled screening remains limited evidence. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Anxiety and anxiety-related disorders | 1 | `disorder*[tiab] OR psychiatric[tiab] OR Mental Disorders[Mesh]` | 27,866 | 0/30 |
| Anxiety and anxiety-related disorders | 2 | `disorder*[tiab] OR psychiatric[tiab] OR Mental Disorders[Mesh]` | 12,335 | 0/30 |
| Cognitive behavioral therapy and named CBT variants | 1 | `Psychotherapy[Mesh] OR psychotherap*[tiab] OR exposure-based[tiab] OR exposure[tiab]` | 25,971 | 0/30 |
| Cognitive behavioral therapy and named CBT variants | 2 | `Psychotherapy[Mesh] OR psychotherap*[tiab] OR exposure-based[tiab] OR exposure[tiab]` | 6,744 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| anxiety_disorders | 35,525 | 0 |
| cbt | 53,666 | 0 |
| long_term | 17,874 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 17,191 | initial | none | Initial two-block broad anxiety-disorder and CBT strategy; screened three relevant follow-up publications from a prior review's cited records. Long-term follow-up held as optional for measured testing. |
| 2 | 8,370 | long_term: +16 / -0 | none | After screening category probes and the optional loss sample, AND the long-term follow-up block based on a 51.3% reduction and no clearly eligible record in the 30-record loss sample. Remove a zero-hit generalized anxiety MeSH term; free-text variants and the Anxiety Disorders MeSH tree remain. |
| 3 | 8,370 | anxiety_disorders: +0 / -1 | none | Remove the zero-hit Generalized Anxiety Disorder MeSH line after inspecting its verified-heading translation and zero count; retain generalized/generalised anxiety text terms and Anxiety Disorders heading. Because the query changed, revalidate category probes and the optional decision. |
| 4 | 8,541 | anxiety_disorders: +2 / -0; cbt: +5 / -0 | none | Add Mutism[Mesh] and selective mutism[tiab] after critic identified this named anxiety-disorder member; add explicit ERP, cognitive processing therapy/CPT, and trauma-focused CBT expressions as eligible named CBT variants. Preserve the required Entrez-date cutoff per the user's instruction. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 3 findings; R1-01 must-fix open, R1-02 should-fix open, R1-03 must-fix open
- Round 2 on version 4: 4 findings; R1-01 must-fix resolved, R1-02 should-fix resolved, R1-03 must-fix rejected, R2-01 should-fix open
- Round 3 on version 4: 4 findings; R1-01 must-fix resolved, R1-02 should-fix resolved, R1-03 must-fix rejected, R2-01 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1058 NCBI requests logged (510 from cache); strategy sha256 8f890f249475._

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
        "location": "concept:anxiety_disorders",
        "blocking": false,
        "requires_review": true,
        "id": "I-8823674160ffd3b1ebe7"
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
        "location": "concept:anxiety_disorders",
        "blocking": false,
        "requires_review": true,
        "id": "I-8823674160ffd3b1ebe7"
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
      "checked_at": "2026-09-29T00:22:25+00:00",
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
      "checked_at": "2026-09-29T00:22:25+00:00",
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
      "requested": "Phobia, Social",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:22:25+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000072861",
          "name": "Phobia, Social",
          "type": "descriptor",
          "scope_note": "Anxiety disorder characterized by the persistent and irrational fear, anxiety, or avoidance of social or performance situations.",
          "tree_numbers": [
            "F03.080.725.500"
          ],
          "entry_terms": 14,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000072861",
      "preferred_label": "Phobia, Social",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "Phobia, Social",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Panic Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:22:25+00:00",
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
      "checked_at": "2026-09-29T00:22:25+00:00",
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
      "checked_at": "2026-09-29T00:22:25+00:00",
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
      "requested": "Anxiety, Separation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:22:25+00:00",
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
        "text": "Anxiety, Separation",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mutism",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:22:25+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D009155",
          "name": "Mutism",
          "type": "descriptor",
          "scope_note": "The inability to generate oral-verbal expression, despite normal comprehension of speech. This may be associated with BRAIN DISEASES or MENTAL DISORDERS. Organic mutism may be associated with damage to the FRONTAL LOBE; BRAIN STEM; THALAMUS; and CEREBELLUM. Selective mutism is a psychological condition that usually affects children characterized by continuous refusal to speak in social situatio...",
          "tree_numbers": [
            "C10.597.606.150.500.800.500",
            "C23.888.592.604.150.500.800.500",
            "F03.625.875"
          ],
          "entry_terms": 24,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D009155",
      "preferred_label": "Mutism",
      "type": "descriptor",
      "location": "vocabulary:27",
      "term": {
        "text": "Mutism",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognitive Behavioral Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:22:25+00:00",
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
      "location": "vocabulary:29",
      "term": {
        "text": "Cognitive Behavioral Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Behavior Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:22:25+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "Behavior Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Follow-Up Studies",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:22:25+00:00",
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
      "location": "vocabulary:53",
      "term": {
        "text": "Follow-Up Studies",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Treatment Outcome",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:22:25+00:00",
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
      "location": "vocabulary:54",
      "term": {
        "text": "Treatment Outcome",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"anxiety disorders\"[MeSH Terms] OR \"phobic disorders\"[MeSH Terms] OR \"phobia, social\"[MeSH Terms] OR \"panic disorder\"[MeSH Terms] OR \"obsessive compulsive disorder\"[MeSH Terms] OR \"stress disorders, post traumatic\"[MeSH Terms] OR \"anxiety, separation\"[MeSH Terms] OR \"anxiety\"[Title/Abstract] OR \"anxiety disorder*\"[Title/Abstract] OR \"anxiety-related\"[Title/Abstract] OR \"panic disorder*\"[Title/Abstract] OR \"panic attack*\"[Title/Abstract] OR \"agoraphobi*\"[Title/Abstract] OR \"phobi*\"[Title/Abstract] OR \"social anxi*\"[Title/Abstract] OR \"social phobi*\"[Title/Abstract] OR \"generalized anxiety\"[Title/Abstract] OR \"generalised anxiety\"[Title/Abstract] OR \"GAD\"[Title/Abstract] OR \"obsessive compulsive disorder*\"[Title/Abstract] OR \"obsessive compulsive disorder*\"[Title/Abstract] OR \"OCD\"[Title/Abstract] OR \"post traumatic stress disorder*\"[Title/Abstract] OR \"posttraumatic stress disorder*\"[Title/Abstract] OR \"PTSD\"[Title/Abstract] OR \"separation anxiety\"[Title/Abstract] OR \"mutism\"[MeSH Terms] OR \"selective mutism\"[Title/Abstract]) AND (\"cognitive behavioral therapy\"[MeSH Terms] OR \"behavior therapy\"[MeSH Terms] OR \"cognitive behavioral therap*\"[Title/Abstract] OR \"cognitive behaviour therap*\"[Title/Abstract] OR \"cognitive behavior therap*\"[Title/Abstract] OR \"cognitive behavioural therap*\"[Title/Abstract] OR \"CBT\"[Title/Abstract] OR \"cognitive therap*\"[Title/Abstract] OR \"behavior therap*\"[Title/Abstract] OR \"behaviour therap*\"[Title/Abstract] OR \"exposure therap*\"[Title/Abstract] OR \"cognitive behavio*\"[Title/Abstract] OR (\"exposure\"[Title/Abstract] AND \"response\"[Title/Abstract] AND \"prevention\"[Title/Abstract]) OR \"ERP\"[Title/Abstract] OR \"cognitive processing therap*\"[Title/Abstract] OR \"CPT\"[Title/Abstract] OR ((\"trauma-focused\"[Title/Abstract] OR \"trauma-focused\"[Title/Abstract]) AND (\"CBT\"[Title/Abstract] OR (\"cognitive\"[Title/Abstract] AND \"behavio*\"[Title/Abstract] AND \"therap*\"[Title/Abstract])))) AND (\"follow up studies\"[MeSH Terms] OR \"treatment outcome\"[MeSH Terms] OR \"follow-up\"[Title/Abstract] OR \"follow-up\"[Title/Abstract] OR \"followup\"[Title/Abstract] OR \"long-term\"[Title/Abstract] OR \"long-term\"[Title/Abstract] OR \"longitudinal\"[Title/Abstract] OR \"maintenance\"[Title/Abstract] OR \"durability\"[Title/Abstract] OR \"sustain*\"[Title/Abstract] OR \"persist*\"[Title/Abstract] OR \"post-treatment\"[Title/Abstract] OR \"posttreatment\"[Title/Abstract] OR \"relapse\"[Title/Abstract] OR \"remission\"[Title/Abstract]) AND 1800/01/01:2017/08/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "d932909ee99945fe0fa32ec5a4a984f6cf43989c9c822ed374c59dbb1c42d8f5",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The anxiety block does not include selective mutism by its own name, although the scope says individual member diagnoses must be searched. The intervention scope also includes clearly named CBT variants that are not represented explicitly in the text terms."
        },
        "operators": {
          "verdict": "pass",
          "note": "The concept blocks use OR within concepts and AND across required concepts. The optional long-term block has a documented retrieval comparison and loss sample; its rationale acknowledges that sampled screening does not prove complete recall."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "The anxiety block lacks a heading or text term for selective mutism. The listed headings otherwise translate as MeSH terms in the supplied diagnostics."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add explicit names and abbreviations for clearly named CBT variants relevant to the stated intervention scope, such as exposure and response prevention (ERP), cognitive processing therapy (CPT), and trauma-focused CBT. The category probes do not establish that these variants are covered."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The supplied query and term diagnostics report no syntax errors or PubMed warning list. The shown field tags and Boolean grouping are consistent."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The final query applies an Entrez date-entry range ending 2017-08-24. That excludes records entered after that date despite the stated absence of date limits; remove the cutoff from the final strategy or clearly treat it as a deliberate search cutoff."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The searched anxiety block omits selective mutism, a named anxiety-disorder member, despite the scope rationale requiring individual member diagnoses to be searched. The broad anxiety term may retrieve some records but does not ensure coverage by the diagnosis name.",
          "recommendation": "Add selective mutism[tiab] and the applicable MeSH heading if available; test the amended block and complete a new evaluation.",
          "status": "open"
        },
        {
          "id": "R1-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The intervention block does not explicitly search several clearly named CBT variants relevant to the stated eligibility, including exposure and response prevention (ERP), cognitive processing therapy (CPT), and trauma-focused CBT. The broad exposure and cognitive behavior terms do not establish coverage of each variant by its name.",
          "recommendation": "Add tested bare-name and abbreviation expressions for eligible named CBT variants, then rerun the complete evaluation.",
          "status": "open"
        },
        {
          "id": "R1-03",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query includes an Entrez date-entry range ending 2017-08-24, which excludes records entered after that date. This conflicts with the stated lack of date limits, even though the cutoff is described as a command setting rather than a publication-date limit.",
          "recommendation": "Remove the EDAT range from the final search strategy, or explicitly define and justify it as the intended search cutoff; rerun the complete evaluation after changing the query.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "b92be1e6ce5bf21138d42e6ce577b84da566cd2631841617a318aaf9169486af",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Selective mutism is now represented by its own text term and the Mutism MeSH heading. The named CBT variants raised in round 1 now have explicit terms: exposure and response prevention components and ERP, cognitive processing therapy and CPT, and trauma-focused CBT wording."
        },
        "operators": {
          "verdict": "revise",
          "note": "The OR-within-concepts and AND-across-required-concepts structure is coherent. However, the optional long-term block is still marked stale despite being AND-ed into the final query. Its loss sample and known-record retrieval are limited evidence; refresh and document the decision for the current strategy."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The anxiety block includes the Mutism MeSH heading alongside selective mutism text wording. The listed MeSH terms are translated in the supplied diagnostics without reported warnings or errors."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The round 1 CBT variant omissions have been addressed with explicit tested text terms. The diagnostics show no syntax errors or warning list for the displayed expressions."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query groups terms within concepts and combines the blocks with AND. Supplied final-query diagnostics report no warning list or error list."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The final query still applies an Entrez date-entry range ending 2017-08-24. This excludes records entered later, but the harness explicitly requires an Entrez-date cutoff through PSB_AS_OF for every command and the generated query. Retain and document this required operational cutoff."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The searched anxiety block omitted selective mutism by its own name.",
          "recommendation": "Add selective mutism[tiab] and the applicable MeSH heading if available; test the amended block and complete a new evaluation.",
          "status": "resolved",
          "response": "The current anxiety block includes selective mutism[tiab] and Mutism[Mesh]."
        },
        {
          "id": "R1-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The intervention block did not explicitly search several clearly named CBT variants, including exposure and response prevention, cognitive processing therapy, and trauma-focused CBT.",
          "recommendation": "Add tested bare-name and abbreviation expressions for eligible named CBT variants, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current block includes exposure/response/prevention terms and ERP, cognitive processing therap* and CPT, and trauma-focused CBT wording."
        },
        {
          "id": "R1-03",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query includes an Entrez date-entry range ending 2017-08-24, excluding records entered after that date despite the stated lack of date limits.",
          "recommendation": "Remove the EDAT range from the final strategy, or explicitly define and justify it as the intended search cutoff; rerun the complete evaluation after changing the query.",
          "status": "rejected",
          "response": "The user explicitly required the 2017-08-24 PubMed Entrez-date cutoff via PSB_AS_OF for every command. It is an intentional inclusion restriction to honor the harness, not an unrequested publication-date filter; no [dp] restriction is present."
        },
        {
          "id": "R2-01",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "The optional long-term block is AND-ed into the final query while its decision is explicitly marked stale. Its current evidence includes all 3 known relevant records and 0 relevant records in a 30-record loss sample, but the sample does not establish complete recall.",
          "recommendation": "Refresh and document the optional-block decision for the current strategy before treating the AND-ed block as settled.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-8823674160ffd3b1ebe7",
          "status": "accepted-risk",
          "response": "The anxiety category probe budget is spent and the probe is stale after adding terms. Accept as a documented coverage uncertainty; the search now explicitly adds selective mutism and its MeSH heading.",
          "evidence": "Two earlier probes screened 30 records each and found no relevant record outside the anxiety block. The new terms were added to cover the named selective-mutism member identified by the critic."
        },
        {
          "issue_id": "I-55bac4b0c1a86e93826e",
          "status": "accepted-risk",
          "response": "The CBT category probe budget is spent and the probe is stale after adding terms. Accept as a documented coverage uncertainty while retaining the newly added named variants.",
          "evidence": "Two earlier probes screened 30 records each and found no relevant record outside the CBT block. The current additions explicitly cover ERP, cognitive processing therapy/CPT, and trauma-focused CBT."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "4f2b00a91380a652aef172d780a69bc642235a62faea58735d69993ad78db380",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Selective mutism has its own text term and the Mutism MeSH heading. The named CBT variants raised earlier are represented by explicit terms for ERP, cognitive processing therapy/CPT, and trauma-focused CBT."
        },
        "operators": {
          "verdict": "pass",
          "note": "The required concept blocks are OR-combined internally and AND-combined. The optional long-term block was refreshed for the current query; its comparison retrieves all 3 screened relevant publications and the 30-record loss sample found 0 relevant records. This remains limited recall evidence."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The anxiety block includes the Mutism MeSH heading, and the supplied diagnostics report no heading translation errors."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The previously identified CBT variant gaps are addressed with tested text terms. Supplied diagnostics report no warning list for the displayed expressions."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query groups terms within concepts and combines the blocks as intended. Final-query diagnostics report no warning list or error list."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez date-entry cutoff through 2017-08-24 remains in the query as the required PSB_AS_OF operational cutoff. The packet specifies no publication-date restriction."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The anxiety block omitted selective mutism by its own name.",
          "recommendation": "Add selective mutism[tiab] and the applicable MeSH heading if available; test and reevaluate.",
          "status": "resolved",
          "response": "The current anxiety block includes selective mutism[tiab] and Mutism[Mesh]."
        },
        {
          "id": "R1-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The intervention block lacked explicit terms for named CBT variants including ERP, CPT, and trauma-focused CBT.",
          "recommendation": "Add tested bare-name and abbreviation expressions for eligible named CBT variants, then reevaluate.",
          "status": "resolved",
          "response": "The current block includes exposure/response/prevention terms and ERP, cognitive processing therap* and CPT, and trauma-focused CBT wording."
        },
        {
          "id": "R1-03",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query includes an Entrez date-entry range ending 2017-08-24.",
          "recommendation": "Remove the EDAT range or define and justify it as the intended cutoff.",
          "status": "rejected",
          "response": "The packet states that the user explicitly required the 2017-08-24 PubMed Entrez-date cutoff via PSB_AS_OF for every command and the generated query. It is an intentional operational cutoff, and no [dp] restriction is present."
        },
        {
          "id": "R2-01",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "The optional long-term block was AND-ed into the final query while its decision was marked stale.",
          "recommendation": "Refresh and document the optional-block decision for the current strategy.",
          "status": "resolved",
          "response": "The block was refreshed for the current base query. It retrieves all 3 screened relevant publications, removes 9,333 records, and the 30-record loss sample found 0 clearly eligible records; the packet documents that this sample is limited evidence."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-8823674160ffd3b1ebe7",
          "status": "accepted-risk",
          "response": "The anxiety category probe budget is spent and the probes are stale after adding terms. Retain this as a documented coverage uncertainty; the named selective-mutism member is now explicitly covered.",
          "evidence": "Two earlier probes screened 30 records each and found no relevant records outside the anxiety block. The current block adds selective mutism[tiab] and Mutism[Mesh]."
        },
        {
          "issue_id": "I-55bac4b0c1a86e93826e",
          "status": "accepted-risk",
          "response": "The CBT category probe budget is spent and the probes are stale after adding terms. Retain this as a documented coverage uncertainty while keeping the explicit named-variant terms.",
          "evidence": "Two earlier probes screened 30 records each and found no relevant records outside the CBT block. The current additions explicitly cover ERP, cognitive processing therapy/CPT, and trauma-focused CBT."
        }
      ]
    }
  ]
}
```

