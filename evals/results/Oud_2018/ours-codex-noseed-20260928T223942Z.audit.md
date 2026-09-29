# PubMed search strategy: audit

Generated 2026-09-28T23:04:58+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Specialized psychotherapies for adults with borderline personality disorder
- Framework: PICO
- Scope confirmed by user: no (The user requested standard depth and asked that the run proceed without questions. Scope roles and assumptions are therefore unconfirmed. Assume the question means empirical studies of adults with BPD receiving a structured, manualized, or BPD-adapted psychotherapy; named modalities include DBT, MBT, transference-focused psychotherapy, schema-focused therapy, STEPPS, and other BPD-specific approaches. Adult status and whether an approach is sufficiently specialized will be judged at screening. No date/publication, language, age, or study-design search limits are used. The run is bounded by PubMed Entrez date 2015-03-27 through PSB_AS_OF, not by publication date. The expanded high-sensitivity query exceeded the default 10,000-record budget, so adult status was reconsidered as an optional searchable concept for measurement; it will be AND-ed only if the optional-concept criteria are met. A matching Cochrane systematic review was found (PMID 22895952), but the screened neighbor candidates could not all be verified as that review's included studies. They were classified as relevant development records, not an external benchmark; relative recall is therefore not independently validated.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Borderline personality disorder | search | The target condition is essential and is a reliably searchable diagnosis; alternate diagnostic labels will be covered in the vocabulary. |
| Psychotherapies used as specialized treatment for borderline personality disorder | search | The intervention concept is essential, but relevant studies may name only a modality (for example, dialectical behavior therapy) rather than psychotherapy generically, so named-member coverage and a category probe are required. |
| Adults | optional | Adult status is required for eligibility. PubMed has age headings and title/abstract age labels, but their coverage can be incomplete; because the high-recall intervention block exceeds the standard screening budget, test age as an optional AND block and leave it out if the loss evidence is unsafe. |
| Specialized or BPD-adapted psychotherapy | screen | Whether a psychotherapy is specialized/adapted is an eligibility judgment and may not be described consistently in searchable fields. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-28T23:03:52+00:00
- Records added to PubMed up to: 2015-03-27
- Total records: 13,536
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `Borderline Personality Disorder[Mesh]` | 5,413 | none |
| 2 | `borderline personality[tiab]` | 4,863 | none |
| 3 | `borderline personality disorder[tiab]` | 4,215 | none |
| 4 | `borderline personality disorders[tiab]` | 271 | none |
| 5 | `BPD[tiab]` | 6,222 | none |
| 6 | `emotionally unstable personality[tiab]` | 30 | none |
| 7 | `emotionally unstable personality disorder[tiab]` | 24 | none |
| 8 | `borderline[tiab]` | 32,409 | none |
| 9 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7 OR #8` | 37,479 | none |
| 10 | `Psychotherapy[Mesh]` | 165,482 | none |
| 11 | `Behavior Therapy[Mesh]` | 57,482 | none |
| 12 | `Cognitive Behavioral Therapy[Mesh]` | 18,757 | none |
| 13 | `Psychotherapy, Psychodynamic[Mesh]` | 210 | none |
| 14 | `Psychoanalytic Therapy[Mesh]` | 15,004 | none |
| 15 | `psychotherap*[tiab]` | 37,596 | none |
| 16 | `psychotherapeutic[tiab]` | 6,956 | none |
| 17 | `psychological therap*[tiab]` | 1,199 | none |
| 18 | `psychological treatment*[tiab]` | 2,598 | none |
| 19 | `psychosocial therap*[tiab]` | 283 | none |
| 20 | `psychosocial treatment*[tiab]` | 1,472 | none |
| 21 | `talking therap*[tiab]` | 82 | none |
| 22 | `dialectical behavior therap*[tiab]` | 278 | none |
| 23 | `dialectical behaviour therap*[tiab]` | 84 | none |
| 24 | `DBT[tiab]` | 1,420 | none |
| 25 | `mentalization[tiab]` | 254 | none |
| 26 | `mentalisation[tiab]` | 33 | none |
| 27 | `mentalizing[tiab]` | 567 | none |
| 28 | `mentalising[tiab]` | 65 | none |
| 29 | `MBT[tiab]` | 1,537 | none |
| 30 | `transference-focused[tiab]` | 54 | none |
| 31 | `transference focused[tiab]` | 54 | none |
| 32 | `TFP[tiab]` | 1,103 | none |
| 33 | `schema therap*[tiab]` | 76 | none |
| 34 | `schema-focused[tiab]` | 60 | none |
| 35 | `schema focused[tiab]` | 60 | none |
| 36 | `SFT[tiab]` | 1,028 | none |
| 37 | `STEPPS[tiab]` | 30 | none |
| 38 | `"systems training for emotional predictability and problem solving"[tiab]` | 16 | none |
| 39 | `dynamic deconstructive psychotherap*[tiab]` | 13 | none |
| 40 | `DDP[tiab]` | 2,490 | none |
| 41 | `general psychiatric management[tiab]` | 14 | none |
| 42 | `good psychiatric management[tiab]` | 1 | none |
| 43 | `GPM[tiab]` | 190 | none |
| 44 | `manual-assisted cognitive therap*[tiab]` | 4 | none |
| 45 | `manual assisted cognitive therap*[tiab]` | 4 | none |
| 46 | `MACT[tiab]` | 272 | none |
| 47 | `interpersonal psychotherap*[tiab]` | 655 | none |
| 48 | `interpersonal therap*[tiab]` | 270 | none |
| 49 | `cognitive analytic therap*[tiab]` | 57 | none |
| 50 | `cognitive therap*[tiab]` | 2,237 | none |
| 51 | `psychodynamic[tiab]` | 4,430 | none |
| 52 | `psychoanalytic[tiab]` | 10,200 | none |
| 53 | `emotion regulation group therap*[tiab]` | 7 | none |
| 54 | `structured clinical management[tiab]` | 4 | none |
| 55 | `disorder-specific treatment[tiab]` | 26 | none |
| 56 | `specialized inpatient treatment[tiab]` | 18 | none |
| 57 | `therapy[tiab]` | 1,438,128 | none |
| 58 | `therap*[tiab]` | 2,101,526 | none |
| 59 | `treat*[tiab]` | 4,027,758 | none |
| 60 | `#10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52 OR #53 OR #54 OR #55 OR #56 OR #57 OR #58 OR #59` | 5,186,521 | none |
| 61 | `#9 AND #60` | 13,536 | none |

### Strategy (single line, for copying into PubMed)

```text
((Borderline Personality Disorder[Mesh] OR borderline personality[tiab] OR borderline personality disorder[tiab] OR borderline personality disorders[tiab] OR BPD[tiab] OR emotionally unstable personality[tiab] OR emotionally unstable personality disorder[tiab] OR borderline[tiab]) AND (Psychotherapy[Mesh] OR Behavior Therapy[Mesh] OR Cognitive Behavioral Therapy[Mesh] OR Psychotherapy, Psychodynamic[Mesh] OR Psychoanalytic Therapy[Mesh] OR psychotherap*[tiab] OR psychotherapeutic[tiab] OR psychological therap*[tiab] OR psychological treatment*[tiab] OR psychosocial therap*[tiab] OR psychosocial treatment*[tiab] OR talking therap*[tiab] OR dialectical behavior therap*[tiab] OR dialectical behaviour therap*[tiab] OR DBT[tiab] OR mentalization[tiab] OR mentalisation[tiab] OR mentalizing[tiab] OR mentalising[tiab] OR MBT[tiab] OR transference-focused[tiab] OR transference focused[tiab] OR TFP[tiab] OR schema therap*[tiab] OR schema-focused[tiab] OR schema focused[tiab] OR SFT[tiab] OR STEPPS[tiab] OR "systems training for emotional predictability and problem solving"[tiab] OR dynamic deconstructive psychotherap*[tiab] OR DDP[tiab] OR general psychiatric management[tiab] OR good psychiatric management[tiab] OR GPM[tiab] OR manual-assisted cognitive therap*[tiab] OR manual assisted cognitive therap*[tiab] OR MACT[tiab] OR interpersonal psychotherap*[tiab] OR interpersonal therap*[tiab] OR cognitive analytic therap*[tiab] OR cognitive therap*[tiab] OR psychodynamic[tiab] OR psychoanalytic[tiab] OR emotion regulation group therap*[tiab] OR structured clinical management[tiab] OR disorder-specific treatment[tiab] OR specialized inpatient treatment[tiab] OR therapy[tiab] OR therap*[tiab] OR treat*[tiab])) AND ("1800/01/01"[edat] : "2015/03/27"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| relevant | relevant (records screened relevant during the build; used for development, not independent) | 30 | 30 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Tested optional concepts

Workload budget: 10,000 records. Each optional concept was tested as an extra AND-ed block. The loss sample is a random sample of the records that block removes, screened against the eligibility criteria.

| Concept | Decision | Records without / with block | Reduction | Known records lost | Loss sample relevant | Reason |
|---|---|---:|---:|---|---|---|
| Adults | left out | 13,536 / 7,637 | 43.6% | 20386260, 22122363 | 0/30 (up to 10% of removed records could be relevant) | Do not AND adult status: the block loses benchmark PMIDs 20386260 and 22122363, both relevant BPD psychotherapy studies without an explicit Adult heading or adult text, despite a 43.6% reduction. Screening all 30 sampled removed records found none eligible; this does not overcome the demonstrated known-record loss. Retain adult status as an eligibility screen. |

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Psychotherapies used as specialized treatment for borderline personality disorder | 1 | `(therap*[tiab] OR treatment*[tiab])` | 2,706 | 0/30 |
| Psychotherapies used as specialized treatment for borderline personality disorder | 2 | `(therap*[tiab] OR treatment*[tiab])` | 0 | 0/0 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| bpd | 5,186,521 | 0 |
| psychotherapy | 37,479 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 0 | initial | none | Initial high-sensitivity strategy: two required concepts from protocol; broad exploded psychotherapy MeSH plus title/abstract synonyms and named BPD psychotherapy families; no limits; adult/specialization criteria left to screening. |
| 2 | 1,992 | psychotherapy: +1 / -1 | none | Corrected lint by quoting the STEPPS program name so its word 'and' is parsed as title/abstract text, not a Boolean operator. |
| 3 | 1,992 | psychotherapy: +0 / -1 | none | Removed the Dialectical Behavior Therapy MeSH heading after authority inspection showed it was introduced in 2019, outside the 2015-03-27 index boundary, and returned zero hits; older records used Behavior Therapy. Retained dialectical behavior/behaviour text variants and broad exploded headings. |
| 4 | 13,536 | bpd: +1 / -0; psychotherapy: +3 / -0 | none | Widened for high sensitivity after the category probe showed a large pool of generic therapy/treatment wording outside the block: added therapy[tiab], therap*[tiab], and treat*[tiab]. Added borderline[tiab] based on term ranking of the screened development records to cover records naming only borderline patients. Probe 1 remains valid because the block only gained terms. |
| 5 | 13,536 | limits/combination | none | Made adult status optional because the generic treatment expansion raised the candidate count above the standard 10,000-record budget. Measured an age heading/text block to determine whether it cuts volume materially without unacceptable losses; adult eligibility itself is unchanged. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 5: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 948 NCBI requests logged (634 from cache); strategy sha256 6375b678f00d._

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
        "message": "13,536 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      }
    ],
    "issues": [
      {
        "code": "over_workload_budget",
        "message": "13,536 results exceed the workload budget of 10,000; confirm every searchable concept that is only screened has been considered as an optional block",
        "severity": "warning",
        "location": "final",
        "budget": 10000,
        "blocking": false,
        "requires_review": true,
        "id": "I-a2ea70e99d0502ed4b2e"
      }
    ]
  },
  "vocabulary": [
    {
      "requested": "Borderline Personality Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:03:52+00:00",
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
      "requested": "Psychotherapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:03:52+00:00",
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
      "location": "vocabulary:9",
      "term": {
        "text": "Psychotherapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Behavior Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:03:52+00:00",
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
      "location": "vocabulary:10",
      "term": {
        "text": "Behavior Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Cognitive Behavioral Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:03:52+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D015928",
          "name": "Cognitive Behavioral Therapy",
          "type": "descriptor",
          "scope_note": "A directive form of psychotherapy based on the interpretation of situations (cognitive structure of experiences) that determine how an individual feels and behaves. It is based on the premise that cognition, the process of acquiring knowledge and forming beliefs, is a primary determinant of mood and behavior. The therapy uses behavioral and verbal techniques to identify and correct negative thi...",
          "tree_numbers": [
            "F04.754.137.350"
          ],
          "entry_terms": 29,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D015928",
      "preferred_label": "Cognitive Behavioral Therapy",
      "type": "descriptor",
      "location": "vocabulary:11",
      "term": {
        "text": "Cognitive Behavioral Therapy",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychotherapy, Psychodynamic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:03:52+00:00",
      "source": "NCBI MeSH ESearch/ESummary",
      "candidates": [
        {
          "ui": "D064889",
          "name": "Psychotherapy, Psychodynamic",
          "type": "descriptor",
          "scope_note": "Forms of PSYCHOTHERAPY falling within or deriving from the psychoanalytic tradition, that view individuals as reacting to unconscious forces (e.g., motivation, drive), that focus on processes of change and development, and that place a premium on self understanding and making meaning of what is unconscious.",
          "tree_numbers": [
            "F04.754.775"
          ],
          "entry_terms": 3,
          "mapped_to": null
        }
      ],
      "status": "verified",
      "ui": "D064889",
      "preferred_label": "Psychotherapy, Psychodynamic",
      "type": "descriptor",
      "location": "vocabulary:12",
      "term": {
        "text": "Psychotherapy, Psychodynamic",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychoanalytic Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-28T23:03:52+00:00",
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
    }
  ],
  "translation": "(\"borderline personality disorder\"[MeSH Terms] OR \"borderline personality\"[Title/Abstract] OR \"borderline personality disorder\"[Title/Abstract] OR \"borderline personality disorders\"[Title/Abstract] OR \"BPD\"[Title/Abstract] OR \"emotionally unstable personality\"[Title/Abstract] OR \"emotionally unstable personality disorder\"[Title/Abstract] OR \"borderline\"[Title/Abstract]) AND (\"psychotherapy\"[MeSH Terms] OR \"behavior therapy\"[MeSH Terms] OR \"cognitive behavioral therapy\"[MeSH Terms] OR \"psychotherapy, psychodynamic\"[MeSH Terms] OR \"psychoanalytic therapy\"[MeSH Terms] OR \"psychotherap*\"[Title/Abstract] OR \"psychotherapeutic\"[Title/Abstract] OR \"psychological therap*\"[Title/Abstract] OR \"psychological treatment*\"[Title/Abstract] OR \"psychosocial therap*\"[Title/Abstract] OR \"psychosocial treatment*\"[Title/Abstract] OR \"talking therap*\"[Title/Abstract] OR \"dialectical behavior therap*\"[Title/Abstract] OR \"dialectical behaviour therap*\"[Title/Abstract] OR \"DBT\"[Title/Abstract] OR \"mentalization\"[Title/Abstract] OR \"mentalisation\"[Title/Abstract] OR \"mentalizing\"[Title/Abstract] OR \"mentalising\"[Title/Abstract] OR \"MBT\"[Title/Abstract] OR \"transference-focused\"[Title/Abstract] OR \"transference-focused\"[Title/Abstract] OR \"TFP\"[Title/Abstract] OR \"schema therap*\"[Title/Abstract] OR \"schema-focused\"[Title/Abstract] OR \"schema-focused\"[Title/Abstract] OR \"SFT\"[Title/Abstract] OR \"STEPPS\"[Title/Abstract] OR \"systems training for emotional predictability and problem solving\"[Title/Abstract] OR \"dynamic deconstructive psychotherap*\"[Title/Abstract] OR \"DDP\"[Title/Abstract] OR \"general psychiatric management\"[Title/Abstract] OR \"good psychiatric management\"[Title/Abstract] OR \"GPM\"[Title/Abstract] OR \"manual assisted cognitive therap*\"[Title/Abstract] OR \"manual assisted cognitive therap*\"[Title/Abstract] OR \"MACT\"[Title/Abstract] OR \"interpersonal psychotherap*\"[Title/Abstract] OR \"interpersonal therap*\"[Title/Abstract] OR \"cognitive analytic therap*\"[Title/Abstract] OR \"cognitive therap*\"[Title/Abstract] OR \"psychodynamic\"[Title/Abstract] OR \"psychoanalytic\"[Title/Abstract] OR \"emotion regulation group therap*\"[Title/Abstract] OR \"structured clinical management\"[Title/Abstract] OR \"disorder specific treatment\"[Title/Abstract] OR \"specialized inpatient treatment\"[Title/Abstract] OR \"therapy\"[Title/Abstract] OR \"therap*\"[Title/Abstract] OR \"treat*\"[Title/Abstract]) AND 1800/01/01:2015/03/27[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 5,
      "review_sha256": "a9e7eeeca2953d705457170e0e152f57999f49a9630c2ada0b2e3047c8aa9b75",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The query translates the MeSH headings and Title/Abstract terms as intended. Diagnostics report no phrase warnings, translation issues, or errors."
        },
        "operators": {
          "verdict": "pass",
          "note": "The BPD and psychotherapy synonym blocks are OR-combined and then AND-combined. The adult block is omitted after testing showed known relevant records would be lost."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The condition and intervention blocks include relevant MeSH headings alongside free-text terms. No heading translation errors are reported."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The vocabulary covers the named modalities and programs in the stated scope, including bare abbreviations such as DBT, MBT, TFP, STEPPS, DDP, GPM, and MACT. Broad terms are retained for sensitivity; the category probe found no relevant omissions in its screened sample."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The reported PubMed translation is structurally coherent, with no syntax errors or warnings."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No adult, language, publication-type, or study-design filter is applied. The documented Entry Date boundary is distinct from publication date and is disclosed in the protocol notes."
        }
      },
      "findings": [],
      "issue_dispositions": [
        {
          "issue_id": "I-a2ea70e99d0502ed4b2e",
          "status": "accepted-risk",
          "response": "The query exceeds the 10,000-record workload budget, but the only identified searchable eligibility concept, adult status, was tested as an optional block and left out because it would lose known relevant records. Preserve adult status for screening; record the larger screening workload as an accepted risk.",
          "evidence": "The adult block reduced results from 13,536 to 7,637 but lost relevant PMIDs 20386260 and 22122363. The 0/30 relevant loss sample does not offset those known losses. Specialization is documented as a screening judgment, and no other searchable eligibility concept is identified for optional-block testing."
        }
      ]
    }
  ]
}
```

