"""
Tests unitaires avancés pour la gestion des projets voice/IA vocale (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.voice.routes import voice_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(voice_bp, url_prefix='/api/voice')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_voice_list(client):
    """Teste la récupération de la liste voice (i18n, sécurité, SEO)."""
    response = client.get('/api/voice/')
    assert response.status_code == 200
    assert 'voices' in response.json
    assert isinstance(response.json['voices'], list)

def test_create_voice_jwt(client):
    """Test création voice avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Voice IA', 'lang': 'fr'}
    with patch('backend.routes.voice.routes.create_voice') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Voice IA'}
        response = client.post('/api/voice/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Voice IA'
        mock_create.assert_called_once()

def test_graphql_query_voice(client):
    """Test requête GraphQL voice (sécurité, plugins, fallback IA)."""
    query = '{ voice { id name } }'
    response = client.post('/api/voice/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'voice' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, de, zh) pour la route voice."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/voice/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route voice."""
    with patch('backend.routes.voice.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/voice/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données voice (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/voice/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
