from pathlib import Path

def test_readme_akcl_index_entrypoint_literal():
    s = Path("README.md").read_text()
    assert "## AKCL index" in s
    assert "docs/rigidity/rh/INDEX.md" in s
    assert "make akcl-truth" in s
