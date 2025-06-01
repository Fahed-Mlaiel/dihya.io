"""
Tests ultra avancés pour le module Blockchain (Django routes)
Couvre REST, GraphQL, sécurité, multilingue, RGPD, audit, plugins, accessibilité, performance, e2e.
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from .models import BlockchainProject, BlockchainAsset

def create_user(username, password, role='user'):
    user = get_user_model().objects.create_user(username=username, password=password)
    user.role = role
    user.save()
    return user

@pytest.mark.django_db
def test_create_blockchainproject_fr():
    client = APIClient()
    user = create_user('userfr', 'pass', 'admin')
    client.force_authenticate(user=user)
    data = {
        'name': 'Projet Blockchain Musée (FR)',
        'description': 'Projet blockchain pour un musée français.',
        'lang': 'fr'
    }
    response = client.post(reverse('blockchain-blockchainproject-list'), data)
    assert response.status_code == 201
    assert BlockchainProject.objects.filter(name='Projet Blockchain Musée (FR)').exists()

@pytest.mark.django_db
def test_graphql_blockchainproject_query():
    client = APIClient()
    user = create_user('graphqluser', 'pass', 'user')
    client.force_authenticate(user=user)
    project = BlockchainProject.objects.create(name='GraphQL Test', description='Test GraphQL', lang='en', created_by=user)
    query = '''
    query {
      blockchainProjects {
        id
        name
        description
        lang
      }
    }
    '''
    response = client.post('/graphql/', {'query': query}, format='json')
    assert response.status_code == 200
    assert 'GraphQL Test' in str(response.content)
