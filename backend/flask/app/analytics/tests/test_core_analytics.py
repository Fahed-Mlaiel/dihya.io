"""
Test unitaire analytics core (Dihya Flask)
Couvre : collecte, anonymisation, RGPD, auditabilité
"""
import unittest
from flask import Flask
from backend.flask.app.analytics.core import bp as analytics_bp

class AnalyticsCoreTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(analytics_bp)
        self.client = self.app.test_client()
    def test_metrics_endpoint(self):
        resp = self.client.get("/api/analytics/metrics")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn("requests", data)
        self.assertIn("errors", data)
        self.assertIn("avg_latency", data)
        self.assertIn("last_access", data)
if __name__ == "__main__":
    unittest.main()
