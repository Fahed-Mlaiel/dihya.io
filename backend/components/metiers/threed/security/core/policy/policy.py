# policy.py – Politiques de sécurité avancées

def enforce_policy(user, action, resource):
    if getattr(user, 'is_admin', False):
        return True
    if hasattr(user, 'permissions') and action in user.permissions:
        return True
    return False
