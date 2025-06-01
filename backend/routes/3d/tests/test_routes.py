import pytest
from ..routes import app

# Exemple de test avancé pour endpoint 3D

def test_get_threedprojects(client):
    response = client.get('/threedprojects/')
    assert response.status_code == 200
    assert 'projects' in response.json

def test_post_threedprojects(client):
    data = {'name': 'Projet Test', 'description': 'Test', 'owner': 'admin'}
    response = client.post('/threedprojects/', json=data)
    assert response.status_code == 201
    assert response.json['name'] == 'Projet Test'
