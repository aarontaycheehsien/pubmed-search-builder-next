# PubMed search strategy: audit

Generated 2026-09-28T04:15:13+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Source of mesenchymal stem cells for the management of osteoarthritis of the knee
- Framework: PCC
- Scope confirmed by user: no (User asked to proceed without questions. Assumed a broad clinical evidence map/comparison of MSC tissue sources for knee OA, with humans as the target population; cell source and knee location are screening criteria to protect recall. Included source-defined MSC-containing preparations such as bone marrow aspirate concentrate and adipose stromal vascular fraction when identified in the study. No known relevant records supplied. Scope proceeded without confirmation at the user's request. PubMed availability is bounded by Entrez date 2022-05-10; no publication-date limit. User requested standard depth.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Osteoarthritis | search | The condition is central and is reliably named/indexed; knee-specific OA is screened to avoid losing records that omit joint location from searchable fields. |
| Mesenchymal stem/stromal cells | search | The intervention class is central and searchable; include broad nomenclature and source-defined cellular preparations because source labels vary. |
| Knee involvement | screen | Required population/joint criterion, but not required as a separate AND block because abstracts may omit location. |
| Cell/tissue source | screen | The review compares or maps sources; source terms are inconsistently stated and are best extracted during screening rather than required as a block. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T04:14:30+00:00
- Records added to PubMed up to: 2022-05-10
- Total records: 2,577
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Osteoarthritis"[Mesh]` | 73,454 | none |
| 2 | `"Osteoarthritis, Knee"[Mesh]` | 25,328 | none |
| 3 | `osteoarthrit*[tiab]` | 81,326 | none |
| 4 | `osteoarthrosis[tiab]` | 3,446 | none |
| 5 | `osteoarthroses[tiab]` | 24 | none |
| 6 | `arthrosis[tiab]` | 5,652 | none |
| 7 | `arthroses[tiab]` | 512 | none |
| 8 | `"degenerative arthritis"[tiab]` | 1,333 | none |
| 9 | `"degenerative joint disease"[tiab]` | 2,782 | none |
| 10 | `gonarthros*[tiab]` | 1,162 | none |
| 11 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10` | 111,455 | none |
| 12 | `"Mesenchymal Stem Cells"[Mesh]` | 47,452 | none |
| 13 | `"Mesenchymal Stem Cell Transplantation"[Mesh]` | 14,289 | none |
| 14 | `"Stromal Vascular Fraction"[Mesh]` | 83 | none |
| 15 | `mesenchymal[tiab] AND stem[tiab]` | 66,439 | none |
| 16 | `mesenchymal[tiab] AND stromal[tiab]` | 19,423 | none |
| 17 | `mesenchymal[tiab] AND progenitor[tiab]` | 7,312 | none |
| 18 | `multipotent[tiab] AND stromal[tiab]` | 2,474 | none |
| 19 | `"bone marrow"[tiab] AND stromal[tiab]` | 17,690 | none |
| 20 | `adipose[tiab] AND stem[tiab]` | 14,811 | none |
| 21 | `adipose[tiab] AND stromal[tiab]` | 5,827 | none |
| 22 | `"fat-derived"[tiab] AND stem[tiab]` | 87 | none |
| 23 | `"bone marrow"[tiab] AND stem[tiab]` | 53,884 | none |
| 24 | `"umbilical cord"[tiab] AND stem[tiab]` | 7,885 | none |
| 25 | `Wharton[tiab] AND jelly[tiab] AND cell*[tiab]` | 1,309 | none |
| 26 | `synovial[tiab] AND stem[tiab]` | 922 | none |
| 27 | `infrapatellar[tiab] AND stem[tiab]` | 152 | none |
| 28 | `peripheral blood[tiab] AND stem[tiab]` | 17,910 | none |
| 29 | `bone marrow[tiab] AND aspirate[tiab] AND concentrate[tiab]` | 376 | none |
| 30 | `BMAC[tiab]` | 277 | none |
| 31 | `stromal[tiab] AND vascular[tiab] AND fraction[tiab]` | 1,769 | none |
| 32 | `SVF[tiab]` | 1,332 | none |
| 33 | `MSC[tiab]` | 23,221 | none |
| 34 | `MSCs[tiab]` | 30,886 | none |
| 35 | `#12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34` | 150,255 | none |
| 36 | `#11 AND #35` | 2,577 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Osteoarthritis"[Mesh] OR "Osteoarthritis, Knee"[Mesh] OR osteoarthrit*[tiab] OR osteoarthrosis[tiab] OR osteoarthroses[tiab] OR arthrosis[tiab] OR arthroses[tiab] OR "degenerative arthritis"[tiab] OR "degenerative joint disease"[tiab] OR gonarthros*[tiab]) AND ("Mesenchymal Stem Cells"[Mesh] OR "Mesenchymal Stem Cell Transplantation"[Mesh] OR "Stromal Vascular Fraction"[Mesh] OR (mesenchymal[tiab] AND stem[tiab]) OR (mesenchymal[tiab] AND stromal[tiab]) OR (mesenchymal[tiab] AND progenitor[tiab]) OR (multipotent[tiab] AND stromal[tiab]) OR ("bone marrow"[tiab] AND stromal[tiab]) OR (adipose[tiab] AND stem[tiab]) OR (adipose[tiab] AND stromal[tiab]) OR ("fat-derived"[tiab] AND stem[tiab]) OR ("bone marrow"[tiab] AND stem[tiab]) OR ("umbilical cord"[tiab] AND stem[tiab]) OR (Wharton[tiab] AND jelly[tiab] AND cell*[tiab]) OR (synovial[tiab] AND stem[tiab]) OR (infrapatellar[tiab] AND stem[tiab]) OR (peripheral blood[tiab] AND stem[tiab]) OR (bone marrow[tiab] AND aspirate[tiab] AND concentrate[tiab]) OR BMAC[tiab] OR (stromal[tiab] AND vascular[tiab] AND fraction[tiab]) OR SVF[tiab] OR MSC[tiab] OR MSCs[tiab])) AND ("1800/01/01"[edat] : "2022/05/10"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 17 | 17 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| osteoarthritis | 150,255 | 0 |
| mesenchymal_stem_cells | 111,455 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial recall-first strategy: AND osteoarthritis and mesenchymal stem/stromal cells. Knee location and reported tissue source remain screening criteria; source terminology is inconsistently indexed. Terms include MeSH headings and synonyms from MeSH and screened clinical records. |
| 2 | 2,255 | osteoarthritis: +10 / -0; mesenchymal_stem_cells: +9 / -0 | none | Initial recall-first strategy: AND osteoarthritis and mesenchymal stem/stromal cells. Knee location and reported tissue source remain screening criteria; source terminology is inconsistently indexed. Terms include MeSH headings and synonyms from MeSH and screened clinical records. |
| 3 | 2,526 | mesenchymal_stem_cells: +9 / -0 | none | Expanded the MSC text block to include searchable tissue-origin plus stem/stromal combinations (adipose, marrow, cord/Wharton's jelly, synovium, infrapatellar fat pad, peripheral blood) because source-focused reports may omit the generic MSC label. Retained broad MeSH and general cell nomenclature. |
| 4 | 2,577 | mesenchymal_stem_cells: +4 / -0 | none | Clarified the no-confirmation scope assumption: include source-defined MSC-containing preparations (including BMAC and adipose SVF) when evaluated as cellular therapy. Added corresponding text terms so source-defined preparations are not missed when MSC wording is absent; knee and source remain screening criteria. |
| 5 | 2,577 | mesenchymal_stem_cells: +1 / -0 | none | Added the verified Stromal Vascular Fraction MeSH heading alongside its text terms so indexed adipose SVF records are retrieved even when title/abstract wording varies. No known development records were lost. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4 (Same-context critic: no separate fresh-context reviewer session was available. Read only the current critic packet and assessed the six PRESS domains against its query translations, counts, scope, and diagnostics.): 0 findings; 
- Round 2 on version 5 (Same-context critic: no separate fresh-context reviewer session was available. This round reviewed the updated packet after adding the verified Stromal Vascular Fraction heading.): 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 479 NCBI requests logged (240 from cache); strategy sha256 02a3ffa77f20._

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
      "requested": "Osteoarthritis",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T04:14:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D010003",
          "name": "Osteoarthritis",
          "type": "descriptor",
          "scope_note": "A progressive, degenerative joint disease, the most common form of arthritis, especially in older persons. The disease is thought to result not from the aging process but from biochemical changes and biomechanical stresses affecting articular cartilage. In the foreign literature it is often called osteoarthrosis deformans.",
          "tree_numbers": [
            "C05.550.114.606",
            "C05.799.613"
          ],
          "entry_terms": 10,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D010003",
      "preferred_label": "Osteoarthritis",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"Osteoarthritis\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Osteoarthritis, Knee",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T04:14:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D020370",
          "name": "Osteoarthritis, Knee",
          "type": "descriptor",
          "scope_note": "Noninflammatory degenerative disease of the knee joint consisting of three large categories: conditions that block normal synchronous movement, conditions that produce abnormal pathways of motion, and conditions that cause stress concentration resulting in changes to articular cartilage. (Crenshaw, Campbell's Operative Orthopaedics, 8th ed, p2019)",
          "tree_numbers": [
            "C05.550.114.606.500",
            "C05.799.613.500"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D020370",
      "preferred_label": "Osteoarthritis, Knee",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Osteoarthritis, Knee\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mesenchymal Stem Cells",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T04:14:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D059630",
          "name": "Mesenchymal Stem Cells",
          "type": "descriptor",
          "scope_note": "Mesenchymal stem cells, also referred to as multipotent stromal cells or mesenchymal stromal cells are multipotent, non-hematopoietic adult stem cells that are present in multiple tissues, including BONE MARROW; ADIPOSE TISSUE; and WHARTON JELLY. Mesenchymal stem cells can differentiate into mesodermal lineages, such as adipocytic, osteocytic and chondrocytic.",
          "tree_numbers": [
            "A11.329.830.500",
            "A11.872.590.500"
          ],
          "entry_terms": 42,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D059630",
      "preferred_label": "Mesenchymal Stem Cells",
      "type": "descriptor",
      "location": "vocabulary:11",
      "term": {
        "text": "\"Mesenchymal Stem Cells\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mesenchymal Stem Cell Transplantation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T04:14:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D045164",
          "name": "Mesenchymal Stem Cell Transplantation",
          "type": "descriptor",
          "scope_note": "Transfer of MESENCHYMAL STEM CELLS between individuals within the same species (TRANSPLANTATION, HOMOLOGOUS) or transfer within the same individual (TRANSPLANTATION, AUTOLOGOUS).",
          "tree_numbers": [
            "E02.095.147.500.500.625",
            "E04.936.225.687.625"
          ],
          "entry_terms": 2,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D045164",
      "preferred_label": "Mesenchymal Stem Cell Transplantation",
      "type": "descriptor",
      "location": "vocabulary:12",
      "term": {
        "text": "\"Mesenchymal Stem Cell Transplantation\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stromal Vascular Fraction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T04:14:30+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000090002",
          "name": "Stromal Vascular Fraction",
          "type": "descriptor",
          "scope_note": "A fraction of ADIPOSE TISSUE prepared to enrich in STEM CELLS with the capacity for multi-lineage differentiation. It is used in various applications for its tissue regeneration and immunomodulation activities.",
          "tree_numbers": [
            "A11.329.830.500.500",
            "A11.872.590.500.500"
          ],
          "entry_terms": 11,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000090002",
      "preferred_label": "Stromal Vascular Fraction",
      "type": "descriptor",
      "location": "vocabulary:13",
      "term": {
        "text": "\"Stromal Vascular Fraction\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Osteoarthritis\"[MeSH Terms] OR \"osteoarthritis, knee\"[MeSH Terms] OR \"osteoarthrit*\"[Title/Abstract] OR \"osteoarthrosis\"[Title/Abstract] OR \"osteoarthroses\"[Title/Abstract] OR \"arthrosis\"[Title/Abstract] OR \"arthroses\"[Title/Abstract] OR \"degenerative arthritis\"[Title/Abstract] OR \"degenerative joint disease\"[Title/Abstract] OR \"gonarthros*\"[Title/Abstract]) AND (\"Mesenchymal Stem Cells\"[MeSH Terms] OR \"Mesenchymal Stem Cell Transplantation\"[MeSH Terms] OR \"Stromal Vascular Fraction\"[MeSH Terms] OR (\"mesenchymal\"[Title/Abstract] AND \"stem\"[Title/Abstract]) OR (\"mesenchymal\"[Title/Abstract] AND \"stromal\"[Title/Abstract]) OR (\"mesenchymal\"[Title/Abstract] AND \"progenitor\"[Title/Abstract]) OR (\"multipotent\"[Title/Abstract] AND \"stromal\"[Title/Abstract]) OR (\"bone marrow\"[Title/Abstract] AND \"stromal\"[Title/Abstract]) OR (\"adipose\"[Title/Abstract] AND \"stem\"[Title/Abstract]) OR (\"adipose\"[Title/Abstract] AND \"stromal\"[Title/Abstract]) OR (\"fat-derived\"[Title/Abstract] AND \"stem\"[Title/Abstract]) OR (\"bone marrow\"[Title/Abstract] AND \"stem\"[Title/Abstract]) OR (\"umbilical cord\"[Title/Abstract] AND \"stem\"[Title/Abstract]) OR (\"Wharton\"[Title/Abstract] AND \"jelly\"[Title/Abstract] AND \"cell*\"[Title/Abstract]) OR (\"synovial\"[Title/Abstract] AND \"stem\"[Title/Abstract]) OR (\"infrapatellar\"[Title/Abstract] AND \"stem\"[Title/Abstract]) OR (\"peripheral blood\"[Title/Abstract] AND \"stem\"[Title/Abstract]) OR (\"bone marrow\"[Title/Abstract] AND \"aspirate\"[Title/Abstract] AND \"concentrate\"[Title/Abstract]) OR \"BMAC\"[Title/Abstract] OR (\"stromal\"[Title/Abstract] AND \"vascular\"[Title/Abstract] AND \"fraction\"[Title/Abstract]) OR \"SVF\"[Title/Abstract] OR \"MSC\"[Title/Abstract] OR \"MSCs\"[Title/Abstract]) AND 1800/01/01:2022/05/10[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "9e369f8236a14749087122515b33735a44c22bed6ba64dcbf8b49c18740e8b21",
      "note": "Same-context critic: no separate fresh-context reviewer session was available. Read only the current critic packet and assessed the six PRESS domains against its query translations, counts, scope, and diagnostics.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The two required blocks represent osteoarthritis and MSC/cell-source therapy. Knee location and source comparisons are screened to protect recall; source-defined BMAC/SVF preparations are explicitly included under the documented assumption."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within each block and the condition and cell-therapy concepts are ANDed. No NOT or proximity clauses are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Verified exploded Osteoarthritis and Osteoarthritis, Knee headings are paired with verified Mesenchymal Stem Cells and Mesenchymal Stem Cell Transplantation headings. No unsupported heading or restrictive major-topic tag is used."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text words cover stem, stromal, progenitor, multipotent, source-specific tissue labels, and cell-preparation names. MSC, BMAC, and SVF acronyms and the peripheral-blood stem-cell expression may add noise; their use is documented for a recall-first source review."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All terms are explicitly tagged, Boolean grouping is clear, wildcard stems meet the minimum length, and PubMed translations show no technical or phrase-index warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, publication-date, human, or study-design filter is applied. The Entrez-date bound is 2022-05-10 and is not a publication-date restriction."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "8cfd5d11f72c1da7a28f82d52736f83ac37d5e3c8690e945875c19ce84779409",
      "note": "Same-context critic: no separate fresh-context reviewer session was available. This round reviewed the updated packet after adding the verified Stromal Vascular Fraction heading.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The question maps to the osteoarthritis and MSC/source-defined cell-preparation blocks. Knee and source comparisons remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are ORed within blocks; blocks are ANDed. No NOT or proximity clauses are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The verified Osteoarthritis, Osteoarthritis, Knee, Mesenchymal Stem Cells, Mesenchymal Stem Cell Transplantation, and Stromal Vascular Fraction headings are appropriate and exploded."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Generic cell names and tissue-origin expressions cover major MSC sources and source-defined preparations. MSC, BMAC, SVF, and peripheral-blood stem wording may add noise, retained to favor recall and documented for screening."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Field tags and grouping are explicit; no syntax, translation, wildcard, or phrase warnings are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, publication-date, human, or design filters are used. The 2022-05-10 cutoff is PubMed Entrez date, not publication date."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```

