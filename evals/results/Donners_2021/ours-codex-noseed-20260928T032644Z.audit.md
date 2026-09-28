# PubMed search strategy: audit

Generated 2026-09-28T03:38:41+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In humans, what are the pharmacokinetics of emicizumab and their association with efficacy in haemophilia A?
- Framework: PECO
- Scope confirmed by user: no (User requested proceeding without questions; scope and assumptions recorded without confirmation. Search only emicizumab/development names. Human participants, pharmacokinetic/exposure outcomes, bleeding-rate efficacy, and study design are screened rather than AND-ed. No language or publication-date limits. PubMed Entrez date bounded through 2020-10-22.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Emicizumab and development names | search | The drug is the defining exposure/topic and is required across the eligible pharmacokinetic/clinical studies. |
| Human participants | screen | All eligible studies are human, but a human block/filter can miss unindexed and healthy-volunteer bridging records. |
| Pharmacokinetics or exposure | screen | An outcome/method reported inconsistently in titles and abstracts; screen for relevant PK/exposure data. |
| Bleeding-rate efficacy association | screen | Outcome is inconsistently named and the scope also includes PK-only studies. |
| Clinical trial, pharmacokinetic, or pharmacometric study | screen | Design terms are unreliable and no validated filter is required for this narrow topic. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T03:38:28+00:00
- Records added to PubMed up to: 2020-10-22
- Total records: 242
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `emicizumab[nm]` | 161 | none |
| 2 | `emicizumab[tiab]` | 193 | none |
| 3 | `ACE910[tiab]` | 29 | none |
| 4 | `"ACE-910"[tiab]` | 1 | none |
| 5 | `Hemlibra[tiab]` | 13 | none |
| 6 | `"factor VIII mimetic bispecific antibody"[tiab:~2]` | 2 | none |
| 7 | `("factor VIII"[tiab] AND bispecific[tiab] AND (mimetic[tiab] OR mimic*[tiab]))` | 51 | none |
| 8 | `(FVIII[tiab] AND bispecific[tiab] AND (mimetic[tiab] OR mimic*[tiab]))` | 44 | none |
| 9 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8` | 242 | none |

### Strategy (single line, for copying into PubMed)

```text
((emicizumab[nm] OR emicizumab[tiab] OR ACE910[tiab] OR "ACE-910"[tiab] OR Hemlibra[tiab] OR "factor VIII mimetic bispecific antibody"[tiab:~2] OR ("factor VIII"[tiab] AND bispecific[tiab] AND (mimetic[tiab] OR mimic*[tiab])) OR (FVIII[tiab] AND bispecific[tiab] AND (mimetic[tiab] OR mimic*[tiab])))) AND ("1800/01/01"[edat] : "2020/10/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 8 | 8 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 4 | 4 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial recall-first single-block emicizumab strategy. MeSH lookup identified supplementary concept C000608208; text names cover emicizumab, ACE910/ACE-910, Hemlibra, and the eligibility criterion's factor VIII-mimetic bispecific description. Population, outcomes, and study design remain screening criteria. |
| 2 | 242 | emicizumab: +1 / -0 | none | Added the critic-requested explicit FVIII spelling to the factor VIII-mimetic bispecific class-description branch, then re-evaluated recall and counts. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 1 findings; R1-1 should-fix open
- Round 2 on version 2: 1 findings; R1-1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 104 NCBI requests logged (16 from cache); strategy sha256 7a3c6a0761d3._

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
      "requested": "emicizumab",
      "expected_type": "supplementary",
      "checked_at": "2026-09-28T03:38:28+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "C000608208",
          "name": "emicizumab",
          "type": "supplementary",
          "scope_note": "a humanized bispecific antibody mimicking the cofactor function of factor VIII",
          "tree_numbers": [
            "@233593"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "C000608208",
      "preferred_label": "emicizumab",
      "type": "supplementary",
      "location": "vocabulary:1",
      "term": {
        "text": "emicizumab",
        "tag": "nm",
        "field": "nm"
      }
    }
  ],
  "translation": "(\"emicizumab\"[Supplementary Concept] OR \"emicizumab\"[Title/Abstract] OR \"ACE910\"[Title/Abstract] OR \"ACE-910\"[Title/Abstract] OR \"Hemlibra\"[Title/Abstract] OR \"factor VIII mimetic bispecific antibody\"[Title/Abstract:~2] OR (\"factor VIII\"[Title/Abstract] AND \"bispecific\"[Title/Abstract] AND (\"mimetic\"[Title/Abstract] OR \"mimic*\"[Title/Abstract])) OR (\"FVIII\"[Title/Abstract] AND \"bispecific\"[Title/Abstract] AND (\"mimetic\"[Title/Abstract] OR \"mimic*\"[Title/Abstract]))) AND 1800/01/01:2020/10/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "dfad7435b3ca0d5a93e6c9f4c794cacec5088a038a93959ce830c188ee8774ab",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The terms are explicitly fielded, and the supplied counts and OR total are internally plausible. Translation diagnostics are not provided."
        },
        "operators": {
          "verdict": "pass",
          "note": "The named emicizumab terms are ORed with the class description terms, preserving recall across naming variants."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports a verified emicizumab supplementary concept and no mapped descriptor; emicizumab[nm] is included."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The class-term fallback uses only the spelled-out factor VIII form. It may miss records using FVIII in descriptions of factor VIII-mimetic bispecific antibodies."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Clause 6 has no wildcard in its proximity expression. The packet specifies that ~2 permits any word order; clause 7 separately provides a broader conjunction."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez date-entry cutoff is stated, and no human, outcome, or design filter is applied despite the packet noting potential indexing and naming inconsistencies."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The generic class-description fallback requires the literal phrase factor VIII in clause 7. Records describing the antibody class with FVIII may therefore be missed if they do not also use one of the named emicizumab terms.",
          "recommendation": "Add and test an explicit FVIII class-description variant, such as FVIII AND bispecific AND (mimetic OR mimic*), then rerun the complete evaluation and report its effect on counts and known-record recall.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "624f3a4afa1654d4b1f75af162aab1dfda6fae94814ef2643406bf6f604de8ef",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The name-based search retrieves candidate records, while human, PK/exposure, efficacy, and study-design criteria are reserved for screening as specified."
        },
        "operators": {
          "verdict": "pass",
          "note": "Name and class-description terms are combined with OR; the date-entry bound is applied separately."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports a verified emicizumab supplementary concept with no mapped descriptor, and the strategy includes its substance-name field."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The name terms and class-description alternatives include both factor VIII and FVIII formulations. The earlier FVIII coverage finding is addressed."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query is parenthesized and the packet reports clean lint and no translation diagnostics."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The only limit is the stated Entrez date-entry bound through 2020-10-22; no human or outcome filter is imposed."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The prior concern was that the class-description fallback required literal factor VIII and could miss descriptions using FVIII.",
          "recommendation": "Add and test FVIII[tiab] AND bispecific[tiab] AND (mimetic[tiab] OR mimic*[tiab]).",
          "status": "resolved",
          "response": "Added the FVIII alternative as term 8; evaluation increased the count from 241 to 242, with no known record loss and 100% relative recall in both reported sets."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

