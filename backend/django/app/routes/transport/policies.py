"""
policies.py – Politiques RBAC, sécurité, conformité RGPD pour transport (Dihya Coding)
"""
from rest_framework.permissions import BasePermission

class IsTransportAdmin(BasePermission):
    """Autorise uniquement les admins transport."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.has_role('transport_admin')

class IsTransportAuditor(BasePermission):
    """Autorise les auditeurs transport."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.has_role('transport_audit')
