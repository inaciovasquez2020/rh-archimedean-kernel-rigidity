# AKCL Simulated Genuine Realization Candidate (2026-04)

## Status
Conditional.

## Simulated exact formula-level data
Using the current AKCL synthetic certificate parameterization, define
\[
X_{\mathrm{AKCL}}^{\mathrm{sim}}:=[u_{\min},u_{\max}]\subset \mathbb R,
\qquad
d\mu_{\mathrm{AKCL}}^{\mathrm{sim}}(u):=du.
\]

Let
\[
\rho_{\alpha}(u):=\exp(-e^u)\,e^{(\alpha+1)u}.
\]

Define the simulated neutral mode
\[
n_{\mathrm{AKCL}}^{\mathrm{sim}}(u)
:=
Z^{-1/2}\exp(-e^u/2)\,e^{\frac{\alpha+1}{2}u},
\]
where
\[
Z:=\int_{u_{\min}}^{u_{\max}}\exp(-e^u)\,e^{(\alpha+1)u}\,du.
\]

Define the simulated theorem-level space
\[
H_{\mathrm{AKCL}}^{\mathrm{sim}}
:=
\left\{
f\in L^2([u_{\min},u_{\max}],du):
\int_{u_{\min}}^{u_{\max}} f(u)\,n_{\mathrm{AKCL}}^{\mathrm{sim}}(u)\,du=0
\right\}.
\]

Define the simulated theorem-level norm
\[
\|f\|_{H_{\mathrm{AKCL}}^{\mathrm{sim}}}
:=
\left(
\int_{u_{\min}}^{u_{\max}} |f(u)|^2\,du
\right)^{1/2}.
\]

## Simulated packet and feature families
Define the raw packet family
\[
p_{c,\sigma}(u):=\exp\!\left(-\frac{(u-c)^2}{2\sigma^2}\right).
\]

Define the simulated energy feature family
\[
\Phi_t^{\mathrm{sim}}(u)
:=
\exp(-e^u/2)\,e^{\left(\frac{\alpha+2}{2}+it\right)u}.
\]

Define the simulated defect feature family
\[
\Psi_{\tau,\varepsilon,\gamma}^{\mathrm{sim}}(u)
:=
\exp(-e^u/2)\,e^{\left(\frac{\alpha+1}{2}+\varepsilon+i\tau\right)u}e^{-\gamma\tau^2}.
\]

## Sampling map
For the uniform log-grid
\[
u_j=u_{\min}+j\Delta u,
\qquad
\Delta u=\frac{u_{\max}-u_{\min}}{N-1},
\]
define the sampling map
\[
S_N(f):=\bigl(f(u_j)\sqrt{\Delta u}\bigr)_{j=0}^{N-1}.
\]

## Simulated consistency claim
Under the current synthetic certificate construction, the discrete neutral vector and feature matrices are exactly the sampled versions of the formulas above up to floating-point roundoff:
\[
S_N\!\left(n_{\mathrm{AKCL}}^{\mathrm{sim}}\right)\approx \texttt{neutral\_mode},
\]
\[
S_N\!\left(\Phi_t^{\mathrm{sim}}\right)\approx \texttt{feature\_matrix column at }t,
\]
\[
S_N\!\left(\Psi_{\tau,\varepsilon,\gamma}^{\mathrm{sim}}\right)\approx \texttt{defect\_feature\_matrix column at }\tau.
\]

## Boundary
This is a simulated candidate realization generated from the current finite AKCL synthetic model. It is not yet a proved genuine theorem-level realization independent of the synthetic construction.
