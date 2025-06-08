# sample_advanced.py - Exemple métier avancé RBAC

def advanced_sample_rbac(user, action):
    if not user or 'role' not in user:
        return False
    if user['role'] == 'admin':
        return True
    if user['role'] == 'user' and action == 'read':
        return True
    return False
