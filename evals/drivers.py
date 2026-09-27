"""Run a skill headlessly with Claude Code or Codex in an isolated directory.

The run directory holds only a copy of the skill and the agent's own work. The answer key never
enters it. ``PSB_AS_OF`` pins every `psb` PubMed search to the fixture's date.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

SKILL_ITEMS = ("SKILL.md", "scripts", "references", ".env")


def stage_skill(skill_dir: Path, run_dir: Path) -> Path:
    target = run_dir / "skill"
    target.mkdir(parents=True)
    for name in os.listdir(skill_dir):
        source = skill_dir / name
        if name.startswith(".") and name != ".env":
            continue
        if name in {"evals", "tests", "runs", "__pycache__"}:
            continue
        if source.is_dir():
            shutil.copytree(source, target / name, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".cache"))
        else:
            shutil.copy2(source, target / name)
    return target


def kill_tree(process: subprocess.Popen) -> None:
    if os.name == "nt":
        subprocess.run(["taskkill", "/PID", str(process.pid), "/T", "/F"], capture_output=True)
    else:
        process.kill()


def run_process(cmd: list[str], *, prompt: str, cwd: Path, env: dict, timeout: int, stdout_path: Path) -> dict:
    started = time.monotonic()
    with stdout_path.open("wb") as out, (cwd.parent / f"{cwd.name}.stderr.txt").open("wb") as err:
        process = subprocess.Popen(cmd, cwd=cwd, env=env, stdin=subprocess.PIPE, stdout=out, stderr=err)
        try:
            process.communicate(prompt.encode("utf-8"), timeout=timeout)
            timed_out = False
        except subprocess.TimeoutExpired:
            kill_tree(process)
            process.wait()
            timed_out = True
    return {"returncode": process.returncode, "timed_out": timed_out, "seconds": round(time.monotonic() - started)}


def find(executable: str) -> str:
    found = shutil.which(executable) or shutil.which(executable + ".cmd")
    if not found:
        raise FileNotFoundError(f"{executable} not found on PATH")
    return found


def run_claude(prompt: str, run_dir: Path, *, env: dict, timeout: int, model: str | None = None) -> dict:
    cmd = [
        find("claude"), "-p", "--output-format", "json",
        "--dangerously-skip-permissions",
        "--setting-sources", "project",
        "--strict-mcp-config", "--mcp-config", json.dumps({"mcpServers": {}}),
        "--disallowedTools", "WebSearch", "WebFetch",
    ]
    if model:
        cmd += ["--model", model]
    result = run_process(cmd, prompt=prompt, cwd=run_dir, env=env, timeout=timeout, stdout_path=run_dir / "transcript.json")
    try:
        data = json.loads((run_dir / "transcript.json").read_text(encoding="utf-8"))
        result.update(
            cost_usd=data.get("total_cost_usd"),
            turns=data.get("num_turns"),
            usage=data.get("usage"),
            final_message=str(data.get("result", ""))[-2000:],
            is_error=data.get("is_error"),
        )
    except (OSError, ValueError):
        pass
    return result


def run_codex(prompt: str, run_dir: Path, *, env: dict, timeout: int, model: str | None = None,
              effort: str = "medium") -> dict:
    cmd = [
        find("codex"), "exec", "-C", str(run_dir), "-s", "workspace-write",
        "-c", "approval_policy=never",
        "-c", "sandbox_workspace_write.network_access=true",
        "-c", f"model_reasoning_effort={effort}",
        "--skip-git-repo-check", "--color", "never", "--json",
        "-o", str(run_dir / "last_message.txt"), "-",
    ]
    if model:
        cmd[2:2] = ["-m", model]
    result = run_process(cmd, prompt=prompt, cwd=run_dir, env=env, timeout=timeout, stdout_path=run_dir / "transcript.jsonl")
    last = run_dir / "last_message.txt"
    if last.exists():
        result["final_message"] = last.read_text(encoding="utf-8", errors="replace")[-2000:]
    return result


DRIVERS = {"claude": run_claude, "codex": run_codex}


def prompt_for(fixture: dict, *, seeds: list[str], depth: str) -> str:
    eligibility = ""
    if fixture.get("eligibility"):
        eligibility = "Eligibility criteria:\n" + "\n".join(f"- {item}" for item in fixture["eligibility"]) + "\n"
    known = (f"Known relevant articles (PMIDs): {', '.join(seeds)}" if seeds
             else "I don't have any known relevant articles.")
    return f"""You are testing a skill for building PubMed search strategies. The skill is in ./skill:
read ./skill/SKILL.md and follow it. Run the skill's scripts from this directory.

The user's request:

\"\"\"
Please build a high-sensitivity PubMed search strategy for my systematic review.

Question: {fixture['question']}
{eligibility}{known}

Use {depth} depth. I can't answer questions during this run, so don't wait for me: make
reasonable decisions, record your assumptions, and carry on to the end.
\"\"\"

Harness rules:
- Keep all working files in ./work (use it as the workspace directory).
- Work as if today were {fixture.get('as_of') or 'the present'}: do not use web search, and do not use
  literature added to PubMed after that date. The harness pins PubMed to that date through the
  PSB_AS_OF environment variable (an Entrez-date bound); leave it set for every command. Do not
  add a publication-date ([dp]) limit for the cutoff: it drops records that were already in
  PubMed but carry a later publication date.
- If the skill generates a protected final-query.txt and validation manifest, finish through its
  report command and leave those generated files intact in ./work. Do not hand-author a substitute
  query when validation is blocked. For a skill without protected delivery, write the final PubMed
  query as a single line to ./final_strategy.txt.
"""
