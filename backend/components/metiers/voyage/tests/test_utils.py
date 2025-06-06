import pytest
from ..utils.audit import auditEnvironnement
from ..utils.i18n import i18n
from ..utils.validators import validate_environnement

def test_audit_environnement():
    result = auditEnvironnement({'statut': 'actif'})
    assert 'score' in result
    assert result['score'] > 0

def test_i18n():
    assert '[FR]' in i18n('Test', 'fr')
    assert '[EN]' in i18n('Test', 'en')

def test_validators_ok():
    validate_environnement({'nom': 'ok', 'statut': 'actif'})

def test_validators_fail():
    with pytest.raises(Exception):
        validate_environnement({'statut': 'actif'})
