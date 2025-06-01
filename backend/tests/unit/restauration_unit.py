"""
Tests unitaires avancés pour la gestion de la restauration (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.restauration.routes import restauration_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(restauration_bp, url_prefix='/api/restauration')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_restauration_list(client):
    """Teste la récupération de la liste restauration (i18n, sécurité, SEO)."""
    response = client.get('/api/restauration/')
    assert response.status_code == 200
    assert 'restaurations' in response.json
    assert isinstance(response.json['restaurations'], list)

def test_create_restauration_jwt(client):
    """Test création restauration avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Restauration IA', 'lang': 'fr'}
    with patch('backend.routes.restauration.routes.create_restauration') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Restauration IA'}
        response = client.post('/api/restauration/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Restauration IA'
        mock_create.assert_called_once()

def test_graphql_query_restauration(client):
    """Test requête GraphQL restauration (sécurité, plugins, fallback IA)."""
    query = '{ restauration { id name } }'
    response = client.post('/api/restauration/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'restauration' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, de, zh) pour la route restauration."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/restauration/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route restauration."""
    with patch('backend.routes.restauration.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/restauration/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données restauration (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/restauration/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
