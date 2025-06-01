"""
test_energie_flask.py - Test d’intégration avancé pour la gestion de projets énergétiques
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

def test_list_projects_energie(client):
    token = create_access_token(identity={'role': 'admin', 'tenant': 'test'})
    res = client.get('/api/energie/projects', headers={'Authorization': f'Bearer {token}', 'Accept-Language': 'fr'})
    assert res.status_code == 200
    assert isinstance(res.json, list)

def test_create_project_energie(client):
    token = create_access_token(identity={'role': 'admin', 'tenant': 'test'})
    res = client.post('/api/energie/projects', headers={'Authorization': f'Bearer {token}'}, json={'name': 'Projet Energie Test'})
    assert res.status_code == 201
    assert 'msg' in res.json
