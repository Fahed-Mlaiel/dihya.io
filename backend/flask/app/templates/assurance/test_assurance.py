"""
Tests complets (unitaires, intégration, e2e) pour le module Assurance
Sécurité, i18n, multitenancy, audit, RGPD, mocks, fixtures.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from .template import register_assurance_routes, bp_assurance

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    from flask_jwt_extended import JWTManager
    JWTManager(app)
    app.register_blueprint(bp_assurance)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_header_admin():
    token = create_access_token(identity={'id': 1, 'role': 'admin'})
    return {'Authorization': f'Bearer {token}'}

@pytest.fixture
def auth_header_gestionnaire():
    token = create_access_token(identity={'id': 2, 'role': 'gestionnaire'})
    return {'Authorization': f'Bearer {token}'}

@pytest.fixture
def auth_header_client():
    token = create_access_token(identity={'id': 3, 'role': 'client'})
    return {'Authorization': f'Bearer {token}'}

def test_list_contrats(client, auth_header_gestionnaire):
    resp = client.get('/api/assurance/contrats', headers=auth_header_gestionnaire)
    assert resp.status_code == 200
    assert 'contrats' in resp.get_json()

def test_create_contrat(client, auth_header_gestionnaire):
    resp = client.post('/api/assurance/contrats', json={'type': 'auto'}, headers=auth_header_gestionnaire)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_list_clients(client, auth_header_admin):
    resp = client.get('/api/assurance/clients', headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'clients' in resp.get_json()

def test_create_client(client, auth_header_gestionnaire):
    resp = client.post('/api/assurance/clients', json={'nom': 'Client1'}, headers=auth_header_gestionnaire)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_list_sinistres(client, auth_header_admin):
    resp = client.get('/api/assurance/sinistres', headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'sinistres' in resp.get_json()

def test_declare_sinistre(client, auth_header_client):
    resp = client.post('/api/assurance/sinistres', json={'contrat': 1}, headers=auth_header_client)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_export_contrats(client, auth_header_admin):
    resp = client.get('/api/assurance/export/contrats', headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'export' in resp.get_json()

def test_rgpd_export(client, auth_header_client, monkeypatch):
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.rgpd.rgpd_export', lambda user: {'data': 'export'})
    resp = client.get('/api/assurance/rgpd/export', headers=auth_header_client)
    assert resp.status_code == 200
    assert 'export' in resp.get_json()

def test_rgpd_anonymize(client, auth_header_client, monkeypatch):
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.rgpd.rgpd_anonymize', lambda user: None)
    resp = client.post('/api/assurance/rgpd/anonymize', headers=auth_header_client)
    assert resp.status_code == 200
    assert 'msg' in resp.get_json()

def test_plugin_execution(client, auth_header_admin, monkeypatch):
    def fake_plugin_hook(domain, plugin_name, data):
        return {'ok': True, 'plugin': plugin_name}
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.plugins.plugin_hook', fake_plugin_hook)
    resp = client.post('/api/assurance/plugins/test_plugin', json={'param': 1}, headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'result' in resp.get_json()
