"""
RBAC sécurité – clé en main
Importe et expose toutes les fonctions du module RBAC
"""

from .engine.rbac_engine import *
from .roles.roles import *
from .permissions.permissions import *

__all__ = [
    'ROLES',
    'PERMISSIONS',
    'check_permission',
]
