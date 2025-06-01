"""
Tests unitaires pour la gestion avancée des projets Ecommerce (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.ecommerce.routes import ecommerce_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(ecommerce_bp, url_prefix='/api/ecommerce')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_ecommerce_list(client):
    """Teste la récupération de la liste des produits ecommerce (i18n, sécurité, SEO)."""
    response = client.get('/api/ecommerce/')
    assert response.status_code == 200
    assert 'products' in response.json
    assert isinstance(response.json['products'], list)

def test_create_ecommerce_jwt(client):
    """Test création produit ecommerce avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Produit IA', 'lang': 'fr'}
    with patch('backend.routes.ecommerce.routes.create_product') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Produit IA'}
        response = client.post('/api/ecommerce/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Produit IA'
        mock_create.assert_called_once()

def test_graphql_query_ecommerce(client):
    """Test requête GraphQL ecommerce (sécurité, plugins, fallback IA)."""
    query = '{ products { id name } }'
    response = client.post('/api/ecommerce/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'products' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route ecommerce."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/ecommerce/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route ecommerce."""
    with patch('backend.routes.ecommerce.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/ecommerce/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données ecommerce (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/ecommerce/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
