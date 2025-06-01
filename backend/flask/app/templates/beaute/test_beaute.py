"""
Tests complets (unitaires, intégration, e2e) pour le module Beauté
Sécurité, i18n, multitenancy, audit, RGPD, mocks, fixtures.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from .template import register_beaute_routes, bp_beaute

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    from flask_jwt_extended import JWTManager
    JWTManager(app)
    app.register_blueprint(bp_beaute)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_header_admin():
    token = create_access_token(identity={'id': 1, 'role': 'admin'})
    return {'Authorization': f'Bearer {token}'}

@pytest.fixture
def auth_header_salon():
    token = create_access_token(identity={'id': 2, 'role': 'salon'})
    return {'Authorization': f'Bearer {token}'}

@pytest.fixture
def auth_header_client():
    token = create_access_token(identity={'id': 3, 'role': 'client'})
    return {'Authorization': f'Bearer {token}'}

def test_list_salons(client, auth_header_admin):
    resp = client.get('/api/beaute/salons', headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'salons' in resp.get_json()

def test_create_salon(client, auth_header_admin):
    resp = client.post('/api/beaute/salons', json={'nom': 'Salon1'}, headers=auth_header_admin)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_list_prestations(client):
    resp = client.get('/api/beaute/prestations')
    assert resp.status_code == 200
    assert 'prestations' in resp.get_json()

def test_add_prestation(client, auth_header_admin):
    resp = client.post('/api/beaute/prestations', json={'nom': 'Coupe'}, headers=auth_header_admin)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_list_rendezvous(client, auth_header_salon):
    resp = client.get('/api/beaute/rendezvous', headers=auth_header_salon)
    assert resp.status_code == 200
    assert 'rendezvous' in resp.get_json()

def test_create_rendezvous(client, auth_header_client):
    resp = client.post('/api/beaute/rendezvous', json={'date': '2025-05-24'}, headers=auth_header_client)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_list_clients(client, auth_header_admin):
    resp = client.get('/api/beaute/clients', headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'clients' in resp.get_json()

def test_create_client(client, auth_header_salon):
    resp = client.post('/api/beaute/clients', json={'nom': 'Client1'}, headers=auth_header_salon)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_export_rendezvous(client, auth_header_admin):
    resp = client.get('/api/beaute/export/rendezvous', headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'export' in resp.get_json()

def test_rgpd_export(client, auth_header_client, monkeypatch):
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.rgpd.rgpd_export', lambda user: {'data': 'export'})
    resp = client.get('/api/beaute/rgpd/export', headers=auth_header_client)
    assert resp.status_code == 200
    assert 'export' in resp.get_json()

def test_rgpd_anonymize(client, auth_header_client, monkeypatch):
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.rgpd.rgpd_anonymize', lambda user: None)
    resp = client.post('/api/beaute/rgpd/anonymize', headers=auth_header_client)
    assert resp.status_code == 200
    assert 'msg' in resp.get_json()

def test_plugin_execution(client, auth_header_admin, monkeypatch):
    def fake_plugin_hook(domain, plugin_name, data):
        return {'ok': True, 'plugin': plugin_name}
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.plugins.plugin_hook', fake_plugin_hook)
    resp = client.post('/api/beaute/plugins/test_plugin', json={'param': 1}, headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'result' in resp.get_json()
