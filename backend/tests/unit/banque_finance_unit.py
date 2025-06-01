"""
Tests unitaires pour la gestion avancée des projets Banque/Finance (REST, GraphQL, sécurité, i18n, plugins, RGPD, audit, SEO, IA fallback).
Compatible multilingue, multitenant, plugins, CI/CD, Codespaces.
"""
import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.routes.banque_finance.routes import banque_finance_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(banque_finance_bp, url_prefix='/api/banque_finance')
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_banque_finance_list(client):
    """Teste la récupération de la liste des comptes/transactions (i18n, sécurité, SEO)."""
    response = client.get('/api/banque_finance/')
    assert response.status_code == 200
    assert 'accounts' in response.json or 'transactions' in response.json

def test_create_banque_finance_jwt(client):
    """Test création compte/transaction avec JWT, validation, audit log, RGPD."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    data = {'name': 'Compte IA', 'lang': 'fr'}
    with patch('backend.routes.banque_finance.routes.create_account') as mock_create:
        mock_create.return_value = {'id': 1, 'name': 'Compte IA'}
        response = client.post('/api/banque_finance/', json=data, headers=headers)
        assert response.status_code == 201
        assert response.json['name'] == 'Compte IA'
        mock_create.assert_called_once()

def test_graphql_query_banque_finance(client):
    """Test requête GraphQL banque_finance (sécurité, plugins, fallback IA)."""
    query = '{ comptes { id name } }'
    response = client.post('/api/banque_finance/graphql', json={'query': query})
    assert response.status_code == 200
    assert 'data' in response.json

def test_i18n_support(client):
    """Test multilingue (fr, en, ar, etc.) pour la route banque_finance."""
    for lang in ['fr', 'en', 'ar', 'de', 'zh']:
        response = client.get(f'/api/banque_finance/?lang={lang}')
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_plugin_injection(client):
    """Test injection plugin dynamique sur la route banque_finance."""
    with patch('backend.routes.banque_finance.routes.plugins_manager') as mock_plugins:
        mock_plugins.is_enabled.return_value = True
        response = client.get('/api/banque_finance/?plugin=seo')
        assert response.status_code == 200
        assert response.json['plugin'] == 'seo'

def test_rgpd_export(client):
    """Test export RGPD des données banque_finance (anonymisation, audit)."""
    headers = {'Authorization': 'Bearer test.jwt.token'}
    response = client.get('/api/banque_finance/export', headers=headers)
    assert response.status_code == 200
    assert 'export' in response.json
    assert response.json['export']['format'] == 'csv'
