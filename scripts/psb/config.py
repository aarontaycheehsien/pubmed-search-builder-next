"""Configuration: process environment first, then the `.env` file at the skill root.

Only allowlisted names are read from the file, and the working directory is never searched,
so a stray `.env` in a run workspace cannot redirect the tools.
"""

from __future__ import annotations

import os
import re
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_ENV_FILE = SKILL_ROOT / ".env"
ALLOWED = frozenset({"NCBI_EMAIL", "NCBI_API_KEY", "NCBI_TOOL", "PSB_CACHE"})
_KEY = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")

_env_file: Path = DEFAULT_ENV_FILE
_file_values: dict[str, str] | None = None


def parse_env_file(path: Path) -> dict[str, str]:
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except OSError:
        return {}
    values: dict[str, str] = {}
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.startswith("export "):
            line = line[len("export "):].strip()
        key, value = (part.strip() for part in line.split("=", 1))
        if not _KEY.fullmatch(key) or key not in ALLOWED:
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
            value = value[1:-1]
        values[key] = value
    return values


def use_env_file(path: str | Path | None) -> None:
    """Point configuration at an explicit env file (None restores the skill-root default)."""
    global _env_file, _file_values
    _env_file = Path(path).expanduser().resolve() if path else DEFAULT_ENV_FILE
    _file_values = None


def read_env(name: str, default: str = "") -> str:
    global _file_values
    value = os.environ.get(name)
    if value:
        return value
    if _file_values is None:
        _file_values = parse_env_file(_env_file)
    return _file_values.get(name) or default
