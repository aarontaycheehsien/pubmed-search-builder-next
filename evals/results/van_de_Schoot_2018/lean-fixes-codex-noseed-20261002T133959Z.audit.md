# PubMed search strategy: audit

Generated 2026-10-02T13:58:40+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Post-traumatic stress disorder symptom trajectories after a traumatic event
- Framework: prognosis / longitudinal symptom course
- Scope confirmed by user: no (User asked not to pause for questions. Scope assumption: PTSD symptoms are the sole searched concept; traumatic-event context and longitudinal trajectory/course are screened. No language, age, publication-date, or study-design search limits. PSB_AS_OF=2016-01-24 applies the PubMed entry-date cutoff; no [dp] limit. MeSH review: the PTSD descriptor has no narrower headings; the acute traumatic stress descriptor was added to capture immediate post-event symptoms. Critic round 1 removed standalone moral-injury text terms after term-only sampling showed unrelated uses; it also consolidated hyphenation variants that PubMed translated identically. The closed posttraumatic form remains. Critic round 2: added explicit post-traumatic/posttraumatic symptom singular and plural phrases, after a focused pilot showed these labels can appear without PTSD/stress in phrasing. PMID 25585484 was screened in and added to the development set.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Post-traumatic stress disorder symptoms | search | The condition and symptom domain define the topic and are named in titles, abstracts, and MeSH. |
| Traumatic event exposure | screen | Context is part of eligibility, but event wording varies and is not needed to identify PTSD symptom-course studies. |
| Longitudinal symptom trajectories or course | screen | The outcome/method is inconsistently labeled; requiring trajectory terminology risks missing longitudinal studies using course, change, persistence, or other descriptions. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T13:58:25+00:00
- Records added to PubMed up to: 2016-01-24
- Total records: 56,663
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Stress Disorders, Post-Traumatic"[Mesh]` | 25,369 | none |
| 2 | `"Stress Disorders, Traumatic, Acute"[Mesh]` | 387 | none |
| 3 | `PTSD[tiab]` | 15,732 | none |
| 4 | `"post-traumatic stress"[tiab]` | 8,160 | none |
| 5 | `posttraumatic stress[tiab]` | 14,174 | none |
| 6 | `posttraumatic[tiab]` | 46,488 | none |
| 7 | `"post-traumatic neurosis"[tiab]` | 22 | none |
| 8 | `posttraumatic neurosis[tiab]` | 7 | none |
| 9 | `"post-traumatic symptom"[tiab]` | 43 | none |
| 10 | `"post-traumatic symptoms"[tiab]` | 170 | none |
| 11 | `"posttraumatic symptom"[tiab]` | 43 | none |
| 12 | `"posttraumatic symptoms"[tiab]` | 320 | none |
| 13 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12` | 56,663 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Stress Disorders, Post-Traumatic"[Mesh] OR "Stress Disorders, Traumatic, Acute"[Mesh] OR PTSD[tiab] OR "post-traumatic stress"[tiab] OR posttraumatic stress[tiab] OR posttraumatic[tiab] OR "post-traumatic neurosis"[tiab] OR posttraumatic neurosis[tiab] OR "post-traumatic symptom"[tiab] OR "post-traumatic symptoms"[tiab] OR "posttraumatic symptom"[tiab] OR "posttraumatic symptoms"[tiab])) AND ("1800/01/01"[edat] : "2016/01/24"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 8 | 8 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 56,670 | initial | none | Initial recall-first PTSD block: PTSD MeSH plus acute traumatic stress MeSH and title/abstract forms for PTSD, spelling variants of post-traumatic stress, historical neurosis wording and MeSH entry-term moral injury; traumatic event and course remain screening criteria. |
| 2 | 56,660 | ptsd: +0 / -4 | none | Removed standalone moral injury terms after sample/unique retrieval exposed scope noise; consolidated PubMed-normalized hyphenation duplicates. Retained all seven development records. |
| 3 | 56,663 | ptsd: +4 / -0 | none | Added and tested singular/plural post-traumatic symptom wording following round 2 critique; precise pilot identified PMID 25585484, screened as eligible and added to relevant development set. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 2 findings; R1-1 should-fix resolved, R1-2 document resolved
- Round 2 on version 2: 3 findings; R1-1 should-fix resolved, R1-2 document resolved, R2-1 should-fix open
- Round 3 on version 3: 3 findings; R1-1 should-fix resolved, R1-2 document resolved, R2-1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 363 NCBI requests logged (128 from cache); strategy sha256 5436dfbf2df9._

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
      "requested": "Stress Disorders, Post-Traumatic",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:58:25+00:00",
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
      "requested": "Stress Disorders, Traumatic, Acute",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:58:25+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D040701",
          "name": "Stress Disorders, Traumatic, Acute",
          "type": "descriptor",
          "scope_note": "A class of traumatic stress disorders that is characterized by the significant dissociative states seen immediately after overwhelming trauma. By definition it cannot last longer than 1 month, if it persists, a diagnosis of post-traumatic stress disorder (STRESS DISORDERS, POST-TRAUMATIC) is more appropriate.",
          "tree_numbers": [
            "F03.950.750.550"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D040701",
      "preferred_label": "Stress Disorders, Traumatic, Acute",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Stress Disorders, Traumatic, Acute\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"stress disorders, post traumatic\"[MeSH Terms] OR \"stress disorders, traumatic, acute\"[MeSH Terms] OR \"PTSD\"[Title/Abstract] OR \"post-traumatic stress\"[Title/Abstract] OR \"posttraumatic stress\"[Title/Abstract] OR \"posttraumatic\"[Title/Abstract] OR \"post-traumatic neurosis\"[Title/Abstract] OR \"posttraumatic neurosis\"[Title/Abstract] OR \"post-traumatic symptom\"[Title/Abstract] OR \"post-traumatic symptoms\"[Title/Abstract] OR \"posttraumatic symptom\"[Title/Abstract] OR \"posttraumatic symptoms\"[Title/Abstract]) AND 1800/01/01:2016/01/24[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "02e0d24fa06e4c5010bc3413213b9356f7394f8357bef934e134157be8fa7ef7",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The sole required block searches PTSD symptoms; traumatic event and trajectory remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are OR-combined; no narrowing AND block or NOT is used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Both headings were verified; the acute traumatic stress heading is included to capture immediate post-event symptoms."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Standalone moral injury terms lack scope support; identical hyphenation forms are redundant."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax or translation errors were reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No filters are applied; the Entrez-date bound is documented without a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "block": "ptsd",
          "finding": "Standalone moral-injury title/abstract terms may retrieve records without PTSD symptoms.",
          "recommendation": "Inspect term-only retrieval and retain only if it contributes in-scope studies.",
          "status": "resolved",
          "response": "Removed both terms after a 28-record sample of the wording retrieved unrelated topics and a residual query without PTSD/post-traumatic-stress wording returned 11 titles including non-PTSD topics. There was no evidence that these standalone terms safely identify this review's condition."
        },
        {
          "id": "R1-2",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "block": "ptsd",
          "finding": "PubMed translates the hyphenated and spaced stress/neurosis variants identically.",
          "recommendation": "Consolidate duplicate forms.",
          "status": "resolved",
          "response": "Removed the spaced variants after the evaluated translations showed identical PubMed expressions for each pair. Retained the hyphenated and closed posttraumatic forms, which translate distinctly."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "c4a49c310683fe4a4f8c1ca24ab57e50ce3dd4b37db391576cd7dc82fafa0119",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "PTSD symptoms are the sole required search concept; event and course are screened."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are OR-combined without restrictive Boolean operators."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Both verified descriptors are OR-ed; the acute heading broadens the post-event time window."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Explicit singular and plural post-traumatic symptom terms are warranted to cover wording without stress or PTSD."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No translation or syntax diagnostics were reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No methodological filters; documented PubMed entry-date cutoff only."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "block": "ptsd",
          "finding": "Standalone moral-injury terms may retrieve records without PTSD symptoms.",
          "recommendation": "Inspect the term-only retrieval and remove if no relevant contribution is supported.",
          "status": "resolved",
          "response": "Removed after term-only sampling showed unrelated uses and no evidence of safe scope equivalence."
        },
        {
          "id": "R1-2",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "block": "ptsd",
          "finding": "PubMed normalizes hyphenated and spaced variants identically.",
          "recommendation": "Consolidate equivalent variants.",
          "status": "resolved",
          "response": "Consolidated the PubMed-equivalent hyphenation pairs, retaining distinct closed posttraumatic wording."
        },
        {
          "id": "R2-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "ptsd",
          "finding": "Post-traumatic symptoms without stress/PTSD wording may be missed.",
          "recommendation": "Test singular/plural hyphenated and closed expressions and evaluate retrieval.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "a471eee48c46a3a1ad56a1d85700fd67dc4119cd43e874afd7fa4a6800458136",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "PTSD symptoms remain the sole searched concept; traumatic-event context and symptom course remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "The PTSD terms are OR-combined without restrictive Boolean operators."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Both verified headings are included, including acute traumatic stress."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Distinct hyphenated and closed forms remain, and singular/plural symptom phrases are added. The added eligible pilot record is retrieved; all eight known relevant records are retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Current evaluation reports no syntax errors, translation issues, or diagnostics."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No study-design or other search filters are applied; the documented PubMed entry-date cutoff is retained."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "block": "ptsd",
          "finding": "Standalone moral-injury terms may retrieve records without PTSD symptoms.",
          "recommendation": "Inspect the term-only retrieval and remove if no relevant contribution is supported.",
          "status": "resolved",
          "response": "Standalone moral-injury terms were removed after term-only sampling found unrelated topics and provided no evidence that those terms safely identify studies with PTSD symptoms."
        },
        {
          "id": "R1-2",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "block": "ptsd",
          "finding": "PubMed normalizes hyphenated and spaced variants identically.",
          "recommendation": "Consolidate equivalent variants.",
          "status": "resolved",
          "response": "PubMed-equivalent spaced variants were consolidated; distinct hyphenated and closed forms remain."
        },
        {
          "id": "R2-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "ptsd",
          "finding": "Post-traumatic symptoms without stress/PTSD wording may be missed.",
          "recommendation": "Test singular/plural hyphenated and closed expressions and evaluate retrieval.",
          "status": "resolved",
          "response": "The strategy now includes singular and plural post-traumatic and posttraumatic symptom phrases. PMID 25585484, located in the focused pilot and added to the relevant set, was retrieved; the current evaluation retrieves all eight known relevant records."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

