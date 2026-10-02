# PubMed search strategy: audit

Generated 2026-10-02T13:46:41+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Comparative effectiveness of common therapies for Wilson disease
- Framework: PICO
- Scope confirmed by user: no (User requested no follow-up questions; scope proceeded with documented assumptions. Interpreted common therapies broadly to include chelators (e.g., penicillamine, trientine), zinc therapy, and liver transplantation when comparative effectiveness is evaluated. No language, age, design, or publication-date limits. PubMed record availability is bounded at Entrez date 2018-12-23 via PSB_AS_OF for every command; no publication-date limit is applied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Wilson disease | search | The disease is the required, reliably named population and the defining topic. |
| Common Wilson disease therapies | screen | Therapy membership is broad and may be incompletely reported in titles/abstracts; requiring named agents risks missing comparative cohorts. Screen for eligible therapies and direct/indirect comparative effectiveness. |
| Comparative effectiveness, outcomes, and study design | screen | Comparators, outcomes, and design terms are inconsistently indexed and are not required search concepts. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T13:46:26+00:00
- Records added to PubMed up to: 2018-12-23
- Total records: 7,282
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Hepatolenticular Degeneration"[Mesh]` | 5,697 | none |
| 2 | `"Wilson disease"[tiab:~0]` | 1,570 | none |
| 3 | `"Wilson's disease"[tiab]` | 4,158 | none |
| 4 | `Wilsons disease[tiab]` | 4,135 | none |
| 5 | `"hepatolenticular degeneration"[tiab:~0]` | 946 | none |
| 6 | `"neurohepatic degeneration"[tiab:~0]` | 0 | warning: pubmed_warning; warning: zero_hits |
| 7 | `"Kinnier Wilson"[tiab:~1]` | 38 | none |
| 8 | `"Westphal Strumpell"[tiab:~1]` | 27 | none |
| 9 | `"copper storage disease"[tiab:~0]` | 27 | none |
| 10 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9` | 7,282 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Hepatolenticular Degeneration"[Mesh] OR "Wilson disease"[tiab:~0] OR "Wilson's disease"[tiab] OR Wilsons disease[tiab] OR "hepatolenticular degeneration"[tiab:~0] OR "neurohepatic degeneration"[tiab:~0] OR "Kinnier Wilson"[tiab:~1] OR "Westphal Strumpell"[tiab:~1] OR "copper storage disease"[tiab:~0])) AND ("1800/01/01"[edat] : "2018/12/23"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 1 | 1 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 7,282 | initial | none | Initial recall-first strategy: one Wilson disease concept with descriptor explosion and text-word synonyms/proximity. Therapy, comparator, outcome, and design remain screen concepts to avoid over-structuring. The one discovered comparative cohort was retained as a relevant development record. |
| 2 | 7,282 | wilson_disease: +0 / -1 | none | Removed the neurohepatic degeneration free-text proximity clause after the bounded PubMed line count returned zero with a No items found warning. Retained the exact descriptor's MeSH layer and other independently named disease aliases; no known-record loss. |
| 3 | 7,282 | wilson_disease: +1 / -0 | none | Restored neurohepatic degeneration[tiab:~0] after internal PRESS critic noted that the zero-hit clause was not enough evidence to remove a potential disease synonym. Retaining this OR alternative favors recall; PubMed currently reports zero hits for the clause in the Entrez-bounded snapshot, which is documented for peer review. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 1 findings; R1-1 should-fix open
- Round 2 on version 3: 1 findings; R1-1 should-fix resolved
- Round 3 on version 3: 1 findings; R1-1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 114 NCBI requests logged (34 from cache); strategy sha256 04edcf3f6321._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "severity": "warning",
        "code": "pubmed_warning",
        "message": "PubMed reported a warning; review the translation.",
        "evidence": "outputmessages: No items found.",
        "query": "(\"neurohepatic degeneration\"[tiab:~0]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
        "translation": "\"neurohepatic degeneration\"[Title/Abstract:~0] AND 1800/01/01:2018/12/23[Date - Entry]",
        "location": "line:6",
        "blocking": false,
        "requires_review": true,
        "id": "I-c836ff8910117855e514"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(\"neurohepatic degeneration\"[tiab:~0]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
        "translation": "\"neurohepatic degeneration\"[Title/Abstract:~0] AND 1800/01/01:2018/12/23[Date - Entry]",
        "location": "line:6",
        "blocking": false,
        "requires_review": true,
        "id": "I-531e71a75d86654f8b68"
      }
    ],
    "issues": [
      {
        "severity": "warning",
        "code": "pubmed_warning",
        "message": "PubMed reported a warning; review the translation.",
        "evidence": "outputmessages: No items found.",
        "query": "(\"neurohepatic degeneration\"[tiab:~0]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
        "translation": "\"neurohepatic degeneration\"[Title/Abstract:~0] AND 1800/01/01:2018/12/23[Date - Entry]",
        "location": "line:6",
        "blocking": false,
        "requires_review": true,
        "id": "I-c836ff8910117855e514"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(\"neurohepatic degeneration\"[tiab:~0]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
        "translation": "\"neurohepatic degeneration\"[Title/Abstract:~0] AND 1800/01/01:2018/12/23[Date - Entry]",
        "location": "line:6",
        "blocking": false,
        "requires_review": true,
        "id": "I-531e71a75d86654f8b68"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Hepatolenticular Degeneration",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:46:26+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D006527",
          "name": "Hepatolenticular Degeneration",
          "type": "descriptor",
          "scope_note": "A rare autosomal recessive disease characterized by the deposition of copper in the BRAIN; LIVER; CORNEA; and other organs. It is caused by defects in the ATP7B gene encoding copper-transporting ATPase 2 (EC 3.6.3.4), also known as the Wilson disease protein. The overload of copper inevitably leads to progressive liver and neurological dysfunction such as LIVER CIRRHOSIS; TREMOR; ATAXIA and int...",
          "tree_numbers": [
            "C06.552.413",
            "C10.228.140.079.493",
            "C10.228.140.163.100.360",
            "C10.228.662.400",
            "C10.574.500.487",
            "C16.320.400.361",
            "C16.320.565.189.360",
            "C16.320.565.618.403",
            "C18.452.132.100.360",
            "C18.452.648.189.360",
            "C18.452.648.618.403"
          ],
          "entry_terms": 47,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D006527",
      "preferred_label": "Hepatolenticular Degeneration",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"Hepatolenticular Degeneration\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Hepatolenticular Degeneration\"[MeSH Terms] OR \"Wilson disease\"[Title/Abstract:~0] OR \"Wilson's disease\"[Title/Abstract] OR \"wilsons disease\"[Title/Abstract] OR \"Hepatolenticular Degeneration\"[Title/Abstract:~0] OR \"neurohepatic degeneration\"[Title/Abstract:~0] OR \"Kinnier Wilson\"[Title/Abstract:~1] OR \"Westphal Strumpell\"[Title/Abstract:~1] OR \"copper storage disease\"[Title/Abstract:~0]) AND 1800/01/01:2018/12/23[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "328e9ec74a11bf8d79af0d45ddc3f98bc145d30835b4f05f2270c28554bdf0b3",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The reported PubMed translations preserve the Wilson disease MeSH and title/abstract terms; no translation issues or diagnostic warnings are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The disease synonyms are combined with OR. The ~0 expressions allow either word order, which remains interpretable for the disease-name clauses; no proximity wildcards are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The Hepatolenticular Degeneration descriptor is verified as the intended MeSH descriptor for Wilson disease."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The previous strategy's neurohepatic degeneration term was removed. The packet provides no term-level evidence or rationale for that removal; retrieval of the single known relevant record and an unchanged total count do not establish that the term is redundant."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All reported lines have no syntax diagnostics, and the final query is explicitly reported as valid."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No study limits are applied. The entry-date bound is documented as the PubMed record-availability cutoff, not a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The prior strategy included neurohepatic degeneration[tiab:~0], but version 2 removes it. The packet gives no term-level retrieval evidence or other rationale for the deletion. The retained known record and unchanged overall result count do not show that this synonym adds no relevant records.",
          "recommendation": "Restore the term and evaluate the complete revised strategy, or provide term-level evidence supporting its removal and evaluate the complete revised strategy.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "ac8b17035bfb9b7e0637b9c933de71d96fe93e95ff9e27c45ce0b2c9eaa18ac3",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The reported translations preserve the MeSH heading and title/abstract clauses. For the flagged term, the exact query is (\"neurohepatic degeneration\"[tiab:~0]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat]); PubMed translates it as \"neurohepatic degeneration\"[Title/Abstract:~0] AND 1800/01/01:2018/12/23[Date - Entry]. No phrase-ignored message or translation error is reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The disease terms are combined with OR. The ~0 expressions allow either word order, and no proximity wildcards are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Hepatolenticular Degeneration is verified in the packet as the intended MeSH descriptor."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The previously removed neurohepatic degeneration clause is restored and the complete revised strategy was evaluated. Its exact phrase query returned 0 records and PubMed reported No items found under the stated entry-date bound. This does not establish that it is an invalid synonym or redundant outside this bounded snapshot."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no syntax diagnostics for the lines or final query."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No study limits are applied. The entry-date bound through 2018-12-23 is documented as the PubMed record-availability cutoff, not a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Round 1 noted that neurohepatic degeneration had been removed without term-level evidence or rationale.",
          "recommendation": "Restore the term and evaluate the complete revised strategy, or provide term-level evidence for removal and evaluate the complete revised strategy.",
          "status": "resolved",
          "response": "The term is restored in version 3, and the complete revised strategy was evaluated. Its term-level check is reported with the exact bounded query, translation, and zero-hit warning; this resolves the earlier unsupported-removal finding."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-c836ff8910117855e514",
          "status": "accepted-risk",
          "response": "Reviewed the warning for the restored phrase clause. The reported translation preserves the quoted phrase and field; the warning reflects no items found in the stated entry-date-bounded search. Retain provisionally as a candidate term rather than treating this warning alone as proof that the phrase is invalid or redundant.",
          "evidence": "Query: (\"neurohepatic degeneration\"[tiab:~0]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat]). Translation: \"neurohepatic degeneration\"[Title/Abstract:~0] AND 1800/01/01:2018/12/23[Date - Entry]. Results: 0; output message: No items found. phrasesignored and quotedphrasesnotfound are empty."
        },
        {
          "issue_id": "I-531e71a75d86654f8b68",
          "status": "accepted-risk",
          "response": "The zero-hit warning is acknowledged for this clause in the bounded snapshot. A zero count does not establish that the term is redundant or invalid beyond the tested query and date bound.",
          "evidence": "The exact term query returned 0 records through the 2018-12-23 entry-date cutoff; the reported translation retains the quoted phrase as Title/Abstract proximity ~0."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "ac8b17035bfb9b7e0637b9c933de71d96fe93e95ff9e27c45ce0b2c9eaa18ac3",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Reported translations preserve the MeSH heading and title/abstract clauses. The neurohepatic degeneration clause retains its quoted phrase and field; no phrase-ignored message or translation error is reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "Disease terms are combined with OR. The ~0 expressions allow either word order, and no proximity wildcards are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Hepatolenticular Degeneration is verified as the intended MeSH descriptor."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The previously removed neurohepatic degeneration term is restored and evaluated in the complete revised strategy. Its zero-hit result is documented for the stated entry-date bound; this does not establish redundancy outside that snapshot."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no syntax diagnostics for the individual lines or final query."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No study limits are applied. The entry-date bound through 2018-12-23 is documented as the PubMed record-availability cutoff, not a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Round 1 noted that neurohepatic degeneration had been removed without term-level evidence or rationale.",
          "recommendation": "Restore the term and evaluate the complete revised strategy, or provide term-level evidence for removal and evaluate the complete revised strategy.",
          "status": "resolved",
          "response": "The term is restored in version 3 and the complete revised strategy was evaluated. Its exact bounded query, translation, and zero-hit result are reported."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-c836ff8910117855e514",
          "status": "accepted-risk",
          "response": "Retain the clause provisionally as a candidate term. The warning reflects no items found in the stated bounded search; the reported translation preserves the quoted phrase and field, so the warning alone does not show that the phrase is invalid or redundant.",
          "evidence": "The exact query returned 0 records through the 2018-12-23 entry-date cutoff. Its translation is \"neurohepatic degeneration\"[Title/Abstract:~0] AND 1800/01/01:2018/12/23[Date - Entry]; phrasesignored and quotedphrasesnotfound are empty."
        },
        {
          "issue_id": "I-531e71a75d86654f8b68",
          "status": "accepted-risk",
          "response": "Acknowledge the zero-hit result for this clause in the bounded snapshot and retain the term provisionally; the count alone does not establish that it is redundant or invalid beyond the tested query and date bound.",
          "evidence": "The exact term query returned 0 records through the 2018-12-23 entry-date cutoff, and the reported translation retains the quoted phrase as Title/Abstract proximity ~0."
        }
      ]
    }
  ]
}
```

