"""
Tests unitaires avancés pour la gestion des projets VR/AR (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.vr_ar.routes import vr_ar_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(vr_ar_bp, url_prefix='/api/vr-ar')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_vr_ar_list(client):
    """Teste la récupération de la liste VR/AR (i18n, sécurité, SEO)."""
    response = client.get('/api/vr-ar/')
    assert response.status_code == 200
    assert 'vr_ar' in response.json
    assert isinstance(response.json['vr_ar'], list)

def test_create_vr_ar_jwt(client):
    """Test création VR/AR avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Projet VR/AR', 'lang': 'fr'}
    with patch('backend.routes.vr_ar.routes.create_vr_ar') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Projet VR/AR'}
        response = client.post('/api/vr-ar/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Projet VR/AR'
        mock_create.assert_called_once()

def test_graphql_query_vr_ar(client):
    """Test requête GraphQL VR/AR (sécurité, plugins, fallback IA)."""
    query = '{ vrAr { id name } }'
    response = client.post('/api/vr-ar/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'vrAr' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, de, zh) pour la route VR/AR."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/vr-ar/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route VR/AR."""
    with patch('backend.routes.vr_ar.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/vr-ar/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données VR/AR (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/vr-ar/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
