# rbac_utils.py – Module RBAC ultra avancé, clé en main, conforme RGPD et logique métier
ROLES = ['admin', 'editor', 'viewer', 'auditor', 'guest']
PERMISSIONS = {
    'admin': ['read', 'write', 'delete', 'manage_users', 'audit'],
    'editor': ['read', 'write'],
    'viewer': ['read'],
    'auditor': ['read', 'audit'],
    'guest': ['read']
}

def has_permission(user, permission):
    if not user or 'roles' not in user:
        return False
    return any(permission in PERMISSIONS.get(role, []) for role in user['roles'])

def get_user_permissions(user):
    if not user or 'roles' not in user:
        return []
    perms = set()
    for role in user['roles']:
        perms.update(PERMISSIONS.get(role, []))
    return list(perms)
