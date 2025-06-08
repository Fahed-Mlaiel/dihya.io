# Exemple avancé moteur RBAC (Python)
def rbac_engine(user, action):
    return 'admin' in getattr(user, 'roles', []) or action == 'read'
