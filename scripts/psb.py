#!/usr/bin/env python3
"""Entry point: `python scripts/psb.py <command> ...` (standard library only, Python 3.10+)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from psb.cli import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
