import json
from pathlib import Path


def test_saved_json_status_regression():
    data = json.loads(Path("experiments/akcl_syn_sample_report.json").read_text())
    assert data["default_pass"]["status"] == "PASS"
    assert data["hard_start_then_restart"]["status"] in {"PASS", "CONDITIONAL"}
