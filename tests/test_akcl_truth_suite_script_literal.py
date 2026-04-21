from pathlib import Path

def test_akcl_truth_suite_script_literal():
    p = Path("scripts/run_akcl_truth_suite.sh")
    s = p.read_text()
    assert "python3 -m pytest -q" in s
    assert "tests/test_akcl_global_rigidity_upgrade_open_problem_literal.py" in s
    assert "tests/test_akcl_complement_coercivity_open_problem_literal.py" in s
    assert "tests/test_akcl_complement_defect_dominance_open_problem_literal.py" in s
    assert "tests/test_akcl_mixed_energy_leakage_open_problem_literal.py" in s
    assert "tests/test_akcl_mixed_defect_leakage_open_problem_literal.py" in s
    assert "tests/test_akcl_spectral_radius_verification_open_problem_literal.py" in s
    assert "tests/test_akcl_global_rigidity_upgrade_registry_literal.py" in s
    assert "tests/test_akcl_global_rigidity_upgrade_truth_sync.py" in s
    assert "tests/test_akcl_completion_snapshot_literal.py" in s
    assert "tests/test_akcl_completion_truth_sync.py" in s
