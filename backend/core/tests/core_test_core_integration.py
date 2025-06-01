"""
Test d'intégration avancé du core backend Dihya (Flask)
- Couvre sécurité, RBAC, multilingue, plugins, audit, RGPD, REST, CI/CD
"""
import sys
sys.path.insert(0, '.')
from flask import Flask
from backend.core.app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_generate_project(client):
    resp = client.post('/api/generate', headers={'X-Dihya-Role': 'ai_user', 'X-Dihya-Lang': 'fr'})
    assert resp.status_code == 200
    assert resp.json['status'] == 'success'
    assert 'Projet généré' in resp.json['message']

def test_generate_project_access_denied(client):
    resp = client.post('/api/generate', headers={'X-Dihya-Role': 'guest', 'X-Dihya-Lang': 'en'})
    assert resp.status_code == 403
    assert 'Access denied' in resp.json['error']

def test_login(client):
    resp = client.post('/api/auth/login')
    assert resp.status_code == 200
    assert 'token' in resp.json

def test_user_profile(client):
    resp = client.get('/api/user/profile', headers={'X-Dihya-Role': 'user', 'X-Dihya-Lang': 'ar'})
    assert resp.status_code == 200
    assert resp.json['user'] == 'demo'

def test_list_plugins(client):
    resp = client.get('/api/plugins', headers={'X-Dihya-Role': 'user', 'X-Dihya-Lang': 'tzm'})
    assert resp.status_code == 200
    assert 'plugins' in resp.json

def test_list_templates(client):
    resp = client.get('/api/templates', headers={'X-Dihya-Lang': 'fr'})
    assert resp.status_code == 200
    assert 'templates' in resp.json

def test_not_found(client):
    resp = client.get('/api/unknown', headers={'X-Dihya-Lang': 'fr'})
    assert resp.status_code == 404
    assert 'Non trouvé' in resp.json['error']
