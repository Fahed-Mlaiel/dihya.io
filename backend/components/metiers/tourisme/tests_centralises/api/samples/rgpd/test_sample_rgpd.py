import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../api/samples/rgpd')))

import unittest
import importlib.util

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../metiers/tourisme/api/samples/rgpd/sample_rgpd.py'))
spec = importlib.util.spec_from_file_location("sample_rgpd", module_path)
sample_rgpd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sample_rgpd)
sample_rgpd_sanitize = sample_rgpd.sample_rgpd_sanitize


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
