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

If any answer is "no" or "unsure", the concept is not `search`. Choose between the other two:

- `optional` when authors usually name it in the title, abstract or MeSH but not reliably
  enough to require it (test 1 or 3 fails, test 2 is about its type): a topic-defining outcome
  ("lifestyle behaviours", "symptom trajectories", "dementia"), a setting, or a design with
  recognisable labels. Optional concepts are tested, never dropped untested.
- `screen` when it cannot be searched reliably at all: comparators, severity, subgroups,
  properties reported only in full text, and designs better handled by a validated filter.

Evidence: C and O elements have lower retrieval potential in PubMed (Frandsen 2020), so they
are not AND-ed by default; but leaving a topic-defining outcome unsearched can multiply the
screening load tenfold with no gain in recall. Testing decides.

References: Frandsen 2020, doi:10.1016/j.jclinepi.2020.07.005; two-block searches found more
relevant reviews than four-block searches (Ho 2016, doi:10.1371/journal.pone.0167170).

## Optional concepts: test, then decide

1. Build the block as carefully as a searched one (MeSH and free text; every member the
   criteria list, by its bare name) and put it in `strategy.json` `candidates`, with the
   concept's `id`. Candidates are never part of the query.
2. `psb eval` reports, for each optional concept: records without and with the block, the
   reduction, and the known records it would lose (by set).
3. `psb optional sample <id>` draws a random sample of the records the block would remove
   (30 at `standard`, 60 at `thorough`). Screen each against the eligibility criteria. Add any
   relevant record to a `relevant` set: it is now a known record the block loses.
4. Decide with `psb optional decide <id> --choice and|leave_out --reason "..." --relevant ...`.
   AND the block only when all three hold:
   - it loses no known record;
   - its loss sample contains no relevant record;
   - it cuts the count materially (about 30% or more).
   Otherwise leave it out and say why. `and` moves the block into `blocks`, where ablation keeps
   checking it; `leave_out` keeps it in `candidates`.
5. A decision is bound to the block and the query it was measured against. Any later change to
   either makes it stale: sample and decide again.

A loss sample of 0/30 only shows that fewer than about 10% of the removed records are relevant
(0/60: about 5%). With thousands removed that can still be many records, so the known-record
loss and the reduction matter as much as the sample. The audit reports all three.

Over the workload budget (`workload_budget` in `protocol.json`), `psb report` refuses delivery
until every optional concept has a current decision, and the count over budget needs a review
disposition: check whether any `screen` concept is in fact searchable and should be `optional`.

## Fragile concepts

A concept is fragile when failing to find its usual label is weak evidence that a paper lacks
it: workflows, behaviours, service settings, methods, and newly named constructs. Treat fragile
concepts as `screen` unless the question cannot be searched without them. If one must be
searched, give it a broad layer of descriptive phrases as well as its labels, and watch its
ablation result: a block whose removal gains known records is losing relevant papers.

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
  "workload_budget": 10000,
  "eligibility": {"include": ["children with UTI", "DMSA or ultrasound compared with VCUG"], "exclude": ["case reports"]},
  "limits": [],
  "as_of": null,
  "depth": "standard",
  "scope_confirmed": true,
  "notes": ""
}
```

The block `id` in `strategy.json` must equal the concept `id`. `psb lint` warns when a `search`
concept has no block or a `screen` concept is AND-ed.
