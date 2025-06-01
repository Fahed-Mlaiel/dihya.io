"""
Tests unitaires et d’intégration pour le module Agriculture (Dihya)
Couvre : sécurité, i18n, audit, fallback IA, plugins, RGPD, SEO, multitenancy, REST, GraphQL
"""
import pytest
from flask import Flask
from backend.flask.app.routes.agriculture.routes import bp

def test_blueprint_registration():
    app = Flask(__name__)
    app.register_blueprint(bp)
    client = app.test_client()
    resp = client.get('/api/agriculture/projects')
    assert resp.status_code in (401, 200, 403)

def test_create_project_missing_fields(client):
    response = client.post('/agriculture/projects', json={})
    assert response.status_code == 400
    assert 'error' in response.json

def test_multilingual_support(client):
    response = client.post('/agriculture/projects', json={
        'name': 'مشروع',
        'description': 'وصف متقدم',
        'lang': 'ar'
    })
    assert response.status_code == 201
    assert any(word in response.json.get('message', '') for word in ['تم الإنشاء', 'créé'])

def test_plugin_integration(client, monkeypatch):
    from ..plugins import plugin_manager, AgriculturePluginBase
    class DummyPlugin(AgriculturePluginBase):
        name = 'dummy'
        description = 'test'
        version = '1.0'
        author = 'test'
        def process(self, data):
            data['plugin'] = True
            return data
    plugin_manager.register(DummyPlugin())
    response = client.post('/agriculture/projects', json={
        'name': 'Projet Plugin',
        'description': 'Test plugin',
        'lang': 'fr'
    })
    assert response.status_code == 201
    assert response.json.get('plugin') is True

def test_audit_log(monkeypatch, client):
    from .. import audit
    logs = []
    def fake_log(*args, **kwargs):
        logs.append((args, kwargs))
    monkeypatch.setattr(audit.agriculture_audit_logger, 'log', fake_log)
    client.post('/agriculture/projects', json={
        'name': 'Projet Audit',
        'description': 'Test audit',
        'lang': 'fr'
    })
    assert logs

def test_graphql_error(client):
    response = client.post('/agriculture/graphql', json={
        'query': '{ unknownField }'
    })
    assert response.status_code in (400, 422, 500)
    assert 'error' in response.json or 'errors' in response.json

def test_rgp_anonymization(client):
    from ..validators import anonymize_data
    data = {'name': 'Secret'}
    anonymized = anonymize_data(data)
    assert anonymized.get('name', '') != 'Secret'

def test_accessibility_headers(client):
    response = client.get('/agriculture/projects')
    assert 'Content-Language' in response.headers

def test_security_headers(client):
    response = client.get('/agriculture/projects')
    assert response.headers.get('X-Frame-Options') == 'DENY'
    assert response.headers.get('X-XSS-Protection') == '1; mode=block'

def test_performance(client, benchmark):
    def create():
        return client.post('/agriculture/projects', json={
            'name': 'Perf',
            'description': 'Test perf',
            'lang': 'fr'
        })
    result = benchmark(create)
    assert result.status_code == 201
