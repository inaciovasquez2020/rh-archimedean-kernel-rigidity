# Executable Artifact Surface 2026-04

## Status
CONDITIONAL

## Scope
This note upgrades repository scaffolding / executable artifact maturity only.
It does not change the AKCL mathematical frontier.

## Required executable surface
1. Root packaging metadata:
   - `pyproject.toml`
   - `requirements.txt`

2. Stable local entrypoints:
   - `make install`
   - `make test`
   - `make verify`
   - `make surface`
   - `make repo-check`

3. Stable repository check:
   - `scripts/run_repo_check.sh`

4. Surface-truth tests:
   - `tests/test_repo_surface.py`

## Verified commands
```sh
python3 -m pytest -q
python3 infra/ci/verify_certificate.py
sh scripts/run_repo_check.sh
Frontier honesty
The repository remains mathematically conditional until the genuine theorem-level function-space realization and explicit coercivity/defect certificate are proved repository-natively.
Finish condition
Replace `CONDITIONAL` by `PROVED` only after the root executable surface is present and repository-native tests enforce it.
