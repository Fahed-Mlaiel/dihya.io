"""
@file test_integration_node.py
@description Test d'intégration global (Python) pour l'ensemble des APIs Dihya (sécurité, i18n, RGPD, plugins, audit, REST/GraphQL, multitenancy, etc.)
@author Dihya
@date 2025-05-25
"""

import requests
import os
import pytest

BASE_URL = os.getenv('DIHYA_API_URL', 'http://localhost:3000')
USER_TOKEN = os.getenv('DIHYA_TEST_USER_TOKEN', 'testtoken')

@pytest.mark.parametrize('api', [
    'loisirs', 'manufacturing', 'marketing', 'medias', 'mobile', 'mode', 'preview', 'publicite', 'recherche',
    'ressources_humaines', 'restauration', 'sante', 'science', 'securite', 'seo', 'services_personne',
    'social', 'sport', 'tourisme', 'transport'
])
def test_api_routes(api):
    headers = {'Authorization': f'Bearer {USER_TOKEN}', 'Accept-Language': 'fr'}
    r = requests.get(f'{BASE_URL}/api/{api}', headers=headers)
    assert r.status_code == 200
    assert 'data' in r.json()
    assert 'x-audit-log-id' in r.headers

def test_graphql_global():
    headers = {'Authorization': f'Bearer {USER_TOKEN}'}
    r = requests.post(f'{BASE_URL}/graphql', json={'query': '{ loisirs { id nom } }'}, headers=headers)
    assert r.status_code == 200
    assert 'loisirs' in r.json().get('data', {})

def test_rgpd_export():
    headers = {'Authorization': f'Bearer {USER_TOKEN}'}
    r = requests.get(f'{BASE_URL}/api/loisirs/export', headers=headers)
    assert r.status_code == 200
    assert 'anonymized' in r.json()
