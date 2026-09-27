# PubMed search strategy: audit

Generated 2026-09-27T22:35:24+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Patients retransitioning from a biosimilar TNF-alpha inhibitor back to the originator biologic
- Framework: PECO
- Scope confirmed by user: no (User asked to proceed without questions. Assumed the review concerns any indication and any outcome or study design, and that studies of the broader biosimilar-originator switching process are eligible candidates if they may report a switch back in a subgroup. Direction, indication, outcomes, and design will be assessed at screening. No user-supplied seeds. PubMed knowledge is bounded by Entrez date 2021-02-12 via PSB_AS_OF for every command; no publication-date limit is used. Vocabulary QA evidence: the live delivery validator marked Tumor Necrosis Factor Inhibitors[Mesh] ambiguous (duplicate authority matches for the same UI, one incomplete and one with the agent scope note), so it was removed to clear a technical blocker; Golimumab[Mesh] returned no descriptor match and PubMed returned "No items found", so it was removed as invalid MeSH. Golimumab remains searched in [tiab], and the class is represented by TNF-alpha heading, other valid TNF drug headings, and drug/class text words.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Biosimilar medicines | search | The exposure must involve a biosimilar; this is a central searchable topic. |
| TNF-alpha inhibitors | search | The drug class defines the review topic; individual drug names will also be searched. |
| Switching or transition between biosimilar and originator | search | Search the broader switch process in either direction because switch-back wording is fragile; screen for the direction back to originator. |
| Retransition from biosimilar to originator | screen | Direction may be reported only as a secondary finding or in full text. |
| Underlying inflammatory disease or indication | screen | The question does not specify an indication; screen across diseases treated with TNF inhibitors. |
| Clinical, safety, immunogenicity, economic, or patient-reported outcomes | screen | Outcomes are not specified and should not be required for retrieval. |
| Eligible study designs | screen | Do not apply a study-design filter; assess eligibility during screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-27T22:34:30+00:00
- Records added to PubMed up to: 2021-02-12
- Total records: 658
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Biosimilar Pharmaceuticals[Mesh]` | 2,555 | none |
| 2 | `Biological Products[Mesh]` | 609,201 | none |
| 3 | `biosimilar*[tiab]` | 3,878 | none |
| 4 | `follow-on biologic*[tiab]` | 114 | none |
| 5 | `follow on biologic*[tiab]` | 114 | none |
| 6 | `subsequent entry biologic*[tiab]` | 23 | none |
| 7 | `CT-P13[tiab]` | 236 | none |
| 8 | `Remsima[tiab]` | 72 | none |
| 9 | `Inflectra[tiab]` | 79 | none |
| 10 | `SB2[tiab]` | 449 | none |
| 11 | `Flixabi[tiab]` | 14 | none |
| 12 | `Renflexis[tiab]` | 16 | none |
| 13 | `SB4[tiab]` | 169 | none |
| 14 | `Benepali[tiab]` | 27 | none |
| 15 | `GP2015[tiab]` | 18 | none |
| 16 | `Erelzi[tiab]` | 15 | none |
| 17 | `ABP 501[tiab]` | 21 | none |
| 18 | `Amgevita[tiab]` | 6 | none |
| 19 | `Imraldi[tiab]` | 13 | none |
| 20 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19` | 611,075 | none |
| 21 | `Tumor Necrosis Factor-alpha[Mesh]` | 129,542 | none |
| 22 | `Infliximab[Mesh]` | 11,046 | none |
| 23 | `Adalimumab[Mesh]` | 6,043 | none |
| 24 | `Etanercept[Mesh]` | 6,162 | none |
| 25 | `Certolizumab Pegol[Mesh]` | 674 | none |
| 26 | `infliximab[tiab]` | 12,876 | none |
| 27 | `adalimumab[tiab]` | 7,410 | none |
| 28 | `etanercept[tiab]` | 7,154 | none |
| 29 | `golimumab[tiab]` | 1,187 | none |
| 30 | `certolizumab[tiab]` | 1,164 | none |
| 31 | `anti-TNF[tiab]` | 11,204 | none |
| 32 | `TNF inhibitor*[tiab]` | 2,009 | none |
| 33 | `tumor necrosis factor inhibitor*[tiab]` | 1,136 | none |
| 34 | `tumour necrosis factor inhibitor*[tiab]` | 431 | none |
| 35 | `#21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34` | 149,237 | none |
| 36 | `Drug Substitution[Mesh]` | 4,274 | none |
| 37 | `switch*[tiab]` | 174,704 | none |
| 38 | `transition*[tiab]` | 435,282 | none |
| 39 | `substitut*[tiab]` | 336,339 | none |
| 40 | `interchangeab*[tiab]` | 10,314 | none |
| 41 | `interchang*[tiab]` | 16,881 | none |
| 42 | `switchback[tiab]` | 207 | none |
| 43 | `switch-back[tiab]` | 269 | none |
| 44 | `#36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43` | 932,982 | none |
| 45 | `#20 AND #35 AND #44` | 658 | none |

### Strategy (single line, for copying into PubMed)

```text
((Biosimilar Pharmaceuticals[Mesh] OR Biological Products[Mesh] OR biosimilar*[tiab] OR follow-on biologic*[tiab] OR follow on biologic*[tiab] OR subsequent entry biologic*[tiab] OR CT-P13[tiab] OR Remsima[tiab] OR Inflectra[tiab] OR SB2[tiab] OR Flixabi[tiab] OR Renflexis[tiab] OR SB4[tiab] OR Benepali[tiab] OR GP2015[tiab] OR Erelzi[tiab] OR ABP 501[tiab] OR Amgevita[tiab] OR Imraldi[tiab]) AND (Tumor Necrosis Factor-alpha[Mesh] OR Infliximab[Mesh] OR Adalimumab[Mesh] OR Etanercept[Mesh] OR Certolizumab Pegol[Mesh] OR infliximab[tiab] OR adalimumab[tiab] OR etanercept[tiab] OR golimumab[tiab] OR certolizumab[tiab] OR anti-TNF[tiab] OR TNF inhibitor*[tiab] OR tumor necrosis factor inhibitor*[tiab] OR tumour necrosis factor inhibitor*[tiab]) AND (Drug Substitution[Mesh] OR switch*[tiab] OR transition*[tiab] OR substitut*[tiab] OR interchangeab*[tiab] OR interchang*[tiab] OR switchback[tiab] OR switch-back[tiab])) AND ("1800/01/01"[edat] : "2021/02/12"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 2 | 2 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| biosimilar | 4,154 | 0 |
| tnf_inhibitor | 11,855 | 0 |
| switching | 9,057 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 658 | initial | none | Initial recall-first strategy: three required topic blocks for biosimilar, TNF-alpha inhibitor, and broad switching/transition process. Direction, indication, outcomes and study design remain screening criteria; no limits. Terms informed by MeSH authority records and a two-study benchmark from references to a prior switch review. |
| 2 | 658 | tnf_inhibitor: +0 / -2 | none | Removed TNF Inhibitors[Mesh] because the vocabulary verification returned an ambiguous canonical record, and Golimumab[Mesh] because no descriptor resolved. Retained the TNF class as searchable text and kept golimumab[tiab] with the other drug names; no benchmark loss is acceptable. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 1 findings; F1 should-fix open
- Round 2 on version 2: 1 findings; F1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 429 NCBI requests logged (224 from cache); strategy sha256 85bfee7bab56._

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
      "requested": "Biosimilar Pharmaceuticals",
      "expected_type": "descriptor",
      "checked_at": "2026-09-27T22:34:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D059451",
          "name": "Biosimilar Pharmaceuticals",
          "type": "descriptor",
          "scope_note": "Biological products that are imitations but not exact replicas of innovator biological products.",
          "tree_numbers": [
            "D20.215.261"
          ],
          "entry_terms": 8,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D059451",
      "preferred_label": "Biosimilar Pharmaceuticals",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "Biosimilar Pharmaceuticals",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Biological Products",
      "expected_type": "descriptor",
      "checked_at": "2026-09-27T22:34:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001688",
          "name": "Biological Products",
          "type": "descriptor",
          "scope_note": "Complex pharmaceutical substances, preparations, or matter derived from organisms usually obtained by biological methods or assay.",
          "tree_numbers": [
            "D20.215"
          ],
          "entry_terms": 31,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001688",
      "preferred_label": "Biological Products",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "Biological Products",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Tumor Necrosis Factor-alpha",
      "expected_type": "descriptor",
      "checked_at": "2026-09-27T22:34:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D014409",
          "name": "Tumor Necrosis Factor-alpha",
          "type": "descriptor",
          "scope_note": "Serum glycoprotein produced by activated MACROPHAGES and other mammalian MONONUCLEAR LEUKOCYTES. It has necrotizing activity against tumor cell lines and increases ability to reject tumor transplants. Also known as TNF-alpha, it is only 30% homologous to TNF-beta (LYMPHOTOXIN), but they share TNF RECEPTORS.",
          "tree_numbers": [
            "D09.400.430.965",
            "D12.644.276.374.500.800",
            "D12.644.276.374.750.626",
            "D12.776.124.900",
            "D12.776.395.930",
            "D12.776.467.374.500.800",
            "D12.776.467.374.750.626",
            "D23.529.374.500.800",
            "D23.529.374.750.626"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D014409",
      "preferred_label": "Tumor Necrosis Factor-alpha",
      "type": "descriptor",
      "location": "vocabulary:20",
      "term": {
        "text": "Tumor Necrosis Factor-alpha",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Infliximab",
      "expected_type": "descriptor",
      "checked_at": "2026-09-27T22:34:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000069285",
          "name": "Infliximab",
          "type": "descriptor",
          "scope_note": "A chimeric monoclonal antibody to TNF-ALPHA that is used in the treatment of RHEUMATOID ARTHRITIS; ANKYLOSING SPONDYLITIS; PSORIATIC ARTHRITIS and CROHN'S DISEASE.",
          "tree_numbers": [
            "D12.776.124.486.485.114.224.608",
            "D12.776.124.790.651.114.224.537",
            "D12.776.377.715.548.114.224.642"
          ],
          "entry_terms": 11,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000069285",
      "preferred_label": "Infliximab",
      "type": "descriptor",
      "location": "vocabulary:21",
      "term": {
        "text": "Infliximab",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adalimumab",
      "expected_type": "descriptor",
      "checked_at": "2026-09-27T22:34:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000068879",
          "name": "Adalimumab",
          "type": "descriptor",
          "scope_note": "A humanized monoclonal antibody that binds specifically to TNF-ALPHA and blocks its interaction with endogenous TNF RECEPTORS to modulate INFLAMMATION. It is used in the treatment of RHEUMATOID ARTHRITIS; PSORIATIC ARTHRITIS; CROHN'S DISEASE and ULCERATIVE COLITIS.",
          "tree_numbers": [
            "D12.776.124.486.485.114.224.060.250",
            "D12.776.124.790.651.114.224.060.250",
            "D12.776.377.715.548.114.224.200.250"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000068879",
      "preferred_label": "Adalimumab",
      "type": "descriptor",
      "location": "vocabulary:22",
      "term": {
        "text": "Adalimumab",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Etanercept",
      "expected_type": "descriptor",
      "checked_at": "2026-09-27T22:34:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000068800",
          "name": "Etanercept",
          "type": "descriptor",
          "scope_note": "A recombinant version of soluble human TNF receptor fused to an IgG FC fragment that binds specifically to TUMOR NECROSIS FACTOR and inhibits its binding with endogenous TNF receptors. It prevents the inflammatory effect of TNF and is used to treat RHEUMATOID ARTHRITIS; PSORIATIC ARTHRITIS and ANKYLOSING SPONDYLITIS.",
          "tree_numbers": [
            "D12.644.541.500.697.624",
            "D12.776.124.486.485.538.500.624",
            "D12.776.124.486.485.680.697.624",
            "D12.776.124.790.651.538.500.624",
            "D12.776.124.790.651.680.660.624",
            "D12.776.377.715.548.538.500.624",
            "D12.776.377.715.548.680.660.624",
            "D12.776.543.750.705.852.760.232"
          ],
          "entry_terms": 15,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000068800",
      "preferred_label": "Etanercept",
      "type": "descriptor",
      "location": "vocabulary:23",
      "term": {
        "text": "Etanercept",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Certolizumab Pegol",
      "expected_type": "descriptor",
      "checked_at": "2026-09-27T22:34:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000068582",
          "name": "Certolizumab Pegol",
          "type": "descriptor",
          "scope_note": "A polyethylene-glycolated Fab' fragment of TUMOR NECROSIS FACTOR antibody that binds specifically to TNF-ALPHA and neutralises it in a dose-dependent manner. It also inhibits the production of lipopolysaccharide-induced TNF-ALPHA and IL-1 BETA and is used to treat RHEUMATOID ARTHRITIS and PSORIATIC ARTHRITIS.",
          "tree_numbers": [
            "D05.750.741.125",
            "D12.644.541.500.650.250",
            "D12.776.124.486.485.114.224.060.500",
            "D12.776.124.486.485.680.650.250",
            "D12.776.124.790.651.114.224.060.500",
            "D12.776.124.790.651.680.650.250",
            "D12.776.377.715.548.114.224.200.500",
            "D12.776.377.715.548.680.650.250"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000068582",
      "preferred_label": "Certolizumab Pegol",
      "type": "descriptor",
      "location": "vocabulary:24",
      "term": {
        "text": "Certolizumab Pegol",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Drug Substitution",
      "expected_type": "descriptor",
      "checked_at": "2026-09-27T22:34:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D057915",
          "name": "Drug Substitution",
          "type": "descriptor",
          "scope_note": "The practice of replacing one prescribed drug with another that is expected to have the same clinical or psychological effect.",
          "tree_numbers": [
            "E02.319.307.312",
            "N02.421.668.778.500.312"
          ],
          "entry_terms": 15,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D057915",
      "preferred_label": "Drug Substitution",
      "type": "descriptor",
      "location": "vocabulary:34",
      "term": {
        "text": "Drug Substitution",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"biosimilar pharmaceuticals\"[MeSH Terms] OR \"biological products\"[MeSH Terms] OR \"biosimilar*\"[Title/Abstract] OR \"follow on biologic*\"[Title/Abstract] OR \"follow on biologic*\"[Title/Abstract] OR \"subsequent entry biologic*\"[Title/Abstract] OR \"CT-P13\"[Title/Abstract] OR \"Remsima\"[Title/Abstract] OR \"Inflectra\"[Title/Abstract] OR \"SB2\"[Title/Abstract] OR \"Flixabi\"[Title/Abstract] OR \"Renflexis\"[Title/Abstract] OR \"SB4\"[Title/Abstract] OR \"Benepali\"[Title/Abstract] OR \"GP2015\"[Title/Abstract] OR \"Erelzi\"[Title/Abstract] OR \"abp 501\"[Title/Abstract] OR \"Amgevita\"[Title/Abstract] OR \"Imraldi\"[Title/Abstract]) AND (\"tumor necrosis factor alpha\"[MeSH Terms] OR \"infliximab\"[MeSH Terms] OR \"adalimumab\"[MeSH Terms] OR \"etanercept\"[MeSH Terms] OR \"certolizumab pegol\"[MeSH Terms] OR \"infliximab\"[Title/Abstract] OR \"adalimumab\"[Title/Abstract] OR \"etanercept\"[Title/Abstract] OR \"golimumab\"[Title/Abstract] OR \"certolizumab\"[Title/Abstract] OR \"anti-TNF\"[Title/Abstract] OR \"tnf inhibitor*\"[Title/Abstract] OR \"tumor necrosis factor inhibitor*\"[Title/Abstract] OR \"tumour necrosis factor inhibitor*\"[Title/Abstract]) AND (\"drug substitution\"[MeSH Terms] OR \"switch*\"[Title/Abstract] OR \"transition*\"[Title/Abstract] OR \"substitut*\"[Title/Abstract] OR \"interchangeab*\"[Title/Abstract] OR \"interchang*\"[Title/Abstract] OR \"switchback\"[Title/Abstract] OR \"switch-back\"[Title/Abstract]) AND 1800/01/01:2021/02/12[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "908f8688ab8f52444399d17a246f64ff095cfc55496a3ba59db53c8a13966859",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched concepts match the scope. The strategy searches switching broadly, while direction and indication remain screening criteria as specified."
        },
        "operators": {
          "verdict": "pass",
          "note": "The three concept blocks are combined with AND and their terms with OR, consistent with the stated searchable concepts."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "The change log says Tumor Necrosis Factor Inhibitors[Mesh] and Golimumab[Mesh] were removed, but gives no rationale or evidence for those removals. Reassess and document them."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The listed individual TNF inhibitor names, including golimumab, have Title/Abstract terms; general biosimilar and switching language is also represented."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The line-numbered strategy uses coherent PubMed field tags, Boolean operators, and set references. No syntax or translation errors are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No study-design, indication, outcome, or publication-date limit is applied. The entry-date boundary is documented as the search's as-of cutoff."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The change log records removal of Tumor Necrosis Factor Inhibitors[Mesh] and Golimumab[Mesh] without a reason or supporting evidence. Golimumab remains as a text word, but the packet does not explain why its heading or the broader class heading was dropped.",
          "recommendation": "Document the basis for each removal and verify whether the headings remain valid and relevant. Restore any heading whose removal is not justified.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 2,
      "review_sha256": "cb1b7977d7852bce2f850df133867709a3550be414f500c5e0a17bb95b21bf03",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The search blocks match the specified searchable concepts. Switching is searched broadly, with direction left for screening as the scope requires; outcomes, indication, and study design are not required."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms within each concept are ORed, and the biosimilar, TNF-inhibitor, and switching blocks are ANDed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet documents removal of Tumor Necrosis Factor Inhibitors[Mesh] because the vocabulary check returned ambiguous duplicate authority matches, and Golimumab[Mesh] because it returned no descriptor match and PubMed returned no items. Golimumab remains in the text-word block."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes biosimilar terminology and product names, TNF-inhibitor class terms and individual drug names, and broad switching and transition terms. The supplied benchmark is retrieved by all three blocks."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The line-numbered strategy uses coherent PubMed field tags, Boolean operators, and set references. The packet reports no lint, translation, or query errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No study-design, indication, outcome, or publication-date limit is applied. The Entrez entry-date boundary of 2021-02-12 is explicitly documented as the evaluation's as-of cutoff."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The prior packet did not explain the removal of Tumor Necrosis Factor Inhibitors[Mesh] and Golimumab[Mesh]. The current packet documents the vocabulary check and rationale for each removal, and retains golimumab as a Title/Abstract term.",
          "recommendation": "Document the basis for each removal and verify whether the headings remain valid and relevant. Restore any heading whose removal is not justified.",
          "status": "resolved",
          "response": "Resolved with the current packet's vocabulary QA evidence: Tumor Necrosis Factor Inhibitors[Mesh] produced ambiguous duplicate authority matches, while Golimumab[Mesh] produced no descriptor match and PubMed returned no items. Golimumab remains searched in [tiab]."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

