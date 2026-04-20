# AKCL Simulated-to-Genuine Identification Open Problem (2026-04)

## Status
OPEN

## Open problem
Prove that the simulated realization
\[
(X_{\mathrm{AKCL}}^{\mathrm{sim}},\mu_{\mathrm{AKCL}}^{\mathrm{sim}},n_{\mathrm{AKCL}}^{\mathrm{sim}},H_{\mathrm{AKCL}}^{\mathrm{sim}})
\]
defined in
`docs/rigidity/rh/AKCL_SIMULATED_GENUINE_REALIZATION_CANDIDATE_2026_04.md`
is the intended genuine theorem-level realization of the AKCL framework rather than a model-induced surrogate.

## Exact theorem target
Construct exact identifications
\[
X_{\mathrm{AKCL}}=X_{\mathrm{AKCL}}^{\mathrm{sim}},
\qquad
\mu_{\mathrm{AKCL}}=\mu_{\mathrm{AKCL}}^{\mathrm{sim}},
\qquad
n_{\mathrm{AKCL}}=n_{\mathrm{AKCL}}^{\mathrm{sim}},
\qquad
H_{\mathrm{AKCL}}=H_{\mathrm{AKCL}}^{\mathrm{sim}},
\]
and prove that the theorem-level operators satisfy
\[
E_{\mathrm{AKCL}}=E_{\mathrm{AKCL}}^{\mathrm{sim}},
\qquad
D_{\mathrm{AKCL}}=D_{\mathrm{AKCL}}^{\mathrm{sim}}
\]
on a common dense domain.

## Required consequences
1. every declared packet family embeds into the genuine theorem-level space through the simulated realization;
2. the finite compression identities hold for all declared packet families;
3. the image packet family is dense in the genuine theorem-level space;
4. the constants
\[
\widetilde c_0>0,
\qquad
0\le \widetilde\eta<1
\]
transfer from the simulated model to the genuine theorem-level realization.

## Minimal missing lemma
The simulated realization is canonical:
every theorem-level AKCL realization satisfying the declared packet compression identities is unitarily equivalent to
\[
(X_{\mathrm{AKCL}}^{\mathrm{sim}},\mu_{\mathrm{AKCL}}^{\mathrm{sim}},n_{\mathrm{AKCL}}^{\mathrm{sim}},H_{\mathrm{AKCL}}^{\mathrm{sim}})
\]
and therefore induces the same quadratic forms \(E_{\mathrm{AKCL}}\) and \(D_{\mathrm{AKCL}}\).

## Finish condition
Replace `OPEN` by `PROVED` only after the canonicality lemma above is proved repository-natively.
