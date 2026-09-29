# PubMed search strategy: audit

Generated 2026-09-28T23:07:45+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In patients with rotator cuff tears, is cellular therapy (e.g. mesenchymal stem cells, bone marrow aspirate, platelet-rich plasma) beneficial compared with controls for healing and clinical outcomes?
- Framework: PICO
- Scope confirmed by user: no (User supplied no known relevant articles and asked not to be queried during this run. Scope roles are therefore based on the stated criteria and remain unconfirmed. Standard-depth discovery and screening will proceed with reasonable assumptions. PubMed requests are bounded by PSB_AS_OF=2020-05-15 (Entrez date); no publication-date limit is applied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Rotator cuff tear or rotator cuff repair population | search | The target condition and its repair population define the review; specific tear and repair language is searchable and required. Probe for records describing only a member or adjacent rotator cuff term. |
| Cellular or biologic augmentation (MSCs, bone marrow aspirate, PRP, adipose- or tendon-derived cells) | search | The intervention defines the review and must be named; eligible records may name a specific therapy rather than the umbrella concept. |
| Healing/retear, pain, or functional outcomes | screen | Outcomes are inconsistently named in abstracts and should not be required in a recall-first effectiveness search. |
| Control/standard repair and randomized or comparative human clinical study | screen | Comparator, human status, and comparative design are eligibility properties better assessed at screening; no ad hoc design filter is justified. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T23:06:39+00:00
- Records added to PubMed up to: 2020-05-15
- Total records: 604
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Rotator Cuff Injuries[Mesh]` | 6,021 | none |
| 2 | `Rotator Cuff[Mesh]` | 6,661 | none |
| 3 | `rotator cuff[tiab]` | 11,564 | none |
| 4 | `rotator cuff tear[tiab]` | 2,632 | none |
| 5 | `rotator cuff tears[tiab]` | 3,703 | none |
| 6 | `rotator cuff repair[tiab]` | 2,813 | none |
| 7 | `rotator cuff repairs[tiab]` | 519 | none |
| 8 | `rotator cuff rupture[tiab]` | 132 | none |
| 9 | `rotator cuff ruptures[tiab]` | 57 | none |
| 10 | `cuff tear*[tiab]` | 5,400 | none |
| 11 | `cuff injur*[tiab]` | 499 | none |
| 12 | `supraspinatus tear*[tiab]` | 294 | none |
| 13 | `infraspinatus tear*[tiab]` | 64 | none |
| 14 | `subscapularis tear*[tiab]` | 223 | none |
| 15 | `teres minor tear*[tiab]` | 4 | none |
| 16 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15` | 13,339 | none |
| 17 | `Platelet-Rich Plasma[Mesh]` | 4,666 | none |
| 18 | `Platelet-Rich Fibrin[Mesh]` | 450 | none |
| 19 | `Mesenchymal Stem Cells[Mesh]` | 39,771 | none |
| 20 | `"Cell- and Tissue-Based Therapy"[Mesh]` | 288,735 | none |
| 21 | `Mesenchymal Stem Cell Transplantation[Mesh]` | 12,417 | none |
| 22 | `Stem Cell Transplantation[Mesh]` | 85,537 | none |
| 23 | `platelet-rich plasma[tiab]` | 9,974 | none |
| 24 | `platelet rich plasma[tiab]` | 9,974 | none |
| 25 | `PRP[tiab]` | 15,823 | none |
| 26 | `platelet-rich fibrin[tiab]` | 1,215 | none |
| 27 | `platelet rich fibrin[tiab]` | 1,215 | none |
| 28 | `platelet-rich fibrin matrix[tiab]` | 59 | none |
| 29 | `platelet rich fibrin matrix[tiab]` | 59 | none |
| 30 | `PRFM[tiab]` | 48 | none |
| 31 | `L-PRF[tiab]` | 124 | none |
| 32 | `(leukocyte[tiab] AND fibrin[tiab])` | 665 | none |
| 33 | `plasma rich in growth factor*[tiab]` | 264 | none |
| 34 | `PRGF[tiab]` | 304 | none |
| 35 | `autologous conditioned plasma[tiab]` | 59 | none |
| 36 | `mesenchymal stem cell*[tiab]` | 43,533 | none |
| 37 | `mesenchymal stromal cell*[tiab]` | 6,831 | none |
| 38 | `multipotent stromal cell*[tiab]` | 426 | none |
| 39 | `MSC[tiab]` | 18,591 | none |
| 40 | `MSCs[tiab]` | 24,583 | none |
| 41 | `bone marrow aspirate[tiab]` | 2,375 | none |
| 42 | `bone marrow aspirates[tiab]` | 1,906 | none |
| 43 | `bone marrow aspirate concentrate[tiab]` | 186 | none |
| 44 | `bone marrow aspirate concentrate*[tiab]` | 191 | none |
| 45 | `BMAC[tiab]` | 175 | none |
| 46 | `bone marrow concentrate[tiab]` | 146 | none |
| 47 | `adipose-derived stem cell*[tiab]` | 4,602 | none |
| 48 | `adipose derived stem cell*[tiab]` | 4,602 | none |
| 49 | `adipose-derived stromal cell*[tiab]` | 637 | none |
| 50 | `adipose derived stromal cell*[tiab]` | 637 | none |
| 51 | `tendon-derived stem cell*[tiab]` | 110 | none |
| 52 | `tendon-derived progenitor cell*[tiab]` | 6 | none |
| 53 | `biologic augmentation[tiab]` | 76 | none |
| 54 | `biological augmentation[tiab]` | 121 | none |
| 55 | `cell therapy[tiab]` | 21,682 | none |
| 56 | `cell therapies[tiab]` | 4,240 | none |
| 57 | `cellular therapy[tiab]` | 2,805 | none |
| 58 | `cellular therapies[tiab]` | 1,396 | none |
| 59 | `adipose-derived cell*[tiab]` | 106 | none |
| 60 | `adipose derived cell*[tiab]` | 106 | none |
| 61 | `tendon-derived cell*[tiab]` | 67 | none |
| 62 | `tendon derived cell*[tiab]` | 67 | none |
| 63 | `#17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62` | 374,608 | none |
| 64 | `#16 AND #63` | 604 | none |

### Strategy (single line, for copying into PubMed)

```text
((Rotator Cuff Injuries[Mesh] OR Rotator Cuff[Mesh] OR rotator cuff[tiab] OR rotator cuff tear[tiab] OR rotator cuff tears[tiab] OR rotator cuff repair[tiab] OR rotator cuff repairs[tiab] OR rotator cuff rupture[tiab] OR rotator cuff ruptures[tiab] OR cuff tear*[tiab] OR cuff injur*[tiab] OR supraspinatus tear*[tiab] OR infraspinatus tear*[tiab] OR subscapularis tear*[tiab] OR teres minor tear*[tiab]) AND (Platelet-Rich Plasma[Mesh] OR Platelet-Rich Fibrin[Mesh] OR Mesenchymal Stem Cells[Mesh] OR "Cell- and Tissue-Based Therapy"[Mesh] OR Mesenchymal Stem Cell Transplantation[Mesh] OR Stem Cell Transplantation[Mesh] OR platelet-rich plasma[tiab] OR platelet rich plasma[tiab] OR PRP[tiab] OR platelet-rich fibrin[tiab] OR platelet rich fibrin[tiab] OR platelet-rich fibrin matrix[tiab] OR platelet rich fibrin matrix[tiab] OR PRFM[tiab] OR L-PRF[tiab] OR (leukocyte[tiab] AND fibrin[tiab]) OR plasma rich in growth factor*[tiab] OR PRGF[tiab] OR autologous conditioned plasma[tiab] OR mesenchymal stem cell*[tiab] OR mesenchymal stromal cell*[tiab] OR multipotent stromal cell*[tiab] OR MSC[tiab] OR MSCs[tiab] OR bone marrow aspirate[tiab] OR bone marrow aspirates[tiab] OR bone marrow aspirate concentrate[tiab] OR bone marrow aspirate concentrate*[tiab] OR BMAC[tiab] OR bone marrow concentrate[tiab] OR adipose-derived stem cell*[tiab] OR adipose derived stem cell*[tiab] OR adipose-derived stromal cell*[tiab] OR adipose derived stromal cell*[tiab] OR tendon-derived stem cell*[tiab] OR tendon-derived progenitor cell*[tiab] OR biologic augmentation[tiab] OR biological augmentation[tiab] OR cell therapy[tiab] OR cell therapies[tiab] OR cellular therapy[tiab] OR cellular therapies[tiab] OR adipose-derived cell*[tiab] OR adipose derived cell*[tiab] OR tendon-derived cell*[tiab] OR tendon derived cell*[tiab])) AND ("1800/01/01"[edat] : "2020/05/15"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 12 | 12 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Rotator cuff tear or rotator cuff repair population | 1 | `Rotator Cuff Injuries[Mesh] OR rotator cuff[tiab] OR supraspinatus[tiab] OR infraspinatus[tiab] OR subscapularis[tiab] OR shoulder tendon[tiab]` | 33 | 0/30 |
| Rotator cuff tear or rotator cuff repair population | 2 | `Rotator Cuff Injuries[Mesh] OR rotator cuff[tiab] OR supraspinatus[tiab] OR infraspinatus[tiab] OR subscapularis[tiab] OR shoulder tendon[tiab]` | 34 | 0/30 |
| Cellular or biologic augmentation (MSCs, bone marrow aspirate, PRP, adipose- or tendon-derived cells) | 1 | `platelet*[tiab] OR cell*[tiab] OR biologic*[tiab] OR marrow[tiab] OR growth factor*[tiab] OR tissue augmentation[tiab]` | 745 | 0/30 |
| Cellular or biologic augmentation (MSCs, bone marrow aspirate, PRP, adipose- or tendon-derived cells) | 2 | `platelet*[tiab] OR cell*[tiab] OR biologic*[tiab] OR marrow[tiab] OR growth factor*[tiab] OR tissue augmentation[tiab]` | 737 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| rotator_cuff | 374,608 | 0 |
| cellular_therapy | 13,339 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial recall-first two-concept strategy; MeSH and title/abstract alternatives added for rotator cuff and the eligible cellular/platelet-rich interventions. No seeds supplied; screened systematic-review citations provide an external benchmark. |
| 2 | 596 | rotator_cuff: +0 / -1; cellular_therapy: +1 / -1 | none | Corrected field-tag parsing for the multiword MeSH heading and removed an impingement heading that was not specific to tear/repair eligibility. |
| 3 | 596 | cellular_therapy: +1 / -1 | none | Rewrote the zero-hit leukocyte-rich fibrin phrase as explicit co-occurrence of the two indexed words; the phrase was flagged by PubMed as not found. Broadens the wording while retaining the named intervention. |
| 4 | 604 | cellular_therapy: +6 / -0 | none | Addressed round-1 critic findings by adding cellular therapy/therapies and bare adipose-/tendon-derived cell forms in hyphenated and unhyphenated variants. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 2 findings; P1-F1 must-fix open, P1-F2 must-fix open
- Round 2 on version 4: 2 findings; P1-F1 must-fix resolved, P1-F2 must-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 824 NCBI requests logged (457 from cache); strategy sha256 0bcae07919a4._

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
      "checked_at": "2026-09-28T23:06:39+00:00",
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
        "text": "Rotator Cuff Injuries",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Rotator Cuff",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:06:39+00:00",
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
        "text": "Rotator Cuff",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Platelet-Rich Plasma",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:06:39+00:00",
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
      "location": "vocabulary:16",
      "term": {
        "text": "Platelet-Rich Plasma",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Platelet-Rich Fibrin",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:06:39+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000073183",
          "name": "Platelet-Rich Fibrin",
          "type": "descriptor",
          "scope_note": "A fibrin matrix derived from platelet-rich plasma that contains high concentration of BLOOD PLATELETS; LEUKOCYTES; CYTOKINES; and GROWTH FACTORS. It is used in a variety of clinical and TISSUE ENGINEERING applications.",
          "tree_numbers": [
            "A12.207.152.693.600.500",
            "A12.207.270.695.600.500",
            "A15.145.693.600.500"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000073183",
      "preferred_label": "Platelet-Rich Fibrin",
      "type": "descriptor",
      "location": "vocabulary:17",
      "term": {
        "text": "Platelet-Rich Fibrin",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mesenchymal Stem Cells",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:06:39+00:00",
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
      "location": "vocabulary:18",
      "term": {
        "text": "Mesenchymal Stem Cells",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cell- and Tissue-Based Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:06:39+00:00",
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
      "location": "vocabulary:19",
      "term": {
        "text": "\"Cell- and Tissue-Based Therapy\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mesenchymal Stem Cell Transplantation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:06:39+00:00",
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
      "location": "vocabulary:20",
      "term": {
        "text": "Mesenchymal Stem Cell Transplantation",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stem Cell Transplantation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:06:39+00:00",
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
      "location": "vocabulary:21",
      "term": {
        "text": "Stem Cell Transplantation",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"rotator cuff injuries\"[MeSH Terms] OR \"rotator cuff\"[MeSH Terms] OR \"rotator cuff\"[Title/Abstract] OR \"rotator cuff tear\"[Title/Abstract] OR \"rotator cuff tears\"[Title/Abstract] OR \"rotator cuff repair\"[Title/Abstract] OR \"rotator cuff repairs\"[Title/Abstract] OR \"rotator cuff rupture\"[Title/Abstract] OR \"rotator cuff ruptures\"[Title/Abstract] OR \"cuff tear*\"[Title/Abstract] OR \"cuff injur*\"[Title/Abstract] OR \"supraspinatus tear*\"[Title/Abstract] OR \"infraspinatus tear*\"[Title/Abstract] OR \"subscapularis tear*\"[Title/Abstract] OR \"teres minor tear*\"[Title/Abstract]) AND (\"platelet rich plasma\"[MeSH Terms] OR \"platelet rich fibrin\"[MeSH Terms] OR \"mesenchymal stem cells\"[MeSH Terms] OR \"cell and tissue based therapy\"[MeSH Terms] OR \"mesenchymal stem cell transplantation\"[MeSH Terms] OR \"stem cell transplantation\"[MeSH Terms] OR \"platelet rich plasma\"[Title/Abstract] OR \"platelet rich plasma\"[Title/Abstract] OR \"PRP\"[Title/Abstract] OR \"platelet rich fibrin\"[Title/Abstract] OR \"platelet rich fibrin\"[Title/Abstract] OR \"platelet rich fibrin matrix\"[Title/Abstract] OR \"platelet rich fibrin matrix\"[Title/Abstract] OR \"PRFM\"[Title/Abstract] OR \"L-PRF\"[Title/Abstract] OR (\"leukocyte\"[Title/Abstract] AND \"fibrin\"[Title/Abstract]) OR \"plasma rich in growth factor*\"[Title/Abstract] OR \"PRGF\"[Title/Abstract] OR \"autologous conditioned plasma\"[Title/Abstract] OR \"mesenchymal stem cell*\"[Title/Abstract] OR \"mesenchymal stromal cell*\"[Title/Abstract] OR \"multipotent stromal cell*\"[Title/Abstract] OR \"MSC\"[Title/Abstract] OR \"MSCs\"[Title/Abstract] OR \"bone marrow aspirate\"[Title/Abstract] OR \"bone marrow aspirates\"[Title/Abstract] OR \"bone marrow aspirate concentrate\"[Title/Abstract] OR \"bone marrow aspirate concentrate*\"[Title/Abstract] OR \"BMAC\"[Title/Abstract] OR \"bone marrow concentrate\"[Title/Abstract] OR \"adipose derived stem cell*\"[Title/Abstract] OR \"adipose derived stem cell*\"[Title/Abstract] OR \"adipose derived stromal cell*\"[Title/Abstract] OR \"adipose derived stromal cell*\"[Title/Abstract] OR \"tendon derived stem cell*\"[Title/Abstract] OR \"tendon derived progenitor cell*\"[Title/Abstract] OR \"biologic augmentation\"[Title/Abstract] OR \"biological augmentation\"[Title/Abstract] OR \"cell therapy\"[Title/Abstract] OR \"cell therapies\"[Title/Abstract] OR \"cellular therapy\"[Title/Abstract] OR \"cellular therapies\"[Title/Abstract] OR \"adipose derived cell*\"[Title/Abstract] OR \"adipose derived cell*\"[Title/Abstract] OR \"tendon derived cell*\"[Title/Abstract] OR \"tendon derived cell*\"[Title/Abstract]) AND 1800/01/01:2020/05/15[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "42af2b5c47fa93ddc7c65c2a59f8b97389cb69856c085d18decf8f968dceeea4",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The searched intervention concept does not cover every therapy name stated in the question and eligibility criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "The population and intervention blocks are combined with AND, and their terms are combined with OR. Outcomes and design are appropriately left for screening."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The listed MeSH headings are verified in the packet, and no translation issues are reported."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The strategy omits the bare phrase cellular therapy and searches adipose-derived and tendon-derived cells only in narrower stem or progenitor cell phrases."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed errors or warnings, and the displayed query is grouped as intended."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No study-design, human, or outcome filter is imposed. The Entrez date boundary is reported as the as-of retrieval boundary, with no publication-date limit."
        }
      },
      "findings": [
        {
          "id": "P1-F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The question names cellular therapy, but the intervention block searches cell therapy and cell therapies without searching the stated bare name.",
          "recommendation": "Add explicit Title/Abstract expressions for cellular therapy and cellular therapies, then rerun the complete evaluation.",
          "status": "open"
        },
        {
          "id": "P1-F2",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility names adipose-derived cells and tendon-derived cells. The block covers only narrower adipose-derived stem or stromal cell phrases and tendon-derived stem or progenitor cell phrases, so it does not cover those members by their bare names.",
          "recommendation": "Add explicit Title/Abstract expressions for adipose-derived cell(s) and tendon-derived cell(s), including hyphenated and unhyphenated forms, then rerun the complete evaluation.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "a921e3e7f95c30e5daf1274470ffd89073d7c3c8443507e8d431c57aa87bd10e",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The intervention block now includes the named cellular therapy, adipose-derived cell, and tendon-derived cell expressions. The packet reports no translation issues, and all 12 benchmark records are retrieved."
        },
        "operators": {
          "verdict": "pass",
          "note": "Population and intervention terms are ORed within their blocks and combined with AND. Outcomes, comparator, and study design remain screening criteria."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports verified MeSH headings and no translation issues."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The revised block explicitly searches cellular therapy/cellular therapies and adipose-derived/tendon-derived cells in hyphenated and unhyphenated forms. The packet reports no PubMed warnings."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed query is grouped as intended; the packet reports no PubMed errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No outcome, human, or study-design filter is imposed. The Entrez date boundary is documented as the retrieval as-of boundary, with no publication-date limit."
        }
      },
      "findings": [
        {
          "id": "P1-F1",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The question names cellular therapy, but the prior intervention block searched cell therapy and cell therapies without the stated bare name.",
          "recommendation": "Add explicit Title/Abstract expressions for cellular therapy and cellular therapies, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The revised strategy includes cellular therapy[tiab] and cellular therapies[tiab]. The packet records a complete version 4 evaluation."
        },
        {
          "id": "P1-F2",
          "domain": "translation",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility names adipose-derived cells and tendon-derived cells, while the prior block searched only narrower stem, stromal, or progenitor cell phrases.",
          "recommendation": "Add explicit Title/Abstract expressions for adipose-derived cell(s) and tendon-derived cell(s), including hyphenated and unhyphenated forms, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The revised strategy includes adipose-derived cell*[tiab], adipose derived cell*[tiab], tendon-derived cell*[tiab], and tendon derived cell*[tiab]. The packet records a complete version 4 evaluation."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

