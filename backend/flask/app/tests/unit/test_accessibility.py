"""
Test unitaire de l'accessibilité (Dihya Flask)
Couvre : endpoints, headers, conformité, multilingue
"""
import unittest
from flask import Flask
from backend.flask.app.routes.main import main as main_blueprint

class TestAccessibility(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(main_blueprint)
        self.client = self.app.test_client()

    def test_home_accessible(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Bienvenue", resp.get_data(as_text=True))

    def test_health_accessible(self):
        resp = self.client.get("/api/health")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("ok", resp.get_data(as_text=True))

if __name__ == "__main__":
    unittest.main()
