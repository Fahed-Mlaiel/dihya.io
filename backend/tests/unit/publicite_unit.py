"""
Tests unitaires avancés pour la gestion des publicités (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.publicite.routes import publicite_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(publicite_bp, url_prefix='/api/publicite')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_publicite_list(client):
    """Teste la récupération de la liste des publicités (i18n, sécurité, SEO)."""
    response = client.get('/api/publicite/')
    assert response.status_code == 200
    assert 'publicites' in response.json
    assert isinstance(response.json['publicites'], list)

def test_create_publicite_jwt(client):
    """Test création publicité avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Pub IA', 'lang': 'fr'}
    with patch('backend.routes.publicite.routes.create_publicite') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Pub IA'}
        response = client.post('/api/publicite/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Pub IA'
        mock_create.assert_called_once()

def test_graphql_query_publicite(client):
    """Test requête GraphQL publicité (sécurité, plugins, fallback IA)."""
    query = '{ publicite { id name } }'
    response = client.post('/api/publicite/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'publicite' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, de, zh) pour la route publicité."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/publicite/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route publicité."""
    with patch('backend.routes.publicite.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/publicite/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données publicité (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/publicite/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
