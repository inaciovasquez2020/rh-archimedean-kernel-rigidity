# AKCL Global Rigidity Upgrade Open Problem (2026-04)

## Status
OPEN

## Minimal missing lemma
Let P be the orthogonal projection onto the certified packet block V_cert and let Q := I - P.

Prove that there exist explicit constants c_infty > 0, eta_infty < 1, kappa_E < 1, and kappa_D >= 0 such that for all f in the packet core C,
\[
\mathcal E[Qf]\ge c_\infty\|Qf\|_{H_{\mathrm{AKCL}}}^2,
\qquad
\mathcal D[Qf]\le \eta_\infty\,\mathcal E[Qf],
\]
\[
|\mathcal E[Pf,Qf]|
\le
\kappa_E\,\mathcal E[Pf]^{1/2}\mathcal E[Qf]^{1/2},
\qquad
|\mathcal D[Pf,Qf]|
\le
\kappa_D\,\mathcal E[Pf]^{1/2}\mathcal E[Qf]^{1/2},
\]
and
\[
\rho\!\left(
\begin{pmatrix}
1 & -\kappa_E\\
-\kappa_E & 1
\end{pmatrix}^{-1/2}
\begin{pmatrix}
\eta_0 & \kappa_D\\
\kappa_D & \eta_\infty
\end{pmatrix}
\begin{pmatrix}
1 & -\kappa_E\\
-\kappa_E & 1
\end{pmatrix}^{-1/2}
\right)<1.
\]

## Consequence
Then there exist c_* > 0 and eta_* < 1 such that
\[
\mathcal E[f]\ge c_*\|f\|_{H_{\mathrm{AKCL}}}^2,
\qquad
\mathcal D[f]\le \eta_*\,\mathcal E[f]
\]
for all f in the closed form domain, yielding the infinite-dimensional AKCL upgrade.

## Finish condition
Replace OPEN by PROVED only after repository-native proofs provide explicit formulas or certified bounds for c_infty, eta_infty, kappa_E, kappa_D and verify the spectral-radius inequality above.
