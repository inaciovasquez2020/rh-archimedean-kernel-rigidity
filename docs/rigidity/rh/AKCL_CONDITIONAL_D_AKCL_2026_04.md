# AKCL Conditional D_AKCL (2026-04)

## Status
Conditional.

## Standing model assumption
Let
\[
M_D:=\texttt{D\_matrix}
\]
from
`experiments/akcl_declared_pair.json`.

## Exact operator
Define
\[
D_{\mathrm{AKCL}}:H_{\mathrm{AKCL}}\to H_{\mathrm{AKCL}}
\]
by
\[
D_{\mathrm{AKCL}}(a):=M_D a.
\]

## Exact quadratic functional
For every
\[
a\in H_{\mathrm{AKCL}},
\]
define
\[
\operatorname{Def}_{\mathrm{AKCL}}[a]
:=
\langle a,D_{\mathrm{AKCL}}a\rangle_{H_{\mathrm{AKCL}}}
=
a^\top M_D a.
\]

## Finish condition
This operator is exact only under the standing model assumption above.
