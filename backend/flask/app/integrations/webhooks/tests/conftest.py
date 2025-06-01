"""
Fichier de configuration des tests (conftest) pour le module Webhooks d’intégration – Dihya Coding.

Ce fichier centralise les fixtures, hooks et configurations Pytest
pour les tests unitaires et d’intégration des webhooks CRM, ERP, paiement, etc.

Bonnes pratiques :
- Définir ici les fixtures réutilisables (payloads, mocks, contextes)
- Ne jamais inclure de secrets ou credentials réels
- Documenter chaque fixture ou hook ajouté
- Prévoir l’extensibilité pour de nouveaux scénarios de test
"""

import pytest

@pytest.fixture
def fake_webhook_payload():
    """
    Fixture fournissant un payload webhook factice pour les tests.
    """
    return {
        "event": "user.created",
        "data": {
            "user_id": "test_user",
            "email": "test@example.com",
            "timestamp": "2025-05-15T12:00:00Z"
        }
    }

@pytest.fixture
def webhook_context():
    """
    Fixture simulant un contexte d’appel webhook (headers, signature, etc.).
    """
    return {
        "headers": {
            "X-Webhook-Signature": "fake-signature",
            "Content-Type": "application/json"
        },
        "ip": "127.0.0.1"
    }

# Exemple d’utilisation :
# def test_webhook_event(fake_webhook_payload):
#     assert fake_webhook_payload["event"] == "user.created"