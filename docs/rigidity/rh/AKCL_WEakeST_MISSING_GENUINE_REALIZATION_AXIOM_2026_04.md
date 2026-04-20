# AKCL Weakest Missing Genuine Realization Axiom (2026-04)

## Status
OPEN

## Weakest missing assumption
There exists an exact formula-level measure-space realization
\[
(X_{\mathrm{AKCL}},\mu_{\mathrm{AKCL}})
\]
together with an exact neutral mode
\[
n_{\mathrm{AKCL}}\in L^2(X_{\mathrm{AKCL}},\mu_{\mathrm{AKCL}})
\]
and a closed theorem-level space
\[
H_{\mathrm{AKCL}}
:=
\left\{
f\in L^2(X_{\mathrm{AKCL}},\mu_{\mathrm{AKCL}}):
\langle f,n_{\mathrm{AKCL}}\rangle=0
\right\},
\qquad
\|f\|_{H_{\mathrm{AKCL}}}:=\|f\|_{L^2(X_{\mathrm{AKCL}},\mu_{\mathrm{AKCL}})},
\]
for which there exist theorem-level quadratic-form operators
\[
E_{\mathrm{AKCL}},
\qquad
D_{\mathrm{AKCL}}
\]
on a common dense domain in \(H_{\mathrm{AKCL}}\), and for every declared packet family parameter \(\theta\) an isometric embedding
\[
J_\theta:\mathbb R^{m(\theta)}\to H_{\mathrm{AKCL}},
\]
such that:

1. finite compression identities hold:
\[
(M_E^{(\theta)})_{ij}
=
\langle J_\theta e_i,\ E_{\mathrm{AKCL}} J_\theta e_j\rangle_{H_{\mathrm{AKCL}}},
\qquad
(M_D^{(\theta)})_{ij}
=
\langle J_\theta e_i,\ D_{\mathrm{AKCL}} J_\theta e_j\rangle_{H_{\mathrm{AKCL}}},
\]

2. embedded packet images are dense:
\[
\overline{\bigcup_\theta J_\theta(\mathbb R^{m(\theta)})}^{\,\|\cdot\|_{H_{\mathrm{AKCL}}}}
=
H_{\mathrm{AKCL}},
\]

3. declared spectral data transfer to theorem-level constants:
\[
\widetilde c_0>0,
\qquad
0\le \widetilde\eta<1,
\]
with
\[
\langle f,E_{\mathrm{AKCL}}f\rangle_{H_{\mathrm{AKCL}}}
\ge
\widetilde c_0\|f\|_{H_{\mathrm{AKCL}}}^2,
\qquad
\langle f,D_{\mathrm{AKCL}}f\rangle_{H_{\mathrm{AKCL}}}
\le
\widetilde\eta\,\langle f,E_{\mathrm{AKCL}}f\rangle_{H_{\mathrm{AKCL}}}
\]
for all \(f\in H_{\mathrm{AKCL}}\).

## Consequence
If this axiom is proved by exact formulas, then the standing finite declared-pair model is no longer needed as the theorem-level realization.

## Finish condition
Replace `OPEN` by `PROVED` only after every symbol above is given by an exact formula-level definition and the three numbered conditions are proved repository-natively.
