# PubMed search strategy: audit

Generated 2026-09-29T02:24:35+00:00 by `psb report` from workspace files. Draft for human PRESS peer review.

## Question and scope

- Question: Specialized psychotherapies for adults with borderline personality disorder
- Framework: PICO
- Scope confirmed by user: yes (User asked to proceed without clarification. Assumptions: PICO intervention question; adults and specialized/structured status will be screened rather than AND-ed or age-filtered. 'Specialized psychotherapies' is interpreted broadly to include named structured psychotherapies for BPD; exact eligible modality boundaries should be confirmed in the review protocol. No known relevant articles supplied. PubMed is bounded by PSB_AS_OF=2015-03-27 (Entrez date), with no publication-date filter.)
- Depth: standard

| Concept | Handling | Rationale |
|---|---|---|
| Borderline personality disorder | search | Target condition defining the review population; consistently named in titles, abstracts, or indexing. |
| Specialized psychotherapies | search | Intervention defining the review; records may name a specific psychotherapy without using the generic category term. Specific modalities such as dialectical behavior therapy, mentalization-based treatment, transference-focused psychotherapy, schema therapy, and STEPPS will be represented where vocabulary supports them. |
| Adults | screen | Age is handled at screening to avoid losing mixed-age or age-unspecified reports; no age filter is applied. |
| Specialized/structured therapy status | screen | Whether an intervention meets the protocol's meaning of specialized requires screening; no narrow modality requirement was supplied. |

## Search details (PRISMA-S)

- Database and platform: PubMed (NCBI E-utilities; includes MEDLINE and non-MEDLINE records)
- Date the final counts were run: 2026-09-29T02:23:39+00:00
- Records added to PubMed up to: 2015-03-27
- Total records: 1,916
- Limits and filters: none

### Strategy (line by line)

