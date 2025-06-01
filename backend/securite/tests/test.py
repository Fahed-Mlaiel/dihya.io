# Test d’intégration sécurité Dihya Coding
# RGPD, plugins, audit, accessibilité, CI/CD, monitoring, fallback AI
import unittest
from utils.utils import check_security, check_gdpr, check_plugins, check_audit, check_accessibility, check_ci, check_monitoring, check_fallback_ai

class TestSecurite(unittest.TestCase):
    def test_advanced_security(self):
        self.assertTrue(check_security())
        self.assertTrue(check_gdpr())
        self.assertTrue(check_plugins())
        self.assertTrue(check_audit())
        self.assertTrue(check_accessibility())
        self.assertTrue(check_ci())
        self.assertTrue(check_monitoring())
        self.assertTrue(check_fallback_ai())

if __name__ == '__main__':
    unittest.main()
