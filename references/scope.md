# Scope: framework, concepts and roles

Decide what the strategy must contain from the question alone, before reading any seed record.
Most recall loss in reviewed LLM strategies comes from AND-ing too many concepts.

## Pick the framework from the question type

| Question type | Framework | Usually not searched |
|---|---|---|
| Intervention effectiveness | PICO | comparator, outcome |
| Exposure, risk factor, aetiology | PECO | comparator; outcome unless it defines the topic |
| Diagnostic accuracy | PIRD (population, index test, reference standard, diagnosis) | reference standard, accuracy terms |
| Prognosis | population + prognostic factor + outcome | comparator |
| Prevalence or incidence | condition + population/context | the measure itself |
| Qualitative experience | PICo or SPIDER | design and evaluation terms |
| Scoping review or map | PCC | context, unless central |
| Method or tool performance | method + task (+ application context if definitional) | comparator, performance outcome |

An umbrella review keeps the framework of its underlying question; the report type (reviews)
is handled with a filter decision, not a new framework.

## The AND-block admission test

A concept becomes an AND-ed block (`role: search`) only if all of these hold:

1. Every relevant record must involve it.
2. It is a searchable topic (a disease, drug, test, population group, technology), not an
   eligibility property judged at screening (a design feature, a quality, an outcome).
3. Authors and indexers name it reliably in the title, abstract or MeSH.
4. It cannot be handled more safely inside another block, at screening, or with a validated
   filter.
5. No high-impact ambiguity about it remains.

If any answer is "no", make it `screen`. If an answer is "unsure", make it `optional` and
measure it (below). Outcomes, comparators, narrow settings, subgroups, severity and study design
fail by default unless the question makes them the topic itself (for example, a review about a
specific cause of death).

Evidence: C and O elements have lower retrieval potential in PubMed (Frandsen 2020,
doi:10.1016/j.jclinepi.2020.07.005); two-block searches found more relevant reviews than
four-block searches (Ho 2016, doi:10.1371/journal.pone.0167170).

## Measure before you decide: optional blocks

Leaving a concept out is as much a decision as AND-ing it, and it has a cost: a search too large
to screen finds nothing. Rule 3 of the admission test (is it named reliably?) is an empirical
question, so answer it with a measurement whenever known records exist.

Give an `optional` concept a block under `optional` in `strategy.json`. It is never part of the
query. `psb eval` reports for it, in `optional_blocks`:

- `count_if_added` and `reduction_percent`: the result with the block AND-ed in;
- `known.lost_if_added`: the known records, now retrieved, that the block would lose;
- `known.by_route`: the same, split by how each record was found. `independent` records are
  those no keyword search led to: user seeds, and the reference list of a prior review
  (`psb neighbors --links refs`). `keyword_derived` records came from a pilot search or from the
  similar and citing articles of its hits. They name the searched words by construction, so they
  cannot show what a block built on those words would lose, however many there are;
- `known.loss_upper_95_percent`: on the independent records only, the largest share of relevant
  records the block could plausibly lose (0 lost of 10 still allows 26%; of 20, 14%; of 30,
  10%). Null when there are no independent records: the loss is then unmeasured;
- `known.block_recall`: how many known records name the concept at all;
- `known.missed_now_but_in_block`: records the current search misses that this block finds. If
  there are several, this concept may be more reliably named than a block you are searching.

AND the block (move it to `blocks`, set the role to `search`) when all of these hold:

1. no known record is lost, in any set;
2. at least about 20 independent known records are retrieved now;
3. the result falls by at least a quarter.

With fewer independent records the loss is unmeasured, whatever the total says. First look for
independent records: the included studies of a prior review are the usual source. AND the block
without them only when the result is otherwise too large to screen, make the block as broad as
the count allows, and report the loss in `narrative.md` as an open, unmeasured risk. Never
describe "none of N keyword-found records lost" as evidence that the block is safe.

If a known record is lost, broaden the block and test again, or leave it optional. Record the
decision and the numbers in the concept's `rationale`. A concept left optional stays in the
audit as a tested alternative.

