# PubMed search strategy: audit

Generated 2026-10-02T13:36:59+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: condition + clinical course
- Scope confirmed by user: yes (User asked to proceed without questions; scope confirmation was waived by instruction. Assumed the review concerns theories or psychological explanatory models of depressive relapse/recurrence, rather than all risk factors or treatment-prevention efficacy. Search depressive disorders AND relapse/recurrence broadly; assess psychological theory relevance at screening because theory language is inconsistently indexed. No limits. Treat PubMed as-of 2018-11-17 via PSB_AS_OF environment on every command; no publication-date limit. No known relevant articles supplied, so any screened discoveries are development evidence, not independent validation.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depressive disorders | search | The condition is explicit in the question and can be named and indexed reliably. |
| Depressive relapse and recurrence | search | Relapse/recurrence defines the clinical course under review and is a searchable topic; search broadly for the process and screen for the psychological-theory focus. |
| Psychological theories and explanatory models | screen | Relevant authors may discuss cognitive, behavioral, interpersonal, psychodynamic, or other psychological explanations without naming them as theories in title, abstract, or indexing; requiring this fragile label risks missed records. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T13:36:00+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 60,709
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Depressive Disorder"[Mesh]` | 105,341 | none |
| 2 | `"Major Depressive Disorder"[Mesh]` | 28,520 | none |
| 3 | `"Depression"[Mesh]` | 112,392 | none |
| 4 | `depress*[tiab]` | 419,764 | none |
| 5 | `melanchol*[tiab]` | 2,939 | none |
| 6 | `dysthymi*[tiab]` | 3,055 | none |
| 7 | `MDD[tiab]` | 10,931 | none |
| 8 | `"unipolar depression"[tiab]` | 2,526 | none |
| 9 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8` | 461,214 | none |
| 10 | `"Recurrence"[Mesh]` | 178,366 | none |
| 11 | `"Secondary Prevention"[Mesh]` | 19,442 | none |
| 12 | `relaps*[tiab]` | 163,847 | none |
| 13 | `recurr*[tiab]` | 518,001 | none |
| 14 | `recrudesc*[tiab]` | 3,310 | none |
| 15 | `return*[tiab]` | 223,418 | none |
| 16 | `episode*[tiab]` | 187,072 | none |
| 17 | `remission*[tiab]` | 113,679 | none |
| 18 | `recover*[tiab]` | 602,986 | none |
| 19 | `(return*[tiab] AND depress*[tiab])` | 7,933 | none |
| 20 | `(return*[tiab] AND episode*[tiab])` | 4,133 | none |
| 21 | `#10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20` | 1,712,006 | none |
| 22 | `#9 AND #21` | 60,709 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Depressive Disorder"[Mesh] OR "Major Depressive Disorder"[Mesh] OR "Depression"[Mesh] OR depress*[tiab] OR melanchol*[tiab] OR dysthymi*[tiab] OR MDD[tiab] OR "unipolar depression"[tiab]) AND ("Recurrence"[Mesh] OR "Secondary Prevention"[Mesh] OR relaps*[tiab] OR recurr*[tiab] OR recrudesc*[tiab] OR return*[tiab] OR episode*[tiab] OR remission*[tiab] OR recover*[tiab] OR (return*[tiab] AND depress*[tiab]) OR (return*[tiab] AND episode*[tiab]))) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 8 | 8 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| depression | 1,712,006 | 0 |
| relapse_recurrence | 461,214 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 18,015 | initial | none | Initial recall-first two-block strategy: depressive disorders AND relapse/recurrence; psychological theory remains a screening criterion because it is inconsistently indexed. Terms include MeSH and title/abstract vocabulary; used screened developments only. |
| 2 | 18,015 | relapse_recurrence: +0 / -2 | none | Removed two exact return-of phrases after PubMed reported no phrase-index entries and zero hits; this form is not required for the topic because broad Relapse/Recurrence MeSH and relaps*/recurr* text terms remain. Preserve broad recall terms and recheck all development records. |
| 3 | 25,528 | relapse_recurrence: +2 / -0 | none | Addressed critic R1-01: restored return-of-course coverage as tested title/abstract co-occurrence clauses (return*[tiab] AND depress*[tiab]) and (return*[tiab] AND episode*[tiab]); direct phrase/proximity tests were unsuitable because PubMed translated return to All Fields, so retained field-specific AND clauses. Re-evaluate recall and translation. |
| 4 | 60,709 | relapse_recurrence: +4 / -0 | none | Addressed R1-01 by adding bare title/abstract stems for return, episode, remission and recovery to cover the named episode-return wording and both phases of the course, while retaining the tested co-occurrence variants and broad relapse/recurrence terms. Kept screening for course and theory relevance; check count, retrieval and translation. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 1 findings; R1-01 must-fix open
- Round 2 on version 4: 1 findings; R1-01 must-fix resolved
- Round 3 on version 4: 1 findings; R1-01 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 359 NCBI requests logged (100 from cache); strategy sha256 62bb0a4399ec._

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
      "requested": "Depressive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:36:00+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003866",
          "name": "Depressive Disorder",
          "type": "descriptor",
          "scope_note": "An affective disorder manifested by either a dysphoric mood or loss of interest or pleasure in usual activities. The mood disturbance is prominent and relatively persistent.",
          "tree_numbers": [
            "F03.600.300"
          ],
          "entry_terms": 20,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003866",
      "preferred_label": "Depressive Disorder",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"Depressive Disorder\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Major Depressive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:36:00+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003865",
          "name": "Major Depressive Disorder",
          "type": "descriptor",
          "scope_note": "Disorder in which five (or more) of the following symptoms have been present during the same 2-week period and represent a change from previous functioning; at least one of the symptoms is either (1) depressed mood or (2) loss of interest or pleasure. Symptoms include: depressed mood most of the day, nearly every day; markedly diminished interest or pleasure in activities most of the day, nearl...",
          "tree_numbers": [
            "F03.600.300.375"
          ],
          "entry_terms": 18,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003865",
      "preferred_label": "Major Depressive Disorder",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Major Depressive Disorder\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:36:00+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003863",
          "name": "Depression",
          "type": "descriptor",
          "scope_note": "Depressive states usually of moderate intensity in contrast with MAJOR DEPRESSIVE DISORDER present in neurotic and psychotic disorders.",
          "tree_numbers": [
            "F01.145.126.350",
            "F01.470.282"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003863",
      "preferred_label": "Depression",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "\"Depression\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Recurrence",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:36:00+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012008",
          "name": "Recurrence",
          "type": "descriptor",
          "scope_note": "The return of a sign, symptom, or disease after a remission.",
          "tree_numbers": [
            "C23.550.291.937"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012008",
      "preferred_label": "Recurrence",
      "type": "descriptor",
      "location": "vocabulary:9",
      "term": {
        "text": "\"Recurrence\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Secondary Prevention",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:36:00+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D055502",
          "name": "Secondary Prevention",
          "type": "descriptor",
          "scope_note": "The prevention of recurrences or exacerbations of a disease or complications of its therapy.",
          "tree_numbers": [
            "E02.897",
            "N02.421.726.825",
            "N06.850.780.750"
          ],
          "entry_terms": 17,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D055502",
      "preferred_label": "Secondary Prevention",
      "type": "descriptor",
      "location": "vocabulary:10",
      "term": {
        "text": "\"Secondary Prevention\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Depressive Disorder\"[MeSH Terms] OR \"Major Depressive Disorder\"[MeSH Terms] OR \"Depression\"[MeSH Terms] OR \"depress*\"[Title/Abstract] OR \"melanchol*\"[Title/Abstract] OR \"dysthymi*\"[Title/Abstract] OR \"MDD\"[Title/Abstract] OR \"unipolar depression\"[Title/Abstract]) AND (\"Recurrence\"[MeSH Terms] OR \"Secondary Prevention\"[MeSH Terms] OR \"relaps*\"[Title/Abstract] OR \"recurr*\"[Title/Abstract] OR \"recrudesc*\"[Title/Abstract] OR \"return*\"[Title/Abstract] OR \"episode*\"[Title/Abstract] OR \"remission*\"[Title/Abstract] OR \"recover*\"[Title/Abstract] OR (\"return*\"[Title/Abstract] AND \"depress*\"[Title/Abstract]) OR (\"return*\"[Title/Abstract] AND \"episode*\"[Title/Abstract])) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "3017a075dcbf71c4581cc4518303191ce60acec09241fade4ef5a54374d0aebe",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The eligibility wording names return of a depressive episode, but the course block searches return and episode only in conjunctive expressions. The packet’s translation checks require named members to be covered by their own bare-name searches and call for searching the process in either direction."
        },
        "operators": {
          "verdict": "pass",
          "note": "The blocks combine synonyms with OR and combine the required condition and course concepts with AND, consistent with the stated scope."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the selected MeSH descriptors, and the condition and course blocks also include free-text terms."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Return and episode appear only in conjunctions, which can miss records using either named term without the paired wording. The return language also covers only one side of the course."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint errors, translation issues, PubMed errors, or warnings for the displayed query."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication or study-design limits are applied. The entry-date bound is consistent with the packet’s stated as-of date."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The eligibility criteria include a return of depressive episode, but the course block searches return and episode only as `(return*[tiab] AND depress*[tiab])` or `(return*[tiab] AND episode*[tiab])`. This does not cover the named members by their own bare-name searches under the packet’s translation check. The added return expressions also search only return-side wording, although the packet requires searching the process in either direction and screening direction.",
          "recommendation": "Add explicit, tested bare-name expressions for the named terms and expressions that cover both sides of the clinical course, such as remission or recovery and subsequent episode return or re-emergence. Screen for whether the wording concerns depressive relapse or recurrence. Re-run the complete evaluation after the rewrite.",
          "status": "open",
          "response": null
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "7c2dd65a20314a8c5f1211707f9553cfbd9f731f1f981126cb9453e0b47c3ab3",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The course block now includes bare-name searches for return* and episode*, alongside terms for relapse, recurrence, remission, and recovery. It covers both course directions for screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are combined with OR, and the required depression and course blocks are combined with AND."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the selected depression, recurrence, and secondary prevention MeSH descriptors; both blocks also include free-text terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Bare return* and episode* searches address the earlier lexical gap. Relaps*, recurr*, remission*, and recover* add course vocabulary; psychological theory remains a screening concept as scoped."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint errors, translation issues, PubMed errors, or warnings for the displayed query."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication or study-design limits are applied. The entry-date bound matches the stated as-of date."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The prior version lacked bare-name searches for return and episode and did not adequately cover both course directions.",
          "recommendation": "Add explicit bare-name searches for the named terms and course vocabulary for both directions, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "Version 4 adds return*[tiab] and episode*[tiab] as standalone terms, and includes remission*[tiab], recover*[tiab], relaps*[tiab], and recurr*[tiab]. The packet reports a complete evaluation with no validation blockers."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "7c2dd65a20314a8c5f1211707f9553cfbd9f731f1f981126cb9453e0b47c3ab3",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The course block includes standalone return* and episode* searches, plus relapse, recurrence, remission, and recovery terms, addressing both course directions for screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are combined with OR, and the depression and clinical-course blocks are combined with AND, consistent with the stated searchable scope."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the selected depression, recurrence, and secondary prevention MeSH descriptors; both blocks also include free-text terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Standalone return* and episode* terms resolve the earlier lexical gap. Psychological theory remains a screening concept, consistent with the scope rationale."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint errors, translation issues, PubMed errors, or warnings for the evaluated query."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication or study-design limits are applied. The entry-date bound matches the stated as-of date."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The earlier version lacked bare-name searches for return and episode and did not adequately cover both course directions.",
          "recommendation": "Add explicit bare-name searches for the named terms and course vocabulary for both directions, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "Version 4 adds return*[tiab] and episode*[tiab] as standalone terms and includes remission*[tiab], recover*[tiab], relaps*[tiab], and recurr*[tiab]. The packet reports a complete evaluation with no validation blockers."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

