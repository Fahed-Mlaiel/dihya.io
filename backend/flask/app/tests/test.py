"""
Tests globaux API (sécurité, RGPD, audit, multi-langues, plugins, mocks)
"""
import pytest
import requests

def test_api_arts_oeuvres():
    url = 'http://localhost:5000/api/arts/oeuvres'
    headers = {'Authorization': 'Bearer test-jwt-token'}
    resp = requests.get(url, headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    assert 'data' in data
    assert isinstance(data['data'], list)
# ...autres tests globaux : sécurité, RGPD, audit, multi-langues, plugins, mocks...
