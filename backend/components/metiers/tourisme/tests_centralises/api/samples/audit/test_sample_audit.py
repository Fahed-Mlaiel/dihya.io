import unittest
import importlib.util
import os

# Correction du chemin pour le module sample_audit.py
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../../metiers/tourisme/api/samples/audit/sample_audit.py'))
spec = importlib.util.spec_from_file_location("sample_audit", module_path)
sample_audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sample_audit)
audit_sample_action = sample_audit.audit_sample_action


class TestSampleAudit(unittest.TestCase):
    def test_audit_trail(self):
        # TODO: Test de la traçabilité audit
        self.assertTrue(True)

    def test_audit_event(self):
        # TODO: Test d'événement d'audit
        self.assertIsInstance("event", str)

    def test_import_audit_sample_action(self):
        self.assertTrue(callable(audit_sample_action), "audit_sample_action n'est pas défini ou n'est pas callable")
        res = audit_sample_action("user1", "login")
        self.assertIn("status", res)
