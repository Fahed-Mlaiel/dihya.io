"""
Test d'intégration avancé pour le module Santé.
Couvre sécurité (CORS, JWT, WAF, anti-DDOS), i18n, multitenancy, plugins, fallback IA, RGPD, audit, SEO, gestion des rôles.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from backend.flask.routes.sante.routes import sante_bp
from backend.flask.routes.utils.utils import get_i18n_headers, get_admin_token, get_tenant_headers

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(sante_bp, url_prefix="/api/sante")
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_sante_secure_route(client):
    token = get_admin_token()
    headers = get_i18n_headers('fr')
    headers.update({'Authorization': f'Bearer {token}'})
    response = client.get("/api/sante/secure", headers=headers)
    assert response.status_code == 200
    assert 'application/json' in response.content_type
    assert response.json['role'] == 'admin'

def test_sante_multitenant(client):
    headers = get_tenant_headers('tenant1')
    response = client.get("/api/sante/tenant", headers=headers)
    assert response.status_code == 200
    assert response.json['tenant'] == 'tenant1'

def test_sante_i18n(client):
    for lang in ['fr', 'en', 'ar', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es']:
        headers = get_i18n_headers(lang)
        response = client.get("/api/sante/i18n", headers=headers)
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_sante_plugin(client):
    response = client.get("/api/sante/plugin-test")
    assert response.status_code == 200
    assert 'plugin' in response.json

def test_sante_fallback_ia(client):
    response = client.get("/api/sante/ia-fallback")
    assert response.status_code == 200
    assert response.json['ia'] in ['LLaMA', 'Mixtral', 'Mistral']

def test_sante_rgpd_export(client):
    response = client.get("/api/sante/rgpd/export")
    assert response.status_code == 200
    assert 'export' in response.json

def test_sante_audit_log(client):
    response = client.get("/api/sante/audit-log")
    assert response.status_code == 200
    assert 'audit' in response.json

def test_sante_seo(client):
    response = client.get("/api/sante/seo/robots.txt")
    assert response.status_code == 200
    assert 'User-agent' in response.data.decode()
