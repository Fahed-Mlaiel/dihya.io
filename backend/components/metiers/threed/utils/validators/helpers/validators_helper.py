# validators_helper.py
# Helper validators Python pour Threed – exemple clé en main
import re

def is_valid_email(email):
    """
    Vérifie si une chaîne est un email valide
    """
    return bool(re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email))
