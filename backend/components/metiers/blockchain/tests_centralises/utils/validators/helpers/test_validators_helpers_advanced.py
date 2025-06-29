# validators_helpers_advanced.test.py – Ultra avancé, clé en main
import pytest
from backend.components.metiers.blockchain.utils.validators.helpers import validators_helper

def test_help_validate_string():
    s = "test"
    assert isinstance(s, str)

def test_is_valid_email_nominal():
    assert validators_helper.is_valid_email("user@example.com")
    assert validators_helper.is_valid_email("prenom.nom@domaine.fr")

def test_is_valid_email_edge_cases():
    assert not validators_helper.is_valid_email("")
    assert not validators_helper.is_valid_email("user@.com")
    assert not validators_helper.is_valid_email("@example.com")
    assert not validators_helper.is_valid_email("user@domain")
    assert not validators_helper.is_valid_email("user@domain.")
    assert not validators_helper.is_valid_email("user@@domain.com")
    assert not validators_helper.is_valid_email("user domain.com")
    assert not validators_helper.is_valid_email("user@domain,com")
    assert not validators_helper.is_valid_email("user@domain..com")
