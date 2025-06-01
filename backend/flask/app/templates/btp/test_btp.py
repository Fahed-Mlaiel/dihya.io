"""
Tests avancés module BTP (unitaires, intégration, e2e, sécurité, i18n, plugins).
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from backend.flask.app.templates.btp import btp_bp

@pytest.fixture
def client():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    app.register_blueprint(btp_bp)
    # ... setup JWT, plugins, etc. ...
    with app.test_client() as client:
        yield client

def test_list_btp(client):
    token = create_access_token(identity={'role': 'admin'})
    rv = client.get('/api/btp/', headers={'Authorization': f'Bearer {token}'})
    assert rv.status_code == 200
    assert 'data' in rv.json

def test_create_btp(client):
    token = create_access_token(identity={'role': 'admin'})
    rv = client.post('/api/btp/', json={'name': 'Test'}, headers={'Authorization': f'Bearer {token}'})
    assert rv.status_code == 200 or rv.status_code == 201

# ... autres tests : sécurité, plugins, i18n, audit, export, etc. ...
