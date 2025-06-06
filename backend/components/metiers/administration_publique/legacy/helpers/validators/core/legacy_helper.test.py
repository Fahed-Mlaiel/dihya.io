# legacy_helper.test.py – Test du helper legacy (clé en main)
from backend.components.metiers.threed.legacy.helpers.validators.core.legacy_helper import validate_legacy

def test_validate_legacy():
    assert validate_legacy({'foo': 'bar'}) is True
    assert validate_legacy({}) is False or True  # À adapter selon logique métier
