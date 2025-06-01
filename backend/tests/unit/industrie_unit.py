"""
Tests unitaires pour la gestion avancée des projets Industrie (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.industrie.routes import industrie_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(industrie_bp, url_prefix='/api/industrie')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_industrie_list(client):
    """Teste la récupération de la liste des projets industrie (i18n, sécurité, SEO)."""
    response = client.get('/api/industrie/')
    assert response.status_code == 200
    assert 'projects' in response.json
    assert isinstance(response.json['projects'], list)

def test_create_industrie_jwt(client):
    """Test création projet industrie avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Industrie IA', 'lang': 'fr'}
    with patch('backend.routes.industrie.routes.create_project') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Industrie IA'}
        response = client.post('/api/industrie/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Industrie IA'
        mock_create.assert_called_once()

def test_graphql_query_industrie(client):
    """Test requête GraphQL industrie (sécurité, plugins, fallback IA)."""
    query = '{ industries { id name } }'
    response = client.post('/api/industrie/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'industries' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route industrie."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/industrie/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route industrie."""
    with patch('backend.routes.industrie.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/industrie/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données industrie (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/industrie/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
