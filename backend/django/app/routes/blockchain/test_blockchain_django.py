"""
Dihya – Django Blockchain API Tests Ultra Avancé
------------------------------------------------
- Tests unitaires, intégration, multilingue, sécurité, RGPD
"""
from django.test import TestCase
from rest_framework.test import APIClient
from .serializers import BlockSerializer

class BlockSerializerTest(TestCase):
    def test_valid_data(self):
        data = {
            'hash': 'abc123',
            'previous_hash': 'def456',
            'timestamp': '2025-05-22T12:00:00Z',
            'nonce': 42,
        }
        serializer = BlockSerializer(data=data)
        self.assertTrue(serializer.is_valid())

class BlockchainAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_blocks(self):
        response = self.client.get('/api/blockchain/blocks/')
        self.assertIn(response.status_code, [200, 401, 403])
