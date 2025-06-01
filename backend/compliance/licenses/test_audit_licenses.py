"""
Tests unitaires pour audit_licenses.py (couverture maximale, multilingue)
"""
import unittest
import os
from audit_licenses import audit_licenses

class TestAuditLicenses(unittest.TestCase):
    def test_audit_licenses(self):
        license_dir = os.path.dirname(__file__)
        found = audit_licenses(license_dir)
        self.assertIn('LICENSE_AGPL.txt', found)
        self.assertIn('LICENSE_APACHE.txt', found)
        self.assertIn('LICENSE_MIT.txt', found)

if __name__ == "__main__":
    unittest.main()
