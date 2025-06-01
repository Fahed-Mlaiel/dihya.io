"""
Dihya – Tests pour le module Sécurité
- Couverture RGPD, sécurité, accessibilité
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import IncidentSecurite, AlerteSecurite, ControleSecurite
from rest_framework.test import APIClient
from rest_framework import status

class SecuriteAPITestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='secuser', password='testpass', is_securite_admin=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.incident = IncidentSecurite.objects.create(titre='Incident Test', description='Desc', niveau='mineur', signale_par=self.user)

    def test_create_alerte(self):
        data = {'titre': 'Alerte Test', 'message': 'Alerte', 'niveau': 'info'}
        response = self.client.post('/api/securite/alertesecurite/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['titre'], 'Alerte Test')

    def test_permission_denied_for_non_admin(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/securite/incidentsecurite/', {'titre': 'X', 'description': 'Y', 'niveau': 'mineur'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