## Fragile concepts

A concept is fragile when failing to find its usual label is weak evidence that a paper lacks
it: workflows, behaviours, service settings, methods, and newly named constructs. Do not AND a
fragile concept on judgement; make it `optional`, give it a broad layer of descriptive phrases
as well as its labels, and measure it. Fragility belongs to the wording, not the category: in a
review of symptom trajectories the method (trajectory, growth mixture, latent class) can be
named in every relevant abstract while the condition is named three different ways. For a
fragile concept you do search, watch its ablation result: a block whose removal gains known
records is losing relevant papers.

### Direction, sequence and events in a subset

A concept that names one direction or step of a process (switching back, reverse switching,
de-escalation, restarting, discontinuation) or an event that happens to only some participants
is fragile even when the question is about it. Studies of the whole process (switching from the
originator to a biosimilar) often report it as a secondary finding, in a sentence of the abstract
or only in the full text. Search the process in either direction (`switch*`, `transition*`,
`substitut*`, the relevant MeSH), and screen for the direction or event. A prior review of the
parent process is a candidate benchmark source: its included studies may report the event.

## Named members of a concept

When the question or eligibility criteria list members of a concept ("SEM-family models (CFA,
latent growth, multilevel, mediation)", "biologics such as infliximab or adalimumab"), every
member belongs in that concept's block, searched by its own bare name: `mediation`,
`multilevel`, `"hierarchical model*"`. Do not narrow a member with the parent's wording
(`"mediation model*"`, `"multilevel structural equation"`): records about a member rarely also
name the parent, which is why the criteria list it. The member terms are usually cheap because
another AND-ed block restricts them; check the final count, not the line count.

## Ambiguity check

Before assigning roles, list ambiguities and ask the user about any that would change which
concepts are AND-ed:

- population or outcome? (post-stroke depression: is depression the condition or the outcome?)
- intervention or exposure? (hormone therapy in trials or in cohorts?)
- diagnostic accuracy or screening effectiveness?
- a narrow action or the broader workflow? ("LLMs writing Boolean queries" versus "LLMs
  supporting any stage of evidence synthesis")

## protocol.json

```json
{
  "question": "In children with urinary tract infection, how accurate are DMSA scans and ultrasound for detecting vesicoureteral reflux?",
  "framework": "PIRD",
  "concepts": [
    {"id": "reflux", "name": "Vesicoureteral reflux", "role": "search", "rationale": "target condition, reliably named and indexed"},
    {"id": "test", "name": "DMSA scan or ultrasound", "role": "search", "rationale": "index tests, named in abstracts"},
    {"id": "children_uti", "name": "Children with UTI", "role": "screen", "rationale": "age and UTI context often only in full text"},
    {"id": "accuracy", "name": "Accuracy measures", "role": "screen", "rationale": "accuracy terms are unreliable in abstracts"}
  ],
  "eligibility": {"include": ["children with UTI", "DMSA or ultrasound compared with VCUG"], "exclude": ["case reports"]},
  "limits": [],
  "as_of": null,
  "depth": "standard",
  "scope_confirmed": true,
  "notes": ""
}
```

To measure a concept instead of guessing, set its role to `optional` and draft it in
`strategy.json` beside the searched blocks:

```json
{
  "blocks": [{"id": "reflux", "name": "Vesicoureteral reflux", "terms": ["..."]},
             {"id": "test", "name": "DMSA scan or ultrasound", "terms": ["..."]}],
  "optional": [{"id": "children_uti", "name": "Children with UTI",
                "terms": ["\"Child\"[Mesh]", "\"Infant\"[Mesh]", "child*[tiab]", "infan*[tiab]", "pediatric*[tiab]", "paediatric*[tiab]"]}],
  "combine": null,
  "limits": []
}
```

The block `id` in `strategy.json` must equal the concept `id`, for `blocks` and for `optional`
alike. `psb lint` warns when a `search` concept has no block or a `screen` concept is AND-ed, and
notes an `optional` concept with no block to measure and a one-block search with nothing tested.