| # | Search | Results | Diagnostics |
|---:|---|---:|---|
| 1 | `"Borderline Personality Disorder"[Mesh]` | 5,413 | none |
| 2 | `"borderline personality disorder"[tiab]` | 4,215 | none |
| 3 | `"borderline personality disorders"[tiab]` | 271 | none |
| 4 | `"borderline personality"[tiab]` | 4,863 | none |
| 5 | `"emotionally unstable personality disorder"[tiab]` | 24 | none |
| 6 | `"emotionally unstable personality"[tiab]` | 30 | none |
| 7 | `BPD[tiab]` | 6,222 | none |
| 8 | `#1 OR #2 OR #3 OR #4 OR #5 OR #6 OR #7` | 10,827 | none |
| 9 | `"Psychotherapy"[Mesh]` | 165,482 | none |
| 10 | `"Psychotherapy, Psychodynamic"[Mesh]` | 210 | none |
| 11 | `"Psychotherapy, Group"[Mesh]` | 24,106 | none |
| 12 | `"Psychoanalytic Therapy"[Mesh]` | 15,004 | none |
| 13 | `"Behavior Therapy"[Mesh]` | 57,482 | none |
| 14 | `psychotherap*[tiab]` | 37,596 | none |
| 15 | `psychological therap*[tiab]` | 1,199 | none |
| 16 | `psychological treatmen*[tiab]` | 2,598 | none |
| 17 | `dialectical behavio*[tiab]` | 441 | none |
| 18 | `DBT[tiab]` | 1,420 | none |
| 19 | `mentalization[tiab]` | 254 | none |
| 20 | `mentalisation[tiab]` | 33 | none |
| 21 | `transference-focused[tiab]` | 54 | none |
| 22 | `transference focused[tiab]` | 54 | none |
| 23 | `schema therap*[tiab]` | 76 | none |
| 24 | `STEPPS[tiab]` | 30 | none |
| 25 | `emotion regulation group therap*[tiab]` | 7 | none |
| 26 | `dynamic deconstructive psychotherap*[tiab]` | 13 | none |
| 27 | `cognitive analytic therap*[tiab]` | 57 | none |
| 28 | `cognitive therap*[tiab]` | 2,237 | none |
| 29 | `psychodynamic therap*[tiab]` | 361 | none |
| 30 | `psychoanalytic therap*[tiab]` | 1,534 | none |
| 31 | `interpersonal psychotherap*[tiab]` | 655 | none |
| 32 | `schema-focused[tiab]` | 60 | none |
| 33 | `schema focused[tiab]` | 60 | none |
| 34 | `SFT[tiab]` | 1,028 | none |
| 35 | `TFP[tiab]` | 1,103 | none |
| 36 | `MBT[tiab]` | 1,537 | none |
| 37 | `mentalization based treatment[tiab]` | 40 | none |
| 38 | `mentalisation based treatment[tiab]` | 8 | none |
| 39 | `general psychiatric management[tiab]` | 14 | none |
| 40 | `GPM[tiab]` | 190 | none |
| 41 | `manual-assisted cognitive treatment[tiab]` | 3 | none |
| 42 | `manual assisted cognitive treatment[tiab]` | 3 | none |
| 43 | `MACT[tiab]` | 272 | none |
| 44 | `conversational model[tiab]` | 22 | none |
| 45 | `conversation model[tiab]` | 4 | none |
| 46 | `cognitive behavioral therap*[tiab]` | 5,059 | none |
| 47 | `cognitive behaviour therap*[tiab]` | 1,117 | none |
| 48 | `behavior therap*[tiab]` | 3,612 | none |
| 49 | `behaviour therap*[tiab]` | 1,833 | none |
| 50 | `client-centered therap*[tiab]` | 72 | none |
| 51 | `client centred therap*[tiab]` | 16 | none |
| 52 | `psychoeducation[tiab]` | 1,808 | none |
| 53 | `#9 OR #10 OR #11 OR #12 OR #13 OR #14 OR #15 OR #16 OR #17 OR #18 OR #19 OR #20 OR #21 OR #22 OR #23 OR #24 OR #25 OR #26 OR #27 OR #28 OR #29 OR #30 OR #31 OR #32 OR #33 OR #34 OR #35 OR #36 OR #37 OR #38 OR #39 OR #40 OR #41 OR #42 OR #43 OR #44 OR #45 OR #46 OR #47 OR #48 OR #49 OR #50 OR #51 OR #52` | 183,740 | none |
| 54 | `#8 AND #53` | 1,916 | none |

### Strategy (single line, for copying into PubMed)

```text
(("Borderline Personality Disorder"[Mesh] OR "borderline personality disorder"[tiab] OR "borderline personality disorders"[tiab] OR "borderline personality"[tiab] OR "emotionally unstable personality disorder"[tiab] OR "emotionally unstable personality"[tiab] OR BPD[tiab]) AND ("Psychotherapy"[Mesh] OR "Psychotherapy, Psychodynamic"[Mesh] OR "Psychotherapy, Group"[Mesh] OR "Psychoanalytic Therapy"[Mesh] OR "Behavior Therapy"[Mesh] OR psychotherap*[tiab] OR psychological therap*[tiab] OR psychological treatmen*[tiab] OR dialectical behavio*[tiab] OR DBT[tiab] OR mentalization[tiab] OR mentalisation[tiab] OR transference-focused[tiab] OR transference focused[tiab] OR schema therap*[tiab] OR STEPPS[tiab] OR emotion regulation group therap*[tiab] OR dynamic deconstructive psychotherap*[tiab] OR cognitive analytic therap*[tiab] OR cognitive therap*[tiab] OR psychodynamic therap*[tiab] OR psychoanalytic therap*[tiab] OR interpersonal psychotherap*[tiab] OR schema-focused[tiab] OR schema focused[tiab] OR SFT[tiab] OR TFP[tiab] OR MBT[tiab] OR mentalization based treatment[tiab] OR mentalisation based treatment[tiab] OR general psychiatric management[tiab] OR GPM[tiab] OR manual-assisted cognitive treatment[tiab] OR manual assisted cognitive treatment[tiab] OR MACT[tiab] OR conversational model[tiab] OR conversation model[tiab] OR cognitive behavioral therap*[tiab] OR cognitive behaviour therap*[tiab] OR behavior therap*[tiab] OR behaviour therap*[tiab] OR client-centered therap*[tiab] OR client centred therap*[tiab] OR psychoeducation[tiab])) AND ("1800/01/01"[edat] : "2015/03/27"[edat])
```

