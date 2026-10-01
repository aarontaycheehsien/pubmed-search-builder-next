# PubMed search strategy: audit

Generated 2026-10-01T12:48:55+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Comparative effectiveness of common therapies for Wilson disease
- Framework: PICO
- Scope confirmed by user: yes (User asked to proceed without clarification. Assumed comparative effectiveness means human comparative clinical evaluation of established medical therapies (for example, chelators and zinc-based treatment) for Wilson disease; comparators, outcomes, and designs are screening criteria. No age, language, or publication-date limits. PubMed Entrez date bounded through PSB_AS_OF=2018-12-23 on every command; no [dp] cutoff. No user-supplied known articles. Scope confirmation is by documented assumption per user instruction.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Wilson disease | search | The target condition is essential to the review and is reliably named/indexed. |
| Medical therapies for Wilson disease | search | The intervention defines the effectiveness question. Relevant records may name individual therapies rather than the category, so the block must include treatment members and be probed. |
| Comparators among therapies | screen | Comparators are inconsistently described and should not be required in a recall-first query. |
| Comparative effectiveness outcomes | screen | Effectiveness and harms may not be named consistently in titles/abstracts. |
| Comparative clinical study designs | screen | No ad hoc design block; screen for eligible comparative studies. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T12:48:11+00:00
- Records added to PubMed up to: 2018-12-23
- Total records: 3,026
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Hepatolenticular Degeneration"[Mesh]` | 5,697 | none |
| 2 | `"Wilson disease"[tiab]` | 5,545 | none |
| 3 | `"Wilson's disease"[tiab]` | 4,158 | none |
| 4 | `Wilson's[tiab]` | 4,762 | none |
| 5 | `Wilsons[tiab]` | 4,692 | none |
| 6 | `hepatolenticular[tiab]` | 975 | none |
| 7 | `"Kinnier-Wilson"[tiab]` | 38 | none |
| 8 | `"hepatocerebral degeneration"[tiab]` | 142 | none |
| 9 | `"copper storage disease"[tiab]` | 25 | none |
| 10 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9` | 7,893 | none |
| 11 | `"Penicillamine"[Mesh]` | 7,878 | none |
| 12 | `"Trientine"[Mesh]` | 380 | none |
| 13 | `"Zinc Compounds"[Mesh]` | 12,484 | none |
| 14 | `"Zinc"[Mesh]` | 58,485 | none |
| 15 | `"Zinc Acetate"[Mesh]` | 246 | none |
| 16 | `penicillamine[tiab]` | 6,853 | none |
| 17 | `treatment[tiab]` | 3,933,275 | none |
| 18 | `therap*[tiab]` | 2,661,898 | none |
| 19 | `trientine[tiab]` | 219 | none |
| 20 | `triethylenetetramine[tiab]` | 360 | none |
| 21 | `zinc[tiab]` | 108,490 | none |
| 22 | `tetrathiomolybdate[tiab]` | 351 | none |
| 23 | `"ammonium tetrathiomolybdate"[tiab]` | 84 | none |
| 24 | `molybdate[tiab]` | 3,049 | none |
| 25 | `chelat*[tiab]` | 62,346 | none |
| 26 | `"zinc therapy"[tiab]` | 353 | none |
| 27 | `"zinc therapies"[tiab]` | 3 | none |
| 28 | `"zinc supplement*"[tiab]` | 2,571 | none |
| 29 | `"zinc acetate"[tiab]` | 817 | none |
| 30 | `"zinc sulfate"[tiab]` | 1,531 | none |
| 31 | `"anti-copper therapy"[tiab]` | 6 | none |
| 32 | `"copper chelat*"[tiab]` | 1,179 | none |
| 33 | `#11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32` | 5,628,014 | none |
| 34 | `#10 AND #33` | 3,026 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Hepatolenticular Degeneration"[Mesh] OR "Wilson disease"[tiab] OR "Wilson's disease"[tiab] OR Wilson's[tiab] OR Wilsons[tiab] OR hepatolenticular[tiab] OR "Kinnier-Wilson"[tiab] OR "hepatocerebral degeneration"[tiab] OR "copper storage disease"[tiab]) AND ("Penicillamine"[Mesh] OR "Trientine"[Mesh] OR "Zinc Compounds"[Mesh] OR "Zinc"[Mesh] OR "Zinc Acetate"[Mesh] OR penicillamine[tiab] OR treatment[tiab] OR therap*[tiab] OR trientine[tiab] OR triethylenetetramine[tiab] OR zinc[tiab] OR tetrathiomolybdate[tiab] OR "ammonium tetrathiomolybdate"[tiab] OR molybdate[tiab] OR chelat*[tiab] OR "zinc therapy"[tiab] OR "zinc therapies"[tiab] OR "zinc supplement*"[tiab] OR "zinc acetate"[tiab] OR "zinc sulfate"[tiab] OR "anti-copper therapy"[tiab] OR "copper chelat*"[tiab])) AND ("1800/01/01"[edat] : "2018/12/23"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Medical therapies for Wilson disease | 1 | `Drug Therapy[Mesh] OR treat*[tiab] OR therap*[tiab] OR drug*[tiab] OR chelat*[tiab] OR supplement*[tiab] OR zinc[tiab] OR copper[tiab]` | 2,767 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| wilson_disease | 5,628,014 | 0 |
| therapy | 7,893 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial two-block recall-first strategy: Wilson disease plus named medical therapy members and treatment-class vocabulary; no seeds available. |
| 2 | 1,942 | wilson_disease: +10 / -0; therapy: +20 / -0 | none | Corrected strategy structure to explicit term arrays and retained MeSH plus title/abstract layers for both required concepts. |
| 3 | 1,903 | wilson_disease: +0 / -1; therapy: +0 / -1 | none | Removed ambiguous generic Chelating Agents MeSH term (authority lookup returned ambiguous duplicate entries; chelat* remains in text) and zero-hit neurohepatic degeneration phrase after count review. |
| 4 | 1,903 | limits/combination | none | Use the default AND combination so the category probe can exclude and measure the therapy block as required by psb. |
| 5 | 3,026 | therapy: +3 / -0 | none | Added Zinc MeSH discovered in screened record indexing and treatment/therapy wording mined from the relevant development records to cover descriptions that name the process generically. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5: 1 findings; R1-F1 must-fix rejected
- Round 2 on version 5: 1 findings; R1-F1 must-fix rejected

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 442 NCBI requests logged (231 from cache); strategy sha256 48275f446e6d._

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
      "checked_at": "2026-10-01T12:48:11+00:00",
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
      "requested": "Penicillamine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:48:11+00:00",
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
      "location": "vocabulary:10",
      "term": {
        "text": "\"Penicillamine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Trientine",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:48:11+00:00",
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
      "location": "vocabulary:11",
      "term": {
        "text": "\"Trientine\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc Compounds",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:48:11+00:00",
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
      "location": "vocabulary:12",
      "term": {
        "text": "\"Zinc Compounds\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:48:11+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D015032",
          "name": "Zinc",
          "type": "descriptor",
          "scope_note": "A metallic element of atomic number 30 and atomic weight 65.38. It is a necessary trace element in the diet, forming an essential part of many enzymes, and playing an important role in protein synthesis and in cell division. Zinc deficiency is associated with ANEMIA, short stature, HYPOGONADISM, impaired WOUND HEALING, and geophagia. It is known by the symbol Zn.",
          "tree_numbers": [
            "D01.268.556.940",
            "D01.268.956.906",
            "D01.552.544.940"
          ],
          "entry_terms": 0,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D015032",
      "preferred_label": "Zinc",
      "type": "descriptor",
      "location": "vocabulary:13",
      "term": {
        "text": "\"Zinc\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Zinc Acetate",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:48:11+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D019345",
          "name": "Zinc Acetate",
          "type": "descriptor",
          "scope_note": "A salt produced by the reaction of zinc oxide with acetic acid and used as an astringent, styptic, and emetic.",
          "tree_numbers": [
            "D02.241.081.018.165.750"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D019345",
      "preferred_label": "Zinc Acetate",
      "type": "descriptor",
      "location": "vocabulary:14",
      "term": {
        "text": "\"Zinc Acetate\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Hepatolenticular Degeneration\"[MeSH Terms] OR \"Wilson disease\"[Title/Abstract] OR \"Wilson's disease\"[Title/Abstract] OR \"Wilson's\"[Title/Abstract] OR \"Wilsons\"[Title/Abstract] OR \"hepatolenticular\"[Title/Abstract] OR \"Kinnier-Wilson\"[Title/Abstract] OR \"hepatocerebral degeneration\"[Title/Abstract] OR \"copper storage disease\"[Title/Abstract]) AND (\"Penicillamine\"[MeSH Terms] OR \"Trientine\"[MeSH Terms] OR \"Zinc Compounds\"[MeSH Terms] OR \"Zinc\"[MeSH Terms] OR \"Zinc Acetate\"[MeSH Terms] OR \"Penicillamine\"[Title/Abstract] OR \"treatment\"[Title/Abstract] OR \"therap*\"[Title/Abstract] OR \"Trientine\"[Title/Abstract] OR \"triethylenetetramine\"[Title/Abstract] OR \"Zinc\"[Title/Abstract] OR \"tetrathiomolybdate\"[Title/Abstract] OR \"ammonium tetrathiomolybdate\"[Title/Abstract] OR \"molybdate\"[Title/Abstract] OR \"chelat*\"[Title/Abstract] OR \"zinc therapy\"[Title/Abstract] OR \"zinc therapies\"[Title/Abstract] OR \"zinc supplement*\"[Title/Abstract] OR \"Zinc Acetate\"[Title/Abstract] OR \"zinc sulfate\"[Title/Abstract] OR \"anti-copper therapy\"[Title/Abstract] OR \"copper chelat*\"[Title/Abstract]) AND 1800/01/01:2018/12/23[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "68f965bfd65bf303c94b0904f04b343ece5a133b12550ded91cf1c40e3d06620",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The disease and therapy blocks match the documented assumed scope; comparators, outcomes, and design remain for screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR joins terms within each concept and AND joins disease with therapy. No NOT or unvalidated design filter is used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "All retained MeSH headings are included with title/abstract terms. The ambiguous generic chelating-agent heading was removed."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The strategy includes common named chelators, zinc-based therapy, tetrathiomolybdate, and generic treatment wording. The category probe found no relevant records in its sample of 30."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Evaluation reports no remaining syntax, translation, or lint problems."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The upper Entrez date bound is required by the task harness, is recorded as protocol as_of=2018-12-23, and PubMed translates it as Date - Entry, not publication date. Removing it would violate the required historical-index snapshot."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The applied Entrez date range ends on 2018-12-23. This omits records entered after that date, including potentially relevant studies, despite the scope specifying no date limits.",
          "recommendation": "Remove the historical entry-date bound or extend it through the intended search date, then rerun and reevaluate the complete strategy. If the review intentionally covers evidence only through 2018-12-23, revise the scope to state that cutoff explicitly.",
          "status": "rejected",
          "response": "The task harness explicitly requires modeling PubMed as of 2018-12-23, and PSB_AS_OF=2018-12-23 has been set on every PubMed command. The protocol records this as an Entrez-entry cutoff, distinct from the review's publication-date limits; PubMed's tested translation shows 1800/01/01:2018/12/23[Date - Entry], not [dp]. The recommendation's own alternative (an intentional evidence cutoff) therefore applies. Removing or extending the bound would violate the user's harness instruction and use later-indexed literature."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 5,
      "review_sha256": "68f965bfd65bf303c94b0904f04b343ece5a133b12550ded91cf1c40e3d06620",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The strategy matches the documented scope: disease and therapy are searched, while comparators, outcomes, and study design remain screening criteria."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR combines terms within each concept and AND combines disease with therapy; no NOT or unvalidated design filter is used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The retained disease and therapy headings are paired with text words, and the earlier note records removal of the ambiguous generic chelating-agent heading."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The therapy block includes named treatments and generic treatment wording. The documented category probe found no relevant records among 30 sampled records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "Evaluation reports no remaining syntax, translation, or lint problems."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The prior date-bound finding is explicitly addressed: the required historical PubMed snapshot uses an Entrez entry-date cutoff, recorded in the protocol and confirmed by translation."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "limits_filters",
          "severity": "must-fix",
          "kind": "filter",
          "finding": "The applied Entrez date range ends on 2018-12-23 and excludes records entered after that date, despite the scope specifying no publication-date limits.",
          "recommendation": "Remove or extend the historical entry-date bound, or document an intentional evidence cutoff, then rerun and reevaluate the complete strategy.",
          "status": "rejected",
          "response": "The task harness requires modeling PubMed as of 2018-12-23, and that cutoff was applied to every PubMed command. The protocol records it as an Entrez entry-date cutoff, distinct from a publication-date limit; the tested translation confirms Date - Entry. The earlier recommendation's intentional-cutoff alternative is therefore met, and removing or extending the bound would violate the harness instruction."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

