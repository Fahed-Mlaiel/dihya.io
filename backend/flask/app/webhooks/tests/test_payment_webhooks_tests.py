"""
Tests unitaires pour la gestion des webhooks de paiement (app.webhooks.payment_webhooks) — Dihya Coding.

Vérifie la validation de signature, la gestion des erreurs, la sécurité des endpoints et la conformité RGPD.
Respecte les bonnes pratiques de sécurité et de traçabilité.
"""

import os
import pytest
from flask import Flask
from backend.flask.app.webhooks import payment_webhooks

def make_app():
    """Crée une app Flask de test avec le blueprint payment_webhook."""
    app = Flask(__name__)
    app.register_blueprint(payment_webhooks.payment_webhook_blueprint, url_prefix="/webhooks/payment")
    return app

def sign_payload(payload: bytes, secret: str) -> str:
    """Génère une signature HMAC-SHA256 pour le payload."""
    import hmac, hashlib
    return hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()

@pytest.fixture
def client(monkeypatch):
    """Client Flask de test avec secret configuré."""
    app = make_app()
    secret = "test_secret"
    monkeypatch.setenv("PAYMENT_WEBHOOK_SECRET", secret)
    with app.test_client() as client:
        yield client

def test_webhook_valid_signature(client):
    """Test réception d'un webhook avec signature valide."""
    payload = b'{"event":"payment_succeeded","payment_id":"pay_1","user_id":"u1"}'
    secret = os.environ["PAYMENT_WEBHOOK_SECRET"]
    signature = sign_payload(payload, secret)
    resp = client.post(
        "/webhooks/payment/",
        data=payload,
        headers={"Content-Type": "application/json", "X-Signature": signature}
    )
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "success"

def test_webhook_invalid_signature(client):
    """Test rejet d'un webhook avec signature invalide."""
    payload = b'{"event":"payment_succeeded","payment_id":"pay_1","user_id":"u1"}'
    resp = client.post(
        "/webhooks/payment/",
        data=payload,
        headers={"Content-Type": "application/json", "X-Signature": "bad_signature"}
    )
    assert resp.status_code == 400

def test_webhook_missing_fields(client):
    """Test rejet si champs obligatoires manquants."""
    payload = b'{"event":"payment_succeeded"}'
    secret = os.environ["PAYMENT_WEBHOOK_SECRET"]
    signature = sign_payload(payload, secret)
    resp = client.post(
        "/webhooks/payment/",
        data=payload,
        headers={"Content-Type": "application/json", "X-Signature": signature}
    )
    assert resp.status_code == 400

def test_webhook_invalid_json(client):
    """Test rejet si payload JSON invalide."""
    payload = b'{invalid json'
    secret = os.environ["PAYMENT_WEBHOOK_SECRET"]
    signature = sign_payload(payload, secret)
    resp = client.post(
        "/webhooks/payment/",
        data=payload,
        headers={"Content-Type": "application/json", "X-Signature": signature}
    )
    assert resp.status_code == 400

def test_webhook_no_secret(monkeypatch):
    """Test erreur serveur si secret manquant en config."""
    app = make_app()
    monkeypatch.delenv("PAYMENT_WEBHOOK_SECRET", raising=False)
    with app.test_client() as client:
        payload = b'{"event":"payment_succeeded","payment_id":"pay_1"}'
        resp = client.post(
            "/webhooks/payment/",
            data=payload,
            headers={"Content-Type": "application/json", "X-Signature": "sig"}
        )
        assert resp.status_code == 500