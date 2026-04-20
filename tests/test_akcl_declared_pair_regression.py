import json
from pathlib import Path
import numpy as np

from src.kernel.akcl_syn_certificate import AKCLConfig, run_once


def test_declared_pair_matches_current_default_certificate():
    data = json.loads(Path("experiments/akcl_declared_pair.json").read_text())
    rep = run_once(AKCLConfig())
    assert abs(data["c0"] - rep["c0"]) <= 1e-12
    assert abs(data["eta"] - rep["eta"]) <= 1e-12
    E = np.array(data["E_matrix"], dtype=float)
    D = np.array(data["D_matrix"], dtype=float)
    assert E.shape == D.shape
    assert E.shape[0] == data["basis_dimension"]
    assert np.allclose(E, E.T, atol=1e-10)
    assert np.allclose(D, D.T, atol=1e-10)
