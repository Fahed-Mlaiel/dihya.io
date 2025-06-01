"""
Module pour la gestion avancée des rôles utilisateurs dans Dihya Coding.

Ce package permet de définir, valider et gérer les différents rôles utilisateurs (Admin, User, Invité, etc.)
et leurs permissions associées pour le backend Flask.

Bonnes pratiques :
- Centraliser la définition des rôles et permissions ici.
- Valider chaque action sensible selon le rôle de l’utilisateur.
- Prévoir l’extension pour de nouveaux rôles ou permissions spécifiques.
- Documenter chaque rôle et ses droits dans le README associé.
- Ne jamais exposer de logique de permission côté client.

Exemple d’utilisation :
    from backend.flask.app.models.roles import has_permission

    if has_permission(user, "delete_project"):
        # action autorisée
"""

ROLES = {
    "admin": ["create_user", "delete_user", "view_logs", "manage_plugins", "delete_project"],
    "user": ["create_project", "edit_project", "view_project"],
    "guest": ["view_project"]
}

def has_permission(user, permission):
    """
    Vérifie si l’utilisateur possède la permission demandée.
    :param user: objet utilisateur (doit avoir un attribut 'role')
    :param permission: nom de la permission à vérifier
    :return: booléen
    """
    role = getattr(user, "role", "guest")
    return permission in ROLES.get(role, [])
