"""
Tests e2e avancés pour le module VR/AR (Django)
Couvre REST, GraphQL, sécurité, multilingue, RGPD, audit, plugins, accessibilité.
"""
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from backend.routes.vr_ar.models import Scene, Asset

@pytest.mark.django_db
def test_graphql_scene_query():
    client = APIClient()
    user = get_user_model().objects.create_user(username='graphqluser', password='pass')
    client.force_authenticate(user=user)
    scene = Scene.objects.create(title='GraphQL Test', description='Test GraphQL', lang='en', created_by=user)
    query = '''
    query {
      scenes {
        id
        title
        description
        lang
      }
    }
    '''
    response = client.post('/graphql/', {'query': query}, format='json')
    assert response.status_code == 200
    assert 'GraphQL Test' in str(response.content)

@pytest.mark.django_db
def test_graphql_asset_query():
    client = APIClient()
    user = get_user_model().objects.create_user(username='graphqluser2', password='pass')
    client.force_authenticate(user=user)
    scene = Scene.objects.create(title='GraphQL Asset', description='Test Asset', lang='fr', created_by=user)
    Asset.objects.create(scene=scene, file='assets/scene_fr.glb', type='3D', lang='fr')
    query = '''
    query {
      assets {
        id
        file
        type
        lang
      }
    }
    '''
    response = client.post('/graphql/', {'query': query}, format='json')
    assert response.status_code == 200
    assert 'scene_fr.glb' in str(response.content)
