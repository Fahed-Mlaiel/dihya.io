"""
Tests d’intégration pour la gestion des webhooks dans Dihya Coding.

Ce module vérifie la réception, la validation et le traitement sécurisé des webhooks entrants,
ainsi que l’envoi correct des webhooks sortants vers des services externes.

Bonnes pratiques :
- Tester la validation des payloads (schéma, signature…).
- Vérifier la gestion des erreurs et des cas limites.
- Ne jamais inclure de secrets ou de données sensibles dans les tests.
- Logger les résultats pour audit.
"""

import pytest
from flask import Flask, request, jsonify

from backend.flask.integrations import send_webhook, handle_incoming_webhook

@pytest.fixture
def app():
    app = Flask(__name__)

    @app.route("/webhook", methods=["POST"])
    def webhook():
        return jsonify(handle_incoming_webhook(request))

    return app

def test_handle_incoming_webhook(client):
    payload = {"event": "test", "data": {"foo": "bar"}}
    response = client.post("/webhook", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "received"
    assert data["data"] == payload

def test_send_webhook(monkeypatch):
    url = "https://example.com/webhook"
    payload = {"event": "test_send"}
    # Mock requests.post pour éviter un vrai appel HTTP
    class MockResponse:
        def raise_for_status(self): pass
        def json(self): return {"success": True}
    def mock_post(*args, **kwargs):
        return MockResponse()
    import requests
    monkeypatch.setattr(requests, "post", mock_post)
    result = send_webhook(url, payload)
    assert result == {"success": True}
