"""
Dihya – Django Blockchain API Permissions Ultra Avancé
------------------------------------------------------
- Permissions RBAC, ABAC, PBAC, RGPD, sécurité, souveraineté
"""
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsNodeOperator(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role == 'node_operator'

class IsSmartContractOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return hasattr(request.user, 'username') and obj.owner == request.user.username
