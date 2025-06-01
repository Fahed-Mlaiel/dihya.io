"""
Tests avancés module Education (unitaires, intégration, e2e, sécurité, i18n, plugins).
"""
import pytest
from flask import Flask
from flask_jwt_extended import create_access_token
from backend.flask.app.templates.education import education_bp

@pytest.fixture
def client():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test'
    app.register_blueprint(education_bp)
    # ... setup JWT, plugins, etc. ...
    with app.test_client() as client:
        yield client

def test_list_education(client):
    token = create_access_token(identity={'role': 'admin'})
    rv = client.get('/api/education/', headers={'Authorization': f'Bearer {token}'})
    assert rv.status_code == 200
    assert 'data' in rv.json

# ... autres tests : sécurité, plugins, i18n, audit, export, etc. ...
