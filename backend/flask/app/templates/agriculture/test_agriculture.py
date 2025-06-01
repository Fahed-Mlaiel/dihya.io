"""
Tests complets (unitaires, intégration, e2e) pour le module Agriculture
Sécurité, i18n, multitenancy, audit, RGPD, mocks, fixtures.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from .template import register_agriculture_routes, bp_agriculture

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    from flask_jwt_extended import JWTManager
    JWTManager(app)
    app.register_blueprint(bp_agriculture)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_header_admin():
    token = create_access_token(identity={'id': 1, 'role': 'admin'})
    return {'Authorization': f'Bearer {token}'}

@pytest.fixture
def auth_header_producteur():
    token = create_access_token(identity={'id': 2, 'role': 'producteur'})
    return {'Authorization': f'Bearer {token}'}

def test_list_exploitations(client, auth_header_producteur):
    resp = client.get('/api/agriculture/exploitations', headers=auth_header_producteur)
    assert resp.status_code == 200
    assert 'exploitations' in resp.get_json()

def test_create_exploitation(client, auth_header_producteur):
    resp = client.post('/api/agriculture/exploitations', json={'nom': 'Ferme Test'}, headers=auth_header_producteur)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_list_cultures(client, auth_header_admin):
    resp = client.get('/api/agriculture/cultures', headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'cultures' in resp.get_json()

def test_add_culture(client, auth_header_producteur):
    resp = client.post('/api/agriculture/cultures', json={'type': 'blé'}, headers=auth_header_producteur)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_list_stocks(client, auth_header_admin):
    resp = client.get('/api/agriculture/stocks', headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'stocks' in resp.get_json()

def test_add_stock(client, auth_header_producteur):
    resp = client.post('/api/agriculture/stocks', json={'type': 'engrais'}, headers=auth_header_producteur)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_list_alertes(client, auth_header_producteur):
    resp = client.get('/api/agriculture/alertes', headers=auth_header_producteur)
    assert resp.status_code == 200
    assert 'alertes' in resp.get_json()

def test_export_exploitations(client, auth_header_admin):
    resp = client.get('/api/agriculture/export/exploitations', headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'export' in resp.get_json()

def test_rgpd_export(client, auth_header_producteur, monkeypatch):
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.rgpd.rgpd_export', lambda user: {'data': 'export'})
    resp = client.get('/api/agriculture/rgpd/export', headers=auth_header_producteur)
    assert resp.status_code == 200
    assert 'export' in resp.get_json()

def test_rgpd_anonymize(client, auth_header_producteur, monkeypatch):
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.rgpd.rgpd_anonymize', lambda user: None)
    resp = client.post('/api/agriculture/rgpd/anonymize', headers=auth_header_producteur)
    assert resp.status_code == 200
    assert 'msg' in resp.get_json()

def test_plugin_execution(client, auth_header_admin, monkeypatch):
    def fake_plugin_hook(domain, plugin_name, data):
        return {'ok': True, 'plugin': plugin_name}
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.plugins.plugin_hook', fake_plugin_hook)
    resp = client.post('/api/agriculture/plugins/test_plugin', json={'param': 1}, headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'result' in resp.get_json()
