"""
i18n.test.py – Tests unitaires Python pour i18n Threed
"""
from .i18n import i18n

def test_i18n_fr():
    assert '[FR]' in i18n('Test', 'fr')

def test_i18n_en():
    assert '[EN]' in i18n('Test', 'en')

def test_i18n_fallback():
    assert i18n('Test', 'es') == 'Test'
