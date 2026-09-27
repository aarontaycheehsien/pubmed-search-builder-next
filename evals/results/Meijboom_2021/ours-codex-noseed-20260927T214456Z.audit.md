# PubMed search strategy: audit

Generated 2026-09-27T21:57:24+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Patients retransitioning from a biosimilar TNF-alpha inhibitor back to the originator biologic
- Framework: PICO (switching process; direction/outcome screened)
- Scope confirmed by user: no (User asked to proceed without follow-up questions; scope interprets retransitioning as a switch from a biosimilar back to the reference/originator product. Search the broader biosimilar TNF inhibitor topic using paired biosimilar and molecule/class terms, including named biosimilar codes and brands; screen switch direction because back-switch events may be secondary or reported only in full text. Treat PubMed records as available only through Entrez date 2021-02-12; no publication-date limit. No user-supplied seed articles; three eligible records were discovered and screened in for development. No web search used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Biosimilar TNF-alpha inhibitors | search | The review concerns biosimilar TNF inhibitors. Pair biosimilar vocabulary with TNF inhibitor class, generic drug, or biosimilar product identifiers in the single required topic block; use MeSH plus title/abstract terms. |
| Switching between biosimilar and originator biologics, in either direction | screen | Reverse switching is a fragile direction/event and may appear only as a secondary result or full-text detail. Do not require switching vocabulary as an AND block; screen for it among biosimilar TNF inhibitor records. |
| Originator biologic comparator | screen | The originator comparator is implicit in the target switch and inconsistently named/indexed; confirm the product direction at screening. |
| Patient population and clinical condition | screen | Underlying conditions and patient setting are not specified and should not narrow the search. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-27T21:57:10+00:00
- Records added to PubMed up to: 2021-02-12
- Total records: 1,056
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `("Biosimilar Pharmaceuticals"[Mesh] AND ("Tumor Necrosis Factor-alpha"[Mesh] OR "Infliximab"[Mesh] OR "Etanercept"[Mesh] OR "Adalimumab"[Mesh] OR "Certolizumab Pegol"[Mesh] OR "Golimumab"[nm]))` | 652 | none |
| 2 | `(biosimilar*[tiab] OR bio-similar*[tiab] OR "follow-on biologic*"[tiab] OR "subsequent entry biologic*"[tiab]) AND ("tumor necrosis factor"[tiab] OR "tumour necrosis factor"[tiab] OR "anti-TNF"[tiab] OR "anti TNF"[tiab] OR TNF[tiab] OR infliximab[tiab] OR etanercept[tiab] OR adalimumab[tiab] OR certolizumab[tiab] OR golimumab[tiab] OR CT-P13[tiab] OR SB2[tiab] OR SB4[tiab] OR GP1111[tiab] OR GP2015[tiab] OR GP2017[tiab] OR "ABP 501"[tiab] OR "BI 695501"[tiab] OR "PF-06438179"[tiab] OR Remsima[tiab] OR Inflectra[tiab] OR Flixabi[tiab] OR Zessly[tiab] OR Renflexis[tiab] OR Ixifi[tiab] OR Benepali[tiab] OR Erelzi[tiab] OR Amjevita[tiab] OR Amgevita[tiab] OR Cyltezo[tiab] OR Hyrimoz[tiab] OR Imraldi[tiab] OR Hulio[tiab])` | 983 | none |
| 3 | `#1 OR #2` | 1,056 | none |

### Strategy (single line, for copying into PubMed)

```text
((("Biosimilar Pharmaceuticals"[Mesh] AND ("Tumor Necrosis Factor-alpha"[Mesh] OR "Infliximab"[Mesh] OR "Etanercept"[Mesh] OR "Adalimumab"[Mesh] OR "Certolizumab Pegol"[Mesh] OR "Golimumab"[nm])) OR ((biosimilar*[tiab] OR bio-similar*[tiab] OR "follow-on biologic*"[tiab] OR "subsequent entry biologic*"[tiab]) AND ("tumor necrosis factor"[tiab] OR "tumour necrosis factor"[tiab] OR "anti-TNF"[tiab] OR "anti TNF"[tiab] OR TNF[tiab] OR infliximab[tiab] OR etanercept[tiab] OR adalimumab[tiab] OR certolizumab[tiab] OR golimumab[tiab] OR CT-P13[tiab] OR SB2[tiab] OR SB4[tiab] OR GP1111[tiab] OR GP2015[tiab] OR GP2017[tiab] OR "ABP 501"[tiab] OR "BI 695501"[tiab] OR "PF-06438179"[tiab] OR Remsima[tiab] OR Inflectra[tiab] OR Flixabi[tiab] OR Zessly[tiab] OR Renflexis[tiab] OR Ixifi[tiab] OR Benepali[tiab] OR Erelzi[tiab] OR Amjevita[tiab] OR Amgevita[tiab] OR Cyltezo[tiab] OR Hyrimoz[tiab] OR Imraldi[tiab] OR Hulio[tiab])))) AND ("1800/01/01"[edat] : "2021/02/12"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,057 | initial | none | Initial recall-first draft: pair the biosimilar descriptor/free text with TNF inhibitor class, molecule names, and known biosimilar codes/brands. Screen switch direction because back-switch may be a secondary event; apply Entrez cutoff 2021-02-12 and no other limits. |
| 2 | 1,056 | biosimilar_tnfi: +1 / -1 | none | Remove the ambiguously resolved Tumor Necrosis Factor Inhibitors descriptor and unsupported Golimumab MeSH term. Keep validated biosimilar and molecule headings, with golimumab retained in title/abstract vocabulary; the free-text layer explicitly covers it. |
| 3 | 1,056 | biosimilar_tnfi: +1 / -1 | none | Address critic R1-01 by adding Golimumab as its verified NCBI supplementary concept ([nm], UI C529000), not as an unsupported MeSH descriptor; it was retained in title/abstract terms already. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 1 findings; F1-01 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 328 NCBI requests logged (181 from cache); strategy sha256 e6e395b8dae7._

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
      "checked_at": "2026-09-27T21:57:10+00:00",
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
        "text": "\"Biosimilar Pharmaceuticals\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Tumor Necrosis Factor-alpha",
      "expected_type": "descriptor",
      "checked_at": "2026-09-27T21:57:10+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"Tumor Necrosis Factor-alpha\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Infliximab",
      "expected_type": "descriptor",
      "checked_at": "2026-09-27T21:57:10+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "\"Infliximab\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Etanercept",
      "expected_type": "descriptor",
      "checked_at": "2026-09-27T21:57:10+00:00",
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
      "location": "vocabulary:4",
      "term": {
        "text": "\"Etanercept\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adalimumab",
      "expected_type": "descriptor",
      "checked_at": "2026-09-27T21:57:10+00:00",
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
      "location": "vocabulary:5",
      "term": {
        "text": "\"Adalimumab\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Certolizumab Pegol",
      "expected_type": "descriptor",
      "checked_at": "2026-09-27T21:57:10+00:00",
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
      "location": "vocabulary:6",
      "term": {
        "text": "\"Certolizumab Pegol\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Golimumab",
      "expected_type": "supplementary",
      "checked_at": "2026-09-27T21:57:10+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "C529000",
          "name": "golimumab",
          "type": "supplementary",
          "scope_note": "Golimumab plus MTX effectively reduces the signs and symptoms of RA and is generally well tolerated in patients with an inadequate response to MTX.",
          "tree_numbers": [
            "@173764"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "C529000",
      "preferred_label": "golimumab",
      "type": "supplementary",
      "location": "vocabulary:7",
      "term": {
        "text": "\"Golimumab\"",
        "tag": "nm",
        "field": "nm"
      }
    }
  ],
  "translation": "((\"Biosimilar Pharmaceuticals\"[MeSH Terms] AND (\"Tumor Necrosis Factor-alpha\"[MeSH Terms] OR \"Infliximab\"[MeSH Terms] OR \"Etanercept\"[MeSH Terms] OR \"Adalimumab\"[MeSH Terms] OR \"Certolizumab Pegol\"[MeSH Terms] OR \"Golimumab\"[Supplementary Concept])) OR ((\"biosimilar*\"[Title/Abstract] OR \"bio similar*\"[Title/Abstract] OR \"follow on biologic*\"[Title/Abstract] OR \"subsequent entry biologic*\"[Title/Abstract]) AND (\"tumor necrosis factor\"[Title/Abstract] OR \"tumour necrosis factor\"[Title/Abstract] OR \"anti tnf\"[Title/Abstract] OR \"anti tnf\"[Title/Abstract] OR \"TNF\"[Title/Abstract] OR \"Infliximab\"[Title/Abstract] OR \"Etanercept\"[Title/Abstract] OR \"Adalimumab\"[Title/Abstract] OR \"certolizumab\"[Title/Abstract] OR \"Golimumab\"[Title/Abstract] OR \"CT-P13\"[Title/Abstract] OR \"SB2\"[Title/Abstract] OR \"SB4\"[Title/Abstract] OR \"GP1111\"[Title/Abstract] OR \"GP2015\"[Title/Abstract] OR \"GP2017\"[Title/Abstract] OR \"ABP 501\"[Title/Abstract] OR \"BI 695501\"[Title/Abstract] OR \"PF-06438179\"[Title/Abstract] OR \"Remsima\"[Title/Abstract] OR \"Inflectra\"[Title/Abstract] OR \"Flixabi\"[Title/Abstract] OR \"Zessly\"[Title/Abstract] OR \"Renflexis\"[Title/Abstract] OR \"Ixifi\"[Title/Abstract] OR \"Benepali\"[Title/Abstract] OR \"Erelzi\"[Title/Abstract] OR \"Amjevita\"[Title/Abstract] OR \"Amgevita\"[Title/Abstract] OR \"Cyltezo\"[Title/Abstract] OR \"Hyrimoz\"[Title/Abstract] OR \"Imraldi\"[Title/Abstract] OR \"Hulio\"[Title/Abstract]))) AND 1800/01/01:2021/02/12[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "174cf63da5ed3409668f10c03c6914130312806a58af0f26ab1625cd7a653aa4",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The required biosimilar TNF inhibitor block matches the protocol; reverse-switch direction and comparator remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "The query correctly pairs biosimilar terms with TNF class, drug, and product terms, and combines controlled vocabulary and text-word branches."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Descriptor terms are verified, and golimumab is included via its verified supplementary concept [nm]."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text words include biosimilar variants, TNF inhibitor class/generic names, and named biosimilar products."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Current evaluation has no syntax, translation, or validation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The as-of date is an Entrez entry-date wrapper only; no publication-date or other eligibility filter is used. The exact wrapper and its implicit application to every displayed line are documented in narrative.md."
        }
      },
      "findings": [
        {
          "id": "F1-01",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The displayed search lines do not include the EDAT cutoff of 2021/02/12, although the complete evidence shows that cutoff in the executed queries and the reported counts are for the cutoff-limited searches. A reader running the displayed lines would not reproduce those counts or the stated record set.",
          "recommendation": "Show the EDAT restriction with the search lines and combination, or clearly label the displayed expressions as having an implicit cutoff and provide the exact tested, cutoff-limited versions alongside them.",
          "status": "resolved",
          "response": "Added a Date-bound line counts section to narrative.md. It explicitly states that every line and set check carries the exact tested wrapper 1800/01/01:2021/02/12[Date - Entry], that the generated full query carries it, and that it is only the harness snapshot control. The wrapper is composed with each displayed line as part of the reported as-of evaluation, while the review strategy has no publication-date limit."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

