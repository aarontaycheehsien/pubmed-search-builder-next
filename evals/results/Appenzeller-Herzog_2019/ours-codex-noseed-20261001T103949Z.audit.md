# PubMed search strategy: audit

Generated 2026-10-01T11:46:20+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Comparative effectiveness of common therapies for Wilson disease
- Framework: PICO
- Scope confirmed by user: no (User asked to proceed without questions. Assumed common established disease-specific therapies include chelating drugs, zinc therapy, tetrathiomolybdate, and liver transplantation; comparative design, comparator, and outcomes were screened, with inclusion limited to direct or treatment-sequence comparisons. No user seeds supplied. Standard depth, default screening budget 10,000, and no language/publication limits. PubMed is evaluated with PSB_AS_OF=2018-12-23 (Entrez-date bound), without a publication-date limit. Scope was not separately confirmed because the user requested no questions. The therapy block intentionally combines named therapy members with broad treatment descriptors as recall hooks; generic terms do not establish eligibility. The 2018-12-23 PubMed entry-date bound is required by the run instructions and does not use a publication-date limit.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Wilson disease | search | Target condition; explicitly named and indexed in relevant clinical records. |
| Common disease-specific therapies for Wilson disease | search | Search named therapy members and broad treatment descriptors together to maximize recall when abstracts discuss Wilson disease treatment without naming the specific agent; screen eligibility for a permitted therapy and comparative design. |
| Comparative effectiveness design | screen | Comparators and study design are inconsistently named in abstracts; determine at screening. |
| Clinical effectiveness and harms outcomes | screen | Clinical outcomes vary and are not required in titles or abstracts. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T11:45:26+00:00
- Records added to PubMed up to: 2018-12-23
- Total records: 3,981
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Hepatolenticular Degeneration"[Mesh]` | 5,697 | none |
| 2 | `"Wilson disease"[tiab]` | 5,545 | none |
| 3 | `"Wilson's disease"[tiab]` | 4,158 | none |
| 4 | `"Wilsons disease"[tiab]` | 4,135 | none |
| 5 | `"Wilson disease"[tiab:~1]` | 5,627 | none |
| 6 | `hepatolenticular[tiab]` | 975 | none |
| 7 | `Kinnier-Wilson[tiab]` | 38 | none |
| 8 | `Kinnier Wilson[tiab]` | 38 | none |
| 9 | `"copper storage disease"[tiab]` | 25 | none |
| 10 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9` | 7,297 | none |
| 11 | `"Drug Therapy"[Mesh]` | 1,305,324 | none |
| 12 | `"Penicillamine"[Mesh]` | 7,878 | none |
| 13 | `"Trientine"[Mesh]` | 380 | none |
| 14 | `"Zinc Compounds"[Mesh]` | 12,484 | none |
| 15 | `"Liver Transplantation"[Mesh]` | 54,773 | none |
| 16 | `treatment[tiab]` | 3,933,275 | none |
| 17 | `treatments[tiab]` | 410,191 | none |
| 18 | `treat*[tiab]` | 5,019,713 | none |
| 19 | `therap*[tiab]` | 2,661,898 | none |
| 20 | `medicat*[tiab]` | 288,908 | none |
| 21 | `pharmacolog*[tiab]` | 366,637 | none |
| 22 | `chelat*[tiab]` | 62,346 | none |
| 23 | `penicillamine[tiab]` | 6,853 | none |
| 24 | `"D-penicillamine"[tiab]` | 3,268 | none |
| 25 | `trientine[tiab]` | 219 | none |
| 26 | `triethylenetetramine[tiab]` | 360 | none |
| 27 | `zinc[tiab]` | 108,490 | none |
| 28 | `"zinc acetate"[tiab]` | 817 | none |
| 29 | `"zinc sulfate"[tiab]` | 1,531 | none |
| 30 | `"zinc sulphate"[tiab]` | 857 | none |
| 31 | `tetrathiomolybdate[tiab]` | 351 | none |
| 32 | `"ammonium tetrathiomolybdate"[tiab]` | 84 | none |
| 33 | `WTX101[tiab]` | 3 | none |
| 34 | `"bis-choline tetrathiomolybdate"[tiab]` | 6 | none |
| 35 | `transplant*[tiab]` | 443,114 | none |
| 36 | `"liver transplantation"[tiab]` | 47,028 | none |
| 37 | `"liver transplant"[tiab]` | 15,249 | none |
| 38 | `"Drug Substitution"[Mesh]` | 3,429 | none |
| 39 | `switch*[tiab]` | 148,719 | none |
| 40 | `transition*[tiab]` | 367,992 | none |
| 41 | `substitut*[tiab]` | 304,988 | none |
| 42 | `sequenc*[tiab]` | 1,088,326 | none |
| 43 | `chang*[tiab]` | 2,853,839 | none |
| 44 | `DMPS[tiab]` | 745 | none |
| 45 | `unithiol[tiab]` | 216 | none |
| 46 | `dimercaptopropane[tiab]` | 206 | none |
| 47 | `dimercaptopropane sulfonate[tiab]` | 36 | none |
| 48 | `"2,3-dimercapto-1-propanesulfonic acid"[tiab]` | 66 | none |
| 49 | `#11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48` | 10,714,780 | none |
| 50 | `#10 AND #49` | 3,981 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Hepatolenticular Degeneration"[Mesh] OR "Wilson disease"[tiab] OR "Wilson's disease"[tiab] OR "Wilsons disease"[tiab] OR "Wilson disease"[tiab:~1] OR hepatolenticular[tiab] OR Kinnier-Wilson[tiab] OR Kinnier Wilson[tiab] OR "copper storage disease"[tiab]) AND ("Drug Therapy"[Mesh] OR "Penicillamine"[Mesh] OR "Trientine"[Mesh] OR "Zinc Compounds"[Mesh] OR "Liver Transplantation"[Mesh] OR treatment[tiab] OR treatments[tiab] OR treat*[tiab] OR therap*[tiab] OR medicat*[tiab] OR pharmacolog*[tiab] OR chelat*[tiab] OR penicillamine[tiab] OR "D-penicillamine"[tiab] OR trientine[tiab] OR triethylenetetramine[tiab] OR zinc[tiab] OR "zinc acetate"[tiab] OR "zinc sulfate"[tiab] OR "zinc sulphate"[tiab] OR tetrathiomolybdate[tiab] OR "ammonium tetrathiomolybdate"[tiab] OR WTX101[tiab] OR "bis-choline tetrathiomolybdate"[tiab] OR transplant*[tiab] OR "liver transplantation"[tiab] OR "liver transplant"[tiab] OR "Drug Substitution"[Mesh] OR switch*[tiab] OR transition*[tiab] OR substitut*[tiab] OR sequenc*[tiab] OR chang*[tiab] OR DMPS[tiab] OR unithiol[tiab] OR dimercaptopropane[tiab] OR dimercaptopropane sulfonate[tiab] OR "2,3-dimercapto-1-propanesulfonic acid"[tiab])) AND ("1800/01/01"[edat] : "2018/12/23"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 11 | 11 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 4 | 4 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Common disease-specific therapies for Wilson disease | 1 | `Hepatolenticular Degeneration[Mesh]` | 3,153 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| wilson | 10,714,780 | 0 |
| therapies | 7,297 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial recall-first strategy: Wilson disease AND broad category of disease-specific therapies with MeSH and free-text names; no filters or limits. |
| 2 | 0 | wilson: +10 / -0; therapies: +28 / -0 | none | Initial recall-first strategy: Wilson disease AND broad category of disease-specific therapies with MeSH and free-text names; no filters or limits. |
| 3 | 3,393 | wilson: +0 / -1; therapies: +1 / -1 | none | Removed a zero-hit disease synonym and an ambiguous authority lookup; added Drug Substitution MeSH for treatment transitions. Retained explicit drug/member terms and generic therapy wording. |
| 4 | 3,980 | therapies: +5 / -0 | none | Added direction-neutral text terms for treatment switching, transitions, substitution, sequencing, and change in response to critic R1-1; preserve eligibility for treatment-sequence comparisons. |
| 5 | 3,981 | therapies: +6 / -0 | none | Added DMPS and expanded-name text terms in response to the round 1 PRESS critique; reran complete evaluation. |
| 6 | 3,981 | therapies: +0 / -1 | none | Removed the malformed 2,3-dimercapto-1-propanesulfonate expression after clause testing showed it fell back to All Fields; retained DMPS, unithiol, dimercaptopropane, and the separately tested sulfonic-acid form. Complete evaluation rerun. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 4: 1 findings; R1-1 should-fix resolved
- Round 2 on version 5: 2 findings; R1-1 should-fix resolved, R2-1 should-fix open
- Round 3 on version 6: 2 findings; R1-1 should-fix resolved, R2-1 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1251 NCBI requests logged (622 from cache); strategy sha256 308687ab3a9d._

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
      "checked_at": "2026-10-01T11:45:26+00:00",
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
      "requested": "Drug Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:45:26+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "Q000188",
          "name": "drug therapy",
          "type": "qualifier",
          "scope_note": "Used with disease headings for the treatment of disease by the administration of drugs, chemicals, and antibiotics. For diet therapy and radiotherapy, use specific subheadings. Excludes immunotherapy for which therapy is used.",
          "tree_numbers": [
            "Y11.020"
          ],
          "entry_terms": 3,
          "mapped_to": null
        },
        {
          "ui": "D004358",
          "name": "Drug Therapy",
          "type": "descriptor",
          "scope_note": "The use of DRUGS to treat a DISEASE or its symptoms. One example is the use of ANTINEOPLASTIC AGENTS to treat CANCER.",
          "tree_numbers": [
            "E02.319"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004358",
      "preferred_label": "Drug Therapy",
      "type": "descriptor",
      "location": "vocabulary:10",
      "term": {
        "text": "\"Drug Therapy\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Penicillamine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:45:26+00:00",
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
      "location": "vocabulary:11",
      "term": {
        "text": "\"Penicillamine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Trientine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:45:26+00:00",
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
      "location": "vocabulary:12",
      "term": {
        "text": "\"Trientine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc Compounds",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:45:26+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D017967",
          "name": "Zinc Compounds",
          "type": "descriptor",
          "scope_note": "Inorganic compounds that contain zinc as an integral part of the molecule.",
          "tree_numbers": [
            "D01.975"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D017967",
      "preferred_label": "Zinc Compounds",
      "type": "descriptor",
      "location": "vocabulary:13",
      "term": {
        "text": "\"Zinc Compounds\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Liver Transplantation",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:45:26+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D016031",
          "name": "Liver Transplantation",
          "type": "descriptor",
          "scope_note": "The transference of a part of or an entire liver from one human or animal to another.",
          "tree_numbers": [
            "E02.095.147.725.490",
            "E04.210.650",
            "E04.936.450.490",
            "E04.936.580.490"
          ],
          "entry_terms": 10,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D016031",
      "preferred_label": "Liver Transplantation",
      "type": "descriptor",
      "location": "vocabulary:14",
      "term": {
        "text": "\"Liver Transplantation\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Drug Substitution",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T11:45:26+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D057915",
          "name": "Drug Substitution",
          "type": "descriptor",
          "scope_note": "The practice of replacing one prescribed drug with another that is expected to have the same clinical or psychological effect.",
          "tree_numbers": [
            "E02.319.307.312",
            "N02.421.668.778.500.312"
          ],
          "entry_terms": 15,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D057915",
      "preferred_label": "Drug Substitution",
      "type": "descriptor",
      "location": "vocabulary:37",
      "term": {
        "text": "\"Drug Substitution\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Hepatolenticular Degeneration\"[MeSH Terms] OR \"Wilson disease\"[Title/Abstract] OR \"Wilson's disease\"[Title/Abstract] OR \"Wilsons disease\"[Title/Abstract] OR \"Wilson disease\"[Title/Abstract:~1] OR \"hepatolenticular\"[Title/Abstract] OR \"Kinnier-Wilson\"[Title/Abstract] OR \"Kinnier-Wilson\"[Title/Abstract] OR \"copper storage disease\"[Title/Abstract]) AND (\"Drug Therapy\"[MeSH Terms] OR \"Penicillamine\"[MeSH Terms] OR \"Trientine\"[MeSH Terms] OR \"Zinc Compounds\"[MeSH Terms] OR \"Liver Transplantation\"[MeSH Terms] OR \"treatment\"[Title/Abstract] OR \"treatments\"[Title/Abstract] OR \"treat*\"[Title/Abstract] OR \"therap*\"[Title/Abstract] OR \"medicat*\"[Title/Abstract] OR \"pharmacolog*\"[Title/Abstract] OR \"chelat*\"[Title/Abstract] OR \"Penicillamine\"[Title/Abstract] OR \"D-penicillamine\"[Title/Abstract] OR \"Trientine\"[Title/Abstract] OR \"triethylenetetramine\"[Title/Abstract] OR \"zinc\"[Title/Abstract] OR \"zinc acetate\"[Title/Abstract] OR \"zinc sulfate\"[Title/Abstract] OR \"zinc sulphate\"[Title/Abstract] OR \"tetrathiomolybdate\"[Title/Abstract] OR \"ammonium tetrathiomolybdate\"[Title/Abstract] OR \"WTX101\"[Title/Abstract] OR \"bis-choline tetrathiomolybdate\"[Title/Abstract] OR \"transplant*\"[Title/Abstract] OR \"Liver Transplantation\"[Title/Abstract] OR \"liver transplant\"[Title/Abstract] OR \"Drug Substitution\"[MeSH Terms] OR \"switch*\"[Title/Abstract] OR \"transition*\"[Title/Abstract] OR \"substitut*\"[Title/Abstract] OR \"sequenc*\"[Title/Abstract] OR \"chang*\"[Title/Abstract] OR \"DMPS\"[Title/Abstract] OR \"unithiol\"[Title/Abstract] OR \"dimercaptopropane\"[Title/Abstract] OR \"dimercaptopropane sulfonate\"[Title/Abstract] OR \"2,3-dimercapto-1-propanesulfonic acid\"[Title/Abstract]) AND 1800/01/01:2018/12/23[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 4,
      "review_sha256": "6d92e2d489c23f142fb23d68ef8be6527bd86d8958d7837cd9c2ef6cf594296e",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The packet reports no PubMed translation warnings or errors. The Wilson proximity expression is retained alongside exact phrases and unquoted variants."
        },
        "operators": {
          "verdict": "pass",
          "note": "The Wilson and therapy blocks are OR-combined and then AND-combined, consistent with the stated scope. Comparative design and outcomes remain screening criteria, as justified."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the Wilson disease, drug therapy, named therapy, and transplantation headings as descriptors. The headings are combined with text words."
        },
        "text_words": {
          "verdict": "revise",
          "note": "DMPS appears in the packet as part of an additional penicillamine/DMPS treatment comparison, but the therapy block has no DMPS or expanded-name text word. Broad treatment descriptors retrieve known records, but do not establish coverage of records that name DMPS without those descriptors."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The strategy parses, has no reported lint or translation issues, and retrieves all 15 known records in the packet."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2018-12-23 bound is applied as an Entrez entry-date limit, as documented; no publication-date limit is applied."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The packet names a penicillamine/DMPS treatment comparison, but the therapy block does not search DMPS or its expanded name. Retrieval of known records through broad treatment descriptors does not show that records naming DMPS alone will be found.",
          "recommendation": "Add DMPS and its expanded name as therapy text words, or document why DMPS is outside the intended common-therapy scope; then reevaluate the complete strategy.",
          "status": "resolved",
          "response": "Added DMPS, unithiol, dimercaptopropane sulfonate, and expanded-name text terms to the therapy block. Full evaluation version 5 retrieved all 15 known records, found no misses or syntax/translation issues, and increased the PubMed count from 3,980 to 3,981. The intended inclusion of DMPS is consistent with the question's common disease-specific therapy scope."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "f31224fea35978b5c0e14a9893b0d716723735f8ebf0a72d353a1f0bf74bf891",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The strategy parses and its Wilson and therapy concepts translate, but version 5 retains warnings for the dimercaptopropane sulfonate wording, including a quoted phrase with zero hits and a warning on the complete therapy and final queries. The packet does not show clause-specific tests of alternatives or comparisons of their counts and known-record losses. The other DMPS-related terms provide some coverage context, but do not establish that these warned expressions behave as intended."
        },
        "operators": {
          "verdict": "pass",
          "note": "The Wilson and therapy blocks are OR-combined and then AND-combined, consistent with the stated search scope. The supplied known records are retrieved, with no losses reported; comparative design and outcomes remain screening criteria as justified."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet reports that the Wilson disease, drug therapy, named therapy, and liver transplantation headings were verified as descriptors and combined with text words."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The therapy block now includes bare text terms for DMPS and related names, in addition to the named common therapies, transplantation, and broad treatment descriptors. Switch, transition, substitution, sequence, and change terms search for the treatment process without restricting direction; screening can determine direction and eligibility. The 0/30 category probe is weak evidence and does not establish that member-only records are absent."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The strategy parses, lint is empty, and the packet reports retrieval of all 15 known records. The phrase warnings are translation review concerns, not reported syntax errors."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2018-12-23 bound is documented as a PubMed Entrez entry-date bound, not a publication-date limit; no other limits are applied."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier packet identified missing DMPS and expanded-name therapy terms despite a known penicillamine/DMPS comparison.",
          "recommendation": "Add DMPS and relevant expanded-name terms, or document why DMPS is outside scope, then reevaluate.",
          "status": "resolved",
          "response": "Version 5 adds DMPS, unithiol, dimercaptopropane, dimercaptopropane sulfonate, and expanded-name terms. The packet reports retrieval of all 15 known records, no known losses, and a count increase from 3,980 to 3,981."
        },
        {
          "id": "R2-1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "syntax",
          "finding": "Version 5 retains phrase-translation warnings for dimercaptopropane sulfonate wording, including a zero-hit quoted phrase, and warnings on the therapy and final queries. The packet supplies no clause-specific tests of alternatives or comparisons of their counts and known-record losses.",
          "recommendation": "Test an appropriate unquoted, proximity, or separately tagged-word expression, or remove the warned wording with justification; compare clause and final counts and known-record retrieval after a complete reevaluation.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-2147658faddc8f309478",
          "status": "accepted-risk",
          "response": "Retained as an unresolved interpretation risk for the dimercaptopropane sulfonate wording; related DMPS terms are present, but this warning has not been resolved by a clause-specific alternative test.",
          "evidence": "Version 5 includes DMPS, unithiol, dimercaptopropane, and dimercaptopropane sulfonate terms, and the strategy retrieves all 15 known records. The packet provides no comparison showing how this warned expression changes clause or final retrieval.",
          "query": "(dimercaptopropane sulfonate[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
          "translation": "\"dimercaptopropane sulfonate\"[Title/Abstract] AND 1800/01/01:2018/12/23[Date - Entry]"
        },
        {
          "issue_id": "I-80de8b00794fcb76a735",
          "status": "accepted-risk",
          "response": "The zero-hit phrase remains unverified as an effective expression. Related terms offer some coverage context but do not prove this phrase redundant.",
          "evidence": "The packet reports zero hits and a quoted-phrase warning for this expression. It also includes related DMPS terms and reports no known-record losses; it gives no alternative-expression comparison.",
          "query": "(\"2,3-dimercapto-1-propanesulfonate\"[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
          "translation": "(\"2,3-dimercapto-1-propanesulfonate\"[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])"
        },
        {
          "issue_id": "I-a7359630733d74eb35df",
          "status": "accepted-risk",
          "response": "PubMed's reported warning is retained as an unresolved interpretation risk for the same zero-hit term.",
          "evidence": "The packet reports “No items found” for the term-level query; no tested rewrite or removal evaluation is provided.",
          "query": "(\"2,3-dimercapto-1-propanesulfonate\"[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
          "translation": "(\"2,3-dimercapto-1-propanesulfonate\"[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])"
        },
        {
          "issue_id": "I-0aa952d82c19a8cd3dc5",
          "status": "accepted-risk",
          "response": "Zero hits alone do not establish redundancy, so the expression remains an unresolved, documented risk.",
          "evidence": "The packet reports zero hits for the quoted phrase. Other DMPS-related terms are included, but the packet does not compare their retrieval with a tested replacement for this phrase.",
          "query": "(\"2,3-dimercapto-1-propanesulfonate\"[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
          "translation": "(\"2,3-dimercapto-1-propanesulfonate\"[tiab]) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])"
        },
        {
          "issue_id": "I-cf8f4c3c293ac3e842b3",
          "status": "accepted-risk",
          "response": "The complete therapy-block warning remains unresolved because no clause-specific alternative or removal was evaluated.",
          "evidence": "The full block retains the warned term. The 15 known records are retrieved, but the packet does not report how this expression affects block retrieval or compare alternative syntax.",
          "query": "((\"Drug Therapy\"[Mesh] OR \"Penicillamine\"[Mesh] OR \"Trientine\"[Mesh] OR \"Zinc Compounds\"[Mesh] OR \"Liver Transplantation\"[Mesh] OR treatment[tiab] OR treatments[tiab] OR treat*[tiab] OR therap*[tiab] OR medicat*[tiab] OR pharmacolog*[tiab] OR chelat*[tiab] OR penicillamine[tiab] OR \"D-penicillamine\"[tiab] OR trientine[tiab] OR triethylenetetramine[tiab] OR zinc[tiab] OR \"zinc acetate\"[tiab] OR \"zinc sulfate\"[tiab] OR \"zinc sulphate\"[tiab] OR tetrathiomolybdate[tiab] OR \"ammonium tetrathiomolybdate\"[tiab] OR WTX101[tiab] OR \"bis-choline tetrathiomolybdate\"[tiab] OR transplant*[tiab] OR \"liver transplantation\"[tiab] OR \"liver transplant\"[tiab] OR \"Drug Substitution\"[Mesh] OR switch*[tiab] OR transition*[tiab] OR substitut*[tiab] OR sequenc*[tiab] OR chang*[tiab] OR DMPS[tiab] OR unithiol[tiab] OR dimercaptopropane[tiab] OR dimercaptopropane sulfonate[tiab] OR \"2,3-dimercapto-1-propanesulfonic acid\"[tiab] OR \"2,3-dimercapto-1-propanesulfonate\"[tiab])) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
          "translation": "(\"Drug Therapy\"[MeSH Terms] OR \"Penicillamine\"[MeSH Terms] OR \"Trientine\"[MeSH Terms] OR \"Zinc Compounds\"[MeSH Terms] OR \"Liver Transplantation\"[MeSH Terms] OR \"treatment\"[Title/Abstract] OR \"treatments\"[Title/Abstract] OR \"treat*\"[Title/Abstract] OR \"therap*\"[Title/Abstract] OR \"medicat*\"[Title/Abstract] OR \"pharmacolog*\"[Title/Abstract] OR \"chelat*\"[Title/Abstract] OR \"Penicillamine\"[Title/Abstract] OR \"D-penicillamine\"[Title/Abstract] OR \"Trientine\"[Title/Abstract] OR \"triethylenetetramine\"[Title/Abstract] OR \"zinc\"[Title/Abstract] OR \"zinc acetate\"[Title/Abstract] OR \"zinc sulfate\"[Title/Abstract] OR \"zinc sulphate\"[Title/Abstract] OR \"tetrathiomolybdate\"[Title/Abstract] OR \"ammonium tetrathiomolybdate\"[Title/Abstract] OR \"WTX101\"[Title/Abstract] OR \"bis-choline tetrathiomolybdate\"[Title/Abstract] OR \"transplant*\"[Title/Abstract] OR \"Liver Transplantation\"[Title/Abstract] OR \"liver transplant\"[Title/Abstract] OR \"Drug Substitution\"[MeSH Terms] OR \"switch*\"[Title/Abstract] OR \"transition*\"[Title/Abstract] OR \"substitut*\"[Title/Abstract] OR \"sequenc*\"[Title/Abstract] OR \"chang*\"[Title/Abstract] OR \"DMPS\"[Title/Abstract] OR \"unithiol\"[Title/Abstract] OR \"dimercaptopropane\"[Title/Abstract] OR \"dimercaptopropane sulfonate\"[Title/Abstract] OR \"2,3-dimercapto-1-propanesulfonic acid\"[Title/Abstract]) AND 1800/01/01:2018/12/23[Date - Entry]"
        },
        {
          "issue_id": "I-a31336ef43c569dcafec",
          "status": "accepted-risk",
          "response": "The final-query warning is retained as an unresolved interpretation risk; known-record coverage does not resolve the phrase-specific translation concern.",
          "evidence": "The full strategy reports all 15 known records and no known losses, but no alternate clause or full-query evaluation is supplied for this warning.",
          "query": "((\"Hepatolenticular Degeneration\"[Mesh] OR \"Wilson disease\"[tiab] OR \"Wilson's disease\"[tiab] OR \"Wilsons disease\"[tiab] OR \"Wilson disease\"[tiab:~1] OR hepatolenticular[tiab] OR Kinnier-Wilson[tiab] OR Kinnier Wilson[tiab] OR \"copper storage disease\"[tiab]) AND (\"Drug Therapy\"[Mesh] OR \"Penicillamine\"[Mesh] OR \"Trientine\"[Mesh] OR \"Zinc Compounds\"[Mesh] OR \"Liver Transplantation\"[Mesh] OR treatment[tiab] OR treatments[tiab] OR treat*[tiab] OR therap*[tiab] OR medicat*[tiab] OR pharmacolog*[tiab] OR chelat*[tiab] OR penicillamine[tiab] OR \"D-penicillamine\"[tiab] OR trientine[tiab] OR triethylenetetramine[tiab] OR zinc[tiab] OR \"zinc acetate\"[tiab] OR \"zinc sulfate\"[tiab] OR \"zinc sulphate\"[tiab] OR tetrathiomolybdate[tiab] OR \"ammonium tetrathiomolybdate\"[tiab] OR WTX101[tiab] OR \"bis-choline tetrathiomolybdate\"[tiab] OR transplant*[tiab] OR \"liver transplantation\"[tiab] OR \"liver transplant\"[tiab] OR \"Drug Substitution\"[Mesh] OR switch*[tiab] OR transition*[tiab] OR substitut*[tiab] OR sequenc*[tiab] OR chang*[tiab] OR DMPS[tiab] OR unithiol[tiab] OR dimercaptopropane[tiab] OR dimercaptopropane sulfonate[tiab] OR \"2,3-dimercapto-1-propanesulfonic acid\"[tiab] OR \"2,3-dimercapto-1-propanesulfonate\"[tiab])) AND (\"1800/01/01\"[edat] : \"2018/12/23\"[edat])",
          "translation": "(\"Hepatolenticular Degeneration\"[MeSH Terms] OR \"Wilson disease\"[Title/Abstract] OR \"Wilson's disease\"[Title/Abstract] OR \"Wilsons disease\"[Title/Abstract] OR \"Wilson disease\"[Title/Abstract:~1] OR \"hepatolenticular\"[Title/Abstract] OR \"Kinnier-Wilson\"[Title/Abstract] OR \"Kinnier-Wilson\"[Title/Abstract] OR \"copper storage disease\"[Title/Abstract]) AND (\"Drug Therapy\"[MeSH Terms] OR \"Penicillamine\"[MeSH Terms] OR \"Trientine\"[MeSH Terms] OR \"Zinc Compounds\"[MeSH Terms] OR \"Liver Transplantation\"[MeSH Terms] OR \"treatment\"[Title/Abstract] OR \"treatments\"[Title/Abstract] OR \"treat*\"[Title/Abstract] OR \"therap*\"[Title/Abstract] OR \"medicat*\"[Title/Abstract] OR \"pharmacolog*\"[Title/Abstract] OR \"chelat*\"[Title/Abstract] OR \"Penicillamine\"[Title/Abstract] OR \"D-penicillamine\"[Title/Abstract] OR \"Trientine\"[Title/Abstract] OR \"triethylenetetramine\"[Title/Abstract] OR \"zinc\"[Title/Abstract] OR \"zinc acetate\"[Title/Abstract] OR \"zinc sulfate\"[Title/Abstract] OR \"zinc sulphate\"[Title/Abstract] OR \"tetrathiomolybdate\"[Title/Abstract] OR \"ammonium tetrathiomolybdate\"[Title/Abstract] OR \"WTX101\"[Title/Abstract] OR \"bis-choline tetrathiomolybdate\"[Title/Abstract] OR \"transplant*\"[Title/Abstract] OR \"Liver Transplantation\"[Title/Abstract] OR \"liver transplant\"[Title/Abstract] OR \"Drug Substitution\"[MeSH Terms] OR \"switch*\"[Title/Abstract] OR \"transition*\"[Title/Abstract] OR \"substitut*\"[Title/Abstract] OR \"sequenc*\"[Title/Abstract] OR \"chang*\"[Title/Abstract] OR \"DMPS\"[Title/Abstract] OR \"unithiol\"[Title/Abstract] OR \"dimercaptopropane\"[Title/Abstract] OR \"dimercaptopropane sulfonate\"[Title/Abstract] OR \"2,3-dimercapto-1-propanesulfonic acid\"[Title/Abstract]) AND 1800/01/01:2018/12/23[Date - Entry]"
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 6,
      "review_sha256": "8addb42246c3c16849892a788fb7808c1861f3fb0b69a020b6a7c6e89bfe4371",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Version 6 removes the malformed quoted 2,3-dimercapto-1-propanesulfonate expression. The complete evaluation reports no translation warnings, errors, or translation issues. DMPS, unithiol, dimercaptopropane, dimercaptopropane sulfonate, and the acid form remain."
        },
        "operators": {
          "verdict": "pass",
          "note": "The Wilson and therapy blocks are OR-combined and then AND-combined, matching the searched concepts. Comparative design and outcomes remain screening criteria, as justified. All 15 known records are retrieved."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet verifies the Wilson disease, drug therapy, named therapy, liver transplantation, and drug substitution headings as descriptors, combined with text words."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The therapy block includes bare names for DMPS and related forms, common disease-specific therapies, transplantation, and broad treatment descriptors. Switching and related process terms do not restrict direction; eligibility can be determined at screening. The category probe found 0 relevant records among 30 screened, which is limited evidence but does not identify a required change."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The strategy parses, lint and translation diagnostics are empty, and the complete evaluation reports all 15 known records retrieved with no misses."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The 2018-12-23 bound is documented as a PubMed Entrez entry-date limit. No publication-date limit or other unreported limit is applied."
        }
      },
      "findings": [
        {
          "id": "R1-1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "An earlier packet identified missing DMPS and expanded-name therapy terms despite a known penicillamine/DMPS comparison.",
          "recommendation": "Add DMPS and relevant expanded-name terms, or document why DMPS is outside scope, then reevaluate.",
          "status": "resolved",
          "response": "Version 6 retains DMPS, unithiol, dimercaptopropane, dimercaptopropane sulfonate, and the acid form. Its complete evaluation retrieves all 15 known records, with no misses."
        },
        {
          "id": "R2-1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "syntax",
          "finding": "An earlier review found phrase-translation warnings for dimercaptopropane sulfonate wording, including the zero-hit quoted expression and warnings on the therapy and final queries.",
          "recommendation": "Test an appropriate alternative or remove the warned wording with justification, then compare clause and final counts and known-record retrieval after a complete reevaluation.",
          "status": "resolved",
          "response": "Version 6 removes the malformed quoted 2,3-dimercapto-1-propanesulfonate expression, retains the other listed DMPS-related terms, and records a complete reevaluation. The current diagnostics report no translation warnings, errors, or issues; all 15 known records are retrieved."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-2147658faddc8f309478",
          "status": "resolved",
          "response": "The complete evaluation for version 6 reports no translation warning for the therapy wording after removal of the malformed quoted 2,3-dimercapto-1-propanesulfonate expression. The generic dimercaptopropane sulfonate term remains.",
          "evidence": "Version 6 has empty raw translation diagnostics and translation_issues, retrieves all 15 known records, and retains DMPS, unithiol, dimercaptopropane, dimercaptopropane sulfonate, and the acid form."
        },
        {
          "issue_id": "I-80de8b00794fcb76a735",
          "status": "resolved",
          "response": "The zero-hit quoted 2,3-dimercapto-1-propanesulfonate expression was removed and the complete strategy reevaluated.",
          "evidence": "The current strategy omits that quoted expression, retains the acid form and other DMPS-related terms, reports no translation issues, and retrieves all 15 known records."
        },
        {
          "issue_id": "I-a7359630733d74eb35df",
          "status": "resolved",
          "response": "The warned zero-hit quoted expression was removed; the complete version 6 evaluation reports no translation issues.",
          "evidence": "Version 6 reports empty raw diagnostics and translation_issues and retrieves all 15 known records."
        },
        {
          "issue_id": "I-0aa952d82c19a8cd3dc5",
          "status": "resolved",
          "response": "The quoted zero-hit expression was removed and the strategy was completely reevaluated; related DMPS terms remain.",
          "evidence": "The current query retains DMPS, unithiol, dimercaptopropane, dimercaptopropane sulfonate, and the acid form. The complete evaluation reports no translation issues and no known-record losses."
        },
        {
          "issue_id": "I-cf8f4c3c293ac3e842b3",
          "status": "resolved",
          "response": "The therapy-block warning no longer appears after removal of the malformed quoted expression and complete reevaluation of version 6.",
          "evidence": "The current therapy block retains the other DMPS-related terms. The full evaluation reports no translation warnings or issues and retrieves all 15 known records."
        },
        {
          "issue_id": "I-a31336ef43c569dcafec",
          "status": "resolved",
          "response": "The final-query warning no longer appears after removal of the malformed quoted expression and complete reevaluation of version 6.",
          "evidence": "The full strategy evaluation reports empty raw translation diagnostics and translation_issues, retrieves all 15 known records, and reports no known losses."
        }
      ]
    }
  ]
}
```

