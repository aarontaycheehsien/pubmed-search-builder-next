# PubMed search strategy: audit

Generated 2026-09-29T03:35:28+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: School-based food and nutrition education interventions for adolescent food consumption
- Framework: PICO
- Scope confirmed by user: no (User requested standard depth and instructed that no questions be asked; roles and interpretations are provisional. No known relevant articles were supplied. No publication-date limit is used; PubMed records are bounded by Entrez date 2017-12-14 via PSB_AS_OF and protocol as_of. Population is interpreted inclusively as adolescents OR school students. The intervention, population, and consumption categories are marked for probing. Similar records were screened into the relevant development set; the miss at PMID 19256179 prompted adding Curriculum MeSH and broader school nutrition curriculum text terms, so this set is no longer independent validation.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Food and nutrition education interventions | search | The intervention is essential to the question and has searchable indexing and title/abstract terminology; category probe will test studies named by a specific educational approach or curriculum. |
| Adolescents or school students | optional | Age/student labels are searchable but could be absent or represented by a school-grade or specific age group; test as optional. |
| School-delivered intervention | optional | School is central to eligibility and often named, but delivery setting is inconsistently reported in abstracts; test an optional block. |
| Eligible food-consumption outcomes | optional | Food-consumption outcomes define the topic and have searchable terms, but are inconsistently named; test an optional block and screen broadly. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T03:34:41+00:00
- Records added to PubMed up to: 2017-12-14
- Total records: 7,762
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `("Health Education"[Mesh] AND ("Nutritional Sciences"[Mesh] OR "Child Nutrition Sciences"[Mesh] OR "Feeding Behavior"[Mesh]))` | 11,430 | none |
| 2 | `("Curriculum"[Mesh] AND "School Health Services"[Mesh])` | 1,008 | none |
| 3 | `(school*[tiab] AND (nutrition[tiab] OR food[tiab] OR dietary[tiab]) AND (curriculum[tiab] OR lesson*[tiab] OR educat*[tiab] OR teach*[tiab]))` | 5,398 | none |
| 4 | `"food education"[tiab]` | 84 | none |
| 5 | `"nutrition education"[tiab]` | 3,866 | none |
| 6 | `"dietary education"[tiab]` | 252 | none |
| 7 | `"nutrition teaching"[tiab]` | 72 | none |
| 8 | `"food and nutrition education"[tiab]` | 105 | none |
| 9 | `"nutrition instruction"[tiab]` | 46 | none |
| 10 | `"food literacy"[tiab]` | 34 | none |
| 11 | `"nutrition literacy"[tiab]` | 48 | none |
| 12 | `"nutrition curriculum"[tiab]` | 87 | none |
| 13 | `(food[tiab] AND curricul*[tiab])` | 540 | none |
| 14 | `"nutrition program"[tiab]` | 1,227 | none |
| 15 | `"nutrition programs"[tiab]` | 970 | none |
| 16 | `"dietary intervention"[tiab]` | 4,247 | none |
| 17 | `"food intervention"[tiab]` | 44 | none |
| 18 | `"nutrition intervention"[tiab]` | 1,150 | none |
| 19 | `"food-based intervention"[tiab]` | 16 | none |
| 20 | `"food-based interventions"[tiab]` | 32 | none |
| 21 | `nutrition promot*[tiab]` | 145 | none |
| 22 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21` | 26,632 | none |
| 23 | `"Schools"[Mesh]` | 107,820 | none |
| 24 | `"School Health Services"[Mesh]` | 21,872 | none |
| 25 | `school*[tiab]` | 246,627 | none |
| 26 | `classroom*[tiab]` | 14,159 | none |
| 27 | `"school-based"[tiab]` | 10,873 | none |
| 28 | `"school based"[tiab]` | 10,873 | none |
| 29 | `"classroom-based"[tiab]` | 587 | none |
| 30 | `"classroom based"[tiab]` | 587 | none |
| 31 | `"school setting"[tiab]` | 1,684 | none |
| 32 | `"school settings"[tiab]` | 1,086 | none |
| 33 | `kindergarten*[tiab]` | 5,565 | none |
| 34 | `#23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33` | 319,130 | none |
| 35 | `#22 AND #34` | 7,762 | none |

### Strategy (single line, for copying into PubMed)

```text
((("Health Education"[Mesh] AND ("Nutritional Sciences"[Mesh] OR "Child Nutrition Sciences"[Mesh] OR "Feeding Behavior"[Mesh])) OR ("Curriculum"[Mesh] AND "School Health Services"[Mesh]) OR (school*[tiab] AND (nutrition[tiab] OR food[tiab] OR dietary[tiab]) AND (curriculum[tiab] OR lesson*[tiab] OR educat*[tiab] OR teach*[tiab])) OR "food education"[tiab] OR "nutrition education"[tiab] OR "dietary education"[tiab] OR "nutrition teaching"[tiab] OR "food and nutrition education"[tiab] OR "nutrition instruction"[tiab] OR "food literacy"[tiab] OR "nutrition literacy"[tiab] OR "nutrition curriculum"[tiab] OR (food[tiab] AND curricul*[tiab]) OR "nutrition program"[tiab] OR "nutrition programs"[tiab] OR "dietary intervention"[tiab] OR "food intervention"[tiab] OR "nutrition intervention"[tiab] OR "food-based intervention"[tiab] OR "food-based interventions"[tiab] OR nutrition promot*[tiab]) AND ("Schools"[Mesh] OR "School Health Services"[Mesh] OR school*[tiab] OR classroom*[tiab] OR "school-based"[tiab] OR "school based"[tiab] OR "classroom-based"[tiab] OR "classroom based"[tiab] OR "school setting"[tiab] OR "school settings"[tiab] OR kindergarten*[tiab])) AND ("1800/01/01"[edat] : "2017/12/14"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 31 | 31 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Adolescents or school students | left out (stale) | 7,762 / 6,890 | 11.2% | none | 0/30 (up to 10% of removed records could be relevant) | Leave out the population block to preserve high sensitivity: the current core count is 6,855 with it and 7,720 without it, so adding it removes only 11.2% and both searches remain within the 10,000-record budget. The fresh 30-record loss sample contained no confirmed eligible study, but PMID 19256197 (in-school obesity prevention, abstract unavailable) remains uncertain and is not treated as excluded proof; omitting the block protects against missing studies whose age/student indexing is absent. The category probe is stale, so no clean-probe claim is used. |
| School-delivered intervention | AND-ed (stale) | 26,632 / 7,762 | 70.9% | none | 0/30 (up to 10% of removed records could be relevant) | AND the school-setting block: all 30 known studies are retrieved after adding kindergarten wording for the school-delivered kindergarten study; the refreshed 30-record loss sample contained no eligible school-delivered study; and the candidate reduces the current base count by more than 70%. School delivery is explicit eligibility, so this measured reduction is useful without a known-record loss. |
| Eligible food-consumption outcomes | left out (stale) | 7,762 / 3,737 | 51.9% | 11918492 | 1/30 | Leave the consumption block out to preserve recall. It would remove 3,993 records from the current 7,720-record school-and-nutrition-education search (about 52%) and leave only 10 previously known records, below the skill's 15-record safety threshold. The fresh 30-record loss sample found PMID 11918492, a school-based nutrition-education project among children aged 6–12 aimed at increasing iodized-salt use, which is relevant under the consumption-outcome criterion; other sample records were outside scope or knowledge-only. A separate ambiguous kindergarten record (PMID 7104935; no abstract) remains unresolved. Therefore outcomes stay for screening. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Food and nutrition education interventions | 1 | `((nutrition[tiab] OR food[tiab] OR dietary[tiab]) AND (educat*[tiab] OR teach*[tiab] OR curriculum[tiab])) OR (Health Education[Mesh] AND (Nutritional Sciences[Mesh] OR Child Nutrition Sciences[Mesh] OR Feeding Behavior[Mesh]))` | 26,022 | 0/30 |
| Food and nutrition education interventions | 2 | `((nutrition[tiab] OR food[tiab] OR dietary[tiab]) AND (educat*[tiab] OR teach*[tiab] OR curriculum[tiab])) OR (Health Education[Mesh] AND (Nutritional Sciences[Mesh] OR Child Nutrition Sciences[Mesh] OR Feeding Behavior[Mesh]))` | 344 | 0/30 |
| Adolescents or school students | 1 | `(middle school[tiab] OR high school[tiab] OR primary school[tiab] OR school-age[tiab] OR school age[tiab] OR grade*[tiab] OR teen*[tiab])` | 178 | 0/30 |
| Adolescents or school students | 2 | `(middle school[tiab] OR high school[tiab] OR primary school[tiab] OR school-age[tiab] OR school age[tiab] OR grade*[tiab] OR teen*[tiab])` | 0 | 0/0 |
| Eligible food-consumption outcomes | 1 | `(diet quality[tiab] OR food frequency[tiab] OR fruit[tiab] OR vegetable*[tiab] OR healthy eating[tiab] OR food selection[tiab] OR food preference[tiab] OR beverage intake[tiab] OR sugar-sweetened beverages[tiab])` | 384 | 2/30 |
| Eligible food-consumption outcomes | 2 | `(diet quality[tiab] OR food frequency[tiab] OR fruit[tiab] OR vegetable*[tiab] OR healthy eating[tiab] OR food selection[tiab] OR food preference[tiab] OR beverage intake[tiab] OR sugar-sweetened beverages[tiab])` | 357 | 2/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| education | 319,130 | 0 |
| setting | 26,632 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial recall-first block uses verified Health Education MeSH plus explicit food/nutrition education and intervention wording; population, school setting, and consumption are optional candidates pending counts and screening. No known records were supplied; no seeds available for recall estimation. |
| 2 | 0 | education: +1 / -1 | none | Corrected protocol date to ISO format required by the tool; revised phrase wildcards to retain explicit variants and avoid PubMed ignoring wildcards embedded in quoted phrases. |
| 3 | 21,557 | education: +1 / -1 | none | Restricted the broad Health Education MeSH term to records also indexed for nutrition or feeding behavior, based on its initial 230,560-record retrieval; explicit food/nutrition education text terms remain available for unindexed and differently indexed records. |
| 4 | 21,557 | limits/combination | none | Consumption category probe 1 identified two eligible studies whose abstracts name fruit/vegetable intake and breakfast behavior/frequency/selection; added those members to the optional outcome candidate and promoted the screened records to the relevant development set. |
| 5 | 21,557 | limits/combination | none | Consumption probe 2 found two additional eligible studies with member-only wording for breakfast and fruit/vegetable eating; added these generic member terms to the optional outcome candidate. Probe budget is exhausted at standard depth; residual risk is documented for the critic. |
| 6 | 21,557 | limits/combination | none | Because consumption probe 2 found two relevant records and indicated a broad residual risk, added all remaining wording from the broader probe query as a generic layer in the outcome candidate. The two-probe standard budget is exhausted; critique must review the residual estimate. |
| 7 | 126,255 | education: +2 / -0 | none | Similar-record screening increased the relevant set and exposed one miss, PMID 19256179. Added Curriculum MeSH and broader food/nutrition education curriculum text wording to recover it, and added child and kindergarten text variants after screening demonstrated a school-based kindergarten intervention. |
| 8 | 26,405 | education: +2 / -2 | none | Narrowed new Curriculum MeSH recovery vocabulary to the school curriculum concept (Curriculum AND School Health Services) and kept a text-word route requiring school plus food/nutrition/diet and curriculum/lesson/education/teaching wording. This recovers the screened missed curriculum study without opening the entire Curriculum heading. |
| 9 | 26,405 | limits/combination | none | Expanded optional population text vocabulary to include grade-level and middle/high/primary-school wording before the final loss sample, consistent with the user’s inclusive adolescent-or-school-student eligibility. |
| 10 | 6,855 | population: +19 / -0; setting: +11 / -0 | none | Population and school-setting optional blocks were moved into the query after refreshed 30-record loss samples, zero known losses, full retrieval of the 30 known studies, and large measured count reductions; consumption remains under review. |
| 11 | 7,720 | population: +0 / -19 | none | Responding to critic R1-F1, moved population from core to candidate and leave it out: preserve recall with 7,720 records within budget; screened a fresh 30-record population loss sample, with one unavailable-abstract candidate treated as uncertain. |
| 12 | 7,762 | education: +1 / -1 | none | Responded to critic R1-F3/R2 text-word finding: replaced the zero-hit exact phrase food curriculum with the tested co-occurrence expression (food[tiab] AND curricul*[tiab]), which retrieved 540 PubMed records at the same Entrez cutoff. Complete evaluation will check the final count and all 31 known records. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 10: 4 findings; R1-F1 should-fix open, R1-F2 should-fix open, R1-F3 should-fix open, R1-F4 should-fix open
- Round 2 on version 11: 5 findings; R1-F1 should-fix resolved, R1-F2 should-fix resolved, R1-F3 should-fix open, R1-F4 should-fix open, R2-F1 should-fix open
- Round 3 on version 12: 5 findings; R1-F1 should-fix resolved, R1-F2 should-fix resolved, R1-F3 should-fix resolved, R1-F4 should-fix resolved, R2-F1 should-fix open

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1579 NCBI requests logged (862 from cache); strategy sha256 eafd29942e3a._

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
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:consumption",
        "blocking": false,
        "requires_review": true,
        "id": "I-0da39503258dbd9b0da8"
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
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:consumption",
        "blocking": false,
        "requires_review": true,
        "id": "I-0da39503258dbd9b0da8"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Health Education",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:34:41+00:00",
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
      "requested": "Nutritional Sciences",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:34:41+00:00",
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
      "location": "vocabulary:2",
      "term": {
        "text": "\"Nutritional Sciences\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Child Nutrition Sciences",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:34:41+00:00",
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
      "location": "vocabulary:3",
      "term": {
        "text": "\"Child Nutrition Sciences\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Feeding Behavior",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:34:41+00:00",
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
      "requested": "Curriculum",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:34:41+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "Q000193",
          "name": "education",
          "type": "qualifier",
          "scope_note": "Used for education, training programs, and courses in various fields and disciplines, and for training groups of persons.",
          "tree_numbers": [
            "Y23"
          ],
          "entry_terms": 3,
          "mapped_to": null
        },
        {
          "ui": "D003479",
          "name": "Curriculum",
          "type": "descriptor",
          "scope_note": "A course of study offered by an educational institution.",
          "tree_numbers": [
            "I02.158"
          ],
          "entry_terms": 6,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003479",
      "preferred_label": "Curriculum",
      "type": "descriptor",
      "location": "vocabulary:5",
      "term": {
        "text": "\"Curriculum\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "School Health Services",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:34:41+00:00",
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
      "location": "vocabulary:6",
      "term": {
        "text": "\"School Health Services\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Schools",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:34:41+00:00",
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
      "location": "vocabulary:34",
      "term": {
        "text": "\"Schools\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "School Health Services",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T03:34:41+00:00",
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
      "location": "vocabulary:35",
      "term": {
        "text": "\"School Health Services\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "((\"Health Education\"[MeSH Terms] AND (\"Nutritional Sciences\"[MeSH Terms] OR \"Child Nutrition Sciences\"[MeSH Terms] OR \"Feeding Behavior\"[MeSH Terms])) OR (\"Curriculum\"[MeSH Terms] AND \"School Health Services\"[MeSH Terms]) OR (\"school*\"[Title/Abstract] AND (\"nutrition\"[Title/Abstract] OR \"food\"[Title/Abstract] OR \"dietary\"[Title/Abstract]) AND (\"Curriculum\"[Title/Abstract] OR \"lesson*\"[Title/Abstract] OR \"educat*\"[Title/Abstract] OR \"teach*\"[Title/Abstract])) OR \"food education\"[Title/Abstract] OR \"nutrition education\"[Title/Abstract] OR \"dietary education\"[Title/Abstract] OR \"nutrition teaching\"[Title/Abstract] OR \"food and nutrition education\"[Title/Abstract] OR \"nutrition instruction\"[Title/Abstract] OR \"food literacy\"[Title/Abstract] OR \"nutrition literacy\"[Title/Abstract] OR \"nutrition curriculum\"[Title/Abstract] OR (\"food\"[Title/Abstract] AND \"curricul*\"[Title/Abstract]) OR \"nutrition program\"[Title/Abstract] OR \"nutrition programs\"[Title/Abstract] OR \"dietary intervention\"[Title/Abstract] OR \"food intervention\"[Title/Abstract] OR \"nutrition intervention\"[Title/Abstract] OR \"food-based intervention\"[Title/Abstract] OR \"food-based interventions\"[Title/Abstract] OR \"nutrition promot*\"[Title/Abstract]) AND (\"Schools\"[MeSH Terms] OR \"School Health Services\"[MeSH Terms] OR \"school*\"[Title/Abstract] OR \"classroom*\"[Title/Abstract] OR \"school-based\"[Title/Abstract] OR \"school-based\"[Title/Abstract] OR \"classroom-based\"[Title/Abstract] OR \"classroom-based\"[Title/Abstract] OR \"school setting\"[Title/Abstract] OR \"school settings\"[Title/Abstract] OR \"kindergarten*\"[Title/Abstract]) AND 1800/01/01:2017/12/14[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 10,
      "review_sha256": "a70359bc59b82f4a812084bad5a9153a4ba35b8211a987721921e6638d4075c1",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The stated scope is partly translated, but the optional population and outcome blocks have stale validation, and the final inclusion of population and setting blocks is supported mainly by small samples. The outcome block is correctly left out for recall, but the packet does not establish independent seed validation of the final search."
        },
        "operators": {
          "verdict": "pass",
          "note": "The visible strategy combines the intervention, population, and setting blocks with AND and terms within blocks with OR. No Boolean grouping error is apparent in the supplied strategy."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy uses relevant MeSH headings for health education, curriculum, nutrition/feeding behavior, adolescents, students, children, schools, and school health services. The packet does not show a demonstrable heading mapping error."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The exact phrase ‘food curriculum’ returns zero records and generated a PubMed warning in a date-restricted probe. That warning cannot be cleared by the displayed full-strategy count; the phrase clause needs an explicit clause-specific translation check. The category probes also do not provide independent validation of text-word coverage."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No malformed field tags, unbalanced grouping, or other syntax defect is evident in the supplied expressions. The PubMed warning is tied to the zero-hit phrase probe and its date restriction, so it is addressed as a text-word/translation issue rather than a demonstrated syntax error."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The final strategy lists no limits. The dated probe for ‘food curriculum’ is a diagnostic query, not evidence that a date limit is applied to the final strategy."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The population category probe is stale and its two-probe budget is spent. The report nevertheless relies on the category probe being clean to justify AND-ing the population block; probe 2 screened zero records, which supplies no additional screening evidence.",
          "recommendation": "Refresh the population category probe against the current block and current final strategy, or remove the clean-probe claim from the rationale and report the population block as an unvalidated recall risk. A zero-record probe must not be described as a clean screen.",
          "status": "open"
        },
        {
          "id": "R1-F2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The eligible food-consumption outcome candidate and its category probe are stale. Although the outcome block is left out of the final query, the packet's category history has two positive findings outside the block (2/30 in each probe) and cannot validate the revised candidate or its coverage.",
          "recommendation": "Refresh the outcome category probe after the candidate is finalized, or clearly state that the category probe is not evidence for the final strategy because the outcome block is excluded. Preserve the rationale for leaving the outcome block out unless a complete re-evaluation supports another decision.",
          "status": "open"
        },
        {
          "id": "R1-F3",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The exact phrase ‘food curriculum’ produced zero hits and PubMed's ‘No items found’ warning in a probe restricted to entry dates through 2017-12-14. This is a real warning for the tested expression, but the date-restricted probe does not establish whether the expression has zero contribution in the current full-date strategy or whether a variant captures records.",
          "recommendation": "Inspect the phrase clause itself and test explicit alternatives such as food[tiab] AND curriculum[tiab] and appropriate curriculum word variants with the current date scope. Record the translated expression and counts. Do not declare the phrase redundant from seed coverage; any rewrite or removal requires a complete re-evaluation.",
          "status": "open"
        },
        {
          "id": "R1-F4",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The packet reports retrieval of 30 known records by the final/base query but provides no independent seed validation set, development/validation split, or independent validation result. The same known records used to develop or tune the blocks cannot establish independent sensitivity.",
          "recommendation": "Report explicitly that independent seed validation was not performed. If a separate set of known eligible records is available, validate the frozen final strategy against it and report misses; do not present the current 30-record check as independent validation.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-17c831561da839c02d17",
          "status": "accepted-risk",
          "response": "The diagnostic is valid and cannot be dismissed: the population block changed after its last probe and the probe budget is spent. The claim that the follow-up category probe found zero outside records does not close this warning because zero were screened. Treat population-block recall as unvalidated pending a refreshed probe.",
          "evidence": "Validation issue says category_probe_stale_budget_spent at concept:population. History shows probe 2 outside_count 0, screened 0, and status stale."
        },
        {
          "issue_id": "I-0da39503258dbd9b0da8",
          "status": "accepted-risk",
          "response": "The diagnostic is valid. The outcome block is not in the final search, so the stale candidate probe does not change the final query's retrieval, but it cannot support claims about the revised candidate's coverage. Keep the outcome block left out for recall pending any complete reevaluation.",
          "evidence": "Validation issue says category_probe_stale_budget_spent at concept:consumption. The final strategy has no outcome block; history is stale and both prior probes found 2 relevant outside records among 30 screened."
        },
        {
          "issue_id": "I-163152d0ac6ce4444140",
          "status": "accepted-risk",
          "response": "The PubMed warning is credible for the tested query and needs clause-specific follow-up. The date restriction shown in the warning means the probe cannot establish the phrase's behavior over the full date scope of the final strategy.",
          "evidence": "PubMed output says ‘No items found’ for the translated phrase query with entry dates 1800/01/01 through 2017/12/14; the strategy line is the exact phrase ‘food curriculum’[tiab]."
        },
        {
          "issue_id": "I-b6dcd0a03f0b1ad02a31",
          "status": "accepted-risk",
          "response": "Accept the zero-hit warning as an unresolved lexical risk, not as evidence that the term is redundant or safe to delete. Test an explicit unquoted/variant expression and rerun the complete evaluation before rewriting or removing it.",
          "evidence": "The term-level table reports 0 results for ‘food curriculum’[tiab], while the warning query is date-restricted and translated as a quoted Title/Abstract phrase."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 11,
      "review_sha256": "7678ff3d1601ff97bcfdb526dacabfef50e883fa8e6889572fc95a09d3a043c3",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The outcome block remains excluded with a documented recall rationale, and the population block is also left out without claiming a clean category probe. However, the required education block has a stale category probe, and the packet does not report independent seed validation. The included school setting block is supported by the stated known-record and loss-sample checks, subject to the limitations of those small samples."
        },
        "operators": {
          "verdict": "pass",
          "note": "The displayed construction ORs terms within the education and school-setting blocks and ANDs those blocks in the final query. No grouping defect is evident."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The education and setting blocks use relevant displayed MeSH headings, and the packet supplies no demonstrable heading mapping error."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The exact phrase food curriculum still has zero hits and the PubMed No items found warning. No clause-specific test of food[tiab] AND curriculum[tiab] or other explicit variants is reported, so the warning remains unresolved."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No malformed field tags, unbalanced grouping, or other syntax defect is evident in the supplied expressions. The food curriculum warning is an unresolved retrieval/lexical issue rather than a demonstrated syntax error."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The final strategy has no limits. The entry-date range appears only in the diagnostic phrase query and does not establish a limit on the final strategy."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The population category probe is stale and its two-probe budget is spent. The earlier rationale relied on a clean category probe even though probe 2 screened zero records.",
          "recommendation": "Do not use the stale probe as evidence of population-block coverage; describe population recall as unvalidated or refresh the probe before using that block.",
          "status": "resolved",
          "response": "The current decision leaves the optional population block out and explicitly says the category probe is stale, so it no longer relies on a clean-probe claim. The packet still records a population recall risk, which is covered by mandatory issue I-17c831561da839c02d17."
        },
        {
          "id": "R1-F2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The outcome candidate and its category probe are stale; the category history cannot validate the revised candidate or its coverage.",
          "recommendation": "Do not treat the stale category probe as evidence for the final strategy. Keep the outcome block excluded unless a complete re-evaluation supports another decision.",
          "status": "resolved",
          "response": "The final strategy excludes the outcome block, and the current rationale bases that choice on the 3,993-record reduction, a relevant known record lost, and the fresh loss sample; it makes no clean category-probe claim. The stale candidate remains a documented limitation, covered by mandatory issue I-0da39503258dbd9b0da8."
        },
        {
          "id": "R1-F3",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The exact phrase food curriculum still returns zero records with PubMed's No items found warning in a date-restricted diagnostic. The packet provides no clause-specific test of the phrase alternatives or full-date behavior.",
          "recommendation": "Test explicit alternatives such as food[tiab] AND curriculum[tiab] and relevant curriculum variants, record the translated expressions and counts, and rerun the complete evaluation before any rewrite or removal.",
          "status": "open"
        },
        {
          "id": "R1-F4",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The packet still reports known-record retrieval but provides no independent seed validation set, development/validation split, or explicit statement that independent validation was not performed.",
          "recommendation": "Report that independent seed validation was not performed, or validate the frozen final strategy against a separate eligible-record set and report misses.",
          "status": "open"
        },
        {
          "id": "R2-F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The education block is part of the final query, but its category probe is stale and the probe budget is spent. The reported category samples therefore do not validate the current education block.",
          "recommendation": "Treat education-block coverage as unvalidated and remove any implication that the stale category probes establish its coverage; refresh validation if permitted before relying on that evidence.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-dbf95b02a2f5650da634",
          "status": "accepted-risk",
          "response": "The stale education category-probe warning is valid. Accept it only as an explicit limitation: the education block remains in the final strategy, but the stale probe is not evidence that the block has adequate category coverage.",
          "evidence": "Validation labels concept:education category_probe_stale_budget_spent; its two-probe budget is spent and the block changed after the last probe. The packet reports no current education category probe."
        },
        {
          "issue_id": "I-17c831561da839c02d17",
          "status": "accepted-risk",
          "response": "The warning is valid and the population block is omitted, with the current rationale explicitly acknowledging that the category probe is stale and cannot support a clean-probe claim. Population recall remains unvalidated.",
          "evidence": "The optional population decision is leave_out; its rationale says the category probe is stale. Probe 2 had outside_count 0 and screened 0 records, which is no screening evidence."
        },
        {
          "issue_id": "I-0da39503258dbd9b0da8",
          "status": "accepted-risk",
          "response": "The stale outcome-candidate warning is valid but does not affect the final query because the outcome block is excluded. The choice is instead supported by the current loss sample and known-record loss; the stale category history must not be used to claim coverage.",
          "evidence": "Validation labels concept:consumption category_probe_stale_budget_spent. The final strategy has no consumption block; the current loss sample found relevant PMID 11918492 among 30 records, and the decision reports 3,993 removed records."
        },
        {
          "issue_id": "I-163152d0ac6ce4444140",
          "status": "accepted-risk",
          "response": "The warning remains unresolved. Accept it as an outstanding lexical risk pending clause-specific follow-up; do not infer redundancy or safe removal.",
          "evidence": "PubMed reports No items found for the quoted food curriculum phrase with an entry-date range ending 2017-12-14. No alternative phrase query or full-date clause test appears in the packet."
        },
        {
          "issue_id": "I-b6dcd0a03f0b1ad02a31",
          "status": "accepted-risk",
          "response": "The zero-hit warning remains unresolved. Retain the expression only as an acknowledged risk until explicit variants are tested and the complete strategy is reevaluated.",
          "evidence": "The term table reports 0 hits for food curriculum[tiab], with a date-restricted diagnostic and a No items found output. The packet gives no alternate-expression count."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 12,
      "review_sha256": "6572765e08295d92801f8f0ddf0cbd08dab21babd4657d5743f6698bd16e616d",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The education block remains in the required final query after changing since the last probe, and its category-probe budget is spent; the stale probe does not validate its coverage. Population and outcome blocks are omitted with explicit recall rationales and no clean-probe claims. The scope notes disclose that records used for development are not an independent validation set."
        },
        "operators": {
          "verdict": "pass",
          "note": "The visible strategy ORs terms within the education and setting blocks and ANDs those blocks. No Boolean grouping defect is shown."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The displayed MeSH headings are relevant to health education, curriculum, nutrition/feeding behavior, schools, and school health services; the packet provides no demonstrable heading-mapping error."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The current education terms replace the zero-hit quoted phrase food curriculum with the explicit expression (food[tiab] AND curricul*[tiab]), which has 540 results in the term table. The full current strategy is reported at 7,762 results, with no known records lost or gained since the prior version. The stale education category probe is a coverage-validation limitation, not an unresolved warning on the removed phrase."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No malformed field tags, unbalanced grouping, or other syntax defect is evident in the displayed expressions."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The final strategy lists no limits. The entry-date restriction appears only in the historical diagnostic for the removed quoted phrase."
        }
      },
      "findings": [
        {
          "id": "R1-F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The population category probe is stale and its two-probe budget is spent; the earlier rationale relied on a clean category probe despite probe 2 screening zero records.",
          "recommendation": "Do not use the stale probe as evidence of population-block coverage; describe population recall as unvalidated or refresh the probe before using that block.",
          "status": "resolved",
          "response": "The population block is left out, and its current rationale explicitly says the category probe is stale and does not rely on a clean-probe claim. Population recall risk remains disclosed and is covered by accepted-risk issue I-17c831561da839c02d17."
        },
        {
          "id": "R1-F2",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The outcome candidate and its category probe are stale and cannot validate coverage of the revised candidate.",
          "recommendation": "Do not treat the stale category probe as evidence for the final strategy; keep the outcome block excluded unless complete reevaluation supports another decision.",
          "status": "resolved",
          "response": "The outcome block is excluded from the final query. The current rationale instead cites the measured reduction, a relevant known record lost, and the fresh loss sample; it makes no clean category-probe claim. The stale candidate limitation is covered by accepted-risk issue I-0da39503258dbd9b0da8."
        },
        {
          "id": "R1-F3",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The exact phrase food curriculum previously returned zero records and a PubMed warning in a date-restricted diagnostic, without testing explicit alternatives or full-date behavior.",
          "recommendation": "Test explicit alternatives, record their translations and counts, and reevaluate the complete strategy before rewriting or removing the expression.",
          "status": "resolved",
          "response": "The current strategy removes the quoted food curriculum phrase and includes the explicit expression (food[tiab] AND curricul*[tiab]), reported with 540 results. Strategy version 12 reports 7,762 results, no known records lost or gained since version 11, and refreshed decision diagnostics. The historical warning is therefore addressed for the current expression; the education category probe remains a separate stale-coverage limitation."
        },
        {
          "id": "R1-F4",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "Known-record retrieval was reported without an independent seed validation set or explicit disclosure that independent validation was not performed.",
          "recommendation": "Disclose that independent seed validation was not performed, or validate the frozen strategy against a separate eligible-record set and report misses.",
          "status": "resolved",
          "response": "The scope notes disclose that no known relevant articles were supplied and that records screened into the relevant development set, including the miss that prompted a strategy change, make that set no longer independent validation. The current known-record checks are therefore not represented as an independent validation result."
        },
        {
          "id": "R2-F1",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The required education block is in the final query, but its category probe is stale and the reported samples do not validate the current block.",
          "recommendation": "Treat education-block coverage as unvalidated and do not imply that the stale category probes establish adequate coverage.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-dbf95b02a2f5650da634",
          "status": "accepted-risk",
          "response": "The warning remains valid. The education block is still in the final query, so accept the stale-probe limitation explicitly; the existing probe cannot establish adequate current category coverage.",
          "evidence": "The packet lists category_probe_stale_budget_spent at concept:education. The strategy changed after the last probe, the two-probe budget is spent, and no current education category probe is reported."
        },
        {
          "issue_id": "I-17c831561da839c02d17",
          "status": "accepted-risk",
          "response": "The warning remains valid, but the population block is omitted and the current rationale no longer treats the stale probe as evidence of coverage. Population recall remains unvalidated.",
          "evidence": "The optional population decision is leave_out and its rationale calls the category probe stale. Probe 2 screened zero records (0/0), so it supplies no screening evidence."
        },
        {
          "issue_id": "I-0da39503258dbd9b0da8",
          "status": "accepted-risk",
          "response": "The warning remains valid for the optional outcome candidate, but that block is omitted from the final search. Its stale probe is not used to justify final-query coverage; the block remains excluded under the documented recall rationale.",
          "evidence": "The packet lists category_probe_stale_budget_spent at concept:consumption; the final strategy has no consumption block. The current loss sample reports relevant PMID 11918492 among 30 records, and the rationale reports a 3,993-record reduction if the block were AND-ed."
        }
      ]
    }
  ]
}
```

