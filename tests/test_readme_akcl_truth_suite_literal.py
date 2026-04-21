from pathlib import Path

def test_readme_akcl_truth_suite_literal():
    s = Path("README.md").read_text()
    assert "## AKCL truth suite" in s
    assert "make akcl-truth" in s
