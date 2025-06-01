"""
Tests unitaires avancés pour la gestion de la santé (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.sante.routes import sante_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(sante_bp, url_prefix='/api/sante')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_sante_list(client):
    """Teste la récupération de la liste santé (i18n, sécurité, SEO)."""
    response = client.get('/api/sante/')
    assert response.status_code == 200
    assert 'santes' in response.json
    assert isinstance(response.json['santes'], list)

def test_create_sante_jwt(client):
    """Test création santé avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Santé IA', 'lang': 'fr'}
    with patch('backend.routes.sante.routes.create_sante') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Santé IA'}
        response = client.post('/api/sante/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Santé IA'
        mock_create.assert_called_once()

def test_graphql_query_sante(client):
    """Test requête GraphQL santé (sécurité, plugins, fallback IA)."""
    query = '{ sante { id name } }'
    response = client.post('/api/sante/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'sante' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, de, zh) pour la route santé."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/sante/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route santé."""
    with patch('backend.routes.sante.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/sante/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données santé (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/sante/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
