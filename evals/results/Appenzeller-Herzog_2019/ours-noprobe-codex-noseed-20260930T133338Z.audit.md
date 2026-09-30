# PubMed search strategy: audit

Generated 2026-09-30T13:54:08+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Comparative effectiveness of common therapies for Wilson disease
- Framework: PICO
- Scope confirmed by user: no (User asked us to proceed without questions. Assumed pharmacologic therapies commonly used for Wilson disease (including D-penicillamine, trientine, zinc salts, and tetrathiomolybdate); comparative effectiveness includes efficacy and safety, and comparators/outcomes are assessed at screening. No language, age, study-design, or publication-date limits. PubMed availability is bounded by Entrez date 2018-12-23 via PSB_AS_OF; no [dp] limit. No known relevant articles supplied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Wilson disease | search | Target condition; disease is the one certain, consistently searchable topic concept. |
| Pharmacologic therapies used for Wilson disease | optional | Named drug therapies are searchable but may be omitted from abstracts; test as a possible second block before deciding. |
| Comparative effectiveness and safety | screen | Comparative outcomes and comparators are not consistently labeled in titles/abstracts; screen for studies comparing therapies. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T13:53:57+00:00
- Records added to PubMed up to: 2018-12-23
- Total records: 7,801
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Hepatolenticular Degeneration[Mesh]` | 5,697 | none |
| 2 | `Wilson[tiab] AND disease[tiab]` | 6,171 | none |
| 3 | `"Wilson disease"[tiab]` | 5,545 | none |
| 4 | `hepatolenticular[tiab]` | 975 | none |
| 5 | `"Kinnier-Wilson"[tiab]` | 38 | none |
| 6 | `"copper storage disease"[tiab]` | 25 | none |
| 7 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6` | 7,801 | none |

### Strategy (single line, for copying into PubMed)

```text
((Hepatolenticular Degeneration[Mesh] OR (Wilson[tiab] AND disease[tiab]) OR "Wilson disease"[tiab] OR hepatolenticular[tiab] OR "Kinnier-Wilson"[tiab] OR "copper storage disease"[tiab])) AND ("1800/01/01"[edat] : "2018/12/23"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Pharmacologic therapies used for Wilson disease | left out | 7,801 / 1,766 | 77.4% | none | 0/30 (up to 10% of removed records could be relevant) | Leave the therapy block out: the strategy now has 7 screened relevant development records, below the required 15-record safety threshold. All 7 are retrieved by the disease block, while the random 30-record loss sample contained no relevant record. The 77.4% reduction does not justify requiring a therapy label without the 15-record safeguard; the disease-only count is within the 10,000-record screening budget. |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial recall-first Wilson disease block; therapy terms held as optional candidate because individual drug names may be inconsistently reported. No known articles supplied; testing against pre-cutoff PubMed and prior review candidates. |
| 2 | 7,801 | wilson: +6 / -0 | none | Initial disease block includes exploded Hepatolenticular Degeneration MeSH and disease/eponym text variants. Pharmacologic therapy names are a tested optional candidate; no therapy AND until comparative risk is evaluated. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 0 findings; 
- Round 2 on version 2: 0 findings; 
- Round 3 on version 2: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 146 NCBI requests logged (37 from cache); strategy sha256 9c654e2ff350._

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
      "checked_at": "2026-09-30T13:53:57+00:00",
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
        "text": "Hepatolenticular Degeneration",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"hepatolenticular degeneration\"[MeSH Terms] OR (\"Wilson\"[Title/Abstract] AND \"disease\"[Title/Abstract]) OR \"Wilson disease\"[Title/Abstract] OR \"hepatolenticular\"[Title/Abstract] OR \"Kinnier-Wilson\"[Title/Abstract] OR \"copper storage disease\"[Title/Abstract]) AND 1800/01/01:2018/12/23[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "75cfe4ed77afe77db5e61041a4c573a507a04213ba9997382ae33cbcbc32a7fc",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched Wilson disease concept matches the scope. Comparative effectiveness and pharmacologic therapies are appropriately treated as screening and optional concepts, respectively."
        },
        "operators": {
          "verdict": "pass",
          "note": "Disease synonyms are OR-combined; Wilson and disease are AND-combined within their text-word expression. The optional therapy block is documented as tested and left out."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Hepatolenticular Degeneration[Mesh] is verified in the packet as the relevant descriptor. No additional disease heading is supported by the supplied evidence."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The disease block includes Wilson disease, hepatolenticular, Kinnier-Wilson, and copper storage disease wording. Therapy vocabulary was tested as an optional block and is not required by the final strategy."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no query errors, warnings, or translation issues. The final query and its date-entry range are shown explicitly."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No publication-date, language, age, or study-design limits are applied. The 2018-12-23 EDAT ceiling is documented as the PubMed snapshot boundary."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "75cfe4ed77afe77db5e61041a4c573a507a04213ba9997382ae33cbcbc32a7fc",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The Wilson disease block represents the sole required searchable concept. Comparative effectiveness is appropriately left to screening, and the optional therapy block is tested and left out with documented rationale and evidence."
        },
        "operators": {
          "verdict": "pass",
          "note": "Disease synonyms are OR-combined, and Wilson and disease are AND-combined within the text-word expression. The final block retrieves all seven development records; the optional block reduction and loss sample are documented alongside the leave-out decision."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Hepatolenticular Degeneration[Mesh] is verified in the packet as the relevant descriptor. No additional disease heading is supported by the supplied evidence."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The disease block includes Wilson disease, hepatolenticular, Kinnier-Wilson, and copper storage disease wording. The packet provides no phrase warnings requiring interpretation review. Therapy terms were tested as an optional block and are not required in the final strategy."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no query errors, warnings, or translation issues. The final query and its date-entry range are explicit."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, publication-date, or study-design filters are applied. The EDAT ceiling is documented as the PubMed snapshot boundary; the disease-only result count remains within the stated screening budget."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "75cfe4ed77afe77db5e61041a4c573a507a04213ba9997382ae33cbcbc32a7fc",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The disease block covers the required Wilson disease concept. Comparative effectiveness is reserved for screening, and the optional therapy block was tested and left out with its rationale documented."
        },
        "operators": {
          "verdict": "pass",
          "note": "Disease synonyms are OR-combined, with Wilson and disease AND-combined in the text-word expression. The final block retrieves all seven development records."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Hepatolenticular Degeneration[Mesh] is verified in the packet as the relevant descriptor; no additional disease heading is supported by the supplied evidence."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The disease block includes Wilson disease, hepatolenticular, Kinnier-Wilson, and copper storage disease wording. Therapy terms were tested as an optional block. The seven-record development set is below the stated 15-record safeguard; this limitation and the leave-out rationale are documented, with all seven known records retrieved and no relevant records in the 30-record loss sample."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no query errors, warnings, or translation issues. The final query and date-entry range are explicit."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, publication-date, or study-design limits are applied. The EDAT ceiling is documented as the PubMed snapshot boundary, and the disease-only result count is within the screening budget."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```

