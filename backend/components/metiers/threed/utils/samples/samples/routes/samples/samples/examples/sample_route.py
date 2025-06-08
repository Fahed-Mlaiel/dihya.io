# sample_route.py - Exemple métier avancé route imbriquée

def sample_route(user, action):
    if not user or 'role' not in user:
        return False
    if user['role'] == 'admin':
        return True
    if user['role'] == 'user' and action == 'read':
        return True
    return False
