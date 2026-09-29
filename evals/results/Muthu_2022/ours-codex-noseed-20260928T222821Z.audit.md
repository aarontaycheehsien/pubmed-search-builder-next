# PubMed search strategy: audit

Generated 2026-09-28T22:51:16+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In patients with rotator cuff tears, is cellular therapy (e.g. mesenchymal stem cells, bone marrow aspirate, platelet-rich plasma) beneficial compared with controls for healing and clinical outcomes?
- Framework: PICO
- Scope confirmed by user: yes (Scope roles were set from the supplied question and eligibility criteria. The user said they cannot answer questions during this run, so scope confirmation is assumed and no clarification pause was made. No known relevant articles were supplied; standard depth and its 10,000-record screening budget are assumed. The run harness explicitly requires the PubMed Entrez-date bound 2020-05-15 on every command, forbids web searching and records added after that date, and forbids a publication-date cutoff; the query therefore retains the protocol as_of entry-date restriction. Outcomes, comparator, and comparative human design are screened rather than required Boolean blocks.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Rotator cuff tear or rotator cuff repair | search | Core population condition/procedure; indexed papers may identify a specific cuff tendon or repair procedure rather than use the phrase rotator cuff tear. |
| Cellular or biologic augmentation (MSCs, bone marrow aspirate/concentrate, PRP, adipose- or tendon-derived cells) | search | Core intervention; papers may name a member such as PRP or bone marrow concentrate without calling it cellular therapy. |
| Randomized or comparative human clinical study | screen | Comparative clinical design and human eligibility are screened; no unvalidated design block or filter is required. |
| Healing/retear, pain, or functional outcome | screen | Outcomes are inconsistently named in titles and abstracts and can be screened against eligibility. |
| Control or standard repair without cellular augmentation | screen | Comparators are not reliably named in abstracts and do not define the searchable topic. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T22:50:09+00:00
- Records added to PubMed up to: 2020-05-15
- Total records: 1,508
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Rotator Cuff Injuries"[Mesh]` | 6,021 | none |
| 2 | `"Rotator Cuff"[Mesh]` | 6,661 | none |
| 3 | `"Tendon Injuries"[Mesh]` | 25,376 | none |
| 4 | `"Shoulder Injuries"[Mesh]` | 19,024 | none |
| 5 | `"rotator cuff"[tiab]` | 11,564 | none |
| 6 | `rotator cuff tear*[tiab]` | 5,069 | none |
| 7 | `rotator cuff injur*[tiab]` | 443 | none |
| 8 | `rotator cuff repair*[tiab]` | 2,985 | none |
| 9 | `cuff tear*[tiab]` | 5,400 | none |
| 10 | `cuff injur*[tiab]` | 499 | none |
| 11 | `cuff repair*[tiab]` | 3,085 | none |
| 12 | `supraspinatus[tiab]` | 3,580 | none |
| 13 | `infraspinatus[tiab]` | 2,148 | none |
| 14 | `subscapularis[tiab]` | 1,974 | none |
| 15 | `teres minor[tiab]` | 438 | none |
| 16 | `shoulder tendon tear*[tiab]` | 3 | none |
| 17 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16` | 44,456 | none |
| 18 | `"Mesenchymal Stem Cells"[Mesh]` | 39,771 | none |
| 19 | `"Platelet-Rich Plasma"[Mesh]` | 4,666 | none |
| 20 | `"Platelet-Rich Fibrin"[Mesh]` | 450 | none |
| 21 | `"Bone Marrow Cells"[Mesh]` | 185,831 | none |
| 22 | `"Adult Stem Cells"[Mesh]` | 16,523 | none |
| 23 | `"Adipose Tissue"[Mesh]` | 100,144 | none |
| 24 | `"Stem Cell Transplantation"[Mesh]` | 85,537 | none |
| 25 | `"Mesenchymal Stem Cell Transplantation"[Mesh]` | 12,417 | none |
| 26 | `"Regenerative Medicine"[Mesh]` | 6,828 | none |
| 27 | `mesenchymal stem cell*[tiab]` | 43,533 | none |
| 28 | `mesenchymal stromal cell*[tiab]` | 6,831 | none |
| 29 | `multipotent stromal cell*[tiab]` | 426 | none |
| 30 | `bone marrow aspirat*[tiab]` | 6,578 | none |
| 31 | `bone marrow concentrat*[tiab]` | 200 | none |
| 32 | `bone marrow-derived cell*[tiab]` | 2,930 | none |
| 33 | `marrow aspirate concentrat*[tiab]` | 194 | none |
| 34 | `BMAC[tiab]` | 175 | none |
| 35 | `platelet-rich plasma[tiab]` | 9,974 | none |
| 36 | `platelet rich plasma[tiab]` | 9,974 | none |
| 37 | `PRP[tiab]` | 15,823 | none |
| 38 | `platelet-rich fibrin[tiab]` | 1,215 | none |
| 39 | `platelet rich fibrin[tiab]` | 1,215 | none |
| 40 | `PRF[tiab]` | 3,559 | none |
| 41 | `platelet gel[tiab]` | 277 | none |
| 42 | `autologous conditioned plasma[tiab]` | 59 | none |
| 43 | `adipose-derived stem cell*[tiab]` | 4,602 | none |
| 44 | `adipose derived stem cell*[tiab]` | 4,602 | none |
| 45 | `adipose-derived cell*[tiab]` | 106 | none |
| 46 | `adipose derived cell*[tiab]` | 106 | none |
| 47 | `adipose-derived stromal cell*[tiab]` | 637 | none |
| 48 | `adipose derived stromal cell*[tiab]` | 637 | none |
| 49 | `adipose-derived regenerative cell*[tiab]` | 76 | none |
| 50 | `adipose derived regenerative cell*[tiab]` | 76 | none |
| 51 | `ADRC[tiab]` | 186 | none |
| 52 | `stromal vascular fraction[tiab]` | 1,216 | none |
| 53 | `SVF[tiab]` | 1,034 | none |
| 54 | `fat-derived stem cell*[tiab]` | 24 | none |
| 55 | `tendon-derived cell*[tiab]` | 67 | none |
| 56 | `tendon derived cell*[tiab]` | 67 | none |
| 57 | `tendon-derived stem cell*[tiab]` | 110 | none |
| 58 | `tendon derived stem cell*[tiab]` | 110 | none |
| 59 | `progenitor cell*[tiab]` | 61,605 | none |
| 60 | `cell therap*[tiab]` | 25,153 | none |
| 61 | `cellular therap*[tiab]` | 4,300 | none |
| 62 | `biologic augmentation[tiab]` | 76 | none |
| 63 | `biological augmentation[tiab]` | 121 | none |
| 64 | `biologic augment*[tiab]` | 81 | none |
| 65 | `biological augment*[tiab]` | 126 | none |
| 66 | `#18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65` | 488,577 | none |
| 67 | `#17 AND #66` | 1,508 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Rotator Cuff Injuries"[Mesh] OR "Rotator Cuff"[Mesh] OR "Tendon Injuries"[Mesh] OR "Shoulder Injuries"[Mesh] OR "rotator cuff"[tiab] OR rotator cuff tear*[tiab] OR rotator cuff injur*[tiab] OR rotator cuff repair*[tiab] OR cuff tear*[tiab] OR cuff injur*[tiab] OR cuff repair*[tiab] OR supraspinatus[tiab] OR infraspinatus[tiab] OR subscapularis[tiab] OR teres minor[tiab] OR shoulder tendon tear*[tiab]) AND ("Mesenchymal Stem Cells"[Mesh] OR "Platelet-Rich Plasma"[Mesh] OR "Platelet-Rich Fibrin"[Mesh] OR "Bone Marrow Cells"[Mesh] OR "Adult Stem Cells"[Mesh] OR "Adipose Tissue"[Mesh] OR "Stem Cell Transplantation"[Mesh] OR "Mesenchymal Stem Cell Transplantation"[Mesh] OR "Regenerative Medicine"[Mesh] OR mesenchymal stem cell*[tiab] OR mesenchymal stromal cell*[tiab] OR multipotent stromal cell*[tiab] OR bone marrow aspirat*[tiab] OR bone marrow concentrat*[tiab] OR bone marrow-derived cell*[tiab] OR marrow aspirate concentrat*[tiab] OR BMAC[tiab] OR platelet-rich plasma[tiab] OR platelet rich plasma[tiab] OR PRP[tiab] OR platelet-rich fibrin[tiab] OR platelet rich fibrin[tiab] OR PRF[tiab] OR platelet gel[tiab] OR autologous conditioned plasma[tiab] OR adipose-derived stem cell*[tiab] OR adipose derived stem cell*[tiab] OR adipose-derived cell*[tiab] OR adipose derived cell*[tiab] OR adipose-derived stromal cell*[tiab] OR adipose derived stromal cell*[tiab] OR adipose-derived regenerative cell*[tiab] OR adipose derived regenerative cell*[tiab] OR ADRC[tiab] OR stromal vascular fraction[tiab] OR SVF[tiab] OR fat-derived stem cell*[tiab] OR tendon-derived cell*[tiab] OR tendon derived cell*[tiab] OR tendon-derived stem cell*[tiab] OR tendon derived stem cell*[tiab] OR progenitor cell*[tiab] OR cell therap*[tiab] OR cellular therap*[tiab] OR biologic augmentation[tiab] OR biological augmentation[tiab] OR biologic augment*[tiab] OR biological augment*[tiab])) AND ("1800/01/01"[edat] : "2020/05/15"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 15 | 15 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 6 | 6 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Rotator cuff tear or rotator cuff repair | 1 | `(shoulder[tiab] AND (tendon*[tiab] OR tear*[tiab] OR injur*[tiab] OR repair*[tiab])) OR Tendon Injuries[Mesh]` | 36 | 0/30 |
| Rotator cuff tear or rotator cuff repair | 2 | `(shoulder[tiab] AND (tendon*[tiab] OR tear*[tiab] OR injur*[tiab] OR repair*[tiab])) OR Tendon Injuries[Mesh]` | 43 | 0/30 |
| Cellular or biologic augmentation (MSCs, bone marrow aspirate/concentrate, PRP, adipose- or tendon-derived cells) | 1 | `(cell*[tiab] OR marrow[tiab] OR platelet*[tiab] OR plasma[tiab] OR growth factor*[tiab] OR tissue engineer*[tiab] OR regenerative[tiab] OR autologous[tiab])` | 1,988 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| rotator_cuff | 488,577 | 0 |
| biologic | 44,456 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,180 | initial | none | Initial broad strategy; both searchable blocks have MeSH and text words. |
| 2 | 1,508 | biologic: +10 / -0 | none | Expanded the biologic block to recover the missed randomized trial of uncultured autologous adipose-derived regenerative cells; added title terms and MeSH headings from the missed record. The validation set remains held out. |
| 3 | 1,508 | biologic: +0 / -1 | none | Removed UA-ADRC as a standalone acronym after PubMed returned a no-items warning and zero hits; retained the expanded adipose-derived regenerative-cell wording plus ADRC and stromal vascular fraction terms that cover the missed record. |
| 4 | 1,508 | biologic: +2 / -0 | none | Added bare adipose-derived cell variants per critic finding R1-01, while retaining stem/stromal/regenerative qualifiers. Entrez cutoff remains required by the task harness for this run. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 2 findings; R1-01 must-fix open, R1-02 must-fix open
- Round 2 on version 4: 2 findings; R1-01 must-fix resolved, R1-02 must-fix accepted-risk
- Round 3 on version 4: 2 findings; R1-01 must-fix resolved, R1-02 must-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1187 NCBI requests logged (739 from cache); strategy sha256 30d03cb866f5._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:rotator_cuff",
        "blocking": false,
        "requires_review": true,
        "id": "I-edaaca22f54a55f9d2dc"
      }
    ],
    "issues": [
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:rotator_cuff",
        "blocking": false,
        "requires_review": true,
        "id": "I-edaaca22f54a55f9d2dc"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Rotator Cuff Injuries",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:50:09+00:00",
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
      "checked_at": "2026-09-28T22:50:09+00:00",
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
      "checked_at": "2026-09-28T22:50:09+00:00",
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
      "requested": "Shoulder Injuries",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:50:09+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000070599",
          "name": "Shoulder Injuries",
          "type": "descriptor",
          "scope_note": "Injuries involving the SHOULDERS and SHOULDER JOINT.",
          "tree_numbers": [
            "C26.803"
          ],
          "entry_terms": 8,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000070599",
      "preferred_label": "Shoulder Injuries",
      "type": "descriptor",
      "location": "vocabulary:4",
      "term": {
        "text": "\"Shoulder Injuries\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mesenchymal Stem Cells",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:50:09+00:00",
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
      "location": "vocabulary:17",
      "term": {
        "text": "\"Mesenchymal Stem Cells\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Platelet-Rich Plasma",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:50:09+00:00",
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
      "location": "vocabulary:18",
      "term": {
        "text": "\"Platelet-Rich Plasma\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Platelet-Rich Fibrin",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:50:09+00:00",
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
      "location": "vocabulary:19",
      "term": {
        "text": "\"Platelet-Rich Fibrin\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Bone Marrow Cells",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:50:09+00:00",
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
      "location": "vocabulary:20",
      "term": {
        "text": "\"Bone Marrow Cells\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adult Stem Cells",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:50:09+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D053687",
          "name": "Adult Stem Cells",
          "type": "descriptor",
          "scope_note": "Tissue-specific stem cells (also known as Somatic Stem Cells) that appear during fetal development and remain in the body throughout life. The key functions of adult stem cells are to maintain and repair the specific tissues where they reside (e.g. skin or blood).",
          "tree_numbers": [
            "A11.872.040"
          ],
          "entry_terms": 8,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D053687",
      "preferred_label": "Adult Stem Cells",
      "type": "descriptor",
      "location": "vocabulary:21",
      "term": {
        "text": "\"Adult Stem Cells\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adipose Tissue",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:50:09+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000273",
          "name": "Adipose Tissue",
          "type": "descriptor",
          "scope_note": "Specialized connective tissue composed of fat cells (ADIPOCYTES). It is the site of stored FATS, usually in the form of TRIGLYCERIDES. In mammals, there are two types of adipose tissue, the WHITE FAT and the BROWN FAT. Their relative distributions vary in different species with most adipose tissue being white.",
          "tree_numbers": [
            "A10.165.114"
          ],
          "entry_terms": 8,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000273",
      "preferred_label": "Adipose Tissue",
      "type": "descriptor",
      "location": "vocabulary:22",
      "term": {
        "text": "\"Adipose Tissue\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Stem Cell Transplantation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:50:09+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "\"Stem Cell Transplantation\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Mesenchymal Stem Cell Transplantation",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:50:09+00:00",
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
      "location": "vocabulary:24",
      "term": {
        "text": "\"Mesenchymal Stem Cell Transplantation\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Regenerative Medicine",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T22:50:09+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D044968",
          "name": "Regenerative Medicine",
          "type": "descriptor",
          "scope_note": "A field of medicine concerned with developing and using strategies aimed at repair or replacement of damaged, diseased, or metabolically deficient organs, tissues, and cells via TISSUE ENGINEERING; CELL TRANSPLANTATION; and ARTIFICIAL ORGANS and BIOARTIFICIAL ORGANS and tissues.",
          "tree_numbers": [
            "H02.403.750"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D044968",
      "preferred_label": "Regenerative Medicine",
      "type": "descriptor",
      "location": "vocabulary:25",
      "term": {
        "text": "\"Regenerative Medicine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Rotator Cuff Injuries\"[MeSH Terms] OR \"Rotator Cuff\"[MeSH Terms] OR \"Tendon Injuries\"[MeSH Terms] OR \"Shoulder Injuries\"[MeSH Terms] OR \"Rotator Cuff\"[Title/Abstract] OR \"rotator cuff tear*\"[Title/Abstract] OR \"rotator cuff injur*\"[Title/Abstract] OR \"rotator cuff repair*\"[Title/Abstract] OR \"cuff tear*\"[Title/Abstract] OR \"cuff injur*\"[Title/Abstract] OR \"cuff repair*\"[Title/Abstract] OR \"supraspinatus\"[Title/Abstract] OR \"infraspinatus\"[Title/Abstract] OR \"subscapularis\"[Title/Abstract] OR \"teres minor\"[Title/Abstract] OR \"shoulder tendon tear*\"[Title/Abstract]) AND (\"Mesenchymal Stem Cells\"[MeSH Terms] OR \"Platelet-Rich Plasma\"[MeSH Terms] OR \"Platelet-Rich Fibrin\"[MeSH Terms] OR \"Bone Marrow Cells\"[MeSH Terms] OR \"Adult Stem Cells\"[MeSH Terms] OR \"Adipose Tissue\"[MeSH Terms] OR \"Stem Cell Transplantation\"[MeSH Terms] OR \"Mesenchymal Stem Cell Transplantation\"[MeSH Terms] OR \"Regenerative Medicine\"[MeSH Terms] OR \"mesenchymal stem cell*\"[Title/Abstract] OR \"mesenchymal stromal cell*\"[Title/Abstract] OR \"multipotent stromal cell*\"[Title/Abstract] OR \"bone marrow aspirat*\"[Title/Abstract] OR \"bone marrow concentrat*\"[Title/Abstract] OR \"bone marrow derived cell*\"[Title/Abstract] OR \"marrow aspirate concentrat*\"[Title/Abstract] OR \"BMAC\"[Title/Abstract] OR \"Platelet-Rich Plasma\"[Title/Abstract] OR \"Platelet-Rich Plasma\"[Title/Abstract] OR \"PRP\"[Title/Abstract] OR \"Platelet-Rich Fibrin\"[Title/Abstract] OR \"Platelet-Rich Fibrin\"[Title/Abstract] OR \"PRF\"[Title/Abstract] OR \"platelet gel\"[Title/Abstract] OR \"autologous conditioned plasma\"[Title/Abstract] OR \"adipose derived stem cell*\"[Title/Abstract] OR \"adipose derived stem cell*\"[Title/Abstract] OR \"adipose derived cell*\"[Title/Abstract] OR \"adipose derived cell*\"[Title/Abstract] OR \"adipose derived stromal cell*\"[Title/Abstract] OR \"adipose derived stromal cell*\"[Title/Abstract] OR \"adipose derived regenerative cell*\"[Title/Abstract] OR \"adipose derived regenerative cell*\"[Title/Abstract] OR \"ADRC\"[Title/Abstract] OR \"stromal vascular fraction\"[Title/Abstract] OR \"SVF\"[Title/Abstract] OR \"fat derived stem cell*\"[Title/Abstract] OR \"tendon derived cell*\"[Title/Abstract] OR \"tendon derived cell*\"[Title/Abstract] OR \"tendon derived stem cell*\"[Title/Abstract] OR \"tendon derived stem cell*\"[Title/Abstract] OR \"progenitor cell*\"[Title/Abstract] OR \"cell therap*\"[Title/Abstract] OR \"cellular therap*\"[Title/Abstract] OR \"biologic augmentation\"[Title/Abstract] OR \"biological augmentation\"[Title/Abstract] OR \"biologic augment*\"[Title/Abstract] OR \"biological augment*\"[Title/Abstract]) AND 1800/01/01:2020/05/15[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "76bca0342d3eb29f5dcc93f6a8ec3d16f8c2ea4e7f61cbe69850d616da316231",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The searched intervention concept names adipose-derived cells, but the text-word terms narrow this to stem, stromal, or regenerative cells. Add the bare adipose-derived cell concept."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two required concepts are combined with AND, and terms within each concept are combined with OR."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes relevant cuff, tendon, shoulder, cell, marrow, platelet, adipose, and regenerative medicine headings. The broader headings can support sensitivity."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add adipose-derived cell*[tiab] and adipose derived cell*[tiab] so coverage does not depend on the narrower cell subtypes already listed."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported PubMed query has balanced grouping, recognized field tags, no reported errors, and no translation issues."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The query restricts entry date through 2020/05/15, but the scope gives no date limit or rationale. This excludes later records and should be removed unless the protocol establishes that cutoff."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The searched intervention concept explicitly includes adipose-derived cells, but the text-word block lists only adipose-derived stem, stromal, and regenerative cells, plus fat-derived stem cells. It lacks the bare adipose-derived cell wording, so records using that general name may be missed.",
          "recommendation": "Add adipose-derived cell*[tiab] and adipose derived cell*[tiab], then rerun the complete evaluation.",
          "status": "open"
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The final query applies an entry-date range ending 2020/05/15. No publication-date or entry-date restriction is stated in the question or eligibility scope, so eligible records entered after that date are excluded.",
          "recommendation": "Remove the entry-date cutoff unless a protocol rationale establishes it; rerun the complete evaluation after changing the query.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "aa860e4c1b3744b1098f171efb85245d9f19f34c5ac1362234703594828596ca",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched intervention members are represented with their own text-word expressions, including bone marrow aspirate/concentrate, platelet-rich plasma, adipose-derived cells, and tendon-derived cells."
        },
        "operators": {
          "verdict": "pass",
          "note": "The population and intervention blocks are joined with AND; terms within each block are joined with OR. Design, outcomes, and comparator remain screening criteria as specified."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes relevant cuff, tendon, shoulder, cell, marrow, platelet, adipose, and regenerative medicine headings. The broader headings support sensitivity."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The block includes rotator cuff and named tendon terms, and intervention expressions covering the eligible biologic members."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported query has balanced grouping, recognized field tags, and no reported PubMed errors or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The Entrez entry-date bound through 2020/05/15 is required by the run harness and is documented in the packet; no publication-date cutoff is applied."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The searched intervention concept explicitly includes adipose-derived cells, but the earlier text-word block lacked the bare adipose-derived cell wording.",
          "recommendation": "Add adipose-derived cell*[tiab] and adipose derived cell*[tiab], then rerun the complete evaluation.",
          "status": "resolved",
          "response": "Both bare expressions are present in version 4. The complete evaluation reports 1,508 records, 100% retrieval of the 15 development and 6 validation records, and no known misses."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query applies an entry-date range ending 2020/05/15, which would exclude later-entered records without a protocol rationale.",
          "recommendation": "Remove the entry-date cutoff unless a protocol rationale establishes it; rerun the complete evaluation after changing the query.",
          "status": "accepted-risk",
          "response": "The packet documents that the run harness explicitly requires the PubMed Entrez-date bound 2020/05/15 on every command and forbids a publication-date cutoff. The entry-date restriction is therefore retained to comply with that constraint, and its scope is documented."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-edaaca22f54a55f9d2dc",
          "status": "accepted-risk",
          "response": "The rotator cuff category probe is stale because the block changed after the final probe and the probe budget is spent. Retain the warning for review; do not treat the earlier probe as validation of the final block.",
          "evidence": "The packet reports two earlier rotator cuff probes with 0 relevant records among 30 screened each. The cuff block itself did not change after probe 2; the probe became stale when the AND-ed intervention block later gained adipose-derived cell wording. The probe budget is exhausted. The current evaluation reports 100% retrieval of all 21 known relevant and validation records, no known misses, and no record-count regression since version 3."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "aa860e4c1b3744b1098f171efb85245d9f19f34c5ac1362234703594828596ca",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched intervention members are represented, including bare adipose-derived cell wording and the named bone marrow, platelet, and tendon-derived terms."
        },
        "operators": {
          "verdict": "pass",
          "note": "The population and intervention blocks are joined with AND, and terms within each block with OR. Design, outcomes, and comparator remain screening criteria as scoped."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes cuff, tendon, shoulder, cell, marrow, platelet, adipose, and regenerative medicine headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text-word terms cover the specified population and biologic members, including both bare adipose-derived cell expressions."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports balanced grouping, recognized field tags, and no PubMed errors or translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date bound through 2020/05/15 is documented as a run-harness requirement; no publication-date cutoff is applied. This is an accepted operational scope restriction."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "The earlier text-word block lacked bare adipose-derived cell wording despite that member being included in the searched intervention concept.",
          "recommendation": "Add adipose-derived cell*[tiab] and adipose derived cell*[tiab], then rerun the complete evaluation.",
          "status": "resolved",
          "response": "Both expressions are present in version 4. The packet reports 1,508 records, retrieval of all 15 development and 6 validation records, and no known misses."
        },
        {
          "id": "R1-02",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The query applies an entry-date range ending 2020/05/15, which would exclude later-entered records without a protocol rationale.",
          "recommendation": "Remove the entry-date cutoff unless a protocol rationale establishes it; rerun the complete evaluation after changing the query.",
          "status": "accepted-risk",
          "response": "The packet documents that the run harness requires the PubMed Entrez-date bound 2020/05/15 on every command and forbids a publication-date cutoff. The restriction is retained to comply with that constraint."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-edaaca22f54a55f9d2dc",
          "status": "accepted-risk",
          "response": "The packet identifies the rotator cuff category probe as stale because the overall strategy changed after the final probe and the probe budget is spent. The warning is retained; the earlier probes are not treated as validation of the final strategy.",
          "evidence": "The packet reports two rotator cuff probes, each with 0 relevant records among 30 screened. It says the cuff block did not change after probe 2, but the intervention block later gained adipose-derived cell wording, changing the combined query. The current evaluation reports retrieval of all 21 known relevant and validation records, no known misses, and no count regression since version 3; these finite known-record checks do not refresh the stale category probe."
        }
      ]
    }
  ]
}
```

