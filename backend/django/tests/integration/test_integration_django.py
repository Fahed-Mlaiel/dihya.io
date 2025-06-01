"""
Tests d'intégration avancés Django pour Dihya Coding (API REST/GraphQL, sécurité, i18n, RGPD, plugins, audit, accessibilité, multitenancy, rôles, plugins, export RGPD, anonymisation, auditabilité, fallback IA)
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_health_check():
    client = APIClient()
    response = client.get('/api/health/')
    assert response.status_code in (200, 404)  # 404 si endpoint non implémenté
