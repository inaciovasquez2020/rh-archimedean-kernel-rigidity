from pathlib import Path

def test_github_workflow_akcl_truth_literal():
    s = Path(".github/workflows/akcl-truth.yml").read_text()
    assert "name: akcl-truth" in s
    assert "pull_request:" in s
    assert "push:" in s
    assert "python-version: '3.11'" in s
    assert "run: make akcl-truth" in s
