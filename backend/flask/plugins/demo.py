"""
Exemple de plugin métier pour Dihya Coding Backend
"""
def run(user, payload):
    return {'msg': f'Plugin exécuté pour {user} avec {payload}'}
