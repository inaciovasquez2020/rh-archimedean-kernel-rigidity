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

    c0_star = float(np.linalg.eigvalsh(E).min())
    eta_star = max_generalized_eig(D, E)

    artifact = {
        "model": "conditional_exact_finite_declared_pair",
        "basis_dimension": int(pair["basis_dimension"]),
        "admissible_class": "R^m",
        "norm": "euclidean",
        "energy_definition": "a^T E a",
        "defect_definition": "a^T D a",
        "c0_star": c0_star,
        "eta_star": eta_star,
        "identified_from_declared_pair": {
            "c0": float(pair["c0"]),
            "eta": float(pair["eta"]),
        },
        "coercive": bool(c0_star > 0.0),
        "defect_dominated": bool(eta_star < 1.0),
    }

    out = Path("experiments/akcl_conditional_exact_model.json")
    out.write_text(json.dumps(artifact, indent=2))
    print(json.dumps(artifact, indent=2))


if __name__ == "__main__":
    main()
