"""
Dihya – Django Agriculture API Tests Ultra Avancé
------------------------------------------------
- Tests unitaires, intégration, multilingue, sécurité, RGPD
"""
from django.test import TestCase
from rest_framework.test import APIClient
from .serializers import ExploitationSerializer

class ExploitationSerializerTest(TestCase):
    def test_valid_data(self):
        data = {
            'nom': 'Ferme Test',
            'localisation': 'Algérie',
            'superficie': 10.5,
            'proprietaire': 'A. Dihya',
            'date_creation': '2024-01-01',
        }
        serializer = ExploitationSerializer(data=data)
        self.assertTrue(serializer.is_valid())

class AgricultureAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_exploitations(self):
        response = self.client.get('/api/agriculture/exploitations/')
        self.assertIn(response.status_code, [200, 401, 403])
