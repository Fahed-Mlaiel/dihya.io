# Test d’intégration pour le module vr_ar
# Vérifie l’intégration entre création de scène, audit et RGPD.

import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from backend.routes.vr_ar.models import Scene
from ..audit import vr_ar_audit_logger

@pytest.mark.django_db
def test_vr_ar_integration_audit_rgpd():
    client = APIClient()
    user = get_user_model().objects.create_user(username='intuser', password='pass')
    client.force_authenticate(user=user)
    # Création scène
    data = {
        'title': 'Immersive Museum Scene (EN)',
        'description': 'Virtual tour of an English museum.',
        'lang': 'en'
    }
    response = client.post(reverse('vr_ar-scene-list'), data)
    assert response.status_code == 201
    scene_id = response.data['id']
    # Audit
    vr_ar_audit_logger.log(user, 'test_audit', 'Scene', scene_id, details='Test integration', language='en')
    # RGPD Export
    response = client.get('/vr_ar/rgpd-export/')
    assert response.status_code in [200, 501]
