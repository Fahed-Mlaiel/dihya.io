import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from ..models import Reservation

@pytest.mark.django_db
def test_voyage_e2e_workflow():
    client = APIClient()
    user = get_user_model().objects.create_user(username='e2euser', password='pass')
    client.force_authenticate(user=user)
    # Création réservation
    data = {
        'voyage': 'Paris-Marseille',
        'date': '2025-06-01T10:00:00Z',
        'status': 'confirmée',
        'lang': 'fr'
    }
    response = client.post(reverse('voyage-reservation-list'), data)
    assert response.status_code == 201
    reservation_id = response.data['id']
    # Suppression
    response = client.delete(reverse('voyage-reservation-detail', args=[reservation_id]))
    assert response.status_code in [204, 200]
