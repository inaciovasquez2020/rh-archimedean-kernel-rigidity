# AKCL Conditional H_AKCL (2026-04)

## Status
Conditional.

## Standing model assumption
Use the finite declared-pair coefficient model exported in
`experiments/akcl_declared_pair.json`.

Let
\[
m:=\texttt{basis\_dimension}.
\]

## Exact theorem-level space
\[
H_{\mathrm{AKCL}}:=\mathbb R^m.
\]

## Exact inner product
For
\[
a,b\in H_{\mathrm{AKCL}},
\]
define
\[
\langle a,b\rangle_{H_{\mathrm{AKCL}}}:=\sum_{r=1}^m a_r b_r.
\]

## Exact norm
\[
\|a\|_{H_{\mathrm{AKCL}}}:=\sqrt{\langle a,a\rangle_{H_{\mathrm{AKCL}}}}=\|a\|_2.
\]

## Finish condition
This file is exact only under the standing model assumption above.
