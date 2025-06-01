import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from backend.routes.vr_ar.models import Scene

@pytest.mark.django_db
def test_vr_ar_e2e_workflow():
    client = APIClient()
    user = get_user_model().objects.create_user(username='e2euser', password='pass')
    client.force_authenticate(user=user)
    # Création scène
    data = {
        'title': 'Scène immersive musée (FR)',
        'description': 'Visite virtuelle d’un musée français.',
        'lang': 'fr'
    }
    response = client.post(reverse('vr_ar-scene-list'), data)
    assert response.status_code == 201
    scene_id = response.data['id']
    # Suppression
    response = client.delete(reverse('vr_ar-scene-detail', args=[scene_id]))
    assert response.status_code in [204, 200]
