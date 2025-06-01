"""
Tests avancés logs/scripts – Dihya Coding
- RGPD, anonymisation, hooks métier, DWeb/IPFS, sectorisation, audit, souveraineté, CI/CD
"""
import pytest
from backend.flask.logs.scripts import main, purge_logs

def test_logs_hook_sector():
    event = {'event': 'log'}
    result = main.logs_hook(event, sector='santé')
    assert result['sector'] == 'santé'

def test_export_logs_to_ipfs():
    assert main.export_logs_to_ipfs() is True

def test_purge_logs_hook_sector():
    event = {'event': 'purge'}
    result = purge_logs.purge_logs_hook(event, sector='ecommerce')
    assert result['sector'] == 'ecommerce'

def test_export_purged_logs_to_ipfs():
    assert purge_logs.export_purged_logs_to_ipfs() is True
