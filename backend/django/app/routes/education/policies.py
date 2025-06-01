"""
policies.py – Politiques RBAC, sécurité, conformité RGPD pour education (Dihya Coding)
"""
from rest_framework.permissions import BasePermission

class IsEducationAdmin(BasePermission):
    """Autorise uniquement les admins education."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.has_role('education_admin')

class IsEducationAuditor(BasePermission):
    """Autorise les auditeurs education."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.has_role('education_audit')
