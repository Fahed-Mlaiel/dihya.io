# Exemple avancé rôles RBAC (Python)
def has_role(user, role):
    return role in getattr(user, "roles", [])
