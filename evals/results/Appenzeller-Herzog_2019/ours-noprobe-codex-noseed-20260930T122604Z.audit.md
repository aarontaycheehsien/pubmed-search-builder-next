# PubMed search strategy: audit

Generated 2026-09-30T12:55:53+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Comparative effectiveness of common therapies for Wilson disease
- Framework: PICO
- Scope confirmed by user: no (Proceeding without clarification at the user's request. Assumptions: broad all-age Wilson disease population; common pharmacologic therapies include D-penicillamine, trientine, zinc salts, and tetrathiomolybdate; comparative design/comparator and heterogeneous effectiveness/safety outcomes are screening criteria rather than required search blocks. No language, date, or study-design limits. No known relevant records supplied. Standard-depth discovery will be attempted. PSB_AS_OF is set to 2018-12-23 for every command; no publication-date limit is imposed.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Wilson disease | search | The target disease defines the population and should be named or indexed in eligible clinical studies. |
| Common pharmacologic therapies for Wilson disease | search | Therapy is the intervention of interest; include named members such as penicillamine, trientine, zinc, and tetrathiomolybdate. |
| Comparative design and comparator | screen | Direct comparisons, usual care, and indirect comparisons are not reliably named in searchable fields; assess at screening. |
| Clinical effectiveness and harms | screen | Outcomes are heterogeneous and may be reported only in abstracts or full text; do not require an outcome block. |
| People of any age with Wilson disease | screen | No age restriction was supplied; age terms are inconsistently indexed and are assessed at screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-30T12:54:56+00:00
- Records added to PubMed up to: 2018-12-23
- Total records: 1,958
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Hepatolenticular Degeneration"[Mesh]` | 5,697 | none |
| 2 | `"Wilson disease"[tiab]` | 5,545 | none |
| 3 | `"Wilson's disease"[tiab]` | 4,158 | none |
| 4 | `"hepatolenticular degeneration"[tiab]` | 946 | none |
| 5 | `"progressive lenticular degeneration"[tiab]` | 10 | none |
| 6 | `"copper storage disease"[tiab]` | 25 | none |
| 7 | `hepatolenticular[tiab]` | 975 | none |
| 8 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7` | 7,256 | none |
| 9 | `"Penicillamine"[Mesh]` | 7,878 | none |
| 10 | `"Trientine"[Mesh]` | 380 | none |
| 11 | `"Zinc Acetate"[Mesh]` | 246 | none |
| 12 | `"Zinc Sulfate"[Mesh]` | 1,802 | none |
| 13 | `"Zinc"[Mesh]` | 58,485 | none |
| 14 | `"Chelation Therapy"[Mesh]` | 1,413 | none |
| 15 | `tetrathiomolybdate[nm]` | 293 | none |
| 16 | `penicillamine[tiab]` | 6,853 | none |
| 17 | `"D-penicillamine"[tiab]` | 3,268 | none |
| 18 | `"D penicillamine"[tiab]` | 3,268 | none |
| 19 | `DPA[tiab]` | 3,338 | none |
| 20 | `trientine[tiab]` | 219 | none |
| 21 | `triethylenetetramine[tiab]` | 360 | none |
| 22 | `TETA[tiab]` | 1,290 | none |
| 23 | `zinc[tiab]` | 108,490 | none |
| 24 | `"zinc acetate"[tiab]` | 817 | none |
| 25 | `"zinc sulfate"[tiab]` | 1,531 | none |
| 26 | `"zinc sulphate"[tiab]` | 857 | none |
| 27 | `tetrathiomolybdate[tiab]` | 351 | none |
| 28 | `"ammonium tetrathiomolybdate"[tiab]` | 84 | none |
| 29 | `"bis-choline tetrathiomolybdate"[tiab]` | 6 | none |
| 30 | `WTX101[tiab]` | 3 | none |
| 31 | `DMPS[tiab]` | 745 | none |
| 32 | `dimercaptopropanesulfonate[tiab]` | 27 | none |
| 33 | `"anti-copper"[tiab]` | 29 | none |
| 34 | `anticopper[tiab]` | 79 | none |
| 35 | `chelat*[tiab]` | 62,346 | none |
| 36 | `#9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35` | 199,011 | none |
| 37 | `#8 AND #36` | 1,958 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Hepatolenticular Degeneration"[Mesh] OR "Wilson disease"[tiab] OR "Wilson's disease"[tiab] OR "hepatolenticular degeneration"[tiab] OR "progressive lenticular degeneration"[tiab] OR "copper storage disease"[tiab] OR hepatolenticular[tiab]) AND ("Penicillamine"[Mesh] OR "Trientine"[Mesh] OR "Zinc Acetate"[Mesh] OR "Zinc Sulfate"[Mesh] OR "Zinc"[Mesh] OR "Chelation Therapy"[Mesh] OR tetrathiomolybdate[nm] OR penicillamine[tiab] OR "D-penicillamine"[tiab] OR "D penicillamine"[tiab] OR DPA[tiab] OR trientine[tiab] OR triethylenetetramine[tiab] OR TETA[tiab] OR zinc[tiab] OR "zinc acetate"[tiab] OR "zinc sulfate"[tiab] OR "zinc sulphate"[tiab] OR tetrathiomolybdate[tiab] OR "ammonium tetrathiomolybdate"[tiab] OR "bis-choline tetrathiomolybdate"[tiab] OR WTX101[tiab] OR DMPS[tiab] OR dimercaptopropanesulfonate[tiab] OR "anti-copper"[tiab] OR anticopper[tiab] OR chelat*[tiab])) AND ("1800/01/01"[edat] : "2018/12/23"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 17 | 17 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| wilson_disease | 199,011 | 0 |
| therapies | 7,256 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,954 | initial | none | Initial Wilson disease and common therapy blocks; terms from clinical comparative and longitudinal treatment records screened from date-bounded PubMed pilots and similar-record discovery. |
| 2 | 1,958 | therapies: +2 / -2 | none | Removed ambiguous Chelating Agents heading after NCBI authority validation returned duplicate canonical matches; dropped ALXN1840 after its bounded line returned zero hits with 'No items found'; added Zinc MeSH and DPA text from development-set treatment vocabularies. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 1 findings; R1-1 must-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 284 NCBI requests logged (65 from cache); strategy sha256 0e4447d72cf3._

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
      "checked_at": "2026-09-30T12:54:56+00:00",
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
      "checked_at": "2026-09-30T12:54:56+00:00",
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
      "checked_at": "2026-09-30T12:54:56+00:00",
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
      "requested": "Zinc Acetate",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T12:54:56+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D019345",
          "name": "Zinc Acetate",
          "type": "descriptor",
          "scope_note": "A salt produced by the reaction of zinc oxide with acetic acid and used as an astringent, styptic, and emetic.",
          "tree_numbers": [
            "D02.241.081.018.165.750"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D019345",
      "preferred_label": "Zinc Acetate",
      "type": "descriptor",
      "location": "vocabulary:10",
      "term": {
        "text": "\"Zinc Acetate\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc Sulfate",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T12:54:56+00:00",
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
      "location": "vocabulary:11",
      "term": {
        "text": "\"Zinc Sulfate\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T12:54:56+00:00",
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
      "requested": "Chelation Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-30T12:54:56+00:00",
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
      "location": "vocabulary:13",
      "term": {
        "text": "\"Chelation Therapy\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "tetrathiomolybdate",
      "expected_type": "supplementary",
      "checked_at": "2026-09-30T12:54:56+00:00",
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
      "location": "vocabulary:14",
      "term": {
        "text": "tetrathiomolybdate",
        "tag": "nm",
        "field": "nm"
      }
    }
  ],
  "translation": "(\"Hepatolenticular Degeneration\"[MeSH Terms] OR \"Wilson disease\"[Title/Abstract] OR \"Wilson's disease\"[Title/Abstract] OR \"Hepatolenticular Degeneration\"[Title/Abstract] OR \"progressive lenticular degeneration\"[Title/Abstract] OR \"copper storage disease\"[Title/Abstract] OR \"hepatolenticular\"[Title/Abstract]) AND (\"Penicillamine\"[MeSH Terms] OR \"Trientine\"[MeSH Terms] OR \"Zinc Acetate\"[MeSH Terms] OR \"Zinc Sulfate\"[MeSH Terms] OR \"Zinc\"[MeSH Terms] OR \"Chelation Therapy\"[MeSH Terms] OR \"tetrathiomolybdate\"[Supplementary Concept] OR \"Penicillamine\"[Title/Abstract] OR \"d penicillamine\"[Title/Abstract] OR \"d penicillamine\"[Title/Abstract] OR \"DPA\"[Title/Abstract] OR \"Trientine\"[Title/Abstract] OR \"triethylenetetramine\"[Title/Abstract] OR \"TETA\"[Title/Abstract] OR \"Zinc\"[Title/Abstract] OR \"Zinc Acetate\"[Title/Abstract] OR \"Zinc Sulfate\"[Title/Abstract] OR \"zinc sulphate\"[Title/Abstract] OR \"tetrathiomolybdate\"[Title/Abstract] OR \"ammonium tetrathiomolybdate\"[Title/Abstract] OR \"bis-choline tetrathiomolybdate\"[Title/Abstract] OR \"WTX101\"[Title/Abstract] OR \"DMPS\"[Title/Abstract] OR \"dimercaptopropanesulfonate\"[Title/Abstract] OR \"anti-copper\"[Title/Abstract] OR \"anticopper\"[Title/Abstract] OR \"chelat*\"[Title/Abstract]) AND 1800/01/01:2018/12/23[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "833bcb72d5b3db091900c9cc9c15c099bab352a4cf52430fc8d654fe09d05af4",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The named therapy members are represented by their own terms, and the packet reports no translation warnings or errors."
        },
        "operators": {
          "verdict": "pass",
          "note": "The disease terms and therapy terms are OR-combined, then the two concept blocks are AND-combined."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The included headings are verified in the packet; no heading translation errors are reported."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes disease names and named therapy terms, including tetrathiomolybdate. No process-direction term triggers the packet's fragility check."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query parses without syntax errors. No proximity operators are used."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The active Entrez cutoff is required by the user's harness and is not a publication-date eligibility limit."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The strategy applies an EDAT cutoff of 2018-12-23 throughout, despite the protocol stating that no date limits are imposed. This excludes records entered into PubMed after the cutoff, including older studies indexed later.",
          "recommendation": "Remove the EDAT restriction from the search and rerun the complete evaluation without a date limit. Keep the as-of date for the pilot separate from the final query.",
          "status": "rejected",
          "response": "The user's harness requires PSB_AS_OF=2018-12-23 for every command to simulate the PubMed corpus available by Entrez entry date and explicitly prohibits a publication-date [dp] cutoff. The [edat] restriction in the tested/exported query is therefore required to reproduce that as-of corpus; it does not restrict eligibility by publication date. Removing it would violate the task and make the final strategy counts inconsistent with the requested historical run."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

