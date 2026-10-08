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
5. Add MeSH that development records carry: `psb terms rank` lists headings common in your
   development sets; `psb fetch` shows each record's headings. Held-out records are never mined.
6. Avoid `[majr]` and `Heading/subheading` combinations in recall-first searches.

## Title and abstract words

For each concept, work through:

- every relevant MeSH entry term (the curated synonym list)
- full phrase, short phrase, acronym, and the acronym spelled out
- singular and plural; UK and US spelling; hyphenated, spaced and closed compounds
- older and newer names, eponyms, lay and technical terms, brand and generic drug names
- word-order variants (use proximity)
- terms from development records (`psb terms rank`) and from missed development records (`psb terms miss`)

Tag with `[tiab]`. Multi-word terms without quotes are searched as a phrase when PubMed knows the
phrase; quote phrases to be explicit.

### Truncation

- A word-final `*` needs at least four letters before it (`colo*`). With fewer, PubMed silently
  searches the bare word (`cat*` becomes `cat`). `psb lint` catches this.
- Truncation turns off Automatic Term Mapping for that term.
- Prefer the longest safe stem (`neurostimulat*` rather than `stimulat*`), and check line counts
  in `psb eval` for noisy stems.
- PubMed rejects a query with more than 256 wildcards, with an error that looks like an outage.

### Proximity

`"shared decision making"[tiab:~2]` finds the words within 2 words of each other, in any order.

- Fields: `[tiab]`, `[ti]` or `[ad]` (and their documented full names) only.
- `~0` means adjacency in any order, not exact ordered phrase matching.
- No wildcards inside a proximity phrase (PubMed ignores the proximity if you add them).
- Test a few values of N; larger N adds recall and noise.
- Use proximity for multi-word concepts whose wording varies, truncation for single-word
  morphology, and combine them with OR across the block.

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

## Controlled vocabulary versus text word gaps (Bramer)

After a block works, compare `"Heading"[Mesh] NOT (<text words>)` with
`(<text words>) NOT "Heading"[Mesh]` using `psb sample`. Records found only by MeSH show wording
your text layer lacks; records found only by text words show recent unindexed records or
headings you missed. Use this to add terms, never to remove them.
