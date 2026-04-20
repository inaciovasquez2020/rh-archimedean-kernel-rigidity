from pathlib import Path

def test_akcl_global_rigidity_upgrade_open_problem_literal():
    p = Path("docs/rigidity/rh/AKCL_GLOBAL_RIGIDITY_UPGRADE_OPEN_PROBLEM_2026_04.md")
    s = p.read_text()
    assert "## Status\nOPEN" in s
    assert "c_infty > 0" in s
    assert "eta_infty < 1" in s
    assert "kappa_E < 1" in s
    assert "kappa_D >= 0" in s
    assert "spectral-radius inequality" in s
