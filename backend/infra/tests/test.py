# Test d’intégration infrastructure Dihya Coding
# Sécurité, monitoring, backup, CI/CD, accessibilité, audit, multilingue
import unittest
from utils.utils import check_security, check_monitoring, check_backup, check_ci, check_accessibility, check_i18n

class TestInfrastructure(unittest.TestCase):
    def test_critical_requirements(self):
        self.assertTrue(check_security())
        self.assertTrue(check_monitoring())
        self.assertTrue(check_backup())
        self.assertTrue(check_ci())
        self.assertTrue(check_accessibility())
        self.assertTrue(check_i18n(['fr','en','ar','de','es','it','pt','ru','zh','ja','tr','ber','nl']))

if __name__ == '__main__':
    unittest.main()
