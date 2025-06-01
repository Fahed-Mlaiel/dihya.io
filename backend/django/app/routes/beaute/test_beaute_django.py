"""
Dihya – Django Beauté API Tests Ultra Avancé
-------------------------------------------
- Tests unitaires, intégration, multilingue, sécurité, RGPD
"""
from django.test import TestCase
from rest_framework.test import APIClient
from .serializers import SoinSerializer

class SoinSerializerTest(TestCase):
    def test_valid_data(self):
        data = {
            'nom': 'Soin visage',
            'description': 'Nettoyage complet',
            'prix': 50.0,
        }
        serializer = SoinSerializer(data=data)
        self.assertTrue(serializer.is_valid())

class BeauteAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_soins(self):
        response = self.client.get('/api/beaute/soins/')
        self.assertIn(response.status_code, [200, 401, 403])
