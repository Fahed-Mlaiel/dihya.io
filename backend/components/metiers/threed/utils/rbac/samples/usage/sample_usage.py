# sample_usage.py - Exemple d'utilisation RBAC

def check_permission(user, permission):
    return user and 'permissions' in user and permission in user['permissions']
