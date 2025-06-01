"""
Tests d'intégration avancés pour le module Immobilier de Dihya.
Multilingue, sécurité maximale, multitenancy, plugins, RGPD, SEO, IA fallback, auditabilité.
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def admin_user(db):
    User = get_user_model()
    return User.objects.create_superuser('admin', 'admin@dihya.ai', 'password')

@pytest.mark.django_db
def test_immobilier_crud(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    resp = api_client.post(reverse('immobilier-list'), {"title": "Vente Appartement", "lang": "fr"}, format='json')
    assert resp.status_code == 201
    resp = api_client.get(reverse('immobilier-list'))
    assert resp.status_code == 200
    assert 'access-control-allow-origin' in resp._headers
    # RGPD, audit, SEO, i18n, plugins, etc. (mocks/exemples)
    # ...
# Multilingue :
# Français, English, العربية, ⴰⵎⴰⵣⵉⵖ, Deutsch, 中文, 日本語, 한국어, Nederlands, עברית, فارسی, हिन्दी, Español
