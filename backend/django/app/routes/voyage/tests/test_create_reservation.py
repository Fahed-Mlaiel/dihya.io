import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from ..models import Reservation

@pytest.mark.django_db
def test_create_reservation_fr():
    client = APIClient()
    user = get_user_model().objects.create_user(username='userfr', password='pass')
    client.force_authenticate(user=user)
    data = {
        'voyage': 'Paris-Marseille',
        'date': '2025-06-01T10:00:00Z',
        'status': 'confirmée',
        'lang': 'fr'
    }
    response = client.post(reverse('voyage-reservation-list'), data)
    assert response.status_code == 201
    assert Reservation.objects.filter(user=user, voyage='Paris-Marseille').exists()
