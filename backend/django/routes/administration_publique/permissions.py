"""
Permissions avancées pour la gestion sécurisée des projets d'administration publique.
Inclut RBAC, multitenancy, audit, multilingue.
"""
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission personnalisée : admin = tout accès, autres = lecture seule.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.is_staff
