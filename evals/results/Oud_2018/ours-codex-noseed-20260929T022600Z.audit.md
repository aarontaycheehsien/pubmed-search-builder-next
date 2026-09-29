# PubMed search strategy: audit

Generated 2026-09-29T02:44:17+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Specialized psychotherapies for adults with borderline personality disorder
- Framework: PICO (intervention effectiveness; comparator and outcomes screened)
- Scope confirmed by user: yes (User requested no questions and authorized reasonable assumptions. No known relevant articles were supplied. Assumed the review concerns identifiable specialist psychotherapy approaches for adults with borderline personality disorder; 'specialized' has no single reliable indexing label and will be decided at screening. Adults are a screening criterion, not an AND block, to avoid age-indexing loss. Comparator and outcomes are screened. No language, publication-date, age, or study-design filter. PubMed is bounded by Entrez date 2015-03-27 through PSB_AS_OF on every command; no publication-date limit is applied. Standard depth; recall will be unvalidated absent screened known studies.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Borderline personality disorder | search | Condition defines the population and is reliably named/indexed; age is screened because age labels are inconsistently searchable. |
| Psychotherapy and named psychotherapy modalities | search | Intervention is essential to the question. Include general psychotherapy terms and named modality members because eligible records may name a modality without the category term. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T02:43:43+00:00
- Records added to PubMed up to: 2015-03-27
- Total records: 1,967
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Borderline Personality Disorder[Mesh]` | 5,413 | none |
| 2 | `borderline personality disorder*[tiab]` | 4,397 | none |
| 3 | `(borderline[tiab] AND personality[tiab])` | 5,910 | none |
| 4 | `emotionally unstable personality disorder*[tiab]` | 24 | none |
| 5 | `emotionally unstable personality[tiab]` | 30 | none |
| 6 | `(BPD[tiab] AND (personality[tiab] OR borderline[tiab]))` | 2,103 | none |
| 7 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6` | 7,494 | none |
| 8 | `Psychotherapy[Mesh]` | 165,482 | none |
| 9 | `Psychotherapy, Psychodynamic[Mesh]` | 210 | none |
| 10 | `Cognitive Behavioral Therapy[Mesh]` | 18,757 | none |
| 11 | `Behavior Therapy[Mesh]` | 57,482 | none |
| 12 | `dialectical behavior therap*[tiab]` | 278 | none |
| 13 | `dialectical behavioural therap*[tiab]` | 18 | none |
| 14 | `DBT[tiab]` | 1,420 | none |
| 15 | `mentalization-based treatment[tiab]` | 40 | none |
| 16 | `mentalisation-based treatment[tiab]` | 8 | none |
| 17 | `mentalization based treatment[tiab]` | 40 | none |
| 18 | `mentalisation based treatment[tiab]` | 8 | none |
| 19 | `"transference-focused psychotherapy"[tiab]` | 46 | none |
| 20 | `"transference focused psychotherapy"[tiab]` | 46 | none |
| 21 | `"transference-focused therapy"[tiab]` | 3 | none |
| 22 | `"schema therapy"[tiab]` | 76 | none |
| 23 | `"schema-focused therapy"[tiab]` | 32 | none |
| 24 | `STEPPS[tiab]` | 30 | none |
| 25 | `"Systems Training for Emotional Predictability and Problem Solving"[tiab]` | 16 | none |
| 26 | `psychotherap*[tiab]` | 37,596 | none |
| 27 | `psychological treatment*[tiab]` | 2,598 | none |
| 28 | `talk therap*[tiab]` | 41 | none |
| 29 | `#8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28` | 176,373 | none |
| 30 | `#7 AND #29` | 1,967 | none |

### Strategy (single line, for copying into PubMed)

```text
((Borderline Personality Disorder[Mesh] OR borderline personality disorder*[tiab] OR (borderline[tiab] AND personality[tiab]) OR emotionally unstable personality disorder*[tiab] OR emotionally unstable personality[tiab] OR (BPD[tiab] AND (personality[tiab] OR borderline[tiab]))) AND (Psychotherapy[Mesh] OR Psychotherapy, Psychodynamic[Mesh] OR Cognitive Behavioral Therapy[Mesh] OR Behavior Therapy[Mesh] OR dialectical behavior therap*[tiab] OR dialectical behavioural therap*[tiab] OR DBT[tiab] OR mentalization-based treatment[tiab] OR mentalisation-based treatment[tiab] OR mentalization based treatment[tiab] OR mentalisation based treatment[tiab] OR "transference-focused psychotherapy"[tiab] OR "transference focused psychotherapy"[tiab] OR "transference-focused therapy"[tiab] OR "schema therapy"[tiab] OR "schema-focused therapy"[tiab] OR STEPPS[tiab] OR "Systems Training for Emotional Predictability and Problem Solving"[tiab] OR psychotherap*[tiab] OR psychological treatment*[tiab] OR talk therap*[tiab])) AND ("1800/01/01"[edat] : "2015/03/27"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 23 | 23 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Psychotherapy and named psychotherapy modalities | 1 | `treatment*[tiab] OR therap*[tiab] OR intervention*[tiab] OR psychosocial[tiab]` | 3,056 | 0/30 |
| Psychotherapy and named psychotherapy modalities | 2 | `treatment*[tiab] OR therap*[tiab] OR intervention*[tiab] OR psychosocial[tiab]` | 1,658 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| bpd | 176,373 | 0 |
| psychotherapy | 7,494 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,874 | initial | none | Initial broad condition plus psychotherapy strategy, including named specialist modality members and MeSH/text layers; age and specialization screened to protect recall. |
| 2 | 1,874 | limits/combination | none | Removed duplicate psychotherap* term after the previous attempt showed no intended retrieval effect. |
| 3 | 1,967 | bpd: +2 / -2 | none | Addressed internal critic R1-01 by replacing proximity with tested explicit title/abstract co-occurrence of borderline and personality (count 5,910 for the clause, before the other condition OR terms). Addressed R1-02 by qualifying BPD with personality or borderline context to reduce acronym collisions. Full evaluation checks retrieval of all 23 screened development records and reports line/final counts. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 2 findings; R1-01 should-fix resolved, R1-02 should-fix resolved
- Round 2 on version 3: 3 findings; R1-01 should-fix resolved, R1-02 should-fix resolved, R2-01 should-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 462 NCBI requests logged (227 from cache); strategy sha256 e493c3fc4a6f._

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
      "requested": "Borderline Personality Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:43:43+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001883",
          "name": "Borderline Personality Disorder",
          "type": "descriptor",
          "scope_note": "A personality disorder marked by a pattern of instability of interpersonal relationships, self-image, and affects, and marked impulsivity beginning by early adulthood and present in a variety of contexts. (DSM-IV)",
          "tree_numbers": [
            "F03.675.100"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001883",
      "preferred_label": "Borderline Personality Disorder",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "Borderline Personality Disorder",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychotherapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:43:43+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011613",
          "name": "Psychotherapy",
          "type": "descriptor",
          "scope_note": "A generic term for the treatment of mental illness or emotional disturbances primarily by verbal or nonverbal communication.",
          "tree_numbers": [
            "F04.754"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011613",
      "preferred_label": "Psychotherapy",
      "type": "descriptor",
      "location": "vocabulary:10",
      "term": {
        "text": "Psychotherapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychotherapy, Psychodynamic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:43:43+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D064889",
          "name": "Psychotherapy, Psychodynamic",
          "type": "descriptor",
          "scope_note": "Forms of PSYCHOTHERAPY falling within or deriving from the psychoanalytic tradition, that view individuals as reacting to unconscious forces (e.g., motivation, drive), that focus on processes of change and development, and that place a premium on self understanding and making meaning of what is unconscious.",
          "tree_numbers": [
            "F04.754.775"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D064889",
      "preferred_label": "Psychotherapy, Psychodynamic",
      "type": "descriptor",
      "location": "vocabulary:11",
      "term": {
        "text": "Psychotherapy, Psychodynamic",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognitive Behavioral Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:43:43+00:00",
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
      "location": "vocabulary:12",
      "term": {
        "text": "Cognitive Behavioral Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Behavior Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:43:43+00:00",
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
      "location": "vocabulary:13",
      "term": {
        "text": "Behavior Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"borderline personality disorder\"[MeSH Terms] OR \"borderline personality disorder*\"[Title/Abstract] OR (\"borderline\"[Title/Abstract] AND \"personality\"[Title/Abstract]) OR \"emotionally unstable personality disorder*\"[Title/Abstract] OR \"emotionally unstable personality\"[Title/Abstract] OR (\"BPD\"[Title/Abstract] AND (\"personality\"[Title/Abstract] OR \"borderline\"[Title/Abstract]))) AND (\"psychotherapy\"[MeSH Terms] OR \"psychotherapy, psychodynamic\"[MeSH Terms] OR \"cognitive behavioral therapy\"[MeSH Terms] OR \"behavior therapy\"[MeSH Terms] OR \"dialectical behavior therap*\"[Title/Abstract] OR \"dialectical behavioural therap*\"[Title/Abstract] OR \"DBT\"[Title/Abstract] OR \"mentalization based treatment\"[Title/Abstract] OR \"mentalisation based treatment\"[Title/Abstract] OR \"mentalization based treatment\"[Title/Abstract] OR \"mentalisation based treatment\"[Title/Abstract] OR \"transference-focused psychotherapy\"[Title/Abstract] OR \"transference-focused psychotherapy\"[Title/Abstract] OR \"transference-focused therapy\"[Title/Abstract] OR \"schema therapy\"[Title/Abstract] OR \"schema-focused therapy\"[Title/Abstract] OR \"STEPPS\"[Title/Abstract] OR \"Systems Training for Emotional Predictability and Problem Solving\"[Title/Abstract] OR \"psychotherap*\"[Title/Abstract] OR \"psychological treatment*\"[Title/Abstract] OR \"talk therap*\"[Title/Abstract]) AND 1800/01/01:2015/03/27[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "ac4fdad32d03821bd518716826fa62e5a128c7f0205dd28e528c4582f94b11d7",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The proximity expression was replaced by explicit word co-occurrence after testing."
        },
        "operators": {
          "verdict": "pass",
          "note": "The blocks use OR internally and AND across condition and intervention."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet's MeSH terms were verified and appropriate."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The BPD acronym's incremental contribution was tested; unqualified acronym results were screened."
        },
        "syntax": {
          "verdict": "revise",
          "note": "The proximity clause was replaced with explicit tagged title/abstract co-occurrence."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age, language, publication-date, or study-design filters are applied; Entrez-date cutoff is explicit."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "syntax",
          "finding": "The condition block uses proximity but its interpretation was not documented or tested.",
          "recommendation": "Document the proximity interpretation and test alternatives or replace it, then evaluate.",
          "status": "resolved",
          "response": "Replaced the proximity term with (borderline[tiab] AND personality[tiab]), an explicit co-occurrence expression. PubMed returned 5,910 for that clause through the pinned Entrez date. The current evaluation has no phrase or syntax issues and retrieves all 23/23 screened relevant development records."
        },
        {
          "id": "R1-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The BPD acronym was ambiguous and its incremental contribution was not quantified.",
          "recommendation": "Measure its contribution and screen incremental results before deciding whether to retain it.",
          "status": "resolved",
          "response": "Compared the full query with and without unqualified BPD[tiab]: the base query returned 1,967 records and adding the unqualified acronym returned 1,985, an increment of 18. Screened all 18 incremental records by title and abstract; none was an eligible adult BPD psychotherapy study (they concerned bipolar disorder, body perception disturbance, or unrelated topics). The strategy retains only context-qualified BPD[tiab] with personality or borderline, and evaluation retains all 23/23 development records."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "02b737bc6612a2770d2a2b2eb52ee9175a04d3dd7b1a120c0058ecbd69e4efdc",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched blocks match the condition and intervention; named modalities have free-text coverage."
        },
        "operators": {
          "verdict": "pass",
          "note": "Alternatives are ORed within each concept and the concepts are ANDed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "MeSH headings are verified and broadly appropriate; free-text terms cover named specialist modalities."
        },
        "text_words": {
          "verdict": "pass",
          "note": "General and modality-specific text words are included; unqualified BPD was measured and screened out."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query has no translation or syntax issues. The second category probe used the current explicit condition block; its recorded query is included in the packet's complete evidence."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age, language, publication-date, or design filters are used; the Entrez-date cutoff is documented."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "syntax",
          "finding": "The condition block uses proximity but its interpretation was not documented or tested.",
          "recommendation": "Document the proximity interpretation and test alternatives or replace it, then evaluate.",
          "status": "resolved",
          "response": "Replaced proximity with the explicit `(borderline[tiab] AND personality[tiab])` condition expression. The current query has no phrase/syntax issues and retrieves all 23 screened development records."
        },
        {
          "id": "R1-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The BPD acronym was ambiguous and its incremental contribution was not quantified.",
          "recommendation": "Measure its contribution and screen incremental results before deciding whether to retain it.",
          "status": "resolved",
          "response": "Unqualified BPD added 18 records (1,985 versus 1,967); all 18 were screened by title and abstract and none was eligible. The strategy keeps only context-qualified BPD and retains all 23 development records."
        },
        {
          "id": "R2-01",
          "domain": "syntax",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "Both category probes use the obsolete proximity clause, so the current condition block has not been probed.",
          "recommendation": "Rerun or verify the category probes using the current condition block, then record probe results and complete evaluation.",
          "status": "rejected",
          "response": "The packet's complete evidence shows probe 1 used the earlier proximity clause, but probe 2 was drawn after the strategy revision and its stored query explicitly contains `(borderline[tiab] AND personality[tiab])` and the context-qualified BPD term. Probe 2 is the required current-block probe; its 30-record sample was screened by title and abstract and found 0 relevant records. The evaluation reports the category as clean. The finding's claim that both probes used the obsolete clause is contradicted by the packet evidence."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

