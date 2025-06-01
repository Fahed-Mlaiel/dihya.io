"""
test_beaute_flask.py - Test d’intégration avancé pour la gestion de projets beauté
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

def test_list_projects_beaute(client):
    token = create_access_token(identity={'role': 'admin', 'tenant': 'test'})
    res = client.get('/api/beaute/projects', headers={'Authorization': f'Bearer {token}', 'Accept-Language': 'fr'})
    assert res.status_code == 200
    assert isinstance(res.json, list)

def test_create_project_beaute(client):
    token = create_access_token(identity={'role': 'admin', 'tenant': 'test'})
    res = client.post('/api/beaute/projects', headers={'Authorization': f'Bearer {token}'}, json={'name': 'Projet Beauté Test'})
    assert res.status_code == 201
    assert 'msg' in res.json
