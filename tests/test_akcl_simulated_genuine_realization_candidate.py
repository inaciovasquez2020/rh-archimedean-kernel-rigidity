import json
from pathlib import Path

from src.kernel.akcl_syn_certificate import (
    AKCLConfig,
    defect_feature_matrix,
    feature_matrix,
    make_log_grid,
    neutral_mode,
)

import numpy as np


def test_simulated_candidate_artifact_matches_discrete_model():
    artifact = json.loads(Path("experiments/akcl_simulated_genuine_realization_candidate.json").read_text())
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

    assert abs(artifact["quadrature_Z"] - z_quad) <= 1e-12
    assert abs(artifact["neutral_consistency_l2"] - float(np.linalg.norm(neutral_disc - neutral_from_cont))) <= 1e-12
    assert abs(artifact["feature_consistency_max"] - float(np.max(np.abs(feature_disc - feature_from_cont)))) <= 1e-12
    assert abs(artifact["defect_consistency_max"] - float(np.max(np.abs(defect_disc - defect_from_cont)))) <= 1e-12
    assert artifact["neutral_consistency_l2"] <= 1e-10
    assert artifact["feature_consistency_max"] <= 1e-10
    assert artifact["defect_consistency_max"] <= 1e-10


def test_simulated_candidate_doc_literals_present():
    text = Path("docs/rigidity/rh/AKCL_SIMULATED_GENUINE_REALIZATION_CANDIDATE_2026_04.md").read_text()
    assert "Conditional." in text
    assert "X_{\\mathrm{AKCL}}^{\\mathrm{sim}}" in text
    assert "\\mu_{\\mathrm{AKCL}}^{\\mathrm{sim}}" in text
    assert "n_{\\mathrm{AKCL}}^{\\mathrm{sim}}" in text
    assert "H_{\\mathrm{AKCL}}^{\\mathrm{sim}}" in text
    assert "\\|f\\|_{H_{\\mathrm{AKCL}}^{\\mathrm{sim}}}" in text
    assert "\\Phi_t^{\\mathrm{sim}}" in text
    assert "\\Psi_{\\tau,\\varepsilon,\\gamma}^{\\mathrm{sim}}" in text
    assert "S_N" in text
