# AKCL Conditional (c0, eta) Pair (2026-04)

## Status
Conditional.

## Standing model assumption
Let
\[
M_E:=\texttt{E\_matrix},
\qquad
M_D:=\texttt{D\_matrix}
\]
from
`experiments/akcl_declared_pair.json`.

## Exact constants
Define
\[
\widetilde c_0:=\lambda_{\min}(M_E),
\qquad
\widetilde\eta:=\lambda_{\max}\!\left(M_E^{-1/2}M_D M_E^{-1/2}\right).
\]

## Exact consequences
For every
\[
a\in H_{\mathrm{AKCL}},
\]
one has
\[
E[a]\ge \widetilde c_0 \|a\|_{H_{\mathrm{AKCL}}}^2,
\qquad
\operatorname{Def}_{\mathrm{AKCL}}[a]\le \widetilde\eta\,E[a].
\]

## Exact identification
\[
\widetilde c_0=\texttt{c0},
\qquad
\widetilde\eta=\texttt{eta}
\]
from
`experiments/akcl_declared_pair.json`.

## Finish condition
This constant identification is exact only under the standing model assumption above.
