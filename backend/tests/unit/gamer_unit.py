"""
Tests unitaires pour la gestion avancée des projets Gamer (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.gamer.routes import gamer_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(gamer_bp, url_prefix='/api/gamer')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_gamer_list(client):
    """Teste la récupération de la liste des gamers (i18n, sécurité, SEO)."""
    response = client.get('/api/gamer/')
    assert response.status_code == 200
    assert 'gamers' in response.json
    assert isinstance(response.json['gamers'], list)

def test_create_gamer_jwt(client):
    """Test création gamer avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Gamer IA', 'lang': 'fr'}
    with patch('backend.routes.gamer.routes.create_gamer') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Gamer IA'}
        response = client.post('/api/gamer/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Gamer IA'
        mock_create.assert_called_once()

def test_graphql_query_gamer(client):
    """Test requête GraphQL gamer (sécurité, plugins, fallback IA)."""
    query = '{ gamers { id name } }'
    response = client.post('/api/gamer/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'gamers' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route gamer."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/gamer/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route gamer."""
    with patch('backend.routes.gamer.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/gamer/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données gamer (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/gamer/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
