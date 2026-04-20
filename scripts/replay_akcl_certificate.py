#!/usr/bin/env python3
import json
from pathlib import Path

from src.kernel.akcl_syn_certificate import AKCLConfig, run_loop, run_once


def main() -> None:
    default = run_once(AKCLConfig())
    restart = run_loop(
        AKCLConfig(packet_count=9, packet_sigma=0.4, t_max=16.0, t_count=81),
        max_rounds=6,
    )
    artifact = {
        "c0": default["c0"],
        "eta": default["eta"],
        "status": default["status"],
        "default_pass": default,
        "hard_start_then_restart": restart,
    }
    out = Path("experiments/akcl_ci_artifact.json")
    out.write_text(json.dumps(artifact, indent=2))
    print(json.dumps({"artifact": str(out), "c0": default["c0"], "eta": default["eta"], "status": default["status"]}, indent=2))


if __name__ == "__main__":
    main()
