"""
Tests avancés hooks métier, DWeb/IPFS, sectorisation – Dihya Coding
"""
from backend.flask.monitoring import alerting, healthcheck

def test_alerting_hook_sector():
    event = {'event': 'alert'}
    result = alerting.alerting_hook(event, sector='ecommerce')
    assert result['sector'] == 'ecommerce'

def test_export_alerts_to_ipfs():
    assert alerting.export_alerts_to_ipfs() is True

def test_healthcheck_hook_sector():
    event = {'event': 'healthcheck'}
    result = healthcheck.healthcheck_hook(event, sector='santé')
    assert result['sector'] == 'santé'

def test_export_healthchecks_to_ipfs():
    assert healthcheck.export_healthchecks_to_ipfs() is True
