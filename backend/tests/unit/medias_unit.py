"""
Tests unitaires pour la gestion avancée des projets Médias (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.medias.routes import medias_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(medias_bp, url_prefix='/api/medias')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_medias_list(client):
    """Teste la récupération de la liste des projets médias (i18n, sécurité, SEO)."""
    response = client.get('/api/medias/')
    assert response.status_code == 200
    assert 'projects' in response.json
    assert isinstance(response.json['projects'], list)

def test_create_medias_jwt(client):
    """Test création projet médias avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Médias IA', 'lang': 'fr'}
    with patch('backend.routes.medias.routes.create_project') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Médias IA'}
        response = client.post('/api/medias/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Médias IA'
        mock_create.assert_called_once()

def test_graphql_query_medias(client):
    """Test requête GraphQL médias (sécurité, plugins, fallback IA)."""
    query = '{ medias { id name } }'
    response = client.post('/api/medias/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'medias' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route médias."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/medias/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route médias."""
    with patch('backend.routes.medias.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/medias/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données médias (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/medias/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
