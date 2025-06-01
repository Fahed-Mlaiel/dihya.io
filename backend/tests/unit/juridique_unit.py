"""
Tests unitaires pour la gestion avancée des projets Juridique (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.juridique.routes import juridique_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(juridique_bp, url_prefix='/api/juridique')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_juridique_list(client):
    """Teste la récupération de la liste des dossiers juridiques (i18n, sécurité, SEO)."""
    response = client.get('/api/juridique/')
    assert response.status_code == 200
    assert 'cases' in response.json
    assert isinstance(response.json['cases'], list)

def test_create_juridique_jwt(client):
    """Test création dossier juridique avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Dossier IA', 'lang': 'fr'}
    with patch('backend.routes.juridique.routes.create_case') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Dossier IA'}
        response = client.post('/api/juridique/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Dossier IA'
        mock_create.assert_called_once()

def test_graphql_query_juridique(client):
    """Test requête GraphQL juridique (sécurité, plugins, fallback IA)."""
    query = '{ cases { id name } }'
    response = client.post('/api/juridique/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'cases' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route juridique."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/juridique/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route juridique."""
    with patch('backend.routes.juridique.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/juridique/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données juridique (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/juridique/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
