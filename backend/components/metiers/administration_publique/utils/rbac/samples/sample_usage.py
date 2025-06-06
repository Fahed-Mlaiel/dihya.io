# sample_usage.py
"""Exemple d'utilisation du module RBAC (Python)"""
from ..core import rbac_core
import json
with open('sample_rbac_data.json') as f:
    data = json.load(f)

print('Peut lire ?', rbac_core.check_permission(data['user'], 'read'))
print('Rôles:', rbac_core.get_user_roles(data['user']))
