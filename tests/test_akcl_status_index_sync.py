from pathlib import Path

def test_akcl_status_index_sync():
    s = Path("docs/status/AKCL_STATUS.md").read_text(encoding="utf-8")
    idx = Path("docs/rigidity/rh/INDEX.md").read_text(encoding="utf-8")
    assert "docs/rigidity/rh/INDEX.md" in s
    assert "## Status\nOPEN" in idx
    assert "blocker registry" in idx.lower()
