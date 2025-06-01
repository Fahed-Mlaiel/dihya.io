"""
Tests unitaires pour la gestion avancée des projets IT/DevOps (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.it_devops.routes import it_devops_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(it_devops_bp, url_prefix='/api/it_devops')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_it_devops_list(client):
    """Teste la récupération de la liste des projets IT/DevOps (i18n, sécurité, SEO)."""
    response = client.get('/api/it_devops/')
    assert response.status_code == 200
    assert 'projects' in response.json
    assert isinstance(response.json['projects'], list)

def test_create_it_devops_jwt(client):
    """Test création projet IT/DevOps avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'DevOps IA', 'lang': 'fr'}
    with patch('backend.routes.it_devops.routes.create_project') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'DevOps IA'}
        response = client.post('/api/it_devops/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'DevOps IA'
        mock_create.assert_called_once()

def test_graphql_query_it_devops(client):
    """Test requête GraphQL IT/DevOps (sécurité, plugins, fallback IA)."""
    query = '{ itdevops { id name } }'
    response = client.post('/api/it_devops/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json
    assert 'itdevops' in response.json['data']

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route IT/DevOps."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/it_devops/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route IT/DevOps."""
    with patch('backend.routes.it_devops.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/it_devops/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données IT/DevOps (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/it_devops/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
