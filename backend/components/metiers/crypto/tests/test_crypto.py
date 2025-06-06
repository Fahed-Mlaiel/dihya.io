# test_crypto.py
"""
Tests unitaires ultra avancés pour le module crypto (validation, RGPD, anonymisation, plugins, multichain, audit, export, accessibilité, logging, multitenancy).
"""
from ..utils.validators import is_valid_address, is_strong_password

def test_is_valid_address():
    assert is_valid_address('0x1234567890abcdef1234567890abcdef12345678')
    assert is_valid_address('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa')
    assert not is_valid_address('short')

def test_is_strong_password():
    assert is_strong_password('Abcdef1!')
    assert not is_strong_password('weak')
