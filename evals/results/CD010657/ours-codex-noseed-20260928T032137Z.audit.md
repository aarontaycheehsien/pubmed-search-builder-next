# PubMed search strategy: audit

Generated 2026-09-28T03:29:45+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In children with urinary tract infection, what is the accuracy of DMSA renal scan or ultrasound for detecting vesicoureteral reflux?
- Framework: PIRD
- Scope confirmed by user: no (No known relevant articles were supplied. User asked to proceed without questions; scope roles are provisional and unconfirmed. PubMed access is bounded by the harness PSB_AS_OF=2013-01-30 environment setting (Entrez date); no publication-date limit is applied. No age, language, study-design, or other limits. Standard-depth discovery will be attempted, but records will only be added to relevant sets after screening against the stated eligibility criteria.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Vesicoureteral reflux | search | Target condition is the focus of detection and is likely named or indexed. |
| DMSA renal scan or renal/urinary ultrasound | search | The eligibility criteria name these index tests; either may be described using test-specific terminology. |
| Children with urinary tract infection | screen | Age and UTI context may be omitted from title/abstract or indexing; screen records for both. |
| Diagnostic accuracy evaluation | screen | Design and accuracy outcomes are inconsistent in bibliographic fields; screen eligible evaluations. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T03:29:13+00:00
- Records added to PubMed up to: 2013-01-30
- Total records: 1,783
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Vesico-Ureteral Reflux"[Mesh]` | 7,234 | none |
| 2 | `vesicoureteral reflux[tiab]` | 3,780 | none |
| 3 | `vesicoureteric reflux[tiab]` | 819 | none |
| 4 | `vesico-ureteral reflux[tiab]` | 1,021 | none |
| 5 | `VUR[tiab]` | 1,500 | none |
| 6 | `#1 OR #2 OR #3 OR #4 OR #5` | 8,917 | none |
| 7 | `"Technetium Tc 99m Dimercaptosuccinic Acid"[Mesh]` | 1,153 | none |
| 8 | `"Ultrasonography"[Mesh]` | 319,531 | none |
| 9 | `DMSA[tiab]` | 1,948 | none |
| 10 | `"DMSA scan"[tiab]` | 243 | none |
| 11 | `dimercaptosuccinic[tiab]` | 1,632 | none |
| 12 | `dimercaptosuccinate[tiab]` | 154 | none |
| 13 | `99mTc[tiab]` | 18,377 | none |
| 14 | `99m-Tc[tiab]` | 5,947 | none |
| 15 | `technetium-99m[tiab]` | 8,740 | none |
| 16 | `renal scintigraphy[tiab]` | 989 | none |
| 17 | `renal scan[tiab]` | 579 | none |
| 18 | `renal ultrasound[tiab]` | 814 | none |
| 19 | `urinary ultrasound[tiab]` | 9 | none |
| 20 | `ultrasound[tiab]` | 141,762 | none |
| 21 | `ultrasonography[tiab]` | 60,748 | none |
| 22 | `sonography[tiab]` | 25,960 | none |
| 23 | `echography[tiab]` | 5,260 | none |
| 24 | `#7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23` | 429,684 | none |
| 25 | `#6 AND #24` | 1,783 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Vesico-Ureteral Reflux"[Mesh] OR vesicoureteral reflux[tiab] OR vesicoureteric reflux[tiab] OR vesico-ureteral reflux[tiab] OR VUR[tiab]) AND ("Technetium Tc 99m Dimercaptosuccinic Acid"[Mesh] OR "Ultrasonography"[Mesh] OR DMSA[tiab] OR "DMSA scan"[tiab] OR dimercaptosuccinic[tiab] OR dimercaptosuccinate[tiab] OR 99mTc[tiab] OR 99m-Tc[tiab] OR technetium-99m[tiab] OR renal scintigraphy[tiab] OR renal scan[tiab] OR renal ultrasound[tiab] OR urinary ultrasound[tiab] OR ultrasound[tiab] OR ultrasonography[tiab] OR sonography[tiab] OR echography[tiab])) AND ("1800/01/01"[edat] : "2013/01/30"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 4 | 4 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| reflux | 429,684 | 0 |
| test | 8,917 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,783 | initial | none | Initial PIRD draft: searched target condition and either index-test family; screened age, UTI context, and accuracy design. Used MeSH plus text vocabulary and terms from two screened discovery records. No publication-date limit; harness Entrez cutoff applied through PSB_AS_OF. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 435 NCBI requests logged (205 from cache); strategy sha256 0ab30f5e9a5d._

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
      "checked_at": "2026-09-28T03:29:13+00:00",
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
      "checked_at": "2026-09-28T03:29:13+00:00",
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
      "location": "vocabulary:6",
      "term": {
        "text": "\"Technetium Tc 99m Dimercaptosuccinic Acid\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Ultrasonography",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T03:29:13+00:00",
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
      "location": "vocabulary:7",
      "term": {
        "text": "\"Ultrasonography\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Vesico-Ureteral Reflux\"[MeSH Terms] OR \"vesicoureteral reflux\"[Title/Abstract] OR \"vesicoureteric reflux\"[Title/Abstract] OR \"Vesico-Ureteral Reflux\"[Title/Abstract] OR \"VUR\"[Title/Abstract]) AND (\"Technetium Tc 99m Dimercaptosuccinic Acid\"[MeSH Terms] OR \"Ultrasonography\"[MeSH Terms] OR \"DMSA\"[Title/Abstract] OR \"DMSA scan\"[Title/Abstract] OR \"dimercaptosuccinic\"[Title/Abstract] OR \"dimercaptosuccinate\"[Title/Abstract] OR \"99mTc\"[Title/Abstract] OR \"99m-Tc\"[Title/Abstract] OR \"technetium-99m\"[Title/Abstract] OR \"renal scintigraphy\"[Title/Abstract] OR \"renal scan\"[Title/Abstract] OR \"renal ultrasound\"[Title/Abstract] OR \"urinary ultrasound\"[Title/Abstract] OR \"ultrasound\"[Title/Abstract] OR \"Ultrasonography\"[Title/Abstract] OR \"sonography\"[Title/Abstract] OR \"echography\"[Title/Abstract]) AND 1800/01/01:2013/01/30[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "6db98be1d74b2d63c987cd9c4badbba65c7fb76db0bf84ecf81153172a586530",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The supplied PubMed translations preserve the intended MeSH and title/abstract fields. No translation warnings or syntax errors are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "The target condition and either index-test block are combined with AND, while synonyms and the two test types are combined with OR. This matches the stated search roles."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The supplied evidence verifies the reflux, DMSA, and ultrasonography descriptors. Omitting age, UTI, and diagnostic-accuracy headings is consistent with screening those concepts."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The text words cover the named target condition and both index tests, including bare DMSA and ultrasound terms alongside more specific expressions. No phrase warning or wildcard issue is shown."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The Boolean combination and field tags are valid in the supplied PubMed run; lint and raw diagnostics report no issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age, language, or study-design filters are applied, consistent with the protocol's screening plan. The entry-date boundary is documented as the harness cutoff, not as a publication-date limit."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```

