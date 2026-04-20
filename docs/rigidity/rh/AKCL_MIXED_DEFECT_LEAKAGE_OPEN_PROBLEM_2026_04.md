# AKCL Mixed Defect Leakage Open Problem (2026-04)

## Status
OPEN

## Target
Let P be the orthogonal projection onto the certified packet block V_cert and let Q := I - P.

Prove that there exists an explicit constant kappa_D >= 0 such that for all f in the packet core C,
\[
|\mathcal D[Pf,Qf]|
\le
\kappa_D\,\mathcal E[Pf]^{1/2}\mathcal E[Qf]^{1/2}.
\]

## Minimal input
A repository-native proof must identify the exact quadratic-form or operator mechanism controlling the mixed defect term between V_cert and V_cert^\perp.

## Consequence
This is item (4) in the AKCL global rigidity upgrade and is required for block-matrix domination of the full defect form.

## Finish condition
Replace OPEN by PROVED only after repository-native proof or certified explicit bound supplies a concrete value or formula for kappa_D.
