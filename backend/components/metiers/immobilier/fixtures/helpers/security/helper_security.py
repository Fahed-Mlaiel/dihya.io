# helper_security.py – Helpers de sécurité (Python)
def hash_password(password):
    """Hash ultra avancé d’un mot de passe."""
    import hashlib

    return hashlib.sha256(password.encode()).hexdigest()
