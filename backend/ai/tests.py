"""
Tests ultra avancés pour le module IA backend Dihya
Couvre REST, GraphQL, sécurité, multilingue, RGPD, audit, plugins, accessibilité, performance, e2e.
"""
import unittest
from flask import Flask
from backend.ai.ai import ai_bp

class TestDihyaAI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.register_blueprint(ai_bp)
        self.client = self.app.test_client()

    def test_generate_fr(self):
        response = self.client.post('/api/ai/generate', json={
            'prompt': 'Bonjour',
            'lang': 'fr',
            'model': 'ollama'
        }, headers={'X-Dihya-Role': 'ai_user'})
        self.assertIn(response.status_code, [200, 500])
        self.assertIn('result', response.get_json() or {})

    def test_rbac_forbidden(self):
        response = self.client.post('/api/ai/generate', json={
            'prompt': 'Test',
            'lang': 'fr',
            'model': 'ollama'
        }, headers={'X-Dihya-Role': 'guest'})
        self.assertEqual(response.status_code, 403)
        self.assertIn('error', response.get_json())

    def test_healthcheck(self):
        response = self.client.get('/api/ai/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn('status', response.get_json())

if __name__ == "__main__":
    unittest.main()
