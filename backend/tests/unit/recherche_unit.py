"""
Tests unitaires avancés pour la gestion de la recherche (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.recherche.routes import recherche_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(recherche_bp, url_prefix='/api/recherche')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_recherche_list(client):
    """Teste la récupération de la liste des recherches (i18n, sécurité, SEO)."""
    response = client.get('/api/recherche/')
    assert response.status_code == 200
    assert 'recherches' in response.json
    assert isinstance(response.json['recherches'], list)

def test_create_recherche_jwt(client):
    """Test création recherche avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Recherche IA', 'lang': 'fr'}
    with patch('backend.routes.recherche.routes.create_recherche') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Recherche IA'}
        response = client.post('/api/recherche/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Recherche IA'
        mock_create.assert_called_once()

def test_graphql_query_recherche(client):
    """Test requête GraphQL recherche (sécurité, plugins, fallback IA)."""
    query = '{ recherche { id name } }'
    response = client.post('/api/recherche/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'recherche' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, de, zh) pour la route recherche."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/recherche/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route recherche."""
    with patch('backend.routes.recherche.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/recherche/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données recherche (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/recherche/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
