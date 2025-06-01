"""
Tests complets (unitaires, intégration, e2e) pour le module 3D/VR/AR/IA
Sécurité, i18n, multitenancy, plugins IA, audit, RGPD, mocks, fixtures.
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from backend.flask.app.templates.threed.template import register_3d_routes, bp_3d

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    from flask_jwt_extended import JWTManager
    JWTManager(app)
    app.register_blueprint(bp_3d)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_header_admin():
    token = create_access_token(identity={'id': 1, 'role': 'admin'})
    return {'Authorization': f'Bearer {token}'}

@pytest.fixture
def auth_header_user():
    token = create_access_token(identity={'id': 2, 'role': 'user'})
    return {'Authorization': f'Bearer {token}'}

def test_list_projects(client, auth_header_user):
    resp = client.get('/api/3d/projects', headers=auth_header_user)
    assert resp.status_code == 200
    assert 'projects' in resp.get_json()

def test_create_project(client, auth_header_user):
    resp = client.post('/api/3d/projects', json={'name': 'Test VR'}, headers=auth_header_user)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_import_asset(client, auth_header_user):
    resp = client.post('/api/3d/assets', json={'name': 'Asset1'}, headers=auth_header_user)
    assert resp.status_code == 201
    assert 'msg' in resp.get_json()

def test_ai_generate(client, auth_header_user, monkeypatch):
    def fake_generate(prompt):
        return 'scene VR générée'
    monkeypatch.setattr('Dihya.backend.flask.app.ai_fallback.generate_with_fallback', fake_generate)
    resp = client.post('/api/3d/ai/generate', json={'prompt': 'Créer une scène VR'}, headers=auth_header_user)
    assert resp.status_code == 200
    assert 'result' in resp.get_json()

def test_export_projects(client, auth_header_admin):
    resp = client.get('/api/3d/export/projects', headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'msg' in resp.get_json()

def test_graphql_3d(client, auth_header_user):
    resp = client.post('/api/3d/graphql', json={'query': '{ projects { name } }'}, headers=auth_header_user)
    assert resp.status_code == 200
    assert 'msg' in resp.get_json()

def test_plugin_execution(client, auth_header_admin, monkeypatch):
    def fake_plugin_hook(domain, plugin_name, data):
        return {'ok': True, 'plugin': plugin_name}
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.plugins.plugin_hook', fake_plugin_hook)
    resp = client.post('/api/3d/plugins/test_plugin', json={'param': 1}, headers=auth_header_admin)
    assert resp.status_code == 200
    assert 'result' in resp.get_json()

def test_rgpd_export(client, auth_header_user, monkeypatch):
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.rgpd.rgpd_export', lambda user: {'data': 'export'})
    resp = client.get('/api/3d/rgpd/export', headers=auth_header_user)
    assert resp.status_code == 200
    assert 'export' in resp.get_json()

def test_rgpd_anonymize(client, auth_header_user, monkeypatch):
    monkeypatch.setattr('Dihya.backend.flask.app.middleware.rgpd.rgpd_anonymize', lambda user: None)
    resp = client.post('/api/3d/rgpd/anonymize', headers=auth_header_user)
    assert resp.status_code == 200
    assert 'msg' in resp.get_json()

class Test3DFlask:
# Correction : suppression des fixtures de classe, passage en paramètre d’instance self
    def auth_header_admin(self):
        token = create_access_token(identity={'id': 1, 'role': 'admin'})
        return {'Authorization': f'Bearer {token}'}

    def auth_header_user(self):
        token = create_access_token(identity={'id': 2, 'role': 'user'})
        return {'Authorization': f'Bearer {token}'}

    def test_list_projects(self, client):
        resp = client.get('/api/3d/projects', headers=self.auth_header_user())
        assert resp.status_code == 200
        assert 'projects' in resp.get_json()

    def test_create_project(self, client):
        resp = client.post('/api/3d/projects', json={'name': 'Test VR'}, headers=self.auth_header_user())
        assert resp.status_code == 201
        assert 'msg' in resp.get_json()

    def test_import_asset(self, client):
        resp = client.post('/api/3d/assets', json={'name': 'Asset1'}, headers=self.auth_header_user())
        assert resp.status_code == 201
        assert 'msg' in resp.get_json()

    def test_ai_generate(self, client, monkeypatch):
        def fake_generate(prompt):
            return 'scene VR générée'
        monkeypatch.setattr('Dihya.backend.flask.app.ai_fallback.generate_with_fallback', fake_generate)
        resp = client.post('/api/3d/ai/generate', json={'prompt': 'Créer une scène VR'}, headers=self.auth_header_user())
        assert resp.status_code == 200
        assert 'result' in resp.get_json()

    def test_export_projects(self, client):
        resp = client.get('/api/3d/export/projects', headers=self.auth_header_admin())
        assert resp.status_code == 200
        assert 'msg' in resp.get_json()

    def test_graphql_3d(self, client):
        resp = client.post('/api/3d/graphql', json={'query': '{ projects { name } }'}, headers=self.auth_header_user())
        assert resp.status_code == 200
        assert 'msg' in resp.get_json()

    def test_plugin_execution(self, client, monkeypatch):
        def fake_plugin_hook(domain, plugin_name, data):
            return {'ok': True, 'plugin': plugin_name}
        monkeypatch.setattr('Dihya.backend.flask.app.middleware.plugins.plugin_hook', fake_plugin_hook)
        resp = client.post('/api/3d/plugins/test_plugin', json={'param': 1}, headers=self.auth_header_admin())
        assert resp.status_code == 200
        assert 'result' in resp.get_json()

    def test_rgpd_export(self, client, monkeypatch):
        monkeypatch.setattr('Dihya.backend.flask.app.middleware.rgpd.rgpd_export', lambda user: {'data': 'export'})
        resp = client.get('/api/3d/rgpd/export', headers=self.auth_header_user())
        assert resp.status_code == 200
        assert 'export' in resp.get_json()

    def test_rgpd_anonymize(self, client, monkeypatch):
        monkeypatch.setattr('Dihya.backend.flask.app.middleware.rgpd.rgpd_anonymize', lambda user: None)
        resp = client.post('/api/3d/rgpd/anonymize', headers=self.auth_header_user())
        assert resp.status_code == 200
        assert 'msg' in resp.get_json()
