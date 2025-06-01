"""
Test unitaire constants.py (Dihya Flask)
Couvre : constantes globales, rôles, statuts
"""
import unittest
from backend.flask.app.core.constants import ROLE_ADMIN, STATUS_READY

class TestCoreConstants(unittest.TestCase):
    def test_roles(self):
        self.assertEqual(ROLE_ADMIN, "admin")
    def test_status(self):
        self.assertEqual(STATUS_READY, "ready")
if __name__ == "__main__":
    unittest.main()
