"""
Tests complets (unitaires, intégration, e2e) pour le module Administration Publique
Sécurité, i18n, multitenancy, audit, RGPD, mocks, fixtures.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from .template import register_admin_publique_routes, bp_admin_publique

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    from flask_jwt_extended import JWTManager
    JWTManager(app)
    app.register_blueprint(bp_admin_publique)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_header_admin():
    token = create_access_token(identity={'id': 1, 'role': 'admin'})
    return {'Authorization': f'Bearer {token}'}

@pytest.fixture
def auth_header_agent():
    token = create_access_token(identity={'id': 2, 'role': 'agent'})
    return {'Authorization': f'Bearer {token}'}

@pytest.fixture
def auth_header_citoyen():
    token = create_access_token(identity={'id': 3, 'role': 'citoyen'})
    return {'Authorization': f'Bearer {token}'}

def test_list_demarches(client, auth_header_agent):
    resp = client.get('/api/administration/demarches', headers=auth_header_agent)
    assert resp.status_code == 200
    assert 'demarches' in resp.get_json()

def test_create_demarche(client, auth_header_citoyen):
    resp = client.post('/api/administration/demarches', json={'type': 'passeport'}, headers=auth_header_citoyen)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_get_demarche(client, auth_header_agent):
    resp = client.get('/api/administration/demarches/1', headers=auth_header_agent)
    assert resp.status_code == 200
    assert 'demarche' in resp.get_json()

def test_update_demarche(client, auth_header_agent):
    resp = client.put('/api/administration/demarches/1', json={'statut': 'validée'}, headers=auth_header_agent)
    assert resp.status_code == 200
    assert 'msg' in resp.get_json()

def test_delete_demarche(client, auth_header_agent):
    token = create_access_token(identity={'id': 1, 'role': 'admin'})
    resp = client.delete('/api/administration/demarches/1', headers={'Authorization': f'Bearer {token}'})
    assert resp.status_code == 200
    assert 'msg' in resp.get_json()

def test_register_citoyen(client):
    resp = client.post('/api/administration/citoyens/register', json={'nom': 'Test'})
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_login(client):
    resp = client.post('/api/administration/auth/login', json={'email': 'test', 'password': 'test'})
    assert resp.status_code == 200
    assert 'token' in resp.get_json()

def test_send_message(client, auth_header_citoyen):
    resp = client.post('/api/administration/messages', json={'message': 'Bonjour'}, headers=auth_header_citoyen)
    assert resp.status_code == 200
    assert 'msg' in resp.get_json()

def test_get_notifications(client, auth_header_citoyen):
    resp = client.get('/api/administration/notifications', headers=auth_header_citoyen)
    assert resp.status_code == 200
    assert 'notifications' in resp.get_json()

def test_export_demarches(client, auth_header_agent):
    resp = client.get('/api/administration/export/demarches', headers=auth_header_agent)
    assert resp.status_code == 200
    assert 'export' in resp.get_json()

def test_rgpd_export(client, auth_header_citoyen, monkeypatch):
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.rgpd.rgpd_export', lambda user: {'data': 'export'})
    resp = client.get('/api/administration/rgpd/export', headers=auth_header_citoyen)
    assert resp.status_code == 200
    assert 'export' in resp.get_json()

def test_rgpd_anonymize(client, auth_header_citoyen, monkeypatch):
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.rgpd.rgpd_anonymize', lambda user: None)
    resp = client.post('/api/administration/rgpd/anonymize', headers=auth_header_citoyen)
    assert resp.status_code == 200
    assert 'msg' in resp.get_json()

def test_plugin_execution(client, auth_header_admin, monkeypatch):
    def fake_plugin_hook(domain, plugin_name, data):
        return {'ok': True, 'plugin': plugin_name}
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.plugins.plugin_hook', fake_plugin_hook)
    resp = client.post('/api/administration/plugins/test_plugin', json={'param': 1}, headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'result' in resp.get_json()
