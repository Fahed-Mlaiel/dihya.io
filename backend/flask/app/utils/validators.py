"""
Utilitaires de validation pour l'application Dihya Coding.
Inclut : validation d'inscription, de connexion, de mise à jour utilisateur, etc.
"""

import re

def validate_email(email):
    """
    Valide le format d'un email.
    Args:
        email (str)
    Returns:
        bool
    """
    if not email:
        return False
    regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(regex, email) is not None

def validate_registration(data):
    """
    Valide les données d'inscription utilisateur.
    Args:
        data (dict)
    Returns:
        list: Liste d'erreurs, vide si aucune erreur
    """
    errors = []
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")

    if not email or not validate_email(email):
        errors.append("Email invalide ou manquant.")
    if not username or len(username) < 3:
        errors.append("Nom d'utilisateur trop court (min 3 caractères).")
    if not password or len(password) < 6:
        errors.append("Mot de passe trop court (min 6 caractères).")
    return errors

def validate_login(data):
    """
    Valide les données de connexion utilisateur.
    Args:
        data (dict)
    Returns:
        list: Liste d'erreurs, vide si aucune erreur
    """
    errors = []
    email = data.get("email")
    password = data.get("password")
    if not email or not validate_email(email):
        errors.append("Email invalide ou manquant.")
    if not password:
        errors.append("Mot de passe manquant.")
    return errors

def validate_user_update(data):
    """
    Valide les données de mise à jour utilisateur.
    Args:
        data (dict)
    Returns:
        list: Liste d'erreurs, vide si aucune erreur
    """
    errors = []
    if "email" in data and not validate_email(data["email"]):
        errors.append("Email invalide.")
    if "username" in data and len(data["username"]) < 3:
        errors.append("Nom d'utilisateur trop court (min 3 caractères).")
    return errors

def validate_generate_payload(data):
    """
    Valide le payload pour la génération de projet (API /api/generate).
    Args:
        data (dict)
    Returns:
        list: Liste d'erreurs, vide si aucune erreur
    """
    errors = []
    spec = data.get("spec")
    type_ = data.get("type")
    stack = data.get("stack")
    if not spec or len(spec) < 10:
        errors.append("Spécification trop courte ou manquante.")
    if not type_:
        errors.append("Type de projet manquant.")
    if not stack:
        errors.append("Stack technique manquante.")
    return errors

def validate_plugin_payload(payload):
    """
    Valide le payload d'un plugin (nom, version, unicité, etc.).
    Args:
        payload (dict)
    Returns:
        bool
    """
    if not isinstance(payload, dict):
        return False
    name = payload.get("name")
    version = payload.get("version")
    if not name or not isinstance(name, str) or len(name) < 2:
        return False
    if not version or not isinstance(version, str):
        return False
    return True
