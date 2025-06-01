"""
Service d'authentification pour l'application Dihya Coding.
Inclut : création utilisateur, vérification mot de passe, gestion sécurité.
"""

from ..models.user import User, get_user_by_email, add_user
from werkzeug.security import generate_password_hash

def register_user(data):
    """
    Crée un nouvel utilisateur après validation.
    Args:
        data (dict): Données d'inscription (email, username, password, etc.)
    Returns:
        (User, str): Utilisateur créé ou None, message d'erreur ou None
    """
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")
    role = data.get("role", "user")

    if get_user_by_email(email):
        return None, "Un utilisateur avec cet email existe déjà."

    user = User(
        id=len(User.USERS_DB) + 1 if hasattr(User, "USERS_DB") else len(globals().get("USERS_DB", {})) + 1,
        email=email,
        username=username,
        password=password,
        role=role
    )
    add_user(user)
    return user, None

def authenticate_user(email, password):
    """
    Authentifie un utilisateur par email et mot de passe.
    Args:
        email (str): Email utilisateur
        password (str): Mot de passe en clair
    Returns:
        User ou None
    """
    user = get_user_by_email(email)
    if user and user.check_password(password):
        return user
    return None