"""
Tests unitaires pour la collecte des métriques de performance (app.metrics.performance_metrics) — Dihya Coding.

Vérifie l’enregistrement des temps de réponse, le calcul des moyennes, la gestion des erreurs et la sécurité d’exposition.
Respecte les bonnes pratiques de sécurité et de conformité RGPD.
"""

import pytest
from flask import Flask
from backend.flask.app.metrics import performance_metrics

def test_record_and_get_performance_metrics():
    """Test l’enregistrement et l’agrégation des temps de réponse."""
    performance_metrics._performance_metrics["response_times"].clear()
    performance_metrics._performance_metrics["error_rates"].clear()
    performance_metrics._performance_metrics["total_requests"].clear()
    performance_metrics.record_response_time("/api/test", 100)
    performance_metrics.record_response_time("/api/test", 200)
    performance_metrics.record_response_time("/api/test", 300, error=True)
    metrics = performance_metrics.get_performance_metrics()
    assert "/api/test" in metrics
    assert metrics["/api/test"]["avg_response_time_ms"] == 200
    assert metrics["/api/test"]["max_response_time_ms"] == 300
    assert metrics["/api/test"]["min_response_time_ms"] == 100
    assert metrics["/api/test"]["total_requests"] == 3
    assert metrics["/api/test"]["error_rate"] == pytest.approx(1/3, 0.001)

def make_app():
    """Crée une app Flask de test avec le blueprint performance_metrics."""
    app = Flask(__name__)
    app.register_blueprint(performance_metrics.performance_metrics_blueprint)
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
    resp = client.get("/metrics/performance")
    assert resp.status_code == 403
    resp = client.get("/metrics/performance", headers={"X-API-KEY": "testkey"})
    assert resp.status_code == 200
    assert isinstance(resp.get_json(), dict)
