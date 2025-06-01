"""
Permissions personnalisées pour le module Administration Publique
"""
from rest_framework import permissions

class IsAdministrationPubliqueProjectOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # RBAC, multitenancy, sectorisation, hooks métier
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
