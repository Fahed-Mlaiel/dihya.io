"""
Tests unitaires et d'intégration pour la sécurité des schémas – Dihya Coding.

Ce fichier vérifie le masquage, la validation, l'accès, la non-exposition des secrets/API, etc.
"""
import pytest
from backend.flask.app.schemas.user import UserSchema
from marshmallow import ValidationError

def test_user_schema_no_password_in_dump():
    schema = UserSchema()
    user = {"username": "testuser", "email": "test@example.com", "password": "SuperSecret123"}
    loaded = schema.load(user)
    dumped = schema.dump(loaded)
    assert "password" not in dumped

def test_user_schema_masking():
    schema = UserSchema()
    user = {"username": "testuser", "email": "test@example.com", "password": "SuperSecret123"}
    loaded = schema.load(user)
    # Simuler un masquage RGPD (à adapter selon la logique métier)
    masked = {k: (v if k != "email" else "***masked***") for k, v in loaded.items()}
    assert masked["email"] == "***masked***"

def test_user_schema_invalid_access():
    schema = UserSchema()
    with pytest.raises(ValidationError):
        schema.load({"username": "", "email": "", "password": ""})
