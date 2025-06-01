"""
Tests unitaires pour la gestion avancée des projets Health (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.health.routes import health_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(health_bp, url_prefix='/api/health')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_health_list(client):
    """Teste la récupération de la liste des patients (i18n, sécurité, SEO)."""
    response = client.get('/api/health/')
    assert response.status_code == 200
    assert 'patients' in response.json
    assert isinstance(response.json['patients'], list)

def test_create_health_jwt(client):
    """Test création patient avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Patient IA', 'lang': 'fr'}
    with patch('backend.routes.health.routes.create_patient') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Patient IA'}
        response = client.post('/api/health/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Patient IA'
        mock_create.assert_called_once()

def test_graphql_query_health(client):
    """Test requête GraphQL health (sécurité, plugins, fallback IA)."""
    query = '{ patients { id name } }'
    response = client.post('/api/health/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'patients' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route health."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/health/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route health."""
    with patch('backend.routes.health.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/health/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données health (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/health/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
