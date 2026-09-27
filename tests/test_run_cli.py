import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "evals"))

import run  # noqa: E402


def test_anon_dir_never_contains_the_readable_topic_id():
    for topic in ("Bos_2018", "CD011926", "gao-2026-Immune checkpoint inhibitors"):
        name = run.anon_dir(topic)
        assert topic.lower() not in name.lower()
        assert all(word.lower() not in name.lower() for word in topic.replace("-", " ").replace("_", " ").split())


def test_anon_dir_is_deterministic_and_distinct_per_topic():
    assert run.anon_dir("Bos_2018") == run.anon_dir("Bos_2018")
    assert run.anon_dir("Bos_2018") != run.anon_dir("CD011926")
