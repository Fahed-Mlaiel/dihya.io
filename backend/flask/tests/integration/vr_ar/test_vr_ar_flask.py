"""
Test d'intégration avancé pour le module VR/AR.
Couvre sécurité, i18n, multitenancy, plugins, fallback IA, RGPD, audit, SEO, gestion des rôles.
"""
import pytest
from flask import Flask
from backend.flask.routes.vr_ar.routes import vr_ar_bp
from backend.flask.routes.utils.utils import get_i18n_headers, get_admin_token, get_tenant_headers

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(vr_ar_bp, url_prefix="/api/vr-ar")
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_vr_ar_secure_route(client):
    token = get_admin_token()
    headers = get_i18n_headers('fr')
    headers.update({'Authorization': f'Bearer {token}'})
    response = client.get("/api/vr-ar/secure", headers=headers)
    assert response.status_code == 200
    assert 'application/json' in response.content_type
    assert response.json['role'] == 'admin'

def test_vr_ar_multitenant(client):
    headers = get_tenant_headers('tenant1')
    response = client.get("/api/vr-ar/tenant", headers=headers)
    assert response.status_code == 200
    assert response.json['tenant'] == 'tenant1'

def test_vr_ar_i18n(client):
    for lang in ['fr', 'en', 'ar', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es']:
        headers = get_i18n_headers(lang)
        response = client.get("/api/vr-ar/i18n", headers=headers)
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_vr_ar_plugin(client):
    response = client.get("/api/vr-ar/plugin-test")
    assert response.status_code == 200
    assert 'plugin' in response.json

def test_vr_ar_fallback_ia(client):
    response = client.get("/api/vr-ar/ia-fallback")
    assert response.status_code == 200
    assert response.json['ia'] in ['LLaMA', 'Mixtral', 'Mistral']

def test_vr_ar_rgpd_export(client):
    response = client.get("/api/vr-ar/rgpd/export")
    assert response.status_code == 200
    assert 'export' in response.json

def test_vr_ar_audit_log(client):
    response = client.get("/api/vr-ar/audit-log")
    assert response.status_code == 200
    assert 'audit' in response.json

def test_vr_ar_seo(client):
    response = client.get("/api/vr-ar/seo/robots.txt")
    assert response.status_code == 200
    assert 'User-agent' in response.data.decode()
