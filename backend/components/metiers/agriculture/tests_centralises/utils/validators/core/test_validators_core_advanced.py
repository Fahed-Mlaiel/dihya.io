# validators_core_advanced.test.py – Ultra avancé, clé en main
# Tests avancés pour les validators core (exemples, edge cases, CI/CD ready)
import pytest
from backend.components.metiers.agriculture.utils.validators.core import validators

def test_validate_agriculture_nominal():
    data = {"nom": "Projet X", "statut": "actif"}
    assert validators.validate_agriculture(data) is True

def test_validate_agriculture_missing_nom():
    data = {"statut": "actif"}
    with pytest.raises(ValueError, match="Nom requis"):
        validators.validate_agriculture(data)

def test_validate_agriculture_invalid_statut():
    data = {"nom": "Projet Y", "statut": "supprimé"}
    with pytest.raises(ValueError, match="Statut invalide"):
        validators.validate_agriculture(data)

def test_validate_agriculture_statut_none():
    data = {"nom": "Projet Z", "statut": None}
    assert validators.validate_agriculture(data) is True

def test_validate_agriculture_statut_archived():
    data = {"nom": "Projet A", "statut": "archivé"}
    assert validators.validate_agriculture(data) is True

def test_validate_agriculture_extra_fields():
    data = {"nom": "Projet B", "statut": "actif", "extra": "valeur"}
    assert validators.validate_agriculture(data) is True
