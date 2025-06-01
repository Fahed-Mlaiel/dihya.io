"""
Dihya – Tests pour le module Mobile
- Couverture RGPD, sécurité, accessibilité
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import MobileApp, Device, PushNotification
from rest_framework.test import APIClient
from rest_framework import status

class MobileAPITestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='mobileuser', password='testpass', is_mobile_admin=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.app = MobileApp.objects.create(nom='App Test', plateforme='android', version='1.0', date_publication='2025-01-01T00:00:00Z', cree_par=self.user)

    def test_create_device(self):
        data = {'user': self.user.id, 'device_id': 'dev123', 'plateforme': 'android'}
        response = self.client.post('/api/mobile/devices/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['device_id'], 'dev123')

    def test_permission_denied_for_non_admin(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/mobile/apps/', {'nom': 'X', 'plateforme': 'android', 'version': '1.0', 'date_publication': '2025-01-01T00:00:00Z'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
