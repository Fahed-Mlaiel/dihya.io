# sample_rbac.py
# Exemple d’intégration avancée pour la gestion des rôles

from helpers_rbac import assign_role, check_permission

user = {'id': 'u123', 'name': 'Alice', 'permissions': ['read']}
user = assign_role(user, 'admin')
print('Roles:', user['roles'])
print('Has read:', check_permission(user, 'read'))
print('Has write:', check_permission(user, 'write'))
