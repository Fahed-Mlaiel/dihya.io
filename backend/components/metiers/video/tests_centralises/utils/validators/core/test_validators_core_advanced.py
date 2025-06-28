# validators_core_advanced.test.py – Ultra avancé, clé en main
# Tests avancés pour les validators core (exemples, edge cases, CI/CD ready)
import pytest
from backend.components.metiers.video.utils.validators.core import validators

def test_validate_video_nominal():
    data = {"nom": "Projet X", "statut": "actif"}
    assert validators.validate_video(data) is True

def test_validate_video_missing_nom():
    data = {"statut": "actif"}
    with pytest.raises(ValueError, match="Nom requis"):
        validators.validate_video(data)

def test_validate_video_invalid_statut():
    data = {"nom": "Projet Y", "statut": "supprimé"}
    with pytest.raises(ValueError, match="Statut invalide"):
        validators.validate_video(data)

def test_validate_video_statut_none():
    data = {"nom": "Projet Z", "statut": None}
    assert validators.validate_video(data) is True

def test_validate_video_statut_archived():
    data = {"nom": "Projet A", "statut": "archivé"}
    assert validators.validate_video(data) is True

def test_validate_video_extra_fields():
    data = {"nom": "Projet B", "statut": "actif", "extra": "valeur"}
    assert validators.validate_video(data) is True
