# PubMed search strategy: audit

Generated 2026-10-02T13:32:17+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Comparative effectiveness of common therapies for Wilson disease
- Framework: PICO
- Scope confirmed by user: no (User asked to proceed without questions; scope assumptions were recorded and not confirmed. Assumed intervention-effectiveness PICO; searched Wilson disease and common therapies; screened comparator, outcome, and study design. No known relevant articles were supplied. Standard depth. PubMed records bounded by Entrez date 2018-12-23; no publication-date limit. Two records found and abstract-screened into the development set; no held-out validation set.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Wilson disease | search | The target population/condition is required for every eligible comparative therapy study and has established disease names and indexing. |
| Common Wilson disease therapies | search | The intervention is central to the comparative effectiveness question; treatment-related terms and named standard anti-copper therapies identify the intervention without requiring a comparator or outcome. |
| Comparators | screen | Comparator labels are inconsistently reported and are not needed to define the topic. |
| Clinical effectiveness and harms | screen | Outcomes are handled at screening because requiring outcome terms can miss comparative studies. |
| Comparative clinical study design | screen | No ad hoc study design filter; comparative design is assessed during screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T13:31:18+00:00
- Records added to PubMed up to: 2018-12-23
- Total records: 3,329
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Hepatolenticular Degeneration"[Mesh]` | 5,697 | none |
| 2 | `"Wilson disease"[tiab]` | 5,545 | none |
| 3 | `"Wilson's disease"[tiab]` | 4,158 | none |
| 4 | `hepatolenticular[tiab]` | 975 | none |
| 5 | `Kinnier-Wilson[tiab]` | 38 | none |
| 6 | `pseudoscleros*[tiab]` | 60 | none |
| 7 | `"copper storage disease"[tiab]` | 25 | none |
| 8 | `ATP7B[tiab]` | 1,016 | none |
| 9 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8` | 7,564 | none |
| 10 | `"Penicillamine"[Mesh]` | 7,878 | none |
| 11 | `"Trientine"[Mesh]` | 380 | none |
| 12 | `"Chelation Therapy"[Mesh]` | 1,413 | none |
| 13 | `"Zinc"[Mesh]` | 58,485 | none |
| 14 | `"Zinc Compounds"[Mesh]` | 12,484 | none |
| 15 | `"Zinc Sulfate"[Mesh]` | 1,802 | none |
| 16 | `"Tetrathiomolybdate"[nm]` | 293 | none |
| 17 | `"Liver Transplantation"[Mesh]` | 54,773 | none |
| 18 | `penicillamine[tiab]` | 6,853 | none |
| 19 | `"D-penicillamine"[tiab]` | 3,268 | none |
| 20 | `trientine[tiab]` | 219 | none |
| 21 | `triethylenetetramine[tiab]` | 360 | none |
| 22 | `zinc[tiab]` | 108,490 | none |
| 23 | `"zinc sulfate"[tiab]` | 1,531 | none |
| 24 | `"zinc acetate"[tiab]` | 817 | none |
| 25 | `"zinc salt"[tiab]` | 178 | none |
| 26 | `chelat*[tiab]` | 62,346 | none |
| 27 | `"anti-copper"[tiab]` | 29 | none |
| 28 | `anticopper[tiab]` | 79 | none |
| 29 | `"copper chelation"[tiab]` | 197 | none |
| 30 | `tetrathiomolybdate[tiab]` | 351 | none |
| 31 | `"ammonium tetrathiomolybdate"[tiab]` | 84 | none |
| 32 | `"ATN-224"[tiab]` | 19 | none |
| 33 | `WTX101[tiab]` | 3 | none |
| 34 | `transplant*[tiab]` | 443,114 | none |
| 35 | `treatment[tiab]` | 3,933,276 | none |
| 36 | `therap*[tiab]` | 2,661,898 | none |
| 37 | `#10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36` | 5,898,079 | none |
| 38 | `#9 AND #37` | 3,329 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Hepatolenticular Degeneration"[Mesh] OR "Wilson disease"[tiab] OR "Wilson's disease"[tiab] OR hepatolenticular[tiab] OR Kinnier-Wilson[tiab] OR pseudoscleros*[tiab] OR "copper storage disease"[tiab] OR ATP7B[tiab]) AND ("Penicillamine"[Mesh] OR "Trientine"[Mesh] OR "Chelation Therapy"[Mesh] OR "Zinc"[Mesh] OR "Zinc Compounds"[Mesh] OR "Zinc Sulfate"[Mesh] OR "Tetrathiomolybdate"[nm] OR "Liver Transplantation"[Mesh] OR penicillamine[tiab] OR "D-penicillamine"[tiab] OR trientine[tiab] OR triethylenetetramine[tiab] OR zinc[tiab] OR "zinc sulfate"[tiab] OR "zinc acetate"[tiab] OR "zinc salt"[tiab] OR chelat*[tiab] OR "anti-copper"[tiab] OR anticopper[tiab] OR "copper chelation"[tiab] OR tetrathiomolybdate[tiab] OR "ammonium tetrathiomolybdate"[tiab] OR "ATN-224"[tiab] OR WTX101[tiab] OR transplant*[tiab] OR treatment[tiab] OR therap*[tiab])) AND ("1800/01/01"[edat] : "2018/12/23"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 2 | 2 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| wilson_disease | 5,898,079 | 0 |
| therapy | 7,564 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 4,115 | initial | none | Initial recall-first PICO strategy: Wilson disease and common therapies searched; comparator, outcome, and design screened. Added MeSH headings and therapy terms from MeSH inspection and two screened pilot records. |
| 2 | 4,100 | therapy: +0 / -1 | none | Removed the ambiguous canonical MeSH heading Chelating Agents after live authority validation flagged duplicate records; other drug-specific headings and free-text chelat* remain. No known-record loss. |
| 3 | 3,329 | wilson_disease: +2 / -1 | none | Replaced broad Wilson* disease-block term with explicit Wilson disease and Wilson's disease title/abstract phrases to avoid unrelated Wilson-named records while retaining disease MeSH, other aliases, and ATP7B wording. Two development records remain retrieved. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 1 findings; R1-01 should-fix accepted-risk
- Round 2 on version 3: 1 findings; R1-01 should-fix accepted-risk
- Round 3 on version 3: 1 findings; R1-01 should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 478 NCBI requests logged (201 from cache); strategy sha256 aa7ede71c2c2._

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
      "checked_at": "2026-10-02T13:31:18+00:00",
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
      "requested": "Penicillamine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:31:18+00:00",
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
      "location": "vocabulary:9",
      "term": {
        "text": "\"Penicillamine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Trientine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:31:18+00:00",
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
      "location": "vocabulary:10",
      "term": {
        "text": "\"Trientine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Chelation Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:31:18+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D015913",
          "name": "Chelation Therapy",
          "type": "descriptor",
          "scope_note": "Therapy of heavy metal poisoning using agents which sequester the metal from organs or tissues and bind it firmly within the ring structure of a new compound which can be eliminated from the body.",
          "tree_numbers": [
            "E02.319.155"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D015913",
      "preferred_label": "Chelation Therapy",
      "type": "descriptor",
      "location": "vocabulary:11",
      "term": {
        "text": "\"Chelation Therapy\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:31:18+00:00",
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
      "location": "vocabulary:12",
      "term": {
        "text": "\"Zinc\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc Compounds",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:31:18+00:00",
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
      "location": "vocabulary:13",
      "term": {
        "text": "\"Zinc Compounds\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc Sulfate",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:31:18+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D019287",
          "name": "Zinc Sulfate",
          "type": "descriptor",
          "scope_note": "A compound given in the treatment of conditions associated with zinc deficiency such as acrodermatitis enteropathica. Externally, zinc sulfate is used as an astringent in lotions and eye drops. (Reynolds JEF(Ed): Martindale: The Extra Pharmacopoeia (electronic version). Micromedex, Inc, Englewood, CO, 1995)",
          "tree_numbers": [
            "D01.875.800.800.850.950",
            "D01.975.987"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D019287",
      "preferred_label": "Zinc Sulfate",
      "type": "descriptor",
      "location": "vocabulary:14",
      "term": {
        "text": "\"Zinc Sulfate\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Tetrathiomolybdate",
      "expected_type": "supplementary",
      "checked_at": "2026-10-02T13:31:18+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "C020809",
          "name": "tetrathiomolybdate",
          "type": "supplementary",
          "scope_note": "RN given refers to (MoS4)-2; chelates copper; inhibits CopB copper ATPase and cytokine proteins important for angiogenesis; structure",
          "tree_numbers": [
            "@14520"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "C020809",
      "preferred_label": "tetrathiomolybdate",
      "type": "supplementary",
      "location": "vocabulary:15",
      "term": {
        "text": "\"Tetrathiomolybdate\"",
        "tag": "nm",
        "field": "nm"
      }
    },
    {
      "requested": "Liver Transplantation",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:31:18+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D016031",
          "name": "Liver Transplantation",
          "type": "descriptor",
          "scope_note": "The transference of a part of or an entire liver from one human or animal to another.",
          "tree_numbers": [
            "E02.095.147.725.490",
            "E04.210.650",
            "E04.936.450.490",
            "E04.936.580.490"
          ],
          "entry_terms": 10,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D016031",
      "preferred_label": "Liver Transplantation",
      "type": "descriptor",
      "location": "vocabulary:16",
      "term": {
        "text": "\"Liver Transplantation\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Hepatolenticular Degeneration\"[MeSH Terms] OR \"Wilson disease\"[Title/Abstract] OR \"Wilson's disease\"[Title/Abstract] OR \"hepatolenticular\"[Title/Abstract] OR \"Kinnier-Wilson\"[Title/Abstract] OR \"pseudoscleros*\"[Title/Abstract] OR \"copper storage disease\"[Title/Abstract] OR \"ATP7B\"[Title/Abstract]) AND (\"Penicillamine\"[MeSH Terms] OR \"Trientine\"[MeSH Terms] OR \"Chelation Therapy\"[MeSH Terms] OR \"Zinc\"[MeSH Terms] OR \"Zinc Compounds\"[MeSH Terms] OR \"Zinc Sulfate\"[MeSH Terms] OR \"Tetrathiomolybdate\"[Supplementary Concept] OR \"Liver Transplantation\"[MeSH Terms] OR \"Penicillamine\"[Title/Abstract] OR \"D-penicillamine\"[Title/Abstract] OR \"Trientine\"[Title/Abstract] OR \"triethylenetetramine\"[Title/Abstract] OR \"Zinc\"[Title/Abstract] OR \"Zinc Sulfate\"[Title/Abstract] OR \"zinc acetate\"[Title/Abstract] OR \"zinc salt\"[Title/Abstract] OR \"chelat*\"[Title/Abstract] OR \"anti-copper\"[Title/Abstract] OR \"anticopper\"[Title/Abstract] OR \"copper chelation\"[Title/Abstract] OR \"Tetrathiomolybdate\"[Title/Abstract] OR \"ammonium tetrathiomolybdate\"[Title/Abstract] OR \"ATN-224\"[Title/Abstract] OR \"WTX101\"[Title/Abstract] OR \"transplant*\"[Title/Abstract] OR \"treatment\"[Title/Abstract] OR \"therap*\"[Title/Abstract]) AND 1800/01/01:2018/12/23[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "8fca8eeb36a634c11c62fd0c97a0615c515da33d2f3b5d4827ef3ccad5cb81a4",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two searched concepts match the protocol. Comparators, outcomes, and study design are appropriately left for screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within each block, and the Wilson disease and therapy blocks are ANDed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verified MeSH or supplementary concept headings for the controlled vocabulary terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The disease block includes established disease names and ATP7B; the therapy block includes named therapies and broader treatment terms. No translation warning or uncovered named process term is reported."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query ran without reported syntax or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No study-design or outcome filter is applied, consistent with the protocol. The Entrez date boundary is disclosed as the 2018-12-23 as-of date."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The reported 100% retrieval is based on only two relevant records, both assigned to the development set; the packet reports no held-out validation set. This result does not independently establish the search's recall.",
          "recommendation": "Report the two-record result as development-set coverage only. If validation is needed, obtain an independent held-out set of relevant records and evaluate the final strategy against it.",
          "status": "accepted-risk",
          "response": "Accepted because no user-supplied known records or held-out set were available and no independent validation set was found in the standard-depth pilot work. The audit will report 100% only as relative recall on the two-record development set, explicitly state that recall was not independently estimated, and identify the strategy as empirically unvalidated pending information-specialist PRESS review."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "8fca8eeb36a634c11c62fd0c97a0615c515da33d2f3b5d4827ef3ccad5cb81a4",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched Wilson disease and therapy concepts match the protocol; comparators, outcomes, and study design are appropriately handled at screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are ORed within each concept block, and the disease and therapy blocks are ANDed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verified controlled vocabulary terms for the headings used."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The disease block includes disease names and ATP7B; the therapy block includes named therapies and broad treatment terms. No translation warnings or uncovered named process terms are reported."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query ran without reported syntax or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No study-design or outcome filter is applied. The Entrez date boundary is disclosed as the 2018-12-23 as-of date."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The reported 100% retrieval is based on only two relevant records, both assigned to the development set; the packet reports no held-out validation set. This result does not independently establish the search's recall.",
          "recommendation": "Report the two-record result as development-set coverage only. If validation is needed, obtain an independent held-out set of relevant records and evaluate the final strategy against it.",
          "status": "accepted-risk",
          "response": "Retain the prior disposition. The audit will report 100% only as relative recall on the two-record development set, state that recall was not independently estimated, and identify the strategy as empirically unvalidated pending information-specialist PRESS review."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "8fca8eeb36a634c11c62fd0c97a0615c515da33d2f3b5d4827ef3ccad5cb81a4",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched Wilson disease and therapy concepts match the protocol; comparators, outcomes, and study design are appropriately left for screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are ORed within each concept block, and the disease and therapy blocks are ANDed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verified controlled vocabulary headings for the terms used."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The disease block includes disease names and ATP7B; the therapy block includes named therapies and broader treatment terms. The two-record coverage remains development-set evidence only, as recorded in R1-01."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query ran without reported syntax or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No study-design or outcome filter is applied. The Entrez date boundary is disclosed as 2018-12-23."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The reported 100% retrieval is based on only two relevant records, both assigned to the development set; the packet reports no held-out validation set. This result does not independently establish the search's recall.",
          "recommendation": "Report the two-record result as development-set coverage only. If validation is needed, obtain an independent held-out set of relevant records and evaluate the final strategy against it.",
          "status": "accepted-risk",
          "response": "Retain the prior accepted-risk disposition. The evidence identifies both records as development-set records and reports no held-out validation set; therefore, 100% is relative recall on those two records only, and independent recall has not been estimated."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

