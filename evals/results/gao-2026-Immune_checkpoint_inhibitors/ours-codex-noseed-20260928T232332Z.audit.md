# PubMed search strategy: audit

Generated 2026-09-28T23:48:06+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Immune checkpoint inhibitors plus chemotherapy for early triple-negative breast cancer
- Framework: PICO
- Scope confirmed by user: yes (User requested no questions and asked to proceed; scope treated as confirmed for this run. Assumed early means non-metastatic stage I-III disease in neoadjuvant, adjuvant, or perioperative treatment; no language, publication-date, age, or design limits. The PSB_AS_OF environment is set to 2025-01-31 for every command to bound PubMed entry date; no publication-date limit is used. No known relevant records were supplied. The chemotherapy combination is tested as optional because its wording may not always be searchable; stage is screened. At standard depth, discovery candidates will be screened up to about 150 records.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Triple-negative breast cancer | search | The target population is explicitly TNBC and is named in titles, abstracts, and indexing; early stage is screened because stage and treatment setting may not be named consistently. |
| Immune checkpoint inhibitors | search | The intervention class is required; relevant records may name individual agents rather than the class, so include drug members and probe the category. |
| Chemotherapy co-administered with an immune checkpoint inhibitor | optional | Combination therapy defines eligibility, but chemotherapy wording may be inconsistently surfaced in abstracts and records can name regimen components; test an explicit block before deciding whether to require it. |
| Early-stage / non-metastatic disease | screen | Early stage is an eligibility facet with variable naming and staging; screen it rather than requiring a stage block. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T23:47:22+00:00
- Records added to PubMed up to: 2025-01-31
- Total records: 2,029
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Triple Negative Breast Neoplasms"[Mesh]` | 12,839 | none |
| 2 | `"triple negative breast cancer"[tiab]` | 19,872 | none |
| 3 | `"triple-negative breast cancer"[tiab]` | 19,872 | none |
| 4 | `"triple negative breast neoplasm"[tiab]` | 12 | none |
| 5 | `"triple-negative breast neoplasm"[tiab]` | 12 | none |
| 6 | `TNBC[tiab]` | 14,325 | none |
| 7 | `TNBCs[tiab]` | 1,409 | none |
| 8 | `"ER-negative PR-negative HER2-negative breast cancer"[tiab]` | 2 | none |
| 9 | `"ER negative PR negative HER2 negative breast cancer"[tiab]` | 2 | none |
| 10 | `"ER-/PR-/HER2-"[tiab]` | 1,006 | none |
| 11 | `"triple negative"[tiab:~2]` | 27,591 | none |
| 12 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11` | 29,199 | none |
| 13 | `"Programmed Cell Death 1 Receptor"[Mesh]` | 13,795 | none |
| 14 | `"B7-H1 Antigen"[Mesh]` | 16,562 | none |
| 15 | `"immune checkpoint inhibitor"[tiab]` | 11,408 | none |
| 16 | `"immune checkpoint inhibitors"[tiab]` | 26,070 | none |
| 17 | `"checkpoint inhibitor"[tiab]` | 14,089 | none |
| 18 | `"checkpoint inhibitors"[tiab]` | 30,466 | none |
| 19 | `"checkpoint blockade"[tiab]` | 9,914 | none |
| 20 | `"immune checkpoint blockade"[tiab]` | 7,628 | none |
| 21 | `"PD-1 inhibitor"[tiab]` | 2,152 | none |
| 22 | `"PD-1 inhibitors"[tiab]` | 1,928 | none |
| 23 | `"PD-L1 inhibitor"[tiab]` | 1,111 | none |
| 24 | `"PD-L1 inhibitors"[tiab]` | 1,923 | none |
| 25 | `"PD1 inhibitor"[tiab]` | 106 | none |
| 26 | `"PDL1 inhibitor"[tiab]` | 22 | none |
| 27 | `"programmed death-1"[tiab]` | 5,303 | none |
| 28 | `"programmed death-ligand 1"[tiab]` | 9,018 | none |
| 29 | `"programmed cell death protein 1"[tiab]` | 5,001 | none |
| 30 | `"anti-PD-1"[tiab]` | 10,138 | none |
| 31 | `"anti-PD-L1"[tiab]` | 3,796 | none |
| 32 | `pembrolizumab[tiab]` | 10,643 | none |
| 33 | `atezolizumab[tiab]` | 3,887 | none |
| 34 | `durvalumab[tiab]` | 2,047 | none |
| 35 | `nivolumab[tiab]` | 10,825 | none |
| 36 | `avelumab[tiab]` | 1,130 | none |
| 37 | `cemiplimab[tiab]` | 535 | none |
| 38 | `ipilimumab[tiab]` | 5,698 | none |
| 39 | `#13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38` | 83,590 | none |
| 40 | `#12 AND #39` | 2,029 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Triple Negative Breast Neoplasms"[Mesh] OR "triple negative breast cancer"[tiab] OR "triple-negative breast cancer"[tiab] OR "triple negative breast neoplasm"[tiab] OR "triple-negative breast neoplasm"[tiab] OR TNBC[tiab] OR TNBCs[tiab] OR "ER-negative PR-negative HER2-negative breast cancer"[tiab] OR "ER negative PR negative HER2 negative breast cancer"[tiab] OR "ER-/PR-/HER2-"[tiab] OR "triple negative"[tiab:~2]) AND ("Programmed Cell Death 1 Receptor"[Mesh] OR "B7-H1 Antigen"[Mesh] OR "immune checkpoint inhibitor"[tiab] OR "immune checkpoint inhibitors"[tiab] OR "checkpoint inhibitor"[tiab] OR "checkpoint inhibitors"[tiab] OR "checkpoint blockade"[tiab] OR "immune checkpoint blockade"[tiab] OR "PD-1 inhibitor"[tiab] OR "PD-1 inhibitors"[tiab] OR "PD-L1 inhibitor"[tiab] OR "PD-L1 inhibitors"[tiab] OR "PD1 inhibitor"[tiab] OR "PDL1 inhibitor"[tiab] OR "programmed death-1"[tiab] OR "programmed death-ligand 1"[tiab] OR "programmed cell death protein 1"[tiab] OR "anti-PD-1"[tiab] OR "anti-PD-L1"[tiab] OR pembrolizumab[tiab] OR atezolizumab[tiab] OR durvalumab[tiab] OR nivolumab[tiab] OR avelumab[tiab] OR cemiplimab[tiab] OR ipilimumab[tiab])) AND ("1800/01/01"[edat] : "2025/01/31"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 6 | 6 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Chemotherapy co-administered with an immune checkpoint inhibitor | left out | 2,029 / 1,093 | 46.1% | none | 0/30 (up to 10% of removed records could be relevant) | Keep chemotherapy out of the required AND structure to protect recall. The 0/30 loss sample leaves material uncertainty across 936 records removed, and searching without this block returns 2,029 records, below the 10,000-record workload budget. Screen chemotherapy co-administration at eligibility. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Immune checkpoint inhibitors | 1 | `immunotherap*[tiab] OR immunomodulat*[tiab] OR monoclonal antibod*[tiab] OR PD-1[tiab] OR PD-L1[tiab] OR CTLA-4[tiab]` | 737 | 0/30 |
| Immune checkpoint inhibitors | 2 | `immunotherap*[tiab] OR immunomodulat*[tiab] OR monoclonal antibod*[tiab] OR PD-1[tiab] OR PD-L1[tiab] OR CTLA-4[tiab]` | 1,769 | 0/30 |
| Chemotherapy co-administered with an immune checkpoint inhibitor | 1 | `antineoplastic agent*[tiab] OR cytotoxic therap*[tiab] OR platinum-based[tiab] OR taxane-based[tiab] OR anthracycline-based[tiab] OR drug regimen*[tiab] OR cytotoxic agent*[tiab]` | 0 | 0/0 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| tnbc | 83,590 | 0 |
| ici | 29,199 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial high-sensitivity strategy from scope and MeSH/free-text vocabulary; required TNBC and ICI blocks, with chemotherapy combination tested as optional. Benchmark came from screened included studies cited by matching prior reviews; no seeds were supplied. |
| 2 | 2,134 | tnbc: +0 / -1 | none | Replaced typographic minus glyphs in receptor-status text with ASCII hyphens after lint blocked evaluation; no concept change. |
| 3 | 2,029 | ici: +0 / -3 | none | Removed ambiguous duplicate NCBI authority results for Immune Checkpoint Inhibitors and Antineoplastic Agents, Immunological and retained the verified PD-1 receptor and B7-H1 descriptors; removed duplicate receptor-status text term. This avoids unverified descriptor labels while preserving broad text and agent terms. |
| 4 | 1,093 | chemotherapy: +16 / -0 | none | Moved the tested chemotherapy block into the required query after 0/30 relevant in the loss sample, 0 benchmark losses, and a 46.6% reduction. This version preserves all six benchmark records. |
| 5 | 2,029 | chemotherapy: +0 / -16 | none | Moved chemotherapy back out of the required AND structure after critic review: 0/30 removed records does not establish low enough risk across 936 removed records, while the broader 2,029-record query is within the 10,000-record workload budget. Chemotherapy co-administration remains an eligibility screening criterion. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 1 findings; R1-F1 should-fix open
- Round 2 on version 4: 2 findings; R1-F1 should-fix resolved, R2-F1 should-fix open
- Round 3 on version 5: 2 findings; R1-F1 should-fix resolved, R2-F1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1044 NCBI requests logged (692 from cache); strategy sha256 428c2dd8a3b2._

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
      "checked_at": "2026-09-28T23:47:22+00:00",
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
      "requested": "Programmed Cell Death 1 Receptor",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:47:22+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D061026",
          "name": "Programmed Cell Death 1 Receptor",
          "type": "descriptor",
          "scope_note": "An inhibitory T-lymphocyte receptor that has specificity for CD274 ANTIGEN and PROGRAMMED CELL DEATH 1 LIGAND 2 PROTEIN. Signaling by the receptor limits T cell proliferation and INTERFERON GAMMA synthesis. The receptor also may play an essential role in the regulatory pathway that induces PERIPHERAL TOLERANCE.",
          "tree_numbers": [
            "D12.776.465.844",
            "D12.776.543.750.705.222.875",
            "D23.050.301.264.894.790",
            "D23.101.100.894.790"
          ],
          "entry_terms": 13,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D061026",
      "preferred_label": "Programmed Cell Death 1 Receptor",
      "type": "descriptor",
      "location": "vocabulary:12",
      "term": {
        "text": "\"Programmed Cell Death 1 Receptor\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "B7-H1 Antigen",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:47:22+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D060890",
          "name": "B7-H1 Antigen",
          "type": "descriptor",
          "scope_note": "An inhibitory B7 antigen that contains V-type and C2 type immunoglobulin domains. It has specificity for the T-CELL receptor PROGRAMMED CELL DEATH 1 PROTEIN and provides negative signals that control and inhibit T-cell responses. It is found at higher than normal levels on tumor cells, suggesting its potential role in TUMOR IMMUNE EVASION.",
          "tree_numbers": [
            "D12.776.465.625",
            "D12.776.467.150.300",
            "D12.776.543.095.300",
            "D23.050.301.285.400",
            "D23.529.168.300"
          ],
          "entry_terms": 17,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D060890",
      "preferred_label": "B7-H1 Antigen",
      "type": "descriptor",
      "location": "vocabulary:13",
      "term": {
        "text": "\"B7-H1 Antigen\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Triple Negative Breast Neoplasms\"[MeSH Terms] OR \"triple-negative breast cancer\"[Title/Abstract] OR \"triple-negative breast cancer\"[Title/Abstract] OR \"triple-negative breast neoplasm\"[Title/Abstract] OR \"triple-negative breast neoplasm\"[Title/Abstract] OR \"TNBC\"[Title/Abstract] OR \"TNBCs\"[Title/Abstract] OR \"er negative pr negative her2 negative breast cancer\"[Title/Abstract] OR \"er negative pr negative her2 negative breast cancer\"[Title/Abstract] OR \"er pr her2\"[Title/Abstract] OR \"triple negative\"[Title/Abstract:~2]) AND (\"Programmed Cell Death 1 Receptor\"[MeSH Terms] OR \"B7-H1 Antigen\"[MeSH Terms] OR \"immune checkpoint inhibitor\"[Title/Abstract] OR \"immune checkpoint inhibitors\"[Title/Abstract] OR \"checkpoint inhibitor\"[Title/Abstract] OR \"checkpoint inhibitors\"[Title/Abstract] OR \"checkpoint blockade\"[Title/Abstract] OR \"immune checkpoint blockade\"[Title/Abstract] OR \"PD-1 inhibitor\"[Title/Abstract] OR \"PD-1 inhibitors\"[Title/Abstract] OR \"PD-L1 inhibitor\"[Title/Abstract] OR \"PD-L1 inhibitors\"[Title/Abstract] OR \"PD1 inhibitor\"[Title/Abstract] OR \"PDL1 inhibitor\"[Title/Abstract] OR \"programmed death-1\"[Title/Abstract] OR \"programmed death-ligand 1\"[Title/Abstract] OR \"programmed cell death protein 1\"[Title/Abstract] OR \"anti-PD-1\"[Title/Abstract] OR \"anti-PD-L1\"[Title/Abstract] OR \"pembrolizumab\"[Title/Abstract] OR \"atezolizumab\"[Title/Abstract] OR \"durvalumab\"[Title/Abstract] OR \"nivolumab\"[Title/Abstract] OR \"avelumab\"[Title/Abstract] OR \"cemiplimab\"[Title/Abstract] OR \"ipilimumab\"[Title/Abstract]) AND 1800/01/01:2025/01/31[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "9e19c7863d2a5c6ec8bdb13cb79a74f4e28c36d821dd31bca5a9a1a207d52ffa",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The TNBC and ICI blocks include controlled headings and relevant text words; bare names are present for the listed drug agents. The chemotherapy block includes broad terms and regimen-class wording. No phrase warnings or translation issues are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three searched concepts are OR-combined within blocks and AND-combined across blocks. The optional chemotherapy block was tested, and the reported loss sample found no eligible records among 30 screened."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The included MeSH descriptors are verified in the packet and align with TNBC, PD-1/PD-L1, and chemotherapy concepts."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text-word coverage includes TNBC variants, checkpoint terminology and named agents, plus chemotherapy and regimen terms. The category probe found no relevant record among 30 screened outside the ICI block."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query translation is shown, with no PubMed errors, warnings, translation issues, or syntax issues reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, design, or publication-date limit is applied. The entry-date range through 2025-01-31 matches the stated as-of boundary."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The optional-block decision rationale says the chemotherapy block reduced the count by 46.6%, while the evidence reports 2,029 records without the block and 1,093 with it, a reduction of about 46.1%.",
          "recommendation": "Correct the decision rationale and any repeated summary to 46.1%, or document the basis for a different calculation.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "c96fe2755b9912df0c87bbb838434f5662a032e492075f90f7c740d9fb34c1aa",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The blocks cover the named drug agents with bare names and include TNBC variants, checkpoint terminology, and chemotherapy or regimen terms. No translation issues or phrase warnings are reported."
        },
        "operators": {
          "verdict": "revise",
          "note": "The optional chemotherapy block is AND-ed despite the protocol's concern that chemotherapy wording may be inconsistently surfaced. The 0/30 loss sample still allows up to 10% of removed records to be relevant, and the 2,029-record search without the block is within the 10,000-record workload budget."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the TNBC, PD-1 receptor, B7-H1 antigen, and chemotherapy descriptors used in the strategy."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text-word coverage includes TNBC forms, checkpoint terms and named agents, and chemotherapy and regimen terms. The ICI category probe found no relevant record in its 30-record sample outside the block."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final PubMed translation is provided, with no reported errors, warnings, translation issues, or syntax issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date boundary through 2025-01-31 matches the stated as-of date. No language, age, design, or publication-date limit is applied."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The earlier discrepancy between the stated 46.6% reduction and the counts has been corrected; the current rationale reports 46.1%, consistent with 2,029 records without the block and 1,093 with it.",
          "recommendation": "No further change needed for this finding.",
          "status": "resolved",
          "response": "The current optional-block rationale reports 46.1%, resolving the earlier discrepancy."
        },
        {
          "id": "R2-F1",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The chemotherapy concept was designated optional because its wording may be inconsistently surfaced, but it is AND-ed into the final strategy. The 0/30 loss sample is compatible with up to 10% of the 936 removed records being relevant, and the 2,029-record query without this block remains within the 10,000-record workload budget.",
          "recommendation": "Keep chemotherapy out of the required AND structure and screen for co-administration, or provide stronger evidence that requiring this block does not miss eligible studies.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 5,
      "review_sha256": "b4d9146c89d323e4cabcef967f94623a6ec056d3a12f6f787d416ea84e074ae6",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The TNBC and ICI blocks include controlled headings, text-word variants, and bare names for the listed agents. No translation issues or phrase warnings are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The final strategy OR-combines terms within the TNBC and ICI blocks and AND-combines those blocks. Chemotherapy is left out of the required structure; the 2,029-record search is within the 10,000-record workload budget, and co-administration is screened at eligibility."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the TNBC, PD-1 receptor, and B7-H1 antigen descriptors used in the strategy."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes TNBC variants, checkpoint terminology, and bare names for the listed agents. The category probes found no relevant records in the screened samples outside the ICI block."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query translation is provided, with no reported PubMed errors, warnings, translation issues, or syntax issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date boundary through 2025-01-31 matches the stated as-of date. No language, age, design, or publication-date limit is applied."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The earlier discrepancy between the stated 46.6% reduction and the counts has been corrected; the current rationale reports 46.1%, consistent with 2,029 records without the block and 1,093 with it.",
          "recommendation": "No further change needed for this finding.",
          "status": "resolved",
          "response": "The current optional-block rationale reports a 46.1% reduction, resolving the earlier discrepancy."
        },
        {
          "id": "R2-F1",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The chemotherapy concept was designated optional because its wording may be inconsistently surfaced, but it is AND-ed into the final strategy. The 0/30 loss sample still allows up to 10% of removed records to be relevant, and the 2,029-record search without the block is within the 10,000-record workload budget.",
          "recommendation": "Keep chemotherapy out of the required AND structure and screen for co-administration, or provide stronger evidence that requiring this block does not miss eligible studies.",
          "status": "resolved",
          "response": "The current strategy omits the chemotherapy block from the required AND structure. Its rationale cites the uncertainty in the 0/30 loss sample and the 2,029-record count within the workload budget, and specifies screening for chemotherapy co-administration at eligibility."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

