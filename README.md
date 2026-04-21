# RH Archimedean Kernel Rigidity

Archimedean Kernel Coercivity Lemma (AKCL) framework for a rigidity-based reduction of the Riemann Hypothesis.

## Contents
- docs/rigidity/rh/archimedean_kernel_coercivity.md — core lemma
- src/kernel/compute_kernel.py — kernel + energy functional
- tests/test_energy_nonnegative.py — basic verification


## Conditional note
- `docs/rigidity/rh/COERCIVITY_GAP_NOTE_2026_04.md` — conditional note isolating the explicit coercivity-plus-defect certificate still missing from the current AKCL framework.

## Goal
Establish coercivity:
E[f] ≥ c0 ||f||^2

with defect control:
Def(f) ≤ η E[f], η < 1

⇒ rigidity closure ⇒ RH.

## AKCL truth suite

Run the canonical AKCL truth lock locally with:

```bash
make akcl-truth
```

## AKCL index

Canonical AKCL status/index entrypoint:

- `docs/rigidity/rh/INDEX.md`

Run the locked truth suite with:

```bash
make akcl-truth
```
