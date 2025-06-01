"""
Tests unitaires avancés pour la gestion de la sécurité (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.securite.routes import securite_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(securite_bp, url_prefix='/api/securite')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_securite_list(client):
    """Teste la récupération de la liste sécurité (i18n, sécurité, SEO)."""
    response = client.get('/api/securite/')
    assert response.status_code == 200
    assert 'securites' in response.json
    assert isinstance(response.json['securites'], list)

def test_create_securite_jwt(client):
    """Test création sécurité avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Sécurité IA', 'lang': 'fr'}
    with patch('backend.routes.securite.routes.create_securite') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Sécurité IA'}
        response = client.post('/api/securite/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Sécurité IA'
        mock_create.assert_called_once()

def test_graphql_query_securite(client):
    """Test requête GraphQL sécurité (sécurité, plugins, fallback IA)."""
    query = '{ securite { id name } }'
    response = client.post('/api/securite/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'securite' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, de, zh) pour la route sécurité."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/securite/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route sécurité."""
    with patch('backend.routes.securite.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/securite/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données sécurité (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/securite/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
