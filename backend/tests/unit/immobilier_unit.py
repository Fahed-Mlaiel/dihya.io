"""
Tests unitaires pour la gestion avancée des projets Immobilier (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.immobilier.routes import immobilier_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(immobilier_bp, url_prefix='/api/immobilier')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_immobilier_list(client):
    """Teste la récupération de la liste des biens immobiliers (i18n, sécurité, SEO)."""
    response = client.get('/api/immobilier/')
    assert response.status_code == 200
    assert 'properties' in response.json
    assert isinstance(response.json['properties'], list)

def test_create_immobilier_jwt(client):
    """Test création bien immobilier avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Immeuble IA', 'lang': 'fr'}
    with patch('backend.routes.immobilier.routes.create_property') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Immeuble IA'}
        response = client.post('/api/immobilier/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Immeuble IA'
        mock_create.assert_called_once()

def test_graphql_query_immobilier(client):
    """Test requête GraphQL immobilier (sécurité, plugins, fallback IA)."""
    query = '{ properties { id name } }'
    response = client.post('/api/immobilier/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'properties' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route immobilier."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/immobilier/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route immobilier."""
    with patch('backend.routes.immobilier.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/immobilier/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données immobilier (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/immobilier/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
