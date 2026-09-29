# PubMed search strategy: audit

Generated 2026-09-29T00:31:03+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Immune checkpoint inhibitors plus chemotherapy for early triple-negative breast cancer
- Framework: PICO
- Scope confirmed by user: yes (User asked to proceed without questions. Assumed PICO intervention-effectiveness scope. No known relevant records supplied; no workload limit beyond the standard default (10,000). Early-stage status and chemotherapy co-treatment will be screened rather than required Boolean blocks for recall. No language, age, publication-date, or design limits. PubMed Entrez-date bound supplied by PSB_AS_OF=2025-01-31 on every command.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Triple-negative breast cancer | search | The target population is named by a recognized disease subtype; early stage is retained for screening because stage is variably explicit in abstracts. |
| Immune checkpoint inhibitors | search | The intervention class is central and identifiable, but studies may name only the individual agent. |
| Chemotherapy co-treatment | screen | Combination eligibility is assessed at screening; requiring a chemotherapy block could miss records whose abstracts describe individual regimens or do not state the co-treatment clearly. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T00:30:11+00:00
- Records added to PubMed up to: 2025-01-31
- Total records: 2,870
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Triple Negative Breast Neoplasms"[Mesh]` | 12,839 | none |
| 2 | `"Breast Neoplasms"[Mesh]` | 365,448 | none |
| 3 | `"triple negative"[tiab]` | 27,452 | none |
| 4 | `"triple-negative"[tiab]` | 27,452 | none |
| 5 | `TNBC[tiab]` | 14,325 | none |
| 6 | `TNBCs[tiab]` | 1,409 | none |
| 7 | `"ER-negative"[tiab]` | 4,225 | none |
| 8 | `"ER negative"[tiab]` | 4,225 | none |
| 9 | `"estrogen receptor-negative"[tiab]` | 2,076 | none |
| 10 | `"estrogen receptor negative"[tiab]` | 2,076 | none |
| 11 | `"hormone receptor-negative"[tiab]` | 947 | none |
| 12 | `"hormone receptor negative"[tiab]` | 947 | none |
| 13 | `"basal-like"[tiab]` | 3,680 | none |
| 14 | `"basal like"[tiab]` | 3,680 | none |
| 15 | `("HER2-negative"[tiab] AND "triple negative"[tiab])` | 1,124 | none |
| 16 | `("HER2 negative"[tiab] AND "ER-negative"[tiab])` | 289 | none |
| 17 | `("HER2 negative"[tiab] AND "ER negative"[tiab])` | 289 | none |
| 18 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17` | 376,232 | none |
| 19 | `"Nivolumab"[Mesh]` | 6,195 | none |
| 20 | `"Ipilimumab"[Mesh]` | 3,337 | none |
| 21 | `"immune checkpoint inhibitor"[tiab]` | 11,408 | none |
| 22 | `"immune checkpoint inhibitors"[tiab]` | 26,070 | none |
| 23 | `"checkpoint inhibitor"[tiab]` | 14,089 | none |
| 24 | `"checkpoint inhibitors"[tiab]` | 30,466 | none |
| 25 | `"checkpoint blockade"[tiab]` | 9,914 | none |
| 26 | `"checkpoint blocking"[tiab]` | 298 | none |
| 27 | `pembrolizumab[tiab]` | 10,643 | none |
| 28 | `atezolizumab[tiab]` | 3,887 | none |
| 29 | `nivolumab[tiab]` | 10,825 | none |
| 30 | `durvalumab[tiab]` | 2,047 | none |
| 31 | `avelumab[tiab]` | 1,130 | none |
| 32 | `cemiplimab[tiab]` | 535 | none |
| 33 | `ipilimumab[tiab]` | 5,698 | none |
| 34 | `tislelizumab[tiab]` | 469 | none |
| 35 | `toripalimab[tiab]` | 396 | none |
| 36 | `sintilimab[tiab]` | 721 | none |
| 37 | `camrelizumab[tiab]` | 793 | none |
| 38 | `dostarlimab[tiab]` | 172 | none |
| 39 | `retifanlimab[tiab]` | 23 | none |
| 40 | `spartalizumab[tiab]` | 42 | none |
| 41 | `envafolimab[tiab]` | 31 | none |
| 42 | `("PD-1"[tiab] AND (block*[tiab] OR inhibit*[tiab] OR antibod*[tiab]))` | 27,079 | none |
| 43 | `("PD-L1"[tiab] AND (block*[tiab] OR inhibit*[tiab] OR antibod*[tiab]))` | 23,252 | none |
| 44 | `("CTLA-4"[tiab] AND (block*[tiab] OR inhibit*[tiab] OR antibod*[tiab]))` | 8,271 | none |
| 45 | `#19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44` | 81,271 | none |
| 46 | `#18 AND #45` | 2,870 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Triple Negative Breast Neoplasms"[Mesh] OR "Breast Neoplasms"[Mesh] OR "triple negative"[tiab] OR "triple-negative"[tiab] OR TNBC[tiab] OR TNBCs[tiab] OR "ER-negative"[tiab] OR "ER negative"[tiab] OR "estrogen receptor-negative"[tiab] OR "estrogen receptor negative"[tiab] OR "hormone receptor-negative"[tiab] OR "hormone receptor negative"[tiab] OR "basal-like"[tiab] OR "basal like"[tiab] OR ("HER2-negative"[tiab] AND "triple negative"[tiab]) OR ("HER2 negative"[tiab] AND "ER-negative"[tiab]) OR ("HER2 negative"[tiab] AND "ER negative"[tiab])) AND ("Nivolumab"[Mesh] OR "Ipilimumab"[Mesh] OR "immune checkpoint inhibitor"[tiab] OR "immune checkpoint inhibitors"[tiab] OR "checkpoint inhibitor"[tiab] OR "checkpoint inhibitors"[tiab] OR "checkpoint blockade"[tiab] OR "checkpoint blocking"[tiab] OR pembrolizumab[tiab] OR atezolizumab[tiab] OR nivolumab[tiab] OR durvalumab[tiab] OR avelumab[tiab] OR cemiplimab[tiab] OR ipilimumab[tiab] OR tislelizumab[tiab] OR toripalimab[tiab] OR sintilimab[tiab] OR camrelizumab[tiab] OR dostarlimab[tiab] OR retifanlimab[tiab] OR spartalizumab[tiab] OR envafolimab[tiab] OR ("PD-1"[tiab] AND (block*[tiab] OR inhibit*[tiab] OR antibod*[tiab])) OR ("PD-L1"[tiab] AND (block*[tiab] OR inhibit*[tiab] OR antibod*[tiab])) OR ("CTLA-4"[tiab] AND (block*[tiab] OR inhibit*[tiab] OR antibod*[tiab])))) AND ("1800/01/01"[edat] : "2025/01/31"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Immune checkpoint inhibitors | 1 | `immunotherapy[tiab] OR immunotherapies[tiab] OR monoclonal antibody[tiab] OR monoclonal antibodies[tiab] OR immune[tiab]` | 16,228 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| tnbc | 81,271 | 0 |
| ici | 376,232 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 2,904 | initial | none | Initial PICO draft: TNBC population AND immune checkpoint inhibitor blocks; early stage and chemotherapy co-treatment screened per scope assumptions. Broad breast cancer indexing retained for high recall; ICI agent names cover records that do not use class terminology. |
| 2 | 2,870 | ici: +0 / -1 | none | Removed the ambiguous Immune Checkpoint Inhibitors heading after live authority verification returned duplicate descriptor records; retained verified individual-drug MeSH headings and broad text terms. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 0 findings; 
- Round 2 on version 2: 0 findings; 
- Round 3 on version 2: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 566 NCBI requests logged (251 from cache); strategy sha256 d8a9afbadbb9._

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
      "requested": "Triple Negative Breast Neoplasms",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:30:11+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D064726",
          "name": "Triple Negative Breast Neoplasms",
          "type": "descriptor",
          "scope_note": "Breast neoplasms that do not express ESTROGEN RECEPTORS; PROGESTERONE RECEPTORS; and do not overexpress the NEU RECEPTOR/HER-2 PROTO-ONCOGENE PROTEIN.",
          "tree_numbers": [
            "C04.588.180.788",
            "C17.800.090.500.788"
          ],
          "entry_terms": 14,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D064726",
      "preferred_label": "Triple Negative Breast Neoplasms",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"Triple Negative Breast Neoplasms\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Breast Neoplasms",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:30:11+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001943",
          "name": "Breast Neoplasms",
          "type": "descriptor",
          "scope_note": "Tumors or cancer of the human BREAST.",
          "tree_numbers": [
            "C04.588.180",
            "C17.800.090.500"
          ],
          "entry_terms": 37,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001943",
      "preferred_label": "Breast Neoplasms",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Breast Neoplasms\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Nivolumab",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:30:11+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000077594",
          "name": "Nivolumab",
          "type": "descriptor",
          "scope_note": "A genetically engineered, fully humanized immunoglobulin G4 monoclonal antibody that binds to the PD-1 RECEPTOR, activating an immune response to tumor cells. It is used as monotherapy or in combination with IPILIMUMAB for the treatment of advanced malignant MELANOMA. It is also used in the treatment of advanced or recurring NON-SMALL CELL LUNG CANCER; RENAL CELL CARCINOMA; and HODGKIN'S LYMPHOMA.",
          "tree_numbers": [
            "D12.776.124.486.485.114.224.060.829",
            "D12.776.124.790.651.114.224.060.829",
            "D12.776.377.715.548.114.224.200.829"
          ],
          "entry_terms": 10,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000077594",
      "preferred_label": "Nivolumab",
      "type": "descriptor",
      "location": "vocabulary:21",
      "term": {
        "text": "\"Nivolumab\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Ipilimumab",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:30:11+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000074324",
          "name": "Ipilimumab",
          "type": "descriptor",
          "scope_note": "An anti-CTLA-4 ANTIGEN monoclonal antibody initially indicated for the treatment of certain types of metastatic MELANOMA. Its mode of actions may include blocking of CTLA-4 mediated inhibition of CYTOTOXIC T LYMPHOCYTES, allowing for more efficient destruction of target tumor cells.",
          "tree_numbers": [
            "D12.776.124.486.485.114.224.060.798",
            "D12.776.124.790.651.114.224.060.798",
            "D12.776.377.715.548.114.224.200.798"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000074324",
      "preferred_label": "Ipilimumab",
      "type": "descriptor",
      "location": "vocabulary:22",
      "term": {
        "text": "\"Ipilimumab\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Triple Negative Breast Neoplasms\"[MeSH Terms] OR \"Breast Neoplasms\"[MeSH Terms] OR \"triple-negative\"[Title/Abstract] OR \"triple-negative\"[Title/Abstract] OR \"TNBC\"[Title/Abstract] OR \"TNBCs\"[Title/Abstract] OR \"er negative\"[Title/Abstract] OR \"er negative\"[Title/Abstract] OR \"estrogen receptor-negative\"[Title/Abstract] OR \"estrogen receptor-negative\"[Title/Abstract] OR \"hormone receptor-negative\"[Title/Abstract] OR \"hormone receptor-negative\"[Title/Abstract] OR \"basal-like\"[Title/Abstract] OR \"basal-like\"[Title/Abstract] OR (\"her2 negative\"[Title/Abstract] AND \"triple-negative\"[Title/Abstract]) OR (\"her2 negative\"[Title/Abstract] AND \"er negative\"[Title/Abstract]) OR (\"her2 negative\"[Title/Abstract] AND \"er negative\"[Title/Abstract])) AND (\"Nivolumab\"[MeSH Terms] OR \"Ipilimumab\"[MeSH Terms] OR \"immune checkpoint inhibitor\"[Title/Abstract] OR \"immune checkpoint inhibitors\"[Title/Abstract] OR \"checkpoint inhibitor\"[Title/Abstract] OR \"checkpoint inhibitors\"[Title/Abstract] OR \"checkpoint blockade\"[Title/Abstract] OR \"checkpoint blocking\"[Title/Abstract] OR \"pembrolizumab\"[Title/Abstract] OR \"atezolizumab\"[Title/Abstract] OR \"Nivolumab\"[Title/Abstract] OR \"durvalumab\"[Title/Abstract] OR \"avelumab\"[Title/Abstract] OR \"cemiplimab\"[Title/Abstract] OR \"Ipilimumab\"[Title/Abstract] OR \"tislelizumab\"[Title/Abstract] OR \"toripalimab\"[Title/Abstract] OR \"sintilimab\"[Title/Abstract] OR \"camrelizumab\"[Title/Abstract] OR \"dostarlimab\"[Title/Abstract] OR \"retifanlimab\"[Title/Abstract] OR \"spartalizumab\"[Title/Abstract] OR \"envafolimab\"[Title/Abstract] OR (\"PD-1\"[Title/Abstract] AND (\"block*\"[Title/Abstract] OR \"inhibit*\"[Title/Abstract] OR \"antibod*\"[Title/Abstract])) OR (\"PD-L1\"[Title/Abstract] AND (\"block*\"[Title/Abstract] OR \"inhibit*\"[Title/Abstract] OR \"antibod*\"[Title/Abstract])) OR (\"CTLA-4\"[Title/Abstract] AND (\"block*\"[Title/Abstract] OR \"inhibit*\"[Title/Abstract] OR \"antibod*\"[Title/Abstract]))) AND 1800/01/01:2025/01/31[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "cd3dc14235b80a3871f043490b73ab624f9d3077bf90e9d4a9848196297c8897",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched concepts have bare disease and intervention terms, including TNBC, ER-negative, individual checkpoint agents, and checkpoint-inhibitor wording. Early stage and chemotherapy co-treatment are retained for screening under the stated scope."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are OR-ed within each block and the searched concepts are AND-ed. Chemotherapy is not a required block, consistent with the protocol rationale."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the selected MeSH headings, and disease and agent headings are combined with text-word coverage. The broad Breast Neoplasms heading may add records, but subtype eligibility is screened."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes disease-subtype wording, abbreviations, receptor-status variants, checkpoint-class wording, individual agents, and target-based expressions. The category probe found no relevant records among 30 screened outside the intervention block."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No lint, translation, or PubMed syntax issues were reported; the translated expressions preserve the intended Boolean structure."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, publication-date, or design limits are applied. The Entrez-date bound through 2025-01-31 is stated and consistently applied."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "cd3dc14235b80a3871f043490b73ab624f9d3077bf90e9d4a9848196297c8897",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Both searched concepts have bare disease or intervention terms alongside headings, abbreviations, receptor-status wording, checkpoint-class wording, and individual agents. Early stage and chemotherapy co-treatment remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are OR-ed within blocks, and the disease and intervention blocks are AND-ed. Chemotherapy is not required as a Boolean block, consistent with the protocol rationale."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the selected MeSH headings, which are accompanied by text-word terms. The broad Breast Neoplasms heading may increase screening volume; subtype eligibility is screened."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The blocks include subtype wording, abbreviations, receptor-status variants, checkpoint-class terms, individual agents, and target-based expressions. The category probe found no eligible records among the 30 screened outside the intervention block."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint, translation, PubMed syntax, or diagnostic issues. The translations preserve the intended Boolean structure."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, publication-date, or design limits are applied. The Entrez-date bound through 2025-01-31 is documented and applied consistently."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 2,
      "review_sha256": "cd3dc14235b80a3871f043490b73ab624f9d3077bf90e9d4a9848196297c8897",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Both searched concepts have bare text-word terms and additional headings or variants. Early stage and chemotherapy co-treatment remain screening criteria as specified."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are OR-ed within each block, and disease and intervention blocks are AND-ed. Chemotherapy is not a required Boolean block, consistent with the protocol rationale."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the selected MeSH headings, accompanied by text-word coverage. The broader Breast Neoplasms heading may increase screening volume; subtype eligibility is screened."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The blocks include TNBC subtype wording, abbreviations, receptor-status variants, checkpoint-class wording, individual agents, and target-based expressions. The category probe found no eligible records among 30 screened outside the intervention block."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint, translation, PubMed syntax, or diagnostic issues. The translations preserve the intended Boolean structure."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, publication-date, or design limits are applied. The Entrez-date bound through 2025-01-31 is documented and applied consistently."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```

