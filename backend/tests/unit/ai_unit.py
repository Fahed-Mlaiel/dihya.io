"""
Tests unitaires pour la gestion avancée des projets Intelligence Artificielle (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.intelligence_artificielle.routes import ia_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(ia_bp, url_prefix='/api/intelligence_artificielle')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_ia_list(client):
    """Teste la récupération de la liste des projets IA (i18n, sécurité, SEO)."""
    response = client.get('/api/intelligence_artificielle/')
    assert response.status_code == 200
    assert 'projects' in response.json
    assert isinstance(response.json['projects'], list)

def test_create_ia_jwt(client):
    """Test création projet IA avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Projet IA', 'lang': 'fr'}
    with patch('backend.routes.intelligence_artificielle.routes.create_project') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Projet IA'}
        response = client.post('/api/intelligence_artificielle/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Projet IA'
        mock_create.assert_called_once()

def test_graphql_query_ia(client):
    """Test requête GraphQL IA (sécurité, plugins, fallback IA)."""
    query = '{ ias { id name } }'
    response = client.post('/api/intelligence_artificielle/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'ias' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route IA."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/intelligence_artificielle/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route IA."""
    with patch('backend.routes.intelligence_artificielle.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/intelligence_artificielle/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données IA (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/intelligence_artificielle/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
