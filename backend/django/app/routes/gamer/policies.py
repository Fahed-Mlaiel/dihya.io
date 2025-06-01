"""
policies.py – Politiques RBAC, sécurité, conformité RGPD pour gamer (Dihya Coding)
"""
from rest_framework.permissions import BasePermission

class IsGamerAdmin(BasePermission):
    """Autorise uniquement les admins gamer."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.has_role('gamer_admin')

class IsGamerAuditor(BasePermission):
    """Autorise les auditeurs gamer."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.has_role('gamer_audit')
