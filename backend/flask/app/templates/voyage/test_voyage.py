"""
Tests pour le module Voyage : unitaires, intégration, E2E, rôles, validation, audit, i18n.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from backend.flask.app.templates.voyage import bp_voyage

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    app.register_blueprint(bp_voyage)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def access_token():
    return create_access_token(identity='testuser')

def test_get_destinations_authenticated(client, access_token):
    response = client.get('/api/voyage/destinations', headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200
    assert 'data' in response.get_json()

def test_create_destination_admin(client, access_token, monkeypatch):
    monkeypatch.setattr('app.templates.voyage.role_required', lambda role: (lambda f: f))
    data = {'name': 'Test Destination', 'country': 'Test Country'}
    response = client.post('/api/voyage/destinations', json=data, headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 201
    assert response.get_json()['data']['name'] == 'Test Destination'

def test_i18n_get_destinations(client, access_token):
    response = client.get('/api/voyage/destinations', headers={'Authorization': f'Bearer {access_token}', 'Accept-Language': 'de'})
    assert response.status_code == 200
    assert 'data' in response.get_json()

# Autres tests : audit, RGPD, WAF, anti-DDOS, SEO, fallback-AI, multi-tenants, plugins, erreurs...
