"""
Gestion centralisée des permissions et rôles pour Dihya Coding.

Ce module définit la matrice des permissions pour chaque rôle utilisateur (admin, user, invité, etc.)
et fournit des fonctions utilitaires pour vérifier l’accès à une ressource ou une action.

Bonnes pratiques :
- Centraliser la logique de permissions pour faciliter la maintenance et l’audit.
- Ne jamais coder en dur les permissions dans les routes ou services.
- Prévoir l’extensibilité pour de nouveaux rôles ou permissions métiers.
- Documenter chaque permission pour la conformité RGPD et la transparence.

Exemple d’utilisation :
    from backend.flask.app.models.roles.permissions import has_permission

    if not has_permission(user, "delete_project"):
        raise PermissionError("Accès refusé")
"""

# Définition des permissions par rôle
ROLE_PERMISSIONS = {
    "admin": {
        "manage_users",
        "manage_plugins",
        "delete_project",
        "view_audit_logs",
        "export_data",
        "import_data",
        "generate_project",
        "manage_templates",
        "manage_roles",
        "access_admin_panel",
        "view_all_projects",
        "manage_settings",
    },
    "user": {
        "generate_project",
        "view_own_projects",
        "update_profile",
        "send_feedback",
        "use_plugins",
        "view_templates",
    },
    "guest": {
        "view_templates",
        "view_public_projects",
        "register_account",
    }
}

def has_permission(user, permission):
    """
    Vérifie si l’utilisateur a la permission demandée.

    Args:
        user (dict): Dictionnaire utilisateur avec au moins le champ 'role'
        permission (str): Permission à vérifier

    Returns:
        bool: True si autorisé, False sinon
    """
    role = user.get("role", "guest")
    return permission in ROLE_PERMISSIONS.get(role, set())

def get_permissions_for_role(role):
    """
    Retourne la liste des permissions pour un rôle donné.

    Args:
        role (str): Nom du rôle

    Returns:
        set: Permissions associées au rôle
    """
    return ROLE_PERMISSIONS.get(role, set())

def is_admin(user):
    """
    Vérifie si l’utilisateur est administrateur.

    Args:
        user (dict): Dictionnaire utilisateur

    Returns:
        bool: True si admin, False sinon
    """
    return user.get("role") == "admin"
