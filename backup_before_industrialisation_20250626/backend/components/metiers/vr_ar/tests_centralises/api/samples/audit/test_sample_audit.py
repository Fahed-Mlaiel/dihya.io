import unittest
import importlib

sample_audit = importlib.import_module("backend.components.metiers.vr_ar.api.samples.audit.sample_audit")
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
