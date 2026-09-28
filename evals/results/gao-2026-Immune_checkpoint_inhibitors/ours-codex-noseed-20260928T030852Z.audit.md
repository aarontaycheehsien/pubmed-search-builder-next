# PubMed search strategy: audit

Generated 2026-09-28T03:25:25+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Immune checkpoint inhibitors plus chemotherapy for early triple-negative breast cancer
- Framework: PICO (intervention effectiveness)
- Scope confirmed by user: no (User asked to proceed without questions; scope and roles are provisional operational assumptions. Interpret early disease as nonmetastatic stage I-III, including neoadjuvant and adjuvant treatment. No language, publication-date, age, or study-design limits. PSB_AS_OF is set to 2025-01-31 for every command, bounding PubMed by Entrez date; no [dp] cutoff. No known articles supplied. Standard-depth discovery will seek candidate prior reviews and screen records if available. Candidate benchmark records were screened from reference lists of PubMed-indexed systematic reviews PMID 37612624 (early-stage TNBC; five included trials) and PMID 39207778 (early breast cancer; follow-up report). The benchmark is a screened subset of primary reports, not a complete independent validation set. Candidate eligibility required early-stage/nonmetastatic TNBC population or extractable TNBC data and checkpoint inhibitor administered with chemotherapy. Stage I-III is an operational interpretation of early disease; include neoadjuvant and adjuvant contexts. Reviewer may need to broaden if they intend a different definition. After inspecting broad query samples containing non-clinical and ICI-only records, the chemotherapy coadministration criterion was promoted from screening to a required search block because it is part of the explicitly specified combined intervention; benchmark retrieval is checked after this change.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Triple-negative breast cancer | search | The disease subtype defines the population and is named in records; broad breast cancer wording alone would create substantial screening burden. |
| Immune checkpoint inhibitors | search | The intervention is central and has searchable drug-class and agent terminology. |
| Early/nonmetastatic stage I-III disease | screen | Stage and resectability may be reported in full text or incompletely in abstracts; screening avoids a fragile required stage block. |
| Chemotherapy administered with the checkpoint inhibitor | search | Coadministration with chemotherapy is explicit in the intervention and required by eligibility. A broad MeSH and text block tests whether requiring the combination reduces ICI-only and mechanistic records while preserving known eligible studies. |
| Comparator and outcomes | screen | Comparator and outcomes are not needed to identify the topic and are screened. |
| Eligible study designs | screen | No study-design restriction was specified; screen study design. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T03:24:23+00:00
- Records added to PubMed up to: 2025-01-31
- Total records: 785
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Triple Negative Breast Neoplasms"[Mesh]` | 12,839 | none |
| 2 | `"triple negative breast cancer"[tiab]` | 19,872 | none |
| 3 | `"triple-negative breast cancer"[tiab]` | 19,872 | none |
| 4 | `"triple negative breast neoplasm*"[tiab]` | 167 | none |
| 5 | `"triple-negative breast neoplasm*"[tiab]` | 167 | none |
| 6 | `(TNBC[tiab] AND breast[tiab])` | 14,239 | none |
| 7 | `("triple-negative"[tiab] AND breast[tiab])` | 26,889 | none |
| 8 | `("ER negative"[tiab] AND "PR negative"[tiab] AND "HER2 negative"[tiab])` | 95 | none |
| 9 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8` | 27,932 | none |
| 10 | `pembrolizumab[nm]` | 4,823 | none |
| 11 | `atezolizumab[nm]` | 1,616 | none |
| 12 | `durvalumab[nm]` | 859 | none |
| 13 | `avelumab[nm]` | 458 | none |
| 14 | `cemiplimab[nm]` | 173 | none |
| 15 | `dostarlimab[nm]` | 71 | none |
| 16 | `tremelimumab[nm]` | 294 | none |
| 17 | `Nivolumab[Mesh]` | 6,195 | none |
| 18 | `Ipilimumab[Mesh]` | 3,337 | none |
| 19 | `"immune checkpoint inhibitor*"[tiab]` | 32,330 | none |
| 20 | `"immune checkpoint blockade"[tiab]` | 7,628 | none |
| 21 | `"checkpoint inhibitor*"[tiab]` | 38,149 | none |
| 22 | `"checkpoint blockade"[tiab]` | 9,914 | none |
| 23 | `"PD-1 inhibitor*"[tiab]` | 3,590 | none |
| 24 | `"PD-L1 inhibitor*"[tiab]` | 2,720 | none |
| 25 | `"PD1 inhibitor*"[tiab]` | 213 | none |
| 26 | `"PDL1 inhibitor*"[tiab]` | 85 | none |
| 27 | `"anti-PD-1"[tiab]` | 10,138 | none |
| 28 | `"anti-PD-L1"[tiab]` | 3,796 | none |
| 29 | `"anti-CTLA-4"[tiab]` | 2,373 | none |
| 30 | `pembrolizumab[tiab]` | 10,643 | none |
| 31 | `Keytruda[tiab]` | 183 | none |
| 32 | `atezolizumab[tiab]` | 3,887 | none |
| 33 | `Tecentriq[tiab]` | 56 | none |
| 34 | `durvalumab[tiab]` | 2,047 | none |
| 35 | `Imfinzi[tiab]` | 24 | none |
| 36 | `nivolumab[tiab]` | 10,825 | none |
| 37 | `Opdivo[tiab]` | 123 | none |
| 38 | `ipilimumab[tiab]` | 5,698 | none |
| 39 | `Yervoy[tiab]` | 74 | none |
| 40 | `avelumab[tiab]` | 1,130 | none |
| 41 | `Bavencio[tiab]` | 17 | none |
| 42 | `cemiplimab[tiab]` | 535 | none |
| 43 | `Libtayo[tiab]` | 19 | none |
| 44 | `dostarlimab[tiab]` | 172 | none |
| 45 | `Jemperli[tiab]` | 19 | none |
| 46 | `tremelimumab[tiab]` | 609 | none |
| 47 | `Imjudo[tiab]` | 8 | none |
| 48 | `#10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47` | 69,681 | none |
| 49 | `"Antineoplastic Combined Chemotherapy Protocols"[Mesh]` | 168,964 | none |
| 50 | `chemotherap*[tiab]` | 545,177 | none |
| 51 | `chemo[tiab]` | 32,749 | none |
| 52 | `chemoimmunotherap*[tiab]` | 5,123 | none |
| 53 | `#49 OR #50 OR #51 OR #52` | 637,979 | none |
| 54 | `#9 AND #48 AND #53` | 785 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Triple Negative Breast Neoplasms"[Mesh] OR "triple negative breast cancer"[tiab] OR "triple-negative breast cancer"[tiab] OR "triple negative breast neoplasm*"[tiab] OR "triple-negative breast neoplasm*"[tiab] OR (TNBC[tiab] AND breast[tiab]) OR ("triple-negative"[tiab] AND breast[tiab]) OR ("ER negative"[tiab] AND "PR negative"[tiab] AND "HER2 negative"[tiab])) AND (pembrolizumab[nm] OR atezolizumab[nm] OR durvalumab[nm] OR avelumab[nm] OR cemiplimab[nm] OR dostarlimab[nm] OR tremelimumab[nm] OR Nivolumab[Mesh] OR Ipilimumab[Mesh] OR "immune checkpoint inhibitor*"[tiab] OR "immune checkpoint blockade"[tiab] OR "checkpoint inhibitor*"[tiab] OR "checkpoint blockade"[tiab] OR "PD-1 inhibitor*"[tiab] OR "PD-L1 inhibitor*"[tiab] OR "PD1 inhibitor*"[tiab] OR "PDL1 inhibitor*"[tiab] OR "anti-PD-1"[tiab] OR "anti-PD-L1"[tiab] OR "anti-CTLA-4"[tiab] OR pembrolizumab[tiab] OR Keytruda[tiab] OR atezolizumab[tiab] OR Tecentriq[tiab] OR durvalumab[tiab] OR Imfinzi[tiab] OR nivolumab[tiab] OR Opdivo[tiab] OR ipilimumab[tiab] OR Yervoy[tiab] OR avelumab[tiab] OR Bavencio[tiab] OR cemiplimab[tiab] OR Libtayo[tiab] OR dostarlimab[tiab] OR Jemperli[tiab] OR tremelimumab[tiab] OR Imjudo[tiab]) AND ("Antineoplastic Combined Chemotherapy Protocols"[Mesh] OR chemotherap*[tiab] OR chemo[tiab] OR chemoimmunotherap*[tiab])) AND ("1800/01/01"[edat] : "2025/01/31"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 6 | 6 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| tnbc | 18,755 | 0 |
| ici | 8,183 | 0 |
| chemotherapy | 1,613 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 7,883 | initial | none | initial draft eval |
| 2 | 7,006 | ici: +0 / -2 | none | Removed two MeSH headings whose authority validation returned ambiguous duplicate records, retaining verified mechanistic headings and text words. |
| 3 | 7,797 | ici: +1 / -3 | none | Replaced broad immune target-protein MeSH headings with the validated Immunotherapy MeSH heading; retained class and agent text terms to represent administered checkpoint treatment. |
| 4 | 6,546 | ici: +9 / -1 | none | Replaced broad Immunotherapy MeSH with agent-specific supplementary concept and drug descriptor headings, following the high result count and nonspecific samples. |
| 5 | 2,935 | tnbc: +0 / -1 | none | Removed broad Breast Neoplasms MeSH after PubMed samples showed unrelated breast subtypes and mechanistic records; tested benchmark I-SPY2 still has TNBC language in its abstract and is expected to remain retrievable. |
| 6 | 1,613 | ici: +0 / -1 | none | Removed generic immunotherapy text because it retrieves non-checkpoint immunotherapies; specific agent names, checkpoint inhibitor/blockade phrases, and mechanisms remain. |
| 7 | 785 | chemotherapy: +4 / -0 | none | Added chemotherapy as a required block because it is a defining coadministered part of the specified intervention; broad query samples had many ICI-only, biomarker and preclinical records. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 7: 1 findings; R1-D1 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 852 NCBI requests logged (516 from cache); strategy sha256 4fbd59fc3aa2._

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
      "checked_at": "2026-09-28T03:24:23+00:00",
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
      "requested": "pembrolizumab",
      "expected_type": "supplementary",
      "checked_at": "2026-09-28T03:24:23+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "C582435",
          "name": "pembrolizumab",
          "type": "supplementary",
          "scope_note": "",
          "tree_numbers": [
            "@215512"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "C582435",
      "preferred_label": "pembrolizumab",
      "type": "supplementary",
      "location": "vocabulary:13",
      "term": {
        "text": "pembrolizumab",
        "tag": "nm",
        "field": "nm"
      }
    },
    {
      "requested": "atezolizumab",
      "expected_type": "supplementary",
      "checked_at": "2026-09-28T03:24:23+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "C000594389",
          "name": "atezolizumab",
          "type": "supplementary",
          "scope_note": "A monoclonal antibody that targets programmed death-ligand 1 (CD274 ANTIGEN) and is used to treat urothelial carcinoma, the most common type of bladder cancer.",
          "tree_numbers": [
            "@224560"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "C000594389",
      "preferred_label": "atezolizumab",
      "type": "supplementary",
      "location": "vocabulary:14",
      "term": {
        "text": "atezolizumab",
        "tag": "nm",
        "field": "nm"
      }
    },
    {
      "requested": "durvalumab",
      "expected_type": "supplementary",
      "checked_at": "2026-09-28T03:24:23+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "C000613593",
          "name": "durvalumab",
          "type": "supplementary",
          "scope_note": "an IgG1 that targets programmed cell death 1 ligand 1 (PD-L1); enhances the immune response to tumor cells and is used for the treatment of locally advanced or metastatic urothelial carcinoma",
          "tree_numbers": [
            "@236871"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "C000613593",
      "preferred_label": "durvalumab",
      "type": "supplementary",
      "location": "vocabulary:15",
      "term": {
        "text": "durvalumab",
        "tag": "nm",
        "field": "nm"
      }
    },
    {
      "requested": "avelumab",
      "expected_type": "supplementary",
      "checked_at": "2026-09-28T03:24:23+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "C000609138",
          "name": "avelumab",
          "type": "supplementary",
          "scope_note": "targets programmed cell death protein-1 ligand; has antineoplastic activity",
          "tree_numbers": [
            "@234238"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "C000609138",
      "preferred_label": "avelumab",
      "type": "supplementary",
      "location": "vocabulary:16",
      "term": {
        "text": "avelumab",
        "tag": "nm",
        "field": "nm"
      }
    },
    {
      "requested": "cemiplimab",
      "expected_type": "supplementary",
      "checked_at": "2026-09-28T03:24:23+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "C000627974",
          "name": "cemiplimab",
          "type": "supplementary",
          "scope_note": "human monoclonal antibody against programmed cell death 1 protein (PD-1) for the treatment of metastatic or unresectable cutaneous squamous cell carcinoma (CSCC)",
          "tree_numbers": [
            "@245506"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "C000627974",
      "preferred_label": "cemiplimab",
      "type": "supplementary",
      "location": "vocabulary:17",
      "term": {
        "text": "cemiplimab",
        "tag": "nm",
        "field": "nm"
      }
    },
    {
      "requested": "dostarlimab",
      "expected_type": "supplementary",
      "checked_at": "2026-09-28T03:24:23+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "C000719628",
          "name": "dostarlimab",
          "type": "supplementary",
          "scope_note": "",
          "tree_numbers": [
            "@316823"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "C000719628",
      "preferred_label": "dostarlimab",
      "type": "supplementary",
      "location": "vocabulary:18",
      "term": {
        "text": "dostarlimab",
        "tag": "nm",
        "field": "nm"
      }
    },
    {
      "requested": "tremelimumab",
      "expected_type": "supplementary",
      "checked_at": "2026-09-28T03:24:23+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "C520704",
          "name": "tremelimumab",
          "type": "supplementary",
          "scope_note": "a fully human anti-cytotoxic T lymphocyte-associated antigen 4 monoclonal antibody for immunotherapy of metastatic melanoma",
          "tree_numbers": [
            "@165985"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "C520704",
      "preferred_label": "tremelimumab",
      "type": "supplementary",
      "location": "vocabulary:19",
      "term": {
        "text": "tremelimumab",
        "tag": "nm",
        "field": "nm"
      }
    },
    {
      "requested": "Nivolumab",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:24:23+00:00",
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
      "location": "vocabulary:20",
      "term": {
        "text": "Nivolumab",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Ipilimumab",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:24:23+00:00",
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
      "location": "vocabulary:21",
      "term": {
        "text": "Ipilimumab",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Antineoplastic Combined Chemotherapy Protocols",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:24:23+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000971",
          "name": "Antineoplastic Combined Chemotherapy Protocols",
          "type": "descriptor",
          "scope_note": "The use of two or more chemicals simultaneously or sequentially in the drug therapy of neoplasms. The drugs need not be in the same dosage form.",
          "tree_numbers": [
            "E02.183.750.500",
            "E02.319.077.500",
            "E02.319.310.037"
          ],
          "entry_terms": 28,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000971",
      "preferred_label": "Antineoplastic Combined Chemotherapy Protocols",
      "type": "descriptor",
      "location": "vocabulary:51",
      "term": {
        "text": "\"Antineoplastic Combined Chemotherapy Protocols\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Triple Negative Breast Neoplasms\"[MeSH Terms] OR \"triple-negative breast cancer\"[Title/Abstract] OR \"triple-negative breast cancer\"[Title/Abstract] OR \"triple negative breast neoplasm*\"[Title/Abstract] OR \"triple negative breast neoplasm*\"[Title/Abstract] OR (\"TNBC\"[Title/Abstract] AND \"breast\"[Title/Abstract]) OR (\"triple-negative\"[Title/Abstract] AND \"breast\"[Title/Abstract]) OR (\"ER negative\"[Title/Abstract] AND \"PR negative\"[Title/Abstract] AND \"HER2 negative\"[Title/Abstract])) AND (\"pembrolizumab\"[Supplementary Concept] OR \"atezolizumab\"[Supplementary Concept] OR \"durvalumab\"[Supplementary Concept] OR \"avelumab\"[Supplementary Concept] OR \"cemiplimab\"[Supplementary Concept] OR \"dostarlimab\"[Supplementary Concept] OR \"tremelimumab\"[Supplementary Concept] OR \"nivolumab\"[MeSH Terms] OR \"ipilimumab\"[MeSH Terms] OR \"immune checkpoint inhibitor*\"[Title/Abstract] OR \"immune checkpoint blockade\"[Title/Abstract] OR \"checkpoint inhibitor*\"[Title/Abstract] OR \"checkpoint blockade\"[Title/Abstract] OR \"pd 1 inhibitor*\"[Title/Abstract] OR \"pd l1 inhibitor*\"[Title/Abstract] OR \"pd1 inhibitor*\"[Title/Abstract] OR \"pdl1 inhibitor*\"[Title/Abstract] OR \"anti-PD-1\"[Title/Abstract] OR \"anti-PD-L1\"[Title/Abstract] OR \"anti-CTLA-4\"[Title/Abstract] OR \"pembrolizumab\"[Title/Abstract] OR \"Keytruda\"[Title/Abstract] OR \"atezolizumab\"[Title/Abstract] OR \"Tecentriq\"[Title/Abstract] OR \"durvalumab\"[Title/Abstract] OR \"Imfinzi\"[Title/Abstract] OR \"nivolumab\"[Title/Abstract] OR \"Opdivo\"[Title/Abstract] OR \"ipilimumab\"[Title/Abstract] OR \"Yervoy\"[Title/Abstract] OR \"avelumab\"[Title/Abstract] OR \"Bavencio\"[Title/Abstract] OR \"cemiplimab\"[Title/Abstract] OR \"Libtayo\"[Title/Abstract] OR \"dostarlimab\"[Title/Abstract] OR \"Jemperli\"[Title/Abstract] OR \"tremelimumab\"[Title/Abstract] OR \"Imjudo\"[Title/Abstract]) AND (\"Antineoplastic Combined Chemotherapy Protocols\"[MeSH Terms] OR \"chemotherap*\"[Title/Abstract] OR \"chemo\"[Title/Abstract] OR \"chemoimmunotherap*\"[Title/Abstract]) AND 1800/01/01:2025/01/31[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 7,
      "review_sha256": "3f8dad46daf074e6a7a091edb2765924062080d0b643d389c15256d9589a28c2",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The final query translation matches the supplied blocks; no translation issues or PubMed warnings are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The TNBC, checkpoint-inhibitor, and chemotherapy blocks are OR-combined and then AND-combined as the stated scope requires. Stage, comparator, outcomes, and study design remain screening criteria."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The supplied MeSH and supplementary concept terms are verified in the packet; the combination chemotherapy heading is complemented by text words."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The blocks include disease, drug-class, agent, and chemotherapy text terms. All six benchmark records are retrieved; the packet reports no missed records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query executes with no reported syntax errors, and the final query translation and count are provided."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, age, or study-design limits are applied. The Entrez date bound is documented as an as-of cutoff, not a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-D1",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "The search is bounded by Entrez date through 2025-01-31. The six-record benchmark is a screened subset of prior-review references, not a complete independent validation set; its 100% retrieval does not establish full sensitivity.",
          "recommendation": "Carry both limitations into the final search report and rerun the search with a current cutoff if the intended search date is later than 2025-01-31.",
          "status": "accepted-risk",
          "response": "The cutoff and benchmark provenance and limits are explicitly documented in the packet; retain them as reporting qualifications."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

