from pathlib import Path


def test_uniform_domination_lock_literals_present():
    text = Path("docs/rigidity/rh/AKCL_UNIFORM_DOMINATION_TRANSFER_LEMMA_2026_04.md").read_text()
    assert "## Status" in text
    assert "OPEN" in text
    assert "Let \\(f\\in \\mathcal A_{\\mathrm{AKCL}}\\)." in text
    assert "\\operatorname{Def}_{\\mathrm{AKCL}}[f_n]" in text
    assert "\\operatorname{Def}_{\\mathrm{AKCL}}[f]" in text
    assert "A proof that the domination constant \\(\\eta\\) is uniform across the approximating packet families." in text
    assert "a proof or certified verifier establishing the limit-passage implication above." in text
