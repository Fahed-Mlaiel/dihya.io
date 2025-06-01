import pytest
from backend.flask.app import create_app

app = create_app()

def test_health():
    client = app.test_client()
    resp = client.get('/health')
    assert resp.status_code == 200
    assert resp.json['status'] == 'ok'

def test_login():
    client = app.test_client()
    resp = client.post('/api/v1/login', json={'username': 'test'})
    assert resp.status_code == 200
    assert 'access_token' in resp.json

def test_i18n():
    client = app.test_client()
    resp = client.get('/api/v1/i18n?lang=fr')
    assert resp.status_code == 200
    assert 'Bienvenue' in resp.json['message']

def test_rgpd_export(monkeypatch):
    client = app.test_client()
    # Mock JWT
    monkeypatch.setattr('flask_jwt_extended.view_decorators.verify_jwt_in_request', lambda *a, **kw: None)
    monkeypatch.setattr('flask_jwt_extended.get_jwt_identity', lambda: 'test')
    resp = client.get('/api/v1/rgpd/export')
    assert resp.status_code == 200
    assert 'data' in resp.json

def test_plugin_run(monkeypatch):
    client = app.test_client()
    monkeypatch.setattr('flask_jwt_extended.view_decorators.verify_jwt_in_request', lambda *a, **kw: None)
    monkeypatch.setattr('flask_jwt_extended.get_jwt_identity', lambda: 'test')
    resp = client.post('/api/v1/plugins/demo/run', json={'input': 'test'})
    assert resp.status_code == 200
    assert 'result' in resp.json

def test_ai_generate(monkeypatch):
    client = app.test_client()
    monkeypatch.setattr('flask_jwt_extended.view_decorators.verify_jwt_in_request', lambda *a, **kw: None)
    monkeypatch.setattr('flask_jwt_extended.get_jwt_identity', lambda: 'test')
    resp = client.post('/api/v1/ai/generate', json={'prompt': 'Hello'})
    assert resp.status_code == 200
    assert 'result' in resp.json

def test_graphql(monkeypatch):
    client = app.test_client()
    query = '{ __schema { queryType { name } } }'
    resp = client.post('/graphql', json={'query': query})
    assert resp.status_code == 200
    assert 'data' in resp.json
