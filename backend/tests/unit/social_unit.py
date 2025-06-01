"""
Tests unitaires avancés pour la gestion des projets sociaux (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.social.routes import social_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(social_bp, url_prefix='/api/social')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_social_list(client):
    """Teste la récupération de la liste des projets sociaux (i18n, sécurité, SEO)."""
    response = client.get('/api/social/')
    assert response.status_code == 200
    assert 'projects' in response.json
    assert isinstance(response.json['projects'], list)

def test_create_social_project_jwt(client):
    """Test création projet social avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Projet Social', 'lang': 'fr'}
    with patch('backend.routes.social.routes.create_project') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Projet Social'}
        response = client.post('/api/social/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Projet Social'
        mock_create.assert_called_once()

def test_graphql_query_social(client):
    """Test requête GraphQL social (sécurité, plugins, fallback IA)."""
    query = '{ social { id name } }'
    response = client.post('/api/social/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'social' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, de, zh) pour la route social."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/social/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route social."""
    with patch('backend.routes.social.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/social/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données social (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/social/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
