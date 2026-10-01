# PubMed search strategy: audit

Generated 2026-10-01T11:54:36+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In people with suspected non-falciparum or Plasmodium vivax malaria in endemic countries, what is the diagnostic accuracy of rapid diagnostic tests for uncomplicated malaria?
- Framework: PIRD
- Scope confirmed by user: no (User asked to proceed without questions. Scope and roles were defined from the stated diagnostic-accuracy question and eligibility criteria; scope was not user-confirmed. No known relevant articles or seeds were supplied. Standard-depth discovery used a focused PubMed pilot; ten eligible records were screened into development/validation sets (7/3). No language or publication-date limit. PubMed Entrez-date cutoff is 2013-06-09 as required by the harness; no publication-date limit. Endemicity, uncomplicated status, eligible reference standard, and accuracy measures are screened rather than AND-ed. The Rapid Diagnostic Tests MeSH descriptor was introduced in 2023, after the requested cutoff, and had zero records under the cutoff; it was removed. Reagent Kits, Diagnostic was retained because it is the established device/test-kit heading and appears on relevant records.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Non-falciparum malaria, including Plasmodium vivax | search | Target diagnosis is essential and searchable. Include broad malaria wording plus vivax and non-falciparum members because papers may name the species without the broader category. |
| Malaria rapid diagnostic tests | search | The index test is essential and usually named as rapid diagnostic test, RDT, or antigen test. |
| Malaria-endemic setting | screen | Study location and endemicity may only be identifiable from methods or full text; no reliable searchable term list captures all endemic countries. |
| Eligible reference standard | screen | Eligible reference standards vary and may not be named in title or abstract. |
| Diagnostic performance | screen | Accuracy measures are inconsistently reported in abstracts; the review is diagnostic accuracy, not screening effectiveness. |
| Uncomplicated malaria | screen | Uncomplicated status may not be stated in titles or abstracts; exclude severe malaria during screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T11:53:54+00:00
- Records added to PubMed up to: 2013-06-09
- Total records: 1,244
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Malaria[Mesh]` | 50,641 | none |
| 2 | `Malaria, Vivax[Mesh]` | 2,872 | none |
| 3 | `Plasmodium vivax[Mesh]` | 3,745 | none |
| 4 | `malaria*[tiab]` | 59,105 | none |
| 5 | `plasmodi*[tiab]` | 35,922 | none |
| 6 | `non-falciparum[tiab]` | 55 | none |
| 7 | `nonfalciparum[tiab]` | 59 | none |
| 8 | `malariae[tiab]` | 888 | none |
| 9 | `ovale[tiab]` | 5,356 | none |
| 10 | `knowlesi[tiab]` | 866 | none |
| 11 | `vivax[tiab]` | 5,921 | none |
| 12 | `benign tertian[tiab]` | 69 | none |
| 13 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12` | 81,813 | none |
| 14 | `Reagent Kits, Diagnostic[Mesh]` | 17,135 | none |
| 15 | `Diagnostic Tests, Routine[Mesh]` | 7,136 | none |
| 16 | `Point-of-Care Systems[Mesh]` | 6,781 | none |
| 17 | `Reagent Strips[Mesh]` | 2,830 | none |
| 18 | `rapid diagnostic test*[tiab]` | 1,321 | none |
| 19 | `rapid diagnos*[tiab]` | 8,326 | none |
| 20 | `rapid test*[tiab]` | 3,281 | none |
| 21 | `RDT[tiab]` | 653 | none |
| 22 | `RDTs[tiab]` | 303 | none |
| 23 | `immunochromatograph*[tiab]` | 1,749 | none |
| 24 | `"lateral flow"[tiab]` | 720 | none |
| 25 | `dipstick test*[tiab]` | 649 | none |
| 26 | `point-of-care test*[tiab]` | 1,572 | none |
| 27 | `antigen test*[tiab]` | 2,616 | none |
| 28 | `"antigen detection"[tiab]` | 3,135 | none |
| 29 | `#14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28` | 48,071 | none |
| 30 | `#13 AND #29` | 1,244 | none |

### Strategy (single line, for copying into PubMed)

```text
((Malaria[Mesh] OR Malaria, Vivax[Mesh] OR Plasmodium vivax[Mesh] OR malaria*[tiab] OR plasmodi*[tiab] OR non-falciparum[tiab] OR nonfalciparum[tiab] OR malariae[tiab] OR ovale[tiab] OR knowlesi[tiab] OR vivax[tiab] OR benign tertian[tiab]) AND (Reagent Kits, Diagnostic[Mesh] OR Diagnostic Tests, Routine[Mesh] OR Point-of-Care Systems[Mesh] OR Reagent Strips[Mesh] OR rapid diagnostic test*[tiab] OR rapid diagnos*[tiab] OR rapid test*[tiab] OR RDT[tiab] OR RDTs[tiab] OR immunochromatograph*[tiab] OR "lateral flow"[tiab] OR dipstick test*[tiab] OR point-of-care test*[tiab] OR antigen test*[tiab] OR "antigen detection"[tiab])) AND ("1800/01/01"[edat] : "2013/06/09"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Non-falciparum malaria, including Plasmodium vivax | 1 | `Plasmodium[Mesh] OR malaria*[tiab] OR parasit*[tiab] OR protozo*[tiab]` | 537 | 0/30 |
| Non-falciparum malaria, including Plasmodium vivax | 2 | `Plasmodium[Mesh] OR malaria*[tiab] OR parasit*[tiab] OR protozo*[tiab]` | 645 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| malaria | 48,071 | 0 |
| rapid_test | 81,813 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial two-block PIRD strategy: diagnosis/species AND rapid diagnostic test; no seeds supplied. |
| 2 | 1,155 | rapid_test: +2 / -2 | none | Fixed proximity syntax by quoting phrases; initial PIRD query. |
| 3 | 1,155 | limits/combination | none | Use default AND combination across diagnosis and index test to allow required category probe. |
| 4 | 1,251 | rapid_test: +1 / -1 | none | Added Reagent Kits, Diagnostic[Mesh] based on its established scope and presence in screened relevant records; removed Rapid Diagnostic Tests[Mesh], introduced in 2023 and outside the 2013 search corpus. Corrected scope_confirmed to false. |
| 5 | 1,244 | rapid_test: +2 / -2 | none | Resolved R1-1 by removing unnecessary proximity operators from the fixed-order phrases lateral flow and antigen detection; now use explicit [tiab] phrase clauses. R1-2 accepted and documented: the harness requires the Entrez-date bound. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 2 findings; R1-1 should-fix open, R1-2 document accepted-risk
- Round 2 on version 5: 2 findings; R1-1 should-fix resolved, R1-2 document accepted-risk
- Round 3 on version 5: 2 findings; R1-1 should-fix resolved, R1-2 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 561 NCBI requests logged (249 from cache); strategy sha256 846e8f34004d._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:malaria",
        "blocking": false,
        "requires_review": true,
        "id": "I-45996a53a1af1ed5c896"
      }
    ],
    "issues": [
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:malaria",
        "blocking": false,
        "requires_review": true,
        "id": "I-45996a53a1af1ed5c896"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Malaria",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:53:54+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D008288",
          "name": "Malaria",
          "type": "descriptor",
          "scope_note": "A protozoan disease caused in humans by four species of the PLASMODIUM genus: PLASMODIUM FALCIPARUM; PLASMODIUM VIVAX; PLASMODIUM OVALE; and PLASMODIUM MALARIAE; and transmitted by the bite of an infected female mosquito of the genus ANOPHELES. Malaria is endemic in parts of Asia, Africa, Central and South America, Oceania, and certain Caribbean islands. It is characterized by extreme exhaustio...",
          "tree_numbers": [
            "C01.610.752.530",
            "C01.920.852.750"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D008288",
      "preferred_label": "Malaria",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "Malaria",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Malaria, Vivax",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:53:54+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D016780",
          "name": "Malaria, Vivax",
          "type": "descriptor",
          "scope_note": "Malaria caused by PLASMODIUM VIVAX. This form of malaria is less severe than MALARIA, FALCIPARUM, but there is a higher probability for relapses to occur. Febrile paroxysms often occur every other day.",
          "tree_numbers": [
            "C01.610.752.530.700",
            "C01.920.852.750.700"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D016780",
      "preferred_label": "Malaria, Vivax",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "Malaria, Vivax",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Plasmodium vivax",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:53:54+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D010966",
          "name": "Plasmodium vivax",
          "type": "descriptor",
          "scope_note": "A protozoan parasite that causes vivax malaria (MALARIA, VIVAX). This species is found almost everywhere malaria is endemic and is the only one that has a range extending into the temperate regions.",
          "tree_numbers": [
            "B01.043.075.380.611.761"
          ],
          "entry_terms": 2,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D010966",
      "preferred_label": "Plasmodium vivax",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "Plasmodium vivax",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Reagent Kits, Diagnostic",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:53:54+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011933",
          "name": "Reagent Kits, Diagnostic",
          "type": "descriptor",
          "scope_note": "Commercially prepared reagent sets, with accessory devices, containing all of the major components and literature necessary to perform one or more designated diagnostic tests or procedures. They may be for laboratory or personal use.",
          "tree_numbers": [
            "D27.505.259.875",
            "D27.720.470.410.680",
            "E07.720"
          ],
          "entry_terms": 16,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011933",
      "preferred_label": "Reagent Kits, Diagnostic",
      "type": "descriptor",
      "location": "vocabulary:13",
      "term": {
        "text": "Reagent Kits, Diagnostic",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diagnostic Tests, Routine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:53:54+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003955",
          "name": "Diagnostic Tests, Routine",
          "type": "descriptor",
          "scope_note": "Diagnostic procedures, such as laboratory tests and x-rays, routinely performed on all individuals or specified categories of individuals in a specified situation, e.g., patients being admitted to the hospital. These include routine tests administered to neonates.",
          "tree_numbers": [
            "E01.370.395"
          ],
          "entry_terms": 27,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003955",
      "preferred_label": "Diagnostic Tests, Routine",
      "type": "descriptor",
      "location": "vocabulary:14",
      "term": {
        "text": "Diagnostic Tests, Routine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Point-of-Care Systems",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:53:54+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D019095",
          "name": "Point-of-Care Systems",
          "type": "descriptor",
          "scope_note": "Laboratory and other services provided to patients at the bedside. These include diagnostic and laboratory testing using automated information entry.",
          "tree_numbers": [
            "N04.452.442.452.452.680",
            "N04.452.515.360.652",
            "N04.590.874"
          ],
          "entry_terms": 12,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D019095",
      "preferred_label": "Point-of-Care Systems",
      "type": "descriptor",
      "location": "vocabulary:15",
      "term": {
        "text": "Point-of-Care Systems",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Reagent Strips",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:53:54+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011934",
          "name": "Reagent Strips",
          "type": "descriptor",
          "scope_note": "Narrow pieces of material impregnated or covered with a substance used to produce a chemical reaction. The strips are used in detecting, measuring, producing, etc., other substances. (From Dorland, 28th ed)",
          "tree_numbers": [
            "D27.505.259.875.680",
            "D27.720.470.410.680.680",
            "E07.720.720"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011934",
      "preferred_label": "Reagent Strips",
      "type": "descriptor",
      "location": "vocabulary:16",
      "term": {
        "text": "Reagent Strips",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"malaria\"[MeSH Terms] OR \"malaria, vivax\"[MeSH Terms] OR \"plasmodium vivax\"[MeSH Terms] OR \"malaria*\"[Title/Abstract] OR \"plasmodi*\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"nonfalciparum\"[Title/Abstract] OR \"malariae\"[Title/Abstract] OR \"ovale\"[Title/Abstract] OR \"knowlesi\"[Title/Abstract] OR \"vivax\"[Title/Abstract] OR \"benign tertian\"[Title/Abstract]) AND (\"reagent kits, diagnostic\"[MeSH Terms] OR \"diagnostic tests, routine\"[MeSH Terms] OR \"point of care systems\"[MeSH Terms] OR \"reagent strips\"[MeSH Terms] OR \"rapid diagnostic test*\"[Title/Abstract] OR \"rapid diagnos*\"[Title/Abstract] OR \"rapid test*\"[Title/Abstract] OR \"RDT\"[Title/Abstract] OR \"RDTs\"[Title/Abstract] OR \"immunochromatograph*\"[Title/Abstract] OR \"lateral flow\"[Title/Abstract] OR \"dipstick test*\"[Title/Abstract] OR \"point of care test*\"[Title/Abstract] OR \"antigen test*\"[Title/Abstract] OR \"antigen detection\"[Title/Abstract]) AND 1800/01/01:2013/06/09[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "abf4d988db14b600204dce0fc101d85f3bc54d032a179b56a2fd39be95e7ad6a",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The search block includes bare terms for vivax and the named non-falciparum species, alongside broader malaria terms."
        },
        "operators": {
          "verdict": "revise",
          "note": "The two proximity expressions need clause-specific interpretation and supporting evidence; the packet provides no reason or evidence for retaining them."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed headings have verified translations. The packet explains why the post-2023 Rapid Diagnostic Tests heading was excluded."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word set covers the named disease members and common RDT, antigen, lateral-flow, and point-of-care wording."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query translated without reported syntax errors or warnings."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The query applies an Entrez-date cutoff of 2013-06-09 despite no publication-date limit; report this as a material search cutoff."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "syntax",
          "finding": "The retained proximity clauses, \"lateral flow\"[tiab:~1] and \"antigen detection\"[tiab:~1], lack clause-specific interpretation, a retention rationale, and evidence in the packet. The per-term counts and overall known-record recall do not establish that these proximity settings are appropriate.",
          "recommendation": "Document why each proximity clause is needed and provide clause-specific evidence, or revise the clauses and run another complete evaluation before adopting the rewrite.",
          "status": "open"
        },
        {
          "id": "R1-2",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "filter",
          "finding": "The search includes records with Entrez dates through 2013-06-09. Although the packet says this cutoff is required by the harness and is not a publication-date limit, it excludes later-entered records and the question itself has no stated time limit.",
          "recommendation": "Clearly label the delivered strategy and its results as limited to records entered by 2013-06-09; rerun without that cutoff for an unrestricted current review search when possible.",
          "status": "accepted-risk",
          "response": "The packet identifies the cutoff as harness-required, so it is recorded as an operational limitation rather than treated as a publication-date limit."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "8a586624a7dd71ef280d6c779d89ecbfbdee8c09e1eae50280f41590b40aa231",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Bare text words cover vivax and the named non-falciparum species alongside broader malaria terms."
        },
        "operators": {
          "verdict": "pass",
          "note": "The strategy combines its disease and test synonym sets with OR, then intersects those blocks with AND. The proximity expressions from the prior round were removed, and the revised strategy was evaluated."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The headings have verified translations; the packet explains the exclusion of the post-2023 Rapid Diagnostic Tests heading."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The terms cover disease names and RDT, antigen, lateral-flow, and point-of-care wording. All ten known records are retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query translated without reported syntax errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez-date cutoff is explicitly identified as harness-required and distinguished from a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "syntax",
          "finding": "The prior finding concerned the two retained proximity clauses, which lacked clause-specific interpretation and evidence.",
          "recommendation": "The clauses were revised to quoted phrases without proximity operators and the complete strategy was evaluated again.",
          "status": "resolved",
          "response": "The current strategy uses \"lateral flow\"[tiab] and \"antigen detection\"[tiab] without proximity operators. The packet reports a fresh evaluation, including translated query syntax and retrieval of all ten known records."
        },
        {
          "id": "R1-2",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "filter",
          "finding": "The strategy is limited to records with Entrez dates through 2013-06-09, although the question has no stated time limit.",
          "recommendation": "Label results as an Entrez-date-limited snapshot; rerun without the cutoff for an unrestricted search when possible.",
          "status": "accepted-risk",
          "response": "The packet explicitly documents that the cutoff is harness-required and is not a publication-date limit. The limitation remains."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-45996a53a1af1ed5c896",
          "status": "accepted-risk",
          "response": "The category probe is stale because the malaria block changed after probing, and its probe budget is spent. No further probe is available in this packet; retain screening for eligibility and do not treat the old probes as current validation of the revised strategy.",
          "evidence": "The validation section identifies category_probe_stale_budget_spent. The two existing probes screened 30 records each and found 0 relevant, but their recorded queries used an earlier test block. The current strategy retrieves all 10 known records, though that does not refresh the category probe."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 5,
      "review_sha256": "8a586624a7dd71ef280d6c779d89ecbfbdee8c09e1eae50280f41590b40aa231",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The strategy includes the named vivax and non-falciparum species terms, alongside broader malaria terms."
        },
        "operators": {
          "verdict": "pass",
          "note": "R1-1 was addressed by removing proximity operators from the phrases and evaluating the revised strategy."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Headings have verified translations, and the packet explains the exclusion of the post-2023 Rapid Diagnostic Tests heading."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The disease and RDT term blocks cover the named concepts, and all ten known records are retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query translated without reported syntax errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "R1-2 remains an accepted risk: the harness-required Entrez-date cutoff is explicitly reported and distinguished from a publication-date limit."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "syntax",
          "finding": "The prior finding concerned proximity operators in the lateral-flow and antigen-detection phrases.",
          "recommendation": "The phrases were revised without proximity operators, followed by a complete evaluation.",
          "status": "resolved",
          "response": "The current strategy uses quoted phrases without proximity operators. The packet reports a fresh evaluation, including query translation and retrieval of all ten known records."
        },
        {
          "id": "R1-2",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "filter",
          "finding": "The strategy is limited to records with Entrez dates through 2013-06-09, though the question has no stated time limit.",
          "recommendation": "Label results as an Entrez-date-limited snapshot; rerun without the cutoff for an unrestricted search when possible.",
          "status": "accepted-risk",
          "response": "The packet documents that this cutoff is harness-required and is not a publication-date limit. The limitation remains."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-45996a53a1af1ed5c896",
          "status": "accepted-risk",
          "response": "The category probe is stale because the block changed after probing, and its probe budget is spent. Keep the stale-probe limitation visible and do not treat the prior probes as current validation.",
          "evidence": "The packet reports category_probe_stale_budget_spent. The existing probes screened 30 records each with 0 relevant, while their recorded queries used an earlier test block. All ten known records are retrieved by the current strategy, but that does not refresh the category probes."
        }
      ]
    }
  ]
}
```

