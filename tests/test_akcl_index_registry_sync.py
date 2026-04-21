from pathlib import Path

ROOT = Path("docs/rigidity/rh")

def test_akcl_index_registry_sync():
    index = (ROOT / "INDEX.md").read_text()
    snapshot = (ROOT / "AKCL_COMPLETION_SNAPSHOT_2026_04.md").read_text()
    registry = (ROOT / "AKCL_GLOBAL_RIGIDITY_UPGRADE_REGISTRY_2026_04.md").read_text()

    assert "## Status\nOPEN" in index
    assert "AKCL_COMPLETION_SNAPSHOT_2026_04.md" in index
    assert "AKCL_GLOBAL_RIGIDITY_UPGRADE_OPEN_PROBLEM_2026_04.md" in index
    assert "AKCL_GLOBAL_RIGIDITY_UPGRADE_REGISTRY_2026_04.md" in index

    blockers = [
        "AKCL_COMPLEMENT_COERCIVITY_OPEN_PROBLEM_2026_04.md",
        "AKCL_COMPLEMENT_DEFECT_DOMINANCE_OPEN_PROBLEM_2026_04.md",
        "AKCL_MIXED_ENERGY_LEAKAGE_OPEN_PROBLEM_2026_04.md",
        "AKCL_MIXED_DEFECT_LEAKAGE_OPEN_PROBLEM_2026_04.md",
        "AKCL_SPECTRAL_RADIUS_VERIFICATION_OPEN_PROBLEM_2026_04.md",
    ]

    for name in blockers:
        assert name in index
        assert name in snapshot
        assert name in registry
