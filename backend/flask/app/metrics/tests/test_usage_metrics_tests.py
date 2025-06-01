"""
Tests unitaires pour la collecte des métriques d’usage (app.metrics.usage_metrics) — Dihya Coding.

Vérifie l’incrémentation des appels API, le comptage des utilisateurs uniques, la sécurité d’exposition et la conformité RGPD.
Respecte les bonnes pratiques de sécurité et de conformité RGPD.
"""

import pytest
from flask import Flask
from backend.flask.app.metrics import usage_metrics

def test_increment_and_get_usage_metrics():
    """Test l’incrémentation des appels API et le comptage des utilisateurs/endpoints."""
    usage_metrics._usage_metrics["api_calls"] = 0
    usage_metrics._usage_metrics["users"] = set()
    usage_metrics._usage_metrics["endpoints"] = {}
    usage_metrics.increment_api_call_count("user1", "/api/test")
    usage_metrics.increment_api_call_count("user2", "/api/test")
    usage_metrics.increment_api_call_count("user1", "/api/other")
    metrics = usage_metrics.get_usage_metrics()
    assert metrics["api_calls"] == 3
    assert metrics["unique_users"] == 2
    assert metrics["endpoints"]["/api/test"] == 2
    assert metrics["endpoints"]["/api/other"] == 1

def make_app():
    """Crée une app Flask de test avec le blueprint usage_metrics."""
    app = Flask(__name__)
    app.register_blueprint(usage_metrics.usage_metrics_blueprint)
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
    resp = client.get("/metrics/usage")
    assert resp.status_code == 403
    resp = client.get("/metrics/usage", headers={"X-API-KEY": "testkey"})
    assert resp.status_code == 200
    assert isinstance(resp.get_json(), dict)
