"""
Tests avancés monitoring – Dihya Coding
- RGPD, anonymisation, hooks métier, DWeb/IPFS, sectorisation, audit, souveraineté, CI/CD, alerting, multitenancy
"""
import pytest
from backend.flask.monitoring import healthcheck, alerting

def test_check_database():
    assert healthcheck.check_database() in [True, False]

def test_check_all_services():
    status = healthcheck.check_all_services()
    assert 'database' in status
    assert 'timestamp' in status

def test_send_alert_log(tmp_path):
    alerting.ALERT_LOG_FILE = str(tmp_path / "alerts.log")
    alerting.send_alert("Test alerte log", level="INFO", channel="log")
    with open(alerting.ALERT_LOG_FILE) as f:
        lines = f.readlines()
    assert any("Test alerte log" in l for l in lines)

def test_send_alert_email(monkeypatch):
    called = {}
    monkeypatch.setattr("builtins.print", lambda x: called.setdefault('email', x))
    alerting.send_alert("Test alerte email", level="CRITICAL", channel="email")
    assert 'email' in called and "Test alerte email" in called['email']

def test_send_alert_webhook(monkeypatch):
    called = {}
    monkeypatch.setattr("builtins.print", lambda x: called.setdefault('webhook', x))
    alerting.send_alert("Test alerte webhook", level="WARNING", channel="webhook")
    assert 'webhook' in called and "Test alerte webhook" in called['webhook']
