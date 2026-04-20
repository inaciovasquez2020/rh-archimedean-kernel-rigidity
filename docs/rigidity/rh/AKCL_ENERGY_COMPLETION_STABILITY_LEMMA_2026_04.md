# AKCL Energy Completion Stability Lemma (2026-04)

## Status
OPEN

## Lemma target
Let \((f_n)_{n\ge 1}\subset \mathcal P_{\mathrm{AKCL}}\) be a sequence converging to
\(f\in \mathcal A_{\mathrm{AKCL}}\) in the theorem-level norm
\(\|\cdot\|_{\mathcal A_{\mathrm{AKCL}}}\).

Prove that the theorem-level energy functional is stable under this completion:
\[
f_n \to f \text{ in } \mathcal A_{\mathrm{AKCL}}
\quad\Longrightarrow\quad
E[f_n] \to E[f].
\]

## Role in the transfer chain
This is Obligation 2 from
`docs/rigidity/rh/AKCL_TRANSFER_OBLIGATIONS_REGISTRY_2026_04.md`.

## Exact missing objects
1. The exact theorem-level energy functional \(E[\cdot]\).
2. The exact theorem-level norm \(\|\cdot\|_{\mathcal A_{\mathrm{AKCL}}}\).
3. A continuity or closed-form extension argument for \(E\) on the completion.
4. A repository-native proof or certified verifier for the convergence implication above.

## Finish condition
Replace `OPEN` by `PROVED` only after the repository contains:
1. an exact formula-level definition of \(E[\cdot]\);
2. an exact formula-level definition of \(\|\cdot\|_{\mathcal A_{\mathrm{AKCL}}}\);
3. a proof or certified verifier establishing completion stability of the energy functional.
