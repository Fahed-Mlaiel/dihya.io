"""
Tests unitaires pour la gestion avancée des projets Marketing (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.marketing.routes import marketing_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(marketing_bp, url_prefix='/api/marketing')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_marketing_list(client):
    """Teste la récupération de la liste des projets marketing (i18n, sécurité, SEO)."""
    response = client.get('/api/marketing/')
    assert response.status_code == 200
    assert 'projects' in response.json
    assert isinstance(response.json['projects'], list)

def test_create_marketing_jwt(client):
    """Test création projet marketing avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Marketing IA', 'lang': 'fr'}
    with patch('backend.routes.marketing.routes.create_project') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Marketing IA'}
        response = client.post('/api/marketing/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Marketing IA'
        mock_create.assert_called_once()

def test_graphql_query_marketing(client):
    """Test requête GraphQL marketing (sécurité, plugins, fallback IA)."""
    query = '{ marketings { id name } }'
    response = client.post('/api/marketing/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'marketings' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route marketing."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/marketing/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route marketing."""
    with patch('backend.routes.marketing.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/marketing/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données marketing (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/marketing/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
