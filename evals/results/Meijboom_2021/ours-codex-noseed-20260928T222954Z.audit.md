# PubMed search strategy: audit

Generated 2026-09-28T22:47:37+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Patients retransitioning from a biosimilar TNF-alpha inhibitor back to the originator biologic
- Framework: PECO
- Scope confirmed by user: no (No seeds or answers were supplied; proceeding at standard depth as requested. Assumption: the review concerns patients who switched from a TNF-alpha inhibitor biosimilar back to its originator, while search terms cover the broader switching process in either direction. Switch direction and clinical eligibility are screened. No language, date, age, or study-design limits. PubMed records are bounded by PSB_AS_OF=2021-02-12 (Entrez date), without a publication-date limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Biosimilar medicines | search | Defines the exposure; the study must involve a biosimilar, though it may name a product rather than the category. |
| TNF-alpha inhibitors | search | Defines the drug class; eligible records may name only a member of the class. |
| Switching or substitution between biologic products | search | Search the broader process in either direction because switching back is a fragile subset event; screen for biosimilar-to-originator direction. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T22:46:39+00:00
- Records added to PubMed up to: 2021-02-12
- Total records: 393
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Biosimilar Pharmaceuticals"[Mesh]` | 2,555 | none |
| 2 | `biosimilar*[tiab]` | 3,878 | none |
| 3 | `"follow-on biologic"[tiab]` | 29 | none |
| 4 | `"follow on biologic"[tiab]` | 29 | none |
| 5 | `"subsequent entry biologic"[tiab]` | 9 | none |
| 6 | `"CT-P13"[tiab]` | 236 | none |
| 7 | `"SB2"[tiab]` | 449 | none |
| 8 | `"SB4"[tiab]` | 169 | none |
| 9 | `Remsima[tiab]` | 72 | none |
| 10 | `Inflectra[tiab]` | 79 | none |
| 11 | `Flixabi[tiab]` | 14 | none |
| 12 | `Renflexis[tiab]` | 16 | none |
| 13 | `Avsola[tiab]` | 1 | none |
| 14 | `Benepali[tiab]` | 27 | none |
| 15 | `Brenzys[tiab]` | 8 | none |
| 16 | `Erelzi[tiab]` | 15 | none |
| 17 | `Amjevita[tiab]` | 5 | none |
| 18 | `Amgevita[tiab]` | 6 | none |
| 19 | `Hulio[tiab]` | 4 | none |
| 20 | `Hyrimoz[tiab]` | 4 | none |
| 21 | `Imraldi[tiab]` | 13 | none |
| 22 | `Cyltezo[tiab]` | 6 | none |
| 23 | `Idacio[tiab]` | 2 | none |
| 24 | `GP2015[tiab]` | 18 | none |
| 25 | `GP2017[tiab]` | 13 | none |
| 26 | `SB5[tiab]` | 185 | none |
| 27 | `ABP 501[tiab]` | 21 | none |
| 28 | `BI 695501[tiab]` | 11 | none |
| 29 | `FKB327[tiab]` | 10 | none |
| 30 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29` | 4,767 | none |
| 31 | `"Infliximab"[Mesh]` | 11,046 | none |
| 32 | `"Adalimumab"[Mesh]` | 6,043 | none |
| 33 | `"Etanercept"[Mesh]` | 6,162 | none |
| 34 | `"Certolizumab Pegol"[Mesh]` | 674 | none |
| 35 | `"tumor necrosis factor inhibitor"[tiab]` | 414 | none |
| 36 | `"tumour necrosis factor inhibitor"[tiab]` | 171 | none |
| 37 | `"anti-TNF"[tiab]` | 11,204 | none |
| 38 | `"anti TNF"[tiab]` | 11,204 | none |
| 39 | `"TNF inhibitor"[tiab]` | 831 | none |
| 40 | `infliximab[tiab]` | 12,876 | none |
| 41 | `adalimumab[tiab]` | 7,410 | none |
| 42 | `etanercept[tiab]` | 7,154 | none |
| 43 | `golimumab[tiab]` | 1,187 | none |
| 44 | `certolizumab[tiab]` | 1,164 | none |
| 45 | `golimumab[nm]` | 725 | none |
| 46 | `#31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45` | 32,339 | none |
| 47 | `"Drug Substitution"[Mesh]` | 4,274 | none |
| 48 | `switch*[tiab]` | 174,704 | none |
| 49 | `transition*[tiab]` | 435,282 | none |
| 50 | `substitut*[tiab]` | 336,339 | none |
| 51 | `interchangeab*[tiab]` | 10,314 | none |
| 52 | `#47 OR #48 OR #49 OR #50 OR #51` | 927,194 | none |
| 53 | `#30 AND #46 AND #52` | 393 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Biosimilar Pharmaceuticals"[Mesh] OR biosimilar*[tiab] OR "follow-on biologic"[tiab] OR "follow on biologic"[tiab] OR "subsequent entry biologic"[tiab] OR "CT-P13"[tiab] OR "SB2"[tiab] OR "SB4"[tiab] OR Remsima[tiab] OR Inflectra[tiab] OR Flixabi[tiab] OR Renflexis[tiab] OR Avsola[tiab] OR Benepali[tiab] OR Brenzys[tiab] OR Erelzi[tiab] OR Amjevita[tiab] OR Amgevita[tiab] OR Hulio[tiab] OR Hyrimoz[tiab] OR Imraldi[tiab] OR Cyltezo[tiab] OR Idacio[tiab] OR GP2015[tiab] OR GP2017[tiab] OR SB5[tiab] OR ABP 501[tiab] OR BI 695501[tiab] OR FKB327[tiab]) AND ("Infliximab"[Mesh] OR "Adalimumab"[Mesh] OR "Etanercept"[Mesh] OR "Certolizumab Pegol"[Mesh] OR "tumor necrosis factor inhibitor"[tiab] OR "tumour necrosis factor inhibitor"[tiab] OR "anti-TNF"[tiab] OR "anti TNF"[tiab] OR "TNF inhibitor"[tiab] OR infliximab[tiab] OR adalimumab[tiab] OR etanercept[tiab] OR golimumab[tiab] OR certolizumab[tiab] OR golimumab[nm]) AND ("Drug Substitution"[Mesh] OR switch*[tiab] OR transition*[tiab] OR substitut*[tiab] OR interchangeab*[tiab])) AND ("1800/01/01"[edat] : "2021/02/12"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 1 | 1 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Biosimilar medicines | 1 | `biologic*[tiab] OR monoclonal antibod*[tiab] OR Remicade[tiab] OR Remsima[tiab] OR Inflectra[tiab] OR Flixabi[tiab] OR Renflexis[tiab] OR Enbrel[tiab] OR Humira[tiab]` | 698 | 0/30 |
| TNF-alpha inhibitors | 1 | `biologic*[tiab] OR monoclonal antibod*[tiab] OR anti-inflammatory agent*[tiab]` | 337 | 0/30 |
| TNF-alpha inhibitors | 2 | `biologic*[tiab] OR monoclonal antibod*[tiab] OR anti-inflammatory agent*` | 337 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| biosimilar | 1,820 | 0 |
| tnfi | 998 | 0 |
| switching | 1,023 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 394 | initial | none | Initial three-block draft: biosimilar category, TNF inhibitor category including named members, and broader switching/substitution process; direction screened because it is fragile. |
| 2 | 394 | tnfi: +1 / -1; switching: +0 / -1 | none | Corrected golimumab to its supplementary concept [nm] field based on MeSH lookup and removed unsupported phrase-index clause change of therapy; broader switching terms retained. |
| 3 | 393 | tnfi: +0 / -1 | none | Removed ambiguous duplicate MeSH label for TNF inhibitors; drug member MeSH headings and free-text class terms represent the category. |
| 4 | 393 | biosimilar: +21 / -0 | none | Addressed critic F1 by adding TNF biosimilar brand names and product identifiers (including names surfaced in the category-probe query) to reduce dependence on explicit biosimilar wording. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 1 findings; F1 should-fix open
- Round 2 on version 4: 1 findings; F1 should-fix resolved
- Round 3 on version 4: 1 findings; F1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 771 NCBI requests logged (327 from cache); strategy sha256 060df96c6b7d._

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
      "checked_at": "2026-09-28T22:46:39+00:00",
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
      "requested": "Infliximab",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:46:39+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "\"Infliximab\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adalimumab",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:46:39+00:00",
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
      "location": "vocabulary:31",
      "term": {
        "text": "\"Adalimumab\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Etanercept",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:46:39+00:00",
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
      "location": "vocabulary:32",
      "term": {
        "text": "\"Etanercept\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Certolizumab Pegol",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:46:39+00:00",
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
      "location": "vocabulary:33",
      "term": {
        "text": "\"Certolizumab Pegol\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "golimumab",
      "expected_type": "supplementary",
      "checked_at": "2026-09-28T22:46:39+00:00",
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
      "location": "vocabulary:44",
      "term": {
        "text": "golimumab",
        "tag": "nm",
        "field": "nm"
      }
    },
    {
      "requested": "Drug Substitution",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:46:39+00:00",
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
      "location": "vocabulary:45",
      "term": {
        "text": "\"Drug Substitution\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Biosimilar Pharmaceuticals\"[MeSH Terms] OR \"biosimilar*\"[Title/Abstract] OR \"follow-on biologic\"[Title/Abstract] OR \"follow-on biologic\"[Title/Abstract] OR \"subsequent entry biologic\"[Title/Abstract] OR \"CT-P13\"[Title/Abstract] OR \"SB2\"[Title/Abstract] OR \"SB4\"[Title/Abstract] OR \"Remsima\"[Title/Abstract] OR \"Inflectra\"[Title/Abstract] OR \"Flixabi\"[Title/Abstract] OR \"Renflexis\"[Title/Abstract] OR \"Avsola\"[Title/Abstract] OR \"Benepali\"[Title/Abstract] OR \"Brenzys\"[Title/Abstract] OR \"Erelzi\"[Title/Abstract] OR \"Amjevita\"[Title/Abstract] OR \"Amgevita\"[Title/Abstract] OR \"Hulio\"[Title/Abstract] OR \"Hyrimoz\"[Title/Abstract] OR \"Imraldi\"[Title/Abstract] OR \"Cyltezo\"[Title/Abstract] OR \"Idacio\"[Title/Abstract] OR \"GP2015\"[Title/Abstract] OR \"GP2017\"[Title/Abstract] OR \"SB5\"[Title/Abstract] OR \"abp 501\"[Title/Abstract] OR \"bi 695501\"[Title/Abstract] OR \"FKB327\"[Title/Abstract]) AND (\"Infliximab\"[MeSH Terms] OR \"Adalimumab\"[MeSH Terms] OR \"Etanercept\"[MeSH Terms] OR \"Certolizumab Pegol\"[MeSH Terms] OR \"tumor necrosis factor inhibitor\"[Title/Abstract] OR \"tumour necrosis factor inhibitor\"[Title/Abstract] OR \"anti tnf\"[Title/Abstract] OR \"anti tnf\"[Title/Abstract] OR \"TNF inhibitor\"[Title/Abstract] OR \"Infliximab\"[Title/Abstract] OR \"Adalimumab\"[Title/Abstract] OR \"Etanercept\"[Title/Abstract] OR \"golimumab\"[Title/Abstract] OR \"certolizumab\"[Title/Abstract] OR \"golimumab\"[Supplementary Concept]) AND (\"Drug Substitution\"[MeSH Terms] OR \"switch*\"[Title/Abstract] OR \"transition*\"[Title/Abstract] OR \"substitut*\"[Title/Abstract] OR \"interchangeab*\"[Title/Abstract]) AND 1800/01/01:2021/02/12[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "36a6203c7e634c276267edb556f92f48e3ea135e5aee5d12dad201b6d6e0b0d1",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The blocks and Boolean structure match the stated concepts, but the biosimilar block may miss eligible records that name a biosimilar product without using a category term."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within each concept and AND across the three required concepts fit the stated scope."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The supplied vocabulary checks verify the selected MeSH headings and the golimumab supplementary concept."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The biosimilar block has selected product codes, but no biosimilar brand names. The packet's broader probe names Remsima, Inflectra, Flixabi, and Renflexis, illustrating a possible route to records that do not say biosimilar."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The tested lines show no syntax errors or warnings; the final query retrieves the supplied relevant record."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, date-of-publication, age, or study-design restriction is applied. The Entrez date bound is documented in the protocol."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The biosimilar block may miss eligible TNF-inhibitor biosimilar studies that identify the biosimilar by product brand without using biosimilar-category language. The packet's broader probe includes Remsima, Inflectra, Flixabi, and Renflexis, none of which appears in the block. Screening 30 records with no relevant hits does not establish that these names can be omitted.",
          "recommendation": "Assess and add applicable TNF-inhibitor biosimilar brand names as bare title/abstract terms, including names surfaced in the packet's probe; then rerun the complete strategy evaluation.",
          "status": "open",
          "response": null
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "c3c05a7af5f66b81fa7e984c9f3f1ba979963e4ea779138d85cdeec867a5a914",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The three searched concepts and their combination match the stated scope. The strategy searches switching in either direction, leaving direction for screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within each concept and AND across the biosimilar, TNF-inhibitor, and switching blocks fit the eligibility criteria."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verified MeSH headings for the selected drug and substitution terms, and verifies golimumab as a supplementary concept."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The biosimilar block now includes bare title/abstract brand terms for Remsima, Inflectra, Flixabi, and Renflexis, as well as other TNF-inhibitor biosimilar brands and product codes. This resolves F1."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The tested lines show no syntax errors or warnings, and the final query retrieves the supplied relevant record."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, publication-date, age, or study-design limit is applied. The Entrez date bound is documented in the protocol."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The biosimilar block may miss eligible TNF-inhibitor biosimilar studies that identify the biosimilar by product brand without using biosimilar-category language.",
          "recommendation": "Assess and add applicable TNF-inhibitor biosimilar brand names as bare title/abstract terms, including names surfaced in the packet's probe; then rerun the complete strategy evaluation.",
          "status": "resolved",
          "response": "The current biosimilar block includes bare title/abstract terms for Remsima, Inflectra, Flixabi, and Renflexis, plus other TNF-inhibitor biosimilar brands and product codes. The packet records a complete evaluation for strategy version 4."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "c3c05a7af5f66b81fa7e984c9f3f1ba979963e4ea779138d85cdeec867a5a914",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The three searched concepts and their combination match the stated scope; switching is searched in either direction so eligible direction can be screened."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within each concept and AND across the three required concepts fit the stated eligibility criteria."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verification of the selected MeSH headings and golimumab supplementary concept."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The biosimilar block includes bare title/abstract terms for the brand names identified in F1, along with other product brands and codes."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The tested lines report no syntax errors or warnings, and the final query retrieves the supplied relevant record."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, publication-date, age, or study-design limit is applied; the Entrez date bound is documented in the protocol."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The biosimilar block may miss eligible TNF-inhibitor biosimilar studies that identify the biosimilar by product brand without using biosimilar-category language.",
          "recommendation": "Assess and add applicable TNF-inhibitor biosimilar brand names as bare title/abstract terms, including names surfaced in the packet's probe; then rerun the complete strategy evaluation.",
          "status": "resolved",
          "response": "The current biosimilar block includes bare title/abstract terms for Remsima, Inflectra, Flixabi, and Renflexis, plus other TNF-inhibitor biosimilar brands and product codes. The packet records a complete evaluation for strategy version 4."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

