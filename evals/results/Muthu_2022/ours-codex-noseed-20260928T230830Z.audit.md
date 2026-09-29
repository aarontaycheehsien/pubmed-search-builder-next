# PubMed search strategy: audit

Generated 2026-09-28T23:32:20+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In patients with rotator cuff tears, is cellular therapy (e.g. mesenchymal stem cells, bone marrow aspirate, platelet-rich plasma) beneficial compared with controls for healing and clinical outcomes?
- Framework: PICO
- Scope confirmed by user: yes (User requested no questions during this run; scope and defaults are recorded as assumptions. PubMed records are bounded by Entrez date 2020-05-15 via PSB_AS_OF for every command. No publication-date restriction. No known relevant records supplied; standard-depth discovery will be attempted, but recall may remain unestimated.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Rotator cuff tear or repair | search | Defines the target condition/procedure and is named in titles, abstracts and MeSH. |
| Cellular and platelet-rich biologic augmentation (including MSCs, bone marrow aspirate concentrate, PRP, adipose- or tendon-derived cells) | search | Defines the intervention, but relevant studies may name only a particular product or cell source. |
| Human comparative clinical studies reporting healing, pain or function | screen | Comparative design, human population and outcomes are eligibility criteria best assessed at screening; no unvalidated design or outcome filter is imposed. |
| Control or standard repair without cellular augmentation | screen | Comparator descriptions are inconsistently reported in searchable fields. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T23:31:22+00:00
- Records added to PubMed up to: 2020-05-15
- Total records: 1,858
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Rotator Cuff Injuries"[Mesh]` | 6,021 | none |
| 2 | `"Rotator Cuff"[Mesh]` | 6,661 | none |
| 3 | `"Tendon Injuries"[Mesh]` | 25,376 | none |
| 4 | `rotator cuff[tiab]` | 11,564 | none |
| 5 | `"rotator cuff tear"[tiab]` | 2,632 | none |
| 6 | `"rotator cuff repair"[tiab]` | 2,813 | none |
| 7 | `"rotator cuff rupture"[tiab]` | 132 | none |
| 8 | `"cuff tear"[tiab]` | 2,988 | none |
| 9 | `"cuff repair"[tiab]` | 2,913 | none |
| 10 | `supraspinatus[tiab]` | 3,580 | none |
| 11 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10` | 32,505 | none |
| 12 | `"Platelet-Rich Plasma"[Mesh]` | 4,666 | none |
| 13 | `"Mesenchymal Stem Cells"[Mesh]` | 39,771 | none |
| 14 | `"Stem Cell Transplantation"[Mesh]` | 85,537 | none |
| 15 | `"Cell- and Tissue-Based Therapy"[Mesh]` | 288,735 | none |
| 16 | `"Bone Marrow Cells"[Mesh]` | 185,831 | none |
| 17 | `"platelet rich plasma"[tiab]` | 9,974 | none |
| 18 | `PRP[tiab]` | 15,823 | none |
| 19 | `MSC[tiab]` | 18,591 | none |
| 20 | `MSCs[tiab]` | 24,583 | none |
| 21 | `PRFM[tiab]` | 48 | none |
| 22 | `ACP[tiab]` | 9,234 | none |
| 23 | `"platelet-rich fibrin"[tiab]` | 1,215 | none |
| 24 | `"platelet rich fibrin matrix"[tiab]` | 59 | none |
| 25 | `"platelet leukocyte membrane"[tiab]` | 2 | none |
| 26 | `"platelet-leukocyte membrane"[tiab]` | 2 | none |
| 27 | `"plasma rich in growth factors"[tiab]` | 255 | none |
| 28 | `PRGF[tiab]` | 304 | none |
| 29 | `"autologous conditioned plasma"[tiab]` | 59 | none |
| 30 | `mesenchymal stem cell*[tiab]` | 43,533 | none |
| 31 | `mesenchymal progenitor cell*[tiab]` | 986 | none |
| 32 | `mesenchymal stromal cell*[tiab]` | 6,831 | none |
| 33 | `bone marrow stromal cell*[tiab]` | 6,230 | none |
| 34 | `bone marrow-derived cell*[tiab]` | 2,930 | none |
| 35 | `bone marrow aspirate[tiab]` | 2,375 | none |
| 36 | `"bone marrow aspirate concentrate"[tiab]` | 186 | none |
| 37 | `"bone marrow concentrate"[tiab]` | 146 | none |
| 38 | `"concentrated bone marrow aspirate"[tiab]` | 43 | none |
| 39 | `BMAC[tiab]` | 175 | none |
| 40 | `adipose-derived stem cell*[tiab]` | 4,602 | none |
| 41 | `adipose derived stem cell*[tiab]` | 4,602 | none |
| 42 | `adipose-derived cell*[tiab]` | 106 | none |
| 43 | `adipose derived cell*[tiab]` | 106 | none |
| 44 | `"adipose-derived regenerative cell"[tiab]` | 16 | none |
| 45 | `"stromal vascular fraction"[tiab]` | 1,216 | none |
| 46 | `tendon-derived stem cell*[tiab]` | 110 | none |
| 47 | `tendon stem cell*[tiab]` | 93 | none |
| 48 | `tenocyte*[tiab]` | 956 | none |
| 49 | `"tendon-derived cell"[tiab]` | 11 | none |
| 50 | `tendon-derived cell*[tiab]` | 67 | none |
| 51 | `tendon derived cell*[tiab]` | 67 | none |
| 52 | `"stem cell"[tiab]` | 158,551 | none |
| 53 | `"stem cells"[tiab]` | 173,395 | none |
| 54 | `"cellular therapy"[tiab]` | 2,805 | none |
| 55 | `"cell therapy"[tiab]` | 21,682 | none |
| 56 | `"biologic augmentation"[tiab]` | 76 | none |
| 57 | `"biological augmentation"[tiab]` | 121 | none |
| 58 | `#12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57` | 675,835 | none |
| 59 | `#11 AND #58` | 1,858 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Rotator Cuff Injuries"[Mesh] OR "Rotator Cuff"[Mesh] OR "Tendon Injuries"[Mesh] OR rotator cuff[tiab] OR "rotator cuff tear"[tiab] OR "rotator cuff repair"[tiab] OR "rotator cuff rupture"[tiab] OR "cuff tear"[tiab] OR "cuff repair"[tiab] OR supraspinatus[tiab]) AND ("Platelet-Rich Plasma"[Mesh] OR "Mesenchymal Stem Cells"[Mesh] OR "Stem Cell Transplantation"[Mesh] OR "Cell- and Tissue-Based Therapy"[Mesh] OR "Bone Marrow Cells"[Mesh] OR "platelet rich plasma"[tiab] OR PRP[tiab] OR MSC[tiab] OR MSCs[tiab] OR PRFM[tiab] OR ACP[tiab] OR "platelet-rich fibrin"[tiab] OR "platelet rich fibrin matrix"[tiab] OR "platelet leukocyte membrane"[tiab] OR "platelet-leukocyte membrane"[tiab] OR "plasma rich in growth factors"[tiab] OR PRGF[tiab] OR "autologous conditioned plasma"[tiab] OR mesenchymal stem cell*[tiab] OR mesenchymal progenitor cell*[tiab] OR mesenchymal stromal cell*[tiab] OR bone marrow stromal cell*[tiab] OR bone marrow-derived cell*[tiab] OR bone marrow aspirate[tiab] OR "bone marrow aspirate concentrate"[tiab] OR "bone marrow concentrate"[tiab] OR "concentrated bone marrow aspirate"[tiab] OR BMAC[tiab] OR adipose-derived stem cell*[tiab] OR adipose derived stem cell*[tiab] OR adipose-derived cell*[tiab] OR adipose derived cell*[tiab] OR "adipose-derived regenerative cell"[tiab] OR "stromal vascular fraction"[tiab] OR tendon-derived stem cell*[tiab] OR tendon stem cell*[tiab] OR tenocyte*[tiab] OR "tendon-derived cell"[tiab] OR tendon-derived cell*[tiab] OR tendon derived cell*[tiab] OR "stem cell"[tiab] OR "stem cells"[tiab] OR "cellular therapy"[tiab] OR "cell therapy"[tiab] OR "biologic augmentation"[tiab] OR "biological augmentation"[tiab])) AND ("1800/01/01"[edat] : "2020/05/15"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 17 | 17 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Cellular and platelet-rich biologic augmentation (including MSCs, bone marrow aspirate concentrate, PRP, adipose- or tendon-derived cells) | 1 | `(Rotator Cuff Injuries[Mesh] OR Rotator Cuff[Mesh] OR rotator cuff[tiab] OR supraspinatus[tiab]) AND (cell*[tiab] OR platelet*[tiab] OR marrow[tiab] OR adipose[tiab] OR plasma[tiab] OR biologic*[tiab] OR stromal[tiab] OR concentrate*[tiab] OR regenerate*[tiab])` | 760 | 0/30 |
| Cellular and platelet-rich biologic augmentation (including MSCs, bone marrow aspirate concentrate, PRP, adipose- or tendon-derived cells) | 2 | `(Rotator Cuff Injuries[Mesh] OR Rotator Cuff[Mesh] OR rotator cuff[tiab] OR supraspinatus[tiab]) AND (cell*[tiab] OR platelet*[tiab] OR marrow[tiab] OR adipose[tiab] OR plasma[tiab] OR biologic*[tiab] OR stromal[tiab] OR concentrate*[tiab] OR regenerate*[tiab])` | 696 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| rotator_cuff | 675,835 | 0 |
| cellular_therapy | 32,505 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,550 | initial | none | Initial two-block strategy: rotator cuff/repair AND the eligible cellular or platelet-rich biologics; comparison, design and outcomes remain for screening. |
| 2 | 1,839 | cellular_therapy: +9 / -10 | none | Revision: expanded intervention word forms and bone marrow aspirate terminology; replaced unsupported zero-hit tenocyte phrase with the single-word tenocyte stem. Removed duplicate hyphen variants after PubMed translated them identically. Completed and screened category probe 1 (30 records, none relevant). |
| 3 | 1,846 | cellular_therapy: +4 / -0 | none | Added the commonly used abbreviations PRFM (platelet-rich fibrin matrix) and ACP (autologous conditioned plasma), plus mesh-related member wording for mesenchymal progenitor and bone marrow-derived cells after review of the screened records and objective term ranks. |
| 4 | 1,852 | cellular_therapy: +4 / -1 | none | Addressed internal critic R1-01 by adding the criteria's bare adipose-derived and tendon-derived cell source expressions with plural-safe truncation. These are broad source terms and do not require the narrower stem or regenerative labels. |
| 5 | 1,852 | cellular_therapy: +1 / -0 | none | Retained the formerly screened exact phrase while adding broader source terms, so the already completed category probes remain valid on a term-expanded block. |
| 6 | 1,858 | cellular_therapy: +2 / -0 | none | Addressed critic R1-T1 by explicitly adding both MSC and MSCs as title/abstract terms; this meets the protocol's named acronym requirement and may also cover unindexed records. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5: 1 findings; R1-T1 must-fix open
- Round 2 on version 6: 1 findings; R1-T1 must-fix resolved
- Round 3 on version 6: 1 findings; R1-T1 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 945 NCBI requests logged (495 from cache); strategy sha256 7b647fa03750._

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
      "requested": "Rotator Cuff Injuries",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:31:22+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000070636",
          "name": "Rotator Cuff Injuries",
          "type": "descriptor",
          "scope_note": "Injuries to the ROTATOR CUFF of the shoulder joint.",
          "tree_numbers": [
            "C26.761.340",
            "C26.803.063",
            "C26.874.400"
          ],
          "entry_terms": 19,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000070636",
      "preferred_label": "Rotator Cuff Injuries",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"Rotator Cuff Injuries\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Rotator Cuff",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:31:22+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D017006",
          "name": "Rotator Cuff",
          "type": "descriptor",
          "scope_note": "The musculotendinous sheath formed by the supraspinatus, infraspinatus, subscapularis, and teres minor muscles. These help stabilize the HUMERAL HEAD in the GLENOID CAVITY of the SCAPULA and allow for rotation of the SHOULDER JOINT about its longitudinal axis.",
          "tree_numbers": [
            "A02.633.567.912",
            "A02.880.700"
          ],
          "entry_terms": 6,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D017006",
      "preferred_label": "Rotator Cuff",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Rotator Cuff\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Tendon Injuries",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:31:22+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D013708",
          "name": "Tendon Injuries",
          "type": "descriptor",
          "scope_note": "Injuries to the fibrous cords of connective tissue which attach muscles to bones or other structures.",
          "tree_numbers": [
            "C26.874"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D013708",
      "preferred_label": "Tendon Injuries",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "\"Tendon Injuries\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Platelet-Rich Plasma",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:31:22+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D053657",
          "name": "Platelet-Rich Plasma",
          "type": "descriptor",
          "scope_note": "A preparation consisting of PLATELETS concentrated in a limited volume of PLASMA. This is used in various surgical tissue regeneration procedures where the GROWTH FACTORS in the platelets enhance wound healing and regeneration.",
          "tree_numbers": [
            "A12.207.152.693.600",
            "A12.207.270.695.600",
            "A15.145.693.600"
          ],
          "entry_terms": 2,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D053657",
      "preferred_label": "Platelet-Rich Plasma",
      "type": "descriptor",
      "location": "vocabulary:11",
      "term": {
        "text": "\"Platelet-Rich Plasma\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mesenchymal Stem Cells",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:31:22+00:00",
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
      "location": "vocabulary:12",
      "term": {
        "text": "\"Mesenchymal Stem Cells\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stem Cell Transplantation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:31:22+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D033581",
          "name": "Stem Cell Transplantation",
          "type": "descriptor",
          "scope_note": "The transfer of STEM CELLS from one individual to another within the same species (TRANSPLANTATION, HOMOLOGOUS) or between species (XENOTRANSPLANTATION), or transfer within the same individual (TRANSPLANTATION, AUTOLOGOUS). The source and location of the stem cells determines their potency or pluripotency to differentiate into various cell types.",
          "tree_numbers": [
            "E02.095.147.500.500",
            "E04.936.225.687"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D033581",
      "preferred_label": "Stem Cell Transplantation",
      "type": "descriptor",
      "location": "vocabulary:13",
      "term": {
        "text": "\"Stem Cell Transplantation\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cell- and Tissue-Based Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:31:22+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D064987",
          "name": "Cell- and Tissue-Based Therapy",
          "type": "descriptor",
          "scope_note": "Therapies that involve the TRANSPLANTATION of CELLS or TISSUES developed for the purpose of restoring the function of diseased or dysfunctional cells or tissues.",
          "tree_numbers": [
            "E02.095.147"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D064987",
      "preferred_label": "Cell- and Tissue-Based Therapy",
      "type": "descriptor",
      "location": "vocabulary:14",
      "term": {
        "text": "\"Cell- and Tissue-Based Therapy\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Bone Marrow Cells",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:31:22+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001854",
          "name": "Bone Marrow Cells",
          "type": "descriptor",
          "scope_note": "Cells contained in the bone marrow including fat cells (see ADIPOCYTES); STROMAL CELLS; MEGAKARYOCYTES; and the immediate precursors of most blood cells.",
          "tree_numbers": [
            "A11.148",
            "A15.378.316"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001854",
      "preferred_label": "Bone Marrow Cells",
      "type": "descriptor",
      "location": "vocabulary:15",
      "term": {
        "text": "\"Bone Marrow Cells\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Rotator Cuff Injuries\"[MeSH Terms] OR \"Rotator Cuff\"[MeSH Terms] OR \"Tendon Injuries\"[MeSH Terms] OR \"Rotator Cuff\"[Title/Abstract] OR \"rotator cuff tear\"[Title/Abstract] OR \"rotator cuff repair\"[Title/Abstract] OR \"rotator cuff rupture\"[Title/Abstract] OR \"cuff tear\"[Title/Abstract] OR \"cuff repair\"[Title/Abstract] OR \"supraspinatus\"[Title/Abstract]) AND (\"Platelet-Rich Plasma\"[MeSH Terms] OR \"Mesenchymal Stem Cells\"[MeSH Terms] OR \"Stem Cell Transplantation\"[MeSH Terms] OR \"cell and tissue based therapy\"[MeSH Terms] OR \"Bone Marrow Cells\"[MeSH Terms] OR \"Platelet-Rich Plasma\"[Title/Abstract] OR \"PRP\"[Title/Abstract] OR \"MSC\"[Title/Abstract] OR \"MSCs\"[Title/Abstract] OR \"PRFM\"[Title/Abstract] OR \"ACP\"[Title/Abstract] OR \"platelet-rich fibrin\"[Title/Abstract] OR \"platelet rich fibrin matrix\"[Title/Abstract] OR \"platelet-leukocyte membrane\"[Title/Abstract] OR \"platelet-leukocyte membrane\"[Title/Abstract] OR \"plasma rich in growth factors\"[Title/Abstract] OR \"PRGF\"[Title/Abstract] OR \"autologous conditioned plasma\"[Title/Abstract] OR \"mesenchymal stem cell*\"[Title/Abstract] OR \"mesenchymal progenitor cell*\"[Title/Abstract] OR \"mesenchymal stromal cell*\"[Title/Abstract] OR \"bone marrow stromal cell*\"[Title/Abstract] OR \"bone marrow derived cell*\"[Title/Abstract] OR \"bone marrow aspirate\"[Title/Abstract] OR \"bone marrow aspirate concentrate\"[Title/Abstract] OR \"bone marrow concentrate\"[Title/Abstract] OR \"concentrated bone marrow aspirate\"[Title/Abstract] OR \"BMAC\"[Title/Abstract] OR \"adipose derived stem cell*\"[Title/Abstract] OR \"adipose derived stem cell*\"[Title/Abstract] OR \"adipose derived cell*\"[Title/Abstract] OR \"adipose derived cell*\"[Title/Abstract] OR \"adipose-derived regenerative cell\"[Title/Abstract] OR \"stromal vascular fraction\"[Title/Abstract] OR \"tendon derived stem cell*\"[Title/Abstract] OR \"tendon stem cell*\"[Title/Abstract] OR \"tenocyte*\"[Title/Abstract] OR \"tendon-derived cell\"[Title/Abstract] OR \"tendon derived cell*\"[Title/Abstract] OR \"tendon derived cell*\"[Title/Abstract] OR \"stem cell\"[Title/Abstract] OR \"stem cells\"[Title/Abstract] OR \"cellular therapy\"[Title/Abstract] OR \"cell therapy\"[Title/Abstract] OR \"biologic augmentation\"[Title/Abstract] OR \"biological augmentation\"[Title/Abstract]) AND 1800/01/01:2020/05/15[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "87b84e13fda27fc9faeb56cc01ecf9e97b222ef68c44c295d6c716c15a5fb68b",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The protocol names MSCs, but the intervention block does not search that bare acronym."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two concept blocks are combined with AND, and terms within each block are combined with OR. No design or outcome filter is imposed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The included MeSH headings cover rotator cuff injuries, the rotator cuff, platelet-rich plasma, mesenchymal stem cells, cell-based therapy, and bone marrow cells."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add the named MSC acronym as a free-text term. The 17 known relevant records are PRP studies, so they do not independently validate coverage of the other eligible intervention types."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed PubMed query is balanced and its field tags, Boolean operators, and date-entry bound are consistent with the stated strategy."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date bound is documented as an as-of cutoff; no publication-date restriction or unvalidated eligibility filter is applied."
        }
      },
      "findings": [
        {
          "id": "R1-T1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The searched intervention concept and eligibility criteria explicitly include MSCs, but the block has no bare MSC acronym term. Expanded phrases and the MeSH heading do not ensure retrieval of records that use only the acronym, particularly records not yet indexed.",
          "recommendation": "Add MSC*[tiab] (or an explicitly tested equivalent covering the acronym) to the cellular_therapy block, then rerun the complete strategy evaluation.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 6,
      "review_sha256": "1284ac41b55eecb58048ceeb17caeea259bdc252a8f9738ec944898fb11015a6",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched blocks represent the stated rotator cuff and biologic augmentation concepts. The intervention block now includes bare MSC and MSCs terms."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms within each concept are combined with OR, and the two concepts are combined with AND. No design or outcome filter is imposed."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed MeSH headings cover rotator cuff and tendon injuries, PRP, mesenchymal stem cells, cell-based therapy, and bone marrow cells."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Free-text terms cover the named intervention types and relevant variants, including MSC and MSCs. All 17 known relevant records are retrieved; the category probes screened 60 records outside the block and found none eligible."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed query has balanced grouping and consistent field tags and Boolean operators. The packet reports no translation issues or PubMed warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date cutoff is documented as an as-of date. No publication-date restriction or unvalidated design, population, or outcome filter is applied."
        }
      },
      "findings": [
        {
          "id": "R1-T1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The searched intervention concept and eligibility criteria include MSCs, but the prior strategy lacked a bare MSC acronym term.",
          "recommendation": "Add an explicitly tested bare MSC acronym expression to the cellular_therapy block and rerun the complete strategy evaluation.",
          "status": "resolved",
          "response": "Version 6 adds MSC[tiab] and MSCs[tiab]. The complete strategy evaluation reports 17/17 known relevant records retrieved, no translation issues, and no regression."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 6,
      "review_sha256": "1284ac41b55eecb58048ceeb17caeea259bdc252a8f9738ec944898fb11015a6",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The rotator cuff and biologic augmentation blocks represent the searched concepts. The intervention block now includes the bare MSC and MSCs terms required by the earlier finding."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms within each concept are combined with OR, and the two searched concepts are combined with AND. Comparative design, human population, comparator, and outcomes remain screening criteria."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes verified MeSH headings for rotator cuff and tendon injuries, PRP, mesenchymal stem cells, cell-based therapy, and bone marrow cells."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Free-text terms cover the named intervention types and variants, including bare MSC and MSCs. The 17 known relevant records are retrieved, and two category probes screened 60 records outside the block with none eligible. The known set comprises PRP studies, so retrieval of other intervention types is not independently established by those seeds."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed query has balanced grouping and consistent field tags and Boolean operators. The packet reports no translation issues or PubMed warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez date-entry cutoff is documented as an as-of bound. No publication-date restriction or unvalidated design, population, or outcome filter is applied."
        }
      },
      "findings": [
        {
          "id": "R1-T1",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The searched intervention concept and eligibility criteria include MSCs, but the prior strategy lacked a bare MSC acronym term.",
          "recommendation": "Add an explicitly tested bare MSC acronym expression to the cellular_therapy block and rerun the complete strategy evaluation.",
          "status": "resolved",
          "response": "Version 6 includes MSC[tiab] and MSCs[tiab]. The current evaluation retrieves all 17 known relevant records, reports no translation issues, and shows no regression."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

