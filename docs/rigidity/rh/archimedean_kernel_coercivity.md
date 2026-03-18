# Archimedean Kernel Coercivity Lemma (AKCL)

## Statement

Let
K(x,y) be the Euler–Gram kernel on L^2((0,∞), w(x)dx).

Define
E[f] = ∬ K(x,y)(f(x)-f(y))^2 w(x)w(y) dx dy.

There exists c0 > 0 such that for all admissible f orthogonal to the neutral mode:

E[f] ≥ c0 ||f||^2.

## Defect Functional

Def(f) = Σ_ρ |∫ f(x)x^{ρ-1/2}w(x)dx|^2.

## Rigidity Condition

Def(f) ≤ η E[f],  with η < 1.

## Consequence

E[f] - λ Def(f) ≥ c0(1-λη)||f||^2 > 0 ⇒ RH.
