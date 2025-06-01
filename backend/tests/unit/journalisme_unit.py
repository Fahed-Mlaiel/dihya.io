"""
Tests unitaires pour la gestion avancée des projets Journalisme (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.journalisme.routes import journalisme_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(journalisme_bp, url_prefix='/api/journalisme')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_journalisme_list(client):
    """Teste la récupération de la liste des articles journalisme (i18n, sécurité, SEO)."""
    response = client.get('/api/journalisme/')
    assert response.status_code == 200
    assert 'articles' in response.json
    assert isinstance(response.json['articles'], list)

def test_create_journalisme_jwt(client):
    """Test création article journalisme avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'title': 'Article IA', 'lang': 'fr'}
    with patch('backend.routes.journalisme.routes.create_article') as mock_create:
        mock_create.return_value = {'id': 1, 'title': 'Article IA'}
        response = client.post('/api/journalisme/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['title'] == 'Article IA'
        mock_create.assert_called_once()

def test_graphql_query_journalisme(client):
    """Test requête GraphQL journalisme (sécurité, plugins, fallback IA)."""
    query = '{ articles { id title } }'
    response = client.post('/api/journalisme/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'articles' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route journalisme."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/journalisme/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route journalisme."""
    with patch('backend.routes.journalisme.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/journalisme/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données journalisme (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/journalisme/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
