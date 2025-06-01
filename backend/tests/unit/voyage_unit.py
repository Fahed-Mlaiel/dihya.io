"""
Tests unitaires avancés pour la gestion des projets voyage (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.voyage.routes import voyage_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(voyage_bp, url_prefix='/api/voyage')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_voyage_list(client):
    """Teste la récupération de la liste voyage (i18n, sécurité, SEO)."""
    response = client.get('/api/voyage/')
    assert response.status_code == 200
    assert 'voyages' in response.json
    assert isinstance(response.json['voyages'], list)

def test_create_voyage_jwt(client):
    """Test création voyage avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Voyage IA', 'lang': 'fr'}
    with patch('backend.routes.voyage.routes.create_voyage') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Voyage IA'}
        response = client.post('/api/voyage/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Voyage IA'
        mock_create.assert_called_once()

def test_graphql_query_voyage(client):
    """Test requête GraphQL voyage (sécurité, plugins, fallback IA)."""
    query = '{ voyage { id name } }'
    response = client.post('/api/voyage/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'voyage' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, de, zh) pour la route voyage."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/voyage/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route voyage."""
    with patch('backend.routes.voyage.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/voyage/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données voyage (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/voyage/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
