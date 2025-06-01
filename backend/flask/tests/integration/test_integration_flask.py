"""
Test d'intégration global Flask pour l'API Dihya.
Couvre sécurité, i18n, multitenancy, plugins, fallback IA, RGPD, audit, SEO, gestion des rôles.
"""
import pytest
from flask import Flask
from backend.flask.routes.health.routes import health_bp
from backend.flask.routes.utils.utils import get_i18n_headers, get_admin_token, get_tenant_headers

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(health_bp, url_prefix="/api/health")
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_secure_route(client):
    token = get_admin_token()
    headers = get_i18n_headers('fr')
    headers.update({'Authorization': f'Bearer {token}'})
    response = client.get("/api/health/secure", headers=headers)
    assert response.status_code == 200
    assert response.json['role'] == 'admin'

def test_i18n(client):
    for lang in ['fr','en','ar','de','zh','ja','ko','nl','he','fa','hi','es']:
        headers = get_i18n_headers(lang)
        response = client.get("/api/health/i18n", headers=headers)
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_multitenant(client):
    headers = get_tenant_headers('tenant1')
    response = client.get("/api/health/tenant", headers=headers)
    assert response.status_code == 200
    assert response.json['tenant'] == 'tenant1'

def test_plugin(client):
    response = client.get("/api/health/plugin-test")
    assert response.status_code == 200
    assert 'plugin' in response.json

def test_fallback_ia(client):
    response = client.get("/api/health/ia-fallback")
    assert response.status_code == 200
    assert response.json['ia'] in ['LLaMA', 'Mixtral', 'Mistral']

def test_rgpd_export(client):
    response = client.get("/api/health/rgpd/export")
    assert response.status_code == 200
    assert 'export' in response.json

def test_audit_log(client):
    response = client.get("/api/health/audit-log")
    assert response.status_code == 200
    assert 'audit' in response.json

def test_seo(client):
    response = client.get("/api/health/seo/robots.txt")
    assert response.status_code == 200
    assert 'User-agent' in response.data.decode()
