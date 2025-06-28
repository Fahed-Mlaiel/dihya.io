import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../api/samples/core')))

import unittest
import importlib.util

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../metiers/tourisme/api/samples/core/sample_core.py'))
spec = importlib.util.spec_from_file_location("sample_core", module_path)
sample_core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sample_core)
sample_core_logic = sample_core.sample_core_logic


class TestSampleCore(unittest.TestCase):
    def test_core_logic(self):
        # TODO: Test de la logique métier core
        self.assertTrue(True)

    def test_core_integration(self):
        # TODO: Test d'intégration core
        self.assertEqual(42, 42)

    def test_import_sample_core_logic(self):
        res = sample_core_logic({"x": 1})
        self.assertIn("core_processed", res)
