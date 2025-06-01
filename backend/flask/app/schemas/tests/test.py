"""
Tests avancés pour la validation des schémas (Python)
Sécurité, multitenancy, plugins, audit, mocks, e2e, multilingue
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from ...routes.validators import validators_bp
from ...utils.test_utils import mock_role, mock_audit

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(validators_bp)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_validate_schema_admin(client):
    mock_role('admin')
    token = create_access_token(identity='admin')
    res = client.post('/api/validators/validate',
                      json={'field': 'value'},
                      headers={'Authorization': f'Bearer {token}'})
    assert res.status_code == 200
    assert res.json['msg'] == 'validated'

def test_validate_schema_invalid(client):
    mock_role('admin')
    token = create_access_token(identity='admin')
    res = client.post('/api/validators/validate',
                      json={},
                      headers={'Authorization': f'Bearer {token}'})
    assert res.status_code >= 400

# ...autres tests : RGPD, plugins, audit, multilingue, e2e...
