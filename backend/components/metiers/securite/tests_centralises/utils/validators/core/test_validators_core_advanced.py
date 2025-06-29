# validators_core_advanced.test.py – Ultra avancé, clé en main
# Tests avancés pour les validators core (exemples, edge cases, CI/CD ready)
import pytest
from backend.components.metiers.securite.utils.validators.core import validators

def test_validate_securite_nominal():
    data = {"nom": "Projet X", "statut": "actif"}
    assert validators.validate_securite(data) is True

def test_validate_securite_missing_nom():
    data = {"statut": "actif"}
    with pytest.raises(ValueError, match="Nom requis"):
        validators.validate_securite(data)

def test_validate_securite_invalid_statut():
    data = {"nom": "Projet Y", "statut": "supprimé"}
    with pytest.raises(ValueError, match="Statut invalide"):
        validators.validate_securite(data)

def test_validate_securite_statut_none():
    data = {"nom": "Projet Z", "statut": None}
    assert validators.validate_securite(data) is True

def test_validate_securite_statut_archived():
    data = {"nom": "Projet A", "statut": "archivé"}
    assert validators.validate_securite(data) is True

def test_validate_securite_extra_fields():
    data = {"nom": "Projet B", "statut": "actif", "extra": "valeur"}
    assert validators.validate_securite(data) is True
