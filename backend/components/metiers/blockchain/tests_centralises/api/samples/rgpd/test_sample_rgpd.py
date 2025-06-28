import unittest
from backend.components.metiers.blockchain.api.samples.rgpd import sample_rgpd_sanitize


class TestSampleRGPD(unittest.TestCase):
    def test_rgpd_compliance(self):
        # TODO: Test de conformité RGPD
        self.assertTrue(True)

    def test_rgpd_data_erasure(self):
        # TODO: Test d'effacement des données RGPD
        self.assertIsNone(None)

    def test_import_sample_rgpd_sanitize(self):
        res = sample_rgpd_sanitize({"d": 1})
        self.assertIn("sanitized", res)
