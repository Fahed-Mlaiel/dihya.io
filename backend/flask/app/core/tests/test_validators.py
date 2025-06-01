"""
Test unitaire validators.py (Dihya Flask)
Couvre : fonctions de validation réutilisables
"""
import unittest
from backend.flask.app.core.validators import is_valid_email

class TestCoreValidators(unittest.TestCase):
    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("valid@dihya.com"))
        self.assertFalse(is_valid_email("invalid-email"))
if __name__ == "__main__":
    unittest.main()
