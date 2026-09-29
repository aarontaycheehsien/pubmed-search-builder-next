# PubMed search strategy: audit

Generated 2026-09-28T21:31:03+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Psychological theories of depressive relapse and recurrence
- Framework: condition plus topic-defining process
- Scope confirmed by user: no (User requested standard depth, provided no known relevant articles, and explicitly asked not to pause for questions. Assumptions: include both conceptual/theoretical papers and empirical tests of psychological explanations; target unipolar depressive disorders, while screening mixed samples for relevance. No language, date, age, or study-design limits. PSB_AS_OF is set to 2018-11-17 for every command; no publication-date limit is applied. Scope proceeded without user confirmation per request. After the initial depression plus relapse strategy remained above the default screening budget, psychological explanatory content was reconsidered as a potentially searchable topic-defining concept and will be tested as an optional block.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Depressive disorders | search | Depression is the condition of interest. Relevant records may name particular depressive diagnoses rather than the broad category, so this is treated as a category and probed. |
| Depressive relapse or recurrence | optional | This process defines the topic, but papers may describe vulnerability, residual symptoms, or subsequent episodes without consistently using relapse/recurrence labels; test it before deciding whether to AND it. |
| Psychological theories or explanatory models | optional | Psychological explanatory content is central to eligibility and has recognizable MeSH and title/abstract vocabulary, but labels are inconsistent, so test this block for workload reduction and screened losses rather than requiring it a priori. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T21:29:52+00:00
- Records added to PubMed up to: 2018-11-17
- Total records: 14,947
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Depressive Disorder[Mesh]` | 105,341 | none |
| 2 | `Depression[Mesh]` | 206,675 | none |
| 3 | `depress*[tiab]` | 419,763 | none |
| 4 | `dysthymi*[tiab]` | 3,055 | none |
| 5 | `melanchol*[tiab]` | 2,939 | none |
| 6 | `unipolar[tiab]` | 10,360 | none |
| 7 | `affective disorder*[tiab]` | 15,894 | none |
| 8 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7` | 472,182 | none |
| 9 | `Recurrence[Mesh]` | 178,366 | none |
| 10 | `relapse[tiab]` | 108,955 | none |
| 11 | `relaps*[tiab]` | 163,847 | none |
| 12 | `recurren*[tiab]` | 496,927 | none |
| 13 | `recrudescen*[tiab]` | 3,173 | none |
| 14 | `recurrent depression[tiab]` | 935 | none |
| 15 | `depressive relapse[tiab]` | 278 | none |
| 16 | `relapse prevention[tiab]` | 2,854 | none |
| 17 | `vulnerab*[tiab]` | 113,966 | none |
| 18 | `susceptib*[tiab]` | 382,817 | none |
| 19 | `(subsequent[tiab] AND depress*[tiab] AND episode*[tiab])` | 883 | none |
| 20 | `(future[tiab] AND depress*[tiab])` | 19,687 | none |
| 21 | `(return*[tiab] AND depress*[tiab])` | 7,933 | none |
| 22 | `#9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21` | 1,208,238 | none |
| 23 | `Psychological Theory[Mesh]` | 92,101 | none |
| 24 | `Models, Psychological[Mesh]` | 44,629 | none |
| 25 | `psychological theor*[tiab]` | 1,408 | none |
| 26 | `psychological model*[tiab]` | 666 | none |
| 27 | `theoretical model*[tiab]` | 21,329 | none |
| 28 | `cognitive theor*[tiab]` | 2,807 | none |
| 29 | `cognitive model*[tiab]` | 2,289 | none |
| 30 | `cognitive vulnerab*[tiab]` | 510 | none |
| 31 | `cognitive reactiv*[tiab]` | 87 | none |
| 32 | `rumination[tiab]` | 3,368 | none |
| 33 | `attributional[tiab]` | 1,334 | none |
| 34 | `hopelessness[tiab]` | 3,729 | none |
| 35 | `learned helplessness[tiab]` | 1,241 | none |
| 36 | `psychodynamic[tiab]` | 5,071 | none |
| 37 | `interpersonal theor*[tiab]` | 337 | none |
| 38 | `behavioral model*[tiab]` | 2,304 | none |
| 39 | `behavioural model*[tiab]` | 662 | none |
| 40 | `vulnerability-stress[tiab]` | 172 | none |
| 41 | `self-esteem[tiab]` | 18,715 | none |
| 42 | `self-blam*[tiab]` | 1,062 | none |
| 43 | `experiential avoidance[tiab]` | 452 | none |
| 44 | `worr*[tiab]` | 19,817 | none |
| 45 | `dysfunctional attitude*[tiab]` | 518 | none |
| 46 | `schema*[tiab]` | 12,428 | none |
| 47 | `stress generation[tiab]` | 529 | none |
| 48 | `cognitive therap*[tiab]` | 3,076 | none |
| 49 | `cognitive behavio* therap*[tiab]` | 14,693 | none |
| 50 | `behavioral therap*[tiab]` | 10,229 | none |
| 51 | `behavioural therap*[tiab]` | 4,164 | none |
| 52 | `interpersonal therap*[tiab]` | 341 | none |
| 53 | `behavioral activation[tiab]` | 1,263 | none |
| 54 | `time perspective[tiab]` | 622 | none |
| 55 | `future perspective[tiab]` | 1,200 | none |
| 56 | `loss event*[tiab]` | 447 | none |
| 57 | `social support[tiab]` | 33,870 | none |
| 58 | `life change event*[tiab]` | 142 | none |
| 59 | `problem solving[tiab]` | 16,603 | none |
| 60 | `reminiscen*[tiab]` | 15,682 | none |
| 61 | `psychological mechanism*[tiab]` | 1,240 | none |
| 62 | `cognitive mechanism*[tiab]` | 1,834 | none |
| 63 | `explanatory model*[tiab]` | 2,007 | none |
| 64 | `psychological explanat*[tiab]` | 189 | none |
| 65 | `theoretical explanat*[tiab]` | 1,210 | none |
| 66 | `theor*[tiab]` | 584,988 | none |
| 67 | `mechanism*[tiab]` | 1,975,606 | none |
| 68 | `#23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59 OR #60 OR #61 OR #62 OR #63 OR #64 OR #65 OR #66 OR #67` | 2,717,041 | none |
| 69 | `#8 AND #22 AND #68` | 14,947 | none |

### Strategy (single line, for copying into PubMed)

```text
((Depressive Disorder[Mesh] OR Depression[Mesh] OR depress*[tiab] OR dysthymi*[tiab] OR melanchol*[tiab] OR unipolar[tiab] OR affective disorder*[tiab]) AND (Recurrence[Mesh] OR relapse[tiab] OR relaps*[tiab] OR recurren*[tiab] OR recrudescen*[tiab] OR recurrent depression[tiab] OR depressive relapse[tiab] OR relapse prevention[tiab] OR vulnerab*[tiab] OR susceptib*[tiab] OR (subsequent[tiab] AND depress*[tiab] AND episode*[tiab]) OR (future[tiab] AND depress*[tiab]) OR (return*[tiab] AND depress*[tiab])) AND (Psychological Theory[Mesh] OR Models, Psychological[Mesh] OR psychological theor*[tiab] OR psychological model*[tiab] OR theoretical model*[tiab] OR cognitive theor*[tiab] OR cognitive model*[tiab] OR cognitive vulnerab*[tiab] OR cognitive reactiv*[tiab] OR rumination[tiab] OR attributional[tiab] OR hopelessness[tiab] OR learned helplessness[tiab] OR psychodynamic[tiab] OR interpersonal theor*[tiab] OR behavioral model*[tiab] OR behavioural model*[tiab] OR vulnerability-stress[tiab] OR self-esteem[tiab] OR self-blam*[tiab] OR experiential avoidance[tiab] OR worr*[tiab] OR dysfunctional attitude*[tiab] OR schema*[tiab] OR stress generation[tiab] OR cognitive therap*[tiab] OR cognitive behavio* therap*[tiab] OR behavioral therap*[tiab] OR behavioural therap*[tiab] OR interpersonal therap*[tiab] OR behavioral activation[tiab] OR time perspective[tiab] OR future perspective[tiab] OR loss event*[tiab] OR social support[tiab] OR life change event*[tiab] OR problem solving[tiab] OR reminiscen*[tiab] OR psychological mechanism*[tiab] OR cognitive mechanism*[tiab] OR explanatory model*[tiab] OR psychological explanat*[tiab] OR theoretical explanat*[tiab] OR theor*[tiab] OR mechanism*[tiab])) AND ("1800/01/01"[edat] : "2018/11/17"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 5 | 5 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Depressive relapse or recurrence | AND-ed | 90,923 / 14,947 | 83.6% | none | 0/30 (up to 10% of removed records could be relevant) | The refreshed 30-record loss sample for the current query was screened against the assumed eligibility criteria. No clearly eligible psychological account of depressive relapse or recurrence was found; the items checked by abstract addressed first-onset/pregnancy depression, general treatment or cognition, non-depressive mechanisms, or relapse in other conditions. Retain this topic-defining block. Current query count is 14,947; the added unqualified theory/mechanism terms raise workload above the default 10,000, but are retained for sensitivity and all searchable optional concepts have been tested. |
| Psychological theories or explanatory models | AND-ed | 58,422 / 14,947 | 74.4% | none | 0/30 (up to 10% of removed records could be relevant) | The refreshed 30-record loss sample for the current query was screened against the assumed eligibility criteria. No clearly eligible record combined depressive relapse/recurrence with a psychological theory or mechanism; potentially related titles were checked by abstract and concerned bipolar disorder, short-term course without a psychological explanation, first-onset risk, treatment need or general depression mechanisms. Retain the concept-defining block. Current query count is 14,947, above the default 10,000 workload budget; broad theory/mechanism words are retained for sensitivity, and the other searchable optional concept has also been tested. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Depressive disorders | 1 | `Major Depressive Disorder[Mesh] OR Dysthymic Disorder[Mesh] OR Seasonal Affective Disorder[Mesh] OR Depression, Postpartum[Mesh] OR depress*[tiab]` | 0 | 0/0 |
| Depressive disorders | 2 | `Major Depressive Disorder[Mesh] OR Dysthymic Disorder[Mesh] OR Seasonal Affective Disorder[Mesh] OR Depression, Postpartum[Mesh] OR depress*[tiab]` | 0 | 0/0 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| depressive_disorders | 134,260 | 0 |
| relapse_recurrence | 90,923 | 0 |
| psychological_theory | 58,422 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 472,182 | initial | none | Initial condition block and optional relapse/recurrence block; no known records supplied; no filters or publication-date limit. |
| 2 | 17,650 | relapse_recurrence: +8 / -0 | none | Added an optional psychological theory/model block after the depression plus relapse query exceeded the standard workload budget; this tests a central and partly searchable eligibility concept. |
| 3 | 17,650 | limits/combination | none | Added an optional psychological theory/model block after the depression plus relapse query exceeded the standard workload budget; this tests a central and partly searchable eligibility concept. |
| 4 | 666 | psychological_theory: +18 / -0 | none | AND-ed the optional psychological theory/model block after the 30-record loss sample contained no clearly eligible record and the measured reduction brought the query below the standard workload budget; documented one borderline cognitive vulnerability record as a scope risk. |
| 5 | 974 | psychological_theory: +7 / -0 | none | Expanded the psychological model block with construct vocabulary relevant to screened development records and established cognitive models (self-esteem, self-blame, experiential avoidance, worry, dysfunctional attitudes, schemas, stress generation); these terms are OR-ed within the block to improve coverage. |
| 6 | 1,964 | psychological_theory: +13 / -0 | none | Broadened the psychological explanation block with cognitive and behavioral therapy labels and psychological time-perspective/social-process vocabulary after screened relevant records showed these forms of explanation may be named without theory/model wording. |
| 7 | 20,851 | relapse_recurrence: +6 / -0; psychological_theory: +3 / -0 | none | Addressed critic findings by adding standalone title/abstract language for depressive return and vulnerability/subsequent episodes, and broader model, mechanism, and explanation terms. This intentionally widens both required blocks; re-evaluate their counts, known-record retrieval, and optional loss samples. |
| 8 | 8,010 | relapse_recurrence: +3 / -3; psychological_theory: +5 / -3 | none | Applied critic lexical recommendations in controlled phrases for depressive return and vulnerability to subsequent depressive episodes, and psychological/cognitive mechanisms and explanatory models. Broad standalone wildcard terms returned 20,851 records and exceeded the standard screening budget, so retained the specific wording that expresses those concepts. |
| 9 | 7,988 | relapse_recurrence: +1 / -2 | none | Replaced two wildcard phrase strings that PubMed translated through All Fields with a field-tagged conjunction of return and depression. This preserves the critic-requested return concept while avoiding phrase-translation fallback; refreshed optional decisions remain current. |
| 10 | 14,947 | psychological_theory: +2 / -0 | none | Addressed critic finding P1-01 by adding standalone title/abstract truncations for theory and mechanism. Re-evaluate query size, known-record recall, and optional block losses; previous decisions are expected to stale after these lexical edits. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 9: 3 findings; P1-01 must-fix open, P1-02 should-fix open, P1-03 should-fix open
- Round 2 on version 10: 3 findings; P1-01 must-fix resolved, P1-02 should-fix resolved, P1-03 should-fix accepted-risk
- Round 3 on version 10: 3 findings; P1-01 must-fix resolved, P1-02 should-fix resolved, P1-03 should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 2551 NCBI requests logged (1247 from cache); strategy sha256 051b0911c135._

## Validation evidence and dispositions

```json
{
  "validation": {
    "policy_version": "1",
    "complete": true,
    "blockers": [],
    "review_required": [
      {
        "code": "over_workload_budget",
        "message": "14,947 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:depressive_disorders",
        "blocking": false,
        "requires_review": true,
        "id": "I-3234fbc22e09cdde98d4"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "14,947 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:depressive_disorders",
        "blocking": false,
        "requires_review": true,
        "id": "I-3234fbc22e09cdde98d4"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Depressive Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:29:52+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003866",
          "name": "Depressive Disorder",
          "type": "descriptor",
          "scope_note": "An affective disorder manifested by either a dysphoric mood or loss of interest or pleasure in usual activities. The mood disturbance is prominent and relatively persistent.",
          "tree_numbers": [
            "F03.600.300"
          ],
          "entry_terms": 20,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003866",
      "preferred_label": "Depressive Disorder",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "Depressive Disorder",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Depression",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:29:52+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D003863",
          "name": "Depression",
          "type": "descriptor",
          "scope_note": "Depressive states usually of moderate intensity in contrast with MAJOR DEPRESSIVE DISORDER present in neurotic and psychotic disorders.",
          "tree_numbers": [
            "F01.145.126.350",
            "F01.470.282"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D003863",
      "preferred_label": "Depression",
      "type": "descriptor",
      "location": "vocabulary:2",
      "term": {
        "text": "Depression",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Recurrence",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:29:52+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D012008",
          "name": "Recurrence",
          "type": "descriptor",
          "scope_note": "The return of a sign, symptom, or disease after a remission.",
          "tree_numbers": [
            "C23.550.291.937"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D012008",
      "preferred_label": "Recurrence",
      "type": "descriptor",
      "location": "vocabulary:8",
      "term": {
        "text": "Recurrence",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychological Theory",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:29:52+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011582",
          "name": "Psychological Theory",
          "type": "descriptor",
          "scope_note": "Principles applied to the analysis and explanation of psychological or behavioral phenomena.",
          "tree_numbers": [
            "F02.739"
          ],
          "entry_terms": 13,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011582",
      "preferred_label": "Psychological Theory",
      "type": "descriptor",
      "location": "vocabulary:25",
      "term": {
        "text": "Psychological Theory",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Models, Psychological",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T21:29:52+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D008960",
          "name": "Models, Psychological",
          "type": "descriptor",
          "scope_note": "Theoretical representations that simulate psychological processes and/or social processes. These include the use of mathematical equations, computers, and other electronic equipment.",
          "tree_numbers": [
            "E05.599.695"
          ],
          "entry_terms": 11,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D008960",
      "preferred_label": "Models, Psychological",
      "type": "descriptor",
      "location": "vocabulary:26",
      "term": {
        "text": "Models, Psychological",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"depressive disorder\"[MeSH Terms] OR (\"depressive disorder\"[MeSH Terms] OR \"depression\"[MeSH Terms]) OR \"depress*\"[Title/Abstract] OR \"dysthymi*\"[Title/Abstract] OR \"melanchol*\"[Title/Abstract] OR \"unipolar\"[Title/Abstract] OR \"affective disorder*\"[Title/Abstract]) AND (\"recurrence\"[MeSH Terms] OR \"relapse\"[Title/Abstract] OR \"relaps*\"[Title/Abstract] OR \"recurren*\"[Title/Abstract] OR \"recrudescen*\"[Title/Abstract] OR \"recurrent depression\"[Title/Abstract] OR \"depressive relapse\"[Title/Abstract] OR \"relapse prevention\"[Title/Abstract] OR \"vulnerab*\"[Title/Abstract] OR \"susceptib*\"[Title/Abstract] OR (\"subsequent\"[Title/Abstract] AND \"depress*\"[Title/Abstract] AND \"episode*\"[Title/Abstract]) OR (\"future\"[Title/Abstract] AND \"depress*\"[Title/Abstract]) OR (\"return*\"[Title/Abstract] AND \"depress*\"[Title/Abstract])) AND (\"psychological theory\"[MeSH Terms] OR \"models, psychological\"[MeSH Terms] OR \"psychological theor*\"[Title/Abstract] OR \"psychological model*\"[Title/Abstract] OR \"theoretical model*\"[Title/Abstract] OR \"cognitive theor*\"[Title/Abstract] OR \"cognitive model*\"[Title/Abstract] OR \"cognitive vulnerab*\"[Title/Abstract] OR \"cognitive reactiv*\"[Title/Abstract] OR \"rumination\"[Title/Abstract] OR \"attributional\"[Title/Abstract] OR \"hopelessness\"[Title/Abstract] OR \"learned helplessness\"[Title/Abstract] OR \"psychodynamic\"[Title/Abstract] OR \"interpersonal theor*\"[Title/Abstract] OR \"behavioral model*\"[Title/Abstract] OR \"behavioural model*\"[Title/Abstract] OR \"vulnerability-stress\"[Title/Abstract] OR \"self-esteem\"[Title/Abstract] OR \"self blam*\"[Title/Abstract] OR \"experiential avoidance\"[Title/Abstract] OR \"worr*\"[Title/Abstract] OR \"dysfunctional attitude*\"[Title/Abstract] OR \"schema*\"[Title/Abstract] OR \"stress generation\"[Title/Abstract] OR \"cognitive therap*\"[Title/Abstract] OR \"cognitive behavio* therap*\"[Title/Abstract] OR \"behavioral therap*\"[Title/Abstract] OR \"behavioural therap*\"[Title/Abstract] OR \"interpersonal therap*\"[Title/Abstract] OR \"behavioral activation\"[Title/Abstract] OR \"time perspective\"[Title/Abstract] OR \"future perspective\"[Title/Abstract] OR \"loss event*\"[Title/Abstract] OR \"social support\"[Title/Abstract] OR \"life change event*\"[Title/Abstract] OR \"problem solving\"[Title/Abstract] OR \"reminiscen*\"[Title/Abstract] OR \"psychological mechanism*\"[Title/Abstract] OR \"cognitive mechanism*\"[Title/Abstract] OR \"explanatory model*\"[Title/Abstract] OR \"psychological explanat*\"[Title/Abstract] OR \"theoretical explanat*\"[Title/Abstract] OR \"theor*\"[Title/Abstract] OR \"mechanism*\"[Title/Abstract]) AND 1800/01/01:2018/11/17[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 9,
      "review_sha256": "59edb5d54b751d77d862ecb747c1cbb535f2aadc0cc6132cceb68baf0a7c5d63",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "The psychological explanatory concept is not fully translated: the eligibility names theory and mechanism, but the text words restrict these to parent-qualified phrases such as psychological theory and cognitive mechanism."
        },
        "operators": {
          "verdict": "pass",
          "note": "The Boolean structure joins the three concepts with AND and their alternatives with OR. The subsequent, future, and return clauses use AND to associate the terms."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes headings for depressive disorder, depression, recurrence, psychological theory, and psychological models."
        },
        "text_words": {
          "verdict": "revise",
          "note": "Add bare title/abstract coverage for theory and mechanism, as required by the packet's translation checks. The current psychological and cognitive qualified forms do not cover those names independently."
        },
        "syntax": {
          "verdict": "pass",
          "note": "No syntax errors or proximity operators are reported. The return clause is an explicit AND expression, so term order is unrestricted."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "Both optional AND-ed concept evaluations are marked stale, and the depressive-disorders category probe is stale with its probe budget spent. Refresh the affected evaluations before treating their evidence as current."
        }
      },
      "findings": [
        {
          "id": "P1-01",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility names psychological theory and mechanism as relevant concepts, but the strategy only searches qualified forms such as psychological theor*, cognitive theor*, psychological mechanism*, and cognitive mechanism*. It does not search theory or mechanism by their own bare names.",
          "recommendation": "Add explicit tested title/abstract expressions for theor* and mechanism* (or other independently searched forms that cover those names), then rerun the complete evaluation after the rewrite.",
          "status": "open"
        },
        {
          "id": "P1-02",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The relapse/recurrence and psychological-theory AND-ed optional-concept evaluations are both marked stale. Their loss samples and workload comparisons therefore do not validate the current strategy version.",
          "recommendation": "Rerun each optional-block evaluation against the current strategy, including a fresh loss sample and workload comparison, before retaining the AND-ed blocks as supported decisions.",
          "status": "open"
        },
        {
          "id": "P1-03",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The depressive-disorders category probe is flagged stale because the block changed after the last probe, and its two-probe budget is spent. The displayed 0/0 observations cannot establish coverage of the current block.",
          "recommendation": "Refresh the category probe when the budget permits, or explicitly document that current category coverage remains unverified.",
          "status": "open"
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-3234fbc22e09cdde98d4",
          "status": "accepted-risk",
          "response": "The warning is valid and current coverage remains unverified; accept it only as a documented limitation pending a refreshed probe.",
          "evidence": "The packet reports two probes with zero records outside the category block, but the issue explicitly marks the probe stale and says the probe budget is spent, so those observations do not verify the changed block."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 10,
      "review_sha256": "f8517e1328588c33d0314614f0ba5a5edc2896a6e6e4ce231bc3e0cdca4d648b",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The strategy covers the named condition, relapse or recurrence process, and psychological explanatory concepts. Standalone theor*[tiab] and mechanism*[tiab] satisfy the bare-name check. The return and subsequent-episode clauses associate terms with depression; screen for direction and relevance."
        },
        "operators": {
          "verdict": "pass",
          "note": "The concept blocks are combined with AND and their alternatives with OR. The multi-term process clauses use AND to connect their components."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes headings for depressive disorders, depression, recurrence, psychological theory, and psychological models."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Standalone theor*[tiab] and mechanism*[tiab] are present alongside qualified theory and mechanism terms, resolving P1-01."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported searches have no syntax diagnostics. No proximity operators or phrase warnings are reported."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Both optional-block decisions have refreshed 30-record loss samples for the current query. The category probe remains stale and its budget is spent; this is recorded as an accepted limitation. The 14,947-record count exceeds the 10,000 budget, with both searchable optional concepts tested."
        }
      },
      "findings": [
        {
          "id": "P1-01",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility names psychological theory and mechanism as relevant concepts, but the strategy previously searched only qualified forms.",
          "recommendation": "Add independently searched bare-name coverage for theory and mechanism, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current strategy includes theor*[tiab] and mechanism*[tiab], and the packet reports a fresh complete evaluation at version 10."
        },
        {
          "id": "P1-02",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The relapse/recurrence and psychological-theory optional-block evaluations were previously flagged stale.",
          "recommendation": "Refresh each evaluation against the current strategy, including a loss sample and workload comparison.",
          "status": "resolved",
          "response": "The current packet reports refreshed 30-record loss samples and current-query comparisons for both optional blocks."
        },
        {
          "id": "P1-03",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The depressive-disorders category probe remains stale after a block change, and its two-probe budget is spent; the displayed 0/0 observations do not verify coverage of the current block.",
          "recommendation": "Refresh the category probe when possible, or document that current category coverage remains unverified.",
          "status": "accepted-risk",
          "response": "The probe warning is accepted as a documented limitation: the probe is stale, the budget is spent, and current category coverage remains unverified."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload warning is accepted for this strategy because both searchable optional concepts have been tested and the packet documents why their broad sensitivity terms were retained.",
          "evidence": "The current query returns 14,947 records against a 10,000-record budget; both optional concepts have current loss samples and workload comparisons."
        },
        {
          "issue_id": "I-3234fbc22e09cdde98d4",
          "status": "accepted-risk",
          "response": "Accept the warning as a limitation; the current category block is not verified by the stale probe.",
          "evidence": "The packet reports two probes with zero records outside the category block, but marks the probe stale and the probe budget spent."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 10,
      "review_sha256": "f8517e1328588c33d0314614f0ba5a5edc2896a6e6e4ce231bc3e0cdca4d648b",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The condition, relapse or recurrence process, and psychological explanatory concepts are represented. Standalone theor*[tiab] and mechanism*[tiab] resolve the bare-name gap. The return and subsequent-episode clauses associate their terms with depression; screen for direction and relevance."
        },
        "operators": {
          "verdict": "pass",
          "note": "The concept blocks are joined with AND, alternatives with OR, and the multi-term process clauses with AND."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The strategy includes headings for depressive disorder, depression, recurrence, psychological theory, and psychological models."
        },
        "text_words": {
          "verdict": "pass",
          "note": "Standalone theor*[tiab] and mechanism*[tiab] are present alongside qualified forms."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported searches have no syntax diagnostics or phrase warnings. The multi-term clauses use explicit AND expressions; no proximity operators are used."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Both optional-block evaluations have current 30-record loss samples and workload comparisons. The category probe remains stale with its budget spent, and its limitation is documented. The 14,947-record count exceeds budget, but both searchable optional concepts were tested."
        }
      },
      "findings": [
        {
          "id": "P1-01",
          "domain": "text_words",
          "severity": "must-fix",
          "kind": "lexical",
          "finding": "Eligibility names psychological theory and mechanism as relevant concepts, but the earlier strategy searched only qualified forms.",
          "recommendation": "Add independently searched bare-name coverage for theory and mechanism, then rerun the complete evaluation.",
          "status": "resolved",
          "response": "The current strategy includes theor*[tiab] and mechanism*[tiab], and the packet reports a complete evaluation at version 10."
        },
        {
          "id": "P1-02",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "scope",
          "finding": "The relapse/recurrence and psychological-theory optional-block evaluations were previously stale.",
          "recommendation": "Refresh each evaluation against the current strategy, including a loss sample and workload comparison.",
          "status": "resolved",
          "response": "The packet reports refreshed 30-record loss samples and current-query comparisons for both optional blocks."
        },
        {
          "id": "P1-03",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The depressive-disorders category probe is stale after a block change, and its probe budget is spent; the displayed 0/0 observations do not verify coverage of the current block.",
          "recommendation": "Refresh the category probe when possible, or document that current category coverage remains unverified.",
          "status": "accepted-risk",
          "response": "Accept this as a documented limitation: the probe is stale, the budget is spent, and current category coverage remains unverified."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload warning is accepted because both searchable optional concepts were tested and the packet explains why broad theory and mechanism terms were retained for sensitivity.",
          "evidence": "The current query returns 14,947 records against a 10,000-record budget; both optional-block evaluations have current loss samples and workload comparisons."
        },
        {
          "issue_id": "I-3234fbc22e09cdde98d4",
          "status": "accepted-risk",
          "response": "Accept the category-probe warning as a limitation; current category coverage remains unverified.",
          "evidence": "The packet reports two probes with zero records outside the category block, but marks the probe stale and its budget spent."
        }
      ]
    }
  ]
}
```

