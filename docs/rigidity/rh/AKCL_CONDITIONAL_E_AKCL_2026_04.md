# AKCL Conditional E_AKCL (2026-04)

## Status
Conditional.

## Standing model assumption
Let
\[
M_E:=\texttt{E\_matrix}
\]
from
`experiments/akcl_declared_pair.json`.

## Exact operator
Define
\[
E_{\mathrm{AKCL}}:H_{\mathrm{AKCL}}\to H_{\mathrm{AKCL}}
\]
by
\[
E_{\mathrm{AKCL}}(a):=M_E a.
\]

## Exact quadratic functional
For every
\[
a\in H_{\mathrm{AKCL}},
\]
define
\[
E[a]:=\langle a,E_{\mathrm{AKCL}}a\rangle_{H_{\mathrm{AKCL}}}=a^\top M_E a.
\]

## Finish condition
This operator is exact only under the standing model assumption above.
