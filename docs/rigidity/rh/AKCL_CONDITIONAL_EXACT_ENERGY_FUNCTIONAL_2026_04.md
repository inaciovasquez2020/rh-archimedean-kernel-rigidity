# AKCL Conditional Exact Energy Functional (2026-04)

## Status
Conditional.

## Standing model assumption
Let
\[
M_E\in\mathbb R^{m\times m}
\]
be the matrix `E_matrix` exported in
`experiments/akcl_declared_pair.json`.

## Exact theorem-level energy functional
For every
\[
a\in\mathcal A_{\mathrm{AKCL}}=\mathbb R^m,
\]
define
\[
E[a]:=a^\top M_E a.
\]

## Finish condition
This functional is exact only under the standing model assumption above.
