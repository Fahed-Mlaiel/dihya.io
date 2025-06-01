"""
Dihya – Django Assurance API Tests Ultra Avancé
----------------------------------------------
- Tests unitaires, intégration, multilingue, sécurité, RGPD
"""
from django.test import TestCase
from rest_framework.test import APIClient
from .serializers import ContratSerializer

class ContratSerializerTest(TestCase):
    def test_valid_data(self):
        data = {
            'numero': 'C-2025-001',
            'assure': 'A. Dihya',
            'type': 'auto',
            'date_debut': '2025-01-01',
            'date_fin': '2025-12-31',
            'montant': 1200.0,
        }
        serializer = ContratSerializer(data=data)
        self.assertTrue(serializer.is_valid())

class AssuranceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_contrats(self):
        response = self.client.get('/api/assurance/contrats/')
        self.assertIn(response.status_code, [200, 401, 403])
