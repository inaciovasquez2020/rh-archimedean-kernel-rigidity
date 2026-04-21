from pathlib import Path

def test_makefile_akcl_truth_target_literal():
    s = Path("Makefile").read_text()
    assert ".PHONY: akcl-truth" in s
    assert "akcl-truth:" in s
    assert "./scripts/run_akcl_truth_suite.sh" in s
