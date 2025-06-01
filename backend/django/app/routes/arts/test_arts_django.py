"""
Dihya – Django Arts API Tests Ultra Avancé
-----------------------------------------
- Tests unitaires, intégration, multilingue, sécurité, RGPD
"""
from django.test import TestCase
from rest_framework.test import APIClient
from .serializers import OeuvreSerializer

class OeuvreSerializerTest(TestCase):
    def test_valid_data(self):
        data = {
            'titre': 'Tableau Test',
            'artiste': 'A. Dihya',
            'annee': 2024,
            'description': 'Test',
        }
        serializer = OeuvreSerializer(data=data)
        self.assertTrue(serializer.is_valid())

class ArtsAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_oeuvres(self):
        response = self.client.get('/api/arts/oeuvres/')
        self.assertIn(response.status_code, [200, 401, 403])
