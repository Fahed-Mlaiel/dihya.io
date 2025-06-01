"""
Test unitaire du modèle User (Dihya Flask)
Couvre : création, hash, rôles, sécurité, RGPD, to_dict
"""
import unittest
from backend.flask.app.models.user import User

class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.user = User(id=1, email="test@dihya.com", username="testuser", password="password123", role="admin")

    def test_password_hash(self):
        self.assertTrue(self.user.check_password("password123"))
        self.assertFalse(self.user.check_password("wrong"))

    def test_is_admin(self):
        self.assertTrue(self.user.is_admin)

    def test_to_dict(self):
        d = self.user.to_dict()
        self.assertEqual(d["email"], "test@dihya.com")
        self.assertEqual(d["role"], "admin")
        self.assertNotIn("password_hash", d)

if __name__ == "__main__":
    unittest.main()
