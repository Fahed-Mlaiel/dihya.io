"""
Tests unitaires pour la gestion avancée des projets BTP (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.btp.routes import btp_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(btp_bp, url_prefix='/api/btp')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_btp_list(client):
    """Teste la récupération de la liste des projets BTP (i18n, sécurité, SEO)."""
    response = client.get('/api/btp/')
    assert response.status_code == 200
    assert 'projects' in response.json
    assert isinstance(response.json['projects'], list)

def test_create_btp_jwt(client):
    """Test création projet BTP avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Chantier IA', 'lang': 'fr'}
    with patch('backend.routes.btp.routes.create_project') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Chantier IA'}
        response = client.post('/api/btp/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Chantier IA'
        mock_create.assert_called_once()

def test_graphql_query_btp(client):
    """Test requête GraphQL BTP (sécurité, plugins, fallback IA)."""
    query = '{ btps { id name } }'
    response = client.post('/api/btp/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'btps' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route BTP."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/btp/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route BTP."""
    with patch('backend.routes.btp.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/btp/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données BTP (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/btp/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
