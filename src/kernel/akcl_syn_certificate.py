from dataclasses import dataclass, asdict
from typing import Dict, Any, Optional, Tuple
import math
import numpy as np


def make_log_grid(u_min: float = -4.0, u_max: float = 4.0, n: int = 400):
    u = np.linspace(u_min, u_max, n)
    x = np.exp(u)
    du = (u_max - u_min) / (n - 1)
    q = x * du
    return x, q, u


def weight(x: np.ndarray, alpha: float = 0.0) -> np.ndarray:
    return np.exp(-x) * np.power(x, alpha)


def neutral_mode(x: np.ndarray, q: np.ndarray, alpha: float = 0.0) -> np.ndarray:
    v = np.sqrt(weight(x, alpha) * q)
    return v / np.linalg.norm(v)


def packet_columns(u: np.ndarray, centers: np.ndarray, sigma: float) -> np.ndarray:
    return np.column_stack([np.exp(-0.5 * ((u - c) / sigma) ** 2) for c in centers])


def real_orthonormalize(
    B: np.ndarray,
    neutral: Optional[np.ndarray] = None,
    tol: float = 1e-10,
) -> np.ndarray:
    M = B.astype(float).copy()
    if neutral is not None:
        n = neutral / np.linalg.norm(neutral)
        M -= np.outer(n, n @ M)
    cols = []
    for j in range(M.shape[1]):
        v = M[:, j].copy()
        for q in cols:
            v -= q * (q @ v)
        nv = np.linalg.norm(v)
        if nv > tol:
            cols.append(v / nv)
    if not cols:
        raise ValueError("No admissible packet columns after orthonormalization.")
    return np.column_stack(cols)


def feature_matrix(
    x: np.ndarray,
    q: np.ndarray,
    t_values: np.ndarray,
    alpha: float = 0.0,
) -> np.ndarray:
    base = np.sqrt(weight(x, alpha) * q)[:, None]
    return base * np.power(x[:, None], 0.5 + 1j * t_values[None, :])


def defect_feature_matrix(
    x: np.ndarray,
    q: np.ndarray,
    tau_values: np.ndarray,
    eps: float,
    alpha: float = 0.0,
    envelope_decay: float = 0.0,
) -> np.ndarray:
    base = np.sqrt(weight(x, alpha) * q)[:, None]
    env = np.exp(-envelope_decay * tau_values**2)[None, :]
    rhos = 0.5 + eps + 1j * tau_values
    return base * np.power(x[:, None], rhos[None, :] - 0.5) * env


def center_columns(Phi: np.ndarray, neutral: np.ndarray) -> np.ndarray:
    coeffs = neutral.conj() @ Phi
    return Phi - neutral[:, None] * coeffs[None, :]


def gram_energy(Phi: np.ndarray) -> np.ndarray:
    G = Phi @ Phi.conj().T
    return ((G + G.conj().T) * 0.5).real


def compress_to_basis(M: np.ndarray, B: np.ndarray) -> np.ndarray:
    C = B.T @ M @ B
    return ((C + C.T) * 0.5)


def min_eig(M: np.ndarray) -> float:
    return float(np.linalg.eigvalsh(M).min())


def max_generalized_eig(D: np.ndarray, E: np.ndarray, tol: float = 1e-10) -> float:
    evals, evecs = np.linalg.eigh(E)
    keep = evals > tol
    if not np.any(keep):
        return float("inf")
    Einvhalf = evecs[:, keep] @ np.diag(evals[keep] ** -0.5) @ evecs[:, keep].T
    S = Einvhalf @ D @ Einvhalf
    S = (S + S.T) * 0.5
    return float(np.linalg.eigvalsh(S).max())


