"""
Test d'intégration avancé pour le module Tourisme.
Couvre sécurité, i18n, multitenancy, plugins, fallback IA, RGPD, audit, SEO, gestion des rôles.
"""
import pytest
from flask import Flask
from backend.flask.routes.tourisme.routes import tourisme_bp
from backend.flask.routes.utils.utils import get_i18n_headers, get_admin_token, get_tenant_headers

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(tourisme_bp, url_prefix="/api/tourisme")
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_tourisme_secure_route(client):
    token = get_admin_token()
    headers = get_i18n_headers('fr')
    headers.update({'Authorization': f'Bearer {token}'})
    response = client.get("/api/tourisme/secure", headers=headers)
    assert response.status_code == 200
    assert 'application/json' in response.content_type
    assert response.json['role'] == 'admin'

def test_tourisme_multitenant(client):
    headers = get_tenant_headers('tenant1')
    response = client.get("/api/tourisme/tenant", headers=headers)
    assert response.status_code == 200
    assert response.json['tenant'] == 'tenant1'

def test_tourisme_i18n(client):
    for lang in ['fr', 'en', 'ar', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es']:
        headers = get_i18n_headers(lang)
        response = client.get("/api/tourisme/i18n", headers=headers)
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_tourisme_plugin(client):
    response = client.get("/api/tourisme/plugin-test")
    assert response.status_code == 200
    assert 'plugin' in response.json

def test_tourisme_fallback_ia(client):
    response = client.get("/api/tourisme/ia-fallback")
    assert response.status_code == 200
    assert response.json['ia'] in ['LLaMA', 'Mixtral', 'Mistral']

def test_tourisme_rgpd_export(client):
    response = client.get("/api/tourisme/rgpd/export")
    assert response.status_code == 200
    assert 'export' in response.json

def test_tourisme_audit_log(client):
    response = client.get("/api/tourisme/audit-log")
    assert response.status_code == 200
    assert 'audit' in response.json

def test_tourisme_seo(client):
    response = client.get("/api/tourisme/seo/robots.txt")
    assert response.status_code == 200
    assert 'User-agent' in response.data.decode()
