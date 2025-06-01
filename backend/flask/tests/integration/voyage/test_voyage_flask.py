"""
Test d'intégration avancé pour le module Voyage.
Couvre sécurité, i18n, multitenancy, plugins, fallback IA, RGPD, audit, SEO, gestion des rôles.
"""
import pytest
from flask import Flask
from backend.flask.routes.voyage.routes import voyage_bp
from backend.flask.routes.utils.utils import get_i18n_headers, get_admin_token, get_tenant_headers

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(voyage_bp, url_prefix="/api/voyage")
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_voyage_secure_route(client):
    token = get_admin_token()
    headers = get_i18n_headers('fr')
    headers.update({'Authorization': f'Bearer {token}'})
    response = client.get("/api/voyage/secure", headers=headers)
    assert response.status_code == 200
    assert 'application/json' in response.content_type
    assert response.json['role'] == 'admin'

def test_voyage_multitenant(client):
    headers = get_tenant_headers('tenant1')
    response = client.get("/api/voyage/tenant", headers=headers)
    assert response.status_code == 200
    assert response.json['tenant'] == 'tenant1'

def test_voyage_i18n(client):
    for lang in ['fr', 'en', 'ar', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es']:
        headers = get_i18n_headers(lang)
        response = client.get("/api/voyage/i18n", headers=headers)
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_voyage_plugin(client):
    response = client.get("/api/voyage/plugin-test")
    assert response.status_code == 200
    assert 'plugin' in response.json

def test_voyage_fallback_ia(client):
    response = client.get("/api/voyage/ia-fallback")
    assert response.status_code == 200
    assert response.json['ia'] in ['LLaMA', 'Mixtral', 'Mistral']

def test_voyage_rgpd_export(client):
    response = client.get("/api/voyage/rgpd/export")
    assert response.status_code == 200
    assert 'export' in response.json

def test_voyage_audit_log(client):
    response = client.get("/api/voyage/audit-log")
    assert response.status_code == 200
    assert 'audit' in response.json

def test_voyage_seo(client):
    response = client.get("/api/voyage/seo/robots.txt")
    assert response.status_code == 200
    assert 'User-agent' in response.data.decode()
