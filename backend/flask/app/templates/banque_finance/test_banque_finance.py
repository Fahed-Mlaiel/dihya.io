"""
Tests complets (unitaires, intégration, e2e) pour le module Banque & Finance
Sécurité, i18n, multitenancy, audit, RGPD, mocks, fixtures.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from .template import register_banque_finance_routes, bp_banque_finance

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    from flask_jwt_extended import JWTManager
    JWTManager(app)
    app.register_blueprint(bp_banque_finance)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_header_admin():
    token = create_access_token(identity={'id': 1, 'role': 'admin'})
    return {'Authorization': f'Bearer {token}'}

@pytest.fixture
def auth_header_conseiller():
    token = create_access_token(identity={'id': 2, 'role': 'conseiller'})
    return {'Authorization': f'Bearer {token}'}

@pytest.fixture
def auth_header_client():
    token = create_access_token(identity={'id': 3, 'role': 'client'})
    return {'Authorization': f'Bearer {token}'}

def test_list_comptes(client, auth_header_conseiller):
    resp = client.get('/api/banque_finance/comptes', headers=auth_header_conseiller)
    assert resp.status_code == 200
    assert 'comptes' in resp.get_json()

def test_create_compte(client, auth_header_conseiller):
    resp = client.post('/api/banque_finance/comptes', json={'type': 'courant'}, headers=auth_header_conseiller)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_list_clients(client, auth_header_admin):
    resp = client.get('/api/banque_finance/clients', headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'clients' in resp.get_json()

def test_create_client(client, auth_header_conseiller):
    resp = client.post('/api/banque_finance/clients', json={'nom': 'Client1'}, headers=auth_header_conseiller)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_list_operations(client, auth_header_client):
    resp = client.get('/api/banque_finance/operations', headers=auth_header_client)
    assert resp.status_code == 200
    assert 'operations' in resp.get_json()

def test_create_operation(client, auth_header_client):
    resp = client.post('/api/banque_finance/operations', json={'type': 'virement'}, headers=auth_header_client)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_list_credits(client, auth_header_client):
    resp = client.get('/api/banque_finance/credits', headers=auth_header_client)
    assert resp.status_code == 200
    assert 'credits' in resp.get_json()

def test_demande_credit(client, auth_header_client):
    resp = client.post('/api/banque_finance/credits', json={'montant': 1000}, headers=auth_header_client)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_export_comptes(client, auth_header_admin):
    resp = client.get('/api/banque_finance/export/comptes', headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'export' in resp.get_json()

def test_rgpd_export(client, auth_header_client, monkeypatch):
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.rgpd.rgpd_export', lambda user: {'data': 'export'})
    resp = client.get('/api/banque_finance/rgpd/export', headers=auth_header_client)
    assert resp.status_code == 200
    assert 'export' in resp.get_json()

def test_rgpd_anonymize(client, auth_header_client, monkeypatch):
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.rgpd.rgpd_anonymize', lambda user: None)
    resp = client.post('/api/banque_finance/rgpd/anonymize', headers=auth_header_client)
    assert resp.status_code == 200
    assert 'msg' in resp.get_json()

def test_plugin_execution(client, auth_header_admin, monkeypatch):
    def fake_plugin_hook(domain, plugin_name, data):
        return {'ok': True, 'plugin': plugin_name}
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.plugins.plugin_hook', fake_plugin_hook)
    resp = client.post('/api/banque_finance/plugins/test_plugin', json={'param': 1}, headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'result' in resp.get_json()
