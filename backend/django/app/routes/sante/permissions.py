"""
Dihya – Permissions pour le module Santé
- RBAC, sécurité, souveraineté
"""
from rest_framework import permissions

class IsSanteAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and (
            request.user.is_superuser or hasattr(request.user, 'is_sante_admin') and request.user.is_sante_admin
        )
