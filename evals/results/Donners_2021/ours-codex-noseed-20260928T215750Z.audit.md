# PubMed search strategy: audit

Generated 2026-09-28T22:14:46+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In humans, what are the pharmacokinetics of emicizumab and their association with efficacy in haemophilia A?
- Framework: PECO
- Scope confirmed by user: yes (User asked not to pause and to use reasonable assumptions. No known relevant articles were supplied. Scope treats emicizumab as the sole required search concept; PK and bleeding efficacy are tested as optional blocks because eligibility allows either domain and either block could exclude eligible records. Human population and design are screened. Work is run with PubMed/Entrez availability bounded by PSB_AS_OF=2020-10-22; no publication-date limit is used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Emicizumab / ACE910 | search | The drug is the essential, reliably named exposure; search emicizumab and its development code/factor VIII-mimetic description. |
| Pharmacokinetics / exposure | optional | Topic-defining but not all eligible efficacy papers may name PK in the title/abstract; test as an optional block. |
| Efficacy / bleeding outcomes | optional | Topic-defining but PK studies may not name bleeding efficacy; test as an optional block. |
| Human population (haemophilia A and healthy-volunteer bridging studies) | screen | Population terms may be absent from abstracts, and healthy-volunteer studies may not name haemophilia; screen eligibility rather than AND-ing. |
| Clinical trial, pharmacokinetic, or pharmacometric study | screen | Design labels are inconsistently indexed; apply at screening without an ad hoc design filter. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T22:14:24+00:00
- Records added to PubMed up to: 2020-10-22
- Total records: 233
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `emicizumab[nm]` | 161 | none |
| 2 | `emicizumab[tiab]` | 193 | none |
| 3 | `ACE910[tiab]` | 29 | none |
| 4 | `ACE-910[tiab]` | 1 | none |
| 5 | `Hemlibra[tiab]` | 13 | none |
| 6 | `emicizumab-kxwh[tiab]` | 3 | none |
| 7 | `factor VIII-mimetic[tiab]` | 8 | none |
| 8 | `(factor VIII[tiab] AND mimetic*[tiab] AND bispecific*[tiab])` | 11 | none |
| 9 | `FVIII-mimetic[tiab]` | 7 | none |
| 10 | `(FVIII[tiab] AND mimetic*[tiab] AND bispecific*[tiab])` | 8 | none |
| 11 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10` | 233 | none |

### Strategy (single line, for copying into PubMed)

```text
((emicizumab[nm] OR emicizumab[tiab] OR ACE910[tiab] OR ACE-910[tiab] OR Hemlibra[tiab] OR emicizumab-kxwh[tiab] OR factor VIII-mimetic[tiab] OR (factor VIII[tiab] AND mimetic*[tiab] AND bispecific*[tiab]) OR FVIII-mimetic[tiab] OR (FVIII[tiab] AND mimetic*[tiab] AND bispecific*[tiab]))) AND ("1800/01/01"[edat] : "2020/10/22"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 13 | 13 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Pharmacokinetics / exposure | left out | 233 / 52 | 77.7% | 28691557, 30157389, 31348595 | 0/30 (up to 10% of removed records could be relevant) | The candidate PK block reduces 233 records to 52 but loses three eligible clinical efficacy reports in the screened development set (28691557, 30157389, 31348595). The refreshed 30-record loss sample had no eligible record. Leave it out because the protocol includes human trial reports with bleeding efficacy even when PK is not named. |
| Efficacy / bleeding outcomes | left out | 233 / 160 | 31.3% | 26626991, 30230257, 32433829 | 2/30 | The efficacy block reduces 233 records to 160 but loses three eligible human PK/pharmacometric studies (26626991, 30230257, 32433829); the current 30-record loss sample contains two eligible bridge/PK studies (30230257, 32433829). Leave it out because the criteria accept PK/exposure studies without bleeding outcomes. |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 233 | initial | none | Initial recall-first draft: required only the named drug; PK/exposure and efficacy/bleeding blocks are candidates because eligibility accepts either domain, so each is tested for coverage and screening reduction. |
| 2 | 233 | emicizumab: +2 / -0 | none | Added the abbreviated FVIII-mimetic forms to cover the protocol's factor VIII-mimetic description when authors use FVIII; retained the broad drug-only structure after optional-block loss checks. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 0 findings; 
- Round 2 on version 2: 0 findings; 
- Round 3 on version 2: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 364 NCBI requests logged (136 from cache); strategy sha256 47ece7642699._

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
      "checked_at": "2026-09-28T22:14:24+00:00",
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
  "translation": "(\"emicizumab\"[Supplementary Concept] OR \"emicizumab\"[Title/Abstract] OR \"ACE910\"[Title/Abstract] OR \"ACE-910\"[Title/Abstract] OR \"Hemlibra\"[Title/Abstract] OR \"emicizumab-kxwh\"[Title/Abstract] OR \"factor viii mimetic\"[Title/Abstract] OR (\"factor viii\"[Title/Abstract] AND \"mimetic*\"[Title/Abstract] AND \"bispecific*\"[Title/Abstract]) OR \"FVIII-mimetic\"[Title/Abstract] OR (\"FVIII\"[Title/Abstract] AND \"mimetic*\"[Title/Abstract] AND \"bispecific*\"[Title/Abstract])) AND 1800/01/01:2020/10/22[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "a1cb3ddd7725a03cd1be012c3d8d583b7c34ded7a175fddecc7457e731b1a851",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The reported PubMed translation matches the emicizumab heading and text-word strategy; no translation issues or warnings are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The essential emicizumab terms are combined with OR. The optional PK and efficacy blocks were evaluated separately and left out with documented recall losses."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "emicizumab[nm] is verified as the emicizumab supplementary concept. Human population and design are appropriately screened rather than imposed as search headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes emicizumab, ACE910 variants, the brand and product name, and factor VIII-mimetic descriptions. The required drug concept is searched without an optional PK or efficacy restriction."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported PubMed expressions and OR combination are syntactically coherent; no syntax errors or translation issues are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date limit or ad hoc design filter is applied. The query has an entry-date range through 2020-10-22, consistent with the stated as-of boundary."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "876664e0fef5e6efa7af23cdb5b3e6f01aeada68bcbc9bcc91e7aa28ce44fbbb",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Emicizumab is the sole required search concept. PK and efficacy were tested as optional blocks and left out because each loses eligible records from the other evidence stream. Human population and design remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "Drug names and descriptor variants are OR-ed within one block. No unnecessary AND block, NOT clause, or proximity operator is used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The emicizumab supplementary concept is verified and searched with [nm]. No disease or population heading is required for the stated screening approach."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The block covers emicizumab, ACE910, ACE-910, Hemlibra, the suffix form, and factor VIII/FVIII mimetic wording. Optional PK and efficacy terms were tested and their exclusions are justified by eligible records lost."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query is field-tagged and grouped with OR within the drug block. PubMed translations show no syntax errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No human, age, language, or study-design filter is applied. The query uses the Entrez entry-date bound through 2020-10-22, with no publication-date limit."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "876664e0fef5e6efa7af23cdb5b3e6f01aeada68bcbc9bcc91e7aa28ce44fbbb",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The drug is the sole required search concept. PK and efficacy were tested as optional blocks and left out because each excludes eligible records from the other evidence stream; population and design remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "Drug names and descriptor variants are OR-ed within one block. No unnecessary AND block, NOT clause, or proximity operator is used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The emicizumab supplementary concept is verified and searched with [nm]. No disease or population heading is required under the stated screening approach."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The block includes emicizumab, ACE910, ACE-910, Hemlibra, the suffix form, and factor VIII/FVIII-mimetic bispecific wording. The optional blocks’ exclusions are supported by eligible records lost."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Terms are field-tagged and grouped with OR within the drug block. PubMed translations report no syntax errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No human, age, language, or study-design filter is applied. The query uses the specified Entrez entry-date bound through 2020-10-22 and no publication-date limit."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```

