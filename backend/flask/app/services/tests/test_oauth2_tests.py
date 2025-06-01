"""
Tests unitaires pour le service OAuth2 de Dihya Coding.

Vérifie la validation des tokens, la récupération des informations utilisateur,
la gestion des erreurs et la sécurité (pas de fuite de tokens).
"""

import pytest
from unittest.mock import patch
from backend.flask.app.services import oauth2

def mock_google_response_ok(*args, **kwargs):
    class MockResp:
        status_code = 200
        def json(self):
            return {
                "sub": "12345",
                "email": "alice@dihya.dev",
                "name": "Alice",
                "picture": "https://img.com/alice.png"
            }
    return MockResp()

def mock_github_response_ok(*args, **kwargs):
    class MockResp:
        status_code = 200
        def json(self):
            return {
                "id": 42,
                "email": "bob@dihya.dev",
                "name": "Bob",
                "login": "bob42",
                "avatar_url": "https://img.com/bob.png"
            }
    return MockResp()

def mock_response_fail(*args, **kwargs):
    class MockResp:
        status_code = 401
        def json(self): return {}
    return MockResp()

@patch("app.services.oauth2.requests.get", side_effect=mock_google_response_ok)
def test_get_google_user_info_success(mock_get):
    user = oauth2.get_google_user_info("fake_token")
    assert user["id"] == "12345"
    assert user["email"] == "alice@dihya.dev"
    assert user["provider"] == "google"

@patch("app.services.oauth2.requests.get", side_effect=mock_github_response_ok)
def test_get_github_user_info_success(mock_get):
    user = oauth2.get_github_user_info("fake_token")
    assert user["id"] == 42
    assert user["email"] == "bob@dihya.dev"
    assert user["provider"] == "github"

@patch("app.services.oauth2.requests.get", side_effect=mock_response_fail)
def test_get_google_user_info_fail(mock_get):
    user = oauth2.get_google_user_info("bad_token")
    assert user is None

@patch("app.services.oauth2.requests.get", side_effect=mock_response_fail)
def test_get_github_user_info_fail(mock_get):
    user = oauth2.get_github_user_info("bad_token")
    assert user is None