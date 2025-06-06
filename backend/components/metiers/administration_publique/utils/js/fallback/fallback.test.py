# fallback.test.py
# Tests unitaires Python pour fallback (équivalent JS, ultra avancé)
from .fallback import fallback_value

def test_fallback_value_normal():
    assert fallback_value(42, 0) == 42

def test_fallback_value_none():
    assert fallback_value(None, 'defaut') == 'defaut'
