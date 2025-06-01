"""
Tests unitaires pour le service d’authentification (auth_service) de Dihya Coding.

Vérifie l’inscription, la connexion, la validation des credentials, la gestion des tokens,
la sécurité (hash, JWT), et la gestion des erreurs.
"""

import pytest
from backend.flask.app.services import auth_service

@pytest.fixture
def user_data():
    return {
        "username": "alice",
        "email": "alice@dihya.dev",
        "password": "motdepassefort"
    }

def test_register_user_success(user_data):
    user = auth_service.register_user(**user_data)
    assert user["username"] == user_data["username"]
    assert user["email"] == user_data["email"]
    assert "password" not in user

def test_register_user_duplicate(user_data):
    auth_service.register_user(**user_data)
    with pytest.raises(Exception):
        auth_service.register_user(**user_data)

def test_login_user_success(user_data):
    auth_service.register_user(**user_data)
    tokens = auth_service.login_user(user_data["email"], user_data["password"])
    assert "access_token" in tokens
    assert "refresh_token" in tokens

def test_login_user_invalid_password(user_data):
    auth_service.register_user(**user_data)
    with pytest.raises(Exception):
        auth_service.login_user(user_data["email"], "wrongpassword")

def test_login_user_not_found():
    with pytest.raises(Exception):
        auth_service.login_user("notfound@dihya.dev", "nopass")