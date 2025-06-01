"""
Fichier de configuration des tests (conftest) pour le module Utils – Dihya Coding.

Ce fichier centralise les fixtures, hooks et configurations Pytest
pour les tests unitaires et d’intégration des utilitaires backend (validation, i18n, sécurité, mailing, etc.).

Bonnes pratiques :
- Définir ici les fixtures réutilisables (mocks, contextes, données de test)
- Ne jamais inclure de secrets ou données sensibles
- Documenter chaque fixture ou hook ajouté
- Prévoir l’extensibilité pour de nouveaux scénarios de test
"""

import pytest

@pytest.fixture
def fake_validation_input():
    """
    Fixture fournissant des données d’entrée factices pour les tests de validation.
    """
    return {
        "email": "test@example.com",
        "password": "FakePassword123!",
        "age": 30
    }

@pytest.fixture
def fake_i18n_context():
    """
    Fixture simulant un contexte i18n pour les tests de traduction dynamique.
    """
    return {
        "locale": "fr",
        "fallback_locale": "en",
        "user_id": "test_user"
    }

@pytest.fixture
def utils_test_context():
    """
    Fixture simulant un contexte d’utilisation des utilitaires (logs, sécurité, etc.).
    """
    return {
        "request_id": "req_123456",
        "ip": "127.0.0.1",
        "user_agent": "pytest"
    }

# Exemple d’utilisation :
# def test_validation_email(fake_validation_input):
#     assert "@" in fake_validation_input["email"]