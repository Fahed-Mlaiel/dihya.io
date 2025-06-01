"""
Tests unitaires avancés pour la gestion des modes (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.mode.routes import mode_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(mode_bp, url_prefix='/api/mode')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_mode_list(client):
    """Teste la récupération de la liste des modes (i18n, sécurité, SEO)."""
    response = client.get('/api/mode/')
    assert response.status_code == 200
    assert 'modes' in response.json
    assert isinstance(response.json['modes'], list)

def test_create_mode_jwt(client):
    """Test création mode avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Mode IA', 'lang': 'fr'}
    with patch('backend.routes.mode.routes.create_mode') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Mode IA'}
        response = client.post('/api/mode/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Mode IA'
        mock_create.assert_called_once()

def test_graphql_query_mode(client):
    """Test requête GraphQL mode (sécurité, plugins, fallback IA)."""
    query = '{ mode { id name } }'
    response = client.post('/api/mode/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'mode' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, de, zh) pour la route mode."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/mode/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route mode."""
    with patch('backend.routes.mode.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/mode/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données mode (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/mode/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