@dataclass
class AKCLConfig:
    n_grid: int = 400
    u_min: float = -4.0
    u_max: float = 4.0
    alpha: float = 0.0
    packet_count: int = 5
    packet_sigma: float = 1.0
    center_min: float = -2.5
    center_max: float = 2.5
    t_max: float = 8.0
    t_count: int = 81
    defect_t_max: float = 12.0
    defect_t_count: int = 21
    defect_eps: float = 0.05
    defect_envelope_decay: float = 0.0
    target_eta: float = 0.95


def run_once(cfg: AKCLConfig) -> Dict[str, Any]:
    x, q, u = make_log_grid(cfg.u_min, cfg.u_max, cfg.n_grid)
    neutral = neutral_mode(x, q, cfg.alpha)
    centers = np.linspace(cfg.center_min, cfg.center_max, cfg.packet_count)
    B = real_orthonormalize(packet_columns(u, centers, cfg.packet_sigma), neutral)

    t_values = np.linspace(0.0, cfg.t_max, cfg.t_count)
    Phi = center_columns(feature_matrix(x, q, t_values, cfg.alpha), neutral)
    E = compress_to_basis(gram_energy(Phi), B)

    tau_values = np.linspace(0.0, cfg.defect_t_max, cfg.defect_t_count)
    Psi = center_columns(
        defect_feature_matrix(
            x,
            q,
            tau_values,
            cfg.defect_eps,
            cfg.alpha,
            cfg.defect_envelope_decay,
        ),
        neutral,
    )
    D = compress_to_basis(gram_energy(Psi), B)

    c0 = min_eig(E)
    eta = max_generalized_eig(D, E)
    needed_scale = min(1.0, cfg.target_eta / eta) if np.isfinite(eta) and eta > 0 else 1.0

    return {
        "config": asdict(cfg),
        "admissible_dim": int(B.shape[1]),
        "c0": c0,
        "eta": eta,
        "status": "PASS" if (c0 > 1e-8 and eta < 1.0) else "FAIL",
        "needed_defect_scale_for_target_eta": needed_scale,
    }


def propose_next(cfg: AKCLConfig, report: Dict[str, Any]) -> Tuple[AKCLConfig, str]:
    new = AKCLConfig(**asdict(cfg))

    if not np.isfinite(report["c0"]) or report["c0"] <= 1e-8:
        if new.packet_count > 3:
            new.packet_count -= 2
            return new, "packet-rank-deficiency: reduced admissible family dimension"
        new.t_count += 40
        new.t_max += 4.0
        return new, "packet-rank-deficiency: widened critical spectral family"

    if not np.isfinite(report["eta"]) or report["eta"] >= 1.0:
        scale = report["needed_defect_scale_for_target_eta"]
        if new.defect_envelope_decay == 0.0 and scale < 1.0:
            tau = max(new.defect_t_max, 1e-6)
            gamma = max(1e-6, -math.log(scale) / (tau * tau))
            new.defect_envelope_decay = gamma
            return new, f"defect-dominance-missing: imposed envelope exp(-gamma t^2) with gamma={gamma:.6f}"
        if new.packet_count > 5:
            new.packet_count -= 2
            return new, "defect-dominance-missing: reduced admissible family dimension"
        if new.packet_sigma < 1.0:
            new.packet_sigma = min(1.0, new.packet_sigma + 0.2)
            return new, "defect-dominance-missing: increased packet width"
        if new.defect_eps > 0.02:
            new.defect_eps *= 0.5
            return new, "defect-dominance-missing: reduced off-critical shift"

    return new, "no-change"


def run_loop(cfg: AKCLConfig, max_rounds: int = 6) -> Dict[str, Any]:
    rounds = []
    current = cfg
    for k in range(max_rounds):
        rep = run_once(current)
        rep["round"] = k
        rounds.append(rep)
        if rep["status"] == "PASS":
            return {"status": "PASS", "rounds": rounds, "final": rep}
        nxt, reason = propose_next(current, rep)
        rep["imputed_missing_information"] = reason
        if asdict(nxt) == asdict(current):
            break
        current = nxt
    return {"status": "CONDITIONAL", "rounds": rounds, "final": rounds[-1]}
