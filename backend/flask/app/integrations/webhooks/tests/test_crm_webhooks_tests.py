"""
Tests unitaires et d’intégration pour les webhooks CRM – Dihya Coding.

Ce fichier vérifie la bonne réception, validation et traitement des webhooks CRM,
en simulant différents scénarios métier et de sécurité.

Bonnes pratiques :
- Utiliser des fixtures pour les payloads et contextes (voir conftest.py)
- Tester les cas de succès, d’erreur, et de sécurité (signature, format, etc.)
- Ne jamais utiliser de données réelles ou sensibles
- Documenter chaque scénario de test
"""

import pytest
from flask import Flask
from backend.flask.app.integrations.webhooks.crm_webhooks import handle_crm_webhook

@pytest.fixture
def app():
    """
    Application Flask minimale pour les tests de webhooks.
    """
    app = Flask(__name__)
    app.config["TESTING"] = True
    return app

def test_crm_webhook_success(app, fake_webhook_payload, webhook_context):
    """
    Teste la réception et le traitement correct d’un webhook CRM valide.
    """
    with app.app_context():
        response = handle_crm_webhook(fake_webhook_payload, webhook_context)
        assert response["status"] == "success"
        assert "event" in response

def test_crm_webhook_invalid_signature(app, fake_webhook_payload, webhook_context):
    """
    Teste le rejet d’un webhook CRM avec une signature invalide.
    """
    webhook_context["headers"]["X-Webhook-Signature"] = "invalid"
    with app.app_context():
        response = handle_crm_webhook(fake_webhook_payload, webhook_context)
        assert response["status"] == "error"
        assert response["reason"] == "invalid_signature"

def test_crm_webhook_missing_data(app, webhook_context):
    """
    Teste le rejet d’un webhook CRM avec un payload incomplet.
    """
    incomplete_payload = {"event": "user.created"}
    with app.app_context():
        response = handle_crm_webhook(incomplete_payload, webhook_context)
        assert response["status"] == "error"
        assert response["reason"] == "invalid_payload"
