#!/usr/bin/env python3
from pathlib import Path
import sys

required = [
    "README.md",
    "docs",
    "experiments",
    "infra",
    "src",
    "tests",
]

missing = [p for p in required if not Path(p).exists()]
if missing:
    print({"valid": False, "missing": missing})
    sys.exit(1)

readme = Path("README.md").read_text(errors="ignore").lower()

checks = {
    "mentions_rh": "riemann hypothesis" in readme or "rh" in readme,
    "mentions_archimedean_kernel": "archimedean kernel" in readme,
    "mentions_coercivity": "coercivity" in readme,
    "mentions_defect_control": "defect control" in readme or "defect" in readme,
    "mentions_conditional_note": "conditional note" in readme,
}

failed = [k for k, v in checks.items() if not v]
if failed:
    print({"valid": False, "failed_checks": failed, "checks": checks})
    sys.exit(1)

print({"valid": True, "checked": required, "checks": checks})
