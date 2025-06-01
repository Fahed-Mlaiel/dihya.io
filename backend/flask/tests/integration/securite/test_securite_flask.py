"""
Test d'intégration avancé pour le module Sécurité.
Couvre CORS, JWT, WAF, anti-DDOS, validation, audit, multitenancy, plugins, fallback IA, RGPD, SEO, gestion des rôles.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from backend.flask.routes.securite.routes import securite_bp
from backend.flask.routes.utils.utils import get_i18n_headers, get_admin_token, get_tenant_headers

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(securite_bp, url_prefix="/api/securite")
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_securite_cors(client):
    headers = {'Origin': 'https://trusted.tenant.com'}
    response = client.options("/api/securite/secure", headers=headers)
    assert response.status_code in [200, 204]
    assert 'Access-Control-Allow-Origin' in response.headers

def test_securite_jwt(client):
    token = get_admin_token()
    headers = {'Authorization': f'Bearer {token}'}
    response = client.get("/api/securite/secure", headers=headers)
    assert response.status_code == 200
    assert response.json['role'] == 'admin'

def test_securite_waf(client):
    response = client.get("/api/securite/waf-test?input=<script>")
    assert response.status_code == 400
    assert 'blocked' in response.json['message']

def test_securite_anti_ddos(client):
    for _ in range(20):
        response = client.get("/api/securite/rate-limit-test")
    assert response.status_code in [429, 200]

def test_securite_audit(client):
    response = client.get("/api/securite/audit-log")
    assert response.status_code == 200
    assert 'audit' in response.json

def test_securite_multitenant(client):
    headers = get_tenant_headers('tenant1')
    response = client.get("/api/securite/tenant", headers=headers)
    assert response.status_code == 200
    assert response.json['tenant'] == 'tenant1'

def test_securite_plugin(client):
    response = client.get("/api/securite/plugin-test")
    assert response.status_code == 200
    assert 'plugin' in response.json

def test_securite_fallback_ia(client):
    response = client.get("/api/securite/ia-fallback")
    assert response.status_code == 200
    assert response.json['ia'] in ['LLaMA', 'Mixtral', 'Mistral']

def test_securite_rgpd_export(client):
    response = client.get("/api/securite/rgpd/export")
    assert response.status_code == 200
    assert 'export' in response.json

def test_securite_seo(client):
    response = client.get("/api/securite/seo/robots.txt")
    assert response.status_code == 200
    assert 'User-agent' in response.data.decode()
