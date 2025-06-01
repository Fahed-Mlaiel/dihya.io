import pytest
import time
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_scene_creation_performance():
    client = APIClient()
    user = get_user_model().objects.create_user(username='perfuser', password='pass')
    client.force_authenticate(user=user)
    data = {
        'title': 'Scène immersive musée (FR)',
        'description': 'Visite virtuelle d’un musée français.',
        'lang': 'fr'
    }
    start = time.time()
    response = client.post(reverse('vr_ar-scene-list'), data)
    duration = time.time() - start
    assert response.status_code == 201
    assert duration < 2  # La création doit être rapide
