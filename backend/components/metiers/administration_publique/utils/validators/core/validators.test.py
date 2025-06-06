"""
validators.test.py – Tests unitaires Python pour validators Threed
"""
from .validators import validate_threed

def test_valid_threed():
    data = {'nom': 'Test', 'statut': 'actif'}
    assert validate_threed(data)

def test_invalid_threed():
    try:
        validate_threed({'nom': '', 'statut': 'foo'})
    except ValueError:
        assert True
    else:
        assert False
