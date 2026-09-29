# PubMed search strategy: audit

Generated 2026-09-28T20:53:29+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In children with urinary tract infection, what is the accuracy of DMSA renal scan or ultrasound for detecting vesicoureteral reflux?
- Framework: PIRD
- Scope confirmed by user: yes (Scope roles proceed on the user's instruction not to pause: DMSA and ultrasound are treated as alternative searchable index-test members; child/UTI and accuracy/reference-standard eligibility are screened. No language or publication-date limits. No user-supplied seeds. Standard-depth prior-review/pilot discovery attempted. PSB_AS_OF is set to 2013-01-30 for every command; no [dp] limit is used.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Vesicoureteral reflux | search | The target condition defines the diagnostic question and is reliably named or indexed. |
| DMSA renal scan or renal/urinary ultrasound | search | Both named index tests are explicit eligibility criteria and are searchable concepts. |
| Children with urinary tract infection | screen | Age and UTI context may be absent from titles/abstracts; screen eligibility without an age or infection filter. |
| Diagnostic accuracy / reference standard | screen | Accuracy and reference-standard terminology is inconsistently reported; assess eligible diagnostic evaluation during screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T20:53:01+00:00
- Records added to PubMed up to: 2013-01-30
- Total records: 2,080
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Vesico-Ureteral Reflux"[Mesh]` | 7,234 | none |
| 2 | `"vesicoureteral reflux"[tiab]` | 3,780 | none |
| 3 | `"vesicoureteric reflux"[tiab]` | 819 | none |
| 4 | `"vesico-ureteral reflux"[tiab]` | 1,021 | none |
| 5 | `"ureteral reflux"[tiab]` | 1,228 | none |
| 6 | `"ureteric reflux"[tiab]` | 530 | none |
| 7 | `VUR[tiab]` | 1,500 | none |
| 8 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7` | 9,144 | none |
| 9 | `"Technetium Tc 99m Dimercaptosuccinic Acid"[Mesh]` | 1,153 | none |
| 10 | `"Radionuclide Imaging"[Mesh]` | 165,890 | none |
| 11 | `"dimercaptosuccinic acid"[tiab]` | 1,492 | none |
| 12 | `DMSA[tiab]` | 1,948 | none |
| 13 | `"Tc-99m"[tiab]` | 7,010 | none |
| 14 | `"renal scan"[tiab]` | 579 | none |
| 15 | `"renal scintigraphy"[tiab]` | 989 | none |
| 16 | `"Ultrasonography"[Mesh]` | 319,531 | none |
| 17 | `ultrasonograph*[tiab]` | 73,208 | none |
| 18 | `ultrasound[tiab]` | 141,762 | none |
| 19 | `sonograph*[tiab]` | 41,566 | none |
| 20 | `echograph*[tiab]` | 8,470 | none |
| 21 | `dimercaptosuccinate[tiab]` | 154 | none |
| 22 | `"DMSA scan"[tiab]` | 243 | none |
| 23 | `"renal US"[tiab]` | 65 | none |
| 24 | `#9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23` | 563,771 | none |
| 25 | `#8 AND #24` | 2,080 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Vesico-Ureteral Reflux"[Mesh] OR "vesicoureteral reflux"[tiab] OR "vesicoureteric reflux"[tiab] OR "vesico-ureteral reflux"[tiab] OR "ureteral reflux"[tiab] OR "ureteric reflux"[tiab] OR VUR[tiab]) AND ("Technetium Tc 99m Dimercaptosuccinic Acid"[Mesh] OR "Radionuclide Imaging"[Mesh] OR "dimercaptosuccinic acid"[tiab] OR DMSA[tiab] OR "Tc-99m"[tiab] OR "renal scan"[tiab] OR "renal scintigraphy"[tiab] OR "Ultrasonography"[Mesh] OR ultrasonograph*[tiab] OR ultrasound[tiab] OR sonograph*[tiab] OR echograph*[tiab] OR dimercaptosuccinate[tiab] OR "DMSA scan"[tiab] OR "renal US"[tiab])) AND ("1800/01/01"[edat] : "2013/01/30"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 3 | 3 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| reflux | 563,771 | 0 |
| index_tests | 9,144 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 2,077 | initial | none | Initial broad two-block PIRD draft. Target reflux and either stated index test are searched; child/UTI population and diagnostic accuracy/reference-standard details remain screening criteria. No known relevant seeds. |
| 2 | 2,080 | index_tests: +4 / -0 | none | Critic round 1 recommended broader DMSA morphology and contextual ultrasound abbreviation coverage; added dimercaptosuccinate, DMSA scan, renal US, and urinary US text variants. |
| 3 | 2,080 | index_tests: +0 / -1 | none | Removed the unsupported zero-hit quoted phrase 'urinary US' after PubMed reported phrase-index absence and zero records. The broader ultrasound layer plus renal US wording remains; all three relevant pilot records must remain retrieved. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 1 (Same-context critic: fresh-context reviewer unavailable (Claude CLI requires login).): 1 findings; text-us-acronym should-fix open
- Round 2 on version 3 (Same-context critic: fresh-context reviewer unavailable (Claude CLI requires login). This round reviews the intended delivery strategy after all planned changes.): 2 findings; text-us-acronym should-fix resolved, empirical-validation-limit document accepted-risk
- Round 3 on version 3 (Same-context closing critic: verifies the earlier lexical revision and documented empirical-validation limitation. Fresh-context review was unavailable because Claude CLI requires login.): 2 findings; text-us-acronym should-fix resolved, empirical-validation-limit document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 369 NCBI requests logged (148 from cache); strategy sha256 bc7e29216bde._

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
      "checked_at": "2026-09-28T20:53:01+00:00",
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
      "checked_at": "2026-09-28T20:53:01+00:00",
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
      "location": "vocabulary:8",
      "term": {
        "text": "\"Technetium Tc 99m Dimercaptosuccinic Acid\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Radionuclide Imaging",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T20:53:01+00:00",
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
    },
    {
      "requested": "Ultrasonography",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T20:53:01+00:00",
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
      "location": "vocabulary:15",
      "term": {
        "text": "\"Ultrasonography\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"vesico ureteral reflux\"[MeSH Terms] OR \"vesicoureteral reflux\"[Title/Abstract] OR \"vesicoureteric reflux\"[Title/Abstract] OR \"vesico ureteral reflux\"[Title/Abstract] OR \"ureteral reflux\"[Title/Abstract] OR \"ureteric reflux\"[Title/Abstract] OR \"VUR\"[Title/Abstract]) AND (\"Technetium Tc 99m Dimercaptosuccinic Acid\"[MeSH Terms] OR \"Radionuclide Imaging\"[MeSH Terms] OR \"dimercaptosuccinic acid\"[Title/Abstract] OR \"DMSA\"[Title/Abstract] OR \"Tc-99m\"[Title/Abstract] OR \"renal scan\"[Title/Abstract] OR \"renal scintigraphy\"[Title/Abstract] OR \"Ultrasonography\"[MeSH Terms] OR \"ultrasonograph*\"[Title/Abstract] OR \"ultrasound\"[Title/Abstract] OR \"sonograph*\"[Title/Abstract] OR \"echograph*\"[Title/Abstract] OR \"dimercaptosuccinate\"[Title/Abstract] OR \"DMSA scan\"[Title/Abstract] OR \"renal US\"[Title/Abstract]) AND 1800/01/01:2013/01/30[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 1,
      "review_sha256": "b02a4be913805818ef68d63c5f75781dc8750e006d1c7c7247f07ff361705286",
      "note": "Same-context critic: fresh-context reviewer unavailable (Claude CLI requires login).",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "PIRD roles align with the question; reflux AND either named index test are searched, with population and accuracy details screened."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR alternatives are grouped within each concept and the two concepts are ANDed; no NOT or proximity terms."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Verified Vesico-Ureteral Reflux, Technetium Tc 99m Dimercaptosuccinic Acid, Radionuclide Imaging and Ultrasonography headings are relevant; MeSH explosion is retained."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add common DMSA scan wording and contextual renal/urinary US acronym variants, which could occur in unindexed records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All terms are explicitly tagged; no phrase-index, truncation or syntax diagnostics."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No arbitrary age, language, publication-date or design limits; the Entrez cutoff is controlled separately by the protocol."
        }
      },
      "findings": [
        {
          "id": "text-us-acronym",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "index_tests",
          "finding": "The text layer does not explicitly cover common DMSA scan forms such as dimercaptosuccinate or contextual abbreviated renal/urinary US wording, potentially reducing retrieval among unindexed records.",
          "recommendation": "Add a dimercaptosuccinate variant and contextual renal/urinary US wording; re-evaluate and inspect line counts and translation.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "7dfbf976732c12149ca795840fecc75dfc924510806c4a8b3fba2974ca899665",
      "note": "Same-context critic: fresh-context reviewer unavailable (Claude CLI requires login). This round reviews the intended delivery strategy after all planned changes.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Two-block diagnostic search remains faithful to PIRD; UTI and pediatric eligibility remain at screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "Concept alternatives are ORed and the target condition is ANDed with either test family; no exclusion logic."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Verified MeSH headings cover reflux, specific DMSA agent, broad radionuclide imaging and ultrasonography. Explosion stays on."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Added dimercaptosuccinate, DMSA scan and renal US. Removed urinary US after PubMed phrase-index warning and zero hits. Final current evaluation has no phrase warnings."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Current terms are explicitly field-tagged and lint has no issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age, language, publication-date or study-design filter. Entry-date cutoff is explicit and not a [dp] limit."
        }
      },
      "findings": [
        {
          "id": "text-us-acronym",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "index_tests",
          "finding": "The text layer did not explicitly cover common DMSA scan forms and contextual renal/urinary US wording.",
          "recommendation": "Add useful variants and re-evaluate.",
          "status": "resolved",
          "response": "Added dimercaptosuccinate[tiab], \"DMSA scan\"[tiab], and \"renal US\"[tiab]. Evaluation grew from 2,077 to 2,080 records after additions, all three development records remained retrieved (100% relative recall against the screened pilot set), with no known losses. The proposed \"urinary US\" phrase generated PubMed phrase-index absence and zero-hit diagnostics, so it was removed and re-evaluated. Current evaluation is complete with no validation blockers or review-required issues."
        },
        {
          "id": "empirical-validation-limit",
          "domain": "translation",
          "severity": "document",
          "kind": "reporting",
          "finding": "Only three pilot discoveries form the relevant development set; no user seeds or in-scope prior-review benchmark were available, so independent recall cannot be estimated.",
          "recommendation": "Obtain expert-supplied known studies and a PRESS peer review before use.",
          "status": "accepted-risk",
          "response": "Reported as an empirical-validation limitation; the strategy requires an information specialist's PRESS peer review before use."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "7dfbf976732c12149ca795840fecc75dfc924510806c4a8b3fba2974ca899665",
      "note": "Same-context closing critic: verifies the earlier lexical revision and documented empirical-validation limitation. Fresh-context review was unavailable because Claude CLI requires login.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Earlier scope assessment remains valid; the search retrieves reflux and either index-test family."
        },
        "operators": {
          "verdict": "pass",
          "note": "Grouped OR blocks are combined with AND; no unreviewed Boolean operator issue."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "MeSH headings and explosion decisions remain appropriate for the concepts."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The resolved wording finding is reflected in the current strategy and evaluation; the unsupported phrase was removed."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Current evaluation reports no blockers, phrase warnings or required issue dispositions."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Only the requested PubMed entry-date cutoff is applied; there is no publication-date limit."
        }
      },
      "findings": [
        {
          "id": "text-us-acronym",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "block": "index_tests",
          "finding": "The text layer did not explicitly cover common DMSA scan forms and contextual renal/urinary US wording.",
          "recommendation": "Add useful variants and re-evaluate.",
          "status": "resolved",
          "response": "Added dimercaptosuccinate[tiab], \"DMSA scan\"[tiab], and \"renal US\"[tiab]. Evaluation grew from 2,077 to 2,080 records after additions, all three development records remained retrieved (100% relative recall against the screened pilot set), with no known losses. The proposed \"urinary US\" phrase generated PubMed phrase-index absence and zero-hit diagnostics, so it was removed and re-evaluated. Current evaluation is complete with no validation blockers or review-required issues."
        },
        {
          "id": "empirical-validation-limit",
          "domain": "translation",
          "severity": "document",
          "kind": "reporting",
          "finding": "Only three pilot discoveries form the relevant development set; no user seeds or in-scope prior-review benchmark were available, so independent recall cannot be estimated.",
          "recommendation": "Obtain expert-supplied known studies and a PRESS peer review before use.",
          "status": "accepted-risk",
          "response": "Reported as an empirical-validation limitation; the strategy requires an information specialist's PRESS peer review before use."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

