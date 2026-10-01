# PubMed search strategy: audit

Generated 2026-10-01T12:35:13+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: School-based food and nutrition education interventions for adolescent food consumption
- Framework: PICO
- Scope confirmed by user: no (Standard depth. User supplied no known articles and cannot answer questions; proceeding with documented assumptions. Population includes adolescents and school students across grades when the student sample has relevant results; food-consumption outcomes include dietary intake, eating behavior/choice, food preference, and diet quality. Search education/intervention approach AND food/nutrition content. School delivery and consumption outcome were tested as optional blocks and AND-ed after screening 30-record loss samples and retaining 16 known records. Age/grade remains a screening criterion because indexing and abstract reporting are inconsistent. No language, geography, study-design, or publication-date limit. PSB_AS_OF=2017-12-14 applies the Entrez-date bound only; no publication-date cutoff was added. Scope was not user-confirmed; proceeding without pause was requested. The as-of date is an Entrez record-entry snapshot, not a publication-date restriction.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Education or nutrition intervention approach | search | Education delivery or intervention terminology is required; records use varied education, curriculum, program, health-promotion, and intervention labels, so a broad union is used. |
| Food or nutrition content | search | Every eligible intervention targets food or nutrition; records may name a specific member such as diet, eating behavior, food choice, or particular foods instead of the category. |
| Adolescents or school students | screen | Age and grade eligibility can be absent or poorly indexed, and includes varied school-age groups; screen titles, abstracts, and full texts. |
| Delivery through a school | optional | Setting is often named but can appear only in methods; evaluate its count reduction and loss sample before deciding. |
| Food-consumption outcomes | optional | This topic-defining outcome is searchable through dietary intake, eating behavior, food choice, and diet-quality wording but can be omitted from abstracts; evaluate before requiring it. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-10-01T12:33:37+00:00
- Records added to PubMed up to: 2017-12-14
- Total records: 6,539
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Health Education"[Mesh]` | 221,709 | none |
| 2 | `"Health Promotion"[Mesh]` | 70,478 | none |
| 3 | `education[tiab]` | 397,711 | none |
| 4 | `educat*[tiab]` | 513,190 | none |
| 5 | `teach*[tiab]` | 165,464 | none |
| 6 | `curricul*[tiab]` | 46,216 | none |
| 7 | `lesson*[tiab]` | 50,204 | none |
| 8 | `program*[tiab]` | 750,384 | none |
| 9 | `programme*[tiab]` | 167,402 | none |
| 10 | `intervention*[tiab]` | 788,474 | none |
| 11 | `"nutrition education"[tiab]` | 3,866 | none |
| 12 | `"nutrition instruction"[tiab]` | 46 | none |
| 13 | `"nutrition teaching"[tiab]` | 72 | none |
| 14 | `"nutrition curriculum"[tiab]` | 87 | none |
| 15 | `"nutrition curricula"[tiab]` | 11 | none |
| 16 | `"dietary education"[tiab]` | 252 | none |
| 17 | `"food education"[tiab]` | 84 | none |
| 18 | `"healthy eating education"[tiab]` | 7 | none |
| 19 | `"nutrition intervention*"[tiab]` | 1,929 | none |
| 20 | `"dietary intervention*"[tiab]` | 5,988 | none |
| 21 | `"nutrition program*"[tiab]` | 2,437 | none |
| 22 | `"nutrition programme*"[tiab]` | 275 | none |
| 23 | `"nutrition promotion"[tiab]` | 129 | none |
| 24 | `"healthy eating promotion"[tiab]` | 16 | none |
| 25 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24` | 2,017,304 | none |
| 26 | `"Child Nutrition Sciences"[Mesh]` | 1,076 | none |
| 27 | `"Adolescent Nutritional Physiological Phenomena"[Mesh]` | 1,486 | none |
| 28 | `"Diet"[Mesh]` | 254,824 | none |
| 29 | `"Feeding Behavior"[Mesh]` | 156,434 | none |
| 30 | `"Food Preferences"[Mesh]` | 13,063 | none |
| 31 | `nutrition*[tiab]` | 244,227 | none |
| 32 | `diet*[tiab]` | 494,942 | none |
| 33 | `food*[tiab]` | 387,680 | none |
| 34 | `"healthy eating"[tiab]` | 5,052 | none |
| 35 | `beverage*[tiab]` | 21,544 | none |
| 36 | `fruit*[tiab]` | 87,538 | none |
| 37 | `vegetable*[tiab]` | 46,125 | none |
| 38 | `#26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37` | 1,164,809 | none |
| 39 | `"School Health Services"[Mesh]` | 21,872 | none |
| 40 | `"Schools"[Mesh]` | 107,820 | none |
| 41 | `school*[tiab]` | 246,627 | none |
| 42 | `classroom*[tiab]` | 14,159 | none |
| 43 | `school-based[tiab]` | 10,873 | none |
| 44 | `school based[tiab]` | 10,873 | none |
| 45 | `in-school[tiab]` | 17,617 | none |
| 46 | `in school[tiab]` | 17,617 | none |
| 47 | `#39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46` | 316,648 | none |
| 48 | `"Diet"[Mesh]` | 254,824 | none |
| 49 | `"Feeding Behavior"[Mesh]` | 156,434 | none |
| 50 | `"Food Preferences"[Mesh]` | 13,063 | none |
| 51 | `"Energy Intake"[Mesh]` | 42,988 | none |
| 52 | `food consumption[tiab]` | 11,651 | none |
| 53 | `"food intake"[tiab]` | 39,819 | none |
| 54 | `"dietary intake"[tiab]` | 20,267 | none |
| 55 | `"energy intake"[tiab]` | 17,744 | none |
| 56 | `"fat intake"[tiab]` | 6,247 | none |
| 57 | `"eating behavior"[tiab]` | 3,945 | none |
| 58 | `"eating behaviours"[tiab]` | 774 | none |
| 59 | `"food choice"[tiab]` | 1,581 | none |
| 60 | `"food choices"[tiab]` | 2,415 | none |
| 61 | `"food preference*"[tiab]` | 2,104 | none |
| 62 | `"diet quality"[tiab]` | 2,540 | none |
| 63 | `"dietary behavior"[tiab]` | 822 | none |
| 64 | `"dietary behaviour"[tiab]` | 402 | none |
| 65 | `"fruit and vegetable intake"[tiab]` | 1,878 | none |
| 66 | `"beverage consumption"[tiab]` | 1,132 | none |
| 67 | `"food purchase*"[tiab]` | 456 | none |
| 68 | `"food sales"[tiab]` | 63 | none |
| 69 | `"eating behaviors"[tiab]` | 2,428 | none |
| 70 | `"eating behaviour"[tiab]` | 1,553 | none |
| 71 | `#48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70` | 404,112 | none |
| 72 | `#25 AND #38 AND #47 AND #71` | 6,539 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Health Education"[Mesh] OR "Health Promotion"[Mesh] OR education[tiab] OR educat*[tiab] OR teach*[tiab] OR curricul*[tiab] OR lesson*[tiab] OR program*[tiab] OR programme*[tiab] OR intervention*[tiab] OR "nutrition education"[tiab] OR "nutrition instruction"[tiab] OR "nutrition teaching"[tiab] OR "nutrition curriculum"[tiab] OR "nutrition curricula"[tiab] OR "dietary education"[tiab] OR "food education"[tiab] OR "healthy eating education"[tiab] OR "nutrition intervention*"[tiab] OR "dietary intervention*"[tiab] OR "nutrition program*"[tiab] OR "nutrition programme*"[tiab] OR "nutrition promotion"[tiab] OR "healthy eating promotion"[tiab]) AND ("Child Nutrition Sciences"[Mesh] OR "Adolescent Nutritional Physiological Phenomena"[Mesh] OR "Diet"[Mesh] OR "Feeding Behavior"[Mesh] OR "Food Preferences"[Mesh] OR nutrition*[tiab] OR diet*[tiab] OR food*[tiab] OR "healthy eating"[tiab] OR beverage*[tiab] OR fruit*[tiab] OR vegetable*[tiab]) AND ("School Health Services"[Mesh] OR "Schools"[Mesh] OR school*[tiab] OR classroom*[tiab] OR school-based[tiab] OR school based[tiab] OR in-school[tiab] OR in school[tiab]) AND ("Diet"[Mesh] OR "Feeding Behavior"[Mesh] OR "Food Preferences"[Mesh] OR "Energy Intake"[Mesh] OR food consumption[tiab] OR "food intake"[tiab] OR "dietary intake"[tiab] OR "energy intake"[tiab] OR "fat intake"[tiab] OR "eating behavior"[tiab] OR "eating behaviours"[tiab] OR "food choice"[tiab] OR "food choices"[tiab] OR "food preference*"[tiab] OR "diet quality"[tiab] OR "dietary behavior"[tiab] OR "dietary behaviour"[tiab] OR "fruit and vegetable intake"[tiab] OR "beverage consumption"[tiab] OR "food purchase*"[tiab] OR "food sales"[tiab] OR "eating behaviors"[tiab] OR "eating behaviour"[tiab])) AND ("1800/01/01"[edat] : "2017/12/14"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 16 | 16 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Delivery through a school | AND-ed | 64,146 / 6,539 | 89.8% | none | 0/30 (up to 10% of removed records could be relevant) | Fresh loss sample (30 records) screened against the criteria; none was an eligible school-delivered food/nutrition education intervention with an eligible consumption outcome. All 16 development records remain, and school delivery defines the question. |
| Food-consumption outcomes | AND-ed | 13,958 / 6,539 | 53.2% | none | 0/30 (up to 10% of removed records could be relevant) | Fresh loss sample (30 records) screened against all criteria; none met both the education-intervention and eligible food-consumption outcome requirements. Records on fruit distribution lacked a nutrition-education component or an eligible measured consumption outcome, and a school obesity program reported BMI rather than food consumption. All 16 development records remain. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Food or nutrition content | 1 | `Fruit[Mesh] OR Vegetables[Mesh] OR Beverages[Mesh] OR Dietary Fats[Mesh] OR Dietary Sugars[Mesh] OR Milk[Mesh] OR Food Services[Mesh] OR Energy Intake[Mesh]` | 2 | 0/2 |
| Food or nutrition content | 2 | `Fruit[Mesh] OR Vegetables[Mesh] OR Beverages[Mesh] OR Dietary Fats[Mesh] OR Dietary Sugars[Mesh] OR Milk[Mesh] OR Food Services[Mesh] OR Energy Intake[Mesh]` | 2 | 0/2 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| education_intervention | 11,609 | 0 |
| nutrition_content | 6,623 | 0 |
| school_setting | 64,146 | 0 |
| food_consumption | 13,958 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial broad intervention block with MeSH and title/abstract vocabulary; added school setting and food-consumption blocks as optional candidates. Five screened PubMed records form development set; no independent validation set. |
| 2 | 156,382 | nutrition_education: +0 / -19; education_intervention: +24 / -0; nutrition_content: +12 / -0 | none | Restructured to AND separate education/intervention approach and food/nutrition content, while keeping setting and outcome as optional candidates; added four clearly eligible records screened from PubMed pilot samples. Broad education MeSH alone was removed after excessive count and the missed TEENS record was examined. |
| 3 | 156,382 | limits/combination | none | Expanded the optional consumption block to include energy intake after eval showed the known eligible primary study PMID 27358261 lacked the original outcome vocabulary. No required strategy block changed. |
| 4 | 13,958 | school_setting: +8 / -0 | none | Added school setting to blocks after 16 relevant records, no known losses, a 30-record clean loss sample, and 91.1% count reduction; re-evaluating outcome candidate against the new base. |
| 5 | 6,499 | food_consumption: +21 / -0 | none | Added the food-consumption block after its 30-record loss sample had no relevant records, the block retained all 16 known studies, and it reduced the post-school query by 53.4%; proceed to category probe and re-evaluate. |
| 6 | 6,539 | food_consumption: +2 / -0 | none | Added US plural and UK singular eating-behavior spellings per critic F1. F2's Entrez cutoff reporting reminder is recorded; no publication-date restriction is used. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5: 2 findings; F1 should-fix open, F2 document accepted-risk
- Round 2 on version 6: 2 findings; F1 should-fix resolved, F2 document accepted-risk
- Round 3 on version 6: 2 findings; F1 should-fix resolved, F2 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 2213 NCBI requests logged (1151 from cache); strategy sha256 fdb682933d65._

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
      "checked_at": "2026-10-01T12:33:37+00:00",
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
      "checked_at": "2026-10-01T12:33:37+00:00",
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
      "requested": "Child Nutrition Sciences",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:33:37+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "\"Child Nutrition Sciences\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adolescent Nutritional Physiological Phenomena",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:33:37+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D017195",
          "name": "Adolescent Nutritional Physiological Phenomena",
          "type": "descriptor",
          "scope_note": "Nutritional physiology of children aged 13-18 years.",
          "tree_numbers": [
            "G07.203.650.220.060"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D017195",
      "preferred_label": "Adolescent Nutritional Physiological Phenomena",
      "type": "descriptor",
      "location": "vocabulary:26",
      "term": {
        "text": "\"Adolescent Nutritional Physiological Phenomena\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:33:37+00:00",
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
      "location": "vocabulary:27",
      "term": {
        "text": "\"Diet\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:33:37+00:00",
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
      "location": "vocabulary:28",
      "term": {
        "text": "\"Feeding Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Food Preferences",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:33:37+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D005518",
          "name": "Food Preferences",
          "type": "descriptor",
          "scope_note": "The selection of one food over another.",
          "tree_numbers": [
            "F01.145.407.516",
            "G07.203.650.353.516"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D005518",
      "preferred_label": "Food Preferences",
      "type": "descriptor",
      "location": "vocabulary:29",
      "term": {
        "text": "\"Food Preferences\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "School Health Services",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:33:37+00:00",
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
      "location": "vocabulary:37",
      "term": {
        "text": "\"School Health Services\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Schools",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:33:37+00:00",
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
      "location": "vocabulary:38",
      "term": {
        "text": "\"Schools\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:33:37+00:00",
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
      "location": "vocabulary:45",
      "term": {
        "text": "\"Diet\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:33:37+00:00",
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
      "location": "vocabulary:46",
      "term": {
        "text": "\"Feeding Behavior\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Food Preferences",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:33:37+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D005518",
          "name": "Food Preferences",
          "type": "descriptor",
          "scope_note": "The selection of one food over another.",
          "tree_numbers": [
            "F01.145.407.516",
            "G07.203.650.353.516"
          ],
          "entry_terms": 7,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D005518",
      "preferred_label": "Food Preferences",
      "type": "descriptor",
      "location": "vocabulary:47",
      "term": {
        "text": "\"Food Preferences\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Energy Intake",
      "expected_type": "descriptor",
      "checked_at": "2026-10-01T12:33:37+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D002149",
          "name": "Energy Intake",
          "type": "descriptor",
          "scope_note": "Total number of calories taken in daily whether ingested or by parenteral routes.",
          "tree_numbers": [
            "G07.203.650.240.340"
          ],
          "entry_terms": 4,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D002149",
      "preferred_label": "Energy Intake",
      "type": "descriptor",
      "location": "vocabulary:48",
      "term": {
        "text": "\"Energy Intake\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Health Education\"[MeSH Terms] OR \"Health Promotion\"[MeSH Terms] OR \"education\"[Title/Abstract] OR \"educat*\"[Title/Abstract] OR \"teach*\"[Title/Abstract] OR \"curricul*\"[Title/Abstract] OR \"lesson*\"[Title/Abstract] OR \"program*\"[Title/Abstract] OR \"programme*\"[Title/Abstract] OR \"intervention*\"[Title/Abstract] OR \"nutrition education\"[Title/Abstract] OR \"nutrition instruction\"[Title/Abstract] OR \"nutrition teaching\"[Title/Abstract] OR \"nutrition curriculum\"[Title/Abstract] OR \"nutrition curricula\"[Title/Abstract] OR \"dietary education\"[Title/Abstract] OR \"food education\"[Title/Abstract] OR \"healthy eating education\"[Title/Abstract] OR \"nutrition intervention*\"[Title/Abstract] OR \"dietary intervention*\"[Title/Abstract] OR \"nutrition program*\"[Title/Abstract] OR \"nutrition programme*\"[Title/Abstract] OR \"nutrition promotion\"[Title/Abstract] OR \"healthy eating promotion\"[Title/Abstract]) AND (\"Child Nutrition Sciences\"[MeSH Terms] OR \"Adolescent Nutritional Physiological Phenomena\"[MeSH Terms] OR \"Diet\"[MeSH Terms] OR \"Feeding Behavior\"[MeSH Terms] OR \"Food Preferences\"[MeSH Terms] OR \"nutrition*\"[Title/Abstract] OR \"diet*\"[Title/Abstract] OR \"food*\"[Title/Abstract] OR \"healthy eating\"[Title/Abstract] OR \"beverage*\"[Title/Abstract] OR \"fruit*\"[Title/Abstract] OR \"vegetable*\"[Title/Abstract]) AND (\"School Health Services\"[MeSH Terms] OR \"Schools\"[MeSH Terms] OR \"school*\"[Title/Abstract] OR \"classroom*\"[Title/Abstract] OR \"school-based\"[Title/Abstract] OR \"school-based\"[Title/Abstract] OR \"in-school\"[Title/Abstract] OR \"in-school\"[Title/Abstract]) AND (\"Diet\"[MeSH Terms] OR \"Feeding Behavior\"[MeSH Terms] OR \"Food Preferences\"[MeSH Terms] OR \"Energy Intake\"[MeSH Terms] OR \"food consumption\"[Title/Abstract] OR \"food intake\"[Title/Abstract] OR \"dietary intake\"[Title/Abstract] OR \"Energy Intake\"[Title/Abstract] OR \"fat intake\"[Title/Abstract] OR \"eating behavior\"[Title/Abstract] OR \"eating behaviours\"[Title/Abstract] OR \"food choice\"[Title/Abstract] OR \"food choices\"[Title/Abstract] OR \"food preference*\"[Title/Abstract] OR \"diet quality\"[Title/Abstract] OR \"dietary behavior\"[Title/Abstract] OR \"dietary behaviour\"[Title/Abstract] OR \"fruit and vegetable intake\"[Title/Abstract] OR \"beverage consumption\"[Title/Abstract] OR \"food purchase*\"[Title/Abstract] OR \"food sales\"[Title/Abstract] OR \"eating behaviors\"[Title/Abstract] OR \"eating behaviour\"[Title/Abstract]) AND 1800/01/01:2017/12/14[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "75c02bac7a533a5ffd85dd02feb3d616703068a25d38fc95ced28dedb0b9a2c2",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched concepts align with the stated eligibility criteria. Adolescents are screened rather than required in the query, consistent with the protocol rationale. No phrase warnings or translation issues are reported."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are ORed within concepts and the education, nutrition-content, school-setting, and outcome blocks are ANDed. Both optional AND decisions retain all 16 known records and meet the packet's minimum-known-record rule; their loss samples contain 0 relevant records out of 30."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes headings for health education and promotion, diet, feeding behavior, food preferences, schools, and energy intake. The packet reports no heading translation errors."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The required outcome block has eating behavior and eating behaviours, but omits the plural US spelling and singular UK spelling. Since the outcome block is ANDed, these phrase variants could affect retrieval when records lack matching indexing."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query is parenthesized by concept, translates successfully, and reports no PubMed errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age or study-design filter is applied. The query is bounded by the stated as-of date, 2017-12-14; report that historical cutoff wherever the strategy is presented."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The mandatory food-consumption block includes the exact phrases eating behavior and eating behaviours, but not eating behaviors or eating behaviour. These are spelling/number variants of an outcome explicitly included in eligibility.",
          "recommendation": "Add and test the missing explicit phrase variants, then run a complete evaluation of the revised strategy, including known-record recall and optional-block checks.",
          "status": "open"
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "The final query limits entry dates to 2017-12-14, matching the packet's as-of date, although the question and eligibility criteria state no publication-date restriction.",
          "recommendation": "State clearly that this is a search snapshot through 2017-12-14, and rerun or update the date boundary if the review is intended to cover later records.",
          "status": "accepted-risk",
          "response": "Accepted as a reporting reminder. The 2017-12-14 limit is an Entrez record-entry snapshot required by the run instructions, not a publication-date restriction. This distinction is recorded in protocol notes and narrative."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 6,
      "review_sha256": "030b0bce5ae17a25c32acd97fe401412d544321d43d6dcbf54b9f73980e969f6",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched blocks align with the stated eligibility criteria. Adolescents remain a screening criterion, as planned. The tested query has no reported translation issues."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are ORed within blocks and the four blocks are ANDed. Both optional blocks meet the packet's minimum-known-record rule, retain all 16 known records, and have loss samples with 0 relevant records out of 30."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes relevant headings for education, nutrition, diet, feeding behavior, food preferences, schools, and energy intake. No heading translation errors are reported."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The outcome block now includes both previously missing variants, eating behaviors and eating behaviour. The complete evaluation retains all 16 known records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query is grouped by concept, translates successfully, and reports no PubMed errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age or study-design filter is applied. The query has an Entrez date-entry bound through 2017-12-14, and the notes correctly distinguish this record-entry snapshot from a publication-date restriction."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The mandatory food-consumption block previously omitted the exact phrases eating behaviors and eating behaviour.",
          "recommendation": "Add and test both phrase variants, then run a complete evaluation of the revised strategy.",
          "status": "resolved",
          "response": "Both phrases are now included in the food-consumption block. The complete evaluation reports all 16 known records retrieved, and the optional-block checks were rerun."
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "The final query limits Entrez entry dates through 2017-12-14, matching the packet's as-of date, although the question and eligibility criteria state no publication-date restriction.",
          "recommendation": "State clearly that this is a search snapshot through 2017-12-14, and rerun or update the date boundary if the review is intended to cover later records.",
          "status": "accepted-risk",
          "response": "Accepted as a reporting reminder. The 2017-12-14 limit is an Entrez record-entry snapshot required by the run instructions, not a publication-date restriction. This distinction is recorded in the protocol notes and narrative."
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 6,
      "review_sha256": "030b0bce5ae17a25c32acd97fe401412d544321d43d6dcbf54b9f73980e969f6",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The searched concepts align with the stated eligibility criteria. Adolescents remain a screening criterion, as planned."
        },
        "operators": {
          "verdict": "pass",
          "note": "Terms are ORed within concepts and the blocks are ANDed. Both optional blocks retain all 16 known records and meet the stated minimum-known-record rule."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes relevant headings for education, nutrition, diet, feeding behavior, food preferences, schools, and energy intake; no heading translation errors are reported."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The current outcome block includes both previously missing variants, eating behaviors and eating behaviour. The complete evaluation retains all 16 known records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The query is grouped by concept, translates successfully, and reports no PubMed errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age or study-design filter is applied. The Entrez entry-date bound through 2017-12-14 is documented as a search snapshot, not a publication-date restriction."
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier outcome-block omission of the phrases eating behaviors and eating behaviour has been addressed in the current strategy.",
          "recommendation": "No further change is needed for this finding.",
          "status": "resolved",
          "response": "Both phrase variants are present in the current outcome block. The complete evaluation retains all 16 known records, and optional-block checks were rerun."
        },
        {
          "id": "F2",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "The strategy uses an Entrez entry-date bound through 2017-12-14, matching the packet's as-of date.",
          "recommendation": "Keep stating that this is a record-entry snapshot through 2017-12-14, and update the boundary if the review is intended to cover later records.",
          "status": "accepted-risk",
          "response": "Accepted as a reporting reminder. The date bound is an Entrez record-entry snapshot required by the run instructions, not a publication-date restriction; this distinction is recorded in the protocol notes and narrative."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

