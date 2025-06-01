"""
Fichier de configuration des tests (conftest) pour le module Notifications – Dihya Coding.

Ce fichier centralise les fixtures, hooks et configurations Pytest
pour les tests unitaires et d’intégration du système de notifications (mail, push, in-app).

Bonnes pratiques :
- Définir ici les fixtures réutilisables (mocks, contextes, données de test)
- Ne jamais inclure de secrets ou données sensibles
- Documenter chaque fixture ou hook ajouté
- Prévoir l’extensibilité pour de nouveaux scénarios de test
"""

import pytest

@pytest.fixture
def fake_notification_payload():
    """
    Fixture fournissant un payload de notification factice pour les tests.
    """
    return {
        "type": "email",
        "recipient": "test@example.com",
        "subject": "Bienvenue sur Dihya Coding",
        "message": "Votre inscription a bien été prise en compte.",
        "timestamp": "2025-05-15T12:00:00Z"
    }

@pytest.fixture
def notification_context():
    """
    Fixture simulant un contexte d’envoi de notification (user, canal, etc.).
    """
    return {
        "user_id": "test_user",
        "channel": "email",
        "locale": "fr"
    }

# Exemple d’utilisation :
# def test_notification_payload(fake_notification_payload):
#     assert fake_notification_payload["type"] == "email"