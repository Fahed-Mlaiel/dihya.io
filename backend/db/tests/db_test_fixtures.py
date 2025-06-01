"""
Tests d'importation et de validation des fixtures multilingues
"""
import pytest
import json
import os
import sys
sys.path.insert(0, '.')
from backend.db import migrations

FIXTURES_PATH = os.path.join(os.path.dirname(__file__), '../fixtures_example.json')

@pytest.fixture(scope='session')
def fixtures():
    with open(FIXTURES_PATH, encoding='utf-8') as f:
        data = json.load(f)
    return data

def test_fixtures_structure(fixtures):
    for user in fixtures:
        assert 'username' in user
        assert 'email' in user
        assert 'lang' in user
        assert user['lang'] in ['fr', 'en', 'ar', 'tzm']

def test_fixtures_rgpd(fixtures):
    for user in fixtures:
        assert isinstance(user['consent_rgpd'], bool)
