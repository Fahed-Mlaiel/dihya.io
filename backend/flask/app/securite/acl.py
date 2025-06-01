"""
Gestion des listes de contrôle d'accès (ACL) pour Dihya Coding.

Ce module fournit des helpers pour vérifier les permissions d'accès aux ressources et routes,
gérer les rôles utilisateurs (Admin, User, Invité, etc.) et centraliser la logique d'autorisation.

Bonnes pratiques :
- Centraliser toutes les règles d'accès ici pour audit et maintenance.
- Documenter chaque fonction et chaque règle.
- Prévoir des tests unitaires pour chaque helper ACL.
- Ne jamais exposer la logique ACL dans les logs ou les messages d'erreur.
- Toujours vérifier le contexte utilisateur avant d'accorder un accès.

Exemple d'utilisation :
    from backend.flask.app.securite.acl import check_access

    if check_access(user, "admin_panel"):
        # action sécurisée
"""

from typing import List, Dict

ROLE_PERMISSIONS: Dict[str, List[str]] = {
    "admin": [
        "access_admin_panel",
        "manage_users",
        "view_reports",
        "edit_content",
        "delete_content",
        "access_sensitive_data",
    ],
    "user": [
        "view_content",
        "edit_own_content",
        "submit_project",
    ],
    "guest": [
        "view_content",
    ],
}

def get_user_roles(user) -> List[str]:
    """
    Récupère la liste des rôles d'un utilisateur.

    Args:
        user: Objet utilisateur (doit avoir un attribut 'roles' ou 'role').

    Returns:
        List[str]: Liste des rôles.
    """
    if hasattr(user, "roles") and user.roles:
        return user.roles
    elif hasattr(user, "role") and user.role:
        return [user.role]
    return []

def check_access(user, permission: str) -> bool:
    """
    Vérifie si l'utilisateur possède la permission demandée.

    Args:
        user: Objet utilisateur.
        permission (str): Permission à vérifier.

    Returns:
        bool: True si l'accès est autorisé, False sinon.
    """
    user_roles = get_user_roles(user)
    for role in user_roles:
        perms = ROLE_PERMISSIONS.get(role, [])
        if permission in perms:
            return True
    return False

def require_permission(permission: str):
    """
    Décorateur Flask pour protéger une route par une permission ACL.

    Args:
        permission (str): Permission requise.

    Usage :
        @require_permission("access_admin_panel")
        def admin_dashboard():
            ...
    """
    from functools import wraps
    from flask import abort, g

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            user = getattr(g, "current_user", None)
            if not user or not check_access(user, permission):
                abort(403)
            return f(*args, **kwargs)
        return wrapper
    return decorator

# Korrigiere alle absoluten app-Imports auf backend.flask.app-Imports
