"""
policies.py – Politiques RBAC, sécurité, conformité RGPD pour health (Dihya Coding)
"""
from rest_framework.permissions import BasePermission

class IsHealthAdmin(BasePermission):
    """Autorise uniquement les admins health."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.has_role('health_admin')

class IsHealthAuditor(BasePermission):
    """Autorise les auditeurs health."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.has_role('health_audit')
