# AKCL Conditional Exact Defect Functional (2026-04)

## Status
Conditional.

## Standing model assumption
Let
\[
M_D\in\mathbb R^{m\times m}
\]
be the matrix `D_matrix` exported in
`experiments/akcl_declared_pair.json`.

## Exact theorem-level defect functional
For every
\[
a\in\mathcal A_{\mathrm{AKCL}}=\mathbb R^m,
\]
define
\[
\operatorname{Def}_{\mathrm{AKCL}}[a]:=a^\top M_D a.
\]

## Finish condition
This functional is exact only under the standing model assumption above.
