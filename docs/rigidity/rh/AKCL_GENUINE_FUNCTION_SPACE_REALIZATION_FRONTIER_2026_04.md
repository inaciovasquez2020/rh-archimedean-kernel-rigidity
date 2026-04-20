# AKCL Genuine Function-Space Realization Frontier (2026-04)

## Status
OPEN

## Replacement target
Replace the standing finite declared-pair coefficient model by a genuine theorem-level function-space realization.

## Exact target package
Construct exact theorem-level objects
\[
X_{\mathrm{AKCL}},
\qquad
\mu_{\mathrm{AKCL}},
\qquad
n_{\mathrm{AKCL}},
\qquad
H_{\mathrm{AKCL}}\subset L^2(X_{\mathrm{AKCL}},\mu_{\mathrm{AKCL}}),
\]
\[
\|\cdot\|_{H_{\mathrm{AKCL}}},
\qquad
J_\theta:\mathbb R^{m(\theta)}\to H_{\mathrm{AKCL}},
\qquad
E_{\mathrm{AKCL}},
\qquad
D_{\mathrm{AKCL}}.
\]

## Exact realization conditions
1. \(H_{\mathrm{AKCL}}\) is given by an exact formula-level definition.
2. \(n_{\mathrm{AKCL}}\) is given by an exact neutral-mode formula.
3. Each packet family embeds by an exact linear map \(J_\theta\).
4. The theorem-level quadratic forms satisfy finite compression identities.
5. Embedded packet images are dense in \(H_{\mathrm{AKCL}}\).
6. The constants \((\widetilde c_0,\widetilde\eta)\) transfer from the realized operators.

## Finite compression identities
For every declared packet basis \((b^{(\theta)}_1,\dots,b^{(\theta)}_{m(\theta)})\),
\[
(M_E^{(\theta)})_{ij}
=
\langle J_\theta e_i,\ E_{\mathrm{AKCL}} J_\theta e_j\rangle_{H_{\mathrm{AKCL}}},
\]
\[
(M_D^{(\theta)})_{ij}
=
\langle J_\theta e_i,\ D_{\mathrm{AKCL}} J_\theta e_j\rangle_{H_{\mathrm{AKCL}}}.
\]

## Closure target
\[
\overline{\bigcup_\theta J_\theta(\mathbb R^{m(\theta)})}^{\,\|\cdot\|_{H_{\mathrm{AKCL}}}}
=
H_{\mathrm{AKCL}}.
\]

## Constant-transfer target
There exist
\[
\widetilde c_0>0,
\qquad
0\le \widetilde\eta<1
\]
such that for every \(f\in H_{\mathrm{AKCL}}\),
\[
\langle f,E_{\mathrm{AKCL}}f\rangle_{H_{\mathrm{AKCL}}}
\ge
\widetilde c_0 \|f\|_{H_{\mathrm{AKCL}}}^2,
\]
\[
\langle f,D_{\mathrm{AKCL}}f\rangle_{H_{\mathrm{AKCL}}}
\le
\widetilde\eta\,\langle f,E_{\mathrm{AKCL}}f\rangle_{H_{\mathrm{AKCL}}}.
\]

## Finish condition
Replace `OPEN` by `PROVED` only after the standing finite declared-pair model is no longer used as the theorem-level realization.
