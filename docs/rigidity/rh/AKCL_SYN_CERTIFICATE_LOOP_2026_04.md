# AKCL Synthetic Certificate Loop (2026-04)

## Status
Conditional.

## Added artifact
This repository now contains an executable surrogate certificate loop in
`src/kernel/akcl_syn_certificate.py`.

## Declared surrogate quantities
For a finite admissible packet family \(\mathcal F_{\mathrm{syn}}\), define
\[
c_0 := \lambda_{\min}(E), \qquad
\eta := \lambda_{\max}\!\left(E^{-1/2} D E^{-1/2}\right),
\]
where \(E\) is the compressed centered energy matrix and \(D\) is the compressed defect matrix.

## Restart rule
If a run fails, the loop imputes the weakest next missing ingredient and reruns:
1. packet-rank deficiency \(\Rightarrow\) reduce admissible family dimension or widen the spectral family;
2. defect dominance failure \(\Rightarrow\) impose an envelope, reduce packet count, widen packets, or reduce off-critical shift.

## Conditional boundary
A passing surrogate run is not the theorem-level Archimedean coercivity proof.
It is a repository-native certificate search layer for the explicit missing object
already isolated in `COERCIVITY_GAP_NOTE_2026_04.md`.

## Finish condition
Replace `Conditional.` by `Proved.` only after the intended Archimedean defect functional
for the intended admissible class satisfies
\[
E[f] \ge c_0 \|f\|^2,
\qquad
\operatorname{Def}(f) \le \eta E[f],
\qquad
0 \le \eta < 1
\]
with a replayable verifier in the repository.
