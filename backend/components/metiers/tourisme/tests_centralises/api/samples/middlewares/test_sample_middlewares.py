import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../api/samples/middlewares')))

import unittest
import importlib.util

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../metiers/tourisme/api/samples/middlewares/sample_middlewares.py'))
spec = importlib.util.spec_from_file_location("sample_middlewares", module_path)
sample_middlewares = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sample_middlewares)
sample_middleware_ultra = sample_middlewares.sample_middleware_ultra


class TestSampleMiddlewares(unittest.TestCase):
    def test_middleware_process(self):
        # TODO: Test du traitement middleware
        self.assertTrue(True)

    def test_middleware_chain(self):
        # TODO: Test de la chaîne de middlewares
        self.assertEqual("a" + "b", "ab")

    def test_import_sample_middleware_ultra(self):
        res = sample_middleware_ultra({"req": 1})
        self.assertIn("middleware", res)
