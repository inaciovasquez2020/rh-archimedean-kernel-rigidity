# RH Archimedean Kernel Rigidity

Archimedean Kernel Coercivity Lemma (AKCL) framework for a rigidity-based reduction of the Riemann Hypothesis.

## Contents
- docs/rigidity/rh/archimedean_kernel_coercivity.md — core lemma
- src/kernel/compute_kernel.py — kernel + energy functional
- tests/test_energy_nonnegative.py — basic verification

## Goal
Establish coercivity:
E[f] ≥ c0 ||f||^2

with defect control:
Def(f) ≤ η E[f], η < 1

⇒ rigidity closure ⇒ RH.
