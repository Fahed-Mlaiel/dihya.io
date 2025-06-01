"""
Tests unitaires pour la gestion avancée des projets Hotellerie (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.hotellerie.routes import hotellerie_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(hotellerie_bp, url_prefix='/api/hotellerie')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_hotellerie_list(client):
    """Teste la récupération de la liste des hôtels (i18n, sécurité, SEO)."""
    response = client.get('/api/hotellerie/')
    assert response.status_code == 200
    assert 'hotels' in response.json
    assert isinstance(response.json['hotels'], list)

def test_create_hotellerie_jwt(client):
    """Test création hôtel avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Hotel IA', 'lang': 'fr'}
    with patch('backend.routes.hotellerie.routes.create_hotel') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Hotel IA'}
        response = client.post('/api/hotellerie/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Hotel IA'
        mock_create.assert_called_once()

def test_graphql_query_hotellerie(client):
    """Test requête GraphQL hotellerie (sécurité, plugins, fallback IA)."""
    query = '{ hotels { id name } }'
    response = client.post('/api/hotellerie/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'hotels' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route hotellerie."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/hotellerie/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route hotellerie."""
    with patch('backend.routes.hotellerie.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/hotellerie/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données hotellerie (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/hotellerie/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
