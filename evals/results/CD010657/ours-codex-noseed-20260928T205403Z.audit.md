# PubMed search strategy: audit

Generated 2026-09-28T21:16:30+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In children with urinary tract infection, what is the accuracy of DMSA renal scan or ultrasound for detecting vesicoureteral reflux?
- Framework: PIRD
- Scope confirmed by user: no (User asked to proceed without questions, so the roles and screening interpretation are documented assumptions rather than user-confirmed scope. No user-supplied records. The related review PMID 15769296 and screened records from a precise pilot supplied development and benchmark records. Harness supplies PSB_AS_OF=2013-01-30 for every psb command; no publication-date limit added.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Vesicoureteral reflux | search | Target condition in a diagnostic-accuracy question; reliably indexed and named, so required as a core block. |
| DMSA renal scan or renal/urinary ultrasound | search | The two named index-test families define the review and are searchable in titles, abstracts, or indexing; both members must be represented. |
| Children with urinary tract infection | screen | Age and UTI context may be incompletely named or indexed; assess eligibility at screening. |
| Diagnostic evaluation / accuracy | screen | Accuracy terminology and eligible evaluation design are inconsistently reported; do not require an accuracy or study-design label. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T21:16:09+00:00
- Records added to PubMed up to: 2013-01-30
- Total records: 2,050
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Vesico-Ureteral Reflux[Mesh]` | 7,234 | none |
| 2 | `vesicoureteral reflux[tiab]` | 3,780 | none |
| 3 | `vesicoureteric reflux[tiab]` | 819 | none |
| 4 | `vesico-ureteral reflux[tiab]` | 1,021 | none |
| 5 | `vesico-ureteric reflux[tiab]` | 456 | none |
| 6 | `VUR[tiab]` | 1,500 | none |
| 7 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6` | 9,000 | none |
| 8 | `Technetium Tc 99m Dimercaptosuccinic Acid[Mesh]` | 1,153 | none |
| 9 | `Radionuclide Imaging[Mesh]` | 165,890 | none |
| 10 | `Ultrasonography[Mesh]` | 319,531 | none |
| 11 | `DMSA[tiab]` | 1,948 | none |
| 12 | `dimercaptosuccinic[tiab]` | 1,632 | none |
| 13 | `ultrasound[tiab]` | 141,762 | none |
| 14 | `ultrasonograph*[tiab]` | 73,208 | none |
| 15 | `sonograph*[tiab]` | 41,566 | none |
| 16 | `#8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15` | 560,428 | none |
| 17 | `#7 AND #16` | 2,050 | none |

### Strategy (single line, for copying into PubMed)

```text
((Vesico-Ureteral Reflux[Mesh] OR vesicoureteral reflux[tiab] OR vesicoureteric reflux[tiab] OR vesico-ureteral reflux[tiab] OR vesico-ureteric reflux[tiab] OR VUR[tiab]) AND (Technetium Tc 99m Dimercaptosuccinic Acid[Mesh] OR Radionuclide Imaging[Mesh] OR Ultrasonography[Mesh] OR DMSA[tiab] OR dimercaptosuccinic[tiab] OR ultrasound[tiab] OR ultrasonograph*[tiab] OR sonograph*[tiab])) AND ("1800/01/01"[edat] : "2013/01/30"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 2 | 2 | 100.0% |
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 9 | 9 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| DMSA renal scan or renal/urinary ultrasound | 1 | `(scan[tiab] OR imaging[tiab] OR scintigraph*[tiab] OR Diagnostic Imaging[Mesh] OR renal ultrasound[tiab] OR kidney ultrasound[tiab])` | 1,953 | 0/30 |
| DMSA renal scan or renal/urinary ultrasound | 2 | `(scan[tiab] OR imaging[tiab] OR scintigraph*[tiab] OR Diagnostic Imaging[Mesh] OR renal ultrasound[tiab] OR kidney ultrasound[tiab])` | 1,952 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| reflux | 560,428 | 0 |
| index_test | 9,000 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial two-block PIRD strategy: VUR and the named DMSA/ultrasound index-test families; age, UTI context, and diagnostic design screened. No limits. |
| 2 | 2,050 | reflux: +6 / -0; index_test: +8 / -0 | none | Initial two-block PIRD strategy: VUR and the named DMSA/ultrasound index-test families; age, UTI context, and diagnostic design screened. No limits. |
| 3 | 2,054 | index_test: +1 / -0 | none | Added the verified historical MeSH term Succimer to the DMSA index-test layer because NCBI reports it as a prior indexing heading for Tc-99m DMSA; retain broad Radionuclide Imaging for unindexed wording/indexing variation. |
| 4 | 2,050 | index_test: +0 / -1 | none | Removed Succimer[Mesh] after testing its unique retrieval: the only four records retrieved by that heading in the VUR block were unrelated to DMSA renal imaging. No known relevant record was lost; the narrower current query is re-evaluated. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3: 2 findings; F1 should-fix open, F2 should-fix open
- Round 2 on version 4: 2 findings; F1 should-fix resolved, F2 should-fix resolved
- Round 3 on version 4: 2 findings; F1 should-fix resolved, F2 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 529 NCBI requests logged (302 from cache); strategy sha256 55686ed97601._

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
        "location": "concept:index_test",
        "blocking": false,
        "requires_review": true,
        "id": "I-73a2f366c37cd8b41709"
      }
    ],
    "issues": [
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:index_test",
        "blocking": false,
        "requires_review": true,
        "id": "I-73a2f366c37cd8b41709"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Vesico-Ureteral Reflux",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:16:09+00:00",
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
        "text": "Vesico-Ureteral Reflux",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Technetium Tc 99m Dimercaptosuccinic Acid",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:16:09+00:00",
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
        "text": "Technetium Tc 99m Dimercaptosuccinic Acid",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Radionuclide Imaging",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:16:09+00:00",
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
      "location": "vocabulary:8",
      "term": {
        "text": "Radionuclide Imaging",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Ultrasonography",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:16:09+00:00",
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
      "location": "vocabulary:9",
      "term": {
        "text": "Ultrasonography",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"vesico ureteral reflux\"[MeSH Terms] OR \"vesicoureteral reflux\"[Title/Abstract] OR \"vesicoureteric reflux\"[Title/Abstract] OR \"vesico ureteral reflux\"[Title/Abstract] OR \"vesico ureteric reflux\"[Title/Abstract] OR \"VUR\"[Title/Abstract]) AND (\"technetium tc 99m dimercaptosuccinic acid\"[MeSH Terms] OR \"radionuclide imaging\"[MeSH Terms] OR \"ultrasonography\"[MeSH Terms] OR \"DMSA\"[Title/Abstract] OR \"dimercaptosuccinic\"[Title/Abstract] OR \"ultrasound\"[Title/Abstract] OR \"ultrasonograph*\"[Title/Abstract] OR \"sonograph*\"[Title/Abstract]) AND 1800/01/01:2013/01/30[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "43874fadbd91bd048e3a772217dbd7f25c5f1de35d227db16a9bc8bcd2f2d393",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The reflux variants cover the named condition, and DMSA and ultrasound each appear as bare title/abstract terms. The listed MeSH translations have no reported errors or warnings."
        },
        "operators": {
          "verdict": "revise",
          "note": "The main blocks are combined clearly with OR within concepts and AND across concepts. The first category probe did not exclude the later-added Succimer[Mesh] term."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "The exact Technetium Tc 99m Dimercaptosuccinic Acid heading is verified. The relevance of Succimer[Mesh] was not demonstrated in this draft."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The DMSA and ultrasound families are each represented by unqualified text-word terms, with additional spelling and morphology coverage. No phrase warning is reported."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed PubMed expressions have balanced grouping, recognized field tags, and no reported errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No review eligibility limits are applied. The harness adds an entry-date cutoff through 2013-01-30; no publication-date limit is used."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Succimer[Mesh] is included in the index-test block, but the packet does not show that it retrieves relevant Tc-99m DMSA renal-scan records.",
          "recommendation": "Check unique retrieval and relevant records; document evidence or remove it and rerun evaluation.",
          "status": "open"
        },
        {
          "id": "F2",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The category-probe NOT clause omitted Succimer[Mesh], so the sample was not demonstrably outside the then-current index-test block.",
          "recommendation": "Rerun the probe with the current block excluded and screen the sample.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 4,
      "review_sha256": "29038227afa4228d87dcf4b43b26581c79c37d746db8d4b09e1ba0ff6a66ff5d",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The displayed PubMed translations report no errors or warnings. The named reflux, DMSA, and ultrasound concepts are represented with the listed MeSH headings and title/abstract terms."
        },
        "operators": {
          "verdict": "pass",
          "note": "The strategy uses OR within each concept block and AND between the reflux and index-test blocks. Probe 1 excluded the current index-test terms and screened 30 records with none relevant; finding F2 is resolved."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The exact Technetium Tc 99m Dimercaptosuccinic Acid heading is verified. Succimer[Mesh], whose relevance was not demonstrated, is absent from the current block; finding F1 is resolved."
        },
        "text_words": {
          "verdict": "pass",
          "note": "DMSA and ultrasound each appear as bare title/abstract terms, with additional spelling or morphology coverage. The strategy does not rely on a phrase narrowed by parent wording."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed expressions have balanced grouping, recognized field tags, and no reported PubMed errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No eligibility limits are applied. The documented entry-date cutoff through 2013-01-30 is supplied by the harness; no publication-date limit is used."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Succimer[Mesh] was included without evidence that it retrieved relevant Tc-99m DMSA renal-scan records.",
          "recommendation": "Remove the unsupported heading or document its unique relevant retrieval and rerun evaluation.",
          "status": "resolved",
          "response": "Succimer[Mesh] is absent from the current index-test block. The current strategy evaluation is recorded at version 4."
        },
        {
          "id": "F2",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The category-probe NOT clause omitted Succimer[Mesh], so that probe did not establish records outside the then-current index-test block.",
          "recommendation": "Rerun a probe excluding the current block and screen its sample.",
          "status": "resolved",
          "response": "Probe 1 excludes the same index-test terms listed in the current block, uses the documented broader query, and screened all 30 sampled records with none relevant."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-73a2f366c37cd8b41709",
          "status": "rejected",
          "response": "The stale-probe warning does not apply to the current block: probe 1 was screened against the same index-test terms now in the strategy. Probe 2 became stale after Succimer[Mesh] was removed, but probe 1 provides evidence for the current block.",
          "evidence": "Probe 1 excludes Technetium Tc 99m Dimercaptosuccinic Acid[Mesh], Radionuclide Imaging[Mesh], Ultrasonography[Mesh], DMSA[tiab], dimercaptosuccinic[tiab], ultrasound[tiab], ultrasonograph*[tiab], and sonograph*[tiab]—the current block's terms. It screened 30 sampled records and found 0 relevant. Probe 2 excluded the additionally removed Succimer[Mesh] and also found 0 relevant, but is stale for the current block."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 4,
      "review_sha256": "29038227afa4228d87dcf4b43b26581c79c37d746db8d4b09e1ba0ff6a66ff5d",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The named reflux, DMSA, and ultrasound concepts are covered by the displayed MeSH headings and title/abstract terms. The current evaluation reports no translation errors."
        },
        "operators": {
          "verdict": "pass",
          "note": "The strategy uses OR within concept blocks and AND between them. Probe 1 excludes the current index-test terms and screened 30 records with none relevant, resolving F2."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The exact Technetium Tc 99m Dimercaptosuccinic Acid heading is included. Succimer[Mesh] is absent, resolving F1."
        },
        "text_words": {
          "verdict": "pass",
          "note": "DMSA and ultrasound each appear as bare title/abstract terms, with additional spelling or morphology variants."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The displayed expressions have balanced grouping and recognized field tags, with no reported PubMed errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No eligibility limits are applied. The documented entry-date cutoff through 2013-01-30 is supplied by the harness; no publication-date limit is used."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Succimer[Mesh] was included without evidence that it retrieved relevant Tc-99m DMSA renal-scan records.",
          "recommendation": "Remove the unsupported heading or document its unique relevant retrieval and rerun evaluation.",
          "status": "resolved",
          "response": "Succimer[Mesh] is absent from the current index-test block. The current strategy evaluation is recorded at version 4."
        },
        {
          "id": "F2",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The category-probe NOT clause omitted Succimer[Mesh], so that probe did not establish records outside the then-current index-test block.",
          "recommendation": "Rerun a probe excluding the current block and screen its sample.",
          "status": "resolved",
          "response": "Probe 1 excludes the same index-test terms listed in the current block, uses the documented broader query, and screened all 30 sampled records with none relevant."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-73a2f366c37cd8b41709",
          "status": "rejected",
          "response": "The stale-probe warning does not undermine evidence for the current block: probe 1 was screened against the same index-test terms now in the strategy. Probe 2 became stale after Succimer[Mesh] was removed.",
          "evidence": "Probe 1 excludes all eight current index-test terms and screened 30 sampled records with 0 relevant. Probe 2 excluded the additionally removed Succimer[Mesh] and also found 0 relevant, but is stale for the current block."
        }
      ]
    }
  ]
}
```

