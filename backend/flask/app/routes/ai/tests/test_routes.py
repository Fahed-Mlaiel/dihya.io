"""
Tests unitaires et d’intégration pour le module IA (Dihya)
Couvre : sécurité, i18n, audit, fallback IA, plugins, RGPD, SEO, multitenancy, REST, GraphQL
"""
import pytest
from flask import Flask
from backend.flask.app.routes.ai.ai import ai_blueprint
from ..services import get_ai_data, create_ai_entry, update_ai_entry, delete_ai_entry, search_ai

def test_blueprint_registration():
    app = Flask(__name__)
    if ai_blueprint:
        app.register_blueprint(ai_blueprint)
        client = app.test_client()
        resp = client.get('/api/ia/projects')
        assert resp.status_code in (401, 200, 403)

def test_create_ai_request_missing_fields(client):
    response = client.post('/ai/generate', json={})
    assert response.status_code == 400
    assert 'error' in response.json

def test_multilingual_support(client):
    response = client.post('/ai/generate', json={
        'prompt': 'مرحبا',
        'lang': 'ar',
        'model': 'ollama'
    })
    assert response.status_code == 200
    assert any(word in response.json.get('result', '') for word in ['مرحبا', 'Hello', 'Bonjour'])

def test_plugin_integration(client, monkeypatch):
    from ..plugins import plugin_manager, AIPluginBase
    class DummyPlugin(AIPluginBase):
        name = 'dummy'
        description = 'test'
        version = '1.0'
        author = 'test'
        def process(self, data):
            data['plugin'] = True
            return data
    plugin_manager.register(DummyPlugin())
    response = client.post('/ai/generate', json={
        'prompt': 'Test plugin',
        'lang': 'fr',
        'model': 'ollama'
    })
    assert response.status_code == 200
    assert response.json.get('plugin') is True

def test_audit_log(monkeypatch, client):
    from .. import audit
    logs = []
    def fake_log(*args, **kwargs):
        logs.append((args, kwargs))
    monkeypatch.setattr(audit.ai_audit_logger, 'log', fake_log)
    client.post('/ai/generate', json={
        'prompt': 'Test audit',
        'lang': 'fr',
        'model': 'ollama'
    })
    assert logs

def test_graphql_error(client):
    response = client.post('/ai/graphql', json={
        'query': '{ unknownField }'
    })
    assert response.status_code in (400, 422, 500)
    assert 'error' in response.json or 'errors' in response.json

def test_rgp_anonymization(client):
    from ..validators import anonymize_data
    data = {'prompt': 'Secret'}
    anonymized = anonymize_data(data)
    assert anonymized.get('prompt', '') == 'anonymized'

def test_accessibility_headers(client):
    response = client.get('/ai/generate')
    assert 'Content-Language' in response.headers

def test_security_headers(client):
    response = client.get('/ai/generate')
    assert response.headers.get('X-Frame-Options') == 'DENY'
    assert response.headers.get('X-XSS-Protection') == '1; mode=block'

def test_performance(client, benchmark):
    def create():
        return client.post('/ai/generate', json={
            'prompt': 'Perf',
            'lang': 'fr',
            'model': 'ollama'
        })
    result = benchmark(create)
    assert result.status_code == 200

def test_create_ai_entry():
    data = {"name": "GPT-4", "type": "NLP"}
    result = create_ai_entry(data, user="testuser")
    assert result["status"] == "created"

def test_get_ai_data():
    result = get_ai_data(1, user="testuser")
    assert "id" in result

def test_update_ai_entry
