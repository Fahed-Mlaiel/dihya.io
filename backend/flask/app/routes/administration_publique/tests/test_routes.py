"""
Tests unitaires et d'intégration avancés pour Administration Publique
Couvre sécurité, RGPD, plugins, audit, i18n, multitenancy, REST+GraphQL.
"""
import pytest
from flask import Flask
from ..routes import administration_publique_blueprint

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(administration_publique_blueprint)
    return app

def test_create_project(client):
    # Test création projet (REST)
    response = client.post('/administration_publique/projects', json={
        'name': 'Projet Test',
        'description': 'Description avancée',
        'lang': 'fr'
    })
    assert response.status_code == 201
    assert 'id' in response.json

def test_i18n_created(client):
    # Test i18n (fr)
    response = client.post('/administration_publique/projects', json={
        'name': 'Projet Test',
        'description': 'Description avancée',
        'lang': 'fr'
    })
    assert 'créé' in response.json.get('message', '')

def test_create_project_missing_fields(client):
    response = client.post('/administration_publique/projects', json={})
    assert response.status_code == 400
    assert 'error' in response.json

def test_multilingual_support(client):
    response = client.post('/administration_publique/projects', json={
        'name': 'مشروع',
        'description': 'وصف متقدم',
        'lang': 'ar'
    })
    assert response.status_code == 201
    assert any(word in response.json.get('message', '') for word in ['تم الإنشاء', 'créé'])

def test_plugin_integration(client, monkeypatch):
    from ..plugins import plugin_manager, AdminPubliquePluginBase
    class DummyPlugin(AdminPubliquePluginBase):
        name = 'dummy'
        description = 'test'
        version = '1.0'
        author = 'test'
        def process(self, data):
            data['plugin'] = True
            return data
    plugin_manager.register(DummyPlugin())
    response = client.post('/administration_publique/projects', json={
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
    monkeypatch.setattr(audit.administration_publique_audit_logger, 'log', fake_log)
    client.post('/administration_publique/projects', json={
        'name': 'Projet Audit',
        'description': 'Test audit',
        'lang': 'fr'
    })
    assert logs

def test_graphql_error(client):
    response = client.post('/administration_publique/graphql', json={
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
    response = client.get('/administration_publique/projects')
    assert 'Content-Language' in response.headers

def test_security_headers(client):
    response = client.get('/administration_publique/projects')
    assert response.headers.get('X-Frame-Options') == 'DENY'
    assert response.headers.get('X-XSS-Protection') == '1; mode=block'

def test_performance(client, benchmark):
    def create():
        return client.post('/administration_publique/projects', json={
            'name': 'Perf',
            'description': 'Test perf',
            'lang': 'fr'
        })
    result = benchmark(create)
    assert result.status_code == 201
