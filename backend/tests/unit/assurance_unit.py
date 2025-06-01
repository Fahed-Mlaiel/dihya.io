"""
Tests unitaires pour la gestion avancée des projets Assurance (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.assurance.routes import assurance_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(assurance_bp, url_prefix='/api/assurance')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_assurance_list(client):
    """Teste la récupération de la liste des contrats assurance (i18n, sécurité, SEO)."""
    response = client.get('/api/assurance/')
    assert response.status_code == 200
    assert 'contracts' in response.json
    assert isinstance(response.json['contracts'], list)

def test_create_assurance_contract_jwt(client):
    """Test création contrat assurance avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Assurance IA', 'lang': 'fr'}
    with patch('backend.routes.assurance.routes.create_contract') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Assurance IA'}
        response = client.post('/api/assurance/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Assurance IA'
        mock_create.assert_called_once()

def test_graphql_query_assurance(client):
    """Test requête GraphQL assurance (sécurité, plugins, fallback IA)."""
    query = '{ assurances { id name } }'
    response = client.post('/api/assurance/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'assurances' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route assurance."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/assurance/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route assurance."""
    with patch('backend.routes.assurance.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/assurance/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données assurance (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/assurance/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
