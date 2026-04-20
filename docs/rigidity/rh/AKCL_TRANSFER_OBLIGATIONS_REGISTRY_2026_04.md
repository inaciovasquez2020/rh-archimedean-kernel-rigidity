# AKCL Transfer Obligations Registry (2026-04)

## Status
OPEN

## Source object
The declared-family pair \((E,D)\) and the numerical invariants \((c_0,\eta)\) exported in
`experiments/akcl_declared_pair.json`.

## Unique transfer target
Lift the declared-family inequalities
\[
a^\top E a \ge c_0 \|a\|_2^2,
\qquad
a^\top D a \le \eta\, a^\top E a
\]
to the theorem-level inequalities
\[
E[f]\ge c_0^\ast \|f\|^2,
\qquad
\operatorname{Def}_{\mathrm{AKCL}}[f]\le \eta^\ast E[f],
\qquad
0\le \eta^\ast < 1
\]
on the intended Archimedean admissible class.

## Remaining obligations
1. Basis-to-class density lemma.
2. Stability of the energy form under the class completion.
3. Stability of the defect form under the class completion.
4. Uniform domination passage from declared packet families to the full admissible class.
5. Identification of theorem-level constants \((c_0^\ast,\eta^\ast)\) from the declared surrogate pair.

## Finish condition
Replace `OPEN` by `PROVED` only after each obligation above is discharged repository-natively and the transfer lemma file is proved.
