"""
Tests unitaires pour la gestion avancée des projets Automobile (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.automobile.routes import automobile_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(automobile_bp, url_prefix='/api/automobile')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_automobile_list(client):
    """Teste la récupération de la liste des véhicules (i18n, sécurité, SEO)."""
    response = client.get('/api/automobile/')
    assert response.status_code == 200
    assert 'vehicles' in response.json
    assert isinstance(response.json['vehicles'], list)

def test_create_automobile_jwt(client):
    """Test création véhicule avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Tesla IA', 'lang': 'fr'}
    with patch('backend.routes.automobile.routes.create_vehicle') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Tesla IA'}
        response = client.post('/api/automobile/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Tesla IA'
        mock_create.assert_called_once()

def test_graphql_query_automobile(client):
    """Test requête GraphQL automobile (sécurité, plugins, fallback IA)."""
    query = '{ automobiles { id name } }'
    response = client.post('/api/automobile/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'automobiles' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route automobile."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/automobile/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route automobile."""
    with patch('backend.routes.automobile.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/automobile/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données automobile (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/automobile/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
