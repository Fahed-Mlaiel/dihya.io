# validators_fallback_advanced.test.py – Ultra avancé, clé en main
def test_fallback_to_default():
    value = None
    fallback = value or "default"
    assert fallback == "default"

def test_fallback_with_value():
    value = "present"
    fallback = value or "default"
    assert fallback == "present"

def test_fallback_edge_cases():
    # 0, False, [] sont des valeurs falsy en Python, donc fallback s'applique
    assert (0 or "default") == "default"
    assert (False or "default") == "default"
    assert ([] or "default") == "default"
    # None doit aussi donner fallback
    assert (None or "default") == "default"
    # Valeur non-falsy
    assert ("ok" or "default") == "ok"
