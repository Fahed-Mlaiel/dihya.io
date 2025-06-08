# helpers_rbac.py
# Helpers avancés pour la gestion des rôles et permissions dynamiques

def assign_role(user, role):
    """Simule l’assignation d’un rôle à un utilisateur"""
    user = dict(user)
    user['roles'] = user.get('roles', []) + [role]
    return user

def check_permission(user, permission):
    """Simule la vérification d’une permission"""
    return user and 'permissions' in user and permission in user['permissions']
