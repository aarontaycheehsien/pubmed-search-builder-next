# PubMed search strategy: audit

Generated 2026-10-02T13:38:18+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In people with suspected non-falciparum or Plasmodium vivax malaria, what is the diagnostic accuracy of rapid diagnostic tests in malaria-endemic settings?
- Framework: PIRD
- Scope confirmed by user: no (The user asked to proceed without follow-up. Scope decisions are provisional: search malaria and rapid diagnostic tests; screen for uncomplicated non-falciparum/P. vivax disease, eligible reference standard, reported performance, and endemic setting. No user-supplied seeds. This is a historical PubMed snapshot with an Entrez Entry Date bound of 2013-06-09 required by the harness (PSB_AS_OF); it is not a publication-date limit and no [dp] restriction is used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Malaria, including non-falciparum and Plasmodium vivax | search | The target diagnosis is malaria; the vivax/non-falciparum subgroup is important to screening but may not be named consistently enough to require a narrow subtype block. |
| Malaria rapid diagnostic tests | search | The index test defines the review and is likely to be named in records. |
| Suspected uncomplicated malaria in an endemic setting | screen | Clinical status, severity, species subgroup, and endemicity may be reported only in full text or inconsistently. |
| Eligible reference standard | screen | Reference standards vary and should not be required in the search. |
| Diagnostic performance | screen | Accuracy outcomes are inconsistently described and should not be required. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T13:36:57+00:00
- Records added to PubMed up to: 2013-06-09
- Total records: 1,453
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Malaria[Mesh]` | 50,641 | none |
| 2 | `Malaria, Vivax[Mesh]` | 2,872 | none |
| 3 | `Plasmodium vivax[Mesh]` | 3,745 | none |
| 4 | `malaria[tiab]` | 55,839 | none |
| 5 | `plasmodium[tiab]` | 34,635 | none |
| 6 | `vivax[tiab]` | 5,921 | none |
| 7 | `Plasmodium vivax[tiab]` | 3,467 | none |
| 8 | `P. vivax[tiab]` | 2,944 | none |
| 9 | `non-falciparum[tiab]` | 55 | none |
| 10 | `nonfalciparum[tiab]` | 59 | none |
| 11 | `ovale[tiab]` | 5,356 | none |
| 12 | `malariae[tiab]` | 888 | none |
| 13 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12` | 79,530 | none |
| 14 | `Reagent Kits, Diagnostic[Mesh]` | 17,135 | none |
| 15 | `rapid diagnostic test[tiab]` | 579 | none |
| 16 | `rapid diagnostic tests[tiab]` | 769 | none |
| 17 | `rapid test[tiab]` | 2,005 | none |
| 18 | `rapid tests[tiab]` | 891 | none |
| 19 | `RDT[tiab]` | 653 | none |
| 20 | `RDTs[tiab]` | 303 | none |
| 21 | `immunochromatograph*[tiab]` | 1,749 | none |
| 22 | `lateral flow[tiab]` | 720 | none |
| 23 | `point-of-care[tiab]` | 6,137 | none |
| 24 | `dipstick[tiab]` | 2,112 | none |
| 25 | `strip test[tiab]` | 405 | none |
| 26 | `malaria antigen test[tiab]` | 3 | none |
| 27 | `malaria antigen tests[tiab]` | 3 | none |
| 28 | `antigen test[tiab]` | 1,412 | none |
| 29 | `antigen tests[tiab]` | 519 | none |
| 30 | `antigen detection[tiab]` | 3,135 | none |
| 31 | `HRP2[tiab]` | 168 | none |
| 32 | `HRP-2[tiab]` | 97 | none |
| 33 | `histidine-rich protein 2[tiab]` | 169 | none |
| 34 | `pLDH[tiab]` | 158 | none |
| 35 | `lactate dehydrogenase[tiab]` | 28,626 | none |
| 36 | `#14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35` | 62,398 | none |
| 37 | `#13 AND #36` | 1,453 | none |

### Strategy (single line, for copying into PubMed)

```text
((Malaria[Mesh] OR Malaria, Vivax[Mesh] OR Plasmodium vivax[Mesh] OR malaria[tiab] OR plasmodium[tiab] OR vivax[tiab] OR Plasmodium vivax[tiab] OR P. vivax[tiab] OR non-falciparum[tiab] OR nonfalciparum[tiab] OR ovale[tiab] OR malariae[tiab]) AND (Reagent Kits, Diagnostic[Mesh] OR rapid diagnostic test[tiab] OR rapid diagnostic tests[tiab] OR rapid test[tiab] OR rapid tests[tiab] OR RDT[tiab] OR RDTs[tiab] OR immunochromatograph*[tiab] OR lateral flow[tiab] OR point-of-care[tiab] OR dipstick[tiab] OR strip test[tiab] OR malaria antigen test[tiab] OR malaria antigen tests[tiab] OR antigen test[tiab] OR antigen tests[tiab] OR antigen detection[tiab] OR HRP2[tiab] OR HRP-2[tiab] OR histidine-rich protein 2[tiab] OR pLDH[tiab] OR lactate dehydrogenase[tiab])) AND ("1800/01/01"[edat] : "2013/06/09"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 5 | 5 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| malaria | 62,398 | 0 |
| rdt | 79,530 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,101 | initial | none | Initial two-block PIRD strategy; broad malaria and RDT vocabulary, no limits. Used screened pilot records for term mining. Excluded the 2023 Rapid Diagnostic Tests MeSH heading because of the 2013 entry-date bound. |
| 2 | 1,453 | rdt: +8 / -3 | none | Addressed critic round 1: removed the broad Diagnostic Tests, Routine heading; added malaria antigen and RDT-target terms (antigen detection, HRP2, pLDH, lactate dehydrogenase); removed equivalent duplicate clauses; recorded the required 2013-06-09 Entry Date as_of snapshot in protocol. No publication-date restriction. |
| 3 | 1,453 | malaria: +0 / -1 | none | Finalized round-1 revisions and removed the P vivax spelling clause after evaluation showed PubMed translates it identically to P. vivax. Retained explicit species names, historical Reagent Kits descriptor, and added antigen/target terms; no known record lost. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 4 findings; R1-1 should-fix open, R1-2 should-fix open, R1-3 should-fix open, R1-4 document open
- Round 2 on version 3: 4 findings; R1-1 should-fix resolved, R1-2 should-fix resolved, R1-3 should-fix resolved, R1-4 document resolved
- Round 3 on version 3: 4 findings; R1-1 should-fix resolved, R1-2 should-fix resolved, R1-3 should-fix resolved, R1-4 document resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 576 NCBI requests logged (201 from cache); strategy sha256 7c1986ee85ce._

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
      "checked_at": "2026-10-02T13:36:57+00:00",
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
      "checked_at": "2026-10-02T13:36:57+00:00",
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
      "checked_at": "2026-10-02T13:36:57+00:00",
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
      "checked_at": "2026-10-02T13:36:57+00:00",
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
    }
  ],
  "translation": "(\"malaria\"[MeSH Terms] OR \"malaria, vivax\"[MeSH Terms] OR \"plasmodium vivax\"[MeSH Terms] OR \"malaria\"[Title/Abstract] OR \"Plasmodium\"[Title/Abstract] OR \"vivax\"[Title/Abstract] OR \"plasmodium vivax\"[Title/Abstract] OR \"p vivax\"[Title/Abstract] OR \"non-falciparum\"[Title/Abstract] OR \"nonfalciparum\"[Title/Abstract] OR \"ovale\"[Title/Abstract] OR \"malariae\"[Title/Abstract]) AND (\"reagent kits, diagnostic\"[MeSH Terms] OR \"rapid diagnostic test\"[Title/Abstract] OR \"rapid diagnostic tests\"[Title/Abstract] OR \"rapid test\"[Title/Abstract] OR \"rapid tests\"[Title/Abstract] OR \"RDT\"[Title/Abstract] OR \"RDTs\"[Title/Abstract] OR \"immunochromatograph*\"[Title/Abstract] OR \"lateral flow\"[Title/Abstract] OR \"point-of-care\"[Title/Abstract] OR \"dipstick\"[Title/Abstract] OR \"strip test\"[Title/Abstract] OR \"malaria antigen test\"[Title/Abstract] OR \"malaria antigen tests\"[Title/Abstract] OR \"antigen test\"[Title/Abstract] OR \"antigen tests\"[Title/Abstract] OR \"antigen detection\"[Title/Abstract] OR \"HRP2\"[Title/Abstract] OR \"HRP-2\"[Title/Abstract] OR \"histidine rich protein 2\"[Title/Abstract] OR \"pLDH\"[Title/Abstract] OR \"lactate dehydrogenase\"[Title/Abstract]) AND 1800/01/01:2013/06/09[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "90db8dbc477a93d9d202498a6ef8e63f60850bca059a40bbfcbcf02970f6d95c",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Both searched blocks cover the named concepts, including bare vivax, P. vivax, non-falciparum, ovale, and malariae wording. The duplicate normalized forms (P. vivax/P vivax and point of care/point-of-care) are redundant but do not create a translation failure; the packet reports no PubMed translation errors or warnings."
        },
        "operators": {
          "verdict": "pass",
          "note": "The OR terms are grouped within the two concepts and the malaria and RDT blocks are combined with AND, consistent with the stated search roles. Broad malaria terms are justified because species subgroup and setting are screening criteria."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "Malaria and vivax headings are relevant and verified. The RDT block relies on broad Reagent Kits, Diagnostic and Diagnostic Tests, Routine headings; the latter describes routine procedures rather than rapid malaria testing. Review whether a more specific point-of-care, immunochromatography, or rapid-test heading is appropriate, and justify or remove the routine-tests heading after evaluation."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The strategy has useful malaria and device synonyms, but most device wording requires generic rapid/strip terminology. It should assess direct malaria rapid-antigen and assay-target wording (for example HRP2 and pLDH) to capture records whose abstracts name the antigen/test format without saying rapid diagnostic test or RDT. Five build-pilot records are development evidence only; the 100% figure is not independent validation."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no lint, translation, or PubMed syntax errors. No phrase warning requiring clause-specific interpretation is reported. The single truncation is not used in a proximity expression."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "No protocol limit is listed, but every executed query includes an Entry Date upper bound of 2013-06-09. The packet documents this as PSB_AS_OF rather than a publication-date limit; the delivered search must make this historical snapshot boundary explicit or remove/update it before a current comprehensive search."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Diagnostic Tests, Routine[Mesh] is included in the malaria RDT block even though its verified scope note describes procedures routinely performed in specified situations, not rapid malaria diagnostic tests. This weakens conceptual precision and may add unrelated records.",
          "recommendation": "Check for and test the most specific applicable MeSH headings for rapid point-of-care or immunochromatographic malaria testing. Remove Diagnostic Tests, Routine[Mesh] unless a documented sensitivity rationale supports retaining it; evaluate the changed full strategy.",
          "status": "open"
        },
        {
          "id": "R1-2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The test block does not include direct rapid-antigen or common malaria RDT target wording such as HRP2 and pLDH. Relevant abstracts may identify the assay by antigen/target without using rapid diagnostic test, RDT, strip, or point-of-care wording.",
          "recommendation": "Assess and test rapid antigen-test wording and common target names/variants (including HRP2 and pLDH/lactate dehydrogenase) in the malaria context, and retain additions only with their retrieval effects documented. Re-run the complete evaluation after changes.",
          "status": "open"
        },
        {
          "id": "R1-3",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "Although the strategy lists no limits and no publication-date limit, the executed query applies an Entry Date range ending 2013-06-09. That boundary excludes later-entered records and is not part of the stated review scope.",
          "recommendation": "Clearly label this as a historical evaluation snapshot, or update/remove the Entry Date cap for the operational search. Re-run the complete evaluation using the intended search date.",
          "status": "open"
        },
        {
          "id": "R1-4",
          "domain": "text_words",
          "severity": "document",
          "kind": "reporting",
          "finding": "The reported 5/5 known-record retrieval uses records screened during the build, explicitly marked as development rather than independent validation. No seeds were supplied, so the 100% result does not establish sensitivity against an independent set.",
          "recommendation": "Report the five records as development checks only and avoid presenting 100% as validation performance. Obtain an independent validation set if available and report its retrieval separately.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "977a4aea4d7f0e1dcfbf265a5db3481c3554748bac878015c0400a3ab2eccdbe",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched concepts are represented by bare malaria, Plasmodium, vivax, non-falciparum, nonfalciparum, ovale, and malariae terms, and the RDT block includes direct rapid-test and antigen wording. PubMed translations report no errors, warnings, or translation issues."
        },
        "operators": {
          "verdict": "pass",
          "note": "The malaria and RDT synonyms are ORed within their blocks, and the two searched concepts are combined with AND. Population/context, reference standard, and diagnostic performance remain screening criteria as specified."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The malaria headings are relevant and verified. Reagent Kits, Diagnostic is a broad but relevant heading for diagnostic kits; the accompanying text terms provide the rapid-test, strip, antigen, and assay-target wording. The previously questioned Diagnostic Tests, Routine heading has been removed."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The current strategy adds malaria antigen-test wording and HRP2, HRP-2, histidine-rich protein 2, pLDH, and lactate dehydrogenase terms in addition to rapid-test and device-format terms. These address the prior lexical gap. The five known records are explicitly identified as development records, not independent validation."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports empty lint and translation-issue lists, no PubMed errors or warnings, and no phrase warning requiring clause-specific interpretation. Truncation is used only in immunochromatograph* and not in proximity searching."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The executed search retains an Entry Date upper bound of 2013-06-09. The protocol notes explicitly identify it as a historical PubMed snapshot boundary required by the harness, not a publication-date limit; this is suitable only as the documented snapshot and not as an unrestricted current operational search."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Diagnostic Tests, Routine[Mesh] was included in the RDT block although its verified scope was not specific to rapid malaria tests.",
          "recommendation": "Remove the heading unless a sensitivity rationale supports retaining it, then evaluate the revised strategy.",
          "status": "resolved",
          "response": "Resolved in version 3: Diagnostic Tests, Routine[Mesh] is absent. The RDT block retains Reagent Kits, Diagnostic[Mesh] and text-word coverage."
        },
        {
          "id": "R1-2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier test block lacked direct malaria rapid-antigen and common RDT target wording such as HRP2 and pLDH.",
          "recommendation": "Assess rapid-antigen wording and common target names/variants, retain additions with retrieval effects documented, and re-evaluate the full strategy.",
          "status": "resolved",
          "response": "Resolved in version 3: malaria antigen test(s), antigen test(s), antigen detection, HRP2, HRP-2, histidine-rich protein 2, pLDH, and lactate dehydrogenase are included. The full query was evaluated; its count remains 1,453, with all five development records retrieved and no regression from the prior version."
        },
        {
          "id": "R1-3",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The executed query has an Entry Date upper bound of 2013-06-09, which excludes later-entered records and is not a publication-date limit.",
          "recommendation": "Label the search as a historical snapshot or update/remove the boundary for an operational search, and evaluate with the intended date.",
          "status": "resolved",
          "response": "Resolved for this packet as a historical evaluation snapshot: the protocol notes explicitly document the 2013-06-09 Entrez Entry Date boundary as a harness-required PSB_AS_OF value and state that it is not a publication-date limit. The delivered query should retain that snapshot label."
        },
        {
          "id": "R1-4",
          "domain": "text_words",
          "severity": "document",
          "kind": "reporting",
          "finding": "The 5/5 retrieval result is based on records screened during the build and does not constitute independent validation.",
          "recommendation": "Report the five records as development checks and avoid presenting the result as independent validation; report an independent set separately if available.",
          "status": "resolved",
          "response": "Resolved in the evidence reporting: the set independence field says the records were used for development, not independent, and the protocol notes state that no user-supplied seeds were available. The 100% figure is therefore not independent validation."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "977a4aea4d7f0e1dcfbf265a5db3481c3554748bac878015c0400a3ab2eccdbe",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The malaria block includes bare malaria, Plasmodium, vivax, non-falciparum, nonfalciparum, ovale, and malariae terms; the RDT block includes direct rapid-test and antigen/test-target wording. The packet reports no translation issues."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within the malaria and RDT blocks, and the two searched concepts are combined with AND. Population/context, reference standard, and diagnostic performance remain screening criteria as specified."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The malaria and vivax headings are relevant. Diagnostic Tests, Routine[Mesh] has been removed; Reagent Kits, Diagnostic[Mesh] is broad but relevant and is accompanied by RDT text-word coverage."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The current strategy contains direct rapid-test and device-format wording plus malaria antigen-test, antigen-detection, HRP2/HRP-2, histidine-rich protein 2, pLDH, and lactate dehydrogenase terms. The full strategy was evaluated and the packet reports retrieval of all five development records; they are explicitly not independent validation records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports empty lint and translation-issue lists, no PubMed errors or warnings, and no phrase warning requiring clause-specific interpretation. The truncation is used only in immunochromatograph* and not in proximity searching."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entry Date upper bound of 2013-06-09 is explicitly documented as the historical PubMed snapshot boundary required by the harness, not as a publication-date limit. The five-record set is identified as development evidence, not independent validation."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Diagnostic Tests, Routine[Mesh] was included in the RDT block although its verified scope was not specific to rapid malaria tests.",
          "recommendation": "Remove the heading unless a sensitivity rationale supports retaining it, then evaluate the revised strategy.",
          "status": "resolved",
          "response": "Resolved in version 3: Diagnostic Tests, Routine[Mesh] is absent. Reagent Kits, Diagnostic[Mesh] and the RDT text-word coverage remain."
        },
        {
          "id": "R1-2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier test block lacked direct malaria rapid-antigen and common RDT target wording such as HRP2 and pLDH.",
          "recommendation": "Assess rapid-antigen wording and common target names/variants, retain additions with retrieval effects documented, and re-evaluate the full strategy.",
          "status": "resolved",
          "response": "Resolved in version 3: malaria antigen test(s), antigen test(s), antigen detection, HRP2, HRP-2, histidine-rich protein 2, pLDH, and lactate dehydrogenase are included. The full query was evaluated; its count remains 1,453 and all five development records were retrieved without regression from the prior version."
        },
        {
          "id": "R1-3",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "filter",
          "finding": "The executed query has an Entry Date upper bound of 2013-06-09, which excludes later-entered records and is not a publication-date limit.",
          "recommendation": "Label the search as a historical snapshot or update/remove the boundary for an operational search, and evaluate with the intended date.",
          "status": "resolved",
          "response": "Resolved for this packet as a historical evaluation snapshot: the protocol notes explicitly document the 2013-06-09 Entrez Entry Date boundary as the harness-required PSB_AS_OF value and state that it is not a publication-date limit. The delivered query should retain that snapshot label."
        },
        {
          "id": "R1-4",
          "domain": "text_words",
          "severity": "document",
          "kind": "reporting",
          "finding": "The 5/5 retrieval result is based on records screened during the build and does not constitute independent validation.",
          "recommendation": "Report the five records as development checks and avoid presenting the result as independent validation; report an independent set separately if available.",
          "status": "resolved",
          "response": "Resolved in the evidence reporting: the set independence field identifies the records as used for development, not independent, and the protocol notes state that no user-supplied seeds were available. The 100% figure is therefore not independent validation."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

