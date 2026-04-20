from pathlib import Path


def test_packet_family_definition_lock_literals_present():
    text = Path("docs/rigidity/rh/AKCL_DECLARED_PACKET_FAMILY_DEFINITION_2026_04.md").read_text()
    assert "## Status" in text
    assert "OPEN" in text
    assert "\\mathcal P_{\\mathrm{AKCL}}" in text
    assert "Admissible parameter set." in text
    assert "Packet centers." in text
    assert "Packet width rule." in text
    assert "Neutral-mode projection rule." in text
    assert "Orthonormalization rule." in text
    assert "Union rule over parameter choices." in text
