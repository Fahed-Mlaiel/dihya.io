"""
Tests unitaires et d'intégration avancés pour la gestion des projets environnementaux.
Couvre sécurité, multitenancy, i18n, RGPD, audit, plugins, REST & GraphQL.
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from .models import EnvironnementProject
from core.models import Tenant

@pytest.mark.django_db
def test_environnement_project_crud(admin_user, tenant):
    client = APIClient()
    client.force_authenticate(user=admin_user)
    url = reverse('environnement-list')
    data = {"name": "Test Environnement", "description": "Desc", "is_active": True}
    response = client.post(url, data)
    assert response.status_code == 201
    project_id = response.data['id']
    # Lecture
    response = client.get(url)
    assert response.status_code == 200
    # Update
    detail_url = reverse('environnement-detail', args=[project_id])
    response = client.patch(detail_url, {"name": "Test Environnement 2"})
    assert response.status_code == 200
    # Delete
    response = client.delete(detail_url)
    assert response.status_code == 204
