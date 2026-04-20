# AKCL Mixed Energy Leakage Open Problem (2026-04)

## Status
OPEN

## Target
Let P be the orthogonal projection onto the certified packet block V_cert and let Q := I - P.

Prove that there exists an explicit constant kappa_E < 1 such that for all f in the packet core C,
\[
|\mathcal E[Pf,Qf]|
\le
\kappa_E\,\mathcal E[Pf]^{1/2}\mathcal E[Qf]^{1/2}.
\]

## Minimal input
A repository-native proof must identify the exact quadratic-form or operator mechanism controlling the mixed energy term between V_cert and V_cert^\perp.

## Consequence
This is item (3) in the AKCL global rigidity upgrade and is required for block-matrix domination of the full energy form.

## Finish condition
Replace OPEN by PROVED only after repository-native proof or certified explicit bound supplies a concrete value or formula for kappa_E.
