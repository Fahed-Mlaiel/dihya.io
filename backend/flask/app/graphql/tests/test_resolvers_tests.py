"""
Tests unitaires pour les resolvers GraphQL de Dihya Coding.

Vérifie la conformité des requêtes, la sécurité des accès, la validation des arguments,
et la robustesse des réponses pour chaque resolver GraphQL.
"""

import pytest
from backend.flask.app.graphql import resolvers

@pytest.fixture
def mock_info():
    class Info:
        context = {"user": {"username": "alice", "role": "admin"}}
    return Info()

def test_resolver_get_user_success(mock_info):
    result = resolvers.resolve_get_user(None, mock_info, email="alice@dihya.dev")
    assert result is not None
    assert "email" in result

def test_resolver_get_user_not_found(mock_info):
    result = resolvers.resolve_get_user(None, mock_info, email="notfound@dihya.dev")
    assert result is None

def test_resolver_list_users_admin(mock_info):
    users = resolvers.resolve_list_users(None, mock_info)
    assert isinstance(users, list)

def test_resolver_list_users_permission_denied():
    class Info:
        context = {"user": {"username": "bob", "role": "user"}}
    with pytest.raises(Exception):
        resolvers.resolve_list_users(None, Info())

def test_resolver_create_user_validation(mock_info):
    with pytest.raises(Exception):
        resolvers.resolve_create_user(None, mock_info, email="bad", username="", password="")

def test_no_sensitive_data_in_resolver_response(mock_info):
    user = resolvers.resolve_get_user(None, mock_info, email="alice@dihya.dev")
    if user:
        assert "password" not in user
        assert "secret" not in str(user).lower()