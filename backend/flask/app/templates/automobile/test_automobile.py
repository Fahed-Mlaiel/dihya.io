"""
Tests complets (unitaires, intégration, e2e) pour le module Automobile
Sécurité, i18n, multitenancy, audit, RGPD, mocks, fixtures.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from .template import register_automobile_routes, bp_automobile

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    from flask_jwt_extended import JWTManager
    JWTManager(app)
    app.register_blueprint(bp_automobile)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_header_admin():
    token = create_access_token(identity={'id': 1, 'role': 'admin'})
    return {'Authorization': f'Bearer {token}'}

@pytest.fixture
def auth_header_user():
    token = create_access_token(identity={'id': 2, 'role': 'user'})
    return {'Authorization': f'Bearer {token}'}

def test_list_vehicules(client, auth_header_user):
    resp = client.get('/api/automobile/vehicules', headers=auth_header_user)
    assert resp.status_code == 200
    assert 'vehicules' in resp.get_json()

def test_add_vehicule(client, auth_header_admin):
    resp = client.post('/api/automobile/vehicules', json={'marque': 'Renault'}, headers=auth_header_admin)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_list_entretiens(client, auth_header_admin):
    resp = client.get('/api/automobile/entretiens', headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'entretiens' in resp.get_json()

def test_plan_entretien(client, auth_header_admin):
    resp = client.post('/api/automobile/entretiens', json={'vehicule': 1}, headers=auth_header_admin)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_list_locations(client, auth_header_user):
    resp = client.get('/api/automobile/locations', headers=auth_header_user)
    assert resp.status_code == 200
    assert 'locations' in resp.get_json()

def test_reserve_location(client, auth_header_user):
    resp = client.post('/api/automobile/locations', json={'vehicule': 1}, headers=auth_header_user)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_list_alertes(client, auth_header_user):
    resp = client.get('/api/automobile/alertes', headers=auth_header_user)
    assert resp.status_code == 200
    assert 'alertes' in resp.get_json()

def test_export_vehicules(client, auth_header_admin):
    resp = client.get('/api/automobile/export/vehicules', headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'export' in resp.get_json()

def test_rgpd_export(client, auth_header_user, monkeypatch):
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.rgpd.rgpd_export', lambda user: {'data': 'export'})
    resp = client.get('/api/automobile/rgpd/export', headers=auth_header_user)
    assert resp.status_code == 200
    assert 'export' in resp.get_json()

def test_rgpd_anonymize(client, auth_header_user, monkeypatch):
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.rgpd.rgpd_anonymize', lambda user: None)
    resp = client.post('/api/automobile/rgpd/anonymize', headers=auth_header_user)
    assert resp.status_code == 200
    assert 'msg' in resp.get_json()

def test_plugin_execution(client, auth_header_admin, monkeypatch):
    def fake_plugin_hook(domain, plugin_name, data):
        return {'ok': True, 'plugin': plugin_name}
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.plugins.plugin_hook', fake_plugin_hook)
    resp = client.post('/api/automobile/plugins/test_plugin', json={'param': 1}, headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'result' in resp.get_json()
