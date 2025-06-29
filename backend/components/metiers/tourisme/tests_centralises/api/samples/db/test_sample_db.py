import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../api/samples/db')))

import unittest
import importlib.util

module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../metiers/tourisme/api/samples/db/sample_db.py'))
spec = importlib.util.spec_from_file_location("sample_db", module_path)
sample_db = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sample_db)
sample_db_ultra = sample_db.sample_db_ultra


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
