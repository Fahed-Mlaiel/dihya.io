# rbac_engine.py – Moteur RBAC

def check_permission(user_role, action):
    # Exemple de logique RBAC simple
    if user_role == 'admin':
        return True
    if user_role == 'auditor' and action == 'audit':
        return True
    if user_role == 'manager' and action in ['read', 'write']:
        return True
    if user_role == 'user' and action == 'read':
        return True
    return False
