# Exemple avancé permissions RBAC (Python)
def has_permission(user, permission):
    return permission in getattr(user, 'permissions', [])
