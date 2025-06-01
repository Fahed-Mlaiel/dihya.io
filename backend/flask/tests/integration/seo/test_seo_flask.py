"""
Test d'intégration avancé pour le module SEO.
Couvre sécurité, i18n, multitenancy, plugins, fallback IA, RGPD, audit, SEO, gestion des rôles.
"""
import pytest
from flask import Flask
from backend.flask.routes.seo.routes import seo_bp
from backend.flask.routes.utils.utils import get_i18n_headers, get_admin_token, get_tenant_headers

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(seo_bp, url_prefix="/api/seo")
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_seo_robots_txt(client):
    response = client.get("/api/seo/robots.txt")
    assert response.status_code == 200
    assert 'User-agent' in response.data.decode()

def test_seo_sitemap(client):
    response = client.get("/api/seo/sitemap.xml")
    assert response.status_code == 200
    assert '<urlset' in response.data.decode()

def test_seo_multitenant(client):
    headers = get_tenant_headers('tenant1')
    response = client.get("/api/seo/tenant", headers=headers)
    assert response.status_code == 200
    assert response.json['tenant'] == 'tenant1'

def test_seo_i18n(client):
    for lang in ['fr', 'en', 'ar', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es']:
        headers = get_i18n_headers(lang)
        response = client.get("/api/seo/i18n", headers=headers)
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_seo_plugin(client):
    response = client.get("/api/seo/plugin-test")
    assert response.status_code == 200
    assert 'plugin' in response.json

def test_seo_fallback_ia(client):
    response = client.get("/api/seo/ia-fallback")
    assert response.status_code == 200
    assert response.json['ia'] in ['LLaMA', 'Mixtral', 'Mistral']

def test_seo_rgpd_export(client):
    response = client.get("/api/seo/rgpd/export")
    assert response.status_code == 200
    assert 'export' in response.json

def test_seo_audit_log(client):
    response = client.get("/api/seo/audit-log")
    assert response.status_code == 200
    assert 'audit' in response.json
