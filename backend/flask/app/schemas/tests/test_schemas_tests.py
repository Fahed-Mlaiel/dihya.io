"""
Tests unitaires et d’intégration pour le module Schemas – Dihya Coding.

Ce fichier vérifie la validation des schémas utilisateur, projet, plugin, etc.,
en simulant différents scénarios métier et de sécurité.

Bonnes pratiques :
- Utiliser des fixtures pour les schémas et contextes (voir conftest.py)
- Tester les cas de succès, d’échec, de champs manquants ou invalides
- Ne jamais utiliser de données réelles ou sensibles
- Documenter chaque scénario de test
- Logger les erreurs critiques pour auditabilité (sans fuite de données sensibles)
"""

import pytest
from backend.flask.app.schemas.project import ProjectSchema

@pytest.fixture
def valid_project_data():
    return {
        "name": "Projet Test",
        "owner": "user_123",
        "stack": ["flask", "react"],
        "modules": [{"name": "backend"}, {"name": "frontend"}],
        "created_at": "2025-01-01T00:00:00Z",
        "config": {},
        "plugins": [],
        "i18n": {},
        "docs": "Documentation du projet."
    }

def test_project_schema_valid(valid_project_data):
    """
    Teste la validation d’un projet complet et conforme.
    """
    assert ProjectSchema.validate(valid_project_data) is True

def test_project_schema_missing_field(valid_project_data):
    """
    Teste la détection d’un champ requis manquant.
    """
    data = valid_project_data.copy()
    data.pop("owner")
    with pytest.raises(ValueError) as exc:
        ProjectSchema.validate(data)
    assert "champs manquants" in str(exc.value)

def test_project_schema_invalid_stack(valid_project_data):
    """
    Teste la détection d’un type de stack invalide.
    """
    data = valid_project_data.copy()
    data["stack"] = "flask"  # Doit être une liste
    with pytest.raises(ValueError) as exc:
        ProjectSchema.validate(data)
    assert "stack doit être une liste" in str(exc.value)

def test_project_schema_config_with_secret(valid_project_data):
    """
    Teste la détection d’un secret dans la config (sécurité RGPD).
    """
    data = valid_project_data.copy()
    data["config"] = {"db_secret": "should_not_be_here"}
    with pytest.raises(ValueError) as exc:
        ProjectSchema.validate(data)
    assert "ne doit pas contenir de secrets" in str(exc.value)

def test_project_schema_optional_fields(valid_project_data):
    """
    Teste la validation avec des champs optionnels manquants.
    """
    data = valid_project_data.copy()
    data.pop("config")
    data.pop("plugins")
    data.pop("i18n")
    data.pop("docs")
    # Doit toujours être valide
    assert ProjectSchema.validate(data) is True