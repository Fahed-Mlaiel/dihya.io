"""
Fichier de configuration des tests (conftest) pour le module Realtime – Dihya Coding.

Ce fichier centralise les fixtures, hooks et configurations Pytest
pour les tests unitaires et d’intégration du serveur temps réel (WebSocket, events, etc.).

Bonnes pratiques :
- Définir ici les fixtures réutilisables (mocks, contextes, données de test)
- Ne jamais inclure de secrets ou données sensibles
- Documenter chaque fixture ou hook ajouté
- Prévoir l’extensibilité pour de nouveaux scénarios de test
"""

import pytest

@pytest.fixture
def fake_realtime_event():
    """
    Fixture fournissant un événement temps réel factice pour les tests.
    """
    return {
        "type": "message",
        "channel": "general",
        "payload": {"text": "Hello, world!", "user_id": "test_user"},
        "timestamp": "2025-05-15T12:00:00Z"
    }

@pytest.fixture
def realtime_context():
    """
    Fixture simulant un contexte de connexion temps réel (utilisateur, permissions, etc.).
    """
    return {
        "user_id": "test_user",
        "roles": ["user"],
        "channels": ["general", "support"]
    }

# Exemple d’utilisation :
# def test_realtime_event(fake_realtime_event):
#     assert fake_realtime_event["type"] == "message"