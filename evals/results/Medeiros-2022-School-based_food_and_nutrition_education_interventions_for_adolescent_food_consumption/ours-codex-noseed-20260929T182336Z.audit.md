# PubMed search strategy: audit

Generated 2026-09-29T19:31:26+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: School-based food and nutrition education interventions for adolescent food consumption
- Framework: PICO
- Scope confirmed by user: no (User asked to proceed without questions. Assumed broad coverage of adolescents and school students; age/school level, school delivery, intervention content, and eligible consumption outcomes are confirmed at screening. No language or publication-date limits. PubMed corpus bounded by Entrez date through 2017-12-14 per harness, not by publication date. Additional scope assumption: school students includes enrolled pupils across primary and secondary grades because the eligibility wording says adolescents or school students; outcomes may be described in US or UK spelling, and food intake, consumption, choice, or dietary behavior terms are searched.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Food and nutrition education intervention | search | Food/nutrition education is the intervention concept; records may describe it as health education, a nutrition curriculum, cooking education, or garden-based learning, so use both MeSH and broad title/abstract wording. |
| Adolescents or school students | search | The population defines eligibility and commonly appears as adolescents, students, or children in records; age and school level will still be checked at screening. |
| School delivery | optional | School is a topic-defining setting that authors often name but may omit from titles and abstracts; test before deciding whether to require it. |
| Eligible food-consumption outcomes | optional | Food or dietary consumption defines the topic, but outcome terms may be inconsistently reported; test a broad outcome block and loss sample. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T19:29:55+00:00
- Records added to PubMed up to: 2017-12-14
- Total records: 5,776
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Health Education[Mesh]` | 221,709 | none |
| 2 | `Health Promotion[Mesh]` | 70,478 | none |
| 3 | `Health Knowledge, Attitudes, Practice[Mesh]` | 99,266 | none |
| 4 | `nutrition education[tiab]` | 3,866 | none |
| 5 | `food education[tiab]` | 84 | none |
| 6 | `dietary education[tiab]` | 252 | none |
| 7 | `nutrition instruction[tiab]` | 46 | none |
| 8 | `nutrition curriculum[tiab]` | 87 | none |
| 9 | `nutrition program*[tiab]` | 2,437 | none |
| 10 | `nutrition intervention*[tiab]` | 1,929 | none |
| 11 | `food literacy[tiab]` | 34 | none |
| 12 | `nutrition knowledge[tiab]` | 922 | none |
| 13 | `garden-based nutrition[tiab]` | 4 | none |
| 14 | `Cooking[Mesh]` | 10,657 | none |
| 15 | `"cooking education"[tiab]` | 6 | none |
| 16 | `"cooking class"[tiab]` | 12 | none |
| 17 | `"cooking classes"[tiab]` | 64 | none |
| 18 | `cooking[tiab]` | 12,112 | none |
| 19 | `culinary[tiab]` | 1,256 | none |
| 20 | `garden*[tiab]` | 10,503 | none |
| 21 | `school garden*[tiab]` | 68 | none |
| 22 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21` | 331,960 | none |
| 23 | `Adolescent[Mesh]` | 1,895,608 | none |
| 24 | `Child[Mesh]` | 1,797,170 | none |
| 25 | `Child, Preschool[Mesh]` | 864,028 | none |
| 26 | `Students[Mesh]` | 112,971 | none |
| 27 | `adolescen*[tiab]` | 248,945 | none |
| 28 | `teen*[tiab]` | 26,895 | none |
| 29 | `youth*[tiab]` | 64,596 | none |
| 30 | `student*[tiab]` | 234,078 | none |
| 31 | `pupil*[tiab]` | 26,074 | none |
| 32 | `schoolchild*[tiab]` | 13,052 | none |
| 33 | `school student*[tiab]` | 14,516 | none |
| 34 | `schoolchildren[tiab]` | 12,947 | none |
| 35 | `child*[tiab]` | 1,257,861 | none |
| 36 | `middle school*[tiab]` | 4,703 | none |
| 37 | `high school*[tiab]` | 27,028 | none |
| 38 | `secondary school*[tiab]` | 8,822 | none |
| 39 | `primary school*[tiab]` | 10,360 | none |
| 40 | `#23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39` | 3,400,727 | none |
| 41 | `Diet[Mesh]` | 254,824 | none |
| 42 | `Feeding Behavior[Mesh]` | 156,434 | none |
| 43 | `Food Preferences[Mesh]` | 13,063 | none |
| 44 | `Fruit[Mesh]` | 91,855 | none |
| 45 | `Vegetables[Mesh]` | 28,363 | none |
| 46 | `food intake[tiab]` | 39,819 | none |
| 47 | `dietary intake[tiab]` | 20,267 | none |
| 48 | `food consumption[tiab]` | 11,651 | none |
| 49 | `food consum*[tiab]` | 12,835 | none |
| 50 | `diet* intake[tiab]` | 20,883 | none |
| 51 | `fruit intake[tiab]` | 893 | none |
| 52 | `vegetable intake[tiab]` | 2,824 | none |
| 53 | `fruit consumption[tiab]` | 960 | none |
| 54 | `vegetable consumption[tiab]` | 2,984 | none |
| 55 | `food choice*[tiab]` | 3,666 | none |
| 56 | `food preference*[tiab]` | 2,104 | none |
| 57 | `eating behavior*[tiab]` | 5,856 | none |
| 58 | `dietary behavior*[tiab]` | 1,632 | none |
| 59 | `food habit*[tiab]` | 1,985 | none |
| 60 | `serving*[tiab]` | 35,913 | none |
| 61 | `intake[tiab]` | 229,738 | none |
| 62 | `consumption[tiab]` | 242,645 | none |
| 63 | `dietary behaviour*[tiab]` | 723 | none |
| 64 | `eating behaviour*[tiab]` | 2,159 | none |
| 65 | `behaviour*[tiab]` | 243,114 | none |
| 66 | `#41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65` | 1,034,999 | none |
| 67 | `Schools[Mesh]` | 107,820 | none |
| 68 | `school*[tiab]` | 246,627 | none |
| 69 | `school-based[tiab]` | 10,873 | none |
| 70 | `classroom*[tiab]` | 14,159 | none |
| 71 | `school setting*[tiab]` | 2,670 | none |
| 72 | `school program*[tiab]` | 1,449 | none |
| 73 | `educational setting*[tiab]` | 1,133 | none |
| 74 | `afterschool[tiab]` | 947 | none |
| 75 | `after-school[tiab]` | 1,282 | none |
| 76 | `#67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73 OR #74 OR #75` | 312,363 | none |
| 77 | `#22 AND #40 AND #66 AND #76` | 5,776 | none |

### Strategy (single line, for copying into PubMed)

```text
((Health Education[Mesh] OR Health Promotion[Mesh] OR Health Knowledge, Attitudes, Practice[Mesh] OR nutrition education[tiab] OR food education[tiab] OR dietary education[tiab] OR nutrition instruction[tiab] OR nutrition curriculum[tiab] OR nutrition program*[tiab] OR nutrition intervention*[tiab] OR food literacy[tiab] OR nutrition knowledge[tiab] OR garden-based nutrition[tiab] OR Cooking[Mesh] OR "cooking education"[tiab] OR "cooking class"[tiab] OR "cooking classes"[tiab] OR cooking[tiab] OR culinary[tiab] OR garden*[tiab] OR school garden*[tiab]) AND (Adolescent[Mesh] OR Child[Mesh] OR Child, Preschool[Mesh] OR Students[Mesh] OR adolescen*[tiab] OR teen*[tiab] OR youth*[tiab] OR student*[tiab] OR pupil*[tiab] OR schoolchild*[tiab] OR school student*[tiab] OR schoolchildren[tiab] OR child*[tiab] OR middle school*[tiab] OR high school*[tiab] OR secondary school*[tiab] OR primary school*[tiab]) AND (Diet[Mesh] OR Feeding Behavior[Mesh] OR Food Preferences[Mesh] OR Fruit[Mesh] OR Vegetables[Mesh] OR food intake[tiab] OR dietary intake[tiab] OR food consumption[tiab] OR food consum*[tiab] OR diet* intake[tiab] OR fruit intake[tiab] OR vegetable intake[tiab] OR fruit consumption[tiab] OR vegetable consumption[tiab] OR food choice*[tiab] OR food preference*[tiab] OR eating behavior*[tiab] OR dietary behavior*[tiab] OR food habit*[tiab] OR serving*[tiab] OR intake[tiab] OR consumption[tiab] OR dietary behaviour*[tiab] OR eating behaviour*[tiab] OR behaviour*[tiab]) AND (Schools[Mesh] OR school*[tiab] OR school-based[tiab] OR classroom*[tiab] OR school setting*[tiab] OR school program*[tiab] OR educational setting*[tiab] OR afterschool[tiab] OR after-school[tiab])) AND ("1800/01/01"[edat] : "2017/12/14"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 22 | 22 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| School delivery | AND-ed | 20,358 / 5,776 | 71.6% | none | 0/30 (up to 10% of removed records could be relevant) | Retain school delivery after retesting it against the current strategy with food-consumption terms included. The matching base contains 20,358 records without school delivery and 5,776 with it, a 71.6% reduction, while retaining all 22 known relevant records. The refreshed 30-record loss sample contained no eligible school-based food/nutrition education study; its small size limits evidence about rare relevant records. |
| Eligible food-consumption outcomes | AND-ed | 25,592 / 5,776 | 77.4% | none | 0/30 (up to 10% of removed records could be relevant) | Retain food-consumption terms after refreshing the test against the current education and school-setting blocks. The current base has 25,592 records and the block removes 19,816 (77.4%), retaining all 22 known relevant records. The refreshed 30-record sample contained no eligible school-based food/nutrition education study. The small random sample is weak evidence; report the limited non-independent development evidence. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Food and nutrition education intervention | 1 | `(education[tiab] OR educat*[tiab] OR lesson*[tiab] OR curriculum[tiab] OR cooking[tiab] OR garden*[tiab] OR program*[tiab] OR intervention*[tiab] OR Health Education[Mesh] OR Health Promotion[Mesh] OR Food Preferences[Mesh] OR Diet[Mesh])` | 12,153 | not screened |
| Food and nutrition education intervention | 2 | `(education[tiab] OR educat*[tiab] OR lesson*[tiab] OR curriculum[tiab] OR cooking[tiab] OR garden*[tiab] OR program*[tiab] OR intervention*[tiab] OR Health Education[Mesh] OR Health Promotion[Mesh] OR Food Preferences[Mesh] OR Diet[Mesh])` | 12,153 | 0/30 |
| Adolescents or school students | 1 | `(grade*[tiab] OR elementary[tiab] OR kindergarten*[tiab] OR school-aged[tiab] OR preschool*[tiab] OR teen*[tiab] OR junior high[tiab] OR high school*[tiab] OR undergraduate*[tiab] OR college student*[tiab] OR Children[Mesh] OR Infant[Mesh])` | 52 | 0/30 |
| Adolescents or school students | 2 | `(grade*[tiab] OR elementary[tiab] OR kindergarten*[tiab] OR school-aged[tiab] OR preschool*[tiab] OR teen*[tiab] OR junior high[tiab] OR high school*[tiab] OR undergraduate*[tiab] OR college student*[tiab] OR Children[Mesh] OR Infant[Mesh])` | 54 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| education | 26,329 | 0 |
| population | 6,256 | 0 |
| consumption | 25,592 | 0 |
| setting | 20,358 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial two-block intervention and population strategy; school-delivery and food-consumption blocks added as optional candidates for measurement. Scope proceeded without user confirmation. |
| 2 | 100,718 | education: +0 / -1 | none | Removed malformed food-and-nutrition phrase after lint identified lowercase Boolean parsing and unintended ATM fallback; vocabulary otherwise unchanged. |
| 3 | 25,111 | setting: +9 / -0 | none | AND-ed school delivery after optional loss sample: all 22 known relevant records are retained; 0 of 30 sampled records removed by the setting block were eligible. Re-evaluating the remaining optional consumption block against the updated base. |
| 4 | 25,111 | limits/combination | none | Expanded the optional food-consumption block with British spellings for dietary/eating behaviour after PMID 25773683 was the only known record it would lose; its abstract reports students eating vegetables and breakfast every day. |
| 5 | 5,583 | consumption: +25 / -0 | none | AND-ed eligible food-consumption outcome block after its refreshed optional loss sample. The block now includes British behaviour spellings and no longer loses any of the 22 known relevant records. |
| 6 | 20,358 | education: +5 / -0; setting: +0 / -9 | none | Addressed critic round 1: added cooking/cooking education and garden member terms to represent experiential food education. Returned school to optional candidate temporarily to remeasure its loss sample and reduction against the updated consumption-constrained strategy; cleared its stale decision. |
| 7 | 104,029 | consumption: +0 / -25 | none | Reset both optional concepts as candidates so their decisions can be refreshed against the expanded education block and current base query; cooking and school-garden terms added in response to critic. |
| 8 | 25,592 | setting: +9 / -0 | none | Refreshed the school-setting decision after critic R1-01 using a current optional sample and updated count baseline; all 22 records retained and 0/30 removed records were eligible. |
| 9 | 5,776 | consumption: +25 / -0 | none | Final re-evaluation after critic revisions and refreshed optional decisions; added explicit cooking and garden approaches, refreshed school/outcome loss samples on the current strategy, and recorded the scope interpretation. |
| 10 | 20,358 | setting: +0 / -9 | none | Reopened the school-setting optional decision so it can be tested against the final consumption-constrained base; this resolves critic R1-01's baseline mismatch. |
| 11 | 5,776 | setting: +9 / -0 | none | Resolved critic R1-01: refreshed the school-setting optional loss sample and re-decided it against the final current base containing education, population, and food-consumption blocks; current comparison is 20,358 without versus 5,776 with setting. |
| 12 | 5,776 | education: +3 / -0 | none | Added explicit cooking education/class phrases requested by the current critic; tested their translation as an isolated clause. |
| 13 | 104,029 | consumption: +0 / -25; setting: +0 / -9 | none | Temporarily moved optional setting and outcome blocks to candidates so both could be retested against the revised education block and current baseline. |
| 14 | 104,029 | limits/combination | none | Re-testing optional school and food-consumption blocks against the revised education block. |
| 15 | 25,592 | setting: +9 / -0 | none | Applied refreshed school-setting decision, then measured remaining optional consumption block against the current education and setting base. |
| 16 | 5,776 | consumption: +25 / -0 | none | Applied refreshed optional outcome decision after the setting decision; final current strategy includes both optional blocks. |
| 17 | 20,358 | setting: +0 / -9 | none | Correcting the school-delivery optional test: keep consumption in the current strategy while testing the setting candidate, to match the final baseline. |
| 18 | 20,358 | limits/combination | none | Correcting the school-delivery optional test: keep consumption in the current strategy while testing the setting candidate, to match the final baseline. |
| 19 | 5,776 | setting: +9 / -0 | none | Applied the corrected school-delivery decision, measured on the baseline that includes consumption; final strategy now has both optional blocks AND-ed. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5: 2 findings; R1-01 must-fix open, R1-02 should-fix open
- Round 2 on version 16: 2 findings; R1-01 must-fix open, R1-02 should-fix resolved
- Round 3 on version 19: 2 findings; R1-01 must-fix resolved, R1-02 should-fix resolved

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 3928 NCBI requests logged (2342 from cache); strategy sha256 7960a9f674c0._

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
        "location": "concept:education",
        "blocking": false,
        "requires_review": true,
        "id": "I-dbf95b02a2f5650da634"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:population",
        "blocking": false,
        "requires_review": true,
        "id": "I-17c831561da839c02d17"
      }
    ],
    "issues": [
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:education",
        "blocking": false,
        "requires_review": true,
        "id": "I-dbf95b02a2f5650da634"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:population",
        "blocking": false,
        "requires_review": true,
        "id": "I-17c831561da839c02d17"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Health Education",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:29:55+00:00",
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
        "text": "Health Education",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Promotion",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:29:55+00:00",
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
        "text": "Health Promotion",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Health Knowledge, Attitudes, Practice",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:29:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D007722",
          "name": "Health Knowledge, Attitudes, Practice",
          "type": "descriptor",
          "scope_note": "Knowledge, attitudes, and associated behaviors which pertain to health-related topics such as PATHOLOGIC PROCESSES or diseases, their prevention, and treatment. This term refers to non-health workers and health workers (HEALTH PERSONNEL).",
          "tree_numbers": [
            "F01.100.150.500",
            "N05.300.150.410"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D007722",
      "preferred_label": "Health Knowledge, Attitudes, Practice",
      "type": "descriptor",
      "location": "vocabulary:3",
      "term": {
        "text": "Health Knowledge, Attitudes, Practice",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cooking",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:29:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003296",
          "name": "Cooking",
          "type": "descriptor",
          "scope_note": "The art or practice of preparing food. It includes the preparation of special foods for diets in various diseases.",
          "tree_numbers": [
            "J01.576.423.200.200"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003296",
      "preferred_label": "Cooking",
      "type": "descriptor",
      "location": "vocabulary:14",
      "term": {
        "text": "Cooking",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Adolescent",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:29:55+00:00",
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
      "location": "vocabulary:22",
      "term": {
        "text": "Adolescent",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Child",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:29:55+00:00",
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
      "location": "vocabulary:23",
      "term": {
        "text": "Child",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Child, Preschool",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:29:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D002675",
          "name": "Child, Preschool",
          "type": "descriptor",
          "scope_note": "A child between the ages of 2 and 5.",
          "tree_numbers": [
            "M01.060.406.448"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D002675",
      "preferred_label": "Child, Preschool",
      "type": "descriptor",
      "location": "vocabulary:24",
      "term": {
        "text": "Child, Preschool",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Students",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:29:55+00:00",
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
      "location": "vocabulary:25",
      "term": {
        "text": "Students",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Diet",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:29:55+00:00",
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
      "location": "vocabulary:39",
      "term": {
        "text": "Diet",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:29:55+00:00",
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
      "location": "vocabulary:40",
      "term": {
        "text": "Feeding Behavior",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Food Preferences",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:29:55+00:00",
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
      "location": "vocabulary:41",
      "term": {
        "text": "Food Preferences",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Fruit",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:29:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D005638",
          "name": "Fruit",
          "type": "descriptor",
          "scope_note": "The fleshy or dry ripened ovary of a plant, enclosing the seed or seeds.",
          "tree_numbers": [
            "A18.024.500",
            "G07.203.300.562",
            "J02.500.562"
          ],
          "entry_terms": 15,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D005638",
      "preferred_label": "Fruit",
      "type": "descriptor",
      "location": "vocabulary:42",
      "term": {
        "text": "Fruit",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Vegetables",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:29:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D014675",
          "name": "Vegetables",
          "type": "descriptor",
          "scope_note": "A food group comprised of EDIBLE PLANTS or their parts.",
          "tree_numbers": [
            "B01.650.160.956",
            "B01.650.510.956",
            "G07.203.300.850",
            "J02.500.850"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D014675",
      "preferred_label": "Vegetables",
      "type": "descriptor",
      "location": "vocabulary:43",
      "term": {
        "text": "Vegetables",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Schools",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T19:29:55+00:00",
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
      "location": "vocabulary:64",
      "term": {
        "text": "Schools",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"health education\"[MeSH Terms] OR \"health promotion\"[MeSH Terms] OR \"health knowledge, attitudes, practice\"[MeSH Terms] OR \"nutrition education\"[Title/Abstract] OR \"food education\"[Title/Abstract] OR \"dietary education\"[Title/Abstract] OR \"nutrition instruction\"[Title/Abstract] OR \"nutrition curriculum\"[Title/Abstract] OR \"nutrition program*\"[Title/Abstract] OR \"nutrition intervention*\"[Title/Abstract] OR \"food literacy\"[Title/Abstract] OR \"nutrition knowledge\"[Title/Abstract] OR \"garden based nutrition\"[Title/Abstract] OR \"cooking\"[MeSH Terms] OR \"cooking education\"[Title/Abstract] OR \"cooking class\"[Title/Abstract] OR \"cooking classes\"[Title/Abstract] OR \"cooking\"[Title/Abstract] OR \"culinary\"[Title/Abstract] OR \"garden*\"[Title/Abstract] OR \"school garden*\"[Title/Abstract]) AND (\"adolescent\"[MeSH Terms] OR \"child\"[MeSH Terms] OR \"child, preschool\"[MeSH Terms] OR \"students\"[MeSH Terms] OR \"adolescen*\"[Title/Abstract] OR \"teen*\"[Title/Abstract] OR \"youth*\"[Title/Abstract] OR \"student*\"[Title/Abstract] OR \"pupil*\"[Title/Abstract] OR \"schoolchild*\"[Title/Abstract] OR \"school student*\"[Title/Abstract] OR \"schoolchildren\"[Title/Abstract] OR \"child*\"[Title/Abstract] OR \"middle school*\"[Title/Abstract] OR \"high school*\"[Title/Abstract] OR \"secondary school*\"[Title/Abstract] OR \"primary school*\"[Title/Abstract]) AND (\"diet\"[MeSH Terms] OR \"feeding behavior\"[MeSH Terms] OR \"food preferences\"[MeSH Terms] OR \"fruit\"[MeSH Terms] OR \"vegetables\"[MeSH Terms] OR \"food intake\"[Title/Abstract] OR \"dietary intake\"[Title/Abstract] OR \"food consumption\"[Title/Abstract] OR \"food consum*\"[Title/Abstract] OR \"diet* intake\"[Title/Abstract] OR \"fruit intake\"[Title/Abstract] OR \"vegetable intake\"[Title/Abstract] OR \"fruit consumption\"[Title/Abstract] OR \"vegetable consumption\"[Title/Abstract] OR \"food choice*\"[Title/Abstract] OR \"food preference*\"[Title/Abstract] OR \"eating behavior*\"[Title/Abstract] OR \"dietary behavior*\"[Title/Abstract] OR \"food habit*\"[Title/Abstract] OR \"serving*\"[Title/Abstract] OR \"intake\"[Title/Abstract] OR \"consumption\"[Title/Abstract] OR \"dietary behaviour*\"[Title/Abstract] OR \"eating behaviour*\"[Title/Abstract] OR \"behaviour*\"[Title/Abstract]) AND (\"schools\"[MeSH Terms] OR \"school*\"[Title/Abstract] OR \"school-based\"[Title/Abstract] OR \"classroom*\"[Title/Abstract] OR \"school setting*\"[Title/Abstract] OR \"school program*\"[Title/Abstract] OR \"educational setting*\"[Title/Abstract] OR \"afterschool\"[Title/Abstract] OR \"after-school\"[Title/Abstract]) AND 1800/01/01:2017/12/14[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "0b260bfc214b658f3bdc35026a0a2d3f5a9c13056912b36a246316b494ccec7b",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The education block does not explicitly cover the named experiential approaches, particularly cooking-based education. The broader probe included cooking and garden terms, but screening 30 records is limited evidence of coverage."
        },
        "operators": {
          "verdict": "revise",
          "note": "The school-delivery AND decision is marked stale, so its earlier test cannot support the current strategy. Its rationale also cites a 100,718-record baseline, while the current table reports 19,245 without the block."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Relevant education, population, school, and food-consumption headings are included, alongside text-word terms."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Consider explicit cooking-based education terms to represent the experiential approaches named in scope; the current terms include garden-based nutrition but not cooking-based education."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no translation issues or lint errors, and the query combines the blocks with explicit Boolean operators."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or publication-date limits are specified. The Entrez-date corpus boundary is documented in the notes."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "operators",
          "severity": "must-fix",
          "kind": "reporting",
          "finding": "The school-delivery optional-concept decision is marked stale, but the current strategy still ANDs that block. The rationale refers to a 100,718-record baseline, whereas the current table reports 19,245 records without the block. The stale test does not establish the current block's reduction or loss risk.",
          "recommendation": "Re-evaluate the school-delivery block against the current strategy, refresh the loss sample and record counts, and update the decision rationale before retaining it as an AND-ed block.",
          "status": "open"
        },
        {
          "id": "R1-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Scope names classroom and experiential approaches, and the education rationale says named educational approaches will be included. The block includes garden-based nutrition but no explicit cooking-based education terms.",
          "recommendation": "Assess explicit terms such as cooking education, cooking class*, or school garden* for the education block, and record the evidence for retaining or excluding them. The broader probe's 0/30 result is useful but limited evidence.",
          "status": "open"
        }
      ],
      "issue_dispositions": []
    },
    {
      "round": 2,
      "strategy_version": 16,
      "review_sha256": "6e068fd43279d90872504d6e44ec02c6d5728148446c1c954a91bf4fe6dddde5",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The education block now includes explicit cooking education and cooking class phrases. Their isolated search lines report results for each phrase with no diagnostics."
        },
        "operators": {
          "verdict": "revise",
          "note": "The setting decision remains stale in the detailed optional evidence. Its current test counts show 20,358 without the block and 5,776 with it, while the refreshed rationale cites a different base of 104,029 and 25,592 after adding the block. Reconcile and retest the setting block against the current strategy before retaining the AND decision."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes relevant education, population, school, and food-consumption headings alongside text words."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The education block now includes the explicit phrases \"cooking education\", \"cooking class\", and \"cooking classes\", addressing the earlier wording gap."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no term diagnostics and shows the concept blocks combined with explicit Boolean operators."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or publication-date filters are applied. The Entrez-date corpus boundary is documented."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "operators",
          "severity": "must-fix",
          "kind": "reporting",
          "finding": "The school-delivery decision is still marked stale in the detailed optional evidence. Its counts (20,358 without the setting block and 5,776 with it) conflict with the refreshed rationale, which cites 104,029 before and 25,592 after the setting block.",
          "recommendation": "Reconcile the counts and stale status, then evaluate the setting block against the current strategy with a matching loss sample and rationale.",
          "status": "open"
        },
        {
          "id": "R1-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Scope and rationale name cooking education as an experiential approach, but the prior education block lacked explicit cooking-based education wording.",
          "recommendation": "Assess explicit cooking education and cooking class terms and record the evidence.",
          "status": "resolved",
          "response": "The education block now includes \"cooking education\", \"cooking class\", and \"cooking classes\". The packet lists isolated result counts of 6, 12, and 64 respectively, each with no diagnostics."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-17c831561da839c02d17",
          "status": "accepted-risk",
          "response": "The population probe is stale because the block changed after its last probe and the probe budget is spent. This remains a limitation of the current evidence; the issue is accepted as a review risk.",
          "evidence": "The packet reports two population probes, each screening 30 records with 0 relevant, but marks the current population probe stale and lists this issue as requiring review."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 19,
      "review_sha256": "a18864e4fc9b9a795dc7d5e36532474bd03348a5547491a777b4227a8b1b90a9",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The education block includes explicit cooking education and cooking class phrases, and population and consumption terms cover the named concepts. The education category probe is stale after block changes; its limited evidence is recorded as accepted risk."
        },
        "operators": {
          "verdict": "pass",
          "note": "The current optional setting test is internally consistent: 20,358 records without the block, 5,776 with it, a 71.6% reduction, no known records lost, and a matching 30-record loss sample. The rationale reports those same counts."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes relevant education, population, school, and food-consumption MeSH headings alongside text words."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The education block now includes cooking education, cooking class, and cooking classes, resolving the earlier wording gap."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no term diagnostics and shows the concept blocks combined with explicit Boolean operators."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No language or publication-date limits are applied; the Entrez-date corpus boundary is documented."
        }
      },
      "findings": [
        {
          "id": "R1-01",
          "domain": "operators",
          "severity": "must-fix",
          "kind": "reporting",
          "finding": "The school-delivery optional-concept decision was previously stale and its reported counts conflicted with the rationale.",
          "recommendation": "Reconcile the counts and stale status, then evaluate the setting block against the current strategy with a matching loss sample and rationale.",
          "status": "resolved",
          "response": "The current optional evidence marks the setting test as current and reports matching counts in the test and rationale: 20,358 without the block and 5,776 with it. It also reports a 30-record loss sample, no known records lost, and all 22 known relevant records retained."
        },
        {
          "id": "R1-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The education block previously lacked explicit cooking-based education wording despite scope naming experiential approaches.",
          "recommendation": "Assess explicit cooking education and cooking class terms and record the evidence.",
          "status": "resolved",
          "response": "The education block includes \"cooking education\", \"cooking class\", and \"cooking classes\"; the packet reports isolated counts of 6, 12, and 64 respectively, with no diagnostics."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-dbf95b02a2f5650da634",
          "status": "accepted-risk",
          "response": "The education category probe is stale because the block changed after the last probe and the probe budget is spent. The concern remains a limitation of the available coverage evidence.",
          "evidence": "The packet records two education probes, with the latest screening 30 records and finding none relevant, but marks the category status stale. The broader probe explicitly included cooking and garden terms; the current education block also contains the tested cooking education and cooking class expressions."
        },
        {
          "issue_id": "I-17c831561da839c02d17",
          "status": "accepted-risk",
          "response": "The population category probe is stale because the block changed after the last probe and the probe budget is spent. The concern remains a limitation of the available coverage evidence.",
          "evidence": "The packet records two population probes, each screening 30 records and finding none relevant, but marks the category status stale after the block changed."
        }
      ]
    }
  ]
}
```

