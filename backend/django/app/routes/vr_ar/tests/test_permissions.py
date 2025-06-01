import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from backend.routes.vr_ar.models import Scene

@pytest.mark.django_db
def test_permission_denied():
    client = APIClient()
    user1 = get_user_model().objects.create_user(username='user1', password='pass')
    user2 = get_user_model().objects.create_user(username='user2', password='pass')
    client.force_authenticate(user=user2)
    scene = Scene.objects.create(title='Immersive Museum Scene (EN)', description='Virtual tour of an English museum.', lang='en', created_by=user1)
    response = client.delete(reverse('vr_ar-scene-detail', args=[scene.id]))
    assert response.status_code == 403
