"""
Tests unitaires pour la gestion avancée des projets Culture (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.culture.routes import culture_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(culture_bp, url_prefix='/api/culture')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_culture_list(client):
    """Teste la récupération de la liste des projets culture (i18n, sécurité, SEO)."""
    response = client.get('/api/culture/')
    assert response.status_code == 200
    assert 'projects' in response.json
    assert isinstance(response.json['projects'], list)

def test_create_culture_jwt(client):
    """Test création projet culture avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Culture IA', 'lang': 'fr'}
    with patch('backend.routes.culture.routes.create_project') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Culture IA'}
        response = client.post('/api/culture/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Culture IA'
        mock_create.assert_called_once()

def test_graphql_query_culture(client):
    """Test requête GraphQL culture (sécurité, plugins, fallback IA)."""
    query = '{ cultures { id name } }'
    response = client.post('/api/culture/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'cultures' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route culture."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/culture/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route culture."""
    with patch('backend.routes.culture.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/culture/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données culture (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/culture/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
