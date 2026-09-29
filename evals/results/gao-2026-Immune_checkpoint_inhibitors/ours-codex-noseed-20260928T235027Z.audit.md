# PubMed search strategy: audit

Generated 2026-09-29T00:14:51+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Immune checkpoint inhibitors plus chemotherapy for early triple-negative breast cancer
- Framework: PICO intervention effectiveness
- Scope confirmed by user: yes (User asked to proceed without questions. No known relevant articles were supplied. Assumed systematic review of clinical intervention studies; age, language, design and publication limits are not required. Early disease context and chemotherapy co-administration will be tested as optional blocks, with final eligibility confirmed at screening. PSB_AS_OF is set to 2025-01-31 for every command; no publication-date limit is used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Triple-negative breast cancer | search | Defining disease subtype; records may name member molecular labels rather than the category. |
| Immune checkpoint inhibitors | search | Defining intervention; studies may name individual agents rather than the drug class. |
| Chemotherapy given with an immune checkpoint inhibitor | optional | Chemotherapy co-administration was measured as an optional block. Specific cytotoxic-agent mentions alone do not establish co-administration, and the two broader probes found no eligible member-only records. |
| Early-stage disease or neoadjuvant/adjuvant treatment context | optional | Topic-defining population context that may be inconsistently labeled; test before requiring. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T00:14:00+00:00
- Records added to PubMed up to: 2025-01-31
- Total records: 2,028
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Triple Negative Breast Neoplasms[Mesh]` | 12,839 | none |
| 2 | `triple negative breast cancer[tiab]` | 19,872 | none |
| 3 | `triple-negative breast cancer[tiab]` | 19,872 | none |
| 4 | `triple-negative breast[tiab]` | 21,215 | none |
| 5 | `triple negative breast neoplasm*[tiab]` | 167 | none |
| 6 | `triple-negative breast neoplasm*[tiab]` | 167 | none |
| 7 | `TNBC[tiab]` | 14,325 | none |
| 8 | `(ER negative[tiab] AND PR negative[tiab] AND HER2 negative[tiab])` | 95 | none |
| 9 | `(estrogen receptor negative[tiab] AND progesterone receptor negative[tiab] AND HER2 negative[tiab])` | 26 | none |
| 10 | `(oestrogen receptor negative[tiab] AND progesterone receptor negative[tiab] AND HER2 negative[tiab])` | 3 | none |
| 11 | `(ER-/PR-/HER2-[tiab])` | 1,006 | none |
| 12 | `(ER-negative[tiab] AND PR-negative[tiab] AND HER2-negative[tiab])` | 95 | none |
| 13 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12` | 24,136 | none |
| 14 | `Immunotherapy[Mesh]` | 358,601 | none |
| 15 | `Immune Checkpoint Proteins[Mesh]` | 42,288 | none |
| 16 | `pembrolizumab[tiab]` | 10,643 | none |
| 17 | `Keytruda[tiab]` | 183 | none |
| 18 | `atezolizumab[tiab]` | 3,887 | none |
| 19 | `Tecentriq[tiab]` | 56 | none |
| 20 | `durvalumab[tiab]` | 2,047 | none |
| 21 | `Imfinzi[tiab]` | 24 | none |
| 22 | `nivolumab[tiab]` | 10,825 | none |
| 23 | `Opdivo[tiab]` | 123 | none |
| 24 | `avelumab[tiab]` | 1,130 | none |
| 25 | `Bavencio[tiab]` | 17 | none |
| 26 | `cemiplimab[tiab]` | 535 | none |
| 27 | `ipilimumab[tiab]` | 5,698 | none |
| 28 | `tremelimumab[tiab]` | 609 | none |
| 29 | `anti-PD-1[tiab]` | 10,138 | none |
| 30 | `anti-PD-L1[tiab]` | 3,796 | none |
| 31 | `PD-L1 block*[tiab]` | 1,757 | none |
| 32 | `PD-1 block*[tiab]` | 2,876 | none |
| 33 | `anti-CTLA-4[tiab]` | 2,373 | none |
| 34 | `PD-1 inhibitor*[tiab]` | 3,590 | none |
| 35 | `PD-L1 inhibitor*[tiab]` | 2,720 | none |
| 36 | `CTLA-4 inhibitor*[tiab]` | 558 | none |
| 37 | `programmed cell death 1 inhibitor*[tiab]` | 193 | none |
| 38 | `programmed death ligand 1 inhibitor*[tiab]` | 180 | none |
| 39 | `immune checkpoint block*[tiab]` | 8,557 | none |
| 40 | `immune checkpoint therap*[tiab]` | 1,175 | none |
| 41 | `checkpoint blockade[tiab]` | 9,914 | none |
| 42 | `#14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41` | 421,493 | none |
| 43 | `#13 AND #42` | 2,028 | none |

### Strategy (single line, for copying into PubMed)

```text
((Triple Negative Breast Neoplasms[Mesh] OR triple negative breast cancer[tiab] OR triple-negative breast cancer[tiab] OR triple-negative breast[tiab] OR triple negative breast neoplasm*[tiab] OR triple-negative breast neoplasm*[tiab] OR TNBC[tiab] OR (ER negative[tiab] AND PR negative[tiab] AND HER2 negative[tiab]) OR (estrogen receptor negative[tiab] AND progesterone receptor negative[tiab] AND HER2 negative[tiab]) OR (oestrogen receptor negative[tiab] AND progesterone receptor negative[tiab] AND HER2 negative[tiab]) OR (ER-/PR-/HER2-[tiab]) OR (ER-negative[tiab] AND PR-negative[tiab] AND HER2-negative[tiab])) AND (Immunotherapy[Mesh] OR Immune Checkpoint Proteins[Mesh] OR pembrolizumab[tiab] OR Keytruda[tiab] OR atezolizumab[tiab] OR Tecentriq[tiab] OR durvalumab[tiab] OR Imfinzi[tiab] OR nivolumab[tiab] OR Opdivo[tiab] OR avelumab[tiab] OR Bavencio[tiab] OR cemiplimab[tiab] OR ipilimumab[tiab] OR tremelimumab[tiab] OR anti-PD-1[tiab] OR anti-PD-L1[tiab] OR PD-L1 block*[tiab] OR PD-1 block*[tiab] OR anti-CTLA-4[tiab] OR PD-1 inhibitor*[tiab] OR PD-L1 inhibitor*[tiab] OR CTLA-4 inhibitor*[tiab] OR programmed cell death 1 inhibitor*[tiab] OR programmed death ligand 1 inhibitor*[tiab] OR immune checkpoint block*[tiab] OR immune checkpoint therap*[tiab] OR checkpoint blockade[tiab])) AND ("1800/01/01"[edat] : "2025/01/31"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 9 | 9 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Chemotherapy given with an immune checkpoint inhibitor | left out | 2,028 / 1,069 | 47.3% | none | 0/30 (up to 10% of removed records could be relevant) | After the checkpoint-wording revision, screened the current 30-record loss sample; none met the eligibility criteria. The block would remove about 47% of current core results, while requiring its wording remains an unnecessary sensitivity risk. |
| Early-stage disease or neoadjuvant/adjuvant treatment context | left out | 2,028 / 551 | 72.8% | none | 0/30 (up to 10% of removed records could be relevant) | After the checkpoint-wording revision, screened the current 30-record loss sample; none met the eligibility criteria. The block would remove about 73% of current core results, and early stage remains a screening criterion. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Triple-negative breast cancer | 1 | `Breast Neoplasms[Mesh] OR breast cancer[tiab] OR breast carcinoma*[tiab]` | 4,925 | 0/30 |
| Triple-negative breast cancer | 2 | `Breast Neoplasms[Mesh] OR breast cancer[tiab] OR breast carcinoma*[tiab]` | 4,917 | 0/30 |
| Immune checkpoint inhibitors | 1 | `PD-1[tiab] OR PD-L1[tiab] OR PD-L2[tiab] OR checkpoint inhibitor*[tiab] OR immunotherapy[tiab]` | 1,149 | 0/30 |
| Immune checkpoint inhibitors | 2 | `PD-1[tiab] OR PD-L1[tiab] OR PD-L2[tiab] OR checkpoint inhibitor*[tiab] OR immunotherapy[tiab]` | 1,172 | 1/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| tnbc | 421,493 | 0 |
| checkpoint | 24,136 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 2,670 | initial | none | Initial recall-first strategy: search TNBC and checkpoint inhibition; test co-administered chemotherapy and early disease context as optional blocks. No supplied seeds; user requested proceeding with assumptions. |
| 2 | 1,986 | tnbc: +0 / -1; checkpoint: +1 / -1 | none | Replaced an ambiguous MeSH authority label with the verified broader Immunotherapy heading plus individual checkpoint inhibitor names; removed unrestricted Breast Neoplasms heading from the TNBC block to avoid treating all breast cancer as TNBC. |
| 3 | 2,017 | tnbc: +1 / -0 | none | Added the ranked phrase triple-negative breast[tiab] to cover records that name the subtype without the word cancer; all eight development records already contained this wording, and evaluation measures whether it expands retrieval without losses. |
| 4 | 2,028 | checkpoint: +2 / -0 | none | Added PD-L1/PD-1 blockade word variants after the category probe found an in-scope neoadjuvant TNBC case report; recorded the missed record in the development set. Chemotherapy category probing showed no relevant drug-member-only records, so its category flag is false for the exact combination concept. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 1 findings; R1-1 document accepted-risk
- Round 2 on version 4: 1 findings; R2-1 must-fix resolved
- Round 3 on version 4: 2 findings; R1-1 document accepted-risk, R2-1 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 843 NCBI requests logged (417 from cache); strategy sha256 8d6cff0d25be._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "code": "category_probe_budget_spent",
        "message": "Probe budget spent while the latest probe still found relevant records",
        "severity": "warning",
        "location": "concept:checkpoint",
        "pmids": [
          "32914041"
        ],
        "blocking": false,
        "requires_review": true,
        "id": "I-ae73badaa6e29f6739c2"
      }
    ],
    "issues": [
      {
        "code": "category_probe_budget_spent",
        "message": "Probe budget spent while the latest probe still found relevant records",
        "severity": "warning",
        "location": "concept:checkpoint",
        "pmids": [
          "32914041"
        ],
        "blocking": false,
        "requires_review": true,
        "id": "I-ae73badaa6e29f6739c2"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Triple Negative Breast Neoplasms",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:14:00+00:00",
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
        "text": "Triple Negative Breast Neoplasms",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Immunotherapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:14:00+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D007167",
          "name": "Immunotherapy",
          "type": "descriptor",
          "scope_note": "Manipulation of the host's immune system in treatment of disease. It includes both active and passive immunization as well as immunosuppressive therapy to prevent graft rejection.",
          "tree_numbers": [
            "E02.095.465.425"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D007167",
      "preferred_label": "Immunotherapy",
      "type": "descriptor",
      "location": "vocabulary:21",
      "term": {
        "text": "Immunotherapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Immune Checkpoint Proteins",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T00:14:00+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000082102",
          "name": "Immune Checkpoint Proteins",
          "type": "descriptor",
          "scope_note": "Immunomodulators that regulate immune system either in stimulatory or inhibitory fashion allowing IMMUNE TOLERANCE. Activation of suppressed immune system (IMMUNOSUPPRESSION (PHYSIOLOGY)) in immunotherapy by IMMUNE CHECKPOINT INHIBITORS often targets inhibitory checkpoint molecules.",
          "tree_numbers": [
            "D12.776.465",
            "D23.383"
          ],
          "entry_terms": 13,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000082102",
      "preferred_label": "Immune Checkpoint Proteins",
      "type": "descriptor",
      "location": "vocabulary:22",
      "term": {
        "text": "Immune Checkpoint Proteins",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"triple negative breast neoplasms\"[MeSH Terms] OR \"triple negative breast cancer\"[Title/Abstract] OR \"triple negative breast cancer\"[Title/Abstract] OR \"triple negative breast\"[Title/Abstract] OR \"triple negative breast neoplasm*\"[Title/Abstract] OR \"triple negative breast neoplasm*\"[Title/Abstract] OR \"TNBC\"[Title/Abstract] OR (\"ER-negative\"[Title/Abstract] AND \"PR-negative\"[Title/Abstract] AND \"HER2-negative\"[Title/Abstract]) OR (\"estrogen receptor negative\"[Title/Abstract] AND \"progesterone receptor negative\"[Title/Abstract] AND \"HER2-negative\"[Title/Abstract]) OR (\"oestrogen receptor negative\"[Title/Abstract] AND \"progesterone receptor negative\"[Title/Abstract] AND \"HER2-negative\"[Title/Abstract]) OR \"er pr her2\"[Title/Abstract] OR (\"ER-negative\"[Title/Abstract] AND \"PR-negative\"[Title/Abstract] AND \"HER2-negative\"[Title/Abstract])) AND (\"immunotherapy\"[MeSH Terms] OR \"immune checkpoint proteins\"[MeSH Terms] OR \"pembrolizumab\"[Title/Abstract] OR \"Keytruda\"[Title/Abstract] OR \"atezolizumab\"[Title/Abstract] OR \"Tecentriq\"[Title/Abstract] OR \"durvalumab\"[Title/Abstract] OR \"Imfinzi\"[Title/Abstract] OR \"nivolumab\"[Title/Abstract] OR \"Opdivo\"[Title/Abstract] OR \"avelumab\"[Title/Abstract] OR \"Bavencio\"[Title/Abstract] OR \"cemiplimab\"[Title/Abstract] OR \"ipilimumab\"[Title/Abstract] OR \"tremelimumab\"[Title/Abstract] OR \"anti-PD-1\"[Title/Abstract] OR \"anti-PD-L1\"[Title/Abstract] OR \"pd l1 block*\"[Title/Abstract] OR \"pd 1 block*\"[Title/Abstract] OR \"anti-CTLA-4\"[Title/Abstract] OR \"pd 1 inhibitor*\"[Title/Abstract] OR \"pd l1 inhibitor*\"[Title/Abstract] OR \"ctla 4 inhibitor*\"[Title/Abstract] OR \"programmed cell death 1 inhibitor*\"[Title/Abstract] OR \"programmed death ligand 1 inhibitor*\"[Title/Abstract] OR \"immune checkpoint block*\"[Title/Abstract] OR \"immune checkpoint therap*\"[Title/Abstract] OR \"checkpoint blockade\"[Title/Abstract]) AND 1800/01/01:2025/01/31[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "78c307eaa17fadd494a06e1395b2c329fa62cea49d5dbd58a348f8dbac557c74",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two required concepts are represented by category headings, text words, and individual agent names. The optional chemotherapy and early-stage blocks were tested and left out with documented screening rationales."
        },
        "operators": {
          "verdict": "pass",
          "note": "The disease and checkpoint concepts are OR-combined, then AND-combined. No fragile direction or participant-event term is used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes Triple Negative Breast Neoplasms, Immunotherapy, and Immune Checkpoint Proteins headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The blocks cover TNBC names and receptor-status formulations, checkpoint agents and brands, and checkpoint mechanism wording. The known relevant set is retrieved in full."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports tested expressions without diagnostics; no proximity operators or phrase warnings require interpretation."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No limits or filters are applied."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "document",
          "kind": "reporting",
          "finding": "Checkpoint category probe 2 found relevant PMID 32914041 outside the broader checkpoint wording used for the probe. This is a sensitivity warning, although the current strategy retrieves that record and all nine known relevant records.",
          "recommendation": "Retain the warning in the audit trail and record that the current strategy retrieves PMID 32914041. The probe budget is spent, so the packet does not establish whether other relevant records remain outside the checkpoint block.",
          "status": "accepted-risk",
          "response": "The warning is retained because the second probe found a relevant record. The current retrieval includes PMID 32914041 and all nine known relevant records, which supports accepting the residual uncertainty for this review.",
          "evidence": "Current retrieved_known includes 32914041; validation reports 9 of 9 known records retrieved. Checkpoint probe 2 found 32914041 among 30 screened records."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-ae73badaa6e29f6739c2",
          "status": "accepted-risk",
          "response": "Retain the warning: the probe found a relevant record outside its broader checkpoint wording, but the current strategy retrieves that record and all known relevant records. The probe budget is spent, so residual category coverage uncertainty remains.",
          "evidence": "Probe 2 found PMID 32914041; current retrieved_known includes it, and validation reports 9/9 known records retrieved."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "78c307eaa17fadd494a06e1395b2c329fa62cea49d5dbd58a348f8dbac557c74",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched concepts include TNBC terminology and named checkpoint agents as bare terms. The optional chemotherapy and early-stage blocks were tested and left out with screening rationales."
        },
        "operators": {
          "verdict": "pass",
          "note": "Disease and checkpoint terms are OR-combined, then the two concept blocks are AND-combined. No one-way process or participant-event terms are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes Triple Negative Breast Neoplasms, Immunotherapy, and Immune Checkpoint Proteins headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The blocks cover TNBC and receptor-status formulations, individual checkpoint agents and brands, and mechanism wording. The current strategy retrieves all nine known relevant records, including PMID 32914041; the exhausted checkpoint probe still leaves residual category coverage uncertainty."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no query errors, translation issues, or phrase warnings requiring clause-specific interpretation."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The EDAT boundary is the explicitly requested PubMed snapshot cutoff, stored in protocol as_of and enforced by PSB_AS_OF; no publication-date [dp] limit is applied."
        }
      },
      "findings": [
        {
          "id": "R2-1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query includes an EDAT range ending 2025-01-31, despite no temporal restriction in the question or eligibility.",
          "recommendation": "Clarify that the date is an intended search cutoff, or remove the EDAT range.",
          "status": "resolved",
          "response": "The explicit run instruction requires a PubMed snapshot as of 2025-01-31 and prohibits using records added after that date. The protocol stores this in as_of, and every PSB command uses PSB_AS_OF=2025-01-31, which constrains Entrez entry date as required. This is a requested snapshot boundary, not a publication-date limit; no [dp] limit is present. The query is retained as generated.",
          "evidence": "protocol.json has as_of=2025-01-31 and notes the requested cutoff; the final query's generated EDAT range is 1800/01/01 through 2025/01/31. The transcript/harness request explicitly requires this cutoff."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-ae73badaa6e29f6739c2",
          "status": "accepted-risk",
          "response": "Retain the warning because checkpoint probe 2 found a relevant record outside its broader probe wording and the probe budget is spent. The current strategy retrieves PMID 32914041 and all nine known relevant records, but the packet cannot establish whether additional relevant records fall outside the checkpoint block.",
          "evidence": "Probe 2 found PMID 32914041; current retrieved_known includes it, and validation reports 9/9 known records retrieved."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "78c307eaa17fadd494a06e1395b2c329fa62cea49d5dbd58a348f8dbac557c74",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched blocks cover triple-negative breast cancer terminology and named checkpoint agents. The optional chemotherapy and early-stage blocks were tested and left out with documented screening rationales."
        },
        "operators": {
          "verdict": "pass",
          "note": "Disease and checkpoint terms are OR-combined, then the two concepts are AND-combined. No fragile direction or participant-event terms are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes Triple Negative Breast Neoplasms, Immunotherapy, and Immune Checkpoint Proteins headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The blocks cover TNBC and receptor-status formulations, individual checkpoint agents and brands, and checkpoint mechanism wording. The strategy retrieves all nine known relevant records, including PMID 32914041. The exhausted checkpoint probe leaves the documented residual coverage uncertainty."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query reports no syntax or translation diagnostics, and no phrase warnings require clause-specific interpretation."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The EDAT boundary implements the explicitly requested PubMed snapshot cutoff of 2025-01-31, recorded in the protocol as as_of. No publication-date limit is applied."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "document",
          "kind": "reporting",
          "finding": "Checkpoint category probe 2 found PMID 32914041 outside the broader checkpoint wording used for the probe. The current strategy retrieves it, but the spent probe budget leaves uncertainty about other records outside the checkpoint block.",
          "recommendation": "Retain the warning in the audit trail and note that the strategy retrieves PMID 32914041 and all nine known relevant records.",
          "status": "accepted-risk",
          "response": "The warning remains accepted because the current strategy retrieves PMID 32914041 and all known relevant records, while the spent probe budget leaves residual category coverage uncertainty."
        },
        {
          "id": "R2-1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query includes an EDAT range ending 2025-01-31, despite no temporal restriction in the question or eligibility.",
          "recommendation": "Clarify that the date is an intended search cutoff, or remove the EDAT range.",
          "status": "resolved",
          "response": "The protocol records the requested PubMed snapshot cutoff as 2025-01-31 and applies it through the EDAT range. This is a requested snapshot boundary, not a publication-date limit; no [dp] limit is present."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-ae73badaa6e29f6739c2",
          "status": "accepted-risk",
          "response": "Retain the warning because checkpoint probe 2 found a relevant record outside its broader wording and the probe budget is spent. The strategy retrieves PMID 32914041 and all nine known relevant records, but residual category coverage uncertainty remains.",
          "evidence": "Probe 2 found PMID 32914041; it appears in retrieved_known, and validation reports 9/9 known records retrieved."
        }
      ]
    }
  ]
}
```

