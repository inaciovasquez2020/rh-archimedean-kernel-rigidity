from pathlib import Path

ROOT = Path("docs/rigidity/rh")

FILES = [
    "AKCL_GLOBAL_RIGIDITY_UPGRADE_OPEN_PROBLEM_2026_04.md",
    "AKCL_GLOBAL_RIGIDITY_UPGRADE_REGISTRY_2026_04.md",
    "AKCL_COMPLEMENT_COERCIVITY_OPEN_PROBLEM_2026_04.md",
    "AKCL_COMPLEMENT_DEFECT_DOMINANCE_OPEN_PROBLEM_2026_04.md",
    "AKCL_MIXED_ENERGY_LEAKAGE_OPEN_PROBLEM_2026_04.md",
    "AKCL_MIXED_DEFECT_LEAKAGE_OPEN_PROBLEM_2026_04.md",
    "AKCL_SPECTRAL_RADIUS_VERIFICATION_OPEN_PROBLEM_2026_04.md",
]

def test_akcl_global_rigidity_upgrade_truth_sync():
    contents = {}
    for name in FILES:
        path = ROOT / name
        assert path.exists(), f"missing file: {path}"
        contents[name] = path.read_text()

    assert "## Status\nOPEN" in contents["AKCL_GLOBAL_RIGIDITY_UPGRADE_OPEN_PROBLEM_2026_04.md"]
    assert "## Status\nOPEN" in contents["AKCL_GLOBAL_RIGIDITY_UPGRADE_REGISTRY_2026_04.md"]

    for name in FILES[2:]:
        assert "## Status\nOPEN" in contents[name]
        assert name in contents["AKCL_GLOBAL_RIGIDITY_UPGRADE_REGISTRY_2026_04.md"]

    assert "all five registry items are PROVED" in contents["AKCL_GLOBAL_RIGIDITY_UPGRADE_REGISTRY_2026_04.md"]
    assert "global rigidity upgrade" in contents["AKCL_GLOBAL_RIGIDITY_UPGRADE_OPEN_PROBLEM_2026_04.md"].lower()
