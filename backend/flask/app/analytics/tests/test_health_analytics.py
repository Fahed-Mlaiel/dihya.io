"""
Test unitaire plugin analytics santé (Dihya Flask)
Couvre : collecte, anonymisation, RGPD
"""
import unittest
from backend.flask.app.analytics.plugins.health_analytics import collect_health_metrics

class TestHealthAnalyticsPlugin(unittest.TestCase):
    def test_collect_health_metrics(self):
        metrics = collect_health_metrics()
        self.assertIn("patients", metrics)
        self.assertIn("appointments", metrics)
        self.assertTrue(metrics["anonymized"])
if __name__ == "__main__":
    unittest.main()
