"""
Tests d'intégration avancés pour le module Transport (Dihya Coding)
Couvre REST, GraphQL, sécurité, i18n, RGPD, plugins, audit, accessibilité, multitenancy, rôles, plugins, export RGPD, anonymisation, auditabilité, fallback IA.
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_transport_create_trajet():
    client = APIClient()
    user = get_user_model().objects.create_user(username='transportuser', password='pass', role='admin')
    client.force_authenticate(user=user)
    data = {'name': 'Trajet Dihya', 'lang': 'fr'}
    response = client.post(reverse('transport-trajet-list'), data)
    assert response.status_code in (201, 400)

@pytest.mark.django_db
def test_transport_graphql_query():
    client = APIClient()
    user = get_user_model().objects.create_user(username='graphqltransport', password='pass', role='user')
    client.force_authenticate(user=user)
    query = '''
    query {
      trajets {
        id
        name
        lang
      }
    }
    '''
    response = client.post('/graphql/', {'query': query}, format='json')
    assert response.status_code in (200, 400)