## Validation against known relevant records

| Set | Role (independence) | In PubMed | Retrieved | Recall |
|---|---|---:|---:|---:|
| benchmark | benchmark (included studies of a prior review; external benchmark) | 19 | 19 | 100.0% |

Relative recall against these sets is not absolute sensitivity. Development sets were used to build the strategy and cannot show how it performs on unseen records.

### Category probes

Each probe sampled records that the rest of the strategy and a broader query retrieve but the category block does not, and screened them against the eligibility criteria.

| Concept | Probe | Broader query | Records outside the block | Relevant / screened |
|---|---:|---|---:|---|
| Specialized psychotherapies | 1 | `therapy[tiab] OR Therapy[Mesh]` | 2,262 | 0/30 |

### Leave-one-block-out

| Block dropped | Records | Known records gained |
|---|---:|---:|
| bpd | 183,740 | 0 |
| psychotherapy | 10,827 | 0 |

## Development history

| Version | Records | Change | Known lost | Note |
|---:|---:|---|---|---|
| 1 | 1,902 | initial | none | Initial two-block strategy from question; no user-supplied seeds. Added generic psychotherapy/psychological therapy language and established named therapy modalities as member coverage for category probe. |
| 2 | 1,916 | psychotherapy: +21 / -0 | none | Expanded the psychotherapy block with named structured modalities and variants (schema-focused therapy, MBT, TFP, cognitive/behavior therapies, MACT, conversational model, GPM, psychoeducation) to capture member-named reports. No known benchmark loss expected; checked below. |

## Internal critic (PRESS-informed, not PRESS peer review)

- Round 1 on version 2: 0 findings; 

## Limitations

- This is a draft. It needs peer review by an information specialist (PRESS) before use.
- The internal critic is automated quality assurance, not PRESS peer review.
- PubMed only: records indexed only in other databases are out of reach of this strategy.

