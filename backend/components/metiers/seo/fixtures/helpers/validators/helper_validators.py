# helper_validators.py – Helpers de validation (Python)
def is_valid_email(email):
    """Valide le format d’un email."""
    import re

    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None
