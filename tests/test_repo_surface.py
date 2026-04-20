from pathlib import Path

ROOT = Path(".")

def test_repo_surface_files_exist():
    required = [
        "pyproject.toml",
        "requirements.txt",
        "Makefile",
        "scripts/run_repo_check.sh",
        "tests/test_repo_surface.py",
        "docs/status/EXECUTABLE_ARTIFACT_SURFACE_2026_04.md",
    ]
    for rel in required:
        assert (ROOT / rel).exists(), rel

def test_repo_surface_literals():
    text = Path("docs/status/EXECUTABLE_ARTIFACT_SURFACE_2026_04.md").read_text()
    required = [
        "## Status\nCONDITIONAL",
        "`pyproject.toml`",
        "`requirements.txt`",
        "`make install`",
        "`make test`",
        "`make verify`",
        "`make surface`",
        "`make repo-check`",
        "`tests/test_repo_surface.py`",
        "genuine theorem-level function-space realization",
        "explicit coercivity/defect certificate",
        "Replace `CONDITIONAL` by `PROVED` only after",
    ]
    for needle in required:
        assert needle in text, needle

def test_makefile_targets_present():
    text = Path("Makefile").read_text()
    required = [
        "install:",
        "test:",
        "verify:",
        "surface:",
        "repo-check:",
        "$(PYTHON) infra/ci/verify_certificate.py",
        "sh scripts/run_repo_check.sh",
    ]
    for needle in required:
        assert needle in text, needle
