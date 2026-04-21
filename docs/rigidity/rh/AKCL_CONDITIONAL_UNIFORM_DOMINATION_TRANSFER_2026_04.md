# AKCL Conditional Uniform Domination Transfer (2026-04)

## Status
Conditional.

## Standing model assumption
Use
\[
\mathcal A_{\mathrm{AKCL}}=\mathbb R^m,
\qquad
E[a]=a^\top M_E a,
\qquad
\operatorname{Def}_{\mathrm{AKCL}}[a]=a^\top M_D a.
\]

Define
\[
\eta^\ast:=
\lambda_{\max}\!\left(M_E^{-1/2}M_D M_E^{-1/2}\right).
\]

## Exact uniform domination statement
For every
\[
a\in\mathcal A_{\mathrm{AKCL}},
\]
one has
\[
\operatorname{Def}_{\mathrm{AKCL}}[a]\le \eta^\ast E[a].
\]

In particular, if
\[
a_n\to a
\quad\text{and}\quad
\operatorname{Def}_{\mathrm{AKCL}}[a_n]\le \eta E[a_n]
\quad\text{for all }n
\]
with
\[
0\le \eta<1,
\]
then continuity gives
\[
\operatorname{Def}_{\mathrm{AKCL}}[a]\le \eta E[a].
\]

## Finish condition
This domination statement is exact only under the standing model assumption above.
