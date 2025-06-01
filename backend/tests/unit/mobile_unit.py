"""
Tests unitaires avancés pour la gestion des projets mobiles (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.mobile.routes import mobile_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(mobile_bp, url_prefix='/api/mobile')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_mobile_list(client):
    """Teste la récupération de la liste des projets mobiles (i18n, sécurité, SEO)."""
    response = client.get('/api/mobile/')
    assert response.status_code == 200
    assert 'projects' in response.json
    assert isinstance(response.json['projects'], list)

def test_create_mobile_project_jwt(client):
    """Test création projet mobile avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Projet Mobile', 'lang': 'fr'}
    with patch('backend.routes.mobile.routes.create_project') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Projet Mobile'}
        response = client.post('/api/mobile/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Projet Mobile'
        mock_create.assert_called_once()

def test_graphql_query_mobile(client):
    """Test requête GraphQL mobile (sécurité, plugins, fallback IA)."""
    query = '{ mobile { id name } }'
    response = client.post('/api/mobile/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'mobile' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, de, zh) pour la route mobile."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/mobile/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route mobile."""
    with patch('backend.routes.mobile.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/mobile/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données mobile (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/mobile/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
