from pathlib import Path

ROOT = Path("docs/rigidity/rh")

SNAPSHOT = "AKCL_COMPLETION_SNAPSHOT_2026_04.md"
REGISTRY = "AKCL_GLOBAL_RIGIDITY_UPGRADE_REGISTRY_2026_04.md"
BLOCKERS = [
    "AKCL_COMPLEMENT_COERCIVITY_OPEN_PROBLEM_2026_04.md",
    "AKCL_COMPLEMENT_DEFECT_DOMINANCE_OPEN_PROBLEM_2026_04.md",
    "AKCL_MIXED_ENERGY_LEAKAGE_OPEN_PROBLEM_2026_04.md",
    "AKCL_MIXED_DEFECT_LEAKAGE_OPEN_PROBLEM_2026_04.md",
    "AKCL_SPECTRAL_RADIUS_VERIFICATION_OPEN_PROBLEM_2026_04.md",
]

def test_akcl_completion_truth_sync():
    snapshot = (ROOT / SNAPSHOT).read_text()
    registry = (ROOT / REGISTRY).read_text()

    assert "## Status\nOPEN" in snapshot
    assert "## Status\nOPEN" in registry
    assert "AKCL remains OPEN until all five canonical blocker files are marked PROVED." in snapshot
    assert "The AKCL infinite-dimensional upgrade remains OPEN exactly until all five registry items are PROVED." in registry

    for name in BLOCKERS:
        text = (ROOT / name).read_text()
        assert "## Status\nOPEN" in text
        assert name in snapshot
        assert name in registry
