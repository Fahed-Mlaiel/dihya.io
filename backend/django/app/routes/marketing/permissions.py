"""
Dihya – Permissions avancées pour le module Marketing
- RBAC, sécurité, souveraineté, multilingue
"""
from rest_framework import permissions

class IsMarketingAdminOrReadOnly(permissions.BasePermission):
    """
    Permission personnalisée : seuls les admins marketing peuvent modifier, les autres ont un accès en lecture seule.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and (
            request.user.is_superuser or hasattr(request.user, 'is_marketing_admin') and request.user.is_marketing_admin
        )
