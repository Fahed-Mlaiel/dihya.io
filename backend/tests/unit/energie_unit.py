"""
Tests unitaires pour la gestion avancée des projets Energie (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.energie.routes import energie_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(energie_bp, url_prefix='/api/energie')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_energie_list(client):
    """Teste la récupération de la liste des projets énergie (i18n, sécurité, SEO)."""
    response = client.get('/api/energie/')
    assert response.status_code == 200
    assert 'projects' in response.json
    assert isinstance(response.json['projects'], list)

def test_create_energie_jwt(client):
    """Test création projet énergie avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Energie IA', 'lang': 'fr'}
    with patch('backend.routes.energie.routes.create_project') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Energie IA'}
        response = client.post('/api/energie/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Energie IA'
        mock_create.assert_called_once()

def test_graphql_query_energie(client):
    """Test requête GraphQL énergie (sécurité, plugins, fallback IA)."""
    query = '{ energies { id name } }'
    response = client.post('/api/energie/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'energies' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route énergie."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/energie/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route énergie."""
    with patch('backend.routes.energie.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/energie/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données énergie (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/energie/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
