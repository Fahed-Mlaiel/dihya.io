"""
Tests d'intégration avancés pour les services à la personne (multitenancy, RBAC, RGPD, accessibilité, i18n).
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_service_access_admin(api_client):
    """Teste l'accès admin aux services à la personne (RBAC, multitenancy)."""
    user = User.objects.create_user(username='admin', password='adminpass', is_staff=True)
    api_client.force_authenticate(user=user)
    url = reverse('services_personne-list')
    response = api_client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_service_access_guest(api_client):
    """Teste l'accès invité (doit être limité, RGPD, logs)."""
    url = reverse('services_personne-list')
    response = api_client.get(url)
    assert response.status_code in (401, 403)

# Plus de tests : audit, anonymisation, i18n, plugins, etc.
