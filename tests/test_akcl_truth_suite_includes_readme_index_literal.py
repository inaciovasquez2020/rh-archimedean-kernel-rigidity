from pathlib import Path

def test_akcl_truth_suite_includes_readme_index_literal():
    s = Path("scripts/run_akcl_truth_suite.sh").read_text()
    assert "tests/test_readme_akcl_index_entrypoint_literal.py" in s
