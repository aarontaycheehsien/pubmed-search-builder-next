# PubMed search strategy: audit

Generated 2026-09-30T13:23:12+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Rapid diagnostic tests for diagnosing uncomplicated non-falciparum or Plasmodium vivax malaria in endemic countries (a diagnostic-test-accuracy review: in people with suspected non-falciparum / P. vivax malaria, what is the accuracy of rapid diagnostic tests?)
- Framework: PIRD
- Scope confirmed by user: no (User asked to proceed without clarification; scope roles are provisional decisions made from the question. No seeds, known relevant PMIDs, or answers were supplied. Default standard depth and 10,000-record screening workload assumed. PubMed Entrez date bound set to 2013-06-09 via PSB_AS_OF on every command; no publication-date limit. The endemic-setting optional block was left out after loss-sample and known-record evaluation; geographic eligibility is assessed during screening. The Rapid Diagnostic Tests MeSH heading was introduced in 2023, after the requested cutoff, and was removed from the strategy; older assay headings and text words remain.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Non-falciparum malaria or Plasmodium vivax malaria | search | Target diagnosis is essential to every eligible study; use a broad malaria layer to retain studies reporting mixed-species populations, then screen species and uncomplicated status. |
| Malaria rapid diagnostic tests | search | Index test is essential and normally named in abstracts or indexed; include rapid diagnostic and antigen-test terminology. |
| Malaria-endemic country setting | optional | Topic-defining eligibility setting that authors may name; test as an optional searchable block, but with no known studies available it cannot be safely AND-ed. |
| Diagnostic performance and reference standard | screen | Accuracy terms and reference standards are inconsistently described in abstracts; determine eligibility at screening. |
| People with suspected or confirmed uncomplicated malaria | screen | Suspected status, severity, and uncomplicated disease are eligibility properties not reliably indexed. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T13:22:25+00:00
- Records added to PubMed up to: 2013-06-09
- Total records: 4,230
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Malaria[Mesh]` | 50,641 | none |
| 2 | `Malaria, Vivax[Mesh]` | 2,872 | none |
| 3 | `Plasmodium vivax[Mesh]` | 3,745 | none |
| 4 | `malaria[tiab]` | 55,839 | none |
| 5 | `plasmodium[tiab]` | 34,635 | none |
| 6 | `plasmodium vivax[tiab]` | 3,467 | none |
| 7 | `P. vivax[tiab]` | 2,944 | none |
| 8 | `P vivax[tiab]` | 2,944 | none |
| 9 | `vivax malaria[tiab]` | 1,672 | none |
| 10 | `non-falciparum[tiab]` | 55 | none |
| 11 | `nonfalciparum[tiab]` | 59 | none |
| 12 | `non falciparum[tiab]` | 55 | none |
| 13 | `P. malariae[tiab]` | 571 | none |
| 14 | `Plasmodium malariae[tiab]` | 421 | none |
| 15 | `P. ovale[tiab]` | 503 | none |
| 16 | `Plasmodium ovale[tiab]` | 274 | none |
| 17 | `Plasmodium knowlesi[tiab]` | 687 | none |
| 18 | `knowlesi malaria[tiab]` | 108 | none |
| 19 | `benign tertian[tiab]` | 69 | none |
| 20 | `quartan malaria[tiab]` | 106 | none |
| 21 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20` | 74,170 | none |
| 22 | `Immunoassay[Mesh]` | 418,448 | none |
| 23 | `Reagent Kits, Diagnostic[Mesh]` | 17,135 | none |
| 24 | `Reagent Strips[Mesh]` | 2,830 | none |
| 25 | `Diagnostic Tests, Routine[Mesh]` | 7,136 | none |
| 26 | `rapid diagnostic test[tiab]` | 579 | none |
| 27 | `rapid diagnostic tests[tiab]` | 769 | none |
| 28 | `rapid test[tiab]` | 2,005 | none |
| 29 | `rapid tests[tiab]` | 891 | none |
| 30 | `rapid antigen test[tiab]` | 134 | none |
| 31 | `rapid antigen tests[tiab]` | 72 | none |
| 32 | `RDT[tiab]` | 653 | none |
| 33 | `RDTs[tiab]` | 303 | none |
| 34 | `immunochromatograph*[tiab]` | 1,749 | none |
| 35 | `immunochromatographic[tiab]` | 1,333 | none |
| 36 | `ICT[tiab]` | 2,484 | none |
| 37 | `dipstick*[tiab]` | 2,298 | none |
| 38 | `lateral flow[tiab]` | 720 | none |
| 39 | `antigen test[tiab]` | 1,412 | none |
| 40 | `antigen tests[tiab]` | 519 | none |
| 41 | `malaria antigen[tiab]` | 192 | none |
| 42 | `antigen detection[tiab]` | 3,135 | none |
| 43 | `point-of-care test[tiab]` | 271 | none |
| 44 | `point of care test[tiab]` | 271 | none |
| 45 | `test strip[tiab]` | 676 | none |
| 46 | `test strips[tiab]` | 775 | none |
| 47 | `OptiMAL[tiab]` | 235,534 | none |
| 48 | `ParaSight[tiab]` | 81 | none |
| 49 | `BinaxNOW[tiab]` | 47 | none |
| 50 | `Paracheck[tiab]` | 53 | none |
| 51 | `#22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50` | 678,737 | none |
| 52 | `#21 AND #51` | 4,230 | none |

### Strategy (single line, for copying into PubMed)

```text
((Malaria[Mesh] OR Malaria, Vivax[Mesh] OR Plasmodium vivax[Mesh] OR malaria[tiab] OR plasmodium[tiab] OR plasmodium vivax[tiab] OR P. vivax[tiab] OR P vivax[tiab] OR vivax malaria[tiab] OR non-falciparum[tiab] OR nonfalciparum[tiab] OR non falciparum[tiab] OR P. malariae[tiab] OR Plasmodium malariae[tiab] OR P. ovale[tiab] OR Plasmodium ovale[tiab] OR Plasmodium knowlesi[tiab] OR knowlesi malaria[tiab] OR benign tertian[tiab] OR quartan malaria[tiab]) AND (Immunoassay[Mesh] OR Reagent Kits, Diagnostic[Mesh] OR Reagent Strips[Mesh] OR Diagnostic Tests, Routine[Mesh] OR rapid diagnostic test[tiab] OR rapid diagnostic tests[tiab] OR rapid test[tiab] OR rapid tests[tiab] OR rapid antigen test[tiab] OR rapid antigen tests[tiab] OR RDT[tiab] OR RDTs[tiab] OR immunochromatograph*[tiab] OR immunochromatographic[tiab] OR ICT[tiab] OR dipstick*[tiab] OR lateral flow[tiab] OR antigen test[tiab] OR antigen tests[tiab] OR malaria antigen[tiab] OR antigen detection[tiab] OR point-of-care test[tiab] OR point of care test[tiab] OR test strip[tiab] OR test strips[tiab] OR OptiMAL[tiab] OR ParaSight[tiab] OR BinaxNOW[tiab] OR Paracheck[tiab])) AND ("1800/01/01"[edat] : "2013/06/09"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 5 | 5 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Malaria-endemic country setting | left out | 4,230 / 1,039 | 75.4% | 23433230, 23692957 | 0/30 (up to 10% of removed records could be relevant) | Leave the setting block out: its previous measured version lost two of five known relevant records, and the known set remains below the 15-record threshold required to AND an optional block. The refreshed loss sample had no clearly eligible record among 30 screened, but that sample cannot demonstrate safety. Screen endemic-country eligibility instead. |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| malaria | 678,737 | 0 |
| rdt | 74,170 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 4,144 | initial | none | Initial PIRD strategy: broad malaria target-condition block AND rapid diagnostic/antigen-test block; accuracy, reference standard, disease severity and setting screened, with endemic setting tested as optional. No known articles supplied. |
| 2 | 4,144 | rdt: +0 / -1 | none | Removed Rapid Diagnostic Tests[Mesh] after authority review showed it was introduced in 2023 and generated a no-items-found/zero-hit warning at the 2013 Entrez cutoff. Updated optional-setting decision using observed loss of two relevant records; retained all older MeSH and text-word coverage. |
| 3 | 4,230 | malaria: +1 / -0; rdt: +2 / -0 | none | Added MeSH headings found on screened relevant studies and verified as fitting MeSH descriptors: Plasmodium vivax, Reagent Kits, Diagnostic, and Diagnostic Tests, Routine. These expand indexed species and diagnostic-kit/test coverage; accuracy heading Sensitivity and Specificity remains screening-only by design. |
| 4 | 4,230 | rdt: +2 / -0 | none | Addressed critic F2 by adding rapid antigen test(s)[tiab] explicitly. Repeated and screened all 30 optional-setting loss records after the vocabulary change; left setting out because known records are insufficient to support AND-ing. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 1 findings; F1 should-fix resolved
- Round 2 on version 3: 2 findings; F1 should-fix resolved, F2 should-fix open
- Round 3 on version 4: 2 findings; F1 should-fix resolved, F2 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 591 NCBI requests logged (335 from cache); strategy sha256 26c7c5bbab46._

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
      "requested": "Malaria",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:22:25+00:00",
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
      "checked_at": "2026-09-30T13:22:25+00:00",
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
      "checked_at": "2026-09-30T13:22:25+00:00",
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
      "requested": "Immunoassay",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:22:25+00:00",
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
      "location": "vocabulary:21",
      "term": {
        "text": "Immunoassay",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Reagent Kits, Diagnostic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:22:25+00:00",
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
      "location": "vocabulary:22",
      "term": {
        "text": "Reagent Kits, Diagnostic",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Reagent Strips",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:22:25+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "Reagent Strips",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diagnostic Tests, Routine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T13:22:25+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "Diagnostic Tests, Routine",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"malaria\"[MeSH Terms] OR \"malaria, vivax\"[MeSH Terms] OR \"plasmodium vivax\"[MeSH Terms] OR \"malaria\"[Title/Abstract] OR \"Plasmodium\"[Title/Abstract] OR \"plasmodium vivax\"[Title/Abstract] OR \"p vivax\"[Title/Abstract] OR \"p vivax\"[Title/Abstract] OR \"vivax malaria\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"nonfalciparum\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"p malariae\"[Title/Abstract] OR \"plasmodium malariae\"[Title/Abstract] OR \"p ovale\"[Title/Abstract] OR \"plasmodium ovale\"[Title/Abstract] OR \"plasmodium knowlesi\"[Title/Abstract] OR \"knowlesi malaria\"[Title/Abstract] OR \"benign tertian\"[Title/Abstract] OR \"quartan malaria\"[Title/Abstract]) AND (\"immunoassay\"[MeSH Terms] OR \"reagent kits, diagnostic\"[MeSH Terms] OR \"reagent strips\"[MeSH Terms] OR \"diagnostic tests, routine\"[MeSH Terms] OR \"rapid diagnostic test\"[Title/Abstract] OR \"rapid diagnostic tests\"[Title/Abstract] OR \"rapid test\"[Title/Abstract] OR \"rapid tests\"[Title/Abstract] OR \"rapid antigen test\"[Title/Abstract] OR \"rapid antigen tests\"[Title/Abstract] OR \"RDT\"[Title/Abstract] OR \"RDTs\"[Title/Abstract] OR \"immunochromatograph*\"[Title/Abstract] OR \"immunochromatographic\"[Title/Abstract] OR \"ICT\"[Title/Abstract] OR \"dipstick*\"[Title/Abstract] OR \"lateral flow\"[Title/Abstract] OR \"antigen test\"[Title/Abstract] OR \"antigen tests\"[Title/Abstract] OR \"malaria antigen\"[Title/Abstract] OR \"antigen detection\"[Title/Abstract] OR \"point of care test\"[Title/Abstract] OR \"point of care test\"[Title/Abstract] OR \"test strip\"[Title/Abstract] OR \"test strips\"[Title/Abstract] OR \"OptiMAL\"[Title/Abstract] OR \"ParaSight\"[Title/Abstract] OR \"BinaxNOW\"[Title/Abstract] OR \"Paracheck\"[Title/Abstract]) AND 1800/01/01:2013/06/09[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "e54af041f811f86bc6237bf92fc993e94667d7b3a3c4c4ddd42ec1fbcfd29f88",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The malaria and rapid diagnostic test blocks represent the core PIRD concepts; eligibility details are screened."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within the two essential blocks, which are ANDed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Relevant verified headings cover malaria, P. vivax and diagnostic assay/test concepts; the post-cutoff Rapid Diagnostic Tests heading was removed."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text terms include broad malaria, named non-falciparum species, rapid/antigen tests, method synonyms and product names."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Current PubMed translation reports no syntax or phrase issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2013-06-09 Entrez Entry Date bound is explicitly required by the user's historical-snapshot instruction. It is not a publication-date eligibility limit; no [dp] restriction is used."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "Every query is limited by PubMed Entry Date through 2013/06/09, although the review question specifies no temporal restriction. This can omit records entered after that date, including older publications.",
          "recommendation": "Confirm and report that the search is intentionally a PubMed snapshot as of 2013/06/09, or remove the Entry Date bound and rerun the complete evaluation.",
          "status": "resolved",
          "response": "The user explicitly required that this run simulate 2013-06-09 and that PSB_AS_OF bound PubMed by Entrez date on every command. The cutoff is therefore a requested historical PubMed snapshot, not a publication-date eligibility criterion. The protocol records the as_of value and the generated search will preserve its Entry Date bound. No [dp] limit is used; records already in PubMed by the cutoff can retain later publication dates."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "e54af041f811f86bc6237bf92fc993e94667d7b3a3c4c4ddd42ec1fbcfd29f88",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The malaria and RDT blocks search the two essential PIRD concepts; endemicity, accuracy, and uncomplicated status are screened as specified."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within blocks, and the two essential blocks are ANDed. The optional endemic-setting block is left out after observed losses."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Malaria, vivax, immunoassay, diagnostic reagent, reagent strip, and routine diagnostic test headings are included; the post-cutoff Rapid Diagnostic Tests heading was removed."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The RDT block does not yet include rapid antigen test(s), a common combined phrase."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed PubMed translations report no syntax or phrase warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entry Date cutoff is documented as the requested 2013-06-09 snapshot, not a publication-date eligibility restriction."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "Every query is limited by PubMed Entry Date through 2013/06/09, although the review question specifies no temporal restriction. This can omit records entered after that date, including older publications.",
          "recommendation": "Confirm and report that the search is intentionally a PubMed snapshot as of 2013/06/09, or remove the Entry Date bound and rerun the complete evaluation.",
          "status": "resolved",
          "response": "The user explicitly required this run to simulate 2013-06-09 and PSB_AS_OF to bound PubMed by Entrez date on every command. The cutoff is therefore a requested historical PubMed snapshot, not a publication-date eligibility criterion. The protocol records the as_of value and preserves the Entry Date bound. No publication-date limit is used."
        },
        {
          "id": "F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The RDT block has the phrases rapid diagnostic test(s), rapid test(s), and antigen test(s), but does not cover the combined wording rapid antigen test(s). Exact phrase searching for rapid test or antigen test does not retrieve that wording when antigen intervenes between rapid and test.",
          "recommendation": "Add explicit tested expressions for rapid antigen test and rapid antigen tests to the RDT block, then rerun the complete evaluation.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "21a0cc20ab37a648f4f3ec0a21012e78e29a1a6ce7fddb18d74661a2bb5dde99",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two essential search blocks cover malaria and rapid diagnostic testing; endemicity, accuracy, and uncomplicated status remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are ORed within the malaria and RDT blocks, and the blocks are ANDed. The optional endemic-setting block remains excluded after known-record losses."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes verified malaria, vivax, immunoassay, diagnostic reagent, reagent strip, and routine diagnostic test headings. The post-cutoff Rapid Diagnostic Tests heading is excluded."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The RDT block now includes explicit rapid antigen test and rapid antigen tests phrases. The complete evaluation reports all five known records retrieved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current PubMed translation reports no syntax or phrase issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez Entry Date bound through 2013-06-09 is documented as the requested historical PubMed snapshot; no publication-date limit is used."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "Every query is limited by PubMed Entry Date through 2013/06/09, although the review question specifies no temporal restriction. This can omit records entered after that date, including older publications.",
          "recommendation": "Confirm and report that the search is intentionally a PubMed snapshot as of 2013/06/09, or remove the Entry Date bound and rerun the complete evaluation.",
          "status": "resolved",
          "response": "The packet documents that the user required a 2013-06-09 historical PubMed snapshot and that PSB_AS_OF bound every command by Entrez date. The cutoff is not a publication-date eligibility limit."
        },
        {
          "id": "F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The RDT block has the phrases rapid diagnostic test(s), rapid test(s), and antigen test(s), but does not cover the combined wording rapid antigen test(s). Exact phrase searching for rapid test or antigen test does not retrieve that wording when antigen intervenes between rapid and test.",
          "recommendation": "Add explicit tested expressions for rapid antigen test and rapid antigen tests to the RDT block, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "Version 4 adds rapid antigen test[tiab] and rapid antigen tests[tiab]. The complete evaluation was rerun: the result count remains 4,230 and all five known records are retrieved."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

