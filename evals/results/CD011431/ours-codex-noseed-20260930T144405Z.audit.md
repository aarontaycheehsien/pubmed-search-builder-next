# PubMed search strategy: audit

Generated 2026-09-30T15:20:51+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Rapid diagnostic tests for diagnosing uncomplicated non-falciparum or Plasmodium vivax malaria in endemic countries (a diagnostic-test-accuracy review: in people with suspected non-falciparum / P. vivax malaria, what is the accuracy of rapid diagnostic tests?)
- Framework: PIRD
- Scope confirmed by user: yes (User asked not to be contacted with questions during this run; scope and assumptions were set from the supplied question and eligibility criteria. PSB_AS_OF=2013-06-09 is required to model PubMed records entered by the requested as-of date; it is a record-coverage cutoff, not a publication-date eligibility limit. No publication-date limit is used. No known relevant records were supplied. Malaria condition and RDT are search blocks; suspected/uncomplicated status, endemic setting, eligible reference standard and performance are screened. The RDT proximity clauses are intended to retrieve either word order and up to one intervening word (for example, rapid malaria diagnostic test and rapid malaria test). PubMed translated the clauses as Title/Abstract proximity searches with no warning; counts were 2,701 for rapid diagnostic ~1 versus 579 for the contiguous rapid diagnostic test phrase, and 6,172 for rapid test ~1 versus 2,005 for the contiguous rapid test phrase. Against the 15 development records, the clauses retrieved 14 and 8 records respectively; they are OR alternatives, not required filters.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Non-falciparum or Plasmodium vivax malaria | search | Target diagnosis; eligible records must concern malaria and may name vivax or another non-falciparum species without using the category phrase. |
| Malaria rapid diagnostic tests | search | Index test; every eligible study evaluates a malaria RDT, which is a named and searchable technology. |
| People with suspected uncomplicated malaria in an endemic setting | screen | Suspected status, uncomplicated severity and endemic setting are eligibility properties inconsistently reported in searchable fields. |
| Eligible reference standard and diagnostic performance | screen | Reference standard and accuracy outcomes are PIRD screening criteria and are not required as search blocks. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T15:20:08+00:00
- Records added to PubMed up to: 2013-06-09
- Total records: 1,101
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Malaria[Mesh]` | 50,641 | none |
| 2 | `Malaria, Vivax[Mesh]` | 2,872 | none |
| 3 | `Plasmodium vivax[Mesh]` | 3,745 | none |
| 4 | `Plasmodium malariae[Mesh]` | 810 | none |
| 5 | `Plasmodium ovale[Mesh]` | 131 | none |
| 6 | `malaria[tiab]` | 55,839 | none |
| 7 | `paludism[tiab]` | 72 | none |
| 8 | `plasmodium[tiab]` | 34,635 | none |
| 9 | `plasmodia[tiab]` | 1,281 | none |
| 10 | `plasmodial[tiab]` | 1,131 | none |
| 11 | `vivax[tiab]` | 5,921 | none |
| 12 | `vivax malaria[tiab]` | 1,672 | none |
| 13 | `P. vivax[tiab]` | 2,944 | none |
| 14 | `Plasmodium vivax[tiab]` | 3,467 | none |
| 15 | `Plasmodium malariae[tiab]` | 421 | none |
| 16 | `P. malariae[tiab]` | 571 | none |
| 17 | `Plasmodium ovale[tiab]` | 274 | none |
| 18 | `P. ovale[tiab]` | 503 | none |
| 19 | `Plasmodium knowlesi[tiab]` | 687 | none |
| 20 | `P. knowlesi[tiab]` | 425 | none |
| 21 | `non-falciparum[tiab]` | 55 | none |
| 22 | `non falciparum[tiab]` | 55 | none |
| 23 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22` | 75,728 | none |
| 24 | `Diagnostic Tests, Routine[Mesh]` | 7,136 | none |
| 25 | `Reagent Kits, Diagnostic[Mesh]` | 17,135 | none |
| 26 | `Point-of-Care Testing[Mesh]` | 1 | none |
| 27 | `rapid diagnostic test*[tiab]` | 1,321 | none |
| 28 | `"rapid diagnostic"[tiab:~1]` | 2,701 | none |
| 29 | `"rapid test"[tiab:~1]` | 6,172 | none |
| 30 | `RDT[tiab]` | 653 | none |
| 31 | `RDTs[tiab]` | 303 | none |
| 32 | `immunochromatograph*[tiab]` | 1,749 | none |
| 33 | `immunochromatographic assay[tiab]` | 336 | none |
| 34 | `lateral flow[tiab]` | 720 | none |
| 35 | `dipstick[tiab]` | 2,112 | none |
| 36 | `point-of-care test*[tiab]` | 1,572 | none |
| 37 | `rapid antigen test*[tiab]` | 226 | none |
| 38 | `#24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37` | 35,779 | none |
| 39 | `#23 AND #38` | 1,101 | none |

### Strategy (single line, for copying into PubMed)

```text
((Malaria[Mesh] OR Malaria, Vivax[Mesh] OR Plasmodium vivax[Mesh] OR Plasmodium malariae[Mesh] OR Plasmodium ovale[Mesh] OR malaria[tiab] OR paludism[tiab] OR plasmodium[tiab] OR plasmodia[tiab] OR plasmodial[tiab] OR vivax[tiab] OR vivax malaria[tiab] OR P. vivax[tiab] OR Plasmodium vivax[tiab] OR Plasmodium malariae[tiab] OR P. malariae[tiab] OR Plasmodium ovale[tiab] OR P. ovale[tiab] OR Plasmodium knowlesi[tiab] OR P. knowlesi[tiab] OR non-falciparum[tiab] OR non falciparum[tiab]) AND (Diagnostic Tests, Routine[Mesh] OR Reagent Kits, Diagnostic[Mesh] OR Point-of-Care Testing[Mesh] OR rapid diagnostic test*[tiab] OR "rapid diagnostic"[tiab:~1] OR "rapid test"[tiab:~1] OR RDT[tiab] OR RDTs[tiab] OR immunochromatograph*[tiab] OR immunochromatographic assay[tiab] OR lateral flow[tiab] OR dipstick[tiab] OR point-of-care test*[tiab] OR rapid antigen test*[tiab])) AND ("1800/01/01"[edat] : "2013/06/09"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 15 | 15 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Non-falciparum or Plasmodium vivax malaria | 1 | `Plasmodium[Mesh] OR parasite*[tiab] OR protozoa[tiab]` | 221 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| malaria | 35,779 | 0 |
| rdt | 75,728 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial strategy uses target-diagnosis and RDT blocks with MeSH and title/abstract terms; included pilot records screened against supplied eligibility to check vocabulary and retrieval. |
| 2 | 0 | malaria: +22 / -0; rdt: +14 / -0 | none | Corrected strategy file to the skill's OR-ed terms schema; target diagnosis and RDT blocks include MeSH and title/abstract synonyms. |
| 3 | 1,101 | rdt: +2 / -2 | none | Quoted proximity phrases as required by PubMed syntax; no intended wording or scope changed. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 3 findings; F1 should-fix open, F2 should-fix open, F3 should-fix open
- Round 2 on version 3: 3 findings; F1 should-fix open, F2 should-fix resolved, F3 should-fix resolved
- Round 3 on version 3: 3 findings; F1 should-fix resolved, F2 should-fix resolved, F3 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 668 NCBI requests logged (316 from cache); strategy sha256 8ca58d107eb8._

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
      "checked_at": "2026-09-30T15:20:08+00:00",
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
      "checked_at": "2026-09-30T15:20:08+00:00",
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
      "checked_at": "2026-09-30T15:20:08+00:00",
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
      "requested": "Plasmodium malariae",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:20:08+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D010965",
          "name": "Plasmodium malariae",
          "type": "descriptor",
          "scope_note": "A protozoan parasite that occurs primarily in subtropical and temperate areas. It is the causal agent of quartan malaria. As the parasite grows it exhibits little ameboid activity.",
          "tree_numbers": [
            "B01.043.075.380.611.661"
          ],
          "entry_terms": 0,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D010965",
      "preferred_label": "Plasmodium malariae",
      "type": "descriptor",
      "location": "vocabulary:4",
      "term": {
        "text": "Plasmodium malariae",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Plasmodium ovale",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:20:08+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D041122",
          "name": "Plasmodium ovale",
          "type": "descriptor",
          "scope_note": "A species of protozoan parasite causing MALARIA. It is the rarest of the four species of PLASMODIUM infecting humans, but is common in West African countries and neighboring areas.",
          "tree_numbers": [
            "B01.043.075.380.611.700"
          ],
          "entry_terms": 2,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D041122",
      "preferred_label": "Plasmodium ovale",
      "type": "descriptor",
      "location": "vocabulary:5",
      "term": {
        "text": "Plasmodium ovale",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diagnostic Tests, Routine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:20:08+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "Diagnostic Tests, Routine",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Reagent Kits, Diagnostic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:20:08+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "Reagent Kits, Diagnostic",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Point-of-Care Testing",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T15:20:08+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000067716",
          "name": "Point-of-Care Testing",
          "type": "descriptor",
          "scope_note": "Allows patient diagnoses in the physician’s office, in other ambulatory setting or at bedside. The results of care are timely, and allow rapid treatment to the patient. (from NIH Fact Sheet Point-of-Care Diagnostic Testing, 2010.)",
          "tree_numbers": [
            "N04.590.874.500"
          ],
          "entry_terms": 26,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000067716",
      "preferred_label": "Point-of-Care Testing",
      "type": "descriptor",
      "location": "vocabulary:25",
      "term": {
        "text": "Point-of-Care Testing",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"malaria\"[MeSH Terms] OR \"malaria, vivax\"[MeSH Terms] OR \"plasmodium vivax\"[MeSH Terms] OR \"plasmodium malariae\"[MeSH Terms] OR \"plasmodium ovale\"[MeSH Terms] OR \"malaria\"[Title/Abstract] OR \"paludism\"[Title/Abstract] OR \"Plasmodium\"[Title/Abstract] OR \"plasmodia\"[Title/Abstract] OR \"plasmodial\"[Title/Abstract] OR \"vivax\"[Title/Abstract] OR \"vivax malaria\"[Title/Abstract] OR \"p vivax\"[Title/Abstract] OR \"plasmodium vivax\"[Title/Abstract] OR \"plasmodium malariae\"[Title/Abstract] OR \"p malariae\"[Title/Abstract] OR \"plasmodium ovale\"[Title/Abstract] OR \"p ovale\"[Title/Abstract] OR \"plasmodium knowlesi\"[Title/Abstract] OR \"p knowlesi\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract]) AND (\"diagnostic tests, routine\"[MeSH Terms] OR \"reagent kits, diagnostic\"[MeSH Terms] OR \"point of care testing\"[MeSH Terms] OR \"rapid diagnostic test*\"[Title/Abstract] OR \"rapid diagnostic\"[Title/Abstract:~1] OR \"rapid test\"[Title/Abstract:~1] OR \"RDT\"[Title/Abstract] OR \"RDTs\"[Title/Abstract] OR \"immunochromatograph*\"[Title/Abstract] OR \"immunochromatographic assay\"[Title/Abstract] OR \"lateral flow\"[Title/Abstract] OR \"dipstick\"[Title/Abstract] OR \"point of care test*\"[Title/Abstract] OR \"rapid antigen test*\"[Title/Abstract]) AND 1800/01/01:2013/06/09[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "0397bd08b874c6e0e7a3f155e8b6380b3869d4d497f7ca8947a34b2a2e5625be",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no translation issues, and PubMed translations preserve the MeSH and title/abstract fields. The malaria text words include generic malaria and Plasmodium terms as well as named target species."
        },
        "operators": {
          "verdict": "revise",
          "note": "The two proximity clauses need clause-specific interpretation. The packet warns that proximity permits either word order; it provides no rationale or examples showing why ~1 is appropriate for rapid diagnostic and rapid test."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed MeSH headings are reported as verified, and the syntax check reports no translation issues."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word block includes malaria and Plasmodium, vivax, named non-falciparum species, and rapid-test technology terms. No deletion is justified by the packet's seed coverage."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query translated without reported syntax errors or warnings. The two proximity clauses still need the operator review noted above."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The executed query applies an Entry Date range ending 2013-06-09. The packet documents that bound but does not explain why this cutoff fits the review scope; it excludes records entered into PubMed after that date, regardless of publication date."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "syntax",
          "finding": "The clauses \"rapid diagnostic\"[tiab:~1] and \"rapid test\"[tiab:~1] use proximity operators, but the packet gives no clause-specific rationale or tested examples for their order and distance behavior.",
          "recommendation": "Document what each clause is intended to retrieve and test representative expressions against known relevant records. If either clause is changed or removed, run a complete evaluation again.",
          "status": "open",
          "response": null
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The executed query includes an Entry Date limit ending 2013-06-09. Although the packet identifies the as-of bound, it gives no review-scope rationale for this cutoff. It excludes records entered after that date, including records about earlier studies.",
          "recommendation": "State the intended date coverage and rationale for using PubMed Entry Date. Confirm that the cutoff matches the review scope, and report the resulting coverage clearly.",
          "status": "open",
          "response": null
        },
        {
          "id": "F3",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The 15 relevant records are described as screened pilot results and are the only reported known set. The 100% recall result therefore does not establish independent validation. The category probe sampled 30 records outside the malaria block, but it does not independently validate the RDT block.",
          "recommendation": "Label the reported recall as development-set coverage and state that independent validation is absent. Add an independent validation set if available, and report its coverage separately.",
          "status": "open",
          "response": null
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "9bb536bb4b69820f7b67368cbd594ce5bec37d8d9963a07a9b5931a446ddf820",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The malaria block includes generic malaria and Plasmodium terms, vivax, and named non-falciparum species. The packet reports no translation issues."
        },
        "operators": {
          "verdict": "revise",
          "note": "The two ~1 clauses still lack clause-specific interpretation and tested examples. The packet provides no evidence for their order and distance behavior, so F1 remains open."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports the listed MeSH headings as verified and no translation issues."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word blocks cover malaria and Plasmodium terminology, target species, and rapid-test technologies. Seed coverage alone does not justify deleting terms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The complete query translated without reported errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The packet explains that the 2013-06-09 Entry Date cutoff is required to model the requested as-of date and is a record-coverage cutoff, not a publication-date eligibility limit."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "syntax",
          "finding": "The clauses \"rapid diagnostic\"[tiab:~1] and \"rapid test\"[tiab:~1] still lack clause-specific interpretation and tested examples for order and distance behavior.",
          "recommendation": "Document what each clause is intended to retrieve and test representative expressions against relevant records. If either clause is changed or removed, run a complete evaluation again.",
          "status": "open",
          "response": null
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The executed query applies an Entry Date limit ending 2013-06-09.",
          "recommendation": "Document the intended date coverage, the reason for using PubMed Entry Date, and the resulting coverage.",
          "status": "resolved",
          "response": "The protocol notes that the cutoff is required to model the requested as-of date and limits record coverage rather than publication-date eligibility. No publication-date limit is used."
        },
        {
          "id": "F3",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The 15 relevant records are a development set, so their 100% recall does not establish independent validation. No independent validation set is reported.",
          "recommendation": "Report recall as development-set coverage and disclose that independent validation is absent; add a separate independent validation set if available.",
          "status": "resolved",
          "response": "The packet identifies the relevant records as screened during the build and used for development, not as independent validation. The reported 100% recall is development-set coverage; no independent validation set is reported."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "ac24cc15a97e09c87ae391662bcbdf478afd24f13c572e9539cfcc3116ab47dc",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The malaria block covers malaria, Plasmodium, vivax, and named non-falciparum species. The category probe found no relevant records among 30 screened records outside the block."
        },
        "operators": {
          "verdict": "pass",
          "note": "The protocol explains that both proximity clauses allow either order and one intervening word, gives examples and counts, and reports retrieval against the development records. The clauses remain OR alternatives."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed MeSH headings are reported as verified, with no translation issues."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The blocks include generic malaria and Plasmodium terms, named target species, and rapid-test technology terms. The packet does not justify deleting terms based on seed coverage."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The strategy translated without reported syntax errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entry Date cutoff is documented as required to model the requested as-of date and as record-coverage rather than publication-date eligibility; no publication-date limit is used."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "syntax",
          "finding": "The proximity clauses previously lacked clause-specific interpretation and tested examples.",
          "recommendation": "Document intended retrieval and test representative expressions; rerun the complete evaluation if either clause is changed or removed.",
          "status": "resolved",
          "response": "The protocol explains that the clauses allow either word order with up to one intervening word, gives examples, reports clause counts and retrieval against the 15 development records, and identifies them as OR alternatives."
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The executed query uses an Entry Date limit ending 2013-06-09.",
          "recommendation": "Document the intended date coverage, rationale for PubMed Entry Date, and resulting coverage.",
          "status": "resolved",
          "response": "The protocol states that the cutoff models the requested as-of date and limits record coverage, not publication-date eligibility. No publication-date limit is used."
        },
        {
          "id": "F3",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The 15 relevant records are a development set, so their 100% recall does not establish independent validation; the malaria category probe does not independently validate the RDT block.",
          "recommendation": "Report recall as development-set coverage and disclose that independent validation is absent; add a separate independent set if available.",
          "status": "resolved",
          "response": "The packet identifies the 15 records as development records from screened pilot results; they are not an independent validation set. No independent validation set is reported."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

