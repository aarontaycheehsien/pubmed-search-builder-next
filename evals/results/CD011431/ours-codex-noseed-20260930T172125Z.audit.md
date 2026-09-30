# PubMed search strategy: audit

Generated 2026-09-30T17:59:40+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In people with suspected non-falciparum or Plasmodium vivax malaria, what is the diagnostic accuracy of rapid diagnostic tests in endemic countries?
- Framework: PIRD
- Scope confirmed by user: yes (User requested no questions and provided no known records. Scope assumed from the stated criteria. Concepts: malaria and rapid diagnostic test are AND-ed; endemic setting is tested as optional and left out based on known losses; reference standard, accuracy and uncomplicated severity are screened. No language, publication-date, or publication-type restrictions. For this harness run, every PubMed request is bounded by Entry Date 2013-06-09 (PSB_AS_OF); no publication-date [dp] limit is used. This artifact is a historical harness-limited evaluation and must be refreshed without the harness ceiling for a current review search.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Non-falciparum malaria, including Plasmodium vivax | search | Target condition is central, searchable and reliably indexed; species-only records may name a member rather than the broader category. |
| Malaria rapid diagnostic tests | search | Index test is central and commonly named or indexed; include general and malaria-specific rapid-test terminology. |
| Malaria-endemic setting | optional | Setting defines eligibility but may be absent from abstracts; test before deciding whether to AND it. |
| Eligible reference standard | screen | Methods may be incompletely named in abstracts and vary; assess eligibility at screening. |
| Diagnostic performance | screen | Accuracy outcomes are inconsistently reported in titles and abstracts. |
| Uncomplicated disease | screen | Severity is inconsistently indexed and often determined in full text. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T17:58:55+00:00
- Records added to PubMed up to: 2013-06-09
- Total records: 9,304
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Malaria[Mesh]` | 50,641 | none |
| 2 | `Malaria, Vivax[Mesh]` | 2,872 | none |
| 3 | `Plasmodium vivax[Mesh]` | 3,745 | none |
| 4 | `malaria[tiab]` | 55,839 | none |
| 5 | `plasmodium[tiab]` | 34,635 | none |
| 6 | `paludism[tiab]` | 72 | none |
| 7 | `"P. vivax"[tiab]` | 2,944 | none |
| 8 | `vivax[tiab]` | 5,921 | none |
| 9 | `"P. ovale"[tiab]` | 503 | none |
| 10 | `ovale[tiab]` | 5,356 | none |
| 11 | `"P. malariae"[tiab]` | 571 | none |
| 12 | `malariae[tiab]` | 888 | none |
| 13 | `"P. knowlesi"[tiab]` | 425 | none |
| 14 | `knowlesi[tiab]` | 866 | none |
| 15 | `"non-falciparum"[tiab]` | 55 | none |
| 16 | `nonfalciparum[tiab]` | 59 | none |
| 17 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16` | 79,547 | none |
| 18 | `Diagnostic Tests, Routine[Mesh]` | 7,136 | none |
| 19 | `Reagent Kits, Diagnostic[Mesh]` | 17,135 | none |
| 20 | `Clinical Laboratory Techniques[Mesh]` | 2,142,378 | none |
| 21 | `"rapid diagnostic test"[tiab:~2]` | 757 | none |
| 22 | `"rapid test"[tiab:~2]` | 8,342 | none |
| 23 | `"point of care test"[tiab:~2]` | 421 | none |
| 24 | `RDT[tiab]` | 653 | none |
| 25 | `RDTs[tiab]` | 303 | none |
| 26 | `ICT[tiab]` | 2,484 | none |
| 27 | `ICTs[tiab]` | 193 | none |
| 28 | `immunochromatograph*[tiab]` | 1,749 | none |
| 29 | `"lateral flow"[tiab:~2]` | 965 | none |
| 30 | `dipstick*[tiab]` | 2,298 | none |
| 31 | `"antigen detection test"[tiab:~2]` | 299 | none |
| 32 | `"antigen test"[tiab:~2]` | 3,780 | none |
| 33 | `rapid antigen test*[tiab]` | 226 | none |
| 34 | `#18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33` | 2,169,771 | none |
| 35 | `#17 AND #34` | 9,304 | none |

### Strategy (single line, for copying into PubMed)

```text
((Malaria[Mesh] OR Malaria, Vivax[Mesh] OR Plasmodium vivax[Mesh] OR malaria[tiab] OR plasmodium[tiab] OR paludism[tiab] OR "P. vivax"[tiab] OR vivax[tiab] OR "P. ovale"[tiab] OR ovale[tiab] OR "P. malariae"[tiab] OR malariae[tiab] OR "P. knowlesi"[tiab] OR knowlesi[tiab] OR "non-falciparum"[tiab] OR nonfalciparum[tiab]) AND (Diagnostic Tests, Routine[Mesh] OR Reagent Kits, Diagnostic[Mesh] OR Clinical Laboratory Techniques[Mesh] OR "rapid diagnostic test"[tiab:~2] OR "rapid test"[tiab:~2] OR "point of care test"[tiab:~2] OR RDT[tiab] OR RDTs[tiab] OR ICT[tiab] OR ICTs[tiab] OR immunochromatograph*[tiab] OR "lateral flow"[tiab:~2] OR dipstick*[tiab] OR "antigen detection test"[tiab:~2] OR "antigen test"[tiab:~2] OR rapid antigen test*[tiab])) AND ("1800/01/01"[edat] : "2013/06/09"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| neighbor_relevant | relevant (records screened relevant during the build; used for development, not independent) | 11 | 11 | 100.0% |
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 9 | 9 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 5 | 5 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Malaria-endemic setting | left out (stale) | 9,304 / 1,060 | 88.6% | 9431947, 18620560, 18983278, 19860920, 20005196, 20046179, 20529273, 20602766, 20979601, 21696587, 21749585, 22818643, 23433230, 23692957, 23731660 | 0/30 (up to 10% of removed records could be relevant) | With the expanded candidate set, 25 known records are in the base strategy and the setting block would lose 15, including all 5 held-out validation records. This is unsafe despite the 0/30 relevant loss sample; the sample screens only a random subset of removed records. Leave out setting to preserve recall. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Non-falciparum malaria, including Plasmodium vivax | 1 | `Plasmodium[Mesh]` | 240 | 0/30 |
| Non-falciparum malaria, including Plasmodium vivax | 2 | `Plasmodium[Mesh]` | 240 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| malaria | 2,169,771 | 0 |
| rapid_test | 79,547 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial PIRD blocks: malaria and malaria rapid-test concepts searched with MeSH and title/abstract terms. Endemic setting retained as an optional candidate for measured testing; no date or other limits added. |
| 2 | 0 | malaria: +16 / -0; rapid_test: +15 / -0 | none | Initial two-block PIRD strategy with MeSH and text synonyms, using available pre-cutoff indexing headings. Endemic setting is an optional tested candidate; no design, accuracy, severity or setting filter is required. |
| 3 | 9,304 | rapid_test: +1 / -0 | none | Round 1 critic lexical finding: added rapid antigen test*[tiab] after a live count/translation check (226; explicit Title/Abstract, no translation issue). Retained harness-required Entry Date ceiling and expanded protocol notes to label the evaluation historical and require refresh before current use. Query wording tested in a complete evaluation. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 2 findings; R1-F1 should-fix resolved, R1-F2 should-fix accepted-risk
- Round 2 on version 3: 3 findings; R1-F1 should-fix resolved, R1-F2 should-fix accepted-risk, R2-F1 should-fix rejected
- Round 3 on version 3: 3 findings; R1-F1 should-fix resolved, R1-F2 should-fix accepted-risk, R2-F1 should-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1111 NCBI requests logged (534 from cache); strategy sha256 4ddf45e1657d._

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
      "checked_at": "2026-09-30T17:58:55+00:00",
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
      "checked_at": "2026-09-30T17:58:55+00:00",
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
      "checked_at": "2026-09-30T17:58:55+00:00",
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
      "requested": "Diagnostic Tests, Routine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:58:55+00:00",
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
      "location": "vocabulary:17",
      "term": {
        "text": "Diagnostic Tests, Routine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Reagent Kits, Diagnostic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:58:55+00:00",
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
      "location": "vocabulary:18",
      "term": {
        "text": "Reagent Kits, Diagnostic",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Clinical Laboratory Techniques",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T17:58:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D019411",
          "name": "Clinical Laboratory Techniques",
          "type": "descriptor",
          "scope_note": "Techniques used to carry out clinical investigative procedures in the diagnosis and therapy of disease.",
          "tree_numbers": [
            "E01.370.225",
            "E05.200"
          ],
          "entry_terms": 19,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D019411",
      "preferred_label": "Clinical Laboratory Techniques",
      "type": "descriptor",
      "location": "vocabulary:19",
      "term": {
        "text": "Clinical Laboratory Techniques",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"malaria\"[MeSH Terms] OR \"malaria, vivax\"[MeSH Terms] OR \"plasmodium vivax\"[MeSH Terms] OR \"malaria\"[Title/Abstract] OR \"plasmodium\"[Title/Abstract] OR \"paludism\"[Title/Abstract] OR \"p vivax\"[Title/Abstract] OR \"vivax\"[Title/Abstract] OR \"p ovale\"[Title/Abstract] OR \"ovale\"[Title/Abstract] OR \"p malariae\"[Title/Abstract] OR \"malariae\"[Title/Abstract] OR \"p knowlesi\"[Title/Abstract] OR \"knowlesi\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"nonfalciparum\"[Title/Abstract]) AND (\"diagnostic tests, routine\"[MeSH Terms] OR \"reagent kits, diagnostic\"[MeSH Terms] OR \"clinical laboratory techniques\"[MeSH Terms] OR \"rapid diagnostic test\"[Title/Abstract:~2] OR \"rapid test\"[Title/Abstract:~2] OR \"point of care test\"[Title/Abstract:~2] OR \"RDT\"[Title/Abstract] OR \"RDTs\"[Title/Abstract] OR \"ICT\"[Title/Abstract] OR \"ICTs\"[Title/Abstract] OR \"immunochromatograph*\"[Title/Abstract] OR \"lateral flow\"[Title/Abstract:~2] OR \"dipstick*\"[Title/Abstract] OR \"antigen detection test\"[Title/Abstract:~2] OR \"antigen test\"[Title/Abstract:~2] OR \"rapid antigen test*\"[Title/Abstract]) AND 1800/01/01:2013/06/09[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "5855e1948b08646931d75c23888bf6f347d9dc31a776de83fe4826fba5223aa4",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "All displayed MeSH terms translate to the intended descriptors, and the packet reports no translation issues, errors, or warnings. The proximity clauses use explicit phrases without wildcards; the packet's diagnostics show them retained as Title/Abstract proximity expressions."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two searchable concepts are OR-combined within blocks and AND-combined across blocks. The optional setting block is left out on documented evidence that it removes 15 of 25 known eligible records, including all five held-out validation records. Reference standard, accuracy, and severity remain screening criteria as scoped."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The selected disease and test headings are verified in the packet. Some test headings are broad, but they are combined with the malaria block and no packet evidence shows a missed eligible record attributable to heading choice."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The test-word block lacks an explicit rapid-antigen expression, a plausible wording variant for the central index test. Complete known-record recall does not establish that the wording set is exhaustive."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed Boolean query is balanced and parsed; the packet reports no syntax or translation errors. Proximity expressions are explicitly tested."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The final query is restricted by Entry Date through 2013-06-09, although the question states no date limit. The packet explains this as a harness bound, so the cutoff must be identified as an evaluation constraint and removed or refreshed for a current search."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The rapid-test block has rapid diagnostic test and rapid test expressions and a separate antigen test expression, but no explicit rapid antigen test wording. The reported 100% recall applies only to the 25 known records and does not resolve this vocabulary gap.",
          "recommendation": "Add and test an explicit rapid antigen test expression (including the plural form or a tested truncation outside proximity), then rerun the complete evaluation and inspect its translation.",
          "status": "resolved",
          "response": "Added rapid antigen test*[tiab] to the test block after live testing returned 226 records with an explicit Title/Abstract translation and no translation issue. A full evaluation retrieved all 25 known records with no losses."
        },
        {
          "id": "R1-F2",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The evaluated query includes an Entry Date ceiling of 2013-06-09 despite no date restriction in the review question. The packet attributes it to a harness bound, but the resulting strategy cannot retrieve records entered after that date.",
          "recommendation": "In the search report, label this as a harness-limited historical evaluation. Before using the strategy for the review, rerun it without the harness ceiling (or with the intended current search date) and report that date explicitly.",
          "status": "accepted-risk",
          "response": "The PSB_AS_OF 2013-06-09 Entry Date bound is required by the harness and user instruction for this historical run, so it remains in the protected query. The protocol and narrative now label this artifact as harness-limited and require a refresh without the harness ceiling before current review use."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "d6940f5ea25cd1fbac06827b0cd1c3c63bc091018f670ea91c685b08ad42e285",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "All displayed MeSH terms translate to intended descriptors, translation_issues is empty, and the raw diagnostics show no warnings or errors. The proximity expressions are explicitly tested and retained as Title/Abstract proximity clauses; no proximity clause contains a wildcard."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are OR-combined within the malaria and rapid-test blocks, and the blocks are AND-combined. The optional endemic-setting block is left out on evidence that it removes 15 of 25 known records, including all five held-out validation records. Reference standard, performance, and severity remain screening criteria as scoped."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "The listed headings are verified, and the category block has its own species terms. However, the two purported category probes use the same seed and report the identical 30-record sample, so they do not provide two independent checks; the category status of clean is not supported by the stated two-probe evidence."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The explicit rapid antigen test*[tiab] expression is now present and has a reported explicit translation; species terms include bare names for vivax, ovale, malariae, and knowlesi alongside non-falciparum forms. The packet reports retrieval of all 25 known records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed Boolean expression is balanced and parsed, and the packet reports no query errors or translation issues. Proximity syntax is explicitly tested."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entry Date ceiling remains a harness constraint rather than an unreported review limit. The protocol and narrative identify the 2013-06-09 historical bound and require refresh without that ceiling before current review use; carry-forward finding R1-F2 records this accepted risk."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The rapid-test block previously lacked an explicit rapid antigen test expression.",
          "recommendation": "Add and test an explicit rapid antigen test expression, including plural coverage or tested truncation, and rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current block includes rapid antigen test*[tiab], reported as returning 226 records with an explicit Title/Abstract translation and no translation issue. The current complete evaluation retrieves all 25 known records."
        },
        {
          "id": "R1-F2",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The evaluated query includes an Entry Date ceiling of 2013-06-09 despite no date restriction in the review question, so it cannot retrieve records entered after that date.",
          "recommendation": "Label this as a harness-limited historical evaluation and refresh the strategy without the harness ceiling, or with the intended current search date, before review use.",
          "status": "accepted-risk",
          "response": "The packet states the PSB_AS_OF 2013-06-09 Entry Date bound is required for this historical harness run. The protocol and narrative label the artifact as harness-limited and require a refresh without the ceiling before current review use."
        },
        {
          "id": "R2-F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The two malaria category probes are not independent: both report seed 1 and the same 30 sampled PMIDs, despite being presented as two probes. Therefore the packet's two-probe evidence does not support the category status of clean.",
          "recommendation": "Run a second category probe with a distinct random seed and independently drawn/screened sample, then update the category status and evidence before relying on the two-probe result.",
          "status": "rejected",
          "response": "The first current-block probe is a screened sample of 30 records with no eligible records and independently satisfies the standard-depth delivery rule, which requires one clean probe. The default seed caused probe 2 to repeat the same records, so it is not claimed as independent evidence. The standard probe budget is spent; this duplicate adds no additional assurance and is disclosed as a limitation in narrative.md."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "d6940f5ea25cd1fbac06827b0cd1c3c63bc091018f670ea91c685b08ad42e285",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The complete query translates the rapid antigen expression and displayed MeSH and proximity clauses as intended; translation_issues is empty and the packet reports no query errors or warnings."
        },
        "operators": {
          "verdict": "pass",
          "note": "Malaria and rapid-test terms are OR-combined within blocks and the blocks are AND-combined. The optional setting block is left out because it would exclude 15 of 25 known records, including all five held-out validation records; reference standard, accuracy, and severity remain screening criteria."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The headings are verified and the malaria block includes species terms. The duplicate second probe is disclosed and is not treated as independent evidence; the first screened 30-record probe found no eligible records and the recorded response says one clean probe meets the standard-depth rule."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The rapid-test block now includes rapid antigen test*[tiab], with an explicit translation, and the malaria block has bare species names for vivax, ovale, malariae, and knowlesi. The complete evaluation retrieves all 25 known records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed Boolean expression is balanced and parsed. Proximity syntax is tested, and the packet reports no syntax errors or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2013-06-09 Entry Date ceiling is identified as a historical harness constraint, and the protocol/narrative require refreshing without that bound before current review use. R1-F2 is carried forward as accepted-risk."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The rapid-test block previously lacked explicit rapid antigen test wording.",
          "recommendation": "Add and test explicit rapid antigen test wording, including plural coverage or a tested truncation, and rerun the full evaluation.",
          "status": "resolved",
          "response": "The current block includes rapid antigen test*[tiab], reported with 226 results and an explicit Title/Abstract translation without translation issues. The full evaluation retrieves all 25 known records."
        },
        {
          "id": "R1-F2",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The evaluated query has an Entry Date ceiling of 2013-06-09 despite no date restriction in the review question, so it cannot retrieve records entered later.",
          "recommendation": "Label the run as a harness-limited historical evaluation and refresh without the harness ceiling, or with the intended current search date, before review use.",
          "status": "accepted-risk",
          "response": "The packet identifies the PSB_AS_OF 2013-06-09 Entry Date bound as required for this historical harness run. The protocol and narrative disclose the bound and require a refresh without it before current review use."
        },
        {
          "id": "R2-F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The two malaria category probes use the same seed and identical sample, so they do not provide two independent checks.",
          "recommendation": "Use an independently drawn and screened second sample before relying on a two-probe result.",
          "status": "rejected",
          "response": "The packet does not claim probe 2 as independent evidence and discloses that the default seed repeated the sample. It reports that the first screened 30-record probe found no eligible records and meets the stated standard-depth delivery rule requiring one clean probe; the duplicate adds no assurance."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

