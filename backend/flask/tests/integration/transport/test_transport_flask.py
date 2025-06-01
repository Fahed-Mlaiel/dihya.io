"""
Test d'intégration avancé pour le module Transport.
Couvre sécurité, i18n, multitenancy, plugins, fallback IA, RGPD, audit, SEO, gestion des rôles.
"""
import pytest
from flask import Flask
from backend.flask.routes.transport.routes import transport_bp
from backend.flask.routes.utils.utils import get_i18n_headers, get_admin_token, get_tenant_headers

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(transport_bp, url_prefix="/api/transport")
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_transport_secure_route(client):
    token = get_admin_token()
    headers = get_i18n_headers('fr')
    headers.update({'Authorization': f'Bearer {token}'})
    response = client.get("/api/transport/secure", headers=headers)
    assert response.status_code == 200
    assert 'application/json' in response.content_type
    assert response.json['role'] == 'admin'

def test_transport_multitenant(client):
    headers = get_tenant_headers('tenant1')
    response = client.get("/api/transport/tenant", headers=headers)
    assert response.status_code == 200
    assert response.json['tenant'] == 'tenant1'

def test_transport_i18n(client):
    for lang in ['fr', 'en', 'ar', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es']:
        headers = get_i18n_headers(lang)
        response = client.get("/api/transport/i18n", headers=headers)
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_transport_plugin(client):
    response = client.get("/api/transport/plugin-test")
    assert response.status_code == 200
    assert 'plugin' in response.json

def test_transport_fallback_ia(client):
    response = client.get("/api/transport/ia-fallback")
    assert response.status_code == 200
    assert response.json['ia'] in ['LLaMA', 'Mixtral', 'Mistral']

def test_transport_rgpd_export(client):
    response = client.get("/api/transport/rgpd/export")
    assert response.status_code == 200
    assert 'export' in response.json

def test_transport_audit_log(client):
    response = client.get("/api/transport/audit-log")
    assert response.status_code == 200
    assert 'audit' in response.json

def test_transport_seo(client):
    response = client.get("/api/transport/seo/robots.txt")
    assert response.status_code == 200
    assert 'User-agent' in response.data.decode()
