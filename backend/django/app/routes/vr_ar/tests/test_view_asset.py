import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from backend.routes.vr_ar.models import Asset, Scene

@pytest.mark.django_db
def test_view_asset_arabic():
    client = APIClient()
    user = get_user_model().objects.create_user(username='userar', password='pass')
    client.force_authenticate(user=user)
    scene = Scene.objects.create(title='مشهد متحف تفاعلي (AR)', description='جولة افتراضية في متحف عربي.', lang='ar', created_by=user)
    asset = Asset.objects.create(scene=scene, file='assets/scene_ar.glb', type='3D', lang='ar')
    response = client.get(reverse('vr_ar-asset-list'))
    assert response.status_code == 200
    assert any(a['lang'] == 'ar' for a in response.data['results'])
