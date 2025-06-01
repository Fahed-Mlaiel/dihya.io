"""
Tests unitaires pour le service utilisateur (user_service) de Dihya Coding.

Vérifie la création, la récupération, la mise à jour et la suppression d’utilisateurs,
ainsi que la gestion des rôles et la sécurité des opérations.
"""

import pytest
from backend.flask.app.services import user_service

@pytest.fixture
def sample_user():
    return {
        "username": "alice",
        "email": "alice@dihya.dev",
        "password": "motdepassefort",
        "role": "user"
    }

def test_create_user(sample_user):
    user = user_service.create_user(**sample_user)
    assert user["username"] == sample_user["username"]
    assert user["email"] == sample_user["email"]
    assert "password" not in user  # Jamais retourner le mot de passe en clair

def test_get_user_by_email(sample_user):
    user_service.create_user(**sample_user)
    user = user_service.get_user_by_email(sample_user["email"])
    assert user is not None
    assert user["email"] == sample_user["email"]

def test_update_user_role(sample_user):
    user = user_service.create_user(**sample_user)
    updated = user_service.update_user_role(user["email"], "admin")
    assert updated["role"] == "admin"

def test_delete_user(sample_user):
    user_service.create_user(**sample_user)
    result = user_service.delete_user(sample_user["email"])
    assert result is True
    assert user_service.get_user_by_email(sample_user["email"]) is None

def test_create_user_duplicate(sample_user):
    user_service.create_user(**sample_user)
    with pytest.raises(Exception):
        user_service.create_user(**sample_user)