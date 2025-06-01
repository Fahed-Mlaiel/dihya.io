"""
policies.py – Politiques RBAC, sécurité, conformité RGPD pour logistique (Dihya Coding)
"""
from rest_framework.permissions import BasePermission

class IsLogistiqueAdmin(BasePermission):
    """Autorise uniquement les admins logistique."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.has_role('logistique_admin')

class IsLogistiqueAuditor(BasePermission):
    """Autorise les auditeurs logistique."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.has_role('logistique_audit')
