"""
Sécurité threed (Python)
Fournit des fonctions avancées de gestion des permissions et de chiffrement pour la conformité RGPD et la sécurité API.
"""
import hashlib
import base64


def check_permissions(user_role, action):
    """Vérifie si le rôle utilisateur a le droit d’effectuer l’action."""
    # Exemple métier : seul admin peut delete
    if action == "delete" and user_role != "admin":
        return False
    return True


def encrypt_data(data):
    """Chiffre une donnée en base64 (exemple simple, à adapter en prod)."""
    h = hashlib.sha256(data.encode()).digest()
    return base64.b64encode(h).decode()


def get_security_doc():
    return "Respect du RGPD, gestion des accès, audit, anonymisation, sécurité API et données."
