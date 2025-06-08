# Exemple d’utilisation avancée des permissions RBAC (Python)
from ...permissions import permissions

permissions.grant_permission('admin', 'resource1', 'read')
