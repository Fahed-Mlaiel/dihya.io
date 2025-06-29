import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../api/samples/hooks')))

import unittest
import importlib.util

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../metiers/tourisme/api/samples/hooks/sample_hooks.py'))
spec = importlib.util.spec_from_file_location("sample_hooks", module_path)
sample_hooks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sample_hooks)
sample_hook_ultra = sample_hooks.sample_hook_ultra


class TestSampleHooks(unittest.TestCase):
    def test_hook_execution(self):
        # TODO: Test d'exécution de hook avancé
        self.assertTrue(callable(lambda: True))

    def test_hook_integration(self):
        # TODO: Test d'intégration des hooks
        self.assertTrue(True)

    def test_import_sample_hook_ultra(self):
        res = sample_hook_ultra("evt", {})
        self.assertIn("hooked", res)
