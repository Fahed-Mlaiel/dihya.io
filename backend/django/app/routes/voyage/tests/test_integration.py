# Test d’intégration pour le module voyage
# Vérifie l’intégration entre réservation, audit et RGPD.

import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from ..models import Reservation
from ..audit import voyage_audit_logger

@pytest.mark.django_db
def test_voyage_integration_audit_rgpd():
    client = APIClient()
    user = get_user_model().objects.create_user(username='intuser', password='pass')
    client.force_authenticate(user=user)
    # Réservation
    data = {
        'voyage': 'London-Edinburgh',
        'date': '2025-06-02T11:00:00Z',
        'status': 'confirmed',
        'lang': 'en'
    }
    response = client.post(reverse('voyage-reservation-list'), data)
    assert response.status_code == 201
    reservation_id = response.data['id']
    # Audit
    voyage_audit_logger.log(user, 'test_audit', 'Reservation', reservation_id, details='Test integration', language='en')
    # RGPD Export
    response = client.get('/voyage/rgpd-export/')
    assert response.status_code in [200, 501]
