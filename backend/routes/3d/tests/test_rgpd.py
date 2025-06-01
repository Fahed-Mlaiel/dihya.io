import pytest
from ..routes import app

def test_export_rgpd(client):
    response = client.post('/threedprojects/1/export_rgpd/')
    assert response.status_code == 200
    assert 'export' in response.json
