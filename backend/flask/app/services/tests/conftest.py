"""
Fichier de configuration des tests (conftest) pour le module Services – Dihya Coding.

Ce fichier centralise les fixtures, hooks et configurations Pytest
pour les tests unitaires et d’intégration des services backend (auth, mail, notifications, user, etc.).

Bonnes pratiques :
- Définir ici les fixtures réutilisables (mocks, contextes, données de test)
- Ne jamais inclure de secrets ou données sensibles
- Documenter chaque fixture ou hook ajouté
- Prévoir l’extensibilité pour de nouveaux scénarios de test
"""

import pytest

@pytest.fixture
def fake_auth_service_response():
    """
    Fixture fournissant une réponse factice du service d’authentification.
    """
    return {
        "status": "success",
        "user_id": "test_user",
        "token": "fake.jwt.token"
    }

@pytest.fixture
def fake_mail_payload():
    """
    Fixture fournissant un payload d’email factice pour les tests.
    """
    return {
        "recipient": "test@example.com",
        "subject": "Bienvenue sur Dihya Coding",
        "body": "Votre inscription a bien été prise en compte.",
        "sent": True
    }

@pytest.fixture
def service_test_context():
    """
    Fixture simulant un contexte d’appel de service (user, session, etc.).
    """
    return {
        "user_id": "test_user",
        "session_id": "sess_987654",
        "locale": "fr"
    }

# Exemple d’utilisation :
# def test_auth_service(fake_auth_service_response):
#     assert fake_auth_service_response["status"] == "success"