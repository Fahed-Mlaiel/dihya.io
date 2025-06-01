"""
Fichier de configuration des tests (conftest) pour le module Routes – Dihya Coding.

Ce fichier centralise les fixtures, hooks et configurations Pytest
pour les tests unitaires et d’intégration des routes API (auth, génération, utilisateur, etc.).

Bonnes pratiques :
- Définir ici les fixtures réutilisables (mocks, contextes, données de test)
- Ne jamais inclure de secrets ou données sensibles
- Documenter chaque fixture ou hook ajouté
- Prévoir l’extensibilité pour de nouveaux scénarios de test
"""

import pytest

@pytest.fixture
def fake_user_token():
    """
    Fixture fournissant un token utilisateur factice pour les tests d’authentification.
    """
    return "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.fake.payload.signature"

@pytest.fixture
def fake_api_request_context():
    """
    Fixture simulant un contexte de requête API (headers, user, params).
    """
    return {
        "headers": {"Authorization": "Bearer testtoken"},
        "user_id": "test_user",
        "roles": ["user"],
        "locale": "fr"
    }

@pytest.fixture
def fake_generation_payload():
    """
    Fixture fournissant un payload de génération de projet factice.
    """
    return {
        "project_type": "webapp",
        "description": "Créer une application de gestion de tâches.",
        "features": ["auth", "multilingue", "notifications"]
    }

# Exemple d’utilisation :
# def test_route_auth(fake_user_token):
#     assert fake_user_token.startswith("eyJ")