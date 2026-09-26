# Internal critic (PRESS-structured)

The critic is a second, independent reading of the draft against the PRESS 2015 guideline
(McGowan et al., J Clin Epidemiol 2016, doi:10.1016/j.jclinepi.2016.01.021). It is automated
quality assurance, not PRESS peer review, and the audit must say so.

## Running a round

1. `psb critic packet` writes `critic/packet-N.md`: the question, concept roles, the strategy with
   line counts, recall on each set, missed records with failing blocks, ablation, and any findings
   still open. It refuses to run if `strategy.json` changed since the last `psb eval`.
2. Give only that file to a reviewer with a fresh context, so it does not share your reasoning:
   - Claude Code: start a subagent with a prompt like "Read <packet path> and follow its
     instructions. Reply with the JSON only." and save the reply as `critic/round-N.json`.
   - Codex or other hosts: run a separate non-interactive session (for example
     `codex exec` or `claude -p`) on the packet, if available.
   - With no fresh context available, review the packet yourself and note "same-context critic"
     in the round's `note` field; the audit will show it.
3. `psb critic check` validates the round: a verdict for all six domains, allowed values, and every
   earlier open finding carried forward by its ID.

## The six domains

| Key | PRESS element | Ask |
|---|---|---|
| `translation` | Translation of the question | Do the AND-ed blocks match the concepts? Is anything AND-ed that should be screened? |
| `operators` | Boolean and proximity operators | Are OR and AND used correctly? Any NOT? Proximity distances sensible? |
| `subject_headings` | Subject headings | Right descriptors, explosion, missing narrower or related headings, supplementary concepts? |
| `text_words` | Text-word searching | Missing synonyms, spellings, plurals, acronyms; truncation too short or too broad? |
| `syntax` | Spelling, syntax, line numbers | Field tags, quotes, parentheses, translation warnings? |
| `limits_filters` | Limits and filters | Is each limit justified, validated, and tested for lost records? |

## Finding fields

`id` (stable across rounds), `domain`, `severity` (`must-fix`, `should-fix`, `document`), `kind`,
`block`, `finding`, `recommendation`, `status` (`open`, `resolved`, `rejected`, `accepted-risk`),
and `response` (required for `rejected` and `accepted-risk`).

## Routing by kind

| Kind | What to do |
|---|---|
| `lexical` | Change terms in the named block; `psb eval`. |
| `structural` | Revisit the concept's role with the admission test in `scope.md`; update `protocol.json`; `psb eval`. |
| `scope` | Ask the user. Never change eligibility on the critic's word alone. |
| `filter` | Compare with and without the limit in `psb eval`; keep it only if justified. |
| `syntax` | Fix; `psb lint` and `psb eval`. |
| `reporting` | Fix the audit text; no strategy change. |

Before accepting a change, check that `psb eval` shows no newly lost known records. Update the
finding's `status` and `response` in the next round's file. Stop when no `must-fix` finding is
open; list remaining `should-fix` and `document` findings in the audit.
