import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from ..models import Reservation

@pytest.mark.django_db
def test_permission_denied():
    client = APIClient()
    user1 = get_user_model().objects.create_user(username='user1', password='pass')
    user2 = get_user_model().objects.create_user(username='user2', password='pass')
    client.force_authenticate(user=user2)
    reservation = Reservation.objects.create(user=user1, voyage='London-Edinburgh', date='2025-06-02T11:00:00Z', status='confirmed', lang='en')
    response = client.delete(reverse('voyage-reservation-detail', args=[reservation.id]))
    assert response.status_code == 403
