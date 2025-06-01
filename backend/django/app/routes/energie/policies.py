"""
policies.py – Politiques RBAC, sécurité, conformité RGPD pour energie (Dihya Coding)
"""
from rest_framework.permissions import BasePermission

class IsEnergieAdmin(BasePermission):
    """Autorise uniquement les admins energie."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.has_role('energie_admin')

class IsEnergieAuditor(BasePermission):
    """Autorise les auditeurs energie."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.has_role('energie_audit')
