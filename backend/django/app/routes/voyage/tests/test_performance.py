import pytest
import time
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_reservation_performance():
    client = APIClient()
    user = get_user_model().objects.create_user(username='perfuser', password='pass')
    client.force_authenticate(user=user)
    data = {
        'voyage': 'Paris-Marseille',
        'date': '2025-06-01T10:00:00Z',
        'status': 'confirmée',
        'lang': 'fr'
    }
    start = time.time()
    response = client.post(reverse('voyage-reservation-list'), data)
    duration = time.time() - start
    assert response.status_code == 201
    assert duration < 2  # La réservation doit être rapide
