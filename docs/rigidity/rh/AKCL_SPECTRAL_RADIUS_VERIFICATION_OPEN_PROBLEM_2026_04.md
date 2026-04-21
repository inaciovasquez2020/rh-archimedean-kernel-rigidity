# AKCL Spectral Radius Verification Open Problem (2026-04)

## Status
OPEN

## Target
Let
\[
A=
\begin{pmatrix}
1 & -\kappa_E\\
-\kappa_E & 1
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
\eta_0 & \kappa_D\\
\kappa_D & \eta_\infty
\end{pmatrix}.
\]

Prove that
\[
\rho\!\left(A^{-1/2}BA^{-1/2}\right)<1.
\]

## Minimal input
A repository-native proof must supply explicit certified values or formulas for \(\eta_0\), \(\eta_\infty\), \(\kappa_E\), and \(\kappa_D\), and then verify the spectral-radius inequality for the resulting \(2\times 2\) block pencil.

## Consequence
This is item (5) in the AKCL global rigidity upgrade and is the final block-matrix domination check required to conclude the infinite-dimensional AKCL upgrade from the certified block and complement/mixed estimates.

## Finish condition
Replace OPEN by PROVED only after repository-native proof or certified explicit computation verifies
\[
\rho\!\left(A^{-1/2}BA^{-1/2}\right)<1
\]
from explicit admissible constants.
