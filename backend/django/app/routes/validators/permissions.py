"""
Dihya – Permissions RBAC pour Validators
- Sécurité, conformité RGPD, accessibilité, multilingue
"""
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsValidator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'is_validator') and request.user.is_validator
