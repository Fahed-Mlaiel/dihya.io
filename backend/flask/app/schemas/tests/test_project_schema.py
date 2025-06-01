"""
Tests unitaires et d'intégration pour le schéma projet (ProjectSchema) – Dihya Coding.

Ce fichier vérifie la validation des schémas projet pour la génération, la sécurité, la conformité RGPD, la non-exposition des secrets, etc.
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
    assert ProjectSchema.validate(valid_project_data) is True

def test_project_schema_missing_field(valid_project_data):
    data = valid_project_data.copy()
    data.pop("owner")
    with pytest.raises(ValueError) as exc:
        ProjectSchema.validate(data)
    assert "champs manquants" in str(exc.value)

def test_project_schema_invalid_stack(valid_project_data):
    data = valid_project_data.copy()
    data["stack"] = "flask"  # Doit être une liste
    with pytest.raises(ValueError) as exc:
        ProjectSchema.validate(data)
    assert "stack doit être une liste" in str(exc.value)

def test_project_schema_config_with_secret(valid_project_data):
    data = valid_project_data.copy()
    data["config"] = {"api_secret": "should_not_be_here"}
    with pytest.raises(ValueError) as exc:
        ProjectSchema.validate(data)
    assert "secret" in str(exc.value).lower()
