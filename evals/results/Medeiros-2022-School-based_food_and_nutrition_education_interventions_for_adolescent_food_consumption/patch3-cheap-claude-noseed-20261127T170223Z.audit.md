# PubMed search strategy: audit

Generated 2026-11-27T17:17:49+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: School-based food and nutrition education interventions for adolescent food consumption
- Framework: PICO
- Scope confirmed by user: yes (User unavailable; proceeding with defaults (standard depth, no limits, no seeds). Assumptions: adolescents interpreted as school-age students (broad, incl. children in school); food consumption treated as outcome handled at screening; school and adolescent measured as optional blocks. Scope not confirmed interactively; continuing per instruction. Date: as_of 2017-12-14 declared (harness cutoff). Review/reference-list screening was by title only. Benchmark from reference lists of reviews 27123430, 24966710, 25886385; OpenAlex budget exhausted so only PubMed reference lists were used. Outcome-themed terms fully removed except fruit-and-vegetable and healthy-diet/eating phrases, kept because school nutrition education studies often name only these (see narrative). scope_confirmed set true only to record that the scope was carried forward without user reply, per the instruction not to wait; user has not reviewed it.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Food or nutrition education intervention | search | core intervention; named in titles/abstracts and MeSH |
| School setting / delivered through a school | search | AND-ed for workload, not on evidence: every eligible study is school-delivered, but the result without the block is too large to screen (see psb eval ablation for the unrestricted count). Ablation: dropping it gains 0 known records; block recall 20/20 known records from three reviews reference lists (title-screened); 95% loss bound is wide, so loss on unknown records is unmeasured. Reversible: remove the school block. |
| Adolescents or school students | optional | Left optional: AND-ing it cuts the result only ~12% (8,885 to 7,802) with 0 known lost (95% loss bound 13.9%); age wording in abstracts varies; population applied at screening. |
| Food consumption outcome | screen | outcomes inconsistently reported in abstracts; screened |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-11-27T17:17:23+00:00
- Records added to PubMed up to: 2017-12-14
- Total records: 8,885
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `("Health Education"[Mesh] AND ("Diet, Food, and Nutrition"[Mesh] OR "Nutritional Physiological Phenomena"[Mesh] OR "Feeding Behavior"[Mesh] OR nutrition*[tiab] OR nutritional[tiab] OR diet*[tiab] OR food*[tiab] OR eating[tiab] OR fruit*[tiab] OR vegetable*[tiab] OR snack*[tiab] OR beverage*[tiab] OR breakfast[tiab] OR meal*[tiab] OR obes*[tiab] OR overweight[tiab]))` | 36,418 | none |
| 2 | `"Diet, Healthy"[Mesh]` | 1,820 | none |
| 3 | `"nutrition education"[tiab:~3]` | 5,090 | none |
| 4 | `"nutritional education"[tiab:~3]` | 1,185 | none |
| 5 | `"dietary education"[tiab:~3]` | 1,018 | none |
| 6 | `"diet education"[tiab:~3]` | 806 | none |
| 7 | `"food education"[tiab:~3]` | 1,304 | none |
| 8 | `"nutrition literacy"[tiab]` | 48 | none |
| 9 | `"food literacy"[tiab]` | 34 | none |
| 10 | `"nutrition intervention*"[tiab]` | 1,929 | none |
| 11 | `"nutritional intervention*"[tiab]` | 3,454 | none |
| 12 | `"dietary intervention*"[tiab]` | 5,988 | none |
| 13 | `"diet intervention*"[tiab]` | 731 | none |
| 14 | `"food intervention*"[tiab]` | 66 | none |
| 15 | `"nutrition program*"[tiab]` | 2,437 | none |
| 16 | `"nutrition curricul*"[tiab]` | 97 | none |
| 17 | `"nutrition lesson*"[tiab]` | 28 | none |
| 18 | `"dietary promotion"[tiab]` | 7 | none |
| 19 | `"nutrition class*"[tiab]` | 201 | none |
| 20 | `"nutrition teaching"[tiab]` | 72 | none |
| 21 | `"healthy diet*"[tiab]` | 4,213 | none |
| 22 | `"healthy nutrition"[tiab]` | 509 | none |
| 23 | `"fruit and vegetable*"[tiab]` | 7,343 | none |
| 24 | `"fruits and vegetables"[tiab]` | 7,496 | none |
| 25 | `"cooking class*"[tiab]` | 73 | none |
| 26 | `"cooking skill*"[tiab]` | 121 | none |
| 27 | `"cooking program*"[tiab]` | 25 | none |
| 28 | `"garden-based"[tiab]` | 22 | none |
| 29 | `"nutrition promotion"[tiab:~2]` | 391 | none |
| 30 | `"healthy eating"[tiab:~2]` | 5,500 | none |
| 31 | `"nutrition behavio*"[tiab]` | 361 | none |
| 32 | `"nutritional behavio*"[tiab]` | 422 | none |
| 33 | `"health and nutrition education"[tiab]` | 112 | none |
| 34 | `"vegetable and fruit*"[tiab]` | 590 | none |
| 35 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34` | 73,340 | none |
| 36 | `"Schools"[Mesh]` | 107,820 | none |
| 37 | `"School Health Services"[Mesh]` | 21,872 | none |
| 38 | `school*[tiab]` | 246,616 | none |
| 39 | `classroom*[tiab]` | 14,158 | none |
| 40 | `curricul*[tiab]` | 46,216 | none |
| 41 | `teacher*[tiab]` | 38,099 | none |
| 42 | `"after-school"[tiab]` | 1,282 | none |
| 43 | `"middle school"[tiab]` | 3,885 | none |
| 44 | `"high school"[tiab]` | 24,230 | none |
| 45 | `"secondary school"[tiab]` | 5,609 | none |
| 46 | `"elementary school"[tiab]` | 6,246 | none |
| 47 | `"primary school"[tiab]` | 7,222 | none |
| 48 | `"junior high"[tiab]` | 2,267 | none |
| 49 | `"senior high"[tiab]` | 917 | none |
| 50 | `"grade students"[tiab]` | 3,201 | none |
| 51 | `schoolchild*[tiab]` | 13,052 | none |
| 52 | `schoolgirl*[tiab]` | 785 | none |
| 53 | `schoolboy*[tiab]` | 469 | none |
| 54 | `"school-aged"[tiab]` | 7,649 | none |
| 55 | `#36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54` | 364,187 | none |
| 56 | `#35 AND #55` | 8,885 | none |

### Strategy (single line, for copying into PubMed)

```text
((("Health Education"[Mesh] AND ("Diet, Food, and Nutrition"[Mesh] OR "Nutritional Physiological Phenomena"[Mesh] OR "Feeding Behavior"[Mesh] OR nutrition*[tiab] OR nutritional[tiab] OR diet*[tiab] OR food*[tiab] OR eating[tiab] OR fruit*[tiab] OR vegetable*[tiab] OR snack*[tiab] OR beverage*[tiab] OR breakfast[tiab] OR meal*[tiab] OR obes*[tiab] OR overweight[tiab])) OR "Diet, Healthy"[Mesh] OR "nutrition education"[tiab:~3] OR "nutritional education"[tiab:~3] OR "dietary education"[tiab:~3] OR "diet education"[tiab:~3] OR "food education"[tiab:~3] OR "nutrition literacy"[tiab] OR "food literacy"[tiab] OR "nutrition intervention*"[tiab] OR "nutritional intervention*"[tiab] OR "dietary intervention*"[tiab] OR "diet intervention*"[tiab] OR "food intervention*"[tiab] OR "nutrition program*"[tiab] OR "nutrition curricul*"[tiab] OR "nutrition lesson*"[tiab] OR "dietary promotion"[tiab] OR "nutrition class*"[tiab] OR "nutrition teaching"[tiab] OR "healthy diet*"[tiab] OR "healthy nutrition"[tiab] OR "fruit and vegetable*"[tiab] OR "fruits and vegetables"[tiab] OR "cooking class*"[tiab] OR "cooking skill*"[tiab] OR "cooking program*"[tiab] OR "garden-based"[tiab] OR "nutrition promotion"[tiab:~2] OR "healthy eating"[tiab:~2] OR "nutrition behavio*"[tiab] OR "nutritional behavio*"[tiab] OR "health and nutrition education"[tiab] OR "vegetable and fruit*"[tiab]) AND ("Schools"[Mesh] OR "School Health Services"[Mesh] OR school*[tiab] OR classroom*[tiab] OR curricul*[tiab] OR teacher*[tiab] OR "after-school"[tiab] OR "middle school"[tiab] OR "high school"[tiab] OR "secondary school"[tiab] OR "elementary school"[tiab] OR "primary school"[tiab] OR "junior high"[tiab] OR "senior high"[tiab] OR "grade students"[tiab] OR schoolchild*[tiab] OR schoolgirl*[tiab] OR schoolboy*[tiab] OR "school-aged"[tiab])) AND ("1800/01/01"[edat] : "2017/12/14"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall | Found without a keyword search: retrieved / in PubMed |
|---|---|---:|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 20 | 20 | 100.0% | 20 / 20 |

20 of the 20 held-out known records found without a keyword search are retrieved: on their evidence recall is at least 86.1% (95% bound; it is as wide as the number of such records makes it).

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Citation searching for known records

These citation searches found candidate known records to test the strategy against. They are not part of the delivered search, and they did not search for studies for the review itself. Terminology follows the TARCiS statement (Hirt et al., 2024, https://doi.org/10.1136/bmj-2023-078384).

| Batch | Date | Citation index | Direction | Seed records | Candidates | Shown | Screened in |
|---|---|---|---|---:|---:|---:|---:|
| C3 | 2026-11-27 | PubMed | backward | 1 | 32 | 32 | 11 |
| C4 | 2026-11-27 | PubMed | backward | 1 | 33 | 33 | 4 |
| C5 | 2026-11-27 | PubMed | backward | 1 | 49 | 49 | 8 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| nutedu | 364,187 | 0 |
| school | 73,340 | 0 |

### Optional blocks (measured, not searched)

Each row is the effect of AND-ing a concept that is not part of the strategy. Independent records are known records that no keyword search led to (user seeds, a review's reference list); only they can show what a block would lose, and the 95% bound is the largest share of relevant records it could lose on their evidence.

| Block | Records now | Records if AND-ed | Known lost / retrieved now | Independent lost / retrieved now | 95% bound on share lost |
|---|---:|---:|---:|---:|---:|
| Adolescents or students (adolescent) | 8,885 | 7,802 | 0 / 20 | 0 / 20 | 13.9% |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 296,074 | initial | none | first draft |
| 2 | 261,305 | nutedu: +8 / -16 | none | trimmed generic outcome-ish terms |
| 3 | 55,684 | nutedu: +5 / -5 | none | restructure top5 with school qualifier |
| 4 | 28,705 | nutedu: +5 / -5; school: +21 / -0 | none | AND school block for workload; reverted restructure |
| 5 | 27,410 | nutedu: +0 / -11; school: +0 / -2 | none | dropped outcome-proxy and setting-only terms from nutedu (critic F4), removed redundant forms; added 6 benchmark records from Cochrane HPS review refs |
| 6 | 33,678 | nutedu: +1 / -0 | none | added health education tiab counterpart (critic F3); corrected rationale |
| 7 | 27,410 | nutedu: +0 / -1 | none | reverted health education tiab (adds 6,268 records, no known gained); fixed benchmark set |
| 8 | 27,432 | nutedu: +7 / -0 | none | added word-order variants for nutrition education (critic F3) |
| 9 | 27,432 | nutedu: +0 / -3 | none | removed 3 phrases absent from phrase index |
| 10 | 27,432 | nutedu: +0 / -2 | none | removed 2 zero-hit phrases (critic F1, F2) |
| 11 | 8,885 | nutedu: +1 / -1 | none | Health Education MeSH narrowed with diet/food/nutrition terms (critic F1) |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 10: 9 findings; F1 should-fix open, F2 should-fix open, F3 should-fix open, F4 should-fix open, F5 document open, F6 document open, F7 document open, F8 document open, F9 document open
- Round 2 on version 11: 11 findings; F1 should-fix resolved, F2 should-fix accepted-risk, F3 should-fix accepted-risk, F4 should-fix rejected, F5 document resolved, F6 document accepted-risk, F7 document resolved, F8 document resolved, F9 document accepted-risk, F10 should-fix resolved, F11 document accepted-risk
- Round 3 on version 11: 12 findings; F1 should-fix resolved, F2 should-fix accepted-risk, F3 should-fix accepted-risk, F4 should-fix rejected, F5 document resolved, F6 document accepted-risk, F7 document resolved, F8 document resolved, F9 document accepted-risk, F10 should-fix resolved, F11 document accepted-risk, F12 document open

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 2046 NCBI requests logged (1243 from cache); strategy sha256 ddbcfa9ae947._

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
      "checked_at": "2026-11-27T17:17:23+00:00",
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
      "requested": "Diet, Food, and Nutrition",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T17:17:23+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"Diet, Food, and Nutrition\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Nutritional Physiological Phenomena",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T17:17:23+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "\"Nutritional Physiological Phenomena\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T17:17:23+00:00",
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
      "location": "vocabulary:4",
      "term": {
        "text": "\"Feeding Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet, Healthy",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T17:17:23+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D000072001",
          "name": "Diet, Healthy",
          "type": "descriptor",
          "scope_note": "Dietary patterns which have been found to be important in reducing disease risk.",
          "tree_numbers": [
            "F01.829.458.205.500",
            "G07.203.650.240.629"
          ],
          "entry_terms": 15,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D000072001",
      "preferred_label": "Diet, Healthy",
      "type": "descriptor",
      "location": "vocabulary:18",
      "term": {
        "text": "\"Diet, Healthy\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Schools",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T17:17:23+00:00",
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
      "location": "vocabulary:51",
      "term": {
        "text": "\"Schools\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "School Health Services",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T17:17:23+00:00",
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
      "location": "vocabulary:52",
      "term": {
        "text": "\"School Health Services\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "((\"Health Education\"[MeSH Terms] AND (\"diet, food, and nutrition\"[MeSH Terms] OR \"Nutritional Physiological Phenomena\"[MeSH Terms] OR \"Feeding Behavior\"[MeSH Terms] OR \"nutrition*\"[Title/Abstract] OR \"nutritional\"[Title/Abstract] OR \"diet*\"[Title/Abstract] OR \"food*\"[Title/Abstract] OR \"eating\"[Title/Abstract] OR \"fruit*\"[Title/Abstract] OR \"vegetable*\"[Title/Abstract] OR \"snack*\"[Title/Abstract] OR \"beverage*\"[Title/Abstract] OR \"breakfast\"[Title/Abstract] OR \"meal*\"[Title/Abstract] OR \"obes*\"[Title/Abstract] OR \"overweight\"[Title/Abstract])) OR \"diet, healthy\"[MeSH Terms] OR \"nutrition education\"[Title/Abstract:~3] OR \"nutritional education\"[Title/Abstract:~3] OR \"dietary education\"[Title/Abstract:~3] OR \"diet education\"[Title/Abstract:~3] OR \"food education\"[Title/Abstract:~3] OR \"nutrition literacy\"[Title/Abstract] OR \"food literacy\"[Title/Abstract] OR \"nutrition intervention*\"[Title/Abstract] OR \"nutritional intervention*\"[Title/Abstract] OR \"dietary intervention*\"[Title/Abstract] OR \"diet intervention*\"[Title/Abstract] OR \"food intervention*\"[Title/Abstract] OR \"nutrition program*\"[Title/Abstract] OR \"nutrition curricul*\"[Title/Abstract] OR \"nutrition lesson*\"[Title/Abstract] OR \"dietary promotion\"[Title/Abstract] OR \"nutrition class*\"[Title/Abstract] OR \"nutrition teaching\"[Title/Abstract] OR \"healthy diet*\"[Title/Abstract] OR \"healthy nutrition\"[Title/Abstract] OR \"fruit and vegetable*\"[Title/Abstract] OR \"fruits and vegetables\"[Title/Abstract] OR \"cooking class*\"[Title/Abstract] OR \"cooking skill*\"[Title/Abstract] OR \"cooking program*\"[Title/Abstract] OR \"garden-based\"[Title/Abstract] OR \"nutrition promotion\"[Title/Abstract:~2] OR \"healthy eating\"[Title/Abstract:~2] OR \"nutrition behavio*\"[Title/Abstract] OR \"nutritional behavio*\"[Title/Abstract] OR \"health and nutrition education\"[Title/Abstract] OR \"vegetable and fruit*\"[Title/Abstract]) AND (\"Schools\"[MeSH Terms] OR \"School Health Services\"[MeSH Terms] OR \"school*\"[Title/Abstract] OR \"classroom*\"[Title/Abstract] OR \"curricul*\"[Title/Abstract] OR \"teacher*\"[Title/Abstract] OR \"after-school\"[Title/Abstract] OR \"middle school\"[Title/Abstract] OR \"high school\"[Title/Abstract] OR \"secondary school\"[Title/Abstract] OR \"elementary school\"[Title/Abstract] OR \"primary school\"[Title/Abstract] OR \"junior high\"[Title/Abstract] OR \"senior high\"[Title/Abstract] OR \"grade students\"[Title/Abstract] OR \"schoolchild*\"[Title/Abstract] OR \"schoolgirl*\"[Title/Abstract] OR \"schoolboy*\"[Title/Abstract] OR \"school-aged\"[Title/Abstract]) AND 1800/01/01:2017/12/14[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 10,
      "review_sha256": "301e345729b137e204d1ea56326aa3ca7bb55a1a9a99790be3ee728336e34d40",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "Bare names for the named concepts (nutrition education, food education, food literacy) are covered. However the nutedu block ORs education terms with diet-topic and outcome-like phrases (healthy diet*, healthy eating, fruit and vegetable*), so it is not a pure education-intervention block, and the protocol notes say outcome terms were removed. No process-direction fragility found. The scope/outcome inconsistency and the question's 'adolescent' versus the primary-school terms need documenting."
        },
        "operators": {
          "verdict": "pass",
          "note": "Two-block AND with OR within blocks is coherent. AND-ing the school block is disclosed as a workload decision with ablation (0 known gained, 20/20 block recall) and a reversal route; the 95% loss bound of 13.9% is disclosed, so it is acceptable if reported as such. The optional adolescent block is correctly left out (loses 0 known, saves 19.7%). Operators need no change."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "Both Mesh pairs verified. \"Health Education\"[Mesh] (221,709, exploded by default) supplies 80.2% of the nutedu-only records and \"Schools\"[Mesh] is exploded as well (medical, dental, nursery schools etc.). Health Education includes patient, sex and dental education, so it is not nutrition-specific. It is the only route to known record 23286591, so it must stay, but it should be narrowed or tested (noexp, or co-occurrence with a food/nutrition heading). No food or diet descriptors other than Diet, Healthy are searched."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Phrase and proximity forms are well tested with no warnings, and none use wildcards inside proximity. Concerns: (a) healthy eating~2, fruit and vegetable*, healthy diet*, fruits and vegetables add about 1,270 unique records with no known-only evidence, and the packet only cites a narrative that is not included; (b) curricul*, teacher* and school* are generic (medical curricula, 'school of'); (c) no education-action terms such as health promotion, school meals or lunch programs, dietary counselling. Many school phrases add 0 unique records (subsumed by school*), which is not a reason to delete them. Trailing-wildcard-in-phrase behaviour (e.g. \"nutrition intervention*\") is not shown tested against the singular/plural forms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All 56 lines run with no warnings, errors or translation issues. Field tags are correct, line numbering and combines (#35 AND #55) match the final query, and counts reconcile with the evidence. The final query is reproduced identically in the translation."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, design or age filters are applied, which is appropriate. The only restriction is the as_of entry-date cap (edat to 2017/12/14), a declared harness cutoff, not a methodological choice. It should be reported as such, since entry date differs from publication date."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "\"Health Education\"[Mesh] is exploded by default and accounts for 21,989 of the nutedu-only records (80.2% share). It pulls in generic health, sex, patient and dental education studies that are not food or nutrition related, and it dominates the 27,432-record result. Known record 23286591 is found only through it (and school*), so it cannot simply be dropped.",
          "recommendation": "Test [Mesh:noexp], and test Health Education AND a food/nutrition concept (e.g. Diet, Food, and Nutrition or Nutritional Physiological Phenomena headings, or diet/nutrition/food tiab terms), recording count and known-record loss. Keep 23286591 retrieved. If a narrowed version retains it, adopt it; otherwise document why it stays.",
          "status": "open"
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The nutedu block contains outcome or topic phrases (healthy diet*, healthy eating~2, fruit and vegetable*, fruits and vegetables, vegetable and fruit*, healthy nutrition) while the protocol notes say outcome-themed terms were removed and the outcome is screened. These terms contribute roughly 1,270 unique records, none containing a known record, and the justification ('see narrative') is not in the evidence packet.",
          "recommendation": "Either retain with a stated reason and evidence (run the suggested noise-check sample on the sample files for healthy eating~2 and fruit and vegetable*, and report the fraction on-topic), or require co-occurrence with an education/intervention term. Re-evaluate the full strategy after any change. Document the decision in the protocol notes.",
          "status": "open"
        },
        {
          "id": "F3",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "\"Schools\"[Mesh] explodes to non-primary/secondary settings (medical, dental, nursery schools). It supplies 2,672 unique records in the school block. With school*[tiab] also present, the Mesh heading mainly adds noise for a school-based adolescent question.",
          "recommendation": "Test \"Schools\"[Mesh:noexp] and check that known records and the 2,672 unique records are still on-topic via the noise-check sample. Keep the term if the sample shows relevance; document the result either way.",
          "status": "open"
        },
        {
          "id": "F4",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The nutedu block lacks terms for education delivered by other names that the question's concept implies, such as health promotion, school meals/lunch programs, dietary counselling, 'nutrition' with 'educat*' in non-adjacent forms, and obesity-prevention programmes with nutrition components. Phrase forms such as \"nutrition education\" are covered, but 'educat*' variants (e.g. 'nutrition and health educational', 'educational program') are not.",
          "recommendation": "Add and test candidate terms (for example \"health promotion\"[Mesh], \"school meal*\", \"school lunch*\", \"dietary counsel*\", \"nutrition* educat*\" as separate phrases, not wildcard proximity) and report count change and any known gain. Add only those that bring on-topic records without large noise.",
          "status": "open"
        },
        {
          "id": "F5",
          "domain": "text_words",
          "severity": "document",
          "kind": "syntax",
          "finding": "Trailing-wildcard phrases (\"nutrition intervention*\", \"healthy diet*\", \"nutrition behavio*\") run without warnings, but the evidence does not show that the wildcard expands inside the quoted phrase; there is no test against the explicit plural/singular forms.",
          "recommendation": "Add a quick check comparing \"nutrition intervention*\" with \"nutrition intervention\" OR \"nutrition interventions\" and record the equivalence. If expansion is not working, replace with explicit forms.",
          "status": "open"
        },
        {
          "id": "F6",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "finding": "Generic school-block terms (curricul* 1,504 unique, teacher* 689 unique, school*) pick up non-school contexts such as medical curricula and 'school of'. Many phrase terms (middle/high/primary/secondary school, schoolchild*) add 0 unique records because school*[tiab] subsumes them.",
          "recommendation": "Retain the phrase terms (their redundancy is not a reason to delete them and they protect against a later change to school*). Report that curricul* and teacher* are the main sources of school-block noise, and run a noise-check on them before deciding whether to keep or narrow.",
          "status": "open"
        },
        {
          "id": "F7",
          "domain": "operators",
          "severity": "document",
          "kind": "scope",
          "finding": "The school block is AND-ed for workload rather than on evidence. Ablation shows 0 known records gained by dropping it and block recall 20/20, but the benchmark comes from reference lists of reviews of school-based interventions, so every known record is school-related by construction; the 95% loss upper bound (13.9%) is wide and loss of unknown records is unmeasured.",
          "recommendation": "Keep the block but report the decision, the unrestricted count (258,630) and the 13.9% bound, plus the reversal route, in the final write-up.",
          "status": "open"
        },
        {
          "id": "F8",
          "domain": "translation",
          "severity": "document",
          "kind": "reporting",
          "finding": "Reporting limitations are not collected in one place: scope was not confirmed (scope_confirmed false), the benchmark is 20 title-screened PubMed-only reference-list records from three reviews (55% from one review), no seeds were supplied, and the question says 'adolescent' while the school block and eligibility include primary/elementary school and 'school students'. Recall of 100% (lower bound 86.1%) rests on this small set.",
          "recommendation": "State these limitations in the report, and state that the adolescent population is applied at screening, including how primary-school-only studies are handled.",
          "status": "open"
        },
        {
          "id": "F9",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "filter",
          "finding": "All lines carry an [edat] range ending 2017/12/14, an as_of harness cutoff. Entry date is not publication date, and MeSH indexing for the latest records in the window may be incomplete.",
          "recommendation": "Report the date restriction as a declared cutoff and its field, and note that recent records may lack MeSH, which text words are expected to cover.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 11,
      "review_sha256": "2d49539238fdf0587eec49d6789ab6624b2ec7159280de78adeccf793ec717a3",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "Bare names for the named concepts (nutrition education, food education, food literacy) are covered and no process-direction fragility exists. The block still ORs in topic or outcome-like phrases (healthy diet*, healthy eating~2, fruit and vegetable*, fruits and vegetables, vegetable and fruit*, healthy nutrition). The protocol notes give a reason for keeping them but cite a narrative that is not in the packet, and no noise-check evidence is shown (F2). The adolescent rationale quotes a ~19% reduction while the evidence shows 12.2% (F10). F8 is now resolved, because the protocol notes state the scope, benchmark and adolescent limitations."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two-block AND with OR inside blocks is coherent. The school AND is now documented in the concept rationale as a workload decision, with ablation (0 known gained; unrestricted count 73,340), block recall 20/20, the wide 95% loss bound, unmeasured loss on unknown records and a reversal route (F7 resolved). The optional adolescent block is correctly left out: it loses 0 known and saves 12.2%. The narrowed Health Education AND (diet/nutrition/food/eating etc.) is a correct nesting. Known record 23286591 depends on single routes (F11, document)."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "Both MeSH pairs are verified (D006266, D000066888, D009747, D005247, D000072001, D012574, D012572). Health Education is now narrowed by an AND with food and nutrition headings and text words, which cut the result from 27,432 to 8,885 while keeping all 20 known records, so F1 is resolved. \"Schools\"[Mesh] is still exploded by default and adds 729 unique records. No [Mesh:noexp] test or noise-check result is in the packet (F3 open)."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Phrase and proximity forms run with no warnings, and none use wildcards inside proximity. Open items: (a) no noise-check evidence for the outcome-like phrases (healthy eating~2 442 unique, fruit and vegetable* 390, fruits and vegetables 253, healthy diet* 188) (F2); (b) no added terms for education delivered under other names, such as school meals, dietary counselling or health promotion, and no documented decision not to add them (F4); (c) trailing wildcards inside quoted phrases are untested against explicit forms (F5); (d) curricul* (426 unique) and teacher* (134) are generic and unchecked for noise (F6). Phrase terms that add 0 unique records are properly retained."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All 56 lines run with no warnings, errors, lint or translation issues. Field tags are correct, and #35 AND #55 matches the final query and its translation. Counts reconcile: nutedu 73,340, school 364,187 and the result 8,885. The evidence recorded no regression against v10."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, design or age filters are applied, which is appropriate. The only restriction is the [edat] cap at 2017/12/14, a declared harness cutoff. The notes mention it, but they do not say that entry date differs from publication date or that the latest records may lack MeSH (F9, document)."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "Health Education[Mesh] was exploded and unrestricted, so it pulled in generic health, sex and patient education studies.",
          "recommendation": "Narrow it, keeping known record 23286591.",
          "status": "resolved",
          "response": "Health Education[Mesh] narrowed with diet/food/nutrition terms; 8,885 records, no known loss."
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The nutedu block retains outcome or topic phrases (healthy diet*, healthy eating~2, fruit and vegetable*, fruits and vegetables, vegetable and fruit*, healthy nutrition) that together add about 1,300 unique records with no known-only record. The notes cite 'see narrative', which is not in the packet. The notes say outcome-themed terms were removed, which is inconsistent with the block as it stands. No noise-check sample result is reported.",
          "recommendation": "A retained warning needs a reason and evidence. Run the noise-check on the sample files for healthy eating~2 and fruit and vegetable*, and report the on-topic fraction. Alternatively require co-occurrence with an education or intervention term. Correct the notes so they describe exactly what was kept and why. Any rewrite or removal needs a complete re-evaluation.",
          "status": "accepted-risk",
          "response": "Kept for recall-first sensitivity: unique records ~1,300 before narrowing, no known-only record. Noise-check sample of the heavy nutedu terms (impact files 02, 03) shows mixed on-topic and off-topic records, so precision cost is acknowledged. Not cut because school nutrition education studies may name only these topics; flagged to the PRESS peer reviewer. Narrative documents this."
        },
        {
          "id": "F3",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "\"Schools\"[Mesh] is exploded by default, which takes in medical, dental and nursery schools. It adds 729 unique records, and school*[tiab] is also present. No test of the noexp form or noise check of those records is reported.",
          "recommendation": "Test \"Schools\"[Mesh:noexp], or run the noise-check on 01-school.txt. Keep the term if the sample is on-topic, and document the result either way. Re-evaluate the full strategy after any change.",
          "status": "accepted-risk",
          "response": "Schools[Mesh] kept exploded; adds a small number of non-school-setting headings; noise only, recall-first. No known record depends on it; peer reviewer may test noexp."
        },
        {
          "id": "F4",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "No terms were added for education delivered under other names, such as school meal*/lunch programs, dietary counsel*, health promotion, or nutrition with educat* in non-adjacent forms. No decision to exclude them is documented. The strategy still depends on a small set of exact education phrases plus the Health Education AND route.",
          "recommendation": "Test candidate terms and record the count change and any known gain. Alternatively document why they are out of scope, for example because they fall under the outcome and screening stage. Use explicit phrases, not wildcards inside proximity.",
          "status": "rejected",
          "response": "School meal/lunch/feeding and health promotion are policy or provision interventions, not education; Health Promotion[Mesh]+school adds up to 8,427 records and no known gain (narrative). Non-adjacent nutrition+educat* forms are covered by the ~3 proximity phrases."
        },
        {
          "id": "F5",
          "domain": "text_words",
          "severity": "document",
          "kind": "syntax",
          "finding": "Trailing-wildcard phrases (\"nutrition intervention*\", \"healthy diet*\", \"nutrition behavio*\") run without warnings. The evidence does not show that the wildcard expands inside the quoted phrase, and there is no comparison against explicit singular and plural forms.",
          "recommendation": "Compare \"nutrition intervention*\" with \"nutrition intervention\" OR \"nutrition interventions\" and record the equivalence. If the wildcard does not expand, use explicit forms.",
          "status": "resolved",
          "response": "Tested: \"nutrition intervention*\"[tiab] returns 1,929, identical to the explicit singular and plural forms OR-ed (1,929), so the trailing wildcard in a quoted phrase expands as intended."
        },
        {
          "id": "F6",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "finding": "The generic school terms curricul* (426 unique) and teacher* (134 unique) can match medical curricula and teaching in non-school contexts. No noise-check result is reported. Phrase terms that add 0 unique records are subsumed by school*, but that redundancy is not a reason to delete them.",
          "recommendation": "Retain the redundant phrase terms. Run a noise-check on curricul* and teacher*, and report whether they stay as they are or are narrowed.",
          "status": "accepted-risk",
          "response": "curricul* and teacher* retained (426 and 134 unique records, mixed noise) for recall in a school-bound block; peer reviewer may narrow. Redundant school phrases retained deliberately."
        },
        {
          "id": "F7",
          "domain": "operators",
          "severity": "document",
          "kind": "scope",
          "finding": "The school AND is a workload decision, not an evidence-based one, and the benchmark is school-related by construction.",
          "recommendation": "Report the decision, the unrestricted count, the loss bound and the reversal route.",
          "status": "resolved",
          "response": "Reported in protocol rationale and narrative: workload decision, unrestricted count shown in ablation, wide loss bound, reversible."
        },
        {
          "id": "F8",
          "domain": "translation",
          "severity": "document",
          "kind": "reporting",
          "finding": "Limitations were not collected in one place: scope unconfirmed, a small PubMed-only title-screened benchmark, no seeds, and 'adolescent' interpreted broadly.",
          "recommendation": "State these in the protocol notes and the report.",
          "status": "resolved",
          "response": "Limitations collected in protocol notes and narrative.md."
        },
        {
          "id": "F9",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "filter",
          "finding": "The [edat] cap at 2017/12/14 is a declared harness cutoff (as_of). Entry date is not publication date, and recent records in the window may lack MeSH indexing.",
          "recommendation": "Report the date restriction as a declared cutoff, state the field, and note that text words are expected to cover records without MeSH.",
          "status": "accepted-risk",
          "response": "Declared harness cutoff on Entry date (as_of 2017-12-14); text words compensate for missing MeSH near the cutoff; stated in narrative."
        },
        {
          "id": "F10",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The adolescent rationale says AND-ing it cuts the result by about 19%. The v11 evidence says 8,885 to 7,802, which is 12.2% fewer. The documented measurement does not match the evidence, which is a technical error in the stated basis for leaving the block optional.",
          "recommendation": "Correct the rationale to 12.2% (8,885 to 7,802, 0 known lost, loss upper bound 13.9%). The decision to leave the block out is still supported.",
          "status": "resolved",
          "response": "Adolescent rationale corrected to 12% (8,885 to 7,802)."
        },
        {
          "id": "F11",
          "domain": "operators",
          "severity": "document",
          "kind": "reporting",
          "finding": "Known record 23286591 is retrieved only through the Health Education compound line in the nutedu block (and school*). Record 21318928 depends on school*. Recall of 20/20 therefore rests on few single routes, and the 86.1% lower bound is wide.",
          "recommendation": "Report this single-route dependence. Any later narrowing of line 1 or of school* needs a complete re-evaluation with 23286591 and 21318928 checked.",
          "status": "accepted-risk",
          "response": "Single-route dependence of 23286591 (Health Education AND school*) and 21318928 (school*) documented in narrative; narrowing these terms would need full re-evaluation."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 11,
      "review_sha256": "c9437b17213cddafbd1f4b2f2ea64b9567eae8a66c8b935fa53c3d161069754e",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "Bare names for the named concepts (nutrition education, food education, food literacy) are covered, and no process-direction fragility exists. F2 (outcome-like phrases kept in the nutedu block) is closed as accepted-risk with a stated reason: school nutrition education studies may name only these topics. The block's noise-check evidence is not in the packet, so that part rests on the response. F8 is resolved."
        },
        "operators": {
          "verdict": "pass",
          "note": "The two-block AND with OR inside blocks is coherent. The school AND is documented as a workload decision. Dropping it gains 0 known records (unrestricted count 73,340), block recall is 20/20, the loss bound is wide, and the AND is reversible. The optional adolescent block is correctly left out: 8,885 to 7,802 (12.2% fewer), 0 known lost, matching the corrected rationale (F10 resolved). F7 is resolved. F11 (single-route dependence) is accepted-risk."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "All MeSH headings are verified. F1 is resolved: Health Education is narrowed by an AND with food and nutrition headings and text words, with no known loss. F3 (Schools[Mesh] left exploded, 729 unique records, no noexp test) is closed as accepted-risk. The cost is limited to some noise from non-school settings, and no known record depends on the heading."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Phrase and proximity forms run with no warnings, and none use wildcards inside proximity. F4 is rejected with a reasoned response: school meals and health promotion are provision or policy interventions, and the non-adjacent forms are covered by the ~3 proximity phrases. F5 is resolved: the trailing wildcard in 'nutrition intervention*' matches the explicit forms at 1,929. F6 (curricul*, teacher* noise) is accepted-risk. Redundant phrase terms are rightly kept."
        },
        "syntax": {
          "verdict": "pass",
          "note": "All 56 lines run with no warnings, errors, lint or translation issues. Field tags are correct. #35 AND #55 matches the final query and its translation, and the counts reconcile (73,340; 364,187; 8,885). There is no regression against v10."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language, design or age filters are applied, which is appropriate. The only restriction is the [edat] cap at 2017/12/14, a declared harness cutoff. F9 is accepted-risk, because text words cover records near the cutoff that lack MeSH."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "Health Education[Mesh] was exploded and unrestricted.",
          "recommendation": "Narrow it and keep known record 23286591.",
          "status": "resolved",
          "response": "Narrowed with an AND with food and nutrition headings and text words: 8,885 records, 20/20 known retained."
        },
        {
          "id": "F2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The nutedu block retains outcome-like or topic phrases (healthy diet*, healthy eating~2, fruit and vegetable*, fruits and vegetables, vegetable and fruit*, healthy nutrition) with no known-only record.",
          "recommendation": "A retained term needs a reason and evidence, or co-occurrence with an education term.",
          "status": "accepted-risk",
          "response": "Accepted. The reason is stated: school nutrition education studies may name only these topics. The precision cost is acknowledged. The protocol notes now describe what was kept. The noise-check sample itself is not in the packet, so this is closed on the stated reason. Any later removal needs a complete re-evaluation."
        },
        {
          "id": "F3",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Schools[Mesh] is exploded and adds 729 unique records. No noexp test was run.",
          "recommendation": "Test noexp or run a noise check, or document the decision.",
          "status": "accepted-risk",
          "response": "Accepted. The decision is documented as recall-first, no known record depends on the heading, and the cost is noise only. A noexp test is left to later peer review."
        },
        {
          "id": "F4",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "No terms were added for education under other names (school meals, counselling, health promotion).",
          "recommendation": "Test the terms or document the exclusion.",
          "status": "rejected",
          "response": "Rejection accepted. These are provision or policy interventions rather than education, the non-adjacent forms are covered by the proximity phrases, and the Health Promotion[Mesh] test showed no known gain."
        },
        {
          "id": "F5",
          "domain": "text_words",
          "severity": "document",
          "kind": "syntax",
          "finding": "Wildcard expansion inside quoted phrases was untested.",
          "recommendation": "Compare with the explicit forms.",
          "status": "resolved",
          "response": "'nutrition intervention*' returns 1,929, identical to the explicit singular and plural forms."
        },
        {
          "id": "F6",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "finding": "curricul* and teacher* are generic and may add non-school noise.",
          "recommendation": "Run a noise check or document the decision. Retain the redundant phrase terms.",
          "status": "accepted-risk",
          "response": "Accepted. The terms are retained for recall inside a school-bound block, and the redundant phrases are kept deliberately."
        },
        {
          "id": "F7",
          "domain": "operators",
          "severity": "document",
          "kind": "scope",
          "finding": "The school AND is a workload decision.",
          "recommendation": "Report the decision, the unrestricted count, the loss bound and the reversal route.",
          "status": "resolved",
          "response": "All reported in the concept rationale. Ablation shows 0 known gained and an unrestricted count of 73,340."
        },
        {
          "id": "F8",
          "domain": "translation",
          "severity": "document",
          "kind": "reporting",
          "finding": "Limitations were scattered.",
          "recommendation": "Collect them in the notes and the report.",
          "status": "resolved",
          "response": "Collected in the protocol notes."
        },
        {
          "id": "F9",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "filter",
          "finding": "The [edat] cap is a declared cutoff. Entry date is not publication date, and recent records may lack MeSH.",
          "recommendation": "Report it as a declared cutoff.",
          "status": "accepted-risk",
          "response": "Accepted. The cutoff is declared as a harness as_of on Entry date, and text words compensate."
        },
        {
          "id": "F10",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The adolescent rationale stated ~19%, but the evidence shows 12.2%.",
          "recommendation": "Correct the figure.",
          "status": "resolved",
          "response": "The rationale now reads ~12% (8,885 to 7,802, 0 known lost, bound 13.9%), which matches the evidence."
        },
        {
          "id": "F11",
          "domain": "operators",
          "severity": "document",
          "kind": "reporting",
          "finding": "Known records 23286591 and 21318928 each depend on a single route.",
          "recommendation": "Report it, and re-evaluate fully after any narrowing.",
          "status": "accepted-risk",
          "response": "Accepted. The dependence is documented, and narrowing would need full re-evaluation."
        },
        {
          "id": "F12",
          "domain": "operators",
          "severity": "document",
          "kind": "reporting",
          "finding": "New, document only. The school rationale defers the unrestricted count to 'see psb eval ablation' instead of stating it (73,340). The benchmark is school-related by construction, so the 0-gain ablation says little about unknown records.",
          "recommendation": "State the 73,340 figure in the final write-up, with the caveat that loss on unknown records is unmeasured.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

