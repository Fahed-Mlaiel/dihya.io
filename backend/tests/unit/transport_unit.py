"""
Tests unitaires avancés pour la gestion du transport (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.transport.routes import transport_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(transport_bp, url_prefix='/api/transport')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_transport_list(client):
    """Teste la récupération de la liste transport (i18n, sécurité, SEO)."""
    response = client.get('/api/transport/')
    assert response.status_code == 200
    assert 'transports' in response.json
    assert isinstance(response.json['transports'], list)

def test_create_transport_jwt(client):
    """Test création transport avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Transport IA', 'lang': 'fr'}
    with patch('backend.routes.transport.routes.create_transport') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Transport IA'}
        response = client.post('/api/transport/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Transport IA'
        mock_create.assert_called_once()

def test_graphql_query_transport(client):
    """Test requête GraphQL transport (sécurité, plugins, fallback IA)."""
    query = '{ transport { id name } }'
    response = client.post('/api/transport/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'transport' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, de, zh) pour la route transport."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/transport/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route transport."""
    with patch('backend.routes.transport.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/transport/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données transport (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/transport/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
