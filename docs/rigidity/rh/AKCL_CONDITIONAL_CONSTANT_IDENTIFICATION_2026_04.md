# AKCL Conditional Constant Identification (2026-04)

## Status
Conditional.

## Standing model assumption
Let
\[
M_E:=\texttt{E\_matrix},
\qquad
M_D:=\texttt{D\_matrix}
\]
be loaded from
`experiments/akcl_declared_pair.json`.

## Exact theorem-level constants
Define
\[
c_0^\ast:=\lambda_{\min}(M_E),
\qquad
\eta^\ast:=\lambda_{\max}\!\left(M_E^{-1/2}M_D M_E^{-1/2}\right).
\]

## Exact identification from the declared pair
These satisfy
\[
c_0^\ast=\texttt{c0},
\qquad
\eta^\ast=\texttt{eta}
\]
from
`experiments/akcl_declared_pair.json`.

## Exact consequences
For every
\[
a\in\mathbb R^m,
\]
one has
\[
E[a]\ge c_0^\ast \|a\|_2^2,
\qquad
\operatorname{Def}_{\mathrm{AKCL}}[a]\le \eta^\ast E[a].
\]

If moreover
\[
0\le \eta^\ast<1,
\]
then the finite coefficient model is coercive and defect-dominated.

## Finish condition
This identification is exact only under the standing model assumption above.
