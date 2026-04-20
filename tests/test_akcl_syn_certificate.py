from src.kernel.akcl_syn_certificate import AKCLConfig, run_once, run_loop


def test_default_certificate_passes():
    rep = run_once(AKCLConfig())
    assert rep["status"] == "PASS"
    assert rep["c0"] > 1e-8
    assert rep["eta"] < 1.0


def test_restart_loop_imputes_missing_information():
    out = run_loop(
        AKCLConfig(packet_count=9, packet_sigma=0.4, t_max=16.0, t_count=81),
        max_rounds=6,
    )
    assert len(out["rounds"]) >= 1
    assert any("imputed_missing_information" in r for r in out["rounds"])
    assert out["status"] in {"PASS", "CONDITIONAL"}
    assert out["final"]["c0"] > 1e-8
