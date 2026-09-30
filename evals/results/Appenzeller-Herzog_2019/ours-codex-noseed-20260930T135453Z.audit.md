# PubMed search strategy: audit

Generated 2026-09-30T14:23:18+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Comparative effectiveness of common therapies for Wilson disease
- Framework: PICO
- Scope confirmed by user: no (User requested proceeding without questions. Assumption: common therapies means pharmacologic anti-copper treatment (chelators and zinc); transplantation alone is out of scope. No language, age, publication-date, or study-design limit. PubMed Entrez-date cutoff is 2018-12-23 via PSB_AS_OF; no [dp] limit. No known relevant records supplied; standard-depth discovery attempted.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Wilson disease (hepatolenticular degeneration) | search | The target condition defines the review population and is reliably named or indexed. |
| Common pharmacologic anti-copper therapies | optional | Comparative therapies are central, but requiring named agents may miss comparative studies whose abstracts do not report all treatments; test this block before deciding. |
| Comparators and effectiveness outcomes | screen | Comparators and outcomes are inconsistently named and are safer to assess during screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T14:23:01+00:00
- Records added to PubMed up to: 2018-12-23
- Total records: 7,600
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Hepatolenticular Degeneration[Mesh]` | 5,697 | none |
| 2 | `wilson disease[tiab]` | 5,545 | none |
| 3 | `wilson's disease[tiab]` | 4,158 | none |
| 4 | `wilsons disease[tiab]` | 4,135 | none |
| 5 | `hepatolenticular degeneration[tiab]` | 946 | none |
| 6 | `hepatolenticular[tiab]` | 975 | none |
| 7 | `progressive lenticular degeneration[tiab]` | 10 | none |
| 8 | `kinnier-wilson[tiab]` | 38 | none |
| 9 | `copper storage disease[tiab]` | 25 | none |
| 10 | `copper storage diseases[tiab]` | 7 | none |
| 11 | `neurohepatic degeneration[tiab]` | 0 | warning: pubmed_warning; warning: zero_hits |
| 12 | `hepatocerebral degeneration[tiab]` | 142 | none |
| 13 | `westphal-strumpell[tiab]` | 26 | none |
| 14 | `ATP7B[tiab]` | 1,016 | none |
| 15 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14` | 7,600 | none |

### Strategy (single line, for copying into PubMed)

```text
((Hepatolenticular Degeneration[Mesh] OR wilson disease[tiab] OR wilson's disease[tiab] OR wilsons disease[tiab] OR hepatolenticular degeneration[tiab] OR hepatolenticular[tiab] OR progressive lenticular degeneration[tiab] OR kinnier-wilson[tiab] OR copper storage disease[tiab] OR copper storage diseases[tiab] OR neurohepatic degeneration[tiab] OR hepatocerebral degeneration[tiab] OR westphal-strumpell[tiab] OR ATP7B[tiab])) AND ("1800/01/01"[edat] : "2018/12/23"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 11 | 11 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Common pharmacologic anti-copper therapies | left out | 7,600 / 3,374 | 55.6% | none | 0/30 (up to 10% of removed records could be relevant) | The block cuts 55.6% of the condition-only set but only 11 screened relevant records sit in the base, below the minimum 15 needed to establish safety to AND. The 30-record loss sample found no eligible study, but that low-prevalence sample is weak reassurance. Leave treatment as a screening criterion to preserve recall. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Common pharmacologic anti-copper therapies | 1 | `disease*[tiab] OR disorder*[tiab] OR condition*[tiab]` | 3,329 | 0/30 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial disease block with drug-therapy block tested as an optional candidate; broad free-text and MeSH capture common chelator and zinc therapy terminology. |
| 2 | 0 | wilson_disease: +14 / -0 | none | Initial disease block with a candidate optional drug-therapy block; candidate covers chelators and zinc therapies using MeSH and title/abstract language. |
| 3 | 7,600 | limits/combination | none | Initial disease block with a candidate optional drug-therapy block; candidate covers chelators and zinc therapies using MeSH and title/abstract language. |
| 4 | 7,600 | wilson_disease: +0 / -1 | none | Removed the neurohepatic degeneration title/abstract phrase after its tested query returned zero hits and PubMed reported no items found; retained indexed Hepatolenticular Degeneration MeSH. Added five screened comparison or comparative-safety studies from related review neighbors; no known records lost. |
| 5 | 7,600 | wilson_disease: +1 / -0 | none | Retained the verified MeSH entry-term alias neurohepatic degeneration despite its zero-hit title/abstract query; translation was intact. Its future retrieval potential remains acceptable as a low-cost OR alternative, to be explicitly dispositioned by the internal critic. Restored the condition block used by the current optional decision and category probe; all 11 screened records remain retrieved. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5: 0 findings; 
- Round 2 on version 5: 0 findings; 
- Round 3 on version 5: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 297 NCBI requests logged (131 from cache); strategy sha256 959849d6957a._

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
        "query": "(neurohepatic degeneration[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
        "translation": "\"neurohepatic degeneration\"[Title/Abstract] AND 1800/01/01:2018/12/23[Date - Entry]",
        "location": "line:11",
        "blocking": false,
        "requires_review": true,
        "id": "I-0dc052b497be622868d6"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(neurohepatic degeneration[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
        "translation": "\"neurohepatic degeneration\"[Title/Abstract] AND 1800/01/01:2018/12/23[Date - Entry]",
        "location": "line:11",
        "blocking": false,
        "requires_review": true,
        "id": "I-5d7637afe677de153f63"
      }
    ],
    "issues": [
      {
        "severity": "warning",
        "code": "pubmed_warning",
        "message": "PubMed reported a warning; review the translation.",
        "evidence": "outputmessages: No items found.",
        "query": "(neurohepatic degeneration[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
        "translation": "\"neurohepatic degeneration\"[Title/Abstract] AND 1800/01/01:2018/12/23[Date - Entry]",
        "location": "line:11",
        "blocking": false,
        "requires_review": true,
        "id": "I-0dc052b497be622868d6"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(neurohepatic degeneration[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
        "translation": "\"neurohepatic degeneration\"[Title/Abstract] AND 1800/01/01:2018/12/23[Date - Entry]",
        "location": "line:11",
        "blocking": false,
        "requires_review": true,
        "id": "I-5d7637afe677de153f63"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Hepatolenticular Degeneration",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T14:23:01+00:00",
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
  "translation": "(\"hepatolenticular degeneration\"[MeSH Terms] OR \"wilson disease\"[Title/Abstract] OR \"wilson s disease\"[Title/Abstract] OR \"wilsons disease\"[Title/Abstract] OR \"hepatolenticular degeneration\"[Title/Abstract] OR \"hepatolenticular\"[Title/Abstract] OR \"progressive lenticular degeneration\"[Title/Abstract] OR \"kinnier-wilson\"[Title/Abstract] OR \"copper storage disease\"[Title/Abstract] OR \"copper storage diseases\"[Title/Abstract] OR \"neurohepatic degeneration\"[Title/Abstract] OR \"hepatocerebral degeneration\"[Title/Abstract] OR \"westphal-strumpell\"[Title/Abstract] OR \"ATP7B\"[Title/Abstract]) AND 1800/01/01:2018/12/23[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "d9a13c128a93d6e48c882b1dcabf7a7f1488662bc21991b6b6f51ffc6c9be431",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The reported PubMed translation preserves the Wilson disease terms and applies the entry-date range. The neurohepatic degeneration phrase translates literally; its zero-hit warning is dispositioned below."
        },
        "operators": {
          "verdict": "pass",
          "note": "The condition synonyms are ORed, and the condition block is ANDed with the stated date range. Leaving the optional therapy block out is supported by the low number of known relevant records and inconclusive loss sample."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Hepatolenticular Degeneration is verified in the packet as the relevant MeSH descriptor. No therapy heading is required because that optional block was left out."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The condition block includes disease names, variants, and ATP7B. The zero-hit phrase is retained with an accepted-risk disposition; its low yield alone does not establish redundancy."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query is parenthesized, has no reported syntax errors, and its PubMed translation is supplied."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date cutoff matches the stated as-of date. No language, age, or study-design limits were added; comparators and outcomes remain screening criteria."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-0dc052b497be622868d6",
          "status": "accepted-risk",
          "response": "Accept the PubMed warning as a zero-result diagnostic for this retained phrase. The packet provides no evidence that the term is redundant, and the warning alone is not a reason to remove a potentially useful synonym.",
          "evidence": "PubMed reports 'No items found.' The reported translation is the literal phrase neurohepatic degeneration[Title/Abstract]; the combined strategy has no translation blockers.",
          "query": "(neurohepatic degeneration[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
          "translation": "\"neurohepatic degeneration\"[Title/Abstract] AND 1800/01/01:2018/12/23[Date - Entry]"
        },
        {
          "issue_id": "I-5d7637afe677de153f63",
          "status": "accepted-risk",
          "response": "Accept the zero-hit warning for this phrase while retaining it. Its zero yield is documented, but deleting it solely on that basis is not warranted by the packet.",
          "evidence": "The term has 0 hits in the reported date range and translates as neurohepatic degeneration[Title/Abstract]. No translation blockers are reported.",
          "query": "(neurohepatic degeneration[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
          "translation": "\"neurohepatic degeneration\"[Title/Abstract] AND 1800/01/01:2018/12/23[Date - Entry]"
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "d9a13c128a93d6e48c882b1dcabf7a7f1488662bc21991b6b6f51ffc6c9be431",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The reported translation preserves the Wilson disease terms and applies the entry-date range. The neurohepatic degeneration phrase translates literally; its zero-result warnings are dispositioned below."
        },
        "operators": {
          "verdict": "pass",
          "note": "Condition synonyms are ORed. The optional therapy block was tested and left out; the packet documents the limited known set and low-prevalence loss sample as insufficient evidence to require it."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies Hepatolenticular Degeneration as the relevant MeSH descriptor. No therapy heading is required for the chosen condition-only strategy."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The condition block includes disease names and variants, plus ATP7B. The zero-hit synonym is retained with a documented risk disposition; its low yield alone does not establish redundancy."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query is parenthesized, has no reported syntax errors or translation blockers, and its PubMed translation is supplied."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date cutoff matches the stated as-of date. No language, age, or study-design limits were added; comparators and outcomes remain screening criteria."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-0dc052b497be622868d6",
          "status": "accepted-risk",
          "response": "Accept the warning as a zero-result diagnostic for this retained phrase. The packet shows that the phrase is translated literally and reports no phrase-translation anomaly. The warning alone does not establish that the synonym is redundant.",
          "evidence": "PubMed reports 'No items found.' The reported translation is neurohepatic degeneration[Title/Abstract]; phrasesignored and quotedphrasesnotfound are empty.",
          "query": "(neurohepatic degeneration[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
          "translation": "\"neurohepatic degeneration\"[Title/Abstract] AND 1800/01/01:2018/12/23[Date - Entry]"
        },
        {
          "issue_id": "I-5d7637afe677de153f63",
          "status": "accepted-risk",
          "response": "Accept the zero-hit warning while retaining the phrase. Its zero yield is documented, but the packet gives no evidence that it is redundant, so deleting it on yield alone is not warranted.",
          "evidence": "The term has 0 hits in the reported date range and translates as neurohepatic degeneration[Title/Abstract]. The combined strategy has no reported translation blockers.",
          "query": "(neurohepatic degeneration[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
          "translation": "\"neurohepatic degeneration\"[Title/Abstract] AND 1800/01/01:2018/12/23[Date - Entry]"
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 5,
      "review_sha256": "d9a13c128a93d6e48c882b1dcabf7a7f1488662bc21991b6b6f51ffc6c9be431",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The reported PubMed translation preserves the condition terms and applies the entry-date range. The neurohepatic degeneration phrase translates literally, with no phrase translation anomaly reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "Condition synonyms are ORed, and the condition block is combined with the date range. The optional therapy block remains excluded based on the documented testing and limited evidence for safely requiring it."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet identifies Hepatolenticular Degeneration as the relevant MeSH descriptor. No therapy heading is required for the chosen condition-only strategy."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The condition block includes disease names, variants, and ATP7B. The zero-hit phrase is retained with an explicit risk disposition; its yield alone does not establish redundancy."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query is parenthesized, and the packet reports no syntax errors or translation blockers."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date cutoff matches the stated as-of date. No language, age, or study-design limits were added; comparators and outcomes remain screening criteria."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-0dc052b497be622868d6",
          "status": "accepted-risk",
          "response": "Accept the PubMed warning as a zero-result diagnostic for this retained phrase. The warning does not establish that the synonym is redundant, and the packet provides no basis to remove it.",
          "evidence": "PubMed reports no items found. The phrase translates literally as neurohepatic degeneration[Title/Abstract], with no phrase translation anomaly reported.",
          "query": "(neurohepatic degeneration[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
          "translation": "\"neurohepatic degeneration\"[Title/Abstract] AND 1800/01/01:2018/12/23[Date - Entry]"
        },
        {
          "issue_id": "I-5d7637afe677de153f63",
          "status": "accepted-risk",
          "response": "Accept the zero-hit warning while retaining the phrase. Its zero yield is documented, but the packet provides no evidence of redundancy, so yield alone does not warrant deletion.",
          "evidence": "The term has 0 hits in the reported date range and translates as neurohepatic degeneration[Title/Abstract]. The combined strategy has no reported translation blockers.",
          "query": "(neurohepatic degeneration[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
          "translation": "\"neurohepatic degeneration\"[Title/Abstract] AND 1800/01/01:2018/12/23[Date - Entry]"
        }
      ]
    }
  ]
}
```

