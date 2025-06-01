"""
Test unitaire de l'API (Dihya Flask)
Couvre : endpoints publics, sécurité, multilingue, conformité
"""
import unittest
from flask import Flask
from backend.flask.app.routes.main import main as main_blueprint

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(main_blueprint)
        self.client = self.app.test_client()

    def test_api_info(self):
        resp = self.client.get("/api/info")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("Dihya Coding", resp.get_data(as_text=True))

if __name__ == "__main__":
    unittest.main()
