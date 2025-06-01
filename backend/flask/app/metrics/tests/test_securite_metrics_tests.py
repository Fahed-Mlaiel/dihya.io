"""
Tests unitaires pour la collecte des métriques de sécurité (app.metrics.security_metrics) — Dihya Coding.

Vérifie l’incrémentation des accès refusés, des tentatives de connexion échouées, la gestion des alertes et la sécurité d’exposition.
Respecte les bonnes pratiques de sécurité et de conformité RGPD.
"""

import pytest
from flask import Flask
from backend.flask.app.metrics import security_metrics

def test_increment_and_get_security_metrics():
    """Test l’incrémentation des accès refusés, des échecs de login et l’ajout d’alertes."""
    security_metrics._security_metrics["failed_logins"] = 0
    security_metrics._security_metrics["access_denied"] = 0
    security_metrics._security_metrics["alerts"] = []
    security_metrics.increment_failed_login("user1")
    security_metrics.increment_access_denied("user2")
    security_metrics.add_security_alert("Tentative d'injection détectée")
    metrics = security_metrics.get_security_metrics()
    assert metrics["failed_logins"] == 1
    assert metrics["access_denied"] == 1
    assert "Tentative d'injection détectée" in metrics["alerts"]

def make_app():
    """Crée une app Flask de test avec le blueprint security_metrics."""
    app = Flask(__name__)
    app.register_blueprint(security_metrics.security_metrics_blueprint)
    return app

@pytest.fixture
def client(monkeypatch):
    """Client Flask de test avec clé API configurée."""
    app = make_app()
    monkeypatch.setenv("METRICS_API_KEY", "testkey")
    with app.test_client() as client:
        yield client

def test_metrics_endpoint_auth(client):
    """Test que l’endpoint refuse sans clé API et accepte avec la bonne clé."""
    resp = client.get("/metrics/security")
    assert resp.status_code == 403
    resp = client.get("/metrics/security", headers={"X-API-KEY": "testkey"})
    assert resp.status_code == 200
    assert isinstance(resp.get_json(), dict)
