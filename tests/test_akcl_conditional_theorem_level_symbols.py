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


def test_conditional_theorem_level_symbol_artifact_matches_declared_pair():
    pair = json.loads(Path("experiments/akcl_declared_pair.json").read_text())
    sym = json.loads(Path("experiments/akcl_conditional_theorem_level_symbols.json").read_text())
    E = np.array(pair["E_matrix"], dtype=float)
    D = np.array(pair["D_matrix"], dtype=float)

    c0_tilde = float(np.linalg.eigvalsh(E).min())
    eta_tilde = max_generalized_eig(D, E)

    assert sym["H_AKCL"] == "R^m"
    assert sym["norm_H_AKCL"] == "euclidean"
    assert sym["J_m"] == "identity"
    assert sym["P_AKCL_img"] == "H_AKCL"
    assert sym["closure_equals_H_AKCL"] is True
    assert abs(sym["c0_tilde"] - c0_tilde) <= 1e-12
    assert abs(sym["eta_tilde"] - eta_tilde) <= 1e-12
    assert abs(sym["identified_from_declared_pair"]["c0"] - pair["c0"]) <= 1e-12
    assert abs(sym["identified_from_declared_pair"]["eta"] - pair["eta"]) <= 1e-12


def test_conditional_theorem_level_docs_literals_present():
    checks = {
        "docs/rigidity/rh/AKCL_CONDITIONAL_H_AKCL_2026_04.md": [
            "Conditional.",
            "H_{\\mathrm{AKCL}}:=\\mathbb R^m",
            "\\|a\\|_{H_{\\mathrm{AKCL}}}",
        ],
        "docs/rigidity/rh/AKCL_CONDITIONAL_J_M_2026_04.md": [
            "J_m:\\mathbb R^m\\to H_{\\mathrm{AKCL}}",
            "J_m(a):=a",
        ],
        "docs/rigidity/rh/AKCL_CONDITIONAL_E_AKCL_2026_04.md": [
            "E_{\\mathrm{AKCL}}",
            "E_{\\mathrm{AKCL}}(a):=M_E a",
            "a^\\top M_E a",
        ],
        "docs/rigidity/rh/AKCL_CONDITIONAL_D_AKCL_2026_04.md": [
            "D_{\\mathrm{AKCL}}",
            "D_{\\mathrm{AKCL}}(a):=M_D a",
            "a^\\top M_D a",
        ],
        "docs/rigidity/rh/AKCL_CONDITIONAL_P_IMG_CLOSURE_2026_04.md": [
            "P_{\\mathrm{AKCL}}^{\\mathrm{img}}:=J_m(\\mathbb R^m)",
            "\\overline{P_{\\mathrm{AKCL}}^{\\mathrm{img}}}^{\\,\\|\\cdot\\|_{H_{\\mathrm{AKCL}}}}",
        ],
        "docs/rigidity/rh/AKCL_CONDITIONAL_C0_ETA_PAIR_2026_04.md": [
            "\\widetilde c_0:=\\lambda_{\\min}(M_E)",
            "\\widetilde\\eta:=\\lambda_{\\max}",
            "\\operatorname{Def}_{\\mathrm{AKCL}}[a]\\le \\widetilde\\eta\\,E[a]",
        ],
        "docs/rigidity/rh/AKCL_CONDITIONAL_THEOREM_LEVEL_SYMBOLS_REGISTRY_2026_04.md": [
            "Conditional.",
            "J_m(a)=a",
            "P_{\\mathrm{AKCL}}^{\\mathrm{img}}=H_{\\mathrm{AKCL}}",
        ],
    }
    for path, pats in checks.items():
        text = Path(path).read_text()
        for pat in pats:
            assert pat in text
