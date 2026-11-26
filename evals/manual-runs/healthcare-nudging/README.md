# Manual runs: healthcare-nudging (held-out)

Interactive builds with `psb`, scored afterwards with
`python evals/run.py score healthcare-nudging --strategy-file ... --heldout`.

They are not `run.py generate` runs: the agent was not isolated from the repository and a user
made scope decisions along the way, so they are kept out of `evals/results/` and are not counted
by `run.py report`. Following the held-out rules, only the strategy and the score are kept: no
audit, narrative, missed records or final message.
