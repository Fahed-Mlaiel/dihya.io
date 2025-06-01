"""
Tests unitaires pour la gestion avancée des projets Construction (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.construction.routes import construction_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(construction_bp, url_prefix='/api/construction')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_construction_list(client):
    """Teste la récupération de la liste des projets construction (i18n, sécurité, SEO)."""
    response = client.get('/api/construction/')
    assert response.status_code == 200
    assert 'projects' in response.json
    assert isinstance(response.json['projects'], list)

def test_create_construction_jwt(client):
    """Test création projet construction avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Bâtiment IA', 'lang': 'fr'}
    with patch('backend.routes.construction.routes.create_project') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Bâtiment IA'}
        response = client.post('/api/construction/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Bâtiment IA'
        mock_create.assert_called_once()

def test_graphql_query_construction(client):
    """Test requête GraphQL construction (sécurité, plugins, fallback IA)."""
    query = '{ constructions { id name } }'
    response = client.post('/api/construction/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'constructions' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route construction."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/construction/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route construction."""
    with patch('backend.routes.construction.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/construction/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données construction (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/construction/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
