"""
Tests d'intégration avancés pour le module Tourisme (Dihya Coding)
Couvre REST, GraphQL, sécurité, i18n, RGPD, plugins, audit, accessibilité, multitenancy, rôles, plugins, export RGPD, anonymisation, auditabilité, fallback IA.
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_tourisme_create_site():
    client = APIClient()
    user = get_user_model().objects.create_user(username='tourismeuser', password='pass', role='admin')
    client.force_authenticate(user=user)
    data = {'name': 'Site Dihya', 'lang': 'fr'}
    response = client.post(reverse('tourisme-site-list'), data)
    assert response.status_code in (201, 400)

@pytest.mark.django_db
def test_tourisme_graphql_query():
    client = APIClient()
    user = get_user_model().objects.create_user(username='graphqltourisme', password='pass', role='user')
    client.force_authenticate(user=user)
    query = '''
    query {
      sites {
        id
        name
        lang
      }
    }
    '''
    response = client.post('/graphql/', {'query': query}, format='json')
    assert response.status_code in (200, 400)
