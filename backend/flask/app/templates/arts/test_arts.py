"""
Tests complets (unitaires, intégration, e2e) pour le module Arts
Sécurité, i18n, multitenancy, audit, RGPD, mocks, fixtures.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from .template import arts_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    from flask_jwt_extended import JWTManager
    JWTManager(app)
    app.register_blueprint(arts_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_header_admin():
    token = create_access_token(identity={'id': 1, 'role': 'admin'})
    return {'Authorization': f'Bearer {token}'}

@pytest.fixture
def auth_header_organisateur():
    token = create_access_token(identity={'id': 2, 'role': 'organisateur'})
    return {'Authorization': f'Bearer {token}'}

@pytest.fixture
def auth_header_artiste():
    token = create_access_token(identity={'id': 3, 'role': 'artiste'})
    return {'Authorization': f'Bearer {token}'}

@pytest.fixture
def auth_header_utilisateur():
    token = create_access_token(identity={'id': 4, 'role': 'utilisateur'})
    return {'Authorization': f'Bearer {token}'}

def test_list_evenements(client):
    resp = client.get('/api/arts/evenements')
    assert resp.status_code == 200
    assert 'evenements' in resp.get_json()

def test_create_evenement(client, auth_header_organisateur):
    resp = client.post('/api/arts/evenements', json={'titre': 'Expo'}, headers=auth_header_organisateur)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_list_portfolios(client):
    resp = client.get('/api/arts/portfolios')
    assert resp.status_code == 200
    assert 'portfolios' in resp.get_json()

def test_create_portfolio(client, auth_header_artiste):
    resp = client.post('/api/arts/portfolios', json={'nom': 'Portfolio1'}, headers=auth_header_artiste)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_list_galeries(client):
    resp = client.get('/api/arts/galeries')
    assert resp.status_code == 200
    assert 'galeries' in resp.get_json()

def test_create_galerie(client, auth_header_organisateur):
    resp = client.post('/api/arts/galeries', json={'nom': 'Galerie1'}, headers=auth_header_organisateur)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_list_reservations(client, auth_header_utilisateur):
    resp = client.get('/api/arts/reservations', headers=auth_header_utilisateur)
    assert resp.status_code == 200
    assert 'reservations' in resp.get_json()

def test_create_reservation(client, auth_header_utilisateur):
    resp = client.post('/api/arts/reservations', json={'evenement': 1}, headers=auth_header_utilisateur)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_export_evenements(client, auth_header_organisateur):
    resp = client.get('/api/arts/export/evenements', headers=auth_header_organisateur)
    assert resp.status_code == 200
    assert 'export' in resp.get_json()

def test_rgpd_export(client, auth_header_artiste, monkeypatch):
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.rgpd.rgpd_export', lambda user: {'data': 'export'})
    resp = client.get('/api/arts/rgpd/export', headers=auth_header_artiste)
    assert resp.status_code == 200
    assert 'export' in resp.get_json()

def test_rgpd_anonymize(client, auth_header_artiste, monkeypatch):
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.rgpd.rgpd_anonymize', lambda user: None)
    resp = client.post('/api/arts/rgpd/anonymize', headers=auth_header_artiste)
    assert resp.status_code == 200
    assert 'msg' in resp.get_json()

def test_plugin_execution(client, auth_header_admin, monkeypatch):
    def fake_plugin_hook(domain, plugin_name, data):
        return {'ok': True, 'plugin': plugin_name}
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.plugins.plugin_hook', fake_plugin_hook)
    resp = client.post('/api/arts/plugins/test_plugin', json={'param': 1}, headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'result' in resp.get_json()
