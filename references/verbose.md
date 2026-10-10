# Verbose progress messages

Read this only when the user has asked for more detailed progress messages, either in their first
message, in reply to the Step 1 request (which offers the choice), or later in the build.

`psb progress mode verbose` stores the preference for this run in `progress-settings.json`;
`psb progress mode standard` switches back, and `psb progress mode` shows the current setting. Set it
once: every later command reads it. It changes only the wording of messages, never what is searched,
screened, evaluated or kept private.

## What changes

Completion messages of these commands end with a short **Details:** section:

| Command | Details |
|---|---|
| `sample --purpose`, `count --purpose`, `neighbors`, `resolve` (your own discovery) | how the records were chosen, PubMed's translation, and example records |
| `mesh lookup` | the candidate headings returned, with their record types; a heading named exactly as the phrase comes first (a message appears only in verbose mode) |
| `mesh show` | the scope note, and the entry terms and narrower headings returned (a message appears only in verbose mode) |
| `terms rank` | example candidates from the ranking; none when comparison records were mined |
| `eval` | blockers, translation warnings, zero-hit terms, block coverage and ablation findings |
| `terms miss` | each missed record's failing blocks, with vocabulary from development records only |

A section has at most three rows, 80 words and 800 characters; it says how many more details were
left out. Warnings come first. Every value comes from the command's own result: "returned" means what
PubMed returned, not everything that exists, and a candidate term is not an addition until `psb eval`
shows it helps. Stage summaries, the allocation messages, the critic, the held-out test and the final
delivery keep their usual wording.

Commands run for the separate screening context never gain details: their messages stay restricted.

## Relaying

Relay `progress.text` verbatim, as always, including the Details section. If a result carries
`progress_notice` (the setting file is invalid, or details could not be prepared), the message itself
is the standard one: relay it and mention the notice once afterwards.
