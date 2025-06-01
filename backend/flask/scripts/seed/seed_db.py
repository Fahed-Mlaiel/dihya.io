"""
Dihya – Script de seed base de données (données de démo, multilingue, métiers)
Usage: python seed_db.py
"""
import sys
from ...app.models.user import User
from ...app.models.user import USERS_DB

def seed():
    USERS_DB[1] = User(id=1, email="admin@dihya.com", username="admin", password="adminpass", role="admin")
    USERS_DB[2] = User(id=2, email="user@dihya.com", username="user", password="userpass", role="user")
    print("Seed utilisateurs injecté.")

if __name__ == "__main__":
    seed()
