"""
Test d'intégration avancé pour le module Voice.
Couvre sécurité, i18n, multitenancy, plugins, fallback IA, RGPD, audit, SEO, gestion des rôles.
"""
import pytest
from flask import Flask
from backend.flask.routes.voice.routes import voice_bp
from backend.flask.routes.utils.utils import get_i18n_headers, get_admin_token, get_tenant_headers

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(voice_bp, url_prefix="/api/voice")
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_voice_secure_route(client):
    token = get_admin_token()
    headers = get_i18n_headers('fr')
    headers.update({'Authorization': f'Bearer {token}'})
    response = client.get("/api/voice/secure", headers=headers)
    assert response.status_code == 200
    assert 'application/json' in response.content_type
    assert response.json['role'] == 'admin'

def test_voice_multitenant(client):
    headers = get_tenant_headers('tenant1')
    response = client.get("/api/voice/tenant", headers=headers)
    assert response.status_code == 200
    assert response.json['tenant'] == 'tenant1'

def test_voice_i18n(client):
    for lang in ['fr', 'en', 'ar', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es']:
        headers = get_i18n_headers(lang)
        response = client.get("/api/voice/i18n", headers=headers)
        assert response.status_code == 200
        assert response.json['lang'] == lang

def test_voice_plugin(client):
    response = client.get("/api/voice/plugin-test")
    assert response.status_code == 200
    assert 'plugin' in response.json

def test_voice_fallback_ia(client):
    response = client.get("/api/voice/ia-fallback")
    assert response.status_code == 200
    assert response.json['ia'] in ['LLaMA', 'Mixtral', 'Mistral']

def test_voice_rgpd_export(client):
    response = client.get("/api/voice/rgpd/export")
    assert response.status_code == 200
    assert 'export' in response.json

def test_voice_audit_log(client):
    response = client.get("/api/voice/audit-log")
    assert response.status_code == 200
    assert 'audit' in response.json

def test_voice_seo(client):
    response = client.get("/api/voice/seo/robots.txt")
    assert response.status_code == 200
    assert 'User-agent' in response.data.decode()
