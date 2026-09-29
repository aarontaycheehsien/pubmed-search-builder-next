# PubMed search strategy: audit

Generated 2026-09-28T23:25:05+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Specialized psychotherapies for adults with borderline personality disorder
- Framework: PICO
- Scope confirmed by user: yes (User asked to proceed without questions; scope and defaults are assumed. Interpret specialized psychotherapy as a structured, named, or specifically adapted psychological treatment for BPD; comparator and outcomes are unrestricted. No known relevant articles supplied. Work as of 2015-03-27 using PSB_AS_OF Entrez cutoff; do not impose a publication-date limit. No language, age, or study-design search limits. Recall cannot be measured without known relevant records.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Borderline personality disorder | search | Target condition; diagnosis is central and reliably named/indexed. |
| Psychotherapy interventions | search | Intervention concept is essential; relevant studies may name a specific therapy rather than the general category, so build from named modalities and probe. |
| Adults | screen | Age is inconsistently indexed and age filters risk losing mixed-age studies; screen eligibility from records/full text. |
| Specialized therapy status | screen | Specialization/manualization is a clinical eligibility judgment that cannot be searched consistently. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T23:24:00+00:00
- Records added to PubMed up to: 2015-03-27
- Total records: 5,065
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Borderline Personality Disorder[Mesh]` | 5,413 | none |
| 2 | `borderline personality disorder[tiab]` | 4,215 | none |
| 3 | `borderline personality disorders[tiab]` | 271 | none |
| 4 | `borderline personality[tiab]` | 4,863 | none |
| 5 | `borderline personality pathology[tiab]` | 35 | none |
| 6 | `emotionally unstable personality disorder[tiab]` | 24 | none |
| 7 | `emotionally unstable personality[tiab]` | 30 | none |
| 8 | `BPD[tiab]` | 6,222 | none |
| 9 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8` | 10,827 | none |
| 10 | `Psychotherapy[Mesh]` | 165,482 | none |
| 11 | `Psychotherapy, Group[Mesh]` | 24,106 | none |
| 12 | `Behavior Therapy[Mesh]` | 57,482 | none |
| 13 | `Cognitive Behavioral Therapy[Mesh]` | 18,757 | none |
| 14 | `Psychoanalytic Therapy[Mesh]` | 15,004 | none |
| 15 | `Psychotherapy, Psychodynamic[Mesh]` | 210 | none |
| 16 | `psychotherap*[tiab]` | 37,596 | none |
| 17 | `psychological therap*[tiab]` | 1,199 | none |
| 18 | `psychological treatment*[tiab]` | 2,598 | none |
| 19 | `therapy[tiab]` | 1,438,128 | none |
| 20 | `therap*[tiab]` | 2,101,526 | none |
| 21 | `treatment[tiab]` | 3,150,610 | none |
| 22 | `treat*[tiab]` | 4,027,758 | none |
| 23 | `intervention*[tiab]` | 609,652 | none |
| 24 | `cognitive therap*[tiab]` | 2,237 | none |
| 25 | `behavior therap*[tiab]` | 3,612 | none |
| 26 | `behaviour therap*[tiab]` | 1,833 | none |
| 27 | `dialectical behavior therap*[tiab]` | 278 | none |
| 28 | `dialectical behaviour therap*[tiab]` | 84 | none |
| 29 | `DBT[tiab]` | 1,420 | none |
| 30 | `mentalization based therap*[tiab]` | 17 | none |
| 31 | `mentalisation based therap*[tiab]` | 5 | none |
| 32 | `mentalization-based therap*[tiab]` | 17 | none |
| 33 | `mentalisation-based therap*[tiab]` | 5 | none |
| 34 | `transference focused psychotherap*[tiab]` | 46 | none |
| 35 | `transference-focused psychotherap*[tiab]` | 46 | none |
| 36 | `schema focused therap*[tiab]` | 32 | none |
| 37 | `schema-focused therap*[tiab]` | 32 | none |
| 38 | `schema therap*[tiab]` | 76 | none |
| 39 | `"Systems Training for Emotional Predictability and Problem Solving"[tiab]` | 16 | none |
| 40 | `STEPPS[tiab]` | 30 | none |
| 41 | `dynamic deconstructive psychotherap*[tiab]` | 13 | none |
| 42 | `DDP[tiab]` | 2,490 | none |
| 43 | `cognitive analytic therap*[tiab]` | 57 | none |
| 44 | `cognitive-analytic therap*[tiab]` | 57 | none |
| 45 | `manual assisted cognitive therap*[tiab]` | 4 | none |
| 46 | `emotion regulation group therap*[tiab]` | 7 | none |
| 47 | `general psychiatric management[tiab]` | 14 | none |
| 48 | `good psychiatric management[tiab]` | 1 | none |
| 49 | `structured clinical management[tiab]` | 4 | none |
| 50 | `supportive psychotherap*[tiab]` | 471 | none |
| 51 | `interpersonal psychotherap*[tiab]` | 655 | none |
| 52 | `MBT[tiab]` | 1,537 | none |
| 53 | `TFP[tiab]` | 1,103 | none |
| 54 | `#10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53` | 5,490,645 | none |
| 55 | `#9 AND #54` | 5,065 | none |

### Strategy (single line, for copying into PubMed)

```text
((Borderline Personality Disorder[Mesh] OR borderline personality disorder[tiab] OR borderline personality disorders[tiab] OR borderline personality[tiab] OR borderline personality pathology[tiab] OR emotionally unstable personality disorder[tiab] OR emotionally unstable personality[tiab] OR BPD[tiab]) AND (Psychotherapy[Mesh] OR Psychotherapy, Group[Mesh] OR Behavior Therapy[Mesh] OR Cognitive Behavioral Therapy[Mesh] OR Psychoanalytic Therapy[Mesh] OR Psychotherapy, Psychodynamic[Mesh] OR psychotherap*[tiab] OR psychological therap*[tiab] OR psychological treatment*[tiab] OR therapy[tiab] OR therap*[tiab] OR treatment[tiab] OR treat*[tiab] OR intervention*[tiab] OR cognitive therap*[tiab] OR behavior therap*[tiab] OR behaviour therap*[tiab] OR dialectical behavior therap*[tiab] OR dialectical behaviour therap*[tiab] OR DBT[tiab] OR mentalization based therap*[tiab] OR mentalisation based therap*[tiab] OR mentalization-based therap*[tiab] OR mentalisation-based therap*[tiab] OR transference focused psychotherap*[tiab] OR transference-focused psychotherap*[tiab] OR schema focused therap*[tiab] OR schema-focused therap*[tiab] OR schema therap*[tiab] OR "Systems Training for Emotional Predictability and Problem Solving"[tiab] OR STEPPS[tiab] OR dynamic deconstructive psychotherap*[tiab] OR DDP[tiab] OR cognitive analytic therap*[tiab] OR cognitive-analytic therap*[tiab] OR manual assisted cognitive therap*[tiab] OR emotion regulation group therap*[tiab] OR general psychiatric management[tiab] OR good psychiatric management[tiab] OR structured clinical management[tiab] OR supportive psychotherap*[tiab] OR interpersonal psychotherap*[tiab] OR MBT[tiab] OR TFP[tiab])) AND ("1800/01/01"[edat] : "2015/03/27"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 0 | 0 | n/a |
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 23 | 23 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Psychotherapy interventions | 1 | `(therap*[tiab] OR treatment*[tiab] OR intervention*[tiab] OR management[tiab] OR psychotherapy[tiab] OR Psychotherapy[Mesh])` | 617 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| bpd | 5,490,645 | 0 |
| psychotherapy | 10,827 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial recall-first two-block strategy from scope, MeSH lookup, title/abstract review of 23 cited BPD psychotherapy treatment reports, and mined development terms. Broad psychotherapy and treatment wording retained to maximize recall; adult age and specialization remain screening criteria. |
| 2 | 4,356 | psychotherapy: +1 / -1 | none | Quoted the full Systems Training for Emotional Predictability and Problem Solving phrase after lint parsed its internal word 'and' as a Boolean operator; no scope changes. |
| 3 | 5,065 | psychotherapy: +3 / -0 | none | Expanded generic intervention morphology with therap*, treat*, and intervention* title/abstract stems after a cutoff-bound core query returned 5,016 records, within the 10,000-record budget. Known records remain retained. |
| 4 | 5,065 | psychotherapy: +2 / -0 | none | Resolved critic finding R1-F1 by adding MBT[tiab] and TFP[tiab] to cover common modality abbreviations. These acronyms can be ambiguous, but the required BPD block provides context; evaluation checks newly retrieved records and count. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 1 findings; R1-F1 should-fix open
- Round 2 on version 4: 1 findings; R1-F1 should-fix resolved
- Round 3 on version 4: 1 findings; R1-F1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 645 NCBI requests logged (333 from cache); strategy sha256 9ac424fc1541._

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
      "checked_at": "2026-09-28T23:24:00+00:00",
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
      "checked_at": "2026-09-28T23:24:00+00:00",
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
      "location": "vocabulary:9",
      "term": {
        "text": "Psychotherapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychotherapy, Group",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:24:00+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011615",
          "name": "Psychotherapy, Group",
          "type": "descriptor",
          "scope_note": "A form of therapy in which two or more patients participate under the guidance of one or more psychotherapists for the purpose of treating emotional disturbances, social maladjustments, and psychotic states.",
          "tree_numbers": [
            "F04.754.864.581"
          ],
          "entry_terms": 18,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011615",
      "preferred_label": "Psychotherapy, Group",
      "type": "descriptor",
      "location": "vocabulary:10",
      "term": {
        "text": "Psychotherapy, Group",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Behavior Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:24:00+00:00",
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
      "location": "vocabulary:11",
      "term": {
        "text": "Behavior Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognitive Behavioral Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:24:00+00:00",
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
      "requested": "Psychoanalytic Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:24:00+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011575",
          "name": "Psychoanalytic Therapy",
          "type": "descriptor",
          "scope_note": "A form of psychiatric treatment, based on Freudian principles, which seeks to eliminate or diminish the undesirable effects of unconscious conflicts by making the patient aware of their existence, origin, and inappropriate expression in current emotions and behavior.",
          "tree_numbers": [
            "F04.754.709"
          ],
          "entry_terms": 10,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011575",
      "preferred_label": "Psychoanalytic Therapy",
      "type": "descriptor",
      "location": "vocabulary:13",
      "term": {
        "text": "Psychoanalytic Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychotherapy, Psychodynamic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:24:00+00:00",
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
      "location": "vocabulary:14",
      "term": {
        "text": "Psychotherapy, Psychodynamic",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"borderline personality disorder\"[MeSH Terms] OR \"borderline personality disorder\"[Title/Abstract] OR \"borderline personality disorders\"[Title/Abstract] OR \"borderline personality\"[Title/Abstract] OR \"borderline personality pathology\"[Title/Abstract] OR \"emotionally unstable personality disorder\"[Title/Abstract] OR \"emotionally unstable personality\"[Title/Abstract] OR \"BPD\"[Title/Abstract]) AND (\"psychotherapy\"[MeSH Terms] OR \"psychotherapy, group\"[MeSH Terms] OR \"behavior therapy\"[MeSH Terms] OR \"cognitive behavioral therapy\"[MeSH Terms] OR \"psychoanalytic therapy\"[MeSH Terms] OR \"psychotherapy, psychodynamic\"[MeSH Terms] OR \"psychotherap*\"[Title/Abstract] OR \"psychological therap*\"[Title/Abstract] OR \"psychological treatment*\"[Title/Abstract] OR \"therapy\"[Title/Abstract] OR \"therap*\"[Title/Abstract] OR \"treatment\"[Title/Abstract] OR \"treat*\"[Title/Abstract] OR \"intervention*\"[Title/Abstract] OR \"cognitive therap*\"[Title/Abstract] OR \"behavior therap*\"[Title/Abstract] OR \"behaviour therap*\"[Title/Abstract] OR \"dialectical behavior therap*\"[Title/Abstract] OR \"dialectical behaviour therap*\"[Title/Abstract] OR \"DBT\"[Title/Abstract] OR \"mentalization based therap*\"[Title/Abstract] OR \"mentalisation based therap*\"[Title/Abstract] OR \"mentalization based therap*\"[Title/Abstract] OR \"mentalisation based therap*\"[Title/Abstract] OR \"transference focused psychotherap*\"[Title/Abstract] OR \"transference focused psychotherap*\"[Title/Abstract] OR \"schema focused therap*\"[Title/Abstract] OR \"schema focused therap*\"[Title/Abstract] OR \"schema therap*\"[Title/Abstract] OR \"Systems Training for Emotional Predictability and Problem Solving\"[Title/Abstract] OR \"STEPPS\"[Title/Abstract] OR \"dynamic deconstructive psychotherap*\"[Title/Abstract] OR \"DDP\"[Title/Abstract] OR \"cognitive analytic therap*\"[Title/Abstract] OR \"cognitive analytic therap*\"[Title/Abstract] OR \"manual assisted cognitive therap*\"[Title/Abstract] OR \"emotion regulation group therap*\"[Title/Abstract] OR \"general psychiatric management\"[Title/Abstract] OR \"good psychiatric management\"[Title/Abstract] OR \"structured clinical management\"[Title/Abstract] OR \"supportive psychotherap*\"[Title/Abstract] OR \"interpersonal psychotherap*\"[Title/Abstract] OR \"MBT\"[Title/Abstract] OR \"TFP\"[Title/Abstract]) AND 1800/01/01:2015/03/27[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "7483f690b6eda7f75ef4267a625885d3699001c02ddf727d139f80a34f5f4a61",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The reported translation issues are empty, and the displayed translations preserve the intended MeSH and title/abstract fields."
        },
        "operators": {
          "verdict": "pass",
          "note": "The strategy combines the condition and intervention blocks with AND and combines terms within each block with OR. No proximity operators require review."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The included MeSH headings are reported as verified and appear in the translated query."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The named-modality list includes full names for mentalization-based therapy and transference-focused psychotherapy but omits their common abbreviations MBT and TFP. Add acronym variants or document why they are unnecessary; the broad intervention terms do not ensure retrieval when a record uses only an abbreviation."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed final query has balanced grouping, valid Boolean structure, and no reported PubMed syntax errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age, language, or study-design limits are applied, consistent with the stated screening approach. The entry-date cutoff is documented as the as-of date."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The psychotherapy block includes full-name variants for mentalization-based therapy and transference-focused psychotherapy but not the common abbreviations MBT and TFP. A record using an abbreviation without spelling out the name may not match the intervention block.",
          "recommendation": "Add MBT[tiab] and TFP[tiab], then rerun the complete evaluation and inspect any newly retrieved records for relevance and acronym ambiguity.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "e8e40c6e3d9abc7b0a1ec3206d8b3ff82f80ce074e567deda53806db1f57d792",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The reported translation issues are empty. The displayed translation preserves the MeSH and title/abstract fields; hyphenated variants normalize to equivalent forms."
        },
        "operators": {
          "verdict": "pass",
          "note": "The condition and intervention blocks are combined with AND, and terms within each block are combined with OR. No proximity operators require review."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed MeSH headings are reported as verified and appear in the final query."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The current intervention block includes MBT[tiab] and TFP[tiab], addressing the earlier omission. The broad intervention terms and named modalities are consistent with the stated search scope; the category probe found no relevant records outside the block."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query has balanced grouping and valid Boolean structure, with no reported PubMed syntax errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age, language, or study-design limits are applied, consistent with the screening plan. The entry-date cutoff is documented as the as-of date."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier draft omitted the common abbreviations MBT and TFP from the psychotherapy block.",
          "recommendation": "Add MBT[tiab] and TFP[tiab], then rerun the complete evaluation and inspect newly retrieved records for relevance and acronym ambiguity.",
          "status": "resolved",
          "response": "Resolved in version 4: MBT[tiab] and TFP[tiab] are included in the current intervention block and final query."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "e8e40c6e3d9abc7b0a1ec3206d8b3ff82f80ce074e567deda53806db1f57d792",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The reported translation issues are empty. MeSH terms translate to MeSH Terms and title/abstract terms retain their intended fields."
        },
        "operators": {
          "verdict": "pass",
          "note": "The condition and intervention blocks are combined with AND, and terms within each block with OR. No proximity operators require interpretation."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed MeSH headings appear in the translated query; no heading-related issues are reported."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The current intervention block includes MBT[tiab] and TFP[tiab], handling the earlier omission. The current evaluation reports all 23 known relevant records retrieved and no relevant records among 30 screened from the intervention category probe."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed query has balanced grouping and valid Boolean structure, with no reported syntax errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age, language, or study-design search limits are applied, consistent with the stated screening plan. The entry-date cutoff is documented as the as-of date."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier draft omitted the common abbreviations MBT and TFP from the psychotherapy block.",
          "recommendation": "Add MBT[tiab] and TFP[tiab], then rerun the complete evaluation and inspect newly retrieved records for relevance and acronym ambiguity.",
          "status": "resolved",
          "response": "Resolved in version 4: MBT[tiab] and TFP[tiab] are present in the current intervention block and final query. The current evaluation is complete and reports all 23 known relevant records retrieved."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

