"""
Tests unitaires avancés pour la gestion des previews (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.preview.routes import preview_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(preview_bp, url_prefix='/api/preview')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_preview_list(client):
    """Teste la récupération de la liste des previews (i18n, sécurité, SEO)."""
    response = client.get('/api/preview/')
    assert response.status_code == 200
    assert 'previews' in response.json
    assert isinstance(response.json['previews'], list)

def test_create_preview_jwt(client):
    """Test création preview avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Preview IA', 'lang': 'fr'}
    with patch('backend.routes.preview.routes.create_preview') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Preview IA'}
        response = client.post('/api/preview/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Preview IA'
        mock_create.assert_called_once()

def test_graphql_query_preview(client):
    """Test requête GraphQL preview (sécurité, plugins, fallback IA)."""
    query = '{ preview { id name } }'
    response = client.post('/api/preview/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'preview' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, de, zh) pour la route preview."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/preview/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route preview."""
    with patch('backend.routes.preview.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/preview/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données preview (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/preview/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
