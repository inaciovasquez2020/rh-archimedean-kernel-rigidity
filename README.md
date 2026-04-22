# RH Archimedean Kernel Rigidity

Archimedean Kernel Coercivity Lemma (AKCL) framework for a rigidity-based reduction of the Riemann Hypothesis.

## Start Here

- `QUICKSTART.md`
- `docs/SETUP_GUIDE.md`
- `docs/rigidity/rh/INDEX.md`

## What this repository is

- a focused AKCL executable artifact surface;
- a status-locked repository for the Archimedean coercivity line;
- a verification-first repository with a canonical truth suite.

## Current status

- repository scope: active executable artifact and status surface;
- theorem status: conditional, with the remaining coercivity-plus-defect certificate isolated in-repo;
- canonical truth lock: `make akcl-truth`.

## Core files

- `docs/rigidity/rh/archimedean_kernel_coercivity.md`
- `docs/rigidity/rh/COERCIVITY_GAP_NOTE_2026_04.md`
- `docs/rigidity/rh/INDEX.md`
- `src/kernel/compute_kernel.py`
- `tests/test_energy_nonnegative.py`

## Quick verification

```bash
make akcl-truth
```

## Contribution paths

- onboarding and documentation improvements;
- truth-suite and regression hardening;
- repository-surface clarifications;
- explicitly justified semantic changes only.

See `CONTRIBUTING.md`.
