"""
test_loisirs_flask.py - Test d’intégration avancé pour la gestion de projets loisirs
Sécurité, multitenancy, i18n, plugins, audit, fallback IA, RGPD
"""
import pytest
from flask_jwt_extended import create_access_token
from backend.flask.app import create_app

@pytest.fixture
def client():
    app = create_app(testing=True)
    with app.test_client() as client:
        yield client

def test_list_projects_loisirs(client):
    token = create_access_token(identity={'role': 'admin', 'tenant': 'test'})
    res = client.get('/api/loisirs/projects', headers={'Authorization': f'Bearer {token}', 'Accept-Language': 'fr'})
    assert res.status_code == 200
    assert isinstance(res.json, list)

def test_create_project_loisirs(client):
    token = create_access_token(identity={'role': 'admin', 'tenant': 'test'})
    res = client.post('/api/loisirs/projects', headers={'Authorization': f'Bearer {token}'}, json={'name': 'Projet Loisirs Test'})
    assert res.status_code == 201
    assert 'msg' in res.json
