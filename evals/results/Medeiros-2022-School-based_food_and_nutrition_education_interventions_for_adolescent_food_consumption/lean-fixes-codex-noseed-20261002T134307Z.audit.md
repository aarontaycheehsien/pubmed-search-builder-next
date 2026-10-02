# PubMed search strategy: audit

Generated 2026-10-02T13:59:18+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: School-based food and nutrition education interventions for adolescent food consumption
- Framework: PICO
- Scope confirmed by user: yes (No known relevant articles were supplied. User requested no follow-up questions; scope and roles are provisional assumptions. PubMed records are bounded by Entrez date 2017-12-14 via PSB_AS_OF, with no publication-date limit. Food-consumption outcome and school delivery are screening criteria, not required search blocks. A targeted PubMed pilot identified one relevant prior review, but its included-study references could not be retrieved with the available skill tool; seven candidate records were screened by abstract and added as a development set.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Education or health-promotion component | search | The intervention includes an educational component, named in text or indexed as health education; school delivery remains for screening. |
| Food, diet, and nutrition topic | search | Every eligible intervention addresses food or nutrition; broad controlled vocabulary and text terms will capture varied dietary topic wording. |
| Adolescents or school students | search | Population is central to eligibility; adolescent, child, and student headings and text terms cover the criteria's alternatives. |
| Delivered through a school | search | School delivery is an explicit defining eligibility criterion and was named or indexed for the screened relevant records; broad school and classroom terms plus school headings are included. |
| Eligible food-consumption outcome | screen | Consumption outcomes are inconsistently reported in records and will be judged during screening. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-02T13:58:15+00:00
- Records added to PubMed up to: 2017-12-14
- Total records: 11,418
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Health Education"[Mesh]` | 221,709 | none |
| 2 | `"Health Promotion"[Mesh]` | 70,478 | none |
| 3 | `educat*[tiab]` | 513,190 | none |
| 4 | `teach*[tiab]` | 165,464 | none |
| 5 | `curriculum[tiab]` | 35,866 | none |
| 6 | `lesson*[tiab]` | 50,204 | none |
| 7 | `instruction*[tiab]` | 53,676 | none |
| 8 | `program*[tiab]` | 750,384 | none |
| 9 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8` | 1,443,791 | none |
| 10 | `"Diet, Food, and Nutrition"[Mesh]` | 993,016 | none |
| 11 | `"Nutritional Sciences"[Mesh]` | 18,906 | none |
| 12 | `"Child Nutrition Sciences"[Mesh]` | 1,076 | none |
| 13 | `"Nutritional Physiological Phenomena"[Mesh]` | 549,510 | none |
| 14 | `"Feeding Behavior"[Mesh]` | 156,434 | none |
| 15 | `"Diet"[Mesh]` | 254,824 | none |
| 16 | `nutrition*[tiab]` | 244,227 | none |
| 17 | `diet*[tiab]` | 494,942 | none |
| 18 | `food*[tiab]` | 387,680 | none |
| 19 | `eating[tiab]` | 61,958 | none |
| 20 | `feeding[tiab]` | 172,589 | none |
| 21 | `#10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20` | 1,590,321 | none |
| 22 | `"Adolescent"[Mesh]` | 1,895,608 | none |
| 23 | `"Students"[Mesh]` | 112,971 | none |
| 24 | `"Child"[Mesh]` | 1,797,170 | none |
| 25 | `adolescen*[tiab]` | 248,945 | none |
| 26 | `teen*[tiab]` | 26,895 | none |
| 27 | `youth[tiab]` | 57,369 | none |
| 28 | `student*[tiab]` | 234,078 | none |
| 29 | `schoolchild*[tiab]` | 13,052 | none |
| 30 | `schoolchildren[tiab]` | 12,947 | none |
| 31 | `pupil*[tiab]` | 26,074 | none |
| 32 | `child*[tiab]` | 1,257,861 | none |
| 33 | `#22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32` | 3,392,932 | none |
| 34 | `"Schools"[Mesh]` | 107,820 | none |
| 35 | `"School Health Services"[Mesh]` | 21,872 | none |
| 36 | `school*[tiab]` | 246,627 | none |
| 37 | `classroom*[tiab]` | 14,159 | none |
| 38 | `#34 OR #35 OR #36 OR #37` | 316,648 | none |
| 39 | `#9 AND #21 AND #33 AND #38` | 11,418 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Health Education"[Mesh] OR "Health Promotion"[Mesh] OR educat*[tiab] OR teach*[tiab] OR curriculum[tiab] OR lesson*[tiab] OR instruction*[tiab] OR program*[tiab]) AND ("Diet, Food, and Nutrition"[Mesh] OR "Nutritional Sciences"[Mesh] OR "Child Nutrition Sciences"[Mesh] OR "Nutritional Physiological Phenomena"[Mesh] OR "Feeding Behavior"[Mesh] OR "Diet"[Mesh] OR nutrition*[tiab] OR diet*[tiab] OR food*[tiab] OR eating[tiab] OR feeding[tiab]) AND ("Adolescent"[Mesh] OR "Students"[Mesh] OR "Child"[Mesh] OR adolescen*[tiab] OR teen*[tiab] OR youth[tiab] OR student*[tiab] OR schoolchild*[tiab] OR schoolchildren[tiab] OR pupil*[tiab] OR child*[tiab]) AND ("Schools"[Mesh] OR "School Health Services"[Mesh] OR school*[tiab] OR classroom*[tiab])) AND ("1800/01/01"[edat] : "2017/12/14"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 7 | 7 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| education | 24,645 | 0 |
| nutrition | 98,556 | 0 |
| population | 13,455 | 0 |
| setting | 45,547 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 45,547 | initial | none | Initial three-block strategy: education and health-promotion, food/diet/nutrition, and adolescent/student population; school setting and consumption outcome remain screening criteria. MeSH and text layers included for each searched concept. |
| 2 | 45,547 | limits/combination | none | Aligned protocol concepts with the three searched blocks and use default AND combination so leave-one-block-out ablation is available. |
| 3 | 11,418 | setting: +4 / -0 | none | Added school and classroom setting as a search block because school delivery defines eligibility and was consistently named or indexed across screened records; tested broad MeSH and text vocabulary. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 3 (Same-context critic: no fresh-context reviewer was available in this run. Reviewed the full packet against all six PRESS domains.): 1 findings; setting-fulltext-risk document accepted-risk
- Round 2 on version 3 (Same-context second revision-round review of the current packet. No new strategy changes were indicated; the documented setting risk is carried forward.): 1 findings; setting-fulltext-risk document accepted-risk
- Round 3 on version 3 (Same-context closing round: verified the current packet and prior dispositions. No independent fresh-context reviewer was available.): 1 findings; setting-fulltext-risk document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 690 NCBI requests logged (292 from cache); strategy sha256 71b54ce200fa._

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
      "requested": "Health Education",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:58:15+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D006266",
          "name": "Health Education",
          "type": "descriptor",
          "scope_note": "Education that increases the awareness and favorably influences the knowledge, attitudes, and behaviors relating to the improvement of health on a personal or community basis.",
          "tree_numbers": [
            "H02.403.720.750.380",
            "N02.421.726.407"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D006266",
      "preferred_label": "Health Education",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "\"Health Education\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Promotion",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:58:15+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D006293",
          "name": "Health Promotion",
          "type": "descriptor",
          "scope_note": "Encouraging consumer behaviors most likely to optimize health potentials (physical and psychosocial) through health information, preventive programs, and access to medical care.",
          "tree_numbers": [
            "H02.403.720.750.380.579",
            "N02.421.726.407.579"
          ],
          "entry_terms": 16,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D006293",
      "preferred_label": "Health Promotion",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "\"Health Promotion\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet, Food, and Nutrition",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:58:15+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000066888",
          "name": "Diet, Food, and Nutrition",
          "type": "descriptor",
          "scope_note": "Concepts involved with nutritional physiology, including categories of substances eaten for sustenance, nutritional phenomena and processes, eating patterns and habits, and measurable nutritional parameters.",
          "tree_numbers": [
            "G07.203"
          ],
          "entry_terms": 0,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000066888",
      "preferred_label": "Diet, Food, and Nutrition",
      "type": "descriptor",
      "location": "vocabulary:9",
      "term": {
        "text": "\"Diet, Food, and Nutrition\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Nutritional Sciences",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:58:15+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D052756",
          "name": "Nutritional Sciences",
          "type": "descriptor",
          "scope_note": "The study of NUTRITION PROCESSES as well as the components of food, their actions, interaction, and balance in relation to health and disease.",
          "tree_numbers": [
            "H02.533"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D052756",
      "preferred_label": "Nutritional Sciences",
      "type": "descriptor",
      "location": "vocabulary:10",
      "term": {
        "text": "\"Nutritional Sciences\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Child Nutrition Sciences",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:58:15+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D053198",
          "name": "Child Nutrition Sciences",
          "type": "descriptor",
          "scope_note": "The study of NUTRITION PROCESSES as well as the components of food, their actions, interaction, and balance in relation to health and disease of children, infants or adolescents.",
          "tree_numbers": [
            "H02.533.252"
          ],
          "entry_terms": 35,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D053198",
      "preferred_label": "Child Nutrition Sciences",
      "type": "descriptor",
      "location": "vocabulary:11",
      "term": {
        "text": "\"Child Nutrition Sciences\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Nutritional Physiological Phenomena",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:58:15+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D009747",
          "name": "Nutritional Physiological Phenomena",
          "type": "descriptor",
          "scope_note": "The processes and properties of living organisms by which they take in and balance the use of nutritive materials for energy, heat production, or building material for the growth, maintenance, or repair of tissues and the nutritive properties of FOOD.",
          "tree_numbers": [
            "G07.203.650"
          ],
          "entry_terms": 45,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D009747",
      "preferred_label": "Nutritional Physiological Phenomena",
      "type": "descriptor",
      "location": "vocabulary:12",
      "term": {
        "text": "\"Nutritional Physiological Phenomena\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:58:15+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D005247",
          "name": "Feeding Behavior",
          "type": "descriptor",
          "scope_note": "Behavioral responses or sequences associated with eating including modes of feeding, rhythmic patterns of eating, and time intervals.",
          "tree_numbers": [
            "F01.145.113.547",
            "F01.145.407",
            "G07.203.650.353"
          ],
          "entry_terms": 35,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D005247",
      "preferred_label": "Feeding Behavior",
      "type": "descriptor",
      "location": "vocabulary:13",
      "term": {
        "text": "\"Feeding Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:58:15+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D004032",
          "name": "Diet",
          "type": "descriptor",
          "scope_note": "Regular course of eating and drinking adopted by a person or animal.",
          "tree_numbers": [
            "G07.203.650.240"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D004032",
      "preferred_label": "Diet",
      "type": "descriptor",
      "location": "vocabulary:14",
      "term": {
        "text": "\"Diet\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adolescent",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:58:15+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000293",
          "name": "Adolescent",
          "type": "descriptor",
          "scope_note": "A person 13 to 18 years of age.",
          "tree_numbers": [
            "M01.060.057"
          ],
          "entry_terms": 16,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000293",
      "preferred_label": "Adolescent",
      "type": "descriptor",
      "location": "vocabulary:20",
      "term": {
        "text": "\"Adolescent\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Students",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:58:15+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D013334",
          "name": "Students",
          "type": "descriptor",
          "scope_note": "Individuals enrolled in a school or formal educational program.",
          "tree_numbers": [
            "M01.848"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D013334",
      "preferred_label": "Students",
      "type": "descriptor",
      "location": "vocabulary:21",
      "term": {
        "text": "\"Students\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Child",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:58:15+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D002648",
          "name": "Child",
          "type": "descriptor",
          "scope_note": "A person 6 to 12 years of age. An individual 2 to 5 years old is CHILD, PRESCHOOL.",
          "tree_numbers": [
            "M01.060.406"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D002648",
      "preferred_label": "Child",
      "type": "descriptor",
      "location": "vocabulary:22",
      "term": {
        "text": "\"Child\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Schools",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:58:15+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012574",
          "name": "Schools",
          "type": "descriptor",
          "scope_note": "Educational institutions.",
          "tree_numbers": [
            "I02.783",
            "J03.832"
          ],
          "entry_terms": 9,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012574",
      "preferred_label": "Schools",
      "type": "descriptor",
      "location": "vocabulary:31",
      "term": {
        "text": "\"Schools\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "School Health Services",
      "expected_type": "descriptor",
      "checked_at": "2026-10-02T13:58:15+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012572",
          "name": "School Health Services",
          "type": "descriptor",
          "scope_note": "Preventive health services provided for students. It excludes college or university students.",
          "tree_numbers": [
            "N02.421.726.809"
          ],
          "entry_terms": 23,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012572",
      "preferred_label": "School Health Services",
      "type": "descriptor",
      "location": "vocabulary:32",
      "term": {
        "text": "\"School Health Services\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Health Education\"[MeSH Terms] OR \"Health Promotion\"[MeSH Terms] OR \"educat*\"[Title/Abstract] OR \"teach*\"[Title/Abstract] OR \"curriculum\"[Title/Abstract] OR \"lesson*\"[Title/Abstract] OR \"instruction*\"[Title/Abstract] OR \"program*\"[Title/Abstract]) AND (\"diet, food, and nutrition\"[MeSH Terms] OR \"Nutritional Sciences\"[MeSH Terms] OR \"Child Nutrition Sciences\"[MeSH Terms] OR \"Nutritional Physiological Phenomena\"[MeSH Terms] OR \"Feeding Behavior\"[MeSH Terms] OR \"Diet\"[MeSH Terms] OR \"nutrition*\"[Title/Abstract] OR \"diet*\"[Title/Abstract] OR \"food*\"[Title/Abstract] OR \"eating\"[Title/Abstract] OR \"feeding\"[Title/Abstract]) AND (\"Adolescent\"[MeSH Terms] OR \"Students\"[MeSH Terms] OR \"Child\"[MeSH Terms] OR \"adolescen*\"[Title/Abstract] OR \"teen*\"[Title/Abstract] OR \"youth\"[Title/Abstract] OR \"student*\"[Title/Abstract] OR \"schoolchild*\"[Title/Abstract] OR \"schoolchildren\"[Title/Abstract] OR \"pupil*\"[Title/Abstract] OR \"child*\"[Title/Abstract]) AND (\"Schools\"[MeSH Terms] OR \"School Health Services\"[MeSH Terms] OR \"school*\"[Title/Abstract] OR \"classroom*\"[Title/Abstract]) AND 1800/01/01:2017/12/14[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 3,
      "review_sha256": "4aad5ed26c1a19d1de80f9924fcf38c54a602a0ff7da2425ad52ea171b7afb69",
      "note": "Same-context critic: no fresh-context reviewer was available in this run. Reviewed the full packet against all six PRESS domains.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched blocks map to the intervention's education, food/nutrition, population, and school-delivery eligibility components. The consumption outcome is screened. The school block is a deliberate context search because school delivery is explicit eligibility; MeSH and broad title/abstract terms are present."
        },
        "operators": {
          "verdict": "pass",
          "note": "Default AND combines the concept blocks and each block uses OR for synonyms. No NOT, proximity, or nested Boolean clauses are used."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Every selected descriptor has been verified through the skill's MeSH authority check. MeSH and text-word layers are included for all searched concepts; headings are exploded by default. Nutrition Education is not a valid heading in this vocabulary, so Health Education plus food/diet/nutrition headings are used."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Terms cover nutrition/diet/food, education and teaching, adolescents/children/students, and school/classroom wording. Safe truncation is used. Objective frequent terms from the screened set (dietary, health education, health promotion, schools, diet) are already covered."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All query terms are explicitly field tagged; PubMed translations show no warnings or translation issues, and lint is clean."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No date, language, age, study-design, or other search filters were added. The Entrez-date bound is the requested as-of setting, not a publication-date filter."
        }
      },
      "findings": [
        {
          "id": "setting-fulltext-risk",
          "domain": "translation",
          "severity": "document",
          "kind": "structural",
          "block": "setting",
          "finding": "The required school block may miss eligible reports when school delivery is described only in the full text or is poorly indexed. The development set is small and was screened from a topic-focused pilot, so 7/7 retrieval is not independent validation.",
          "recommendation": "Retain the broad school/classroom MeSH and text layer because school delivery defines eligibility and improves manageability; disclose the risk and request specialist review of the setting decision.",
          "status": "accepted-risk",
          "response": "Accepted with limitation: school delivery is an explicit inclusion criterion; the block includes exploded Schools and School Health Services headings plus school* and classroom* text terms, and all seven screened development records are retrieved. The strategy remains empirically unvalidated beyond this convenience development set, so the school block needs PRESS peer review and sensitivity checking against additional known studies."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 3,
      "review_sha256": "4aad5ed26c1a19d1de80f9924fcf38c54a602a0ff7da2425ad52ea171b7afb69",
      "note": "Same-context second revision-round review of the current packet. No new strategy changes were indicated; the documented setting risk is carried forward.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The role of the setting block is supported by the explicit inclusion criterion. Its possible full-text-only reporting is already documented as an accepted risk."
        },
        "operators": {
          "verdict": "pass",
          "note": "Default AND and within-block OR remain appropriate."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Verified headings and explosive use remain appropriate, with both MeSH and text terms in each block."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The topic, population, and setting vocabulary is broad and captures all seven screened records. No unaddressed objective term is needed; mined terms are already covered."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The current evaluation reports no translation issues or technical blockers."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No unjustified PubMed filters are present; the Entrez date cutoff is required by the run instructions."
        }
      },
      "findings": [
        {
          "id": "setting-fulltext-risk",
          "domain": "translation",
          "severity": "document",
          "kind": "structural",
          "block": "setting",
          "finding": "The required school block may miss eligible reports when school delivery is described only in the full text or is poorly indexed. The development set is small and was screened from a topic-focused pilot, so 7/7 retrieval is not independent validation.",
          "recommendation": "Retain broad school/classroom terms because school delivery defines eligibility; document the risk for an information specialist.",
          "status": "accepted-risk",
          "response": "Retained with this limitation: exploded Schools and School Health Services MeSH plus school* and classroom* text terms retrieve all seven screened development records. PRESS peer review should examine additional records and the setting requirement."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 3,
      "review_sha256": "4aad5ed26c1a19d1de80f9924fcf38c54a602a0ff7da2425ad52ea171b7afb69",
      "note": "Same-context closing round: verified the current packet and prior dispositions. No independent fresh-context reviewer was available.",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The school block remains a justified but risk-bearing search representation of explicit eligibility; the prior finding is carried as accepted-risk for PRESS peer review."
        },
        "operators": {
          "verdict": "pass",
          "note": "Default AND and OR combination are valid."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The selected headings remain verified and are combined with text terms."
        },
        "text_words": {
          "verdict": "pass",
          "note": "No missing critical text vocabulary was identified from the search and screened records; the mined common terms are already represented."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax, tag, translation, or lint problems remain."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No discretionary limits or filters are used; the Entrez bound is part of the requested historical search frame."
        }
      },
      "findings": [
        {
          "id": "setting-fulltext-risk",
          "domain": "translation",
          "severity": "document",
          "kind": "structural",
          "block": "setting",
          "finding": "The required school block may miss eligible reports when school delivery is described only in the full text or is poorly indexed. The development set is small and was screened from a topic-focused pilot, so 7/7 retrieval is not independent validation.",
          "recommendation": "Retain broad school/classroom terms because school delivery defines eligibility; document the risk for an information specialist.",
          "status": "accepted-risk",
          "response": "Accepted as a documented risk: the block includes exploded Schools and School Health Services MeSH plus school* and classroom* text terms and retrieves all seven screened development records. This is not independent validation; additional known studies and the school block should be reviewed by an information specialist."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

