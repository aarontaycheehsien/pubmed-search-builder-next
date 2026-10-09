# Internal critic (PRESS-structured)

The critic is a second, independent reading of the draft against the PRESS 2015 guideline
(McGowan et al., J Clin Epidemiol 2016, doi:10.1016/j.jclinepi.2016.01.021). It is automated
quality assurance, not PRESS peer review, and the audit must say so.

## Running a round

1. `psb critic packet` writes `critic/packet-N.md`: the question, concept roles, the strategy with
   line counts, development and comparison retrieval per set, missed records with failing blocks,
   ablation, and any findings still open. It requires a complete current evaluation and includes all
   line translations, vocabulary evidence, structured diagnostics, and a `review_sha256` binding.
   Changed scope, sets, effective dates or interpretation require a new packet; count/timestamp
   changes alone do not. Held-out records are never in the packet: it says only how many units are
   reserved, and the reviewer must not ask for them. The held-out test runs after the review.
2. Give only that file to a reviewer with a fresh context, so it does not share your reasoning:
   - Claude Code: start a subagent with a prompt like "Read <packet path> and follow its
     instructions. Reply with the JSON only." and save the reply as `critic/round-N.json`.
   - Codex or other hosts: run a separate non-interactive session (for example
     `codex exec` or `claude -p`) on the packet, if available.
   - With no fresh context available, review the packet yourself and note "same-context critic"
     in the round's `note` field; the audit will show it.
3. `psb critic check` validates the round: a verdict for all six domains, allowed values, and every
   earlier open finding carried forward by its ID, a current evidence binding, and dispositions
   for every mandatory diagnostic review. It returns nonzero while blocking findings remain.

## The six domains

| Key | PRESS element | Ask |
|---|---|---|
| `translation` | Translation of the question | Do the AND-ed blocks match the concepts? Is anything AND-ed that should be screened? Is every member the criteria name searched by its bare name? Does a block require one direction of a process? (`scope.md`) |
| `operators` | Boolean and proximity operators | Are OR and AND used correctly? Any NOT? Proximity distances sensible? |
| `subject_headings` | Subject headings | Right descriptors, explosion, missing narrower or related headings, supplementary concepts? |
| `text_words` | Text-word searching | Missing synonyms, spellings, plurals, acronyms; truncation too short or too broad? |
| `syntax` | Spelling, syntax, line numbers | Field tags, quotes, parentheses, translation warnings? |
| `limits_filters` | Limits and filters | Is each limit justified, validated, and tested for lost records? |

## Finding fields

`id` (stable across rounds), `domain`, `severity` (`must-fix`, `should-fix`, `document`), `kind`,
`block`, `finding`, `recommendation`, `status` (`open`, `resolved`, `rejected`, `accepted-risk`),
and `response` (required for every non-open status, including `resolved`).

Copy `review_sha256` from the packet. Never copy a binding from another evaluation. The
`issue_dispositions` array addresses each `validation.review_required` issue by `issue_id`,
with `status` (`accepted-risk` or `rejected`), `response`, and `evidence`. Phrase issues also
require the exact `query` and `translation` shown in the packet. A generic "query works" is
not evidence. Fixes/removals require a new evaluation; an issue still present cannot be marked
resolved to bypass review. Technical blockers are independent of all critic dispositions.
Read `validation.md` for the phrase-review decision tree.

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
finding's `status` and `response` in the next round's file. Stop when no substantive (`must-fix` or `should-fix`) finding is open; accepted risks need
explanations. List remaining documentation findings in the audit. Every depth requires review;
quick/standard/thorough allow 1/2/3 revision rounds, then one closing round. Make all planned
changes before the last revision round, and check them with `psb report --diagnostic`. `psb status`
shows the rounds left (`critic_rounds_left`). `psb critic packet` refuses the last revision round,
the closing round and the verification round while the latest evaluation has technical blockers,
which no critic round can clear: fix them and `psb eval` first. `--anyway` issues the round regardless;
use it only when you know the blocker will not reach `psb report`.

## Closing round

When the revision rounds are used, `psb critic packet` issues a closing round (`"closing": true`).
Its reviewer verifies how each earlier finding was handled in the current strategy: resolved,
rejected or accepted-risk with a response, or still open with the domain at `revise`. It may not
raise a new `must-fix` or `should-fix` finding (`psb critic check` rejects one); a new concern is
recorded as `document`. A closing round must be the last round. After it, only an open `must-fix`
finding blocks delivery: an open `should-fix` finding is delivered as a documented open concern
(list it in `narrative.md` for the peer reviewer). Historical unbound rounds remain readable but
do not authorize delivery.

## After the closing round

- **A change after the closing round.** If you fix a closing-round finding, or change anything
  else the critic reviewed, `psb critic packet` issues one verification round (also
  `"closing": true`, same rules). Nothing may follow it. Editing only `notes` or
  `scope_confirmed` never needs a critic round: run `psb report` again.
- **An open must-fix you disagree with.** For a `lexical`, `structural`, `scope` or `reporting`
  finding, `psb critic override <id> --reason "..."` records why the finding is wrong for this
  search, with the evidence (counts, known records, loss samples). `psb report` then delivers,
  and the audit opens with "Delivered over an open critic objection" for the peer reviewer.
  Use it for a disagreement on evidence, never to skip work you could do. A `syntax` or
  `filter` finding cannot be overridden, nor can any technical blocker. An override answers one
  round: after a verification round, make it again if the finding is still open.
- **Stale after the verification round, with nothing changed.** `psb report` re-evaluates live, so
  PubMed's translation or a development record gaining indexing can make the review stale after the
  last round. Explain this to the user. Only if they explicitly ask for it, `psb critic extend --reason
  "..."` opens one more review period (one revision round, then a closing round and a verification
  round), once per build; it never touches held-out records. Never run it on your own initiative: it
  has the same standing as `--proceed-default`. The audit discloses it on its first page.
- Otherwise deliver the diagnostic handoff.

## Repair after the held-out test

The held-out test never asks the critic for anything: misses are delivered unchanged with a repair
offer. If the user asks for the repair, `psb holdout-release` starts a new **epoch**. Its rounds carry
`"epoch": N` (the packet's template includes it) and are counted afresh: one revision round, then a
closing round, and one verification round, at every depth. Earlier findings carry forward as usual.
The packet marks the review as a repair review. A review extension (`psb critic extend`) is also an
epoch with this budget, marked as an extension; a repair after it starts the next epoch.
