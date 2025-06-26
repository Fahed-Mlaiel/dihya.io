import unittest
from threed.api.samples.middlewares import sample_middleware_ultra


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
