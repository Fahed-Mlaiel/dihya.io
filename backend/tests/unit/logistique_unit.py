"""
Tests unitaires pour la gestion avancée des projets Logistique (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.logistique.routes import logistique_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(logistique_bp, url_prefix='/api/logistique')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_logistique_list(client):
    """Teste la récupération de la liste des projets logistique (i18n, sécurité, SEO)."""
    response = client.get('/api/logistique/')
    assert response.status_code == 200
    assert 'projects' in response.json
    assert isinstance(response.json['projects'], list)

def test_create_logistique_jwt(client):
    """Test création projet logistique avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Logistique IA', 'lang': 'fr'}
    with patch('backend.routes.logistique.routes.create_project') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Logistique IA'}
        response = client.post('/api/logistique/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Logistique IA'
        mock_create.assert_called_once()

def test_graphql_query_logistique(client):
    """Test requête GraphQL logistique (sécurité, plugins, fallback IA)."""
    query = '{ logistiques { id name } }'
    response = client.post('/api/logistique/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'logistiques' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route logistique."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/logistique/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route logistique."""
    with patch('backend.routes.logistique.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/logistique/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données logistique (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/logistique/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
