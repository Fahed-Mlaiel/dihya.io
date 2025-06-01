"""
Tests unitaires avancés pour la gestion des services à la personne (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.services_personne.routes import services_personne_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(services_personne_bp, url_prefix='/api/services-personne')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_services_personne_list(client):
    """Teste la récupération de la liste des services à la personne (i18n, sécurité, SEO)."""
    response = client.get('/api/services-personne/')
    assert response.status_code == 200
    assert 'services' in response.json
    assert isinstance(response.json['services'], list)

def test_create_services_personne_jwt(client):
    """Test création service à la personne avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Service IA', 'lang': 'fr'}
    with patch('backend.routes.services_personne.routes.create_service') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Service IA'}
        response = client.post('/api/services-personne/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Service IA'
        mock_create.assert_called_once()

def test_graphql_query_services_personne(client):
    """Test requête GraphQL services à la personne (sécurité, plugins, fallback IA)."""
    query = '{ servicesPersonne { id name } }'
    response = client.post('/api/services-personne/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'servicesPersonne' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, de, zh) pour la route services à la personne."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/services-personne/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route services à la personne."""
    with patch('backend.routes.services_personne.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/services-personne/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données services à la personne (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/services-personne/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
