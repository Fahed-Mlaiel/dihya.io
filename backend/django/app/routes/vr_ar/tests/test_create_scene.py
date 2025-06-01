import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from backend.routes.vr_ar.models import Scene

@pytest.mark.django_db
def test_create_scene_fr():
    client = APIClient()
    user = get_user_model().objects.create_user(username='userfr', password='pass')
    client.force_authenticate(user=user)
    data = {
        'title': 'Scène immersive musée (FR)',
        'description': 'Visite virtuelle d’un musée français.',
        'lang': 'fr'
    }
    response = client.post(reverse('vr_ar-scene-list'), data)
    assert response.status_code == 201
    assert Scene.objects.filter(title='Scène immersive musée (FR)').exists()
