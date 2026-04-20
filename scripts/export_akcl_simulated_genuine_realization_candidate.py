#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np

from src.kernel.akcl_syn_certificate import (
    AKCLConfig,
    defect_feature_matrix,
    feature_matrix,
    make_log_grid,
    neutral_mode,
)


def main() -> None:
    cfg = AKCLConfig()
    x, q, u = make_log_grid(cfg.u_min, cfg.u_max, cfg.n_grid)
    du = (cfg.u_max - cfg.u_min) / (cfg.n_grid - 1)

    neutral_disc = neutral_mode(x, q, cfg.alpha)

    n_raw = np.exp(-x / 2.0) * np.power(x, (cfg.alpha + 1.0) / 2.0)
    z_quad = float(np.sum(n_raw**2) * du)
    n_cont_sample = n_raw / np.sqrt(z_quad)
    neutral_from_cont = n_cont_sample * np.sqrt(du)
    neutral_from_cont = neutral_from_cont / np.linalg.norm(neutral_from_cont)

    t_values = np.linspace(0.0, cfg.t_max, cfg.t_count)
    feature_disc = feature_matrix(x, q, t_values, cfg.alpha)

    phi_cont = (
        np.exp(-x[:, None] / 2.0)
        * np.power(x[:, None], (cfg.alpha + 2.0) / 2.0 + 1j * t_values[None, :])
    )
    feature_from_cont = phi_cont * np.sqrt(du)

    tau_values = np.linspace(0.0, cfg.defect_t_max, cfg.defect_t_count)
    defect_disc = defect_feature_matrix(
        x,
        q,
        tau_values,
        cfg.defect_eps,
        cfg.alpha,
        cfg.defect_envelope_decay,
    )
    psi_cont = (
        np.exp(-x[:, None] / 2.0)
        * np.power(
            x[:, None],
            (cfg.alpha + 1.0) / 2.0 + cfg.defect_eps + 1j * tau_values[None, :],
        )
        * np.exp(-cfg.defect_envelope_decay * tau_values**2)[None, :]
    )
    defect_from_cont = psi_cont * np.sqrt(du)

    artifact = {
        "model": "simulated_genuine_realization_candidate",
        "u_min": cfg.u_min,
        "u_max": cfg.u_max,
        "n_grid": cfg.n_grid,
        "alpha": cfg.alpha,
        "X_AKCL_sim": f"[{cfg.u_min}, {cfg.u_max}]",
        "mu_AKCL_sim": "du",
        "neutral_formula": "Z^(-1/2) * exp(-exp(u)/2) * exp(((alpha+1)/2) * u)",
        "H_AKCL_sim": "{f in L2([u_min,u_max],du) : integral f(u) n_AKCL_sim(u) du = 0}",
        "norm_H_AKCL_sim": "(integral |f(u)|^2 du)^(1/2)",
        "packet_formula": "exp(-(u-c)^2 / (2 sigma^2))",
        "energy_feature_formula": "exp(-exp(u)/2) * exp(((alpha+2)/2 + i t) * u)",
        "defect_feature_formula": "exp(-exp(u)/2) * exp(((alpha+1)/2 + eps + i tau) * u) * exp(-gamma tau^2)",
        "quadrature_Z": z_quad,
        "neutral_consistency_l2": float(np.linalg.norm(neutral_disc - neutral_from_cont)),
        "feature_consistency_max": float(np.max(np.abs(feature_disc - feature_from_cont))),
        "defect_consistency_max": float(np.max(np.abs(defect_disc - defect_from_cont))),
    }

    out = Path("experiments/akcl_simulated_genuine_realization_candidate.json")
    out.write_text(json.dumps(artifact, indent=2))
    print(json.dumps(artifact, indent=2))


if __name__ == "__main__":
    main()
