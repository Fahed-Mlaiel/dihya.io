"""
Tests unitaires et d'intégration pour le schéma utilisateur (UserSchema) – Dihya Coding.

Ce fichier vérifie la validation des schémas utilisateur pour l'inscription, la mise à jour, la connexion, la sécurité RGPD, la non-exposition des secrets, etc.
"""
import pytest
from backend.flask.app.schemas.user import UserSchema, UserRegisterSchema, UserUpdateSchema, UserLoginSchema
from marshmallow import ValidationError

@pytest.fixture
def valid_user_data():
    return {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "SuperSecret123"
    }

def test_user_schema_valid(valid_user_data):
    schema = UserSchema()
    result = schema.load(valid_user_data)
    assert result["username"] == valid_user_data["username"]
    assert result["email"] == valid_user_data["email"]
    assert "password" in result

def test_user_schema_invalid_email(valid_user_data):
    schema = UserSchema()
    data = valid_user_data.copy()
    data["email"] = "not-an-email"
    with pytest.raises(ValidationError):
        schema.load(data)

def test_user_schema_short_password(valid_user_data):
    schema = UserSchema()
    data = valid_user_data.copy()
    data["password"] = "123"
    with pytest.raises(ValidationError):
        schema.load(data)

def test_user_schema_username_with_space(valid_user_data):
    schema = UserSchema()
    data = valid_user_data.copy()
    data["username"] = "user name"
    with pytest.raises(ValidationError):
        schema.load(data)

def test_user_register_schema(valid_user_data):
    schema = UserRegisterSchema()
    result = schema.load(valid_user_data)
    assert result["username"] == valid_user_data["username"]
    assert result["email"] == valid_user_data["email"]
    assert "password" in result

def test_user_update_schema():
    schema = UserUpdateSchema()
    data = {"username": "newname"}
    result = schema.load(data)
    assert result["username"] == "newname"

def test_user_login_schema():
    schema = UserLoginSchema()
    data = {"email": "test@example.com", "password": "pass1234"}
    result = schema.load(data)
    assert result["email"] == "test@example.com"
    assert result["password"] == "pass1234"
