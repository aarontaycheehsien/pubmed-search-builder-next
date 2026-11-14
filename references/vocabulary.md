# Vocabulary: MeSH and free text

A block is `(MeSH layer OR text-word layer)`. Neither replaces the other: MeSH finds records
that use unexpected words, and text words find records that are not yet (or never) indexed.

## MeSH

1. `psb mesh lookup <concept>` for the concept, its synonyms, acronyms and spelled-out forms.
   Look at supplementary concept records (drugs, chemicals, rare diseases) as well as
   descriptors; a supplementary record lists the heading it maps to.
2. `psb mesh show <UI>` for the best matches: scope note (is it really your concept?), entry
   terms, tree numbers, narrower headings, and counts exploded versus `[Mesh:noexp]`.
3. Explode by default (`"Heading"[Mesh]`). Use `:noexp` only when the narrower headings are
   clearly out of scope, and say why.
4. Tag every heading explicitly. Never rely on a bare phrase mapping to MeSH.
5. Add MeSH that known records carry: `psb terms rank` lists headings common in your
   relevant sets; `psb fetch` shows each record's headings.
6. Avoid `[majr]` and `Heading/subheading` combinations in recall-first searches.
7. Check `year_introduced` and `previous_indexing` in `psb mesh show`. A heading only indexes
   records from the year it was introduced; when the literature is older than the heading, add
   the headings listed under previous indexing, or the earlier records rest on text words alone.
8. Drugs and chemicals: `psb terms rank` also lists substance names (`field: nm`) that known
   records carry in their chemical list, including supplementary concepts that have no heading.
   Search them as `"name"[nm]`. For a drug class, `"Class Name"[pa]` (pharmacological action)
   retrieves every substance PubMed assigns that action, descriptors and supplementary concepts
   alike, which exploding the class heading does not: use both, and check the count.

## Title and abstract words

For each concept, work through:

- every relevant MeSH entry term (the curated synonym list)
- full phrase, short phrase, acronym, and the acronym spelled out
- singular and plural; UK and US spelling; hyphenated, spaced and closed compounds
- older and newer names, eponyms, lay and technical terms, brand and generic drug names
- word-order variants (use proximity)
- terms from known records (`psb terms rank`) and from missed records (`psb terms miss`)

Tag with `[tiab]`. Multi-word terms without quotes are searched as a phrase when PubMed knows the
phrase; quote phrases to be explicit.

### Truncation

- A word-final `*` needs at least four letters before it (`colo*`). With fewer, PubMed silently
  searches the bare word (`cat*` becomes `cat`). `psb lint` catches this.
- Truncation turns off Automatic Term Mapping for that term.
- Prefer the longest safe stem (`neurostimulat*` rather than `stimulat*`), and check line counts
  in `psb eval` for noisy stems.
- PubMed rejects a query with more than 256 wildcards, with an error that looks like an outage.
- There is no left truncation: `virus*` finds viruses, not rotavirus, polyomavirus or
  coronavirus. When a concept word is also the tail of compound words (-virus, -itis, -oma, -mab,
  -statin, schoolchild), the text layer needs those words or their families by name; MeSH
  explosion covers them only for indexed records. `psb terms miss` reports this as
  `embedded_stem`.

### Proximity

`"shared decision making"[tiab:~2]` finds the words within 2 words of each other, in any order.

- Fields: `[tiab]`, `[ti]` or `[ad]` (and their documented full names) only.
- `~0` means adjacency in any order, not exact ordered phrase matching.
- No wildcards inside a proximity phrase (PubMed ignores the proximity if you add them).
- Test a few values of N; larger N adds recall and noise.
- Use proximity for multi-word concepts whose wording varies, truncation for single-word
  morphology, and combine them with OR across the block.
- A quoted or tagged phrase matches only those words in that order with nothing between them:
  `"high throughput sequencing"[tiab]` misses "high-throughput DNA sequencing". For a phrase
  authors can interrupt or reorder, add the proximity form (`[tiab:~1]` to `[tiab:~3]`).
- A long phrase requires every word. `cognitive behavio* therap*[tiab]` misses
  "cognitive-behavioral approaches" and "cognitive behavioural group treatment". When the
  distinctive part is specific on its own (`"cognitive behavio*"[tiab]`), search that and drop
  the head noun; check the line count.
- `psb terms miss` reports both as `phrase_gap`, with the form to test.

### Acronyms

Short or ambiguous acronyms (`US`, `AI`, `LLaMA`) retrieve unrelated records. Check the line
count; pair the acronym with a context term, or drop it if the spelled-out forms cover it.

## Reading `psb eval` and `psb count`

- `phrase_not_found` / `quoted_phrase_not_found`: inspect the affected clause's actual translation.
  Phrase-index absence is different from zero hits. Use the decision tree in `validation.md`;
  a retained warning needs an evidence-bound disposition, while a rewrite/removal needs re-evaluation.
- `zero_hits`: check spelling, effective date restrictions and Boolean role. A zero-hit OR
  alternative differs from a zero-hit required clause; neither seed coverage nor zero hits alone
  justifies removing vocabulary.
- `automatic_term_mapping` / `all_fields` / `untagged`: add field tags.
- `truncation_dropped`: the stem is too short; lengthen it or list the variants.
- A line with a very large count inside an AND-ed block is usually fine; a large count in the
  final result is the thing to manage. Cut noise only when no known record is lost.
- `psb eval --term-impact` measures that directly: `records_only_here` is what leaves the final
  result when one term is removed, `known_only_here` the known records that leave with it. A
  term with a large share and no known record of its own is a candidate, not a verdict: sample
  what it alone finds from its `sample_file` and judge that. It costs two requests per term,
  so run it when the result is too large, not on every eval.

## Controlled vocabulary versus text word gaps (Bramer)

After a block works, compare `"Heading"[Mesh] NOT (<text words>)` with
`(<text words>) NOT "Heading"[Mesh]` using `psb sample`. Records found only by MeSH show wording
your text layer lacks; records found only by text words show recent unindexed records or
headings you missed. Use this to add terms, never to remove them.
