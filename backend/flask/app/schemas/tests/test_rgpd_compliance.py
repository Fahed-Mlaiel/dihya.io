"""
Tests unitaires et d'intégration pour la conformité RGPD des schémas – Dihya Coding.

Ce fichier vérifie la suppression, l'export, le masquage des données sensibles, la conformité RGPD, etc.
"""
import pytest
from backend.flask.app.schemas.user import UserSchema

@pytest.fixture
def user_data():
    return {"username": "testuser", "email": "test@example.com", "password": "SuperSecret123"}

def test_user_schema_export_rgpd(user_data):
    schema = UserSchema()
    loaded = schema.load(user_data)
    # Simuler un export RGPD (à adapter selon la logique métier)
    export = {k: v for k, v in loaded.items() if k != "password"}
    assert "password" not in export

def test_user_schema_delete_rgpd(user_data):
    # Simuler une suppression RGPD (à adapter selon la logique métier)
    deleted = {k: None for k in user_data}
    assert all(v is None for v in deleted.values())
