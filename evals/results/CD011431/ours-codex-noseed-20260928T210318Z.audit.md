# PubMed search strategy: audit

Generated 2026-09-28T21:32:05+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Rapid diagnostic tests for diagnosing uncomplicated non-falciparum or Plasmodium vivax malaria in endemic countries (a diagnostic-test-accuracy review: in people with suspected non-falciparum / P. vivax malaria, what is the accuracy of rapid diagnostic tests?)
- Framework: PIRD
- Scope confirmed by user: yes (User asked to proceed without clarification and supplied no known relevant articles. Scope assumptions: malaria and the rapid diagnostic test are the two required search blocks; endemic setting is tested as an optional block because it is a topic-defining context. Uncomplicated status, suspected/confirmed status, reference standard and diagnostic performance remain screening criteria. No language, geography or publication-date filters. PubMed is bounded by Entrez date through 2013-06-09 via the harness; no publication-date limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Malaria, including Plasmodium vivax and non-falciparum malaria | search | Target condition of every eligible study; species terms are needed because relevant records may name P. vivax or another non-falciparum species without using the broader malaria label. |
| Malaria rapid diagnostic tests | search | Index test central to the review; include rapid-test terminology and named test families or products because records may identify the test by its member name. |
| Endemic malaria setting | optional | Endemic setting is a topic-defining eligibility context and may be named in abstracts; test an endemic-setting block before deciding whether it is safe to AND. Uncomplicated status and suspected/confirmed status remain screening criteria. |
| Eligible reference standard and diagnostic performance | screen | Reference method and accuracy outcomes are not reliably named in titles or abstracts; assess against protocol at screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T21:31:21+00:00
- Records added to PubMed up to: 2013-06-09
- Total records: 5,899
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Malaria"[Mesh]` | 50,641 | none |
| 2 | `"Malaria, Vivax"[Mesh]` | 2,872 | none |
| 3 | `"Plasmodium vivax"[Mesh]` | 3,745 | none |
| 4 | `malaria*[tiab]` | 59,105 | none |
| 5 | `plasmodium[tiab]` | 34,635 | none |
| 6 | `plasmodia[tiab]` | 1,281 | none |
| 7 | `"P. vivax"[tiab]` | 2,944 | none |
| 8 | `"Plasmodium vivax"[tiab]` | 3,467 | none |
| 9 | `"vivax malaria"[tiab]` | 1,672 | none |
| 10 | `"non-falciparum"[tiab]` | 55 | none |
| 11 | `"non falciparum"[tiab]` | 55 | none |
| 12 | `"Plasmodium ovale"[tiab]` | 274 | none |
| 13 | `"P. ovale"[tiab]` | 503 | none |
| 14 | `"Plasmodium malariae"[tiab]` | 421 | none |
| 15 | `"P. malariae"[tiab]` | 571 | none |
| 16 | `"Plasmodium knowlesi"[tiab]` | 687 | none |
| 17 | `"P. knowlesi"[tiab]` | 425 | none |
| 18 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17` | 76,140 | none |
| 19 | `"Immunologic Tests"[Mesh]` | 403,920 | none |
| 20 | `"Immunoassay"[Mesh]` | 418,448 | none |
| 21 | `"Reagent Kits, Diagnostic"[Mesh]` | 17,135 | none |
| 22 | `"rapid diagnostic test"[tiab]` | 579 | none |
| 23 | `"rapid diagnostic tests"[tiab]` | 769 | none |
| 24 | `"rapid test"[tiab]` | 2,005 | none |
| 25 | `"rapid tests"[tiab]` | 891 | none |
| 26 | `"rapid malaria test"[tiab]` | 25 | none |
| 27 | `"rapid malaria tests"[tiab]` | 12 | none |
| 28 | `immunochromatograph*[tiab]` | 1,749 | none |
| 29 | `"rapid antigen test"[tiab]` | 134 | none |
| 30 | `"rapid antigen tests"[tiab]` | 72 | none |
| 31 | `dipstick*[tiab]` | 2,298 | none |
| 32 | `RDT[tiab]` | 653 | none |
| 33 | `RDTs[tiab]` | 303 | none |
| 34 | `CareStart[tiab]` | 21 | none |
| 35 | `"SD Bioline"[tiab]` | 59 | none |
| 36 | `OptiMAL[tiab]` | 235,534 | none |
| 37 | `OnSite[tiab]` | 7,425 | none |
| 38 | `"First Response"[tiab]` | 902 | none |
| 39 | `ParaHIT[tiab]` | 9 | none |
| 40 | `#19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39` | 1,032,521 | none |
| 41 | `#18 AND #40` | 5,899 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Malaria"[Mesh] OR "Malaria, Vivax"[Mesh] OR "Plasmodium vivax"[Mesh] OR malaria*[tiab] OR plasmodium[tiab] OR plasmodia[tiab] OR "P. vivax"[tiab] OR "Plasmodium vivax"[tiab] OR "vivax malaria"[tiab] OR "non-falciparum"[tiab] OR "non falciparum"[tiab] OR "Plasmodium ovale"[tiab] OR "P. ovale"[tiab] OR "Plasmodium malariae"[tiab] OR "P. malariae"[tiab] OR "Plasmodium knowlesi"[tiab] OR "P. knowlesi"[tiab]) AND ("Immunologic Tests"[Mesh] OR "Immunoassay"[Mesh] OR "Reagent Kits, Diagnostic"[Mesh] OR "rapid diagnostic test"[tiab] OR "rapid diagnostic tests"[tiab] OR "rapid test"[tiab] OR "rapid tests"[tiab] OR "rapid malaria test"[tiab] OR "rapid malaria tests"[tiab] OR immunochromatograph*[tiab] OR "rapid antigen test"[tiab] OR "rapid antigen tests"[tiab] OR dipstick*[tiab] OR RDT[tiab] OR RDTs[tiab] OR CareStart[tiab] OR "SD Bioline"[tiab] OR OptiMAL[tiab] OR OnSite[tiab] OR "First Response"[tiab] OR ParaHIT[tiab])) AND ("1800/01/01"[edat] : "2013/06/09"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 6 | 6 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Endemic malaria setting | left out | 5,899 / 903 | 84.7% | 23608372, 23692957, 23731660 | 0/30 (up to 10% of removed records could be relevant) | The current 30-record loss sample contained no abstract that clearly met all eligibility criteria. A few candidate malaria RDT studies did not establish non-falciparum/P. vivax performance from their abstracts. Earlier screened-in relevant records still demonstrate that endemic locations may be named without endemic wording, so screen setting. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Malaria, including Plasmodium vivax and non-falciparum malaria | 1 | `vivax[tiab] OR ovale[tiab] OR malariae[tiab] OR knowlesi[tiab]` | 3,119 | 0/30 |
| Malaria, including Plasmodium vivax and non-falciparum malaria | 2 | `vivax[tiab] OR ovale[tiab] OR malariae[tiab] OR knowlesi[tiab]` | 109 | 0/30 |
| Malaria rapid diagnostic tests | 1 | `point-of-care[tiab] OR assay*[tiab] OR test*[tiab] OR antigen[tiab]` | 9,628 | 0/30 |
| Malaria rapid diagnostic tests | 2 | `point-of-care[tiab] OR assay*[tiab] OR test*[tiab] OR antigen[tiab]` | 11,731 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| malaria | 1,032,521 | 0 |
| rapid_test | 76,140 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 13,641 | initial | none | Initial PIRD two-block strategy; broad malaria and RDT vocabulary, no date/publication limits beyond Entrez cutoff. |
| 2 | 13,641 | limits/combination | none | Added an optional endemic-setting block for required loss testing because this eligibility context may be stated in abstracts. |
| 3 | 5,258 | malaria: +1 / -0; rapid_test: +2 / -1 | none | Added organism MeSH term from the screened relevant set, added plural RDT acronym from term mining, and replaced the very broad diagnostic-procedures heading with the directly relevant diagnostic reagent-kit heading. |
| 4 | 5,899 | rapid_test: +6 / -0 | none | Addressed the internal text-word critique by adding product names present in the six screened-in relevant records: CareStart, SD Bioline, OptiMAL, OnSite, First Response and ParaHIT. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 2 findings; R1-F1 must-fix rejected, R1-F2 should-fix resolved
- Round 2 on version 4: 3 findings; R1-F1 must-fix rejected, R1-F2 should-fix resolved, I-45996a53a1af1ed5c896 should-fix accepted-risk
- Round 3 on version 4: 3 findings; R1-F1 must-fix rejected, R1-F2 should-fix resolved, I-45996a53a1af1ed5c896 should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 821 NCBI requests logged (392 from cache); strategy sha256 41a035589430._

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
      "checked_at": "2026-09-28T21:31:21+00:00",
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
        "text": "\"Malaria\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Malaria, Vivax",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:31:21+00:00",
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
        "text": "\"Malaria, Vivax\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Plasmodium vivax",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:31:21+00:00",
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
        "text": "\"Plasmodium vivax\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Immunologic Tests",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:31:21+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D007159",
          "name": "Immunologic Tests",
          "type": "descriptor",
          "scope_note": "Immunologic techniques involved in diagnosis.",
          "tree_numbers": [
            "E01.370.225.812",
            "E05.200.812",
            "E05.478.594"
          ],
          "entry_terms": 17,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D007159",
      "preferred_label": "Immunologic Tests",
      "type": "descriptor",
      "location": "vocabulary:18",
      "term": {
        "text": "\"Immunologic Tests\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Immunoassay",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:31:21+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D007118",
          "name": "Immunoassay",
          "type": "descriptor",
          "scope_note": "A technique using antibodies for identifying or quantifying a substance. Usually the substance being studied serves as antigen both in antibody production and in measurement of antibody by the test substance.",
          "tree_numbers": [
            "E05.478.566",
            "E05.601.470"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D007118",
      "preferred_label": "Immunoassay",
      "type": "descriptor",
      "location": "vocabulary:19",
      "term": {
        "text": "\"Immunoassay\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Reagent Kits, Diagnostic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:31:21+00:00",
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
      "location": "vocabulary:20",
      "term": {
        "text": "\"Reagent Kits, Diagnostic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Malaria\"[MeSH Terms] OR \"malaria, vivax\"[MeSH Terms] OR \"Plasmodium vivax\"[MeSH Terms] OR \"malaria*\"[Title/Abstract] OR \"plasmodium\"[Title/Abstract] OR \"plasmodia\"[Title/Abstract] OR \"p vivax\"[Title/Abstract] OR \"Plasmodium vivax\"[Title/Abstract] OR \"vivax malaria\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"Plasmodium ovale\"[Title/Abstract] OR \"p ovale\"[Title/Abstract] OR \"Plasmodium malariae\"[Title/Abstract] OR \"p malariae\"[Title/Abstract] OR \"Plasmodium knowlesi\"[Title/Abstract] OR \"p knowlesi\"[Title/Abstract]) AND (\"Immunologic Tests\"[MeSH Terms] OR \"Immunoassay\"[MeSH Terms] OR \"reagent kits, diagnostic\"[MeSH Terms] OR \"rapid diagnostic test\"[Title/Abstract] OR \"rapid diagnostic tests\"[Title/Abstract] OR \"rapid test\"[Title/Abstract] OR \"rapid tests\"[Title/Abstract] OR \"rapid malaria test\"[Title/Abstract] OR \"rapid malaria tests\"[Title/Abstract] OR \"immunochromatograph*\"[Title/Abstract] OR \"rapid antigen test\"[Title/Abstract] OR \"rapid antigen tests\"[Title/Abstract] OR \"dipstick*\"[Title/Abstract] OR \"RDT\"[Title/Abstract] OR \"RDTs\"[Title/Abstract] OR \"CareStart\"[Title/Abstract] OR \"SD Bioline\"[Title/Abstract] OR \"OptiMAL\"[Title/Abstract] OR \"OnSite\"[Title/Abstract] OR \"First Response\"[Title/Abstract] OR \"ParaHIT\"[Title/Abstract]) AND 1800/01/01:2013/06/09[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "ebb7d510c1abc432b1c2f94f3d320a26043ee2db2cd8c7c866947c80a4ef339c",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The PIRD question is represented by malaria and rapid-test blocks; other properties remain for screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within the two concepts and the concepts are ANDed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "All listed MeSH headings were verified; the broad diagnostic procedure heading was replaced with a diagnostic-kit heading after count review."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The documented rationale says member product names should be considered, but none are yet present."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The evaluation reports no syntax or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2013-06-09 Entry Date bound is required by the harness and recorded in protocol.json as_of and notes; no publication-date filter is used."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The executed query includes an Entry Date bound through 2013/06/09, which the critic believed was undocumented.",
          "recommendation": "Remove the Entry Date restriction unless required by scope.",
          "status": "rejected",
          "response": "The cutoff is explicit in protocol.json as_of and notes, and the user/harness requires PSB_AS_OF=2013-06-09 on every PubMed command. It represents Entrez entry date, not a publication-date limit. Removing it would violate the task instructions."
        },
        {
          "id": "R1-F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The documented rationale says to consider named rapid-test families or products, but the test block currently has generic terms only.",
          "recommendation": "Add suitable product names observed in screened-in relevant records and re-evaluate.",
          "status": "resolved",
          "response": "Added CareStart, SD Bioline, OptiMAL, OnSite, First Response and ParaHIT as title/abstract terms from the six screened-in relevant studies. The current evaluation retained all six relevant records (100% development-set relative recall)."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "8b09491c8dbf3235ec377cc61648870029716051753d9e3bc19de5e69ff8d43b",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The required malaria and rapid-test concepts are searched; clinical properties and endemic setting are screened, with the tested endemic block left out."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within concepts; malaria and rapid test are ANDed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "MeSH headings are verified; the diagnostic-kit heading replaces the very broad diagnostic-procedures heading."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes species names, generic RDT terms and product names from screened-in records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No PubMed syntax or translation warnings are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entry Date bound is the required harness cutoff and is documented; no publication-date restriction is applied."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "Round 1 questioned whether the Entry Date bound through 2013-06-09 was documented.",
          "recommendation": "Remove the bound unless required by scope.",
          "status": "rejected",
          "response": "The bound is documented in the protocol and notes as the required harness Entrez Entry Date cutoff, not a publication-date limit. Removing it would violate the task instructions."
        },
        {
          "id": "R1-F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Round 1 found that the product-name rationale was not reflected in the rapid-test block.",
          "recommendation": "Add suitable product names from screened-in relevant records and reevaluate.",
          "status": "resolved",
          "response": "CareStart, SD Bioline, OptiMAL, OnSite, First Response, and ParaHIT were added as title/abstract terms. The current evaluation reports all six development records retrieved."
        },
        {
          "id": "I-45996a53a1af1ed5c896",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The malaria category probe is marked stale because the block changed after its last probe and the probe budget is spent.",
          "recommendation": "Reprobe the current malaria block if the probe budget can be extended; otherwise document the residual validation uncertainty.",
          "status": "accepted-risk",
          "response": "The warning is nonblocking. Two probes each screened 30 records outside the malaria block, with 0 relevant records found in either sample; the final combined strategy retrieves all six development records. The stale status still reduces assurance for the final malaria block."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-45996a53a1af1ed5c896",
          "status": "accepted-risk",
          "response": "Accept the nonblocking stale-probe warning with reduced assurance because both recorded category probes found no relevant records, while recognizing that the current malaria block has not received a fresh probe.",
          "evidence": "The packet reports two malaria probes with 0/30 relevant records each, a spent probe budget, and 6/6 known relevant records retrieved by the final strategy."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "8b09491c8dbf3235ec377cc61648870029716051753d9e3bc19de5e69ff8d43b",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The strategy searches malaria and rapid-test concepts; endemic setting and other clinical properties remain for screening. The tested endemic block is left out."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within the malaria and rapid-test blocks, and the two blocks are ANDed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The current strategy uses verified malaria, vivax malaria, immunologic-test, immunoassay, and diagnostic-kit headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes malaria species terms, generic rapid-test terms, and named products. All six known development records are retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current evaluation reports no syntax or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez Entry Date cutoff through 2013-06-09 is documented as the required harness bound; no publication-date filter is applied."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "Round 1 questioned whether the Entry Date bound through 2013-06-09 was documented.",
          "recommendation": "Remove the bound unless required by scope.",
          "status": "rejected",
          "response": "The bound is documented in the protocol and notes as the required harness Entrez Entry Date cutoff, not a publication-date limit. Removing it would violate the task instructions."
        },
        {
          "id": "R1-F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Round 1 found that the rationale to consider named rapid-test products was not reflected in the test block.",
          "recommendation": "Add suitable product names from screened-in relevant records and reevaluate.",
          "status": "resolved",
          "response": "CareStart, SD Bioline, OptiMAL, OnSite, First Response, and ParaHIT were added as title/abstract terms. The current evaluation reports all six development records retrieved."
        },
        {
          "id": "I-45996a53a1af1ed5c896",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The malaria category probe is stale because the block changed after its last probe and the probe budget is spent.",
          "recommendation": "Reprobe the current malaria block if the probe budget can be extended; otherwise document the residual validation uncertainty.",
          "status": "accepted-risk",
          "response": "The nonblocking warning remains accepted with reduced assurance: both recorded malaria probes found 0 relevant records among 30 screened, and the final strategy retrieves all six development records, but the current malaria block has not received a fresh probe."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-45996a53a1af1ed5c896",
          "status": "accepted-risk",
          "response": "Accept the nonblocking stale-probe warning with reduced assurance because both recorded category probes found no relevant records, while recognizing that the current malaria block has not received a fresh probe.",
          "evidence": "The packet reports two malaria probes with 0/30 relevant records each, a spent probe budget, and 6/6 known relevant records retrieved by the final strategy."
        }
      ]
    }
  ]
}
```

