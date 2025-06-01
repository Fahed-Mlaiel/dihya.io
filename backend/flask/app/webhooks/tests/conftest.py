"""
Fichier de configuration des tests (conftest) pour le module Webhooks – Dihya Coding.

Ce fichier centralise les fixtures, hooks et configurations Pytest
pour les tests unitaires et d’intégration des webhooks internes (CI/CD, notifications, paiement, etc.).

Bonnes pratiques :
- Définir ici les fixtures réutilisables (payloads, mocks, contextes)
- Ne jamais inclure de secrets ou données sensibles
- Documenter chaque fixture ou hook ajouté
- Prévoir l’extensibilité pour de nouveaux scénarios de test
"""

import pytest

@pytest.fixture
def fake_internal_webhook_payload():
    """
    Fixture fournissant un payload webhook interne factice pour les tests.
    """
    return {
        "event": "build.completed",
        "data": {
            "build_id": "build_123",
            "status": "success",
            "timestamp": "2025-05-15T12:00:00Z"
        }
    }

@pytest.fixture
def internal_webhook_context():
    """
    Fixture simulant un contexte d’appel webhook interne (headers, signature, etc.).
    """
    return {
        "headers": {
            "X-Webhook-Signature": "fake-signature",
            "Content-Type": "application/json"
        },
        "ip": "127.0.0.1"
    }

# Exemple d’utilisation :
# def test_internal_webhook_event(fake_internal_webhook_payload):
#     assert fake_internal_webhook_payload["event"] == "build.completed"