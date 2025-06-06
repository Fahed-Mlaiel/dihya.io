# Tests principaux pour le module Arts

def test_get_expositions():
    from .arts import get_expositions
    expositions = get_expositions()
    assert len(expositions) >= 1
    assert "nom" in expositions[0]

def test_rechercher_oeuvre():
    from .arts import rechercher_oeuvre
    result = rechercher_oeuvre("Impression")
    assert len(result) == 1
    assert result[0]["nom"] == "Impression, soleil levant"
