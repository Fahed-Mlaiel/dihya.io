"""
Module de validation – Dihya Coding

Ce module centralise les fonctions de validation réutilisables pour les données d’entrée
(formulaires, API, modèles), afin de garantir la sécurité, la cohérence métier et la conformité RGPD.

Bonnes pratiques :
- Toujours valider les emails, mots de passe, champs critiques côté backend
- Retourner des messages d’erreur génériques (jamais d’info sensible)
- Documenter chaque fonction de validation
"""

import re

EMAIL_REGEX = re.compile(r"^[^@]+@[^@]+\.[^@]+$")
PASSWORD_POLICY = {
    "min_length": 8,
    "require_upper": True,
    "require_lower": True,
    "require_digit": True,
    "require_special": True
}

def is_valid_email(email: str) -> bool:
    """
    Valide le format d’une adresse email (RFC 5322 simplifié).

    Args:
        email (str): Adresse email à valider.

    Returns:
        bool: True si l’email est valide, False sinon.
    """
    return bool(email and EMAIL_REGEX.match(email))

def is_valid_password(password: str, policy: dict = PASSWORD_POLICY) -> bool:
    """
    Valide un mot de passe selon la politique de sécurité Dihya Coding.

    Args:
        password (str): Mot de passe à valider.
        policy (dict): Politique de sécurité (modifiable pour tests).

    Returns:
        bool: True si le mot de passe est conforme, False sinon.
    """
    if not password or len(password) < policy["min_length"]:
        return False
    if policy["require_upper"] and not re.search(r"[A-Z]", password):
        return False
    if policy["require_lower"] and not re.search(r"[a-z]", password):
        return False
    if policy["require_digit"] and not re.search(r"\d", password):
        return False
    if policy["require_special"] and not re.search(r"[^\w\s]", password):
        return False
    return True

def is_valid_username(username: str) -> bool:
    """
    Valide un nom d’utilisateur (alphanumérique, tirets, 3-32 caractères).

    Args:
        username (str): Nom d’utilisateur à valider.

    Returns:
        bool: True si le nom est valide, False sinon.
    """
    return bool(username and re.match(r"^[a-zA-Z0-9_-]{3,32}$", username))

def is_valid_project_name(name: str) -> bool:
    """
    Valide un nom de projet (alphanumérique, espaces, tirets, 3-64 caractères).

    Args:
        name (str): Nom de projet à valider.

    Returns:
        bool: True si le nom est valide, False sinon.
    """
    return bool(name and re.match(r"^[\w\s\-]{3,64}$", name))

def sanitize_input(text: str) -> str:
    """
    Nettoie une chaîne de caractères pour éviter les injections simples (XSS, SQL).

    Args:
        text (str): Texte à nettoyer.

    Returns:
        str: Texte nettoyé.
    """
    if not text:
        return ""
    # Supprime les balises HTML simples
    return re.sub(r"<.*?>", "", text)