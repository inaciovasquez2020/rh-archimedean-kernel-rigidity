from pathlib import Path

def test_akcl_spectral_radius_verification_open_problem_literal():
    p = Path("docs/rigidity/rh/AKCL_SPECTRAL_RADIUS_VERIFICATION_OPEN_PROBLEM_2026_04.md")
    s = p.read_text()
    assert "## Status\nOPEN" in s
    assert "rho\\!\\left(A^{-1/2}BA^{-1/2}\\right)<1" in s
    assert "2\\times 2" in s
    assert "Finish condition" in s
