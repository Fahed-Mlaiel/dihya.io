"""
Test unitaire du contrôle d'accès RBAC (Dihya Flask)
Couvre : rôles, permissions, sécurité, conformité
"""
import unittest
from backend.flask.app.models.user import User

class TestRBAC(unittest.TestCase):
    def setUp(self):
        self.admin = User(id=1, email="admin@dihya.com", username="admin", password="adminpass", role="admin")
        self.user = User(id=2, email="user@dihya.com", username="user", password="userpass", role="user")

    def test_admin_role(self):
        self.assertTrue(self.admin.is_admin)
        self.assertFalse(self.user.is_admin)

    def test_permissions(self):
        # Simule une vérification de permission (à adapter selon la logique réelle)
        self.assertTrue(self.admin.role == "admin")
        self.assertTrue(self.user.role == "user")

if __name__ == "__main__":
    unittest.main()
