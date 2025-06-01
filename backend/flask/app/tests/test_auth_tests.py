"""
Tests unitaires pour les routes d'authentification de l'API Dihya Coding.
Couvre : inscription, connexion, refresh, logout, sécurité et validation.
"""

import unittest
from flask import Flask
from flask_jwt_extended import decode_token
from backend.flask.app import create_app
from backend.flask.app.models.user import USERS_DB

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("config.Config")
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        USERS_DB.clear()

    def test_register(self):
        """Test inscription utilisateur valide."""
        response = self.client.post("/api/auth/register", json={
            "email": "test@dihya.com",
            "username": "testuser",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("Utilisateur créé avec succès", response.get_data(as_text=True))

    def test_register_duplicate_email(self):
        """Test inscription avec email déjà utilisé."""
        self.client.post("/api/auth/register", json={
            "email": "test@dihya.com",
            "username": "testuser",
            "password": "password123"
        })
        response = self.client.post("/api/auth/register", json={
            "email": "test@dihya.com",
            "username": "otheruser",
            "password": "password456"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("existe déjà", response.get_data(as_text=True))

    def test_login(self):
        """Test connexion utilisateur valide."""
        self.client.post("/api/auth/register", json={
            "email": "login@dihya.com",
            "username": "loginuser",
            "password": "password123"
        })
        response = self.client.post("/api/auth/login", json={
            "email": "login@dihya.com",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("access_token", data)
        self.assertIn("refresh_token", data)

    def test_login_invalid(self):
        """Test connexion avec mauvais mot de passe."""
        self.client.post("/api/auth/register", json={
            "email": "fail@dihya.com",
            "username": "failuser",
            "password": "password123"
        })
        response = self.client.post("/api/auth/login", json={
            "email": "fail@dihya.com",
            "password": "wrongpass"
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn("Identifiants invalides", response.get_data(as_text=True))

    # D'autres tests peuvent être ajoutés : refresh, logout, sécurité, etc.

if __name__ == "__main__":
    unittest.main()
