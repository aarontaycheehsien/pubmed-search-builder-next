# Limits and methodological filters

Add a limit or filter only when the question or protocol requires it. Each one can remove
relevant records, so each needs a rationale in `strategy.json` `limits`, and `psb eval` reports
the count before and after limits and any known record the limits remove.

## Decision order

1. Is a filter needed at all? Usually not for scoping reviews, maps, small topics, or when
   study design is not an eligibility criterion.
2. What exactly should it find (RCTs, diagnostic studies, reviews, humans, an age group)?
3. Use a published, validated filter written for PubMed, in its sensitivity-maximising version.
4. Add it as a limit, run `psb eval`, and check which known records it removes.
5. Report the source, version, any adaptation, and the recall risk.

Do not present a hand-built block as a validated filter. If you change a published filter,
say it was adapted and that its published performance may no longer hold.

## Cochrane highly sensitive search strategy for RCTs (2008, PubMed format)

Sensitivity-maximising version (clause for `limits`, with the animal exclusion as a second limit):

```text
randomized controlled trial[pt] OR controlled clinical trial[pt] OR randomized[tiab] OR placebo[tiab] OR drug therapy[sh] OR randomly[tiab] OR trial[tiab] OR groups[tiab]
NOT (animals[mh] NOT humans[mh])
```

Sensitivity- and precision-maximising version:

```text
randomized controlled trial[pt] OR controlled clinical trial[pt] OR randomized[tiab] OR placebo[tiab] OR clinical trials as topic[mesh:noexp] OR randomly[tiab] OR trial[ti]
NOT (animals[mh] NOT humans[mh])
```

Source: Lefebvre C, et al. Cochrane Handbook for Systematic Reviews of Interventions,
Technical Supplement to Chapter 4, section 3.6.

## Other sources

| Need | Source |
|---|---|
| Therapy, diagnosis, prognosis, aetiology, prediction, economics, qualitative, reviews | McMaster HIRU Hedges (use the broad/sensitive version) |
| Filters for other designs and populations | ISSG Search Filters Resource (appraise before use: listing is not endorsement) |
| Systematic reviews | `systematic[sb]` is broader than `systematic review[pt]`; neither proves a record is a review |

## Cautions

- PubMed sidebar filters and many hedges depend on MeSH and publication types, so they miss
  records not yet indexed. Write any filter you use as search syntax so it can be reported.
- Ovid syntax (`.ti,ab.`, `exp`, `adj3`, `$`) must be translated for PubMed, and translations are
  not always one-to-one. If only an Ovid version exists, say that the translation needs checking
  by an information specialist.
- Language and date limits: use only when the protocol requires them.
