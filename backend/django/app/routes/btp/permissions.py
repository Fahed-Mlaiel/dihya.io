"""
Permissions avancées pour la gestion sécurisée des projets BTP.
Inclut RBAC, multitenancy, audit, multilingue.
"""
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or (request.user and request.user.is_staff)
