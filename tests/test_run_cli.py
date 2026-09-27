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


def test_find_strategy_file_prefers_root_then_falls_back_to_work(tmp_path):
    run_dir = tmp_path / "run"
    (run_dir / "work").mkdir(parents=True)
    assert run.find_strategy_file(run_dir) is None

    (run_dir / "work" / "final_strategy.txt").write_text("query one", encoding="utf-8")
    found = run.find_strategy_file(run_dir)
    assert found is not None and found.read_text(encoding="utf-8") == "query one"

    (run_dir / "final_strategy.txt").write_text("query two", encoding="utf-8")
    found = run.find_strategy_file(run_dir)
    assert found == run_dir / "final_strategy.txt" and found.read_text(encoding="utf-8") == "query two"


def test_find_strategy_file_ignores_an_empty_root_file(tmp_path):
    run_dir = tmp_path / "run"
    (run_dir / "work").mkdir(parents=True)
    (run_dir / "final_strategy.txt").write_text("   \n", encoding="utf-8")
    (run_dir / "work" / "final_strategy.txt").write_text("real query", encoding="utf-8")
    found = run.find_strategy_file(run_dir)
    assert found == run_dir / "work" / "final_strategy.txt"
