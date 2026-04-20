# AKCL Uniform Domination Transfer Lemma (2026-04)

## Status
OPEN

## Lemma target
Let \(f\in \mathcal A_{\mathrm{AKCL}}\). Assume there exists a sequence
\[
(f_n)_{n\ge 1}\subset \mathcal P_{\mathrm{AKCL}}
\]
such that
\[
f_n \to f
\quad\text{in}\quad
\|\cdot\|_{\mathcal A_{\mathrm{AKCL}}}.
\]

Assume moreover that for every \(n\),
\[
\operatorname{Def}_{\mathrm{AKCL}}[f_n]
\le
\eta\, E[f_n]
\]
for a constant \(0\le \eta<1\) independent of \(n\).

Prove that the same domination passes to the limit:
\[
\operatorname{Def}_{\mathrm{AKCL}}[f]
\le
\eta\, E[f].
\]

## Role in the transfer chain
This is Obligation 4 from
`docs/rigidity/rh/AKCL_TRANSFER_OBLIGATIONS_REGISTRY_2026_04.md`.

## Exact missing objects
1. The exact theorem-level energy functional \(E[\cdot]\).
2. The exact theorem-level defect functional \(\operatorname{Def}_{\mathrm{AKCL}}[\cdot]\).
3. The exact theorem-level norm \(\|\cdot\|_{\mathcal A_{\mathrm{AKCL}}}\).
4. A proof that the domination constant \(\eta\) is uniform across the approximating packet families.
5. A repository-native proof or certified verifier for the limit-passage implication above.

## Finish condition
Replace `OPEN` by `PROVED` only after the repository contains:
1. exact formula-level definitions of \(E[\cdot]\), \(\operatorname{Def}_{\mathrm{AKCL}}[\cdot]\), and \(\|\cdot\|_{\mathcal A_{\mathrm{AKCL}}}\);
2. a proof or certified verifier that the domination constant \(\eta\) is uniform on the declared approximating packet families;
3. a proof or certified verifier establishing the limit-passage implication above.
