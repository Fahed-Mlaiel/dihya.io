# validators_helper.py
# Helper validators Python pour A_I – exemple clé en main
import re


def is_valid_email(email):
    """
    Vérifie si une chaîne est un email valide
    """
    # Interdit les doubles points
    if ".." in email:
        return False
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email))
