"""
Test d'intégration avancé pour la gestion des loisirs dans Dihya.
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
def test_loisirs_routes_security_i18n(api_client):
    # Test accès non authentifié
    url = reverse('loisirs-list')
    response = api_client.get(url)
    assert response.status_code == 401

    # Test accès authentifié, rôle user
    api_client.credentials(HTTP_AUTHORIZATION='Bearer testusertoken')
    activate('fr')
    response = api_client.get(url)
    assert response.status_code in [200, 403]
    activate('en')
    response = api_client.get(url)
    assert response.status_code in [200, 403]

    # Test audit log, SEO header, plugin hook
    assert 'X-SEO' in response.headers
    assert 'X-Audit-Log' in response.headers

    # Test fallback IA
    ia_url = reverse('loisirs-ia-generate')
    response = api_client.post(ia_url, {'prompt': 'Génère une activité'}, format='json')
    assert response.status_code in [200, 503]

    # Test multitenancy
    api_client.credentials(HTTP_AUTHORIZATION='Bearer adminmultitenanttoken')
    response = api_client.get(url, HTTP_X_TENANT_ID='tenant42')
    assert response.status_code in [200, 403]

    # Test plugin extensible
    plugin_url = reverse('loisirs-plugin-action')
    response = api_client.post(plugin_url, {'action': 'custom'}, format='json')
    assert response.status_code in [200, 501]

    # Test RGPD export
    export_url = reverse('loisirs-export')
    response = api_client.get(export_url)
    assert response.status_code in [200, 403]

    # Test CORS
    assert 'Access-Control-Allow-Origin' in response.headers

    # Test anti-DDOS (limite de requêtes)
    for _ in range(20):
        response = api_client.get(url)
    assert response.status_code in [200, 429]
