#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np


def max_generalized_eig(D: np.ndarray, E: np.ndarray, tol: float = 1e-12) -> float:
    evals, evecs = np.linalg.eigh(E)
    keep = evals > tol
    if not np.any(keep):
        return float("inf")
    Einvhalf = evecs[:, keep] @ np.diag(evals[keep] ** -0.5) @ evecs[:, keep].T
    S = Einvhalf @ D @ Einvhalf
    S = (S + S.T) * 0.5
    return float(np.linalg.eigvalsh(S).max())


def main() -> None:
    pair = json.loads(Path("experiments/akcl_declared_pair.json").read_text())
    E = np.array(pair["E_matrix"], dtype=float)
    D = np.array(pair["D_matrix"], dtype=float)

    c0_tilde = float(np.linalg.eigvalsh(E).min())
    eta_tilde = max_generalized_eig(D, E)

    out = {
        "model": "conditional_finite_theorem_level_symbols",
        "basis_dimension": int(pair["basis_dimension"]),
        "H_AKCL": "R^m",
        "norm_H_AKCL": "euclidean",
        "J_m": "identity",
        "E_AKCL": "left-multiplication by E_matrix",
        "D_AKCL": "left-multiplication by D_matrix",
        "P_AKCL_img": "H_AKCL",
        "closure_equals_H_AKCL": True,
        "c0_tilde": c0_tilde,
        "eta_tilde": eta_tilde,
        "identified_from_declared_pair": {
            "c0": float(pair["c0"]),
            "eta": float(pair["eta"]),
        },
    }

    path = Path("experiments/akcl_conditional_theorem_level_symbols.json")
    path.write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
