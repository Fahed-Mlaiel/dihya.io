"""
Test unitaire plugin analytics finance (Dihya Flask)
Couvre : collecte, anonymisation, RGPD
"""
import unittest
from backend.flask.app.analytics.plugins.finance_analytics import collect_finance_metrics

class TestFinanceAnalyticsPlugin(unittest.TestCase):
    def test_collect_finance_metrics(self):
        metrics = collect_finance_metrics()
        self.assertIn("transactions", metrics)
        self.assertIn("volume", metrics)
        self.assertTrue(metrics["anonymized"])
if __name__ == "__main__":
    unittest.main()
