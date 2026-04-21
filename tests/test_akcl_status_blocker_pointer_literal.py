from pathlib import Path

def test_akcl_status_blocker_pointer_literal():
    s = Path("docs/status/AKCL_STATUS.md").read_text(encoding="utf-8")
    assert "## Canonical blocker registry" in s
    assert "docs/rigidity/rh/INDEX.md" in s
