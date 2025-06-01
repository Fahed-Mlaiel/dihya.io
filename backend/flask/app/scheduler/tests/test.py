"""
Tests avancés pour le scheduler (Python)
Sécurité, multitenancy, plugins, audit, mocks, e2e, multilingue
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from ... import scheduler
from ...utils.test_utils import mock_role, mock_audit

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(scheduler.bp)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_schedule_task_admin(client):
    mock_role('admin')
    token = create_access_token(identity='admin')
    res = client.post('/api/scheduler/schedule',
                      json={'task': 'backup', 'time': '2025-05-25T00:00:00Z'},
                      headers={'Authorization': f'Bearer {token}'})
    assert res.status_code == 200
    assert res.json['success'] is True

def test_schedule_task_unauthorized(client):
    mock_role('guest')
    token = create_access_token(identity='guest')
    res = client.post('/api/scheduler/schedule',
                      json={'task': 'backup', 'time': '2025-05-25T00:00:00Z'},
                      headers={'Authorization': f'Bearer {token}'})
    assert res.status_code == 403

# ...autres tests : plugins, audit, multilingue, e2e...
