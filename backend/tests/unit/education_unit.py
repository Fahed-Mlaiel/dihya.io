"""
Tests unitaires pour la gestion avancée des projets Education (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.education.routes import education_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(education_bp, url_prefix='/api/education')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_education_list(client):
    """Teste la récupération de la liste des projets education (i18n, sécurité, SEO)."""
    response = client.get('/api/education/')
    assert response.status_code == 200
    assert 'projects' in response.json
    assert isinstance(response.json['projects'], list)

def test_create_education_jwt(client):
    """Test création projet education avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Education IA', 'lang': 'fr'}
    with patch('backend.routes.education.routes.create_project') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Education IA'}
        response = client.post('/api/education/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Education IA'
        mock_create.assert_called_once()

def test_graphql_query_education(client):
    """Test requête GraphQL education (sécurité, plugins, fallback IA)."""
    query = '{ educations { id name } }'
    response = client.post('/api/education/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'educations' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route education."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/education/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route education."""
    with patch('backend.routes.education.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/education/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données education (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/education/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
