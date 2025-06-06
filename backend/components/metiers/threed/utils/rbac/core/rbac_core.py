# rbac_core.py
"""Logique métier principale RBAC (Python)"""
def check_permission(user, permission):
    return permission in getattr(user, 'permissions', [])

def get_user_roles(user):
    return getattr(user, 'roles', [])

def has_permission(user, permission):
    # Permissions ultra basiques pour tests (à adapter selon logique métier)
    roles = user.get('roles', [])
    if 'admin' in roles:
        return True
    if 'guest' in roles and permission == 'read':
        return True
    return False
