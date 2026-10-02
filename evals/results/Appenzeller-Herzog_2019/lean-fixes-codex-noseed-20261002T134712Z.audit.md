# PubMed search strategy: audit

Generated 2026-10-02T14:08:13+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Comparative effectiveness of common therapies for Wilson disease
- Framework: PICO
- Scope confirmed by user: no (User asked to proceed without follow-up and supplied no known relevant articles. Assumption: common therapies means pharmacologic management, including chelators and zinc; direct comparative effectiveness is screened, while specific comparator/outcome terms and study design are not required. Excludes liver transplantation as outside this assumed pharmacotherapy scope. Discovery was cutoff-bounded and included a prior review (PMID 19210288), similar/cited-in candidates, and title-focused pilots. Scope is provisional because the user could not confirm it.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Wilson disease | search | The disease is the population-defining topic and should be reliably named or indexed. |
| Pharmacologic therapy for Wilson disease | search | Comparative effectiveness requires a drug treatment; generic treatment terms and established agent names can retrieve comparative studies. |
| Comparators between therapies | screen | Comparator terminology is inconsistently reported; screen for a direct comparison. |
| Effectiveness and safety outcomes | screen | Outcomes vary and may not be stated in abstracts; screen for effectiveness or safety. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T14:07:30+00:00
- Records added to PubMed up to: 2018-12-23
- Total records: 4,099
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Hepatolenticular Degeneration"[Mesh]` | 5,697 | none |
| 2 | `Wilson*[tiab]` | 11,437 | none |
| 3 | `"hepatolenticular degeneration"[tiab]` | 946 | none |
| 4 | `"hepatocerebral degeneration"[tiab]` | 142 | none |
| 5 | `"copper storage disease"[tiab]` | 25 | none |
| 6 | `"Westphal-Strumpell syndrome"[tiab]` | 1 | none |
| 7 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6` | 12,978 | none |
| 8 | `"Drug Therapy"[Mesh]` | 1,305,324 | none |
| 9 | `"Penicillamine"[Mesh]` | 7,878 | none |
| 10 | `"Trientine"[Mesh]` | 380 | none |
| 11 | `"Zinc Compounds"[Mesh]` | 12,484 | none |
| 12 | `"Zinc"[Mesh]` | 58,485 | none |
| 13 | `treat*[tiab]` | 5,019,714 | none |
| 14 | `therap*[tiab]` | 2,661,898 | none |
| 15 | `pharmacotherap*[tiab]` | 32,759 | none |
| 16 | `chelat*[tiab]` | 62,346 | none |
| 17 | `penicillamin*[tiab]` | 6,973 | none |
| 18 | `trientin*[tiab]` | 220 | none |
| 19 | `zinc[tiab]` | 108,490 | none |
| 20 | `"zinc acetate"[tiab]` | 817 | none |
| 21 | `"zinc sulfate"[tiab]` | 1,531 | none |
| 22 | `tetrathiomolybdate[tiab]` | 351 | none |
| 23 | `dimercaprol[tiab]` | 623 | none |
| 24 | `"Unithiol"[Mesh]` | 571 | none |
| 25 | `Unithiol[tiab]` | 216 | none |
| 26 | `DMPS[tiab]` | 745 | none |
| 27 | `dimercaptopropane*[tiab]` | 267 | none |
| 28 | `#8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27` | 7,044,887 | none |
| 29 | `#7 AND #28` | 4,099 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Hepatolenticular Degeneration"[Mesh] OR Wilson*[tiab] OR "hepatolenticular degeneration"[tiab] OR "hepatocerebral degeneration"[tiab] OR "copper storage disease"[tiab] OR "Westphal-Strumpell syndrome"[tiab]) AND ("Drug Therapy"[Mesh] OR "Penicillamine"[Mesh] OR "Trientine"[Mesh] OR "Zinc Compounds"[Mesh] OR "Zinc"[Mesh] OR treat*[tiab] OR therap*[tiab] OR pharmacotherap*[tiab] OR chelat*[tiab] OR penicillamin*[tiab] OR trientin*[tiab] OR zinc[tiab] OR "zinc acetate"[tiab] OR "zinc sulfate"[tiab] OR tetrathiomolybdate[tiab] OR dimercaprol[tiab] OR "Unithiol"[Mesh] OR Unithiol[tiab] OR DMPS[tiab] OR dimercaptopropane*[tiab])) AND ("1800/01/01"[edat] : "2018/12/23"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 4 | 4 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| wilson | 7,044,887 | 0 |
| therapy | 12,978 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial two-block strategy; disease plus broad pharmacologic treatment vocabulary, no limits. No seeds were supplied. |
| 2 | 3,962 | wilson: +8 / -0; therapy: +18 / -0 | none | Initial two-block strategy; disease plus broad pharmacologic treatment vocabulary, no limits. No seeds were supplied. |
| 3 | 4,115 | wilson: +0 / -2; therapy: +2 / -3 | none | Revised vocabulary after reviewing PubMed translations and screening comparative-treatment candidates: removed a zero-hit synonym with phrase-index warning and a phrase PubMed could not translate; added Zinc MeSH/free text based on relevant record indexing. |
| 4 | 4,099 | therapy: +0 / -1 | none | Removed Chelating Agents[Mesh] because the MeSH authority check returned duplicate, ambiguous records and blocks technical validation; agent-specific headings plus text chelat* terms remain. No known relevant records were lost in the prior evaluation. |
| 5 | 4,099 | therapy: +4 / -0 | none | Added verified Unithiol MeSH heading and common text forms (Unithiol, DMPS, dimercaptopropane*) following critic finding R1-LEX-DMPS and MeSH entry-term review. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4 (same-context critic; no independent fresh-context reviewer was available in this run): 1 findings; R1-LEX-DMPS should-fix open
- Round 2 on version 5 (same-context critic; reviewed the updated packet after applying the one lexical recommendation): 1 findings; R1-LEX-DMPS should-fix resolved
- Round 3 on version 5 (same-context closing critic; verifies the only earlier finding was addressed): 1 findings; R1-LEX-DMPS should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 535 NCBI requests logged (211 from cache); strategy sha256 77308290a940._

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
      "requested": "Hepatolenticular Degeneration",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:07:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D006527",
          "name": "Hepatolenticular Degeneration",
          "type": "descriptor",
          "scope_note": "A rare autosomal recessive disease characterized by the deposition of copper in the BRAIN; LIVER; CORNEA; and other organs. It is caused by defects in the ATP7B gene encoding copper-transporting ATPase 2 (EC 3.6.3.4), also known as the Wilson disease protein. The overload of copper inevitably leads to progressive liver and neurological dysfunction such as LIVER CIRRHOSIS; TREMOR; ATAXIA and int...",
          "tree_numbers": [
            "C06.552.413",
            "C10.228.140.079.493",
            "C10.228.140.163.100.360",
            "C10.228.662.400",
            "C10.574.500.487",
            "C16.320.400.361",
            "C16.320.565.189.360",
            "C16.320.565.618.403",
            "C18.452.132.100.360",
            "C18.452.648.189.360",
            "C18.452.648.618.403"
          ],
          "entry_terms": 47,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D006527",
      "preferred_label": "Hepatolenticular Degeneration",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"Hepatolenticular Degeneration\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Drug Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:07:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "Q000188",
          "name": "drug therapy",
          "type": "qualifier",
          "scope_note": "Used with disease headings for the treatment of disease by the administration of drugs, chemicals, and antibiotics. For diet therapy and radiotherapy, use specific subheadings. Excludes immunotherapy for which therapy is used.",
          "tree_numbers": [
            "Y11.020"
          ],
          "entry_terms": 3,
          "mapped_to": null
        },
        {
          "ui": "D004358",
          "name": "Drug Therapy",
          "type": "descriptor",
          "scope_note": "The use of DRUGS to treat a DISEASE or its symptoms. One example is the use of ANTINEOPLASTIC AGENTS to treat CANCER.",
          "tree_numbers": [
            "E02.319"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004358",
      "preferred_label": "Drug Therapy",
      "type": "descriptor",
      "location": "vocabulary:7",
      "term": {
        "text": "\"Drug Therapy\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Penicillamine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:07:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D010396",
          "name": "Penicillamine",
          "type": "descriptor",
          "scope_note": "3-Mercapto-D-valine. The most characteristic degradation product of the penicillin antibiotics. It is used as an antirheumatic and as a chelating agent in Wilson's disease.",
          "tree_numbers": [
            "D02.886.030.786",
            "D12.125.166.786"
          ],
          "entry_terms": 13,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D010396",
      "preferred_label": "Penicillamine",
      "type": "descriptor",
      "location": "vocabulary:8",
      "term": {
        "text": "\"Penicillamine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Trientine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:07:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D014266",
          "name": "Trientine",
          "type": "descriptor",
          "scope_note": "An ethylenediamine derivative used as stabilizer for EPOXY RESINS, as ampholyte for ISOELECTRIC FOCUSING and as chelating agent for copper in HEPATOLENTICULAR DEGENERATION.",
          "tree_numbers": [
            "D02.092.782.258.368.880"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D014266",
      "preferred_label": "Trientine",
      "type": "descriptor",
      "location": "vocabulary:9",
      "term": {
        "text": "\"Trientine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc Compounds",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:07:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D017967",
          "name": "Zinc Compounds",
          "type": "descriptor",
          "scope_note": "Inorganic compounds that contain zinc as an integral part of the molecule.",
          "tree_numbers": [
            "D01.975"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D017967",
      "preferred_label": "Zinc Compounds",
      "type": "descriptor",
      "location": "vocabulary:10",
      "term": {
        "text": "\"Zinc Compounds\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:07:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D015032",
          "name": "Zinc",
          "type": "descriptor",
          "scope_note": "A metallic element of atomic number 30 and atomic weight 65.38. It is a necessary trace element in the diet, forming an essential part of many enzymes, and playing an important role in protein synthesis and in cell division. Zinc deficiency is associated with ANEMIA, short stature, HYPOGONADISM, impaired WOUND HEALING, and geophagia. It is known by the symbol Zn.",
          "tree_numbers": [
            "D01.268.556.940",
            "D01.268.956.906",
            "D01.552.544.940"
          ],
          "entry_terms": 0,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D015032",
      "preferred_label": "Zinc",
      "type": "descriptor",
      "location": "vocabulary:11",
      "term": {
        "text": "\"Zinc\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Unithiol",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T14:07:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D014494",
          "name": "Unithiol",
          "type": "descriptor",
          "scope_note": "A chelating agent used as an antidote to heavy metal poisoning.",
          "tree_numbers": [
            "D02.886.489.180.900"
          ],
          "entry_terms": 19,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D014494",
      "preferred_label": "Unithiol",
      "type": "descriptor",
      "location": "vocabulary:23",
      "term": {
        "text": "\"Unithiol\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Hepatolenticular Degeneration\"[MeSH Terms] OR \"wilson*\"[Title/Abstract] OR \"Hepatolenticular Degeneration\"[Title/Abstract] OR \"hepatocerebral degeneration\"[Title/Abstract] OR \"copper storage disease\"[Title/Abstract] OR \"Westphal-Strumpell syndrome\"[Title/Abstract]) AND (\"Drug Therapy\"[MeSH Terms] OR \"Penicillamine\"[MeSH Terms] OR \"Trientine\"[MeSH Terms] OR \"Zinc Compounds\"[MeSH Terms] OR \"Zinc\"[MeSH Terms] OR \"treat*\"[Title/Abstract] OR \"therap*\"[Title/Abstract] OR \"pharmacotherap*\"[Title/Abstract] OR \"chelat*\"[Title/Abstract] OR \"penicillamin*\"[Title/Abstract] OR \"trientin*\"[Title/Abstract] OR \"Zinc\"[Title/Abstract] OR \"zinc acetate\"[Title/Abstract] OR \"zinc sulfate\"[Title/Abstract] OR \"tetrathiomolybdate\"[Title/Abstract] OR \"dimercaprol\"[Title/Abstract] OR \"Unithiol\"[MeSH Terms] OR \"Unithiol\"[Title/Abstract] OR \"DMPS\"[Title/Abstract] OR \"dimercaptopropane*\"[Title/Abstract]) AND 1800/01/01:2018/12/23[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "049702f3e78d5002de4a3e0f967fb6abbfd60fb830ae7569c6c16b0257d0959a",
      "note": "same-context critic; no independent fresh-context reviewer was available in this run",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Wilson disease plus drug treatment are the two necessary named concepts; comparators and outcomes are screened. No unnecessary design or outcome block."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two concept blocks are OR-expanded and AND-combined. No NOT or proximity operators."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Disease heading and drug/agent headings are explicitly tagged and verified. A technically ambiguous Chelating Agents heading was removed; chelat* text and named agent headings remain."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The 2018 treatment literature also names sodium dimercaptopropane sulfonate (DMPS/Unithiol), a Wilson disease chelator absent from the current agent vocabulary. Include its established forms to reduce avoidable loss."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Field tags and truncation lengths are valid; current evaluation reports no translation or syntax issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No limits or study-design filters are imposed; the Entrez cutoff is set separately as requested."
        }
      },
      "findings": [
        {
          "id": "R1-LEX-DMPS",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "therapy",
          "finding": "Sodium dimercaptopropane sulfonate (DMPS/Unithiol), described as a Wilson disease treatment in cutoff-eligible treatment literature, is absent from the pharmacologic therapy block.",
          "recommendation": "Add the verified Unithiol MeSH heading and common DMPS/sodium dimercaptopropane sulfonate free-text variants, then evaluate the updated strategy.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "262094e208a3e2907f26c4f33463fccc7e15d0b732b834a647106f2a110243ad",
      "note": "same-context critic; reviewed the updated packet after applying the one lexical recommendation",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The required Wilson disease and pharmacologic treatment blocks remain appropriate. Comparator and outcome criteria stay at screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR within concept blocks, AND between concepts; no NOT or proximity."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Disease, Drug Therapy, and named agent MeSH headings are explicitly tagged and the current authority checks pass. Unithiol is an explicitly validated descriptor."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Added Unithiol, DMPS, and dimercaptopropane* forms. The updated evaluation remains warning-free and retains all known relevant records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Current lint and live evaluation show no syntax, phrase translation, or field issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No unnecessary filters or limits; the requested Entrez date bound is applied."
        }
      },
      "findings": [
        {
          "id": "R1-LEX-DMPS",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "therapy",
          "finding": "Sodium dimercaptopropane sulfonate (DMPS/Unithiol), described as a Wilson disease treatment in cutoff-eligible treatment literature, was absent from the pharmacologic therapy block.",
          "recommendation": "Add the verified Unithiol MeSH heading and common DMPS/sodium dimercaptopropane sulfonate free-text variants, then evaluate the updated strategy.",
          "status": "resolved",
          "response": "Added \"Unithiol\"[Mesh], Unithiol[tiab], DMPS[tiab], and dimercaptopropane*[tiab]. MeSH show lists DMPS and sodium 2,3-dimercaptopropane sulfonate as entry terms. Live evaluation is complete with no blockers or review-required issues, and no known records were lost."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 5,
      "review_sha256": "262094e208a3e2907f26c4f33463fccc7e15d0b732b834a647106f2a110243ad",
      "note": "same-context closing critic; verifies the only earlier finding was addressed",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The disease and pharmacologic treatment blocks remain aligned with the assumed PICO scope; comparators and outcomes remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "The strategy uses OR within blocks and AND between blocks without NOT or proximity."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The live evaluation verifies the selected disease and therapy headings, including Unithiol. No MeSH validation issues remain."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The DMPS/Unithiol vocabulary recommendation is implemented in the current therapy block."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current evaluated strategy has no syntax, translation, or phrase warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No unsupported filters or limits; Entrez as-of bound is 2018-12-23."
        }
      },
      "findings": [
        {
          "id": "R1-LEX-DMPS",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "therapy",
          "finding": "Sodium dimercaptopropane sulfonate (DMPS/Unithiol), described as a Wilson disease treatment in cutoff-eligible treatment literature, was absent from the pharmacologic therapy block.",
          "recommendation": "Add the verified Unithiol MeSH heading and common DMPS/sodium dimercaptopropane sulfonate free-text variants, then evaluate the updated strategy.",
          "status": "resolved",
          "response": "Resolved in round 2: added \"Unithiol\"[Mesh], Unithiol[tiab], DMPS[tiab], and dimercaptopropane*[tiab]; complete evaluation retained all known records and has no validation issues."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

