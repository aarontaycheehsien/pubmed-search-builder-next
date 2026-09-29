# PubMed search strategy: audit

Generated 2026-09-28T23:52:48+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Specialized psychotherapies for adults with borderline personality disorder
- Framework: PICO (intervention effectiveness; comparator and outcomes screened)
- Scope confirmed by user: yes (User asked to proceed without questions; assumptions: adults means 18 years or older; specialized psychotherapy means an identifiable psychotherapy or structured psychological treatment intended for BPD; outcomes and comparators are screened. No known relevant articles supplied. Do not use web search. PubMed entry-date cutoff is enforced by PSB_AS_OF=2015-03-27 for every command; no publication-date limit. A tested optional specialization filter was not retained after internal critique found it duplicated the broad psychotherapy MeSH layer, so it could not reliably enforce specialization. The BPD category probe history includes an initial malformed CLI argument and a later probe that became tautological after broadening; BPD category coverage remains uncertain.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Borderline personality disorder | search | The condition defines the review and is usually named or indexed; include historical and diagnostic synonyms and probe terminology that may name a member or alternate label. |
| Psychotherapies for borderline personality disorder | search | The intervention defines the topic; specialized modality names are varied, so search psychotherapy terminology and named modalities then probe the category. |
| Adults | screen | Age is inconsistently indexed and mixed-age studies may qualify; screen at eligibility. |
| Specialized or structured treatment | screen | Labels such as specialized, specific, structured, or manualized were tested as an optional block. The sample did not establish that those labels are sufficiently reliable to require; screen treatment structure and specialization from study reports. |
| Comparators and outcomes | screen | These are not required search concepts for an intervention question. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T23:51:55+00:00
- Records added to PubMed up to: 2015-03-27
- Total records: 13,713
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Borderline Personality Disorder[Mesh]` | 5,413 | none |
| 2 | `"borderline personality disorder"[tiab]` | 4,215 | none |
| 3 | `"borderline personality"[tiab]` | 4,863 | none |
| 4 | `borderline personality disorder*[tiab]` | 4,397 | none |
| 5 | `"emotionally unstable personality"[tiab]` | 30 | none |
| 6 | `"emotionally unstable personality disorder"[tiab]` | 24 | none |
| 7 | `EUPD[tiab]` | 4 | none |
| 8 | `BPD[tiab]` | 6,222 | none |
| 9 | `Personality Disorders[Mesh]` | 36,706 | none |
| 10 | `personality disorder*[tiab]` | 15,183 | none |
| 11 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8 OR #9 OR #10` | 45,771 | none |
| 12 | `Psychotherapy[Mesh]` | 165,482 | none |
| 13 | `Behavior Therapy[Mesh]` | 57,482 | none |
| 14 | `Psychoanalytic Therapy[Mesh]` | 15,004 | none |
| 15 | `Psychotherapy, Group[Mesh]` | 24,106 | none |
| 16 | `psychotherap*[tiab]` | 37,596 | none |
| 17 | `psychological therapy[tiab]` | 596 | none |
| 18 | `psychological therapies[tiab]` | 649 | none |
| 19 | `psychological treatment[tiab]` | 1,719 | none |
| 20 | `therapy[tiab]` | 1,438,128 | none |
| 21 | `therapies[tiab]` | 175,723 | none |
| 22 | `treatment[tiab]` | 3,150,610 | none |
| 23 | `"dialectical behavior therapy"[tiab]` | 278 | none |
| 24 | `"dialectical behaviour therapy"[tiab]` | 84 | none |
| 25 | `DBT[tiab]` | 1,420 | none |
| 26 | `"mentalization based treatment"[tiab]` | 40 | none |
| 27 | `"mentalization-based treatment"[tiab]` | 40 | none |
| 28 | `"mentalisation based treatment"[tiab]` | 8 | none |
| 29 | `"mentalisation-based treatment"[tiab]` | 8 | none |
| 30 | `MBT[tiab]` | 1,537 | none |
| 31 | `"transference focused psychotherapy"[tiab]` | 46 | none |
| 32 | `"transference-focused psychotherapy"[tiab]` | 46 | none |
| 33 | `"schema therapy"[tiab]` | 76 | none |
| 34 | `"schema-focused therapy"[tiab]` | 32 | none |
| 35 | `"schema focused therapy"[tiab]` | 32 | none |
| 36 | `STEPPS[tiab]` | 30 | none |
| 37 | `"systems training for emotional predictability and problem solving"[tiab]` | 16 | none |
| 38 | `"dynamic deconstructive psychotherapy"[tiab]` | 13 | none |
| 39 | `"cognitive analytic therapy"[tiab]` | 56 | none |
| 40 | `"cognitive behavioural therapy"[tiab]` | 2,146 | none |
| 41 | `"cognitive behavioral therapy"[tiab]` | 4,838 | none |
| 42 | `"cognitive therapy"[tiab]` | 2,057 | none |
| 43 | `"general psychiatric management"[tiab]` | 14 | none |
| 44 | `"structured clinical management"[tiab]` | 4 | none |
| 45 | `"good clinical care"[tiab]` | 83 | none |
| 46 | `psychoeducation[tiab]` | 1,808 | none |
| 47 | `"emotion regulation group therapy"[tiab]` | 7 | none |
| 48 | `"manual assisted cognitive treatment"[tiab]` | 3 | none |
| 49 | `MACT[tiab]` | 272 | none |
| 50 | `#12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49` | 4,114,885 | none |
| 51 | `#11 AND #50` | 13,713 | none |

### Strategy (single line, for copying into PubMed)

```text
((Borderline Personality Disorder[Mesh] OR "borderline personality disorder"[tiab] OR "borderline personality"[tiab] OR borderline personality disorder*[tiab] OR "emotionally unstable personality"[tiab] OR "emotionally unstable personality disorder"[tiab] OR EUPD[tiab] OR BPD[tiab] OR Personality Disorders[Mesh] OR personality disorder*[tiab]) AND (Psychotherapy[Mesh] OR Behavior Therapy[Mesh] OR Psychoanalytic Therapy[Mesh] OR Psychotherapy, Group[Mesh] OR psychotherap*[tiab] OR psychological therapy[tiab] OR psychological therapies[tiab] OR psychological treatment[tiab] OR therapy[tiab] OR therapies[tiab] OR treatment[tiab] OR "dialectical behavior therapy"[tiab] OR "dialectical behaviour therapy"[tiab] OR DBT[tiab] OR "mentalization based treatment"[tiab] OR "mentalization-based treatment"[tiab] OR "mentalisation based treatment"[tiab] OR "mentalisation-based treatment"[tiab] OR MBT[tiab] OR "transference focused psychotherapy"[tiab] OR "transference-focused psychotherapy"[tiab] OR "schema therapy"[tiab] OR "schema-focused therapy"[tiab] OR "schema focused therapy"[tiab] OR STEPPS[tiab] OR "systems training for emotional predictability and problem solving"[tiab] OR "dynamic deconstructive psychotherapy"[tiab] OR "cognitive analytic therapy"[tiab] OR "cognitive behavioural therapy"[tiab] OR "cognitive behavioral therapy"[tiab] OR "cognitive therapy"[tiab] OR "general psychiatric management"[tiab] OR "structured clinical management"[tiab] OR "good clinical care"[tiab] OR psychoeducation[tiab] OR "emotion regulation group therapy"[tiab] OR "manual assisted cognitive treatment"[tiab] OR MACT[tiab])) AND ("1800/01/01"[edat] : "2015/03/27"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 15 | 15 | 100.0% |
| validation | validation (relevant records held out from term mining; semi-independent) | 6 | 6 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Borderline personality disorder | 1 | `Personality Disorders[Mesh] OR " personality disorder*\[tiab] --n 30 --seed 71` | 2,232 | 2/30 |
| Borderline personality disorder | 2 | `Personality Disorders[Mesh] OR "personality disorder*"[tiab]` | 0 | 0/0 |
| Psychotherapies for borderline personality disorder | 1 | `Borderline Personality Disorder[Mesh] AND (intervention*[tiab] OR program*[tiab] OR management[tiab] OR care[tiab] OR psychosocial[tiab])` | 334 | 0/30 |
| Psychotherapies for borderline personality disorder | 2 | `Borderline Personality Disorder[Mesh] AND (intervention*[tiab] OR program*[tiab] OR management[tiab] OR care[tiab] OR psychosocial[tiab])` | 95 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| bpd | 4,114,885 | 0 |
| psychotherapy | 45,771 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 4,408 | initial | none | Initial two-block recall-first strategy; broad BPD and psychotherapy/modality terms informed by scope, MeSH and development set term ranking; adult/specialization screened |
| 2 | 13,713 | bpd: +2 / -0 | none | Widened BPD category with Personality Disorders MeSH and generic personality-disorder wording after probe 1 found two eligible cited records outside the original block; inspect probe-frame discrepancy |
| 3 | 13,713 | limits/combination | none | Added optional specialization block to test whether structured/manualized/specific labels can lower the workload; no population age limit added |
| 4 | 13,713 | limits/combination | none | Refined optional specialization test to include available broad MeSH therapy headings plus structured/manualized/specialized wording; no post-cutoff MeSH headings used |
| 5 | 8,006 | specialization: +12 / -0 | none | AND-ed optional specialization block after material reduction, no known-record loss, and 0 relevant of 30 loss-sample records |
| 6 | 13,713 | psychotherapy: +0 / -1; specialization: +0 / -12 | none | Reconsidered specialization as a screening criterion after critic found duplicate MeSH headings in its optional block; removed that block to preserve recall, and removed proximity clause because exact transference-focused phrases remain. Workload now exceeds standard default budget; record for critic disposition. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5: 4 findings; P1-01 should-fix open, P1-02 should-fix open, P1-03 document accepted-risk, I-c63926f9f0a4c7c3fa67 should-fix accepted-risk
- Round 2 on version 6: 6 findings; P1-01 should-fix resolved, P1-02 should-fix resolved, P1-03 document resolved, I-c63926f9f0a4c7c3fa67 should-fix accepted-risk, I-3b47b207ba8f2c0ae264 should-fix accepted-risk, I-a2ea70e99d0502ed4b2e should-fix accepted-risk
- Round 3 on version 6: 6 findings; P1-01 should-fix resolved, P1-02 should-fix resolved, P1-03 document resolved, I-c63926f9f0a4c7c3fa67 should-fix accepted-risk, I-3b47b207ba8f2c0ae264 should-fix accepted-risk, I-a2ea70e99d0502ed4b2e should-fix accepted-risk

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 929 NCBI requests logged (540 from cache); strategy sha256 c7b13419cec3._

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
        "message": "13,713 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:bpd",
        "blocking": false,
        "requires_review": true,
        "id": "I-c63926f9f0a4c7c3fa67"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:psychotherapy",
        "blocking": false,
        "requires_review": true,
        "id": "I-3b47b207ba8f2c0ae264"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "13,713 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
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
        "location": "concept:bpd",
        "blocking": false,
        "requires_review": true,
        "id": "I-c63926f9f0a4c7c3fa67"
      },
      {
        "code": "category_probe_stale_budget_spent",
        "message": "The block changed after the last probe and the probe budget is spent",
        "severity": "warning",
        "location": "concept:psychotherapy",
        "blocking": false,
        "requires_review": true,
        "id": "I-3b47b207ba8f2c0ae264"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Borderline Personality Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:51:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001883",
          "name": "Borderline Personality Disorder",
          "type": "descriptor",
          "scope_note": "A personality disorder marked by a pattern of instability of interpersonal relationships, self-image, and affects, and marked impulsivity beginning by early adulthood and present in a variety of contexts. (DSM-IV)",
          "tree_numbers": [
            "F03.675.100"
          ],
          "entry_terms": 5,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001883",
      "preferred_label": "Borderline Personality Disorder",
      "type": "descriptor",
      "location": "vocabulary:1",
      "term": {
        "text": "Borderline Personality Disorder",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Personality Disorders",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:51:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D010554",
          "name": "Personality Disorders",
          "type": "descriptor",
          "scope_note": "A major deviation from normal patterns of behavior.",
          "tree_numbers": [
            "F03.675"
          ],
          "entry_terms": 10,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D010554",
      "preferred_label": "Personality Disorders",
      "type": "descriptor",
      "location": "vocabulary:9",
      "term": {
        "text": "Personality Disorders",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychotherapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:51:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011613",
          "name": "Psychotherapy",
          "type": "descriptor",
          "scope_note": "A generic term for the treatment of mental illness or emotional disturbances primarily by verbal or nonverbal communication.",
          "tree_numbers": [
            "F04.754"
          ],
          "entry_terms": 1,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011613",
      "preferred_label": "Psychotherapy",
      "type": "descriptor",
      "location": "vocabulary:11",
      "term": {
        "text": "Psychotherapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Behavior Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:51:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D001521",
          "name": "Behavior Therapy",
          "type": "descriptor",
          "scope_note": "The application of modern theories of learning and conditioning in the treatment of behavior disorders.",
          "tree_numbers": [
            "F04.754.137"
          ],
          "entry_terms": 30,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D001521",
      "preferred_label": "Behavior Therapy",
      "type": "descriptor",
      "location": "vocabulary:12",
      "term": {
        "text": "Behavior Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychoanalytic Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:51:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011575",
          "name": "Psychoanalytic Therapy",
          "type": "descriptor",
          "scope_note": "A form of psychiatric treatment, based on Freudian principles, which seeks to eliminate or diminish the undesirable effects of unconscious conflicts by making the patient aware of their existence, origin, and inappropriate expression in current emotions and behavior.",
          "tree_numbers": [
            "F04.754.709"
          ],
          "entry_terms": 10,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011575",
      "preferred_label": "Psychoanalytic Therapy",
      "type": "descriptor",
      "location": "vocabulary:13",
      "term": {
        "text": "Psychoanalytic Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychotherapy, Group",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:51:55+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D011615",
          "name": "Psychotherapy, Group",
          "type": "descriptor",
          "scope_note": "A form of therapy in which two or more patients participate under the guidance of one or more psychotherapists for the purpose of treating emotional disturbances, social maladjustments, and psychotic states.",
          "tree_numbers": [
            "F04.754.864.581"
          ],
          "entry_terms": 18,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D011615",
      "preferred_label": "Psychotherapy, Group",
      "type": "descriptor",
      "location": "vocabulary:14",
      "term": {
        "text": "Psychotherapy, Group",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"borderline personality disorder\"[MeSH Terms] OR \"borderline personality disorder\"[Title/Abstract] OR \"borderline personality\"[Title/Abstract] OR \"borderline personality disorder*\"[Title/Abstract] OR \"emotionally unstable personality\"[Title/Abstract] OR \"emotionally unstable personality disorder\"[Title/Abstract] OR \"EUPD\"[Title/Abstract] OR \"BPD\"[Title/Abstract] OR \"personality disorders\"[MeSH Terms] OR \"personality disorder*\"[Title/Abstract]) AND (\"psychotherapy\"[MeSH Terms] OR \"behavior therapy\"[MeSH Terms] OR \"psychoanalytic therapy\"[MeSH Terms] OR \"psychotherapy, group\"[MeSH Terms] OR \"psychotherap*\"[Title/Abstract] OR \"psychological therapy\"[Title/Abstract] OR \"psychological therapies\"[Title/Abstract] OR \"psychological treatment\"[Title/Abstract] OR \"therapy\"[Title/Abstract] OR \"therapies\"[Title/Abstract] OR \"treatment\"[Title/Abstract] OR \"dialectical behavior therapy\"[Title/Abstract] OR \"dialectical behaviour therapy\"[Title/Abstract] OR \"DBT\"[Title/Abstract] OR \"mentalization-based treatment\"[Title/Abstract] OR \"mentalization-based treatment\"[Title/Abstract] OR \"mentalisation-based treatment\"[Title/Abstract] OR \"mentalisation-based treatment\"[Title/Abstract] OR \"MBT\"[Title/Abstract] OR \"transference-focused psychotherapy\"[Title/Abstract] OR \"transference-focused psychotherapy\"[Title/Abstract] OR \"schema therapy\"[Title/Abstract] OR \"schema-focused therapy\"[Title/Abstract] OR \"schema-focused therapy\"[Title/Abstract] OR \"STEPPS\"[Title/Abstract] OR \"systems training for emotional predictability and problem solving\"[Title/Abstract] OR \"dynamic deconstructive psychotherapy\"[Title/Abstract] OR \"cognitive analytic therapy\"[Title/Abstract] OR \"cognitive behavioural therapy\"[Title/Abstract] OR \"cognitive behavioral therapy\"[Title/Abstract] OR \"cognitive therapy\"[Title/Abstract] OR \"general psychiatric management\"[Title/Abstract] OR \"structured clinical management\"[Title/Abstract] OR \"good clinical care\"[Title/Abstract] OR \"psychoeducation\"[Title/Abstract] OR \"emotion regulation group therapy\"[Title/Abstract] OR \"manual assisted cognitive treatment\"[Title/Abstract] OR \"MACT\"[Title/Abstract]) AND 1800/01/01:2015/03/27[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "e5bbb52b0c03dec2d1834980d3e3ae5b80b91dcbb78cffb1bf14e1a007d8b31c",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The condition terms include diagnostic and historical labels, and the intervention block includes general psychotherapy terms and named modalities. No named member in the scope or eligibility is represented only by a phrase narrowed with its parent concept."
        },
        "operators": {
          "verdict": "revise",
          "note": "The optional specialization block duplicates psychotherapy MeSH terms from the intervention block, so those headings can satisfy both AND-ed blocks without a specialization term."
        },
        "subject_headings": {
          "verdict": "revise",
          "note": "Psychotherapy, Behavior Therapy, and Psychoanalytic Therapy appear in both the intervention and specialization blocks, weakening the intended specialization constraint."
        },
        "text_words": {
          "verdict": "revise",
          "note": "The proximity expression for transference-focused treatment has no clause-specific interpretation documented. The optional specialization block also carries an acknowledged but incompletely assessed recall risk."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query has balanced Boolean structure, no reported PubMed errors or warnings, and an explicit entry-date range."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "The entry-date cutoff is explicit and consistent with the packet; age is appropriately left for screening."
        }
      },
      "findings": [
        {
          "id": "P1-01",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "The specialization block repeats Psychotherapy[Mesh], Behavior Therapy[Mesh], and Psychoanalytic Therapy[Mesh] from the intervention block. Any one of these headings can satisfy both blocks, so the AND does not ensure that retrieved records carry a specialization or structure indicator.",
          "recommendation": "Remove the duplicated headings from the specialization block or reconsider the block's role, then rerun the complete evaluation and workload assessment.",
          "status": "open"
        },
        {
          "id": "P1-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "\"transference focused\"[tiab:~2] has no clause-specific interpretation review or rationale in the packet. Exact expressions for both hyphenated and unhyphenated transference-focused psychotherapy are already present.",
          "recommendation": "Document the intended interpretation and evidence for the proximity clause, or remove it after assessing its contribution; rerun the complete evaluation after any rewrite or removal.",
          "status": "open"
        },
        {
          "id": "P1-03",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "filter",
          "finding": "The optional specialization block excludes 5,707 of 13,713 otherwise retrieved records. No known relevant records were lost and the 30-record loss sample found none, but that sample leaves residual recall risk, as the packet acknowledges.",
          "recommendation": "Retain the workload rationale and residual recall risk in the audit record; treat the current sample as limited evidence rather than proof that the excluded records are ineligible.",
          "status": "accepted-risk",
          "response": "Accepted for this review because the stated workload budget is 10,000 and the block reduces the set to 8,006; the 30-record sample and 21 known retrieved records provide limited, not conclusive, reassurance."
        },
        {
          "id": "I-c63926f9f0a4c7c3fa67",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The BPD category probe is marked stale because the block changed after its last probe and the probe budget is spent. The current category block therefore lacks a fresh probe validation.",
          "recommendation": "Refresh the category probe if possible; otherwise report the validation as stale and retain the associated uncertainty.",
          "status": "accepted-risk",
          "response": "Accepted with explicit residual uncertainty: the first probe found two relevant records among 30 outside the narrower BPD terms, while the second probe found zero outside records. The packet reports the probe as stale, so these observations do not establish fresh validation of the current block."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-c63926f9f0a4c7c3fa67",
          "status": "accepted-risk",
          "response": "The current BPD category block remains unverified by a fresh probe because the probe budget is spent; retain the stale status and its uncertainty in reporting.",
          "evidence": "Probe 1 found 2 relevant records among 30 outside the narrower BPD terms; probe 2 found 0 outside records. The packet marks the category as stale after a block change."
        }
      ]
    },
    {
      "round": 2,
      "strategy_version": 6,
      "review_sha256": "50966c61f6771d543f7ce6b4cc8d7bb9dcc77f6a183b7d39c8d821f94277ea55",
      "domains": {
        "translation": {
          "verdict": "revise",
          "note": "Condition and intervention terms cover the concepts named in scope, including historical labels and named modalities. The category probes are stale after changes to both blocks, so they do not freshly validate the current translation."
        },
        "operators": {
          "verdict": "pass",
          "note": "The final strategy combines the condition and psychotherapy blocks with AND. Removing the specialization block resolves the prior duplicate-heading problem."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The condition and psychotherapy blocks include relevant MeSH headings. No duplicate specialization block remains to let the same heading satisfy both sides of an AND."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The final query no longer contains the unreviewed transference proximity clause. The phrase-specific warning therefore does not apply to this version."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The final query has balanced Boolean structure, no reported PubMed errors or warnings, and an explicit entry-date range."
        },
        "limits_filters": {
          "verdict": "revise",
          "note": "The age limit is appropriately left for screening, and the entry-date cutoff is explicit. The final result count exceeds the stated workload budget; that tradeoff needs an explicit disposition."
        }
      },
      "findings": [
        {
          "id": "P1-01",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "The prior specialization block repeated Psychotherapy[Mesh], Behavior Therapy[Mesh], and Psychoanalytic Therapy[Mesh] from the intervention block, allowing those headings to satisfy both blocks.",
          "recommendation": "Remove the duplicated headings from the specialization block or reconsider the block's role, then rerun the complete evaluation and workload assessment.",
          "status": "resolved",
          "response": "The specialization block was removed in version 6, so the final strategy no longer uses those duplicated headings in an AND-ed block."
        },
        {
          "id": "P1-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The prior proximity clause for transference-focused treatment had no clause-specific interpretation review or rationale in the packet.",
          "recommendation": "Document the intended interpretation and evidence for the proximity clause, or remove it after assessing its contribution; rerun the complete evaluation after any rewrite or removal.",
          "status": "resolved",
          "response": "The proximity clause was removed in version 6. The final strategy retains exact hyphenated and unhyphenated psychotherapy expressions."
        },
        {
          "id": "P1-03",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "filter",
          "finding": "The prior optional specialization block excluded 5,707 of 13,713 otherwise retrieved records. Its 30-record loss sample provided limited reassurance, not proof that excluded records were ineligible.",
          "recommendation": "Retain the workload rationale and residual recall risk in the audit record; treat the sample as limited evidence.",
          "status": "resolved",
          "response": "The specialization block was removed in version 6, so that exclusion no longer applies to the final query. The final query instead exceeds the workload budget."
        },
        {
          "id": "I-c63926f9f0a4c7c3fa67",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The BPD category probe is marked stale because the block changed after its last probe and the probe budget is spent. The current category block lacks fresh probe validation.",
          "recommendation": "Refresh the category probe if possible; otherwise report the stale validation and retain the associated uncertainty.",
          "status": "accepted-risk",
          "response": "The probe budget is spent, so fresh validation is unavailable. The stale status and uncertainty are retained in the audit record."
        },
        {
          "id": "I-3b47b207ba8f2c0ae264",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The psychotherapy category probe is marked stale because the block changed after its last probe and the probe budget is spent. The current category block lacks fresh probe validation.",
          "recommendation": "Refresh the category probe if possible; otherwise report the stale validation and retain the associated uncertainty.",
          "status": "accepted-risk",
          "response": "The probe budget is spent, so fresh validation is unavailable. The stale status and uncertainty are retained in the audit record."
        },
        {
          "id": "I-a2ea70e99d0502ed4b2e",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The final query retrieves 13,713 records, exceeding the stated workload budget of 10,000.",
          "recommendation": "Document the workload tradeoff and the decision to screen specialization rather than require a specialization block, consistent with the protocol and the limited probe evidence.",
          "status": "accepted-risk",
          "response": "The protocol assigns specialization to screening because the sample did not establish that specialization labels are reliable enough to require. The optional block was considered and removed; the remaining workload above budget is accepted to preserve that search scope."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The workload exceeds budget, but the protocol makes specialization a screening criterion because the sample did not establish a reliable searchable block. The optional block was considered and removed.",
          "evidence": "The final query returns 13,713 records against a 10,000-record budget. The earlier block excluded 5,707 records; its 30-record sample found no relevant records, which is limited evidence and not proof of ineligibility."
        },
        {
          "issue_id": "I-c63926f9f0a4c7c3fa67",
          "status": "accepted-risk",
          "response": "Fresh BPD category-probe validation is unavailable because the probe budget is spent; retain the stale status and uncertainty.",
          "evidence": "Probe 1 found 2 relevant records among 30 outside the narrower BPD terms, while probe 2 found 0 outside records. The packet marks the category probe stale after a block change."
        },
        {
          "issue_id": "I-3b47b207ba8f2c0ae264",
          "status": "accepted-risk",
          "response": "Fresh psychotherapy category-probe validation is unavailable because the probe budget is spent; retain the stale status and uncertainty.",
          "evidence": "The packet reports two psychotherapy category probes, each screening 30 records outside the block and finding zero relevant records, but marks the current category probe stale after a block change."
        }
      ]
    },
    {
      "round": 3,
      "closing": true,
      "strategy_version": 6,
      "review_sha256": "50966c61f6771d543f7ce6b4cc8d7bb9dcc77f6a183b7d39c8d821f94277ea55",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The BPD and psychotherapy terms cover the concepts and named modalities in scope. Fresh category-probe validation remains unavailable after block changes, so the associated uncertainty is accepted and retained."
        },
        "operators": {
          "verdict": "pass",
          "note": "The final strategy ANDs the condition and psychotherapy blocks. Removing the specialization block resolves the duplicated-heading issue."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "Relevant condition and psychotherapy MeSH headings remain, and no specialization block duplicates headings across an AND."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The unreviewed proximity clause was removed; exact hyphenated and unhyphenated transference-focused psychotherapy expressions remain."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports balanced query structure, no PubMed warnings or errors, an explicit entry-date range, and no lint findings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "Age and specialization remain screening criteria as specified. The 13,713-record workload exceeds the 10,000 budget; that tradeoff is explicitly accepted to preserve the stated search scope."
        }
      },
      "findings": [
        {
          "id": "P1-01",
          "domain": "operators",
          "severity": "should-fix",
          "kind": "structural",
          "finding": "The earlier specialization block repeated psychotherapy MeSH headings from the intervention block, allowing the same headings to satisfy both sides of an AND.",
          "recommendation": "Remove the duplicated headings or reconsider the block, then rerun the evaluation.",
          "status": "resolved",
          "response": "Version 6 removed the specialization block, so those duplicated headings no longer satisfy both sides of an AND."
        },
        {
          "id": "P1-02",
          "domain": "text_words",
          "severity": "should-fix",
          "kind": "lexical",
          "finding": "The earlier transference proximity clause lacked clause-specific interpretation review and rationale.",
          "recommendation": "Document its interpretation and evidence or remove it after assessing its contribution; rerun the evaluation after a change.",
          "status": "resolved",
          "response": "Version 6 removed the proximity clause and retains exact hyphenated and unhyphenated psychotherapy expressions."
        },
        {
          "id": "P1-03",
          "domain": "limits_filters",
          "severity": "document",
          "kind": "filter",
          "finding": "The earlier specialization block excluded 5,707 records; its 30-record sample offered limited reassurance and left residual recall risk.",
          "recommendation": "Retain the workload rationale and the sample's limitations in the audit record.",
          "status": "resolved",
          "response": "The specialization block was removed in version 6, so that exclusion no longer applies. The final query exceeds the stated workload budget instead."
        },
        {
          "id": "I-c63926f9f0a4c7c3fa67",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The current BPD category block lacks fresh probe validation after a block change, and one probe reported two relevant records outside the block.",
          "recommendation": "Refresh the probe if possible; otherwise document the stale validation and residual uncertainty.",
          "status": "accepted-risk",
          "response": "The probe budget is spent, so fresh validation is unavailable. The first probe reported two relevant records among 30 outside the narrower terms, while the correctly quoted second probe found zero outside records; the packet also flags a possible query/record inconsistency. These observations do not establish fresh validation."
        },
        {
          "id": "I-3b47b207ba8f2c0ae264",
          "domain": "translation",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The current psychotherapy category block lacks fresh probe validation after a block change.",
          "recommendation": "Refresh the probe if possible; otherwise document the stale validation and residual uncertainty.",
          "status": "accepted-risk",
          "response": "The probe budget is spent, so fresh validation is unavailable. Both reported samples screened 30 records outside the intervention block and found zero relevant records, but the packet marks the current block's probe status stale."
        },
        {
          "id": "I-a2ea70e99d0502ed4b2e",
          "domain": "limits_filters",
          "severity": "should-fix",
          "kind": "reporting",
          "finding": "The final query returns 13,713 records, exceeding the stated workload budget of 10,000.",
          "recommendation": "Document the workload tradeoff and why specialization remains a screening criterion.",
          "status": "accepted-risk",
          "response": "The protocol assigns specialization to screening because the sample did not establish that specialization labels are reliable enough to require. The optional block was considered and removed; the remaining workload is accepted to preserve the stated search scope."
        }
      ],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The protocol makes specialization a screening criterion, and removing the optional block preserves that scope despite the workload exceeding budget.",
          "evidence": "The final query returns 13,713 records against a 10,000-record budget. The earlier block excluded 5,707 records; its 30-record sample found no relevant records, which is limited evidence."
        },
        {
          "issue_id": "I-c63926f9f0a4c7c3fa67",
          "status": "accepted-risk",
          "response": "Fresh BPD category-probe validation is unavailable because the probe budget is spent; retain the stale status and uncertainty.",
          "evidence": "One probe reported 2 relevant records among 30 outside the narrower terms; another correctly quoted probe found 0 outside records. The packet notes a possible query/record inconsistency and marks the validation stale."
        },
        {
          "issue_id": "I-3b47b207ba8f2c0ae264",
          "status": "accepted-risk",
          "response": "Fresh psychotherapy category-probe validation is unavailable because the probe budget is spent; retain the stale status and uncertainty.",
          "evidence": "Two reported probes screened 30 records outside the block and found zero relevant records, but the packet marks the current block's validation stale after a change."
        }
      ]
    }
  ]
}
```

