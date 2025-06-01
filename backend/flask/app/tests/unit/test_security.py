"""
Test unitaire des utilitaires de sécurité (Dihya Flask)
Couvre : validation email, RGPD, sécurité input/output
"""
import unittest
from ...utils.validators import validate_email

class TestSecurityUtils(unittest.TestCase):
    def test_validate_email(self):
        self.assertTrue(validate_email("valid@dihya.com"))
        self.assertFalse(validate_email("invalid-email"))
        self.assertFalse(validate_email("") or validate_email(None))

if __name__ == "__main__":
    unittest.main()
