# AKCL Basis-to-Class Density Lemma (2026-04)

## Status
OPEN

## Lemma target
Let \(\mathcal P_{\mathrm{AKCL}}\) be the union of all declared packet families produced by the admissible
AKCL parameter sets, and let \(\mathcal A_{\mathrm{AKCL}}\) be the intended Archimedean admissible class.

Prove that \(\mathcal P_{\mathrm{AKCL}}\) is dense in \(\mathcal A_{\mathrm{AKCL}}\) in the norm relevant for the
theorem-level energy functional:
\[
\forall f\in \mathcal A_{\mathrm{AKCL}},\ \forall \varepsilon>0,\ \exists g\in \mathcal P_{\mathrm{AKCL}}
\text{ such that } \|f-g\|_{\mathcal A_{\mathrm{AKCL}}}<\varepsilon .
\]

## Role in the transfer chain
This is Obligation 1 from
`docs/rigidity/rh/AKCL_TRANSFER_OBLIGATIONS_REGISTRY_2026_04.md`.

## Exact missing objects
1. The precise theorem-level norm \(\|\cdot\|_{\mathcal A_{\mathrm{AKCL}}}\).
2. The exact definition of the intended admissible class \(\mathcal A_{\mathrm{AKCL}}\).
3. The admissible parameter family generating \(\mathcal P_{\mathrm{AKCL}}\).
4. A constructive approximation scheme from packet families to arbitrary class elements.

## Finish condition
Replace `OPEN` by `PROVED` only after the repository contains:
1. an exact definition file for \(\mathcal A_{\mathrm{AKCL}}\);
2. an exact definition file for \(\|\cdot\|_{\mathcal A_{\mathrm{AKCL}}}\);
3. a proof or certified approximation procedure establishing the density statement above.
