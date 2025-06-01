"""
policies.py – Politiques RBAC, sécurité, conformité RGPD pour environnement (Dihya Coding)
"""
from rest_framework.permissions import BasePermission

class IsEnvironnementAdmin(BasePermission):
    """Autorise uniquement les admins environnement."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.has_role('environnement_admin')

class IsEnvironnementAuditor(BasePermission):
    """Autorise les auditeurs environnement."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.has_role('environnement_audit')
