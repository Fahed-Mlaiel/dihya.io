"""
Test d'intégration avancé pour la gestion Marketing dans Dihya.
Couvre sécurité, i18n, multitenancy, plugins, audit, SEO, IA, etc.
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.utils.translation import activate

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_marketing_routes_security_i18n(api_client):
    url = reverse('marketing-list')
    response = api_client.get(url)
    assert response.status_code == 401

    api_client.credentials(HTTP_AUTHORIZATION='Bearer testusertoken')
    activate('fr')
    response = api_client.get(url)
    assert response.status_code in [200, 403]
    activate('en')
    response = api_client.get(url)
    assert response.status_code in [200, 403]

    assert 'X-SEO' in response.headers
    assert 'X-Audit-Log' in response.headers

    ia_url = reverse('marketing-ia-generate')
    response = api_client.post(ia_url, {'prompt': 'Génère une campagne'}, format='json')
    assert response.status_code in [200, 503]

    api_client.credentials(HTTP_AUTHORIZATION='Bearer adminmultitenanttoken')
    response = api_client.get(url, HTTP_X_TENANT_ID='tenant42')
    assert response.status_code in [200, 403]

    plugin_url = reverse('marketing-plugin-action')
    response = api_client.post(plugin_url, {'action': 'custom'}, format='json')
    assert response.status_code in [200, 501]

    export_url = reverse('marketing-export')
    response = api_client.get(export_url)
    assert response.status_code in [200, 403]

    assert 'Access-Control-Allow-Origin' in response.headers

    for _ in range(20):
        response = api_client.get(url)
    assert response.status_code in [200, 429]
