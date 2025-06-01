"""
Tests unitaires pour la gestion sécurisée des secrets (app.security.secrets) — Dihya Coding.

Vérifie la récupération, la validation et la gestion des erreurs pour les secrets applicatifs.
Respecte les bonnes pratiques de sécurité et de conformité RGPD.
"""

import os
import pytest
from backend.flask.app.securite import secrets

def test_get_secret_present(monkeypatch):
    """Test récupération d'un secret présent dans l'environnement."""
    monkeypatch.setenv("TEST_SECRET", "valeur123")
    assert secrets.get_secret("TEST_SECRET") == "valeur123"

def test_get_secret_absent_raises(monkeypatch):
    """Test exception si le secret est requis et absent."""
    monkeypatch.delenv("TEST_SECRET", raising=False)
    with pytest.raises(secrets.SecretNotFound):
        secrets.get_secret("TEST_SECRET", required=True)

def test_get_secret_default(monkeypatch):
    """Test récupération d'une valeur par défaut si le secret est absent et non requis."""
    monkeypatch.delenv("TEST_SECRET", raising=False)
    assert secrets.get_secret("TEST_SECRET", default="defaut", required=False) == "defaut"

def test_validate_secrets_all_present(monkeypatch):
    """Test validation de plusieurs secrets présents."""
    monkeypatch.setenv("SECRET_A", "a")
    monkeypatch.setenv("SECRET_B", "b")
    # Ne doit pas lever d'exception
    secrets.validate_secrets(["SECRET_A", "SECRET_B"])

def test_validate_secrets_missing(monkeypatch):
    """Test validation échoue si un secret est manquant."""
    monkeypatch.setenv("SECRET_A", "a")
    monkeypatch.delenv("SECRET_B", raising=False)
    with pytest.raises(secrets.SecretNotFound):
        secrets.validate_secrets(["SECRET_A", "SECRET_B"])
