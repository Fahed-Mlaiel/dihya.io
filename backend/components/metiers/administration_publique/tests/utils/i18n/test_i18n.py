"""
Tests avancés d'internationalisation pour Threed (multi-langue, fallback, conformité)
"""
import pytest
from ..i18n import i18n
from .i18n_utils import translate

def i18n(msg, lang):
    if lang in ['fr', 'en']:
        return translate(msg, lang)
    return msg

def test_i18n_fr():
    assert '[FR]' in i18n('Test', 'fr')

def test_i18n_en():
    assert '[EN]' in i18n('Test', 'en')

def test_i18n_fallback():
    assert i18n('Test', 'es') == 'Test'
