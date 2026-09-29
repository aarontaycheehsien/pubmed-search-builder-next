# PubMed search strategy: audit

Generated 2026-09-28T21:34:18+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In children with urinary tract infection, how accurate are DMSA scans and ultrasound for detecting vesicoureteral reflux?
- Framework: PIRD
- Scope confirmed by user: no (No known relevant articles were supplied. User asked to proceed without questions; roles and eligibility are assumed from the stated question and criteria. PubMed is bounded by Entrez date through 2013-01-30 via PSB_AS_OF; no publication-date limit is applied.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Vesicoureteral reflux | search | Target condition that defines the diagnostic question and is expected to be named or indexed. |
| DMSA renal scan or renal/urinary ultrasound | search | The two eligible index tests are explicitly named in the question and form the diagnostic focus. |
| Children with urinary tract infection | screen | Age and UTI context can be incompletely reported in abstracts; apply eligibility at screening. |
| Diagnostic accuracy or screening outcomes | screen | Accuracy language and eligible diagnostic evaluation are inconsistently named; do not require accuracy terms. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T21:33:48+00:00
- Records added to PubMed up to: 2013-01-30
- Total records: 2,043
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Vesico-Ureteral Reflux"[Mesh]` | 7,234 | none |
| 2 | `"vesicoureteral reflux"[tiab]` | 3,780 | none |
| 3 | `"vesico-ureteral reflux"[tiab]` | 1,021 | none |
| 4 | `"vesicoureteric reflux"[tiab]` | 819 | none |
| 5 | `"vesico-ureteric reflux"[tiab]` | 456 | none |
| 6 | `VUR[tiab]` | 1,500 | none |
| 7 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6` | 9,000 | none |
| 8 | `"Technetium Tc 99m Dimercaptosuccinic Acid"[Mesh]` | 1,153 | none |
| 9 | `"Ultrasonography"[Mesh]` | 319,531 | none |
| 10 | `"Radionuclide Imaging"[Mesh]` | 165,890 | none |
| 11 | `DMSA[tiab]` | 1,948 | none |
| 12 | `"dimercaptosuccinic acid"[tiab]` | 1,492 | none |
| 13 | `"dimercaptosuccinate"[tiab]` | 154 | none |
| 14 | `"renal scintigraphy"[tiab]` | 989 | none |
| 15 | `renal scintigraph*[tiab]` | 1,024 | none |
| 16 | `ultrasound[tiab]` | 141,762 | none |
| 17 | `ultrasonograph*[tiab]` | 73,208 | none |
| 18 | `sonograph*[tiab]` | 41,566 | none |
| 19 | `echograph*[tiab]` | 8,470 | none |
| 20 | `"renal ultrasound"[tiab]` | 814 | none |
| 21 | `"renal ultrasonography"[tiab]` | 568 | none |
| 22 | `"urinary tract ultrasound"[tiab]` | 39 | none |
| 23 | `"voiding urosonography"[tiab]` | 52 | none |
| 24 | `cystosonograph*[tiab]` | 25 | none |
| 25 | `#8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24` | 562,726 | none |
| 26 | `#7 AND #25` | 2,043 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Vesico-Ureteral Reflux"[Mesh] OR "vesicoureteral reflux"[tiab] OR "vesico-ureteral reflux"[tiab] OR "vesicoureteric reflux"[tiab] OR "vesico-ureteric reflux"[tiab] OR VUR[tiab]) AND ("Technetium Tc 99m Dimercaptosuccinic Acid"[Mesh] OR "Ultrasonography"[Mesh] OR "Radionuclide Imaging"[Mesh] OR DMSA[tiab] OR "dimercaptosuccinic acid"[tiab] OR "dimercaptosuccinate"[tiab] OR "renal scintigraphy"[tiab] OR renal scintigraph*[tiab] OR ultrasound[tiab] OR ultrasonograph*[tiab] OR sonograph*[tiab] OR echograph*[tiab] OR "renal ultrasound"[tiab] OR "renal ultrasonography"[tiab] OR "urinary tract ultrasound"[tiab] OR "voiding urosonography"[tiab] OR cystosonograph*[tiab])) AND ("1800/01/01"[edat] : "2013/01/30"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 5 | 5 | 100.0% |
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 8 | 8 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 2 | 2 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| reflux | 562,726 | 0 |
| index_test | 9,000 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 2,043 | initial | none | Initial PIRD strategy: searched vesicoureteral reflux and DMSA/ultrasound terms; child/UTI context and accuracy design screened. Added MeSH plus broad text terms, including historical radionuclide imaging indexing. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 0 findings; 
- Round 2 on version 1: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 283 NCBI requests logged (92 from cache); strategy sha256 b1fa857f031b._

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
      "requested": "Vesico-Ureteral Reflux",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:33:48+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D014718",
          "name": "Vesico-Ureteral Reflux",
          "type": "descriptor",
          "scope_note": "Retrograde flow of urine from the URINARY BLADDER into the URETER. This is often due to incompetence of the vesicoureteral valve.",
          "tree_numbers": [
            "C12.050.351.968.829.920",
            "C12.200.777.829.920",
            "C12.950.829.920"
          ],
          "entry_terms": 16,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D014718",
      "preferred_label": "Vesico-Ureteral Reflux",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"Vesico-Ureteral Reflux\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Technetium Tc 99m Dimercaptosuccinic Acid",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:33:48+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D019783",
          "name": "Technetium Tc 99m Dimercaptosuccinic Acid",
          "type": "descriptor",
          "scope_note": "A nontoxic radiopharmaceutical that is used in the diagnostic imaging of the renal cortex.",
          "tree_numbers": [
            "D02.241.081.337.759.500.725",
            "D02.691.825.468",
            "D02.886.489.750.725"
          ],
          "entry_terms": 22,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D019783",
      "preferred_label": "Technetium Tc 99m Dimercaptosuccinic Acid",
      "type": "descriptor",
      "location": "vocabulary:7",
      "term": {
        "text": "\"Technetium Tc 99m Dimercaptosuccinic Acid\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Ultrasonography",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:33:48+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D014463",
          "name": "Ultrasonography",
          "type": "descriptor",
          "scope_note": "The visualization of deep structures of the body by recording the reflections or echoes of ultrasonic pulses directed into the tissues. Use of ultrasound for imaging or diagnostic purposes employs frequencies ranging from 1.6 to 10 megahertz.",
          "tree_numbers": [
            "E01.370.350.850"
          ],
          "entry_terms": 25,
          "mapped_to": null
        },
        {
          "ui": "Q000000981",
          "name": "diagnostic imaging",
          "type": "qualifier",
          "scope_note": "Used for the visualization of an anatomical structure or for the diagnosis of disease. Commonly used imaging techniques include radiography, radionuclide imaging, thermography, tomography, and ultrasonography",
          "tree_numbers": [
            "Y04.010"
          ],
          "entry_terms": 12,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D014463",
      "preferred_label": "Ultrasonography",
      "type": "descriptor",
      "location": "vocabulary:8",
      "term": {
        "text": "\"Ultrasonography\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Radionuclide Imaging",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:33:48+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011877",
          "name": "Radionuclide Imaging",
          "type": "descriptor",
          "scope_note": "The production of an image obtained by cameras that detect the radioactive emissions of an injected radionuclide as it has distributed differentially throughout tissues in the body. The image obtained from a moving detector is called a scan, while the image obtained from a stationary camera device is called a scintiphotograph.",
          "tree_numbers": [
            "E01.370.350.710",
            "E01.370.384.730"
          ],
          "entry_terms": 7,
          "mapped_to": null
        },
        {
          "ui": "Q000000981",
          "name": "diagnostic imaging",
          "type": "qualifier",
          "scope_note": "Used for the visualization of an anatomical structure or for the diagnosis of disease. Commonly used imaging techniques include radiography, radionuclide imaging, thermography, tomography, and ultrasonography",
          "tree_numbers": [
            "Y04.010"
          ],
          "entry_terms": 12,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011877",
      "preferred_label": "Radionuclide Imaging",
      "type": "descriptor",
      "location": "vocabulary:9",
      "term": {
        "text": "\"Radionuclide Imaging\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"vesico ureteral reflux\"[MeSH Terms] OR \"vesicoureteral reflux\"[Title/Abstract] OR \"vesico ureteral reflux\"[Title/Abstract] OR \"vesicoureteric reflux\"[Title/Abstract] OR \"vesico-ureteric reflux\"[Title/Abstract] OR \"VUR\"[Title/Abstract]) AND (\"Technetium Tc 99m Dimercaptosuccinic Acid\"[MeSH Terms] OR \"Ultrasonography\"[MeSH Terms] OR \"Radionuclide Imaging\"[MeSH Terms] OR \"DMSA\"[Title/Abstract] OR \"dimercaptosuccinic acid\"[Title/Abstract] OR \"dimercaptosuccinate\"[Title/Abstract] OR \"renal scintigraphy\"[Title/Abstract] OR \"renal scintigraph*\"[Title/Abstract] OR \"ultrasound\"[Title/Abstract] OR \"ultrasonograph*\"[Title/Abstract] OR \"sonograph*\"[Title/Abstract] OR \"echograph*\"[Title/Abstract] OR \"renal ultrasound\"[Title/Abstract] OR \"renal ultrasonography\"[Title/Abstract] OR \"urinary tract ultrasound\"[Title/Abstract] OR \"voiding urosonography\"[Title/Abstract] OR \"cystosonograph*\"[Title/Abstract]) AND 1800/01/01:2013/01/30[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "884be0271ae12f2c427fda1060b8553153cee4ebc3fc725445ba0cf83b7a8e2f",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The reflux and index-test concepts are represented in the translated query. DMSA and ultrasound each appear by their own bare name; neither is searched only in a phrase narrowed by a parent concept. Population and accuracy remain screening criteria as specified."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are combined with OR within each concept, and the reflux and index-test blocks are combined with AND. The supplied benchmark and relevant records are all retrieved."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy uses the verified Vesico-Ureteral Reflux, DMSA, Ultrasonography, and Radionuclide Imaging headings. No heading translation errors are reported."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Free-text terms cover the supplied reflux spellings and abbreviation, DMSA terminology, renal scintigraphy, and ultrasound terminology, including renal and urinary phrases. No known records are missed."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed strategy has balanced concept groups and valid PubMed field tags and Boolean operators. No syntax or translation issues are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No population, accuracy, or study-design filter narrows retrieval. The entry-date bound through 2013-01-30 is documented as the requested as-of boundary, and the known records are retrieved."
        }
      },
      "findings": [],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 1,
      "review_sha256": "1c3b24347f403f35219529b1371f9df07923704b0e70a4f9c3bfbe2d5a63739b",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Both searched concepts appear in the translated query. DMSA and ultrasound have bare-name terms, and population and diagnostic-accuracy criteria remain for screening as specified."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms are combined with OR within each concept, and the reflux and index-test blocks are combined with AND. All supplied benchmark, relevant, and held-out validation records are retrieved."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The MeSH headings for reflux, DMSA, ultrasonography, and radionuclide imaging are verified, with no reported heading translation errors."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Free-text terms cover reflux spellings and abbreviation, DMSA terminology, renal scintigraphy, and ultrasound terminology. No known records are missed."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query has balanced concept groups and valid PubMed field tags and Boolean operators. No syntax or translation issues are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No population, accuracy, or study-design filter narrows retrieval. The entry-date bound through 2013-01-30 is documented as the as-of boundary. Earlier round 1 had no findings to carry forward."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```

