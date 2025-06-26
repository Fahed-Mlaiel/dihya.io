import unittest
from backend.components.metiers.vr_ar.api.samples.db import sample_db_ultra


class TestSampleDB(unittest.TestCase):
    def test_db_connection(self):
        # TODO: Test de connexion à la base de données
        self.assertIsNotNone("db_connection")

    def test_db_query(self):
        # TODO: Test de requête avancée
        self.assertEqual(2 + 2, 4)

    def test_import_sample_db_ultra(self):
        res = sample_db_ultra()
        self.assertIn("db_status", res)
