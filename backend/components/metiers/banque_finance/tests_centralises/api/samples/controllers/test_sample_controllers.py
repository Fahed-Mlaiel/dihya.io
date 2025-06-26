import sys
import os
import importlib.util

spec = importlib.util.spec_from_file_location("sample_controllers", "/workspaces/dihya.io/backend/components/metiers/banque_finance/api/samples/controllers/sample_controllers.py")
sample_controllers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sample_controllers)


import unittest


class TestSampleControllers(unittest.TestCase):
    def test_controller_logic(self):
        # Test nominal
        result = sample_controllers.sample_controller_ultra()
        self.assertIn("created", result)
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["created"]["name"], "UltraCube")
        # Edge case: données manquantes
        # (à compléter si la fonction évolue)

    def test_controller_integration(self):
        # Test d'intégration avancé pour les controllers (placeholder)
        self.assertEqual(1, 1)
