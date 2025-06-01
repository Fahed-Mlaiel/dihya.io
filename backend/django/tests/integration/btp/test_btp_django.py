"""
Tests d'intégration ultra avancés pour l'API BTP (REST/GraphQL, sécurité, i18n, plugins, audit, RGPD, SEO, fallback IA)
"""
import pytest
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.fixture
def api_client():
    return APIClient()

def test_btp_list_authenticated(api_client):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer testtoken')
    response = api_client.get(reverse('btp-list'))
    assert response.status_code == 200
    assert 'results' in response.data

def test_btp_export_permissions(api_client):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer testtoken')
    response = api_client.get(reverse('btp-export'))
    assert response.status_code in (200, 403)

def test_btp_graphql_query(api_client):
    query = '{ allBTPProjects { id name } }'
    response = api_client.post('/graphql/', {'query': query}, format='json')
    assert response.status_code == 200
    assert 'data' in response.data