_Provenance: 480 NCBI requests logged (190 from cache); strategy sha256 12af982f92f0._

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
      "requested": "Borderline Personality Disorder",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:23:39+00:00",
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
        "text": "\"Borderline Personality Disorder\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychotherapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:23:39+00:00",
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
      "location": "vocabulary:8",
      "term": {
        "text": "\"Psychotherapy\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychotherapy, Psychodynamic",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:23:39+00:00",
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
      "location": "vocabulary:9",
      "term": {
        "text": "\"Psychotherapy, Psychodynamic\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychotherapy, Group",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:23:39+00:00",
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
      "location": "vocabulary:10",
      "term": {
        "text": "\"Psychotherapy, Group\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Psychoanalytic Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:23:39+00:00",
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
      "location": "vocabulary:11",
      "term": {
        "text": "\"Psychoanalytic Therapy\"",
        "tag": "Mesh",
        "field": "mh"
      }
    },
    {
      "requested": "Behavior Therapy",
      "expected_type": "descriptor",
      "checked_at": "2026-09-29T02:23:39+00:00",
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
        "text": "\"Behavior Therapy\"",
        "tag": "Mesh",
        "field": "mh"
      }
    }
  ],
  "translation": "(\"Borderline Personality Disorder\"[MeSH Terms] OR \"Borderline Personality Disorder\"[Title/Abstract] OR \"borderline personality disorders\"[Title/Abstract] OR \"borderline personality\"[Title/Abstract] OR \"emotionally unstable personality disorder\"[Title/Abstract] OR \"emotionally unstable personality\"[Title/Abstract] OR \"BPD\"[Title/Abstract]) AND (\"Psychotherapy\"[MeSH Terms] OR \"psychotherapy, psychodynamic\"[MeSH Terms] OR \"psychotherapy, group\"[MeSH Terms] OR \"Psychoanalytic Therapy\"[MeSH Terms] OR \"Behavior Therapy\"[MeSH Terms] OR \"psychotherap*\"[Title/Abstract] OR \"psychological therap*\"[Title/Abstract] OR \"psychological treatmen*\"[Title/Abstract] OR \"dialectical behavio*\"[Title/Abstract] OR \"DBT\"[Title/Abstract] OR \"mentalization\"[Title/Abstract] OR \"mentalisation\"[Title/Abstract] OR \"transference-focused\"[Title/Abstract] OR \"transference-focused\"[Title/Abstract] OR \"schema therap*\"[Title/Abstract] OR \"STEPPS\"[Title/Abstract] OR \"emotion regulation group therap*\"[Title/Abstract] OR \"dynamic deconstructive psychotherap*\"[Title/Abstract] OR \"cognitive analytic therap*\"[Title/Abstract] OR \"cognitive therap*\"[Title/Abstract] OR \"psychodynamic therap*\"[Title/Abstract] OR \"psychoanalytic therap*\"[Title/Abstract] OR \"interpersonal psychotherap*\"[Title/Abstract] OR \"schema-focused\"[Title/Abstract] OR \"schema-focused\"[Title/Abstract] OR \"SFT\"[Title/Abstract] OR \"TFP\"[Title/Abstract] OR \"MBT\"[Title/Abstract] OR \"mentalization based treatment\"[Title/Abstract] OR \"mentalisation based treatment\"[Title/Abstract] OR \"general psychiatric management\"[Title/Abstract] OR \"GPM\"[Title/Abstract] OR \"manual assisted cognitive treatment\"[Title/Abstract] OR \"manual assisted cognitive treatment\"[Title/Abstract] OR \"MACT\"[Title/Abstract] OR \"conversational model\"[Title/Abstract] OR \"conversation model\"[Title/Abstract] OR \"cognitive behavioral therap*\"[Title/Abstract] OR \"cognitive behaviour therap*\"[Title/Abstract] OR \"behavior therap*\"[Title/Abstract] OR \"behaviour therap*\"[Title/Abstract] OR \"client centered therap*\"[Title/Abstract] OR \"client centred therap*\"[Title/Abstract] OR \"psychoeducation\"[Title/Abstract]) AND 1800/01/01:2015/03/27[Date - Entry]",
  "critic": [
    {
      "round": 1,
      "strategy_version": 2,
      "review_sha256": "694ef6db68c26193b3286c4e5c85f456c9d9511a21a036416117666ec1bb5202",
      "domains": {
        "translation": {
          "verdict": "pass",
          "note": "The search covers the condition and named modalities; adults and specialized-therapy status are handled at screening."
        },
        "operators": {
          "verdict": "pass",
          "note": "OR is used within concepts and AND between condition and intervention; no proximity or direction-specific process terms require correction."
        },
        "subject_headings": {
          "verdict": "pass",
          "note": "The packet's verified MeSH headings complement free-text coverage for modalities without dedicated headings."
        },
        "text_words": {
          "verdict": "pass",
          "note": "The terms cover common named modalities and variants; all 19 benchmark reports were retrieved, and the category probe screened 30 with no relevant records."
        },
        "syntax": {
          "verdict": "pass",
          "note": "The packet reports no PubMed query errors or warnings; repeated translated variants do not change retrieval."
        },
        "limits_filters": {
          "verdict": "pass",
          "note": "No age or publication-date filter is applied; the Entrez date cutoff is documented."
        }
      },
      "findings": [],
      "issue_dispositions": []
    }
  ]
}
```

