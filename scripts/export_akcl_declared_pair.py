#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np

from src.kernel.akcl_syn_certificate import (
    AKCLConfig,
    center_columns,
    compress_to_basis,
    defect_feature_matrix,
    feature_matrix,
    gram_energy,
    make_log_grid,
    max_generalized_eig,
    min_eig,
    neutral_mode,
    packet_columns,
    real_orthonormalize,
)

def main() -> None:
    cfg = AKCLConfig()
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

    artifact = {
        "config": {
            "n_grid": cfg.n_grid,
            "u_min": cfg.u_min,
            "u_max": cfg.u_max,
            "alpha": cfg.alpha,
            "packet_count": cfg.packet_count,
            "packet_sigma": cfg.packet_sigma,
            "center_min": cfg.center_min,
            "center_max": cfg.center_max,
            "t_max": cfg.t_max,
            "t_count": cfg.t_count,
            "defect_t_max": cfg.defect_t_max,
            "defect_t_count": cfg.defect_t_count,
            "defect_eps": cfg.defect_eps,
            "defect_envelope_decay": cfg.defect_envelope_decay,
        },
        "basis_dimension": int(B.shape[1]),
        "c0": min_eig(E),
        "eta": max_generalized_eig(D, E),
        "E_matrix": E.tolist(),
        "D_matrix": D.tolist(),
    }

    out = Path("experiments/akcl_declared_pair.json")
    out.write_text(json.dumps(artifact, indent=2))
    print(json.dumps({"artifact": str(out), "c0": artifact["c0"], "eta": artifact["eta"]}, indent=2))

if __name__ == "__main__":
    main()
