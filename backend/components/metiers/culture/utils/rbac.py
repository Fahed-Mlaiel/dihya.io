"""
Contrôle d'accès basé sur les rôles (RBAC) pour Environnement.
"""

def check_permission(user, action):
    """
    Vérifie si l'utilisateur a la permission d'effectuer une action.
    """
    # Exemple métier : admin a tous les droits, les autres seulement lecture
    return user == "admin" or action == "read"
