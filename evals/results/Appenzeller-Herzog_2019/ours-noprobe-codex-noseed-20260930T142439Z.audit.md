# PubMed search strategy: audit

Generated 2026-09-30T14:53:29+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Comparative effectiveness of common therapies for Wilson disease
- Framework: PICO
- Scope confirmed by user: no (User asked to proceed without questions; roles and criteria are provisional assumptions. No known relevant records supplied. Search constrained by Entrez date as of 2018-12-23 per harness; no publication-date limit. Standard-depth workload budget 10,000. Wilson disease is required; a comprehensive named-treatment block is tested as optional. Outcomes, comparators, age, and design are screened. Common therapies are interpreted broadly to include chelators, zinc, and liver transplantation. Eligibility interpretation: comparative effectiveness is taken to require comparison of at least two WD-directed treatments/regimens; uncontrolled single-treatment studies remain outside scope.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Wilson disease | search | The target condition defines every eligible clinical study and has established disease terminology. |
| Therapies for Wilson disease | optional | Treatment is central but records may name a specific drug, copper-directed treatment, or transplant without using general therapy wording; test the treatment block against disease-only retrieval before requiring it. |
| Comparative outcomes and effectiveness | screen | Comparators and outcome/effectiveness reporting are inconsistently named and should be assessed at screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T14:53:16+00:00
- Records added to PubMed up to: 2018-12-23
- Total records: 7,313
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Hepatolenticular Degeneration"[Mesh]` | 5,697 | none |
| 2 | `wilson disease[tiab]` | 5,545 | none |
| 3 | `wilson's disease[tiab]` | 4,158 | none |
| 4 | `wilsons disease[tiab]` | 4,135 | none |
| 5 | `hepatolenticular degeneration[tiab]` | 946 | none |
| 6 | `hepatocerebral degeneration[tiab]` | 142 | none |
| 7 | `copper storage disease[tiab]` | 25 | none |
| 8 | `westphal-strumpell syndrome[tiab]` | 1 | none |
| 9 | `pseudosclerosis[tiab]` | 55 | none |
| 10 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9` | 7,313 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Hepatolenticular Degeneration"[Mesh] OR wilson disease[tiab] OR wilson's disease[tiab] OR wilsons disease[tiab] OR hepatolenticular degeneration[tiab] OR hepatocerebral degeneration[tiab] OR copper storage disease[tiab] OR westphal-strumpell syndrome[tiab] OR pseudosclerosis[tiab])) AND ("1800/01/01"[edat] : "2018/12/23"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 8 | 8 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Therapies for Wilson disease | left out | 7,313 / 2,316 | 68.3% | none | 0/30 (up to 10% of removed records could be relevant) | The therapy block removes 68.3% of disease retrieval but only 8 eligible known records are available, below the 15-record safety threshold for requiring it; none of the 30 randomly sampled records it would remove met the comparative-treatment eligibility criteria. Keep the block out to preserve recall; disease-only count remains below the 10,000 screening budget. |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 7,324 | initial | none | Initial high-sensitivity scope: disease required; optional broad treatment block measured before deciding whether to require therapy terms. Outcomes, comparators, and designs screened. |
| 2 | 7,313 | wilson_disease: +0 / -1 | none | Corrected optional role for treatment and removed a legacy hyphenated phrase whose PubMed translation fell back to All Fields; MeSH and other synonym coverage retained. |
| 3 | 7,313 | wilson_disease: +0 / -1 | none | Screened precise pilot titles/abstracts; added in-scope comparative treatment records to development set, tightened eligibility to comparisons of at least two regimens, removed a zero-hit legacy synonym, and added historical dimercaprol vocabulary. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 0 findings; 
- Round 2 on version 3: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 181 NCBI requests logged (51 from cache); strategy sha256 1e3a8eeb37db._

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
      "requested": "Hepatolenticular Degeneration",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:53:16+00:00",
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
  "translation": "(\"Hepatolenticular Degeneration\"[MeSH Terms] OR \"wilson disease\"[Title/Abstract] OR \"wilson s disease\"[Title/Abstract] OR \"wilsons disease\"[Title/Abstract] OR \"Hepatolenticular Degeneration\"[Title/Abstract] OR \"hepatocerebral degeneration\"[Title/Abstract] OR \"copper storage disease\"[Title/Abstract] OR \"westphal strumpell syndrome\"[Title/Abstract] OR \"pseudosclerosis\"[Title/Abstract]) AND 1800/01/01:2018/12/23[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "1a949790d1189beb9d068c385303702c42bf9c0aaeee2018300e7e1158bd4bd0",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The displayed PubMed translations preserve the disease terms as Title/Abstract phrases, and the MeSH heading is verified. No translation warnings or errors are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "Disease synonyms are combined with OR. The therapy block is optional and was left out after testing; the disease-only retrieval is within the stated screening budget. Comparators and outcomes are reserved for screening."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes the verified Hepatolenticular Degeneration MeSH descriptor for Wilson disease."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The disease block includes Wilson disease variants and the listed disease synonyms as bare text terms. The optional therapy vocabulary was tested, and the packet gives a recall-based rationale for not requiring it."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query is displayed with balanced grouping, OR-combined disease terms, and the stated entry-date range. No syntax errors or translation issues are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No study-design, human, or other eligibility filters are applied. The entry-date cutoff is identified as a harness constraint, not a publication-date limit."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "1a949790d1189beb9d068c385303702c42bf9c0aaeee2018300e7e1158bd4bd0",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The displayed translations preserve the disease terms as Title/Abstract phrases, and the Hepatolenticular Degeneration MeSH heading is verified. No translation warnings or errors are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "Disease terms are OR-combined. The optional therapy block was tested and left out with a stated recall rationale; disease-only retrieval is within budget. Comparators and outcomes remain screening criteria."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes the verified Hepatolenticular Degeneration MeSH descriptor for Wilson disease."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The disease block covers Wilson disease variants and listed disease synonyms with bare text terms. No required searched-concept members are covered only by a narrowed phrase."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query is displayed with balanced grouping, OR-combined disease terms, and the stated entry-date range. No syntax errors or translation issues are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No study-design, human, or other eligibility filters are applied. The entry-date cutoff is identified as a harness constraint rather than a publication-date limit."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```

