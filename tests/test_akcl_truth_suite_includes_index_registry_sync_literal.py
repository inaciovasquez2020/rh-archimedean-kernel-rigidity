from pathlib import Path

def test_akcl_truth_suite_includes_index_registry_sync_literal():
    s = Path("scripts/run_akcl_truth_suite.sh").read_text()
    assert "tests/test_akcl_index_registry_sync.py" in s
