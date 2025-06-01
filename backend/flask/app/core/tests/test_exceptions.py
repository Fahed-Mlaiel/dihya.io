"""
Test unitaire exceptions.py (Dihya Flask)
Couvre : exceptions globales, héritage, messages
"""
import unittest
from backend.flask.app.core.exceptions import DihyaBaseException, ValidationError

class TestCoreExceptions(unittest.TestCase):
    def test_base_exception(self):
        e = DihyaBaseException("Erreur générique")
        self.assertEqual(str(e), "Erreur générique")
    def test_validation_error(self):
        e = ValidationError("Erreur de validation")
        self.assertEqual(str(e), "Erreur de validation")
        self.assertTrue(isinstance(e, DihyaBaseException))
if __name__ == "__main__":
    unittest.main()
