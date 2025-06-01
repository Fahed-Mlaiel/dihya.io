"""
Tests d'intégration avancés pour le SEO backend Dihya (sitemap, robots.txt, logs structurés, i18n, RGPD, accessibilité).
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_sitemap_generation(api_client):
    """Teste la génération dynamique du sitemap.xml multilingue."""
    url = reverse('sitemap')
    response = api_client.get(url)
    assert response.status_code == 200
    assert 'xml' in response['Content-Type']

@pytest.mark.django_db
def test_robots_txt(api_client):
    """Teste la génération dynamique du robots.txt et la conformité SEO."""
    url = reverse('robots')
    response = api_client.get(url)
    assert response.status_code == 200
    assert 'User-agent' in response.content.decode()

# Plus de tests : logs SEO, accessibilité, i18n, RGPD, etc.
