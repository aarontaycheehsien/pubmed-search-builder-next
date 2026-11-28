# PubMed search strategy: audit

Generated 2026-11-27T17:29:39+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: School-based food and nutrition education interventions for adolescent food consumption
- Framework: PICO
- Scope confirmed by user: yes (User gave no seeds, standard depth, could not answer questions; proceeded with defaults. Assumption: 'adolescents or school students' kept optional (measured); school and nutrition education are AND-ed. No design limits. Scope not paused for confirmation per user instruction. No independent known records: no seeds, PubMed holds no reference lists for 3 prior reviews, OpenAlex unavailable (budget). Recall is not estimated; 6 title-screened pilot records check wording only. Adolescents block left optional and not AND-ed: loss unmeasured; result see latest eval, assumed screenable for a high-sensitivity review. Broad MeSH (Health Education, Health Promotion, Diet Food and Nutrition) dropped for noise. Search date bound 2017-12-14 is the as-of date pinned by the run harness (Entrez date), not a review limit. Removed Nutritional Sciences/Food Services MeSH (discipline/service headings, not education).)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Food or nutrition education intervention | search | core intervention, named in titles/abstracts and MeSH |
| School setting / delivered through a school | search | definitional setting; schools reliably named and indexed (School, Students MeSH) |
| Adolescents or school students | optional | age often unstated in abstracts (students, pupils, children); tested as optional: AND-ing loses 0 of the known records but loss is unmeasured (no independent known records); left out so the result stays screenable; see latest eval for counts |
| Food consumption outcome | screen | outcome; unreliably named in abstracts, judged at screening |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-11-27T17:29:09+00:00
- Records added to PubMed up to: 2017-12-14
- Total records: 8,292
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"nutrition education"[tiab]` | 3,866 | none |
| 2 | `"nutritional education"[tiab]` | 744 | none |
| 3 | `"nutrition educat*"[tiab]` | 4,029 | none |
| 4 | `"food education"[tiab]` | 84 | none |
| 5 | `"dietary education"[tiab]` | 252 | none |
| 6 | `"diet education"[tiab]` | 115 | none |
| 7 | `"nutrition teaching"[tiab]` | 72 | none |
| 8 | `"nutrition intervention*"[tiab]` | 1,929 | none |
| 9 | `"nutritional intervention*"[tiab]` | 3,454 | none |
| 10 | `"dietary intervention*"[tiab]` | 5,988 | none |
| 11 | `"diet intervention*"[tiab]` | 731 | none |
| 12 | `"food intervention*"[tiab]` | 66 | none |
| 13 | `"nutrition program*"[tiab]` | 2,437 | none |
| 14 | `"nutrition curricul*"[tiab]` | 97 | none |
| 15 | `"nutrition lesson*"[tiab]` | 28 | none |
| 16 | `"nutrition promotion"[tiab]` | 129 | none |
| 17 | `"healthy eating"[tiab]` | 5,052 | none |
| 18 | `"healthy diet*"[tiab]` | 4,213 | none |
| 19 | `"healthy food*"[tiab]` | 2,889 | none |
| 20 | `"food literacy"[tiab]` | 34 | none |
| 21 | `"nutrition literacy"[tiab]` | 48 | none |
| 22 | `"school meal*"[tiab]` | 667 | none |
| 23 | `"school lunch*"[tiab]` | 789 | none |
| 24 | `"school breakfast*"[tiab]` | 194 | none |
| 25 | `"school garden*"[tiab]` | 68 | none |
| 26 | `"school food*"[tiab]` | 492 | none |
| 27 | `"school canteen*"[tiab]` | 141 | none |
| 28 | `"school cafeteria*"[tiab]` | 161 | none |
| 29 | `"tuck shop*"[tiab]` | 23 | none |
| 30 | `"fruit and vegetable*"[tiab]` | 7,343 | none |
| 31 | `"nutrition education"[tiab:~3]` | 5,090 | none |
| 32 | `"nutrition intervention"[tiab:~3]` | 2,114 | none |
| 33 | `"nutrition program"[tiab:~3]` | 2,664 | none |
| 34 | `"dietary intervention"[tiab:~3]` | 5,484 | none |
| 35 | `"nutrition curriculum"[tiab:~3]` | 223 | none |
| 36 | `"food education"[tiab:~1]` | 594 | none |
| 37 | `"diet education"[tiab:~1]` | 363 | none |
| 38 | `"dietary education"[tiab:~1]` | 503 | none |
| 39 | `"nutrition counsel*"[tiab]` | 724 | none |
| 40 | `"dietary counsel*"[tiab]` | 1,224 | none |
| 41 | `"nutrition knowledge"[tiab]` | 922 | none |
| 42 | `"food skills"[tiab]` | 31 | none |
| 43 | `"cooking class*"[tiab]` | 73 | none |
| 44 | `"cooking skill*"[tiab]` | 121 | none |
| 45 | `"cooking program*"[tiab]` | 25 | none |
| 46 | `"gardening program*"[tiab]` | 34 | none |
| 47 | `"Diet, Healthy"[Mesh]` | 1,820 | none |
| 48 | `("health education"[tiab:~3] AND (diet*[tiab] OR nutrition*[tiab] OR food*[tiab]))` | 5,040 | none |
| 49 | `"healthy eating"[tiab:~3]` | 5,665 | none |
| 50 | `"nutritional curricul*"[tiab]` | 4 | none |
| 51 | `"diet* curricul*"[tiab]` | 18 | none |
| 52 | `"garden-based"[tiab]` | 22 | none |
| 53 | `"gardening"[tiab]` | 1,088 | none |
| 54 | `"nutrition class*"[tiab]` | 201 | none |
| 55 | `"food lesson*"[tiab]` | 1 | none |
| 56 | `"nutrition-based"[tiab]` | 170 | none |
| 57 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56` | 48,086 | none |
| 58 | `"Schools"[Mesh]` | 107,820 | none |
| 59 | `"School Health Services"[Mesh]` | 21,872 | none |
| 60 | `"Students"[Mesh]` | 112,973 | none |
| 61 | `school*[tiab]` | 246,616 | none |
| 62 | `schoolchild*[tiab]` | 13,052 | none |
| 63 | `schoolgirl*[tiab]` | 785 | none |
| 64 | `schoolboy*[tiab]` | 469 | none |
| 65 | `schoolbased[tiab]` | 10,120 | none |
| 66 | `pupil*[tiab]` | 26,074 | none |
| 67 | `student*[tiab]` | 234,057 | none |
| 68 | `classroom*[tiab]` | 14,158 | none |
| 69 | `"secondary education"[tiab]` | 1,898 | none |
| 70 | `"high school*"[tiab]` | 27,027 | none |
| 71 | `"middle school*"[tiab]` | 4,703 | none |
| 72 | `"junior high"[tiab]` | 2,267 | none |
| 73 | `"senior high"[tiab]` | 917 | none |
| 74 | `#58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67 OR #68 OR #69 OR #70 OR #71 OR #72 OR #73` | 510,319 | none |
| 75 | `#57 AND #74` | 8,292 | none |

