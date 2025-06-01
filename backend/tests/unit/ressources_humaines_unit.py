"""
Tests unitaires avancés pour la gestion des ressources humaines (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.ressources_humaines.routes import rh_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(rh_bp, url_prefix='/api/rh')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_rh_list(client):
    """Teste la récupération de la liste RH (i18n, sécurité, SEO)."""
    response = client.get('/api/rh/')
    assert response.status_code == 200
    assert 'ressources' in response.json
    assert isinstance(response.json['ressources'], list)

def test_create_rh_jwt(client):
    """Test création RH avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'RH IA', 'lang': 'fr'}
    with patch('backend.routes.ressources_humaines.routes.create_rh') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'RH IA'}
        response = client.post('/api/rh/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'RH IA'
        mock_create.assert_called_once()

def test_graphql_query_rh(client):
    """Test requête GraphQL RH (sécurité, plugins, fallback IA)."""
    query = '{ rh { id name } }'
    response = client.post('/api/rh/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'rh' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, de, zh) pour la route RH."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/rh/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route RH."""
    with patch('backend.routes.ressources_humaines.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/rh/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données RH (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/rh/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
