import numpy as np
from src.kernel.akcl_syn_certificate import (
    AKCLConfig,
    center_columns,
    compress_to_basis,
    feature_matrix,
    gram_energy,
    make_log_grid,
    min_eig,
    neutral_mode,
    packet_columns,
    real_orthonormalize,
)


def test_declared_packet_energy_matrix_is_psd():
    cfg = AKCLConfig()
    x, q, u = make_log_grid(cfg.u_min, cfg.u_max, cfg.n_grid)
    neutral = neutral_mode(x, q, cfg.alpha)
    centers = np.linspace(cfg.center_min, cfg.center_max, cfg.packet_count)
    B = real_orthonormalize(packet_columns(u, centers, cfg.packet_sigma), neutral)
    t_values = np.linspace(0.0, cfg.t_max, cfg.t_count)
    Phi = center_columns(feature_matrix(x, q, t_values, cfg.alpha), neutral)
    E = compress_to_basis(gram_energy(Phi), B)
    assert np.allclose(E, E.T, atol=1e-10)
    assert min_eig(E) >= -1e-10
