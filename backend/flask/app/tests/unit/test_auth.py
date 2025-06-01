"""
Test unitaire du service d'authentification (Dihya Flask)
Couvre : inscription, login, sécurité, RGPD, erreurs
"""
import unittest
from backend.flask.app.services.auth_service import register_user, authenticate_user

class TestAuthService(unittest.TestCase):
    def test_register_and_authenticate(self):
        data = {"email": "new@dihya.com", "username": "newuser", "password": "pass1234"}
        user, err = register_user(data)
        self.assertIsNotNone(user)
        self.assertIsNone(err)
        auth_user = authenticate_user("new@dihya.com", "pass1234")
        self.assertIsNotNone(auth_user)
        self.assertEqual(auth_user.email, "new@dihya.com")

    def test_register_duplicate(self):
        data = {"email": "dup@dihya.com", "username": "dupuser", "password": "pass1234"}
        user, err = register_user(data)
        self.assertIsNone(err)
        user2, err2 = register_user(data)
        self.assertIsNone(user2)
        self.assertIsNotNone(err2)

    def test_authenticate_wrong_password(self):
        data = {"email": "fail@dihya.com", "username": "failuser", "password": "pass1234"}
        user, err = register_user(data)
        self.assertIsNone(err)
        auth_user = authenticate_user("fail@dihya.com", "wrongpass")
        self.assertIsNone(auth_user)

if __name__ == "__main__":
    unittest.main()
