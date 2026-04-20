from pathlib import Path

def test_akcl_mixed_defect_leakage_open_problem_literal():
    p = Path("docs/rigidity/rh/AKCL_MIXED_DEFECT_LEAKAGE_OPEN_PROBLEM_2026_04.md")
    s = p.read_text()
    assert "## Status\nOPEN" in s
    assert "kappa_D >= 0" in s
    assert "V_cert^\\perp" in s
    assert "Finish condition" in s
