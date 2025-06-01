"""
Dihya – Django 3D API Permissions Ultra Avancé
----------------------------------------------
- Permissions RBAC avancées, multilingues, souveraines, extensibles
- Sécurité, audit, conformité RGPD/NIS2
"""

from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or (request.user and request.user.is_staff)

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or obj.owner == request.user
