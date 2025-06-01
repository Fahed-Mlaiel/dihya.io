"""
Dihya – Tests pour le module Publicité
- Couverture RGPD, sécurité, accessibilité
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import CampagnePublicitaire, AnalyticsPublicite
from rest_framework.test import APIClient
from rest_framework import status

class PubliciteAPITestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='pubuser', password='testpass', is_publicite_admin=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.campagne = CampagnePublicitaire.objects.create(nom='Pub Test', canal='display', budget='1000.00', date_debut='2025-01-01T00:00:00Z', date_fin='2025-12-31T23:59:59Z', cree_par=self.user)

    def test_create_analytics(self):
        data = {'campagne': self.campagne.id, 'impressions': 1000, 'clics': 100, 'conversions': 10}
        response = self.client.post('/api/publicite/analyticspublicite/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['impressions'], 1000)

    def test_permission_denied_for_non_admin(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/publicite/campagnepublicitaire/', {'nom': 'X', 'canal': 'display', 'budget': '1000.00', 'date_debut': '2025-01-01T00:00:00Z', 'date_fin': '2025-12-31T23:59:59Z'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
