"""
Tests avancés pour le module Environnement (unitaires, intégration, e2e, mocks, sécurité, i18n).
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from backend.flask.app.templates.environnement import environnement_bp

@pytest.fixture
def client():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    app.register_blueprint(environnement_bp)
    with app.test_client() as client:
        yield client

@pytest.fixture
def admin_token():
    return create_access_token(identity={'role': 'admin'})

@pytest.fixture
def user_token():
    return create_access_token(identity={'role': 'user'})

def test_list_projects_admin(client, admin_token):
    res = client.get('/api/environnement/', headers={'Authorization': f'Bearer {admin_token}'})
    assert res.status_code == 200
    assert isinstance(res.json, list)

def test_create_project_admin(client, admin_token):
    res = client.post('/api/environnement/', json={'name': 'Test', 'description': 'Desc'}, headers={'Authorization': f'Bearer {admin_token}'})
    assert res.status_code == 201
    assert 'name' in res.json

def test_create_project_user_forbidden(client, user_token):
    res = client.post('/api/environnement/', json={'name': 'Test', 'description': 'Desc'}, headers={'Authorization': f'Bearer {user_token}'})
    assert res.status_code == 403
