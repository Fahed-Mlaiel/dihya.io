"""
policies.py – Politiques RBAC, sécurité, conformité RGPD pour ecommerce (Dihya Coding)
"""
from rest_framework.permissions import BasePermission

class IsEcommerceAdmin(BasePermission):
    """Autorise uniquement les admins ecommerce."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.has_role('ecommerce_admin')

class IsEcommerceAuditor(BasePermission):
    """Autorise les auditeurs ecommerce."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.has_role('ecommerce_audit')
