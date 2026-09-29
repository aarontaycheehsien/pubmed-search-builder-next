# PubMed search strategy: audit

Generated 2026-09-28T22:28:51+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Patients retransitioning from a biosimilar TNF-alpha inhibitor back to the originator biologic
- Framework: PECO
- Scope confirmed by user: no (User asked to proceed without questions; scope assumptions were not confirmed. Search both biosimilar and TNF-alpha inhibitor categories. Treat the direction/event of switching back as a screening criterion because it may be a secondary or full-text finding; search the parent switching process broadly if a process block is later tested. No known relevant articles were supplied. No date, language, or design limits. The run is constrained by the harness through PSB_AS_OF=2021-02-12 (Entrez-date bound); do not apply a publication-date filter. The parent switch process is tested as an optional block, rather than searching only a reverse-switch phrase.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Biosimilar medicines | search | The exposure-defining medicine category is searchable, but relevant records may name individual biosimilar products rather than biosimilars generally. |
| TNF-alpha inhibitors | search | The medication class is required by the question; records may name a specific member (for example, infliximab, etanercept, or adalimumab) without saying TNF inhibitor. |
| Switching between biosimilar and originator products | optional | The parent switch process is searchable and may greatly reduce screening, but requiring it could lose studies that report switch-back only under broad discontinuation or treatment-persistence language. Test the parent process block; screen the reverse direction. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T22:27:52+00:00
- Records added to PubMed up to: 2021-02-12
- Total records: 400
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Biosimilar Pharmaceuticals"[Mesh]` | 2,555 | none |
| 2 | `biosimilar*[tiab]` | 3,878 | none |
| 3 | `"follow-on biologic*"[tiab]` | 114 | none |
| 4 | `"subsequent entry biologic*"[tiab]` | 23 | none |
| 5 | `"similar biologic*"[tiab]` | 1,772 | none |
| 6 | `"similar biological medicinal product*"[tiab]` | 25 | none |
| 7 | `"bio-originator*"[tiab]` | 24 | none |
| 8 | `CT-P13[tiab]` | 236 | none |
| 9 | `Remsima[tiab]` | 72 | none |
| 10 | `Inflectra[tiab]` | 79 | none |
| 11 | `Renflexis[tiab]` | 16 | none |
| 12 | `SB2[tiab]` | 449 | none |
| 13 | `GP1111[tiab]` | 12 | none |
| 14 | `PF-06438179[tiab]` | 13 | none |
| 15 | `SB4[tiab]` | 169 | none |
| 16 | `Benepali[tiab]` | 27 | none |
| 17 | `GP2015[tiab]` | 18 | none |
| 18 | `Erelzi[tiab]` | 15 | none |
| 19 | `ABP 501[tiab]` | 21 | none |
| 20 | `Amjevita[tiab]` | 5 | none |
| 21 | `Cyltezo[tiab]` | 6 | none |
| 22 | `Hyrimoz[tiab]` | 4 | none |
| 23 | `Imraldi[tiab]` | 13 | none |
| 24 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23` | 6,369 | none |
| 25 | `"Infliximab"[Mesh]` | 11,046 | none |
| 26 | `"Etanercept"[Mesh]` | 6,162 | none |
| 27 | `"Adalimumab"[Mesh]` | 6,043 | none |
| 28 | `"Certolizumab Pegol"[Mesh]` | 674 | none |
| 29 | `"tumor necrosis factor inhibitor*"[tiab]` | 1,136 | none |
| 30 | `"tumour necrosis factor inhibitor*"[tiab]` | 431 | none |
| 31 | `"TNF inhibitor*"[tiab]` | 2,009 | none |
| 32 | `"TNF-alpha inhibitor*"[tiab]` | 1,833 | none |
| 33 | `anti-TNF[tiab]` | 11,204 | none |
| 34 | `infliximab[tiab]` | 12,876 | none |
| 35 | `etanercept[tiab]` | 7,154 | none |
| 36 | `adalimumab[tiab]` | 7,410 | none |
| 37 | `certolizumab[tiab]` | 1,164 | none |
| 38 | `golimumab[tiab]` | 1,187 | none |
| 39 | `#25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38` | 34,017 | none |
| 40 | `"Drug Substitution"[Mesh]` | 4,274 | none |
| 41 | `switch*[tiab]` | 174,704 | none |
| 42 | `transition*[tiab]` | 435,282 | none |
| 43 | `substitut*[tiab]` | 336,339 | none |
| 44 | `interchangeab*[tiab]` | 10,314 | none |
| 45 | `"switch back"[tiab:~2]` | 292 | none |
| 46 | `"reverse switch*"[tiab]` | 26 | none |
| 47 | `"back-switch*"[tiab]` | 18 | none |
| 48 | `revert*[tiab]` | 25,295 | none |
| 49 | `resum*[tiab]` | 31,725 | none |
| 50 | `re-establish*[tiab]` | 9,092 | none |
| 51 | `#40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50` | 988,478 | none |
| 52 | `#24 AND #39 AND #51` | 400 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Biosimilar Pharmaceuticals"[Mesh] OR biosimilar*[tiab] OR "follow-on biologic*"[tiab] OR "subsequent entry biologic*"[tiab] OR "similar biologic*"[tiab] OR "similar biological medicinal product*"[tiab] OR "bio-originator*"[tiab] OR CT-P13[tiab] OR Remsima[tiab] OR Inflectra[tiab] OR Renflexis[tiab] OR SB2[tiab] OR GP1111[tiab] OR PF-06438179[tiab] OR SB4[tiab] OR Benepali[tiab] OR GP2015[tiab] OR Erelzi[tiab] OR ABP 501[tiab] OR Amjevita[tiab] OR Cyltezo[tiab] OR Hyrimoz[tiab] OR Imraldi[tiab]) AND ("Infliximab"[Mesh] OR "Etanercept"[Mesh] OR "Adalimumab"[Mesh] OR "Certolizumab Pegol"[Mesh] OR "tumor necrosis factor inhibitor*"[tiab] OR "tumour necrosis factor inhibitor*"[tiab] OR "TNF inhibitor*"[tiab] OR "TNF-alpha inhibitor*"[tiab] OR anti-TNF[tiab] OR infliximab[tiab] OR etanercept[tiab] OR adalimumab[tiab] OR certolizumab[tiab] OR golimumab[tiab]) AND ("Drug Substitution"[Mesh] OR switch*[tiab] OR transition*[tiab] OR substitut*[tiab] OR interchangeab*[tiab] OR "switch back"[tiab:~2] OR "reverse switch*"[tiab] OR "back-switch*"[tiab] OR revert*[tiab] OR resum*[tiab] OR re-establish*[tiab])) AND ("1800/01/01"[edat] : "2021/02/12"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 10 | 10 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Switching between biosimilar and originator products | AND-ed | 1,046 / 400 | 61.8% | none | 0/30 (up to 10% of removed records could be relevant) | Fresh decision for the current strategy fingerprint: the parent-process block cuts the candidate set by 61.8%, no known relevant record is lost, and the same 30 records in the refreshed loss sample were screened against the eligibility criteria with none relevant. Keep the parent process block and screen the reverse direction. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Biosimilar medicines | 1 | `biologic*[tiab] OR biological[tiab] OR immunotherap*[tiab]` | 707 | 0/30 |
| Biosimilar medicines | 2 | `biologic*[tiab] OR biological[tiab] OR immunotherap*[tiab]` | 707 | 0/30 |
| TNF-alpha inhibitors | 1 | `biologic*[tiab] OR biological[tiab] OR immunotherap*[tiab]` | 404 | 0/30 |
| TNF-alpha inhibitors | 2 | `biologic*[tiab] OR biological[tiab] OR immunotherap*[tiab]` | 404 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| biosimilar | 2,039 | 0 |
| tnfi | 1,069 | 0 |
| switch_process | 1,046 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,047 | initial | none | First draft: two required medication-category blocks; test the broad parent switching process as optional. Mined terms from 10 screened relevant records; direction remains a screening criterion. |
| 2 | 1,046 | tnfi: +0 / -1 | none | Removed the MeSH class heading after the validator returned two conflicting descriptor summaries; retain its class wording in text plus verified member-drug headings. |
| 3 | 400 | switch_process: +11 / -0 | none | AND-ed the optional parent switching process after no known loss, 0/30 relevant in loss sample, and 61.8% reduction. |
| 4 | 400 | biosimilar: +0 / -1; tnfi: +0 / -2 | none | Removed duplicate free-text variants with identical PubMed translations per F1 (follow-on biologic, TNF-alpha inhibitor, and anti-TNF). Retained the distinct UK tumor/tumour spelling alternatives. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3 (Same-context critic: only the packet was used; no fresh-context reviewer was available.): 1 findings; F1 should-fix open
- Round 2 on version 4 (Same-context critic: only packet 2 was used; no fresh-context reviewer was available.): 2 findings; F1 should-fix resolved, F2 must-fix open
- Round 3 on version 4 (Closing same-context critic: checked only packet 3 and its evidence because no fresh-context reviewer was available.): 2 findings; F1 should-fix resolved, F2 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1153 NCBI requests logged (573 from cache); strategy sha256 9ef423ecb693._

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
      "checked_at": "2026-09-28T22:27:52+00:00",
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
      "checked_at": "2026-09-28T22:27:52+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "\"Infliximab\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Etanercept",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:27:52+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "\"Etanercept\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adalimumab",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:27:52+00:00",
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
      "location": "vocabulary:26",
      "term": {
        "text": "\"Adalimumab\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Certolizumab Pegol",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:27:52+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "\"Certolizumab Pegol\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Drug Substitution",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:27:52+00:00",
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
      "location": "vocabulary:38",
      "term": {
        "text": "\"Drug Substitution\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Biosimilar Pharmaceuticals\"[MeSH Terms] OR \"biosimilar*\"[Title/Abstract] OR \"follow on biologic*\"[Title/Abstract] OR \"subsequent entry biologic*\"[Title/Abstract] OR \"similar biologic*\"[Title/Abstract] OR \"similar biological medicinal product*\"[Title/Abstract] OR \"bio originator*\"[Title/Abstract] OR \"CT-P13\"[Title/Abstract] OR \"Remsima\"[Title/Abstract] OR \"Inflectra\"[Title/Abstract] OR \"Renflexis\"[Title/Abstract] OR \"SB2\"[Title/Abstract] OR \"GP1111\"[Title/Abstract] OR \"PF-06438179\"[Title/Abstract] OR \"SB4\"[Title/Abstract] OR \"Benepali\"[Title/Abstract] OR \"GP2015\"[Title/Abstract] OR \"Erelzi\"[Title/Abstract] OR \"abp 501\"[Title/Abstract] OR \"Amjevita\"[Title/Abstract] OR \"Cyltezo\"[Title/Abstract] OR \"Hyrimoz\"[Title/Abstract] OR \"Imraldi\"[Title/Abstract]) AND (\"Infliximab\"[MeSH Terms] OR \"Etanercept\"[MeSH Terms] OR \"Adalimumab\"[MeSH Terms] OR \"Certolizumab Pegol\"[MeSH Terms] OR \"tumor necrosis factor inhibitor*\"[Title/Abstract] OR \"tumour necrosis factor inhibitor*\"[Title/Abstract] OR \"tnf inhibitor*\"[Title/Abstract] OR \"tnf alpha inhibitor*\"[Title/Abstract] OR \"anti-TNF\"[Title/Abstract] OR \"Infliximab\"[Title/Abstract] OR \"Etanercept\"[Title/Abstract] OR \"Adalimumab\"[Title/Abstract] OR \"certolizumab\"[Title/Abstract] OR \"golimumab\"[Title/Abstract]) AND (\"Drug Substitution\"[MeSH Terms] OR \"switch*\"[Title/Abstract] OR \"transition*\"[Title/Abstract] OR \"substitut*\"[Title/Abstract] OR \"interchangeab*\"[Title/Abstract] OR \"switch back\"[Title/Abstract:~2] OR \"reverse switch*\"[Title/Abstract] OR \"back switch*\"[Title/Abstract] OR \"revert*\"[Title/Abstract] OR \"resum*\"[Title/Abstract] OR \"re establish*\"[Title/Abstract]) AND 1800/01/01:2021/02/12[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "74c40f2b7bdf8d41018a5517c090bf88969f7965a16534d3552bfb955e8d49b8",
      "note": "Same-context critic: only the packet was used; no fresh-context reviewer was available.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The required medication concepts are AND-ed, direction is screened, and the parent switch process was tested as optional before AND-ing."
        },
        "operators": {
          "verdict": "pass",
          "note": "The OR alternatives are grouped within each concept and the three measured blocks are AND-ed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Biosimilar Pharmaceuticals and verified MeSH descriptors for infliximab, etanercept, adalimumab, certolizumab pegol, and Drug Substitution are included; no unsupported heading remains."
        },
        "text_words": {
          "verdict": "revise",
          "note": "PubMed translation normalizes several hyphenated/spaced alternatives to identical clauses; remove duplicate spellings to simplify the final strategy and retest."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Fields and syntax are valid; no live translation warning remains."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No date, language, or design limits were imposed; the tested Entrez entry-date bound is supplied by the harness."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "biosimilar",
          "finding": "The free-text alternatives \"follow-on biologic*\" and \"follow on biologic*\" have the same PubMed translation and count. Likewise \"bio-originator*\" normalizes to \"bio originator*\". The TNFi block also contains duplicate normalized pairs: tumor/tumour are distinct, but TNF-alpha/TNF alpha and anti-TNF/anti TNF translate identically.",
          "recommendation": "Remove one member from each identical normalized pair while retaining the distinct UK spelling alternative; rerun a complete evaluation and check that no known record is lost.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "0618d3e8dc3eb5a9f97a61c5c3b9f65acf2bd7ab6dc5441fddcb27f6bbc664fb",
      "note": "Same-context critic: only packet 2 was used; no fresh-context reviewer was available.",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The duplicate text variants are removed. The current packet exposes stale optional and category-probe evidence after that vocabulary edit; refresh all of these checks before delivery."
        },
        "operators": {
          "verdict": "pass",
          "note": "The grouped OR blocks and AND combination remain correct."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The checked headings are appropriate and authority-verified in the current evaluation."
        },
        "text_words": {
          "verdict": "pass",
          "note": "F1 is resolved. The current search retains the unique text variants and tested product names."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Field tags and translations are valid with no phrase warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No discretionary filters or limits were added."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "biosimilar",
          "finding": "The free-text alternatives \"follow-on biologic*\" and \"follow on biologic*\" have the same PubMed translation and count. The TNFi block also contains duplicate normalized pairs: TNF-alpha/TNF alpha and anti-TNF/anti TNF translate identically.",
          "recommendation": "Remove one member from each identical normalized pair while retaining the distinct UK spelling alternative; rerun a complete evaluation and check that no known record is lost.",
          "status": "resolved",
          "response": "Removed the duplicate forms and reran evaluation. The query count remained 400, the change record lists no known losses, all 10 development records remain retrieved, and there are no translation warnings."
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "structural",
          "block": "switch_process",
          "finding": "The vocabulary edit changed the strategy fingerprint and made the previously recorded optional loss-sample decision and both category probes stale. Evaluation now blocks on category_probe_stale for biosimilar and TNFi, while the optional decision is marked stale.",
          "recommendation": "Redraw and screen the optional loss sample, make a fresh decision for the current block, and redraw/screen both category probes before delivery.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "f16db8ae2dff3f6dcc9b7b0962e6b0fdf2572b41443a8a0cee325862af527196",
      "note": "Closing same-context critic: checked only packet 3 and its evidence because no fresh-context reviewer was available.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The switch direction remains a screening criterion; current parent-process optional decision and both category probes are screened and current."
        },
        "operators": {
          "verdict": "pass",
          "note": "The OR terms are grouped within concept blocks and the current tested blocks are AND-ed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The current strategy retains authority-verified Biosimilar Pharmaceuticals, TNFi member-drug descriptors, and Drug Substitution headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The identical normalized variants identified in F1 have been removed, and the current translations show no warnings."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All lines are field-tagged and the current PubMed translation is valid."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No discretionary limits or filters are used; the Entrez-date bound remains the harness setting."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "biosimilar",
          "finding": "The free-text alternatives \"follow-on biologic*\" and \"follow on biologic*\" had the same PubMed translation and count. The TNFi block also had duplicate normalized pairs: TNF-alpha/TNF alpha and anti-TNF/anti TNF translated identically.",
          "recommendation": "Remove one member from each identical normalized pair while retaining the distinct UK spelling alternative; rerun a complete evaluation and check that no known record is lost.",
          "status": "resolved",
          "response": "Removed the repeated forms. The final evaluation still retrieves all 10 screened development records, the query count stayed 400, and no translation warnings remain."
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "structural",
          "block": "switch_process",
          "finding": "The vocabulary edit made the optional loss-sample decision and both category probes stale.",
          "recommendation": "Redraw and screen the optional loss sample, make a fresh decision for the current block, and redraw/screen both category probes before delivery.",
          "status": "resolved",
          "response": "Repeated the optional sample and re-recorded the decision against the current fingerprint. Its 30 records were screened from abstracts (the draw reproduced the previously screened PMIDs); none was eligible, there was no known-record loss, and the block reduces results by 61.8%. Redrew both category probes; each reproduced the same 30 previously screened PMIDs, none relevant. The current evaluation reports no validation blockers."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

