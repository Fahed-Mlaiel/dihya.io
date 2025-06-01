"""
Test unitaire plugin analytics IA (Dihya Flask)
Couvre : collecte, anonymisation, RGPD
"""
import unittest
from backend.flask.app.analytics.plugins.ia_analytics import collect_ia_metrics

class TestIAAnalyticsPlugin(unittest.TestCase):
    def test_collect_ia_metrics(self):
        metrics = collect_ia_metrics()
        self.assertIn("requests", metrics)
        self.assertIn("models", metrics)
        self.assertTrue(metrics["anonymized"])
if __name__ == "__main__":
    unittest.main()
