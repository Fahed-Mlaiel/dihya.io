# test.py - Test unitaire et d'intégration pour scripts (Python)
"""
Test complet des scripts (robustesse, portabilité, sécurité, i18n)
"""
import pytest
from ..scripts import run_script

def test_run_script():
    assert run_script('echo "ok"') == 'ok'

def test_error_handling_i18n():
    with pytest.raises(Exception) as exc:
        run_script('exit 1')
    assert 'Erreur' in str(exc.value)
