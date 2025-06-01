"""
Permissions personnalisées pour le module Industrie
"""
from rest_framework import permissions

class IsIndustrieProjectOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # RBAC, multitenancy, sectorisation, hooks métier
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsIndustrieAssetManagerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # RBAC, multitenancy, sectorisation, hooks métier
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
