# Coercivity Gap Note (2026-04)

## Status
Conditional.

## Repository-compatible boundary
This repository already contains:
1. a core Archimedean kernel coercivity note;
2. kernel / energy computation code;
3. a basic nonnegativity test.

The README states the target implication:
\[
E[f] \ge c_0 \|f\|^2,
\qquad
\operatorname{Def}(f)\le \eta E[f],\ \eta<1
\Longrightarrow
\text{rigidity closure} \Longrightarrow \mathrm{RH}.
\]

Thus the weakest current missing object is not a new framework, but an explicit coercivity-plus-defect certificate.

## Weakest sufficient missing theorem
The weakest sufficient theorem is:

There exist explicit constants
\[
c_0>0,\qquad 0\le \eta<1
\]
and an admissible function class
\[
\mathcal F
\]
such that for all
\[
f\in\mathcal F,
\]
one has
\[
E[f]\ge c_0\|f\|^2
\]
and
\[
\operatorname{Def}(f)\le \eta E[f].
\]

## Minimal next artifact
The weakest next artifact is an executable certificate emitter producing:
1. the declared function class \(\mathcal F\);
2. the numerical or symbolic candidate \(c_0\);
3. the numerical or symbolic candidate \(\eta\);
4. a replayable verification script checking
   \[
   E[f]\ge c_0\|f\|^2,\qquad \operatorname{Def}(f)\le \eta E[f]
   \]
   on the repository’s supported test family.

## Label
This note is CONDITIONAL.
It isolates the current coercivity/defect gap already identified by the repository goal.
