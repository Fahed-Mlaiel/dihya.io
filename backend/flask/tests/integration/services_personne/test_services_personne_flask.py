"""
Test d'intégration avancé pour le module Services à la Personne.
Couvre sécurité, i18n, multitenancy, plugins, fallback IA, RGPD, audit, SEO, gestion des rôles.
"""
import pytest
from flask import Flask
from backend.flask.routes.services_personne.routes import services_personne_bp
from backend.flask.routes.utils.utils import get_i18n_headers, get_admin_token, get_tenant_headers

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(services_personne_bp, url_prefix="/api/services-personne")
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_services_personne_secure_route(client):
    token = get_admin_token()
    headers = get_i18n_headers('fr')
    headers.update({'Authorization': f'Bearer {token}'})
    response = client.get("/api/services-personne/secure", headers=headers)
    assert response.status_code == 200
    assert 'application/json' in response.content_type
    assert response.json['role'] == 'admin'

def test_services_personne_multitenant(client):
    headers = get_tenant_headers('tenant1')
    response = client.get("/api/services-personne/tenant", headers=headers)
    assert response.status_code == 200
    assert response.json['tenant'] == 'tenant1'

def test_services_personne_i18n(client):
    for lang in ['fr', 'en', 'ar', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es']:
        headers = get_i18n_headers(lang)
        response = client.get("/api/services-personne/i18n", headers=headers)
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_services_personne_plugin(client):
    response = client.get("/api/services-personne/plugin-test")
    assert response.status_code == 200
    assert 'plugin' in response.json

def test_services_personne_fallback_ia(client):
    response = client.get("/api/services-personne/ia-fallback")
    assert response.status_code == 200
    assert response.json['ia'] in ['LLaMA', 'Mixtral', 'Mistral']

def test_services_personne_rgpd_export(client):
    response = client.get("/api/services-personne/rgpd/export")
    assert response.status_code == 200
    assert 'export' in response.json

def test_services_personne_audit_log(client):
    response = client.get("/api/services-personne/audit-log")
    assert response.status_code == 200
    assert 'audit' in response.json

def test_services_personne_seo(client):
    response = client.get("/api/services-personne/seo/robots.txt")
    assert response.status_code == 200
    assert 'User-agent' in response.data.decode()
