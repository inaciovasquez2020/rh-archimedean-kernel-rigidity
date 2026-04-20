# Intended Defect Functional Lock (2026-04)

## Status
Conditional.

## Declared executable family
Fix `AKCLConfig = (u_min,u_max,n_grid,alpha,packet_count,packet_sigma,center_min,center_max,t_max,t_count,defect_t_max,defect_t_count,defect_eps,defect_envelope_decay)` and let
\[
x_j = e^{u_j}, \qquad q_j = x_j\,\Delta u, \qquad w(x)=e^{-x}x^\alpha .
\]

Let the neutral mode be
\[
n(x_j)=\frac{\sqrt{w(x_j)q_j}}{\left(\sum_\ell w(x_\ell)q_\ell\right)^{1/2}} .
\]

Let \(B=[b_1,\dots,b_m]\) be the orthonormalized packet family obtained from
\[
\widetilde b_r(u)=\exp\!\left(-\frac{(u-c_r)^2}{2\sigma^2}\right)
\]
after projection away from \(n\).

## Exact defect features
For each defect parameter \(\tau\) in the declared defect grid and with
\[
\varepsilon := \texttt{defect\_eps}, \qquad \gamma := \texttt{defect\_envelope\_decay},
\]
define the raw defect column
\[
\widetilde\psi_\tau(x_j)
=
\sqrt{w(x_j)q_j}\,
x_j^{\varepsilon+i\tau}\,
e^{-\gamma \tau^2}.
\]

Define the centered defect column
\[
\psi_\tau
=
\widetilde\psi_\tau
-
\langle n,\widetilde\psi_\tau\rangle n .
\]

Let \(\Psi\) be the matrix whose columns are the \(\psi_\tau\). Define
\[
G_{\Psi}:=\Psi\Psi^*,
\qquad
D:=B^\top \operatorname{Re}(G_{\Psi}) B .
\]

## Exact intended defect functional on the declared family
For every coefficient vector \(a\in\mathbb R^m\), define
\[
\operatorname{Def}_{\mathrm{AKCL,decl}}(a)
:=
a^\top D a .
\]

Equivalently, for the packet superposition
\[
f_a := \sum_{r=1}^m a_r b_r ,
\]
the declared-family defect functional is exactly the quadratic form
\[
\operatorname{Def}_{\mathrm{AKCL,decl}}[f_a]
=
a^\top D a .
\]

## Lock condition
Do not replace this lock by a theorem-level defect functional until the declared-family quadratic form above is transferred to the intended Archimedean admissible class.
