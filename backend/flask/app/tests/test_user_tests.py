"""
Tests unitaires pour les routes utilisateurs de l'API Dihya Coding.
Couvre : CRUD utilisateur, profil, sécurité, validation des accès et rôles.
"""

import unittest
from flask import Flask
from backend.flask.app import create_app
from backend.flask.app.models.user import USERS_DB

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("config.Config")
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        USERS_DB.clear()
        # Création d'un admin pour les tests
        self.admin_email = "admin@dihya.com"
        self.admin_password = "adminpass"
        self.client.post("/api/auth/register", json={
            "email": self.admin_email,
            "username": "admin",
            "password": self.admin_password,
            "role": "admin"
        })
        # Récupérer le token admin
        resp = self.client.post("/api/auth/login", json={
            "email": self.admin_email,
            "password": self.admin_password
        })
        self.admin_token = resp.get_json().get("access_token")

    def auth_header(self, token):
        return {"Authorization": f"Bearer {token}"}

    def test_get_profile(self):
        """Test récupération du profil utilisateur connecté."""
        resp = self.client.get("/api/users/me", headers=self.auth_header(self.admin_token))
        self.assertEqual(resp.status_code, 200)
        self.assertIn("email", resp.get_json())

    def test_list_users_admin(self):
        """Test que l'admin peut lister tous les utilisateurs."""
        resp = self.client.get("/api/users", headers=self.auth_header(self.admin_token))
        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.get_json(), list)

    def test_update_user_self(self):
        """Test mise à jour de son propre profil."""
        resp = self.client.put("/api/users/1", headers=self.auth_header(self.admin_token), json={
            "username": "admin_updated"
        })
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()["username"], "admin_updated")

    def test_delete_user_admin(self):
        """Test suppression d'un utilisateur par l'admin."""
        # Créer un user à supprimer
        self.client.post("/api/auth/register", json={
            "email": "user@dihya.com",
            "username": "user",
            "password": "userpass"
        })
        resp = self.client.delete("/api/users/2", headers=self.auth_header(self.admin_token))
        self.assertEqual(resp.status_code, 204)

    def test_access_denied_for_non_admin(self):
        """Test qu'un user non-admin ne peut pas lister ou supprimer d'autres users."""
        # Créer un user simple
        self.client.post("/api/auth/register", json={
            "email": "user2@dihya.com",
            "username": "user2",
            "password": "userpass"
        })
        resp = self.client.post("/api/auth/login", json={
            "email": "user2@dihya.com",
            "password": "userpass"
        })
        user_token = resp.get_json().get("access_token")
        # Tentative de listage
        resp = self.client.get("/api/users", headers=self.auth_header(user_token))
        self.assertEqual(resp.status_code, 403)
        # Tentative de suppression
        resp = self.client.delete("/api/users/1", headers=self.auth_header(user_token))
        self.assertEqual(resp.status_code, 403)

if __name__ == "__main__":
    unittest.main()
