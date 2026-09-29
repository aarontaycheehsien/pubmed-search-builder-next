# PubMed search strategy: audit

Generated 2026-09-28T23:21:45+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Patients retransitioning from a biosimilar TNF-alpha inhibitor back to the originator biologic
- Framework: PECO
- Scope confirmed by user: no (User supplied no known relevant articles and cannot answer questions during this run; proceeded at standard depth without pausing. Assumed the population is humans receiving TNF-alpha inhibitor biosimilars and the event of interest is a switch back to the originator/reference product. No date, language, or study-design limits. Direction and biosimilar/originator status will be screened. This is a search-development assumption rather than user-confirmed scope.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| TNF-alpha inhibitors (including named drug members) | search | The drug class defines the intervention; abstracts may identify only a member drug, so individual drug names and available drug headings are included. |
| Switching or substitution process between products | search | The topic concerns retransitioning. Search broadly for switching processes in either direction because back-switching is a fragile secondary event; screen the direction and biosimilar/originator status. |
| Biosimilar product status | optional | This defines the exposure of interest, but requiring authors to label the product as a biosimilar may miss reports naming only the products. Test its retrieval and loss sample before deciding. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T23:20:20+00:00
- Records added to PubMed up to: 2021-02-12
- Total records: 396
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Infliximab[Mesh]` | 11,046 | none |
| 2 | `Adalimumab[Mesh]` | 6,043 | none |
| 3 | `Etanercept[Mesh]` | 6,162 | none |
| 4 | `Golimumab[nm]` | 725 | none |
| 5 | `Certolizumab Pegol[Mesh]` | 674 | none |
| 6 | `infliximab[tiab]` | 12,876 | none |
| 7 | `adalimumab[tiab]` | 7,410 | none |
| 8 | `etanercept[tiab]` | 7,154 | none |
| 9 | `golimumab[tiab]` | 1,187 | none |
| 10 | `Simponi[tiab]` | 36 | none |
| 11 | `"CNTO-148"[tiab]` | 4 | none |
| 12 | `"CNTO 148"[tiab]` | 4 | none |
| 13 | `certolizumab[tiab]` | 1,164 | none |
| 14 | `"anti-TNF"[tiab]` | 11,204 | none |
| 15 | `"TNF inhibitor"[tiab]` | 831 | none |
| 16 | `"tumor necrosis factor inhibitor"[tiab]` | 414 | none |
| 17 | `"tumour necrosis factor inhibitor"[tiab]` | 171 | none |
| 18 | `"anti-tumor necrosis factor"[tiab]` | 4,120 | none |
| 19 | `"anti-tumour necrosis factor"[tiab]` | 1,418 | none |
| 20 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19` | 34,003 | none |
| 21 | `Drug Substitution[Mesh]` | 4,274 | none |
| 22 | `switch*[tiab]` | 174,704 | none |
| 23 | `transition*[tiab]` | 435,282 | none |
| 24 | `substitut*[tiab]` | 336,339 | none |
| 25 | `interchangeab*[tiab]` | 10,314 | none |
| 26 | `retransition*[tiab]` | 7 | none |
| 27 | `reintroduc*[tiab]` | 11,529 | none |
| 28 | `restart*[tiab]` | 6,354 | none |
| 29 | `revert*[tiab]` | 25,295 | none |
| 30 | `return*[tiab]` | 250,007 | none |
| 31 | `#21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30` | 1,207,637 | none |
| 32 | `Biosimilar Pharmaceuticals[Mesh]` | 2,555 | none |
| 33 | `biosimilar*[tiab]` | 3,878 | none |
| 34 | `"follow-on biologic"[tiab]` | 29 | none |
| 35 | `"follow on biologic"[tiab]` | 29 | none |
| 36 | `"subsequent entry biologic"[tiab]` | 9 | none |
| 37 | `"CT-P13"[tiab]` | 236 | none |
| 38 | `"SB2"[tiab]` | 449 | none |
| 39 | `"SB4"[tiab]` | 169 | none |
| 40 | `"SB5"[tiab]` | 185 | none |
| 41 | `"GP2015"[tiab]` | 18 | none |
| 42 | `"GP2017"[tiab]` | 13 | none |
| 43 | `"ABP 501"[tiab]` | 21 | none |
| 44 | `"BI 695501"[tiab]` | 11 | none |
| 45 | `"PF-06438179"[tiab]` | 13 | none |
| 46 | `"infliximab-dyyb"[tiab]` | 19 | none |
| 47 | `"infliximab-abda"[tiab]` | 7 | none |
| 48 | `"etanercept-szzs"[tiab]` | 1 | none |
| 49 | `"adalimumab-atto"[tiab]` | 1 | none |
| 50 | `"adalimumab-adbm"[tiab]` | 1 | none |
| 51 | `"adalimumab-bwwd"[tiab]` | 0 | warning: pubmed_warning; warning: zero_hits |
| 52 | `"adalimumab-fkjp"[tiab]` | 0 | warning: pubmed_warning; warning: zero_hits |
| 53 | `"Remsima"[tiab]` | 72 | none |
| 54 | `"Inflectra"[tiab]` | 79 | none |
| 55 | `"Renflexis"[tiab]` | 16 | none |
| 56 | `"Flixabi"[tiab]` | 14 | none |
| 57 | `"Benepali"[tiab]` | 27 | none |
| 58 | `"Erelzi"[tiab]` | 15 | none |
| 59 | `"Amjevita"[tiab]` | 5 | none |
| 60 | `"Amgevita"[tiab]` | 6 | none |
| 61 | `"Imraldi"[tiab]` | 13 | none |
| 62 | `"Hyrimoz"[tiab]` | 4 | none |
| 63 | `"Cyltezo"[tiab]` | 6 | none |
| 64 | `"Idacio"[tiab]` | 2 | none |
| 65 | `"Hulio"[tiab]` | 4 | none |
| 66 | `"Zessly"[tiab]` | 4 | none |
| 67 | `"Ixifi"[tiab]` | 7 | none |
| 68 | `#32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67` | 4,769 | none |
| 69 | `#20 AND #31 AND #68` | 396 | none |

### Strategy (single line, for copying into PubMed)

```text
((Infliximab[Mesh] OR Adalimumab[Mesh] OR Etanercept[Mesh] OR Golimumab[nm] OR Certolizumab Pegol[Mesh] OR infliximab[tiab] OR adalimumab[tiab] OR etanercept[tiab] OR golimumab[tiab] OR Simponi[tiab] OR "CNTO-148"[tiab] OR "CNTO 148"[tiab] OR certolizumab[tiab] OR "anti-TNF"[tiab] OR "TNF inhibitor"[tiab] OR "tumor necrosis factor inhibitor"[tiab] OR "tumour necrosis factor inhibitor"[tiab] OR "anti-tumor necrosis factor"[tiab] OR "anti-tumour necrosis factor"[tiab]) AND (Drug Substitution[Mesh] OR switch*[tiab] OR transition*[tiab] OR substitut*[tiab] OR interchangeab*[tiab] OR retransition*[tiab] OR reintroduc*[tiab] OR restart*[tiab] OR revert*[tiab] OR return*[tiab]) AND (Biosimilar Pharmaceuticals[Mesh] OR biosimilar*[tiab] OR "follow-on biologic"[tiab] OR "follow on biologic"[tiab] OR "subsequent entry biologic"[tiab] OR "CT-P13"[tiab] OR "SB2"[tiab] OR "SB4"[tiab] OR "SB5"[tiab] OR "GP2015"[tiab] OR "GP2017"[tiab] OR "ABP 501"[tiab] OR "BI 695501"[tiab] OR "PF-06438179"[tiab] OR "infliximab-dyyb"[tiab] OR "infliximab-abda"[tiab] OR "etanercept-szzs"[tiab] OR "adalimumab-atto"[tiab] OR "adalimumab-adbm"[tiab] OR "adalimumab-bwwd"[tiab] OR "adalimumab-fkjp"[tiab] OR "Remsima"[tiab] OR "Inflectra"[tiab] OR "Renflexis"[tiab] OR "Flixabi"[tiab] OR "Benepali"[tiab] OR "Erelzi"[tiab] OR "Amjevita"[tiab] OR "Amgevita"[tiab] OR "Imraldi"[tiab] OR "Hyrimoz"[tiab] OR "Cyltezo"[tiab] OR "Idacio"[tiab] OR "Hulio"[tiab] OR "Zessly"[tiab] OR "Ixifi"[tiab])) AND ("1800/01/01"[edat] : "2021/02/12"[edat])
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
| Biosimilar product status | AND-ed | 2,281 / 396 | 82.6% | none | 0/30 (up to 10% of removed records could be relevant) | Reconfirmed after adding the verified Golimumab supplementary concept: current evaluation reports a material reduction from 2,281 records without the biosimilar block to 396 with it; all nine screened relevant records are retained, and none of the current 30-record loss sample met eligibility. The sample does not exclude residual false-negative risk, which remains documented. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| TNF-alpha inhibitors (including named drug members) | 1 | `((biologic*[tiab] OR biological therap*[tiab] OR biological product*[tiab] OR biologic agent*[tiab] OR Biological Products[Mesh]) AND (switch*[tiab] OR transition*[tiab] OR substitut*[tiab] OR reintroduc*[tiab]))` | 57,864 | 0/30 |
| TNF-alpha inhibitors (including named drug members) | 2 | `(biologic*[tiab] OR biological therap*[tiab] OR biological product*[tiab] OR biologic agent*[tiab] OR Biological Products[Mesh])` | 475 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| tnfi | 1,022 | 0 |
| switching | 1,029 | 0 |
| biosimilar | 2,281 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 5,766 | initial | none | Initial broad search blocks: TNF inhibitor class/member drugs AND switching process; biosimilar status remains optional. Added two screened records from a prior systematic review's references that explicitly report re-establishing or switching back to originator after biosimilar use. |
| 2 | 2,281 | tnfi: +0 / -3 | none | Removed the TNF-alpha cytokine heading because it is not an inhibitor heading; removed an unverified Golimumab MeSH clause. Kept validated drug headings and title/abstract drug names. This also addresses the heading ambiguity/translation warnings. |
| 3 | 396 | biosimilar: +37 / -0 | none | Promoted the biosimilar status block to required after its optional loss sample: it materially reduces retrieval, retains both screened relevant records, and no sampled excluded record met eligibility. Recorded a category probe of broader biologic therapy/switch wording; 0 of 30 outside-block sample records were relevant. |
| 4 | 396 | biosimilar: +0 / -1 | none | live finalization attempt |
| 5 | 396 | biosimilar: +0 / -2 | none | Removed two quoted adalimumab suffix clauses with zero retrieval and PubMed warning under the fixed entry-date snapshot; other generic and brand names remain. No known relevant record was lost. |
| 6 | 396 | biosimilar: +2 / -0 | none | Restored two valid title/abstract biosimilar suffix clauses so the screened second category probe remains bound to the current strategy; retained them despite zero counts in the bounded record set and documented that evidence. |
| 7 | 396 | tnfi: +4 / -0 | none | Added Golimumab as a verified supplementary concept (Golimumab[nm]) and its Simponi/CNTO-148 title-abstract entry terms after internal critic recommendation; the descriptor label is not available. This adds terms to the current category block, so the two screened probes remain valid. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 6: 1 findings; F1 should-fix open
- Round 2 on version 7: 1 findings; F1 should-fix resolved
- Round 3 on version 7: 1 findings; F1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1443 NCBI requests logged (780 from cache); strategy sha256 c93618a7855a._

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
        "query": "(\"adalimumab-bwwd\"[tiab]) AND (\"1800/01/01\"[edat] : \"2021/02/12\"[edat])",
        "translation": "\"adalimumab-bwwd\"[Title/Abstract] AND 1800/01/01:2021/02/12[Date - Entry]",
        "location": "line:51",
        "blocking": false,
        "requires_review": true,
        "id": "I-63ce9099d7afeaa67230"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(\"adalimumab-bwwd\"[tiab]) AND (\"1800/01/01\"[edat] : \"2021/02/12\"[edat])",
        "translation": "\"adalimumab-bwwd\"[Title/Abstract] AND 1800/01/01:2021/02/12[Date - Entry]",
        "location": "line:51",
        "blocking": false,
        "requires_review": true,
        "id": "I-bdc8e0018fd297339711"
      },
      {
        "severity": "warning",
        "code": "pubmed_warning",
        "message": "PubMed reported a warning; review the translation.",
        "evidence": "outputmessages: No items found.",
        "query": "(\"adalimumab-fkjp\"[tiab]) AND (\"1800/01/01\"[edat] : \"2021/02/12\"[edat])",
        "translation": "\"adalimumab-fkjp\"[Title/Abstract] AND 1800/01/01:2021/02/12[Date - Entry]",
        "location": "line:52",
        "blocking": false,
        "requires_review": true,
        "id": "I-99914e9566817d033e0c"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(\"adalimumab-fkjp\"[tiab]) AND (\"1800/01/01\"[edat] : \"2021/02/12\"[edat])",
        "translation": "\"adalimumab-fkjp\"[Title/Abstract] AND 1800/01/01:2021/02/12[Date - Entry]",
        "location": "line:52",
        "blocking": false,
        "requires_review": true,
        "id": "I-ea450a9ab396ab74a26d"
      }
    ],
    "issues": [
      {
        "severity": "warning",
        "code": "pubmed_warning",
        "message": "PubMed reported a warning; review the translation.",
        "evidence": "outputmessages: No items found.",
        "query": "(\"adalimumab-bwwd\"[tiab]) AND (\"1800/01/01\"[edat] : \"2021/02/12\"[edat])",
        "translation": "\"adalimumab-bwwd\"[Title/Abstract] AND 1800/01/01:2021/02/12[Date - Entry]",
        "location": "line:51",
        "blocking": false,
        "requires_review": true,
        "id": "I-63ce9099d7afeaa67230"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(\"adalimumab-bwwd\"[tiab]) AND (\"1800/01/01\"[edat] : \"2021/02/12\"[edat])",
        "translation": "\"adalimumab-bwwd\"[Title/Abstract] AND 1800/01/01:2021/02/12[Date - Entry]",
        "location": "line:51",
        "blocking": false,
        "requires_review": true,
        "id": "I-bdc8e0018fd297339711"
      },
      {
        "severity": "warning",
        "code": "pubmed_warning",
        "message": "PubMed reported a warning; review the translation.",
        "evidence": "outputmessages: No items found.",
        "query": "(\"adalimumab-fkjp\"[tiab]) AND (\"1800/01/01\"[edat] : \"2021/02/12\"[edat])",
        "translation": "\"adalimumab-fkjp\"[Title/Abstract] AND 1800/01/01:2021/02/12[Date - Entry]",
        "location": "line:52",
        "blocking": false,
        "requires_review": true,
        "id": "I-99914e9566817d033e0c"
      },
      {
        "severity": "warning",
        "code": "zero_hits",
        "message": "Zero hits: inspect spelling, restrictions and Boolean role; do not infer redundancy from seeds",
        "query": "(\"adalimumab-fkjp\"[tiab]) AND (\"1800/01/01\"[edat] : \"2021/02/12\"[edat])",
        "translation": "\"adalimumab-fkjp\"[Title/Abstract] AND 1800/01/01:2021/02/12[Date - Entry]",
        "location": "line:52",
        "blocking": false,
        "requires_review": true,
        "id": "I-ea450a9ab396ab74a26d"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Infliximab",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:20:20+00:00",
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
      "location": "vocabulary:1",
      "term": {
        "text": "Infliximab",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adalimumab",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:20:20+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "Adalimumab",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Etanercept",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:20:20+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "Etanercept",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Golimumab",
      "expected_type": "supplementary",
      "checked_at": "2026-09-28T23:20:20+00:00",
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
      "location": "vocabulary:4",
      "term": {
        "text": "Golimumab",
        "tag": "nm",
        "field": "nm"
      }
    },
    {
      "requested": "Certolizumab Pegol",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:20:20+00:00",
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
      "location": "vocabulary:5",
      "term": {
        "text": "Certolizumab Pegol",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Drug Substitution",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:20:20+00:00",
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
      "location": "vocabulary:20",
      "term": {
        "text": "Drug Substitution",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Biosimilar Pharmaceuticals",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:20:20+00:00",
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
      "location": "vocabulary:30",
      "term": {
        "text": "Biosimilar Pharmaceuticals",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"infliximab\"[MeSH Terms] OR \"adalimumab\"[MeSH Terms] OR \"etanercept\"[MeSH Terms] OR \"golimumab\"[Supplementary Concept] OR \"certolizumab pegol\"[MeSH Terms] OR \"infliximab\"[Title/Abstract] OR \"adalimumab\"[Title/Abstract] OR \"etanercept\"[Title/Abstract] OR \"golimumab\"[Title/Abstract] OR \"Simponi\"[Title/Abstract] OR \"cnto 148\"[Title/Abstract] OR \"cnto 148\"[Title/Abstract] OR \"certolizumab\"[Title/Abstract] OR \"anti-TNF\"[Title/Abstract] OR \"TNF inhibitor\"[Title/Abstract] OR \"tumor necrosis factor inhibitor\"[Title/Abstract] OR \"tumour necrosis factor inhibitor\"[Title/Abstract] OR \"anti-tumor necrosis factor\"[Title/Abstract] OR \"anti-tumour necrosis factor\"[Title/Abstract]) AND (\"drug substitution\"[MeSH Terms] OR \"switch*\"[Title/Abstract] OR \"transition*\"[Title/Abstract] OR \"substitut*\"[Title/Abstract] OR \"interchangeab*\"[Title/Abstract] OR \"retransition*\"[Title/Abstract] OR \"reintroduc*\"[Title/Abstract] OR \"restart*\"[Title/Abstract] OR \"revert*\"[Title/Abstract] OR \"return*\"[Title/Abstract]) AND (\"biosimilar pharmaceuticals\"[MeSH Terms] OR \"biosimilar*\"[Title/Abstract] OR \"follow-on biologic\"[Title/Abstract] OR \"follow-on biologic\"[Title/Abstract] OR \"subsequent entry biologic\"[Title/Abstract] OR \"CT-P13\"[Title/Abstract] OR \"SB2\"[Title/Abstract] OR \"SB4\"[Title/Abstract] OR \"SB5\"[Title/Abstract] OR \"GP2015\"[Title/Abstract] OR \"GP2017\"[Title/Abstract] OR \"ABP 501\"[Title/Abstract] OR \"BI 695501\"[Title/Abstract] OR \"PF-06438179\"[Title/Abstract] OR \"infliximab-dyyb\"[Title/Abstract] OR \"infliximab-abda\"[Title/Abstract] OR \"etanercept-szzs\"[Title/Abstract] OR \"adalimumab-atto\"[Title/Abstract] OR \"adalimumab-adbm\"[Title/Abstract] OR \"adalimumab-bwwd\"[Title/Abstract] OR \"adalimumab-fkjp\"[Title/Abstract] OR \"Remsima\"[Title/Abstract] OR \"Inflectra\"[Title/Abstract] OR \"Renflexis\"[Title/Abstract] OR \"Flixabi\"[Title/Abstract] OR \"Benepali\"[Title/Abstract] OR \"Erelzi\"[Title/Abstract] OR \"Amjevita\"[Title/Abstract] OR \"Amgevita\"[Title/Abstract] OR \"Imraldi\"[Title/Abstract] OR \"Hyrimoz\"[Title/Abstract] OR \"Cyltezo\"[Title/Abstract] OR \"Idacio\"[Title/Abstract] OR \"Hulio\"[Title/Abstract] OR \"Zessly\"[Title/Abstract] OR \"Ixifi\"[Title/Abstract]) AND 1800/01/01:2021/02/12[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 6,
      "review_sha256": "12dd33285bbe90e30286a08e4e2cd7ef0a0e28aff23a6e78cb25d28ffd32ad00",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no translation issues. The two zero-hit clauses retain their Title/Abstract field and hyphenated wording in PubMed’s translation."
        },
        "operators": {
          "verdict": "pass",
          "note": "The drug, switching-process, and biosimilar blocks are joined with AND; terms within each block are joined with OR. The switching block searches broadly for process terms rather than requiring a back-switch direction."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "The strategy includes a free-text golimumab term but no Golimumab MeSH heading. Check and add the heading if available for the intended search date."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The searched member drugs and switching terms are represented by explicit expressions. The packet’s two zero-hit biosimilar name clauses are addressed in the issue dispositions."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query is explicitly grouped, uses no proximity operators, and has no reported query-level syntax or translation errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No population or study-design filter is applied. The entry-date cutoff is stated as 2021-02-12 and should be reported with the strategy."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The searched member-drug list includes golimumab[tiab], but the TNF-alpha block has no Golimumab MeSH expression. The rationale says individual drug names and available drug headings are included.",
          "recommendation": "Check whether Golimumab[Mesh] is available for the intended search date; if so, add it to the TNF-alpha block, test its translation, and rerun the complete evaluation.",
          "status": "open",
          "response": ""
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-e270b68aaf22a7a6b9fd",
          "status": "accepted-risk",
          "response": "The warning applies to the exact clause \"adalimumab-bwwd\"[tiab] with the stated entry-date cutoff. Retain it as a product-name variant; as an OR arm, its zero hits do not invalidate the rest of the block.",
          "evidence": "The packet reports zero hits and PubMed’s translation as \"adalimumab-bwwd\"[Title/Abstract] AND 1800/01/01:2021/02/12[Date - Entry]."
        },
        {
          "issue_id": "I-38668fb0cb138579e2c1",
          "status": "accepted-risk",
          "response": "The warning applies to the exact clause \"adalimumab-bwwd\"[tiab] with the stated entry-date cutoff. Retain it as a product-name variant; as an OR arm, its zero hits do not invalidate the rest of the block.",
          "evidence": "The packet reports zero hits for this clause under the cutoff and shows the intended Title/Abstract translation."
        },
        {
          "issue_id": "I-6b49487d241e6104c9f4",
          "status": "accepted-risk",
          "response": "The warning applies to the exact clause \"adalimumab-fkjp\"[tiab] with the stated entry-date cutoff. Retain it as a product-name variant; as an OR arm, its zero hits do not invalidate the rest of the block.",
          "evidence": "The packet reports zero hits and PubMed’s translation as \"adalimumab-fkjp\"[Title/Abstract] AND 1800/01/01:2021/02/12[Date - Entry]."
        },
        {
          "issue_id": "I-c844e966966d626a1fe2",
          "status": "accepted-risk",
          "response": "The warning applies to the exact clause \"adalimumab-fkjp\"[tiab] with the stated entry-date cutoff. Retain it as a product-name variant; as an OR arm, its zero hits do not invalidate the rest of the block.",
          "evidence": "The packet reports zero hits for this clause under the cutoff and shows the intended Title/Abstract translation."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 7,
      "review_sha256": "e4e743d782533ba1a2fffd5055a9c52d9130b89e198262129c06a27fd05ea6bf",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet shows the zero-hit product-name clauses retain their quoted wording and Title/Abstract field, with the stated entry-date cutoff in PubMed’s translation. No query-level translation error is reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The drug, switching-process, and biosimilar blocks are combined with AND, with terms within each block combined by OR. Switching terms cover the process broadly without requiring a direction."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "A separate psb MeSH lookup for Golimumab returned the supplementary concept C529000 and no descriptor. The strategy searches this with Golimumab[nm] and includes its entry terms in [tiab]."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The searched TNF inhibitor members have bare-name text clauses, and the switching block includes broad process terms. The zero-hit biosimilar name variants remain explicit OR arms with documented reasons for retention."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final combination is explicitly grouped, uses no proximity operators, and has no reported query-level syntax errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No population or study-design filter is applied. The entry-date cutoff is 2021-02-12 and should be reported with the strategy."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The searched member-drug list includes golimumab[tiab], but the TNF-alpha block has no Golimumab MeSH expression. The rationale says individual drug names and available drug headings are included.",
          "recommendation": "Check whether Golimumab[Mesh] is available for the intended search date; if so, add it to the TNF-alpha block, test its translation, and rerun the complete evaluation.",
          "status": "resolved",
          "response": "Checked with `psb mesh lookup \"Golimumab\"`: NCBI returned the supplementary concept C529000, not a descriptor heading. `psb mesh show C529000` returned the entry terms Simponi, CNTO-148, and CNTO 148; the search therefore includes `Golimumab[nm]` and these [tiab] names. The full evaluation validated these clauses, retained all nine relevant development records, and showed no known-record loss."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-63ce9099d7afeaa67230",
          "status": "accepted-risk",
          "response": "Retain the exact product-name variant as an OR arm. Its zero hits do not invalidate the other clauses, and the warning does not indicate a changed field or query translation.",
          "evidence": "The packet reports zero hits for (\"adalimumab-bwwd\"[tiab]) with the entry-date cutoff and shows the translation as \"adalimumab-bwwd\"[Title/Abstract] AND 1800/01/01:2021/02/12[Date - Entry]."
        },
        {
          "issue_id": "I-bdc8e0018fd297339711",
          "status": "accepted-risk",
          "response": "Retain the exact product-name variant as an OR arm. Its zero hits do not invalidate the other clauses, and the warning does not indicate a changed field or query translation.",
          "evidence": "The packet reports zero hits for (\"adalimumab-bwwd\"[tiab]) with the entry-date cutoff and shows the translation as \"adalimumab-bwwd\"[Title/Abstract] AND 1800/01/01:2021/02/12[Date - Entry]."
        },
        {
          "issue_id": "I-99914e9566817d033e0c",
          "status": "accepted-risk",
          "response": "Retain the exact product-name variant as an OR arm. Its zero hits do not invalidate the other clauses, and the warning does not indicate a changed field or query translation.",
          "evidence": "The packet reports zero hits for (\"adalimumab-fkjp\"[tiab]) with the entry-date cutoff and shows the translation as \"adalimumab-fkjp\"[Title/Abstract] AND 1800/01/01:2021/02/12[Date - Entry]."
        },
        {
          "issue_id": "I-ea450a9ab396ab74a26d",
          "status": "accepted-risk",
          "response": "Retain the exact product-name variant as an OR arm. Its zero hits do not invalidate the other clauses, and the warning does not indicate a changed field or query translation.",
          "evidence": "The packet reports zero hits for (\"adalimumab-fkjp\"[tiab]) with the entry-date cutoff and shows the translation as \"adalimumab-fkjp\"[Title/Abstract] AND 1800/01/01:2021/02/12[Date - Entry]."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 7,
      "review_sha256": "e4e743d782533ba1a2fffd5055a9c52d9130b89e198262129c06a27fd05ea6bf",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two zero-hit product-name clauses retain their quoted Title/Abstract wording and the stated entry-date cutoff in PubMed's translations. The warnings report no items found; no field or translation error is shown."
        },
        "operators": {
          "verdict": "pass",
          "note": "The TNF inhibitor, switching-process, and biosimilar blocks are combined with AND, and terms within each block are combined with OR. Switching is searched broadly in either direction for screening."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The earlier Golimumab heading finding was addressed: the lookup identified supplementary concept C529000 rather than a descriptor, and the strategy includes Golimumab[nm] plus its entry terms in Title/Abstract."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes bare-name clauses for the TNF inhibitor members and broad process terms. The zero-hit biosimilar name variants remain explicit OR arms with clause-specific dispositions."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The strategy is explicitly grouped, uses no proximity operators, and reports no query-level syntax errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No population or study-design filter is applied. The entry-date cutoff is 2021-02-12 and should be reported with the strategy."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The searched member-drug list includes golimumab[tiab], but the TNF-alpha block has no Golimumab MeSH expression. The rationale says individual drug names and available drug headings are included.",
          "recommendation": "Check whether Golimumab[Mesh] is available for the intended search date; if so, add it to the TNF-alpha block, test its translation, and rerun the complete evaluation.",
          "status": "resolved",
          "response": "The lookup found supplementary concept C529000, not a Golimumab descriptor heading. The strategy searches Golimumab[nm] and includes the listed entry terms Simponi, CNTO-148, and CNTO 148 in Title/Abstract. The packet reports that the full evaluation validated these clauses, retained all nine relevant development records, and had no known-record loss."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-63ce9099d7afeaa67230",
          "status": "accepted-risk",
          "response": "Retain the exact product-name variant as an OR arm. Its warning is specific to this clause and reports no items found; the translated field and wording are as intended.",
          "evidence": "The packet shows the query (\"adalimumab-bwwd\"[tiab]) with the entry-date cutoff, zero hits, and translation as \"adalimumab-bwwd\"[Title/Abstract] AND 1800/01/01:2021/02/12[Date - Entry]."
        },
        {
          "issue_id": "I-bdc8e0018fd297339711",
          "status": "accepted-risk",
          "response": "Retain the exact product-name variant as an OR arm. Zero hits for this clause do not invalidate the other clauses in the biosimilar block.",
          "evidence": "The packet shows the query (\"adalimumab-bwwd\"[tiab]) with the entry-date cutoff, zero hits, and the intended Title/Abstract translation."
        },
        {
          "issue_id": "I-99914e9566817d033e0c",
          "status": "accepted-risk",
          "response": "Retain the exact product-name variant as an OR arm. Its warning is specific to this clause and reports no items found; the translated field and wording are as intended.",
          "evidence": "The packet shows the query (\"adalimumab-fkjp\"[tiab]) with the entry-date cutoff, zero hits, and translation as \"adalimumab-fkjp\"[Title/Abstract] AND 1800/01/01:2021/02/12[Date - Entry]."
        },
        {
          "issue_id": "I-ea450a9ab396ab74a26d",
          "status": "accepted-risk",
          "response": "Retain the exact product-name variant as an OR arm. Zero hits for this clause do not invalidate the other clauses in the biosimilar block.",
          "evidence": "The packet shows the query (\"adalimumab-fkjp\"[tiab]) with the entry-date cutoff, zero hits, and the intended Title/Abstract translation."
        }
      ]
    }
  ]
}
```

