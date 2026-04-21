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


def test_conditional_exact_model_artifact_matches_declared_pair():
    pair = json.loads(Path("experiments/akcl_declared_pair.json").read_text())
    exact = json.loads(Path("experiments/akcl_conditional_exact_model.json").read_text())
    E = np.array(pair["E_matrix"], dtype=float)
    D = np.array(pair["D_matrix"], dtype=float)

    c0_star = float(np.linalg.eigvalsh(E).min())
    eta_star = max_generalized_eig(D, E)

    assert abs(exact["c0_star"] - c0_star) <= 1e-12
    assert abs(exact["eta_star"] - eta_star) <= 1e-12
    assert abs(exact["identified_from_declared_pair"]["c0"] - pair["c0"]) <= 1e-12
    assert abs(exact["identified_from_declared_pair"]["eta"] - pair["eta"]) <= 1e-12
    assert exact["coercive"] is True
    assert exact["defect_dominated"] is True


def test_conditional_exact_docs_literals_present():
    checks = {
        "docs/rigidity/rh/AKCL_CONDITIONAL_EXACT_ADMISSIBLE_CLASS_2026_04.md": [
            "Conditional.",
            "\\mathcal A_{\\mathrm{AKCL}}:=\\mathbb R^m",
        ],
        "docs/rigidity/rh/AKCL_CONDITIONAL_EXACT_NORM_2026_04.md": [
            "\\|a\\|_{\\mathcal A_{\\mathrm{AKCL}}}:=\\|a\\|_2",
        ],
        "docs/rigidity/rh/AKCL_CONDITIONAL_EXACT_ENERGY_FUNCTIONAL_2026_04.md": [
            "E[a]:=a^\\top M_E a",
        ],
        "docs/rigidity/rh/AKCL_CONDITIONAL_EXACT_DEFECT_FUNCTIONAL_2026_04.md": [
            "\\operatorname{Def}_{\\mathrm{AKCL}}[a]:=a^\\top M_D a",
        ],
        "docs/rigidity/rh/AKCL_CONDITIONAL_BASIS_TO_CLASS_DENSITY_2026_04.md": [
            "\\overline{\\mathcal P_{\\mathrm{AKCL}}}^{\\,\\|\\cdot\\|_{\\mathcal A_{\\mathrm{AKCL}}}}",
        ],
        "docs/rigidity/rh/AKCL_CONDITIONAL_ENERGY_COMPLETION_STABILITY_2026_04.md": [
            "E[a_n]\\to E[a]",
        ],
        "docs/rigidity/rh/AKCL_CONDITIONAL_DEFECT_COMPLETION_STABILITY_2026_04.md": [
            "\\operatorname{Def}_{\\mathrm{AKCL}}[a_n]\\to \\operatorname{Def}_{\\mathrm{AKCL}}[a]",
        ],
        "docs/rigidity/rh/AKCL_CONDITIONAL_UNIFORM_DOMINATION_TRANSFER_2026_04.md": [
            "\\operatorname{Def}_{\\mathrm{AKCL}}[a]\\le \\eta^\\ast E[a]",
        ],
        "docs/rigidity/rh/AKCL_CONDITIONAL_CONSTANT_IDENTIFICATION_2026_04.md": [
            "c_0^\\ast:=\\lambda_{\\min}(M_E)",
            "\\eta^\\ast:=\\lambda_{\\max}",
        ],
        "docs/rigidity/rh/AKCL_CONDITIONAL_EXACT_PACKAGE_REGISTRY_2026_04.md": [
            "conditional exact package",
            "\\operatorname{Def}_{\\mathrm{AKCL}}[a]=a^\\top M_D a",
        ],
    }
    for path, patterns in checks.items():
        text = Path(path).read_text()
        for pattern in patterns:
            assert pattern in text
