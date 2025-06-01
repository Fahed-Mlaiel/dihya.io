"""
Dihya – Permissions pour le module Ressources Humaines
- RBAC, sécurité, souveraineté
"""
from rest_framework import permissions

class IsRHAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and (
            request.user.is_superuser or hasattr(request.user, 'is_rh_admin') and request.user.is_rh_admin
        )
