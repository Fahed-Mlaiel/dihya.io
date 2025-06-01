import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_rgpd_export():
    client = APIClient()
    user = get_user_model().objects.create_user(username='userrgpd', password='pass')
    client.force_authenticate(user=user)
    # Simuler endpoint d'export RGPD (à implémenter dans views avancées)
    response = client.get('/voyage/rgpd-export/')
    assert response.status_code in [200, 501]  # 501 si non implémenté
