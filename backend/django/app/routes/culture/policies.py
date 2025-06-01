"""
policies.py – Politiques RBAC, sécurité, conformité RGPD pour culture (Dihya Coding)
"""
from rest_framework.permissions import BasePermission

class IsCultureAdmin(BasePermission):
    """Autorise uniquement les admins culture."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.has_role('culture_admin')

class IsCultureAuditor(BasePermission):
    """Autorise les auditeurs culture."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.has_role('culture_audit')
