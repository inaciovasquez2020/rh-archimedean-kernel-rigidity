# AKCL Complement Coercivity Open Problem (2026-04)

## Status
OPEN

## Target
Let P be the orthogonal projection onto the certified packet block V_cert and let Q := I - P.

Prove that there exists an explicit constant c_infty > 0 such that for all f in the packet core C,
\[
\mathcal E[Qf]\ge c_\infty \|Qf\|_{H_{\mathrm{AKCL}}}^2.
\]

## Minimal input
A repository-native proof must identify the exact operator or quadratic-form mechanism that yields coercivity on V_cert^\perp.

## Consequence
This is item (1) in the AKCL global rigidity upgrade and is required for any uniform lower bound on finite packet compressions beyond the certified block.

## Finish condition
Replace OPEN by PROVED only after repository-native proof or certified explicit bound supplies a concrete value or formula for c_infty.
