"""
test.py - Tests GraphQL API (Python)
"""
import pytest
from flask import Flask
from backend.flask.app.graphql.routes import graphql_bp
from backend.flask.app.utils.test_helpers import get_jwt

@pytest.fixture(scope="module")
def client():
    app = Flask(__name__)
    app.register_blueprint(graphql_bp)
    with app.test_client() as client:
        yield client

@pytest.fixture(scope="module")
def admin_token():
    return get_jwt('admin')

def test_projects_query(client, admin_token):
    res = client.post('/graphql', headers={"Authorization": f"Bearer {admin_token}"}, json={"query": "{ projects { id name } }"})
    assert res.status_code == 200
    assert isinstance(res.json["data"]["projects"], list)

def test_access_denied_without_jwt(client):
    res = client.post('/graphql', json={"query": "{ projects { id } }"})
    assert res.status_code == 401
