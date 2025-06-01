"""
Modèle User pour l'application Dihya Coding.
Inclut : ORM, gestion des rôles, hash de mot de passe, méthodes utilitaires.
"""

from werkzeug.security import generate_password_hash, check_password_hash

class User:
    """
    Modèle utilisateur (exemple générique, à adapter selon l'ORM utilisé).
    Attributs :
        - id : identifiant unique
        - email : email unique
        - username : nom d'utilisateur
        - password_hash : hash du mot de passe
        - role : rôle utilisateur (admin, user, invité, etc.)
        - is_active : booléen actif/inactif
    """

    def __init__(self, id, email, username, password, role="user", is_active=True):
        self.id = id
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.role = role
        self.is_active = is_active

    def check_password(self, password):
        """Vérifie le mot de passe."""
        return check_password_hash(self.password_hash, password)

    @property
    def is_admin(self):
        """Retourne True si l'utilisateur est admin."""
        return self.role == "admin"

    def to_dict(self):
        """Représentation JSON safe de l'utilisateur."""
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "role": self.role,
            "is_active": self.is_active
        }

# Exemple de stockage temporaire (à remplacer par une vraie base de données/ORM)
USERS_DB = {}

def get_user_by_email(email):
    """Récupère un utilisateur par email."""
    return next((u for u in USERS_DB.values() if u.email == email), None)

def get_user_by_id(user_id):
    """Récupère un utilisateur par ID."""
    return USERS_DB.get(user_id)

def add_user(user):
    """Ajoute un utilisateur à la base temporaire."""
    USERS_DB[user.id] = user

def remove_user(user_id):
    """Supprime un utilisateur."""
    return USERS_DB.pop(user_id, None)