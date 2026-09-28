# PubMed search strategy: audit

Generated 2026-09-27T20:24:04+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: In population-based cohorts, is cerebral small vessel disease (and its MRI markers) associated with the risk of incident dementia and cognitive decline?
- Framework: PECO (exposure search; outcomes and eligibility screened)
- Scope confirmed by user: no (User requested no questions and reasonable assumptions. No known relevant articles were supplied. Evaluation is constrained to records available by 2017-05-06; this is the requested historical cutoff, not an eligibility restriction inherent to the review question. Standard-depth candidate discovery will use PubMed/NCBI tooling only, without web search.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Cerebral small vessel disease and MRI markers | search | The disease and its specified MRI manifestations define the exposure and are searchable with controlled vocabulary and text words. |
| Incident dementia and cognitive decline or impairment | screen | Outcome labels are inconsistently reported and indexing them as a required block can lose relevant exposure cohorts. |
| Population-based community-dwelling cohorts | screen | Population source and community setting are eligibility properties that may not be named in abstracts. |
| Prospective or longitudinal observational follow-up | screen | Study design and follow-up are screening criteria; no ad hoc design filter will be required. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-27T20:23:12+00:00
- Records added to PubMed up to: 2017-05-06
- Total records: 54,277 (54,341 before limits)
- Limits and filters: `("1800/01/01"[dp] : "2017/05/06"[dp])` (The user requested a historical search as of 2017-05-06 and explicitly excluded literature published after that date; the workspace as_of date separately limits records to those entered into PubMed by that date.)

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Cerebral Small Vessel Diseases[Mesh]` | 6,257 | none |
| 2 | `Leukoaraiosis[Mesh]` | 470 | none |
| 3 | `Brain Infarction[Mesh]` | 34,827 | none |
| 4 | `"cerebral small vessel disease"[tiab]` | 813 | none |
| 5 | `"cerebral small vessel diseases"[tiab]` | 105 | none |
| 6 | `"small vessel disease"[tiab]` | 2,316 | none |
| 7 | `"small vessel diseases"[tiab]` | 203 | none |
| 8 | `"cerebral microangiopathy"[tiab]` | 136 | none |
| 9 | `"cerebral microangiopathies"[tiab]` | 14 | none |
| 10 | `"cerebral microvascular disease"[tiab]` | 53 | none |
| 11 | `WML[tiab]` | 582 | none |
| 12 | `"subcortical ischemic vascular disease"[tiab]` | 60 | none |
| 13 | `"subcortical ischaemic vascular disease"[tiab]` | 12 | none |
| 14 | `"small vessel ischemic disease"[tiab]` | 15 | none |
| 15 | `SIVD[tiab]` | 120 | none |
| 16 | `leukoaraiosis[tiab]` | 1,008 | none |
| 17 | `"white matter hyperintensity"[tiab]` | 738 | none |
| 18 | `"white matter hyperintensities"[tiab]` | 1,776 | none |
| 19 | `WMH[tiab]` | 1,105 | none |
| 20 | `WMHs[tiab]` | 313 | none |
| 21 | `"white matter hyperintense lesion"[tiab]` | 5 | none |
| 22 | `"white matter hyperintense lesions"[tiab]` | 29 | none |
| 23 | `"periventricular white matter lesions"[tiab]` | 151 | none |
| 24 | `"deep white matter lesions"[tiab]` | 149 | none |
| 25 | `"white matter lesion"[tiab]` | 615 | none |
| 26 | `"white matter lesions"[tiab]` | 3,662 | none |
| 27 | `"white matter change"[tiab]` | 112 | none |
| 28 | `"white matter changes"[tiab]` | 1,796 | none |
| 29 | `"white matter abnormality"[tiab]` | 130 | none |
| 30 | `"white matter abnormalities"[tiab]` | 1,490 | none |
| 31 | `"white matter signal"[tiab]` | 267 | none |
| 32 | `"periventricular hyperintensities"[tiab]` | 126 | none |
| 33 | `"deep white matter hyperintensities"[tiab]` | 115 | none |
| 34 | `"lacunar infarct"[tiab]` | 396 | none |
| 35 | `"lacunar infarcts"[tiab]` | 968 | none |
| 36 | `"lacunar infarction"[tiab]` | 927 | none |
| 37 | `"lacunar infarctions"[tiab]` | 317 | none |
| 38 | `lacune[tiab]` | 153 | none |
| 39 | `lacunes[tiab]` | 585 | none |
| 40 | `"silent infarct"[tiab]` | 68 | none |
| 41 | `"silent infarcts"[tiab]` | 151 | none |
| 42 | `"silent brain infarct"[tiab]` | 24 | none |
| 43 | `"silent brain infarcts"[tiab]` | 115 | none |
| 44 | `"cerebral infarct"[tiab]` | 1,933 | none |
| 45 | `"cerebral infarcts"[tiab]` | 1,332 | none |
| 46 | `"brain infarct"[tiab]` | 783 | none |
| 47 | `"brain infarcts"[tiab]` | 642 | none |
| 48 | `"subclinical infarct"[tiab]` | 5 | none |
| 49 | `"subclinical infarcts"[tiab]` | 14 | none |
| 50 | `"cerebral microbleed"[tiab]` | 65 | none |
| 51 | `"cerebral microbleeds"[tiab]` | 685 | none |
| 52 | `"brain microbleed"[tiab]` | 2 | none |
| 53 | `"brain microbleeds"[tiab]` | 59 | none |
| 54 | `microbleed*[tiab]` | 1,468 | none |
| 55 | `micro-bleed*[tiab]` | 28 | none |
| 56 | `microhemorrhag*[tiab]` | 578 | none |
| 57 | `"vascular brain injury"[tiab]` | 73 | none |
| 58 | `"vascular brain lesions"[tiab]` | 72 | none |
| 59 | `"MRI-defined brain infarct"[tiab]` | 4 | none |
| 60 | `"MRI-defined brain infarcts"[tiab]` | 7 | none |
| 61 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60` | 54,341 | none |
| 62 | `#61 AND ("1800/01/01"[dp] : "2017/05/06"[dp])` | 54,277 | none |

### Strategy (single line, for copying into PubMed)

```text
(((Cerebral Small Vessel Diseases[Mesh] OR Leukoaraiosis[Mesh] OR Brain Infarction[Mesh] OR "cerebral small vessel disease"[tiab] OR "cerebral small vessel diseases"[tiab] OR "small vessel disease"[tiab] OR "small vessel diseases"[tiab] OR "cerebral microangiopathy"[tiab] OR "cerebral microangiopathies"[tiab] OR "cerebral microvascular disease"[tiab] OR WML[tiab] OR "subcortical ischemic vascular disease"[tiab] OR "subcortical ischaemic vascular disease"[tiab] OR "small vessel ischemic disease"[tiab] OR SIVD[tiab] OR leukoaraiosis[tiab] OR "white matter hyperintensity"[tiab] OR "white matter hyperintensities"[tiab] OR WMH[tiab] OR WMHs[tiab] OR "white matter hyperintense lesion"[tiab] OR "white matter hyperintense lesions"[tiab] OR "periventricular white matter lesions"[tiab] OR "deep white matter lesions"[tiab] OR "white matter lesion"[tiab] OR "white matter lesions"[tiab] OR "white matter change"[tiab] OR "white matter changes"[tiab] OR "white matter abnormality"[tiab] OR "white matter abnormalities"[tiab] OR "white matter signal"[tiab] OR "periventricular hyperintensities"[tiab] OR "deep white matter hyperintensities"[tiab] OR "lacunar infarct"[tiab] OR "lacunar infarcts"[tiab] OR "lacunar infarction"[tiab] OR "lacunar infarctions"[tiab] OR lacune[tiab] OR lacunes[tiab] OR "silent infarct"[tiab] OR "silent infarcts"[tiab] OR "silent brain infarct"[tiab] OR "silent brain infarcts"[tiab] OR "cerebral infarct"[tiab] OR "cerebral infarcts"[tiab] OR "brain infarct"[tiab] OR "brain infarcts"[tiab] OR "subclinical infarct"[tiab] OR "subclinical infarcts"[tiab] OR "cerebral microbleed"[tiab] OR "cerebral microbleeds"[tiab] OR "brain microbleed"[tiab] OR "brain microbleeds"[tiab] OR microbleed*[tiab] OR micro-bleed*[tiab] OR microhemorrhag*[tiab] OR "vascular brain injury"[tiab] OR "vascular brain lesions"[tiab] OR "MRI-defined brain infarct"[tiab] OR "MRI-defined brain infarcts"[tiab])) AND (("1800/01/01"[dp] : "2017/05/06"[dp]))) AND ("1800/01/01"[edat] : "2017/05/06"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 337,929 | initial | none | Initial recall-first single exposure block based on the question and screened included studies from prior longitudinal review PMID 20660506; date limits implement the requested 2017-05-06 historical run. |
| 2 | 53,908 | csvd: +0 / -6 | none | Removed the two phrase-index-unavailable zero-hit text alternatives after inspecting their literal translations; retained singular broader alternatives. Removed three broad/overlapping MeSH headings (Cerebrovascular Disorders, Stroke, Lacunar, Cerebral Infarction) to reduce irrelevant retrieval; Brain Infarction remains exploded and captures narrower infarction headings. The benchmark terms remain represented in the text and remaining MeSH layers. |
| 3 | 53,981 | csvd: +4 / -0 | none | Added validated older terminology for subcortical ischemic/ischaemic vascular disease and its common acronym SIVD; the initial candidates returned records in PubMed and no translation warnings. This closes a lexical gap in historical small-vessel-disease naming. |
| 4 | 54,183 | csvd: +6 / -0 | none | Expanded white-matter-marker text coverage with tested hyperintense-lesion wordings, periventricular/deep white matter lesions, and common WMH/WMHs abbreviations. PubMed candidate checks returned counts without phrase-index warnings; abbreviations are retained for recall and may add noise. |
| 5 | 54,277 | csvd: +1 / -0 | none | Added WML acronym identified by objective term ranking from the seven screened-in relevant records (present in two records; PubMed candidate count 582). The broader Cerebrovascular Disorders heading ranked from two records was not restored because its single-term count (329,326) was disproportionate; explicit disease and marker terms remain. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5 (Same-context critic: no fresh-context reviewer was available. Review is PRESS-structured internal QA, not independent peer review.): 2 findings; F1 document accepted-risk, F2 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 851 NCBI requests logged (562 from cache); strategy sha256 32c938d1a57b._

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
      "requested": "Cerebral Small Vessel Diseases",
      "expected_type": "descriptor",
      "checked_at": "2026-09-27T20:23:12+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D059345",
          "name": "Cerebral Small Vessel Diseases",
          "type": "descriptor",
          "scope_note": "Pathological processes or diseases where cerebral MICROVESSELS show abnormalities. They are often associated with aging, hypertension and risk factors for lacunar infarcts (see LACUNAR INFARCTION); LEUKOARAIOSIS; and CEREBRAL HEMORRHAGE.",
          "tree_numbers": [
            "C10.228.140.300.275",
            "C14.907.253.329"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D059345",
      "preferred_label": "Cerebral Small Vessel Diseases",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "Cerebral Small Vessel Diseases",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Leukoaraiosis",
      "expected_type": "descriptor",
      "checked_at": "2026-09-27T20:23:12+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D049292",
          "name": "Leukoaraiosis",
          "type": "descriptor",
          "scope_note": "Non-specific white matter changes in the BRAIN, often seen after age 65. Changes include loss of AXONS; MYELIN pallor, GLIOSIS, loss of ependymal cells, and enlarged perivascular spaces. Leukoaraiosis is a risk factor for DEMENTIA and CEREBROVASCULAR DISORDERS.",
          "tree_numbers": [
            "C23.550.522"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D049292",
      "preferred_label": "Leukoaraiosis",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "Leukoaraiosis",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Brain Infarction",
      "expected_type": "descriptor",
      "checked_at": "2026-09-27T20:23:12+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D020520",
          "name": "Brain Infarction",
          "type": "descriptor",
          "scope_note": "Tissue NECROSIS in any area of the brain, including the CEREBRAL HEMISPHERES, the CEREBELLUM, and the BRAIN STEM. Brain infarction is the result of a cascade of events initiated by inadequate blood flow through the brain that is followed by HYPOXIA and HYPOGLYCEMIA in brain tissue. Damage may be temporary, permanent, selective or pan-necrosis.",
          "tree_numbers": [
            "C10.228.140.300.150.477",
            "C10.228.140.300.775.200",
            "C14.907.253.092.477",
            "C14.907.253.855.200",
            "C23.550.513.355.250",
            "C23.550.717.489.250"
          ],
          "entry_terms": 31,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D020520",
      "preferred_label": "Brain Infarction",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "Brain Infarction",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"cerebral small vessel diseases\"[MeSH Terms] OR \"leukoaraiosis\"[MeSH Terms] OR \"brain infarction\"[MeSH Terms] OR \"cerebral small vessel disease\"[Title/Abstract] OR \"cerebral small vessel diseases\"[Title/Abstract] OR \"small vessel disease\"[Title/Abstract] OR \"small vessel diseases\"[Title/Abstract] OR \"cerebral microangiopathy\"[Title/Abstract] OR \"cerebral microangiopathies\"[Title/Abstract] OR \"cerebral microvascular disease\"[Title/Abstract] OR \"WML\"[Title/Abstract] OR \"subcortical ischemic vascular disease\"[Title/Abstract] OR \"subcortical ischaemic vascular disease\"[Title/Abstract] OR \"small vessel ischemic disease\"[Title/Abstract] OR \"SIVD\"[Title/Abstract] OR \"leukoaraiosis\"[Title/Abstract] OR \"white matter hyperintensity\"[Title/Abstract] OR \"white matter hyperintensities\"[Title/Abstract] OR \"WMH\"[Title/Abstract] OR \"WMHs\"[Title/Abstract] OR \"white matter hyperintense lesion\"[Title/Abstract] OR \"white matter hyperintense lesions\"[Title/Abstract] OR \"periventricular white matter lesions\"[Title/Abstract] OR \"deep white matter lesions\"[Title/Abstract] OR \"white matter lesion\"[Title/Abstract] OR \"white matter lesions\"[Title/Abstract] OR \"white matter change\"[Title/Abstract] OR \"white matter changes\"[Title/Abstract] OR \"white matter abnormality\"[Title/Abstract] OR \"white matter abnormalities\"[Title/Abstract] OR \"white matter signal\"[Title/Abstract] OR \"periventricular hyperintensities\"[Title/Abstract] OR \"deep white matter hyperintensities\"[Title/Abstract] OR \"lacunar infarct\"[Title/Abstract] OR \"lacunar infarcts\"[Title/Abstract] OR \"lacunar infarction\"[Title/Abstract] OR \"lacunar infarctions\"[Title/Abstract] OR \"lacune\"[Title/Abstract] OR \"lacunes\"[Title/Abstract] OR \"silent infarct\"[Title/Abstract] OR \"silent infarcts\"[Title/Abstract] OR \"silent brain infarct\"[Title/Abstract] OR \"silent brain infarcts\"[Title/Abstract] OR \"cerebral infarct\"[Title/Abstract] OR \"cerebral infarcts\"[Title/Abstract] OR \"brain infarct\"[Title/Abstract] OR \"brain infarcts\"[Title/Abstract] OR \"subclinical infarct\"[Title/Abstract] OR \"subclinical infarcts\"[Title/Abstract] OR \"cerebral microbleed\"[Title/Abstract] OR \"cerebral microbleeds\"[Title/Abstract] OR \"brain microbleed\"[Title/Abstract] OR \"brain microbleeds\"[Title/Abstract] OR \"microbleed*\"[Title/Abstract] OR \"micro bleed*\"[Title/Abstract] OR \"microhemorrhag*\"[Title/Abstract] OR \"vascular brain injury\"[Title/Abstract] OR \"vascular brain lesions\"[Title/Abstract] OR \"MRI-defined brain infarct\"[Title/Abstract] OR \"MRI-defined brain infarcts\"[Title/Abstract]) AND 1800/01/01:2017/05/06[Date - Publication] AND 1800/01/01:2017/05/06[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "bbd19787322be879b9c6caec15e40cd462208b97dcb2a4d3b72359bdc539a914",
      "note": "Same-context critic: no fresh-context reviewer was available. Review is PRESS-structured internal QA, not independent peer review.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "One broad exposure block reflects PECO. Outcome, population/setting, and longitudinal design remain screening criteria to protect recall."
        },
        "operators": {
          "verdict": "pass",
          "note": "Synonyms and marker families are ORed in the exposure block. No NOT or study-design block is used. The publication-date and entry-date bounds are applied as explicit limits."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Cerebral Small Vessel Diseases and Leukoaraiosis are relevant verified headings; Brain Infarction is retained exploded to cover infarct-marker indexing. No specific microbleed heading was identified in the lookup; microbleeds are covered by text words."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Text covers current and historical disease names, white-matter lesion terms, infarct/lacune variants, microbleed variants, vascular brain injury, and common WMH and SIVD abbreviations. Candidate wording was checked in PubMed; no phrase warnings remain."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All clauses have explicit field tags, syntax checks pass, MeSH headings are verified, and PubMed returned no translation issues."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The publication date limit enforces the requested 2017-05-06 historical cutoff; the workspace entry-date bound separately limits records to those in PubMed by that date. No design or language filter is imposed."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "document",
          "kind": "lexical",
          "block": "csvd",
          "finding": "Brain Infarction[Mesh] is a broad heading and contributes substantial non-specific retrieval, although it may capture MRI infarct markers indexed without specific wording.",
          "recommendation": "Retain for this recall-first search and flag the additional screening burden for peer review.",
          "status": "accepted-risk",
          "response": "Screened development records and MRI-defined infarct concepts support retaining the exploded infarction descriptor. It is retained to preserve sensitivity; the tested final count is high and results require eligibility screening."
        },
        {
          "id": "F2",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "block": "csvd",
          "finding": "WMH and SIVD abbreviations can have meanings outside cerebral small vessel disease and may add irrelevant hits.",
          "recommendation": "Retain these commonly used field abbreviations for recall, with screening for irrelevant acronym matches.",
          "status": "accepted-risk",
          "response": "They were tested in PubMed and add a limited number of records to the broad OR block. Full-form synonyms remain present, and abbreviations help retrieve abstracts that use shorthand only. WML was also added based on term ranking in the relevant development set."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

