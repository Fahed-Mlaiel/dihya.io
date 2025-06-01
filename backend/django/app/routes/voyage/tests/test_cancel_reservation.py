import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from ..models import Reservation

@pytest.mark.django_db
def test_cancel_reservation_arabic():
    client = APIClient()
    user = get_user_model().objects.create_user(username='userar', password='pass')
    client.force_authenticate(user=user)
    reservation = Reservation.objects.create(user=user, voyage='القاهرة-الإسكندرية', date='2025-06-03T12:00:00Z', status='مؤكدة', lang='ar')
    response = client.delete(reverse('voyage-reservation-detail', args=[reservation.id]))
    assert response.status_code in [204, 200]
    assert not Reservation.objects.filter(id=reservation.id).exists()
