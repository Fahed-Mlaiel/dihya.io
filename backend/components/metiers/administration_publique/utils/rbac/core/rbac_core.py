# rbac_core.py
"""Logique métier principale RBAC (Python)"""
def check_permission(user, permission):
    return permission in getattr(user, 'permissions', [])

def get_user_roles(user):
    return getattr(user, 'roles', [])