### Strategy (single line, for copying into PubMed)

```text
(("nutrition education"[tiab] OR "nutritional education"[tiab] OR "nutrition educat*"[tiab] OR "food education"[tiab] OR "dietary education"[tiab] OR "diet education"[tiab] OR "nutrition teaching"[tiab] OR "nutrition intervention*"[tiab] OR "nutritional intervention*"[tiab] OR "dietary intervention*"[tiab] OR "diet intervention*"[tiab] OR "food intervention*"[tiab] OR "nutrition program*"[tiab] OR "nutrition curricul*"[tiab] OR "nutrition lesson*"[tiab] OR "nutrition promotion"[tiab] OR "healthy eating"[tiab] OR "healthy diet*"[tiab] OR "healthy food*"[tiab] OR "food literacy"[tiab] OR "nutrition literacy"[tiab] OR "school meal*"[tiab] OR "school lunch*"[tiab] OR "school breakfast*"[tiab] OR "school garden*"[tiab] OR "school food*"[tiab] OR "school canteen*"[tiab] OR "school cafeteria*"[tiab] OR "tuck shop*"[tiab] OR "fruit and vegetable*"[tiab] OR "nutrition education"[tiab:~3] OR "nutrition intervention"[tiab:~3] OR "nutrition program"[tiab:~3] OR "dietary intervention"[tiab:~3] OR "nutrition curriculum"[tiab:~3] OR "food education"[tiab:~1] OR "diet education"[tiab:~1] OR "dietary education"[tiab:~1] OR "nutrition counsel*"[tiab] OR "dietary counsel*"[tiab] OR "nutrition knowledge"[tiab] OR "food skills"[tiab] OR "cooking class*"[tiab] OR "cooking skill*"[tiab] OR "cooking program*"[tiab] OR "gardening program*"[tiab] OR "Diet, Healthy"[Mesh] OR ("health education"[tiab:~3] AND (diet*[tiab] OR nutrition*[tiab] OR food*[tiab])) OR "healthy eating"[tiab:~3] OR "nutritional curricul*"[tiab] OR "diet* curricul*"[tiab] OR "garden-based"[tiab] OR "gardening"[tiab] OR "nutrition class*"[tiab] OR "food lesson*"[tiab] OR "nutrition-based"[tiab]) AND ("Schools"[Mesh] OR "School Health Services"[Mesh] OR "Students"[Mesh] OR school*[tiab] OR schoolchild*[tiab] OR schoolgirl*[tiab] OR schoolboy*[tiab] OR schoolbased[tiab] OR pupil*[tiab] OR student*[tiab] OR classroom*[tiab] OR "secondary education"[tiab] OR "high school*"[tiab] OR "middle school*"[tiab] OR "junior high"[tiab] OR "senior high"[tiab])) AND ("1800/01/01"[edat] : "2017/12/14"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall | Found without a keyword search: retrieved / in PubMed |
|---|---|---:|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 6 | 6 | 100.0% | 0 / 0 |

Every known record came from a keyword search, or from the similar or citing articles of one. Such records name the searched words by construction, so the recall figures check the strategy's wording; they do not estimate recall. A prior review's reference list (psb neighbors <review PMID> --links refs) gives records that do not depend on your wording.

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| nutrition_ed | 510,319 | 0 |
| school | 48,086 | 0 |

### Optional blocks (measured, not searched)

Each row is the effect of AND-ing a concept that is not part of the strategy. Independent records are known records that no keyword search led to (user seeds, a review's reference list); only they can show what a block would lose, and the 95% bound is the largest share of relevant records it could lose on their evidence.

| Block | Records now | Records if AND-ed | Known lost / retrieved now | Independent lost / retrieved now | 95% bound on share lost |
|---|---:|---:|---:|---:|---:|
| Adolescents or school students (adolescents) | 8,292 | 5,968 | 0 / 6 | 0 / 0 | unmeasured |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 50,536 | initial | none | first draft |
| 2 | 16,257 | nutrition_ed: +1 / -3; school: +0 / -2 | none | dropped broad Health Education/Health Promotion/Diet Food Nutrition MeSH and curricul*/teacher* (30%+27% of result from noise, no known loss); added Feeding Behavior |
| 3 | 16,590 | nutrition_ed: +1 / -1 | none | replaced subheading combination with unqualified Nutritional Sciences heading |
| 4 | 21,758 | nutrition_ed: +12 / -14 | none | critic F1-F4: removed outcome/behaviour terms, Feeding Behavior, Nutrition Policy, loose proximity; added counselling, cooking, knowledge terms |
| 5 | 9,327 | nutrition_ed: +0 / -1 | none | removed health education proximity: 57% of result alone, school-health-education noise, no known record |
| 6 | 10,249 | nutrition_ed: +3 / -0 | none | critic round 1: added Diet Healthy MeSH, tight health education+diet/nutrition/food compound, healthy eating proximity; refreshed notes |
| 7 | 8,292 | nutrition_ed: +7 / -2 | none | critic r1: dropped Nutritional Sciences/Food Services MeSH; added curriculum/garden/class/lesson terms; as_of recorded |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 7: 8 findings; F1 should-fix accepted-risk, F2 should-fix accepted-risk, F3 should-fix accepted-risk, F4 document accepted-risk, F5 document accepted-risk, F6 should-fix rejected, F7 document accepted-risk, F8 document accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 1666 NCBI requests logged (805 from cache); strategy sha256 41511b07546c._

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
      "requested": "Diet, Healthy",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T17:29:09+00:00",
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
      "location": "vocabulary:47",
      "term": {
        "text": "\"Diet, Healthy\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Schools",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T17:29:09+00:00",
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
      "location": "vocabulary:60",
      "term": {
        "text": "\"Schools\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "School Health Services",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T17:29:09+00:00",
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
      "location": "vocabulary:61",
      "term": {
        "text": "\"School Health Services\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Students",
      "expected_type": "descriptor",
      "checked_at": "2026-11-27T17:29:09+00:00",
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
      "location": "vocabulary:62",
      "term": {
        "text": "\"Students\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"nutrition education\"[Title/Abstract] OR \"nutritional education\"[Title/Abstract] OR \"nutrition educat*\"[Title/Abstract] OR \"food education\"[Title/Abstract] OR \"dietary education\"[Title/Abstract] OR \"diet education\"[Title/Abstract] OR \"nutrition teaching\"[Title/Abstract] OR \"nutrition intervention*\"[Title/Abstract] OR \"nutritional intervention*\"[Title/Abstract] OR \"dietary intervention*\"[Title/Abstract] OR \"diet intervention*\"[Title/Abstract] OR \"food intervention*\"[Title/Abstract] OR \"nutrition program*\"[Title/Abstract] OR \"nutrition curricul*\"[Title/Abstract] OR \"nutrition lesson*\"[Title/Abstract] OR \"nutrition promotion\"[Title/Abstract] OR \"healthy eating\"[Title/Abstract] OR \"healthy diet*\"[Title/Abstract] OR \"healthy food*\"[Title/Abstract] OR \"food literacy\"[Title/Abstract] OR \"nutrition literacy\"[Title/Abstract] OR \"school meal*\"[Title/Abstract] OR \"school lunch*\"[Title/Abstract] OR \"school breakfast*\"[Title/Abstract] OR \"school garden*\"[Title/Abstract] OR \"school food*\"[Title/Abstract] OR \"school canteen*\"[Title/Abstract] OR \"school cafeteria*\"[Title/Abstract] OR \"tuck shop*\"[Title/Abstract] OR \"fruit and vegetable*\"[Title/Abstract] OR \"nutrition education\"[Title/Abstract:~3] OR \"nutrition intervention\"[Title/Abstract:~3] OR \"nutrition program\"[Title/Abstract:~3] OR \"dietary intervention\"[Title/Abstract:~3] OR \"nutrition curriculum\"[Title/Abstract:~3] OR \"food education\"[Title/Abstract:~1] OR \"diet education\"[Title/Abstract:~1] OR \"dietary education\"[Title/Abstract:~1] OR \"nutrition counsel*\"[Title/Abstract] OR \"dietary counsel*\"[Title/Abstract] OR \"nutrition knowledge\"[Title/Abstract] OR \"food skills\"[Title/Abstract] OR \"cooking class*\"[Title/Abstract] OR \"cooking skill*\"[Title/Abstract] OR \"cooking program*\"[Title/Abstract] OR \"gardening program*\"[Title/Abstract] OR \"diet, healthy\"[MeSH Terms] OR (\"health education\"[Title/Abstract:~3] AND (\"diet*\"[Title/Abstract] OR \"nutrition*\"[Title/Abstract] OR \"food*\"[Title/Abstract])) OR \"healthy eating\"[Title/Abstract:~3] OR \"nutritional curricul*\"[Title/Abstract] OR \"diet* curricul*\"[Title/Abstract] OR \"garden-based\"[Title/Abstract] OR \"gardening\"[Title/Abstract] OR \"nutrition class*\"[Title/Abstract] OR \"food lesson*\"[Title/Abstract] OR \"nutrition-based\"[Title/Abstract]) AND (\"Schools\"[MeSH Terms] OR \"School Health Services\"[MeSH Terms] OR \"Students\"[MeSH Terms] OR \"school*\"[Title/Abstract] OR \"schoolchild*\"[Title/Abstract] OR \"schoolgirl*\"[Title/Abstract] OR \"schoolboy*\"[Title/Abstract] OR \"schoolbased\"[Title/Abstract] OR \"pupil*\"[Title/Abstract] OR \"student*\"[Title/Abstract] OR \"classroom*\"[Title/Abstract] OR \"secondary education\"[Title/Abstract] OR \"high school*\"[Title/Abstract] OR \"middle school*\"[Title/Abstract] OR \"junior high\"[Title/Abstract] OR \"senior high\"[Title/Abstract]) AND 1800/01/01:2017/12/14[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 7,
      "review_sha256": "4dc7f31e77f40114ddaf30eb4c1b983b790b86fdc8de0b715f01da534dda3c90",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "see F1,F2,F6"
        },
        "operators": {
          "verdict": "revise",
          "note": "see F1,F4"
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Diet, Healthy adds records; school headings verified"
        },
        "text_words": {
          "verdict": "revise",
          "note": "see F2,F3,F5"
        },
        "syntax": {
          "verdict": "pass",
          "note": "no warnings or translation issues"
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "only bound is the harness as-of date"
        }
      },
      "findings": [
        {
          "id": "F1",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "School food provision terms sit in the intervention block and are satisfied by school*.",
          "recommendation": "see response",
          "status": "accepted-risk",
          "response": "Multicomponent school nutrition education studies commonly include school meal, garden or canteen components and describe them this way; kept for recall (about 1,200 unique records) and screened for an education component. Eligibility is unchanged."
        },
        {
          "id": "F2",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "Food/diet phrases and a health-education proximity compound add off-topic volume.",
          "recommendation": "see response",
          "status": "accepted-risk",
          "response": "Kept for recall: these label healthy-eating programmes in school; the consumption outcome stays a screening criterion. Volume (8,292) assumed screenable for a high-sensitivity review; noise reduction would be unmeasured recall loss."
        },
        {
          "id": "F3",
          "domain": "subject_headings",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "school* and Students MeSH are broad and include university/professional schools.",
          "recommendation": "see response",
          "status": "accepted-risk",
          "response": "Adult, university and preschool records are removed at screening; narrowing school* on the non-independent known set would risk recall."
        },
        {
          "id": "F4",
          "domain": "operators",
          "severity": "document",
          "kind": "scope",
          "finding": "Adolescent block optional; loss unmeasured.",
          "recommendation": "see response",
          "status": "accepted-risk",
          "response": "Left out of the AND: 0 of 6 known lost but none independent, so loss is unmeasured; age is screened at title/abstract. Recall is not estimated."
        },
        {
          "id": "F5",
          "domain": "text_words",
          "severity": "document",
          "kind": "lexical",
          "finding": "Redundant exact phrases retained.",
          "recommendation": "see response",
          "status": "accepted-risk",
          "response": "Retained for transparency; no volume cost."
        },
        {
          "id": "F6",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "Indirect obesity-prevention/health-promotion labels not searched.",
          "recommendation": "see response",
          "status": "rejected",
          "response": "Eligibility is food or nutrition education; obesity-prevention or health-promotion terms would AND with school* to many thousands of records with weight outcomes, not food consumption. Not added; limitation recorded."
        },
        {
          "id": "F7",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "Date bound is the harness as-of date.",
          "recommendation": "see response",
          "status": "accepted-risk",
          "response": "The upper bound 2017/12/14 on Entry date is the run's as-of date, not a review limit; reported as such."
        },
        {
          "id": "F8",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "reporting",
          "finding": "Recall not estimated.",
          "recommendation": "see response",
          "status": "accepted-risk",
          "response": "Recall is reported as unmeasured; 6 title-screened pilot records check wording only."
        }
      ],
      "issue_dispositions": []
    }
  ]
}
```

