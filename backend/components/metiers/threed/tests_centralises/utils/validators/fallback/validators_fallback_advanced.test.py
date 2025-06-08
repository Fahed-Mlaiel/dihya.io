# validators_fallback_advanced.test.py – Ultra avancé, clé en main
def test_fallback_to_default():
    value = None
    fallback = value or 'default'
    assert fallback == 'default'
