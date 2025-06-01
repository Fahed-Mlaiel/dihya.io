# test_monitoring_client.py – Tests unitaires pour Monitoring Client (pytest, mock)
import pytest
from backend.flask.app.api_clients import monitoring_client

@pytest.fixture(autouse=True)
def patch_env(monkeypatch):
    monkeypatch.setenv("PROMETHEUS_PUSHGATEWAY_URL", "http://localhost:9091")
    monkeypatch.setenv("SENTRY_DSN", "dummy-dsn")

@pytest.fixture(autouse=True)
def patch_requests(monkeypatch):
    class DummyResp:
        def raise_for_status(self): pass
    monkeypatch.setattr(monitoring_client.requests, "post", lambda *a, **k: DummyResp())

def test_push_metric_success():
    assert monitoring_client.push_metric("testjob", {"test": 1})

def test_push_metric_no_url(monkeypatch):
    monkeypatch.delenv("PROMETHEUS_PUSHGATEWAY_URL", raising=False)
    assert not monitoring_client.push_metric("testjob", {"test": 1})

def test_send_alert_sentry_success():
    assert monitoring_client.send_alert_sentry("Alerte test", "warning")

def test_send_alert_sentry_no_dsn(monkeypatch):
    monkeypatch.delenv("SENTRY_DSN", raising=False)
    assert not monitoring_client.send_alert_sentry("Alerte test")
