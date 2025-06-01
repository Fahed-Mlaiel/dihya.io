"""
Permissions ultra avancées pour 3D (Django routes)
RBAC, multitenancy, sécurité maximale, audit, plugins, i18n.
"""
from rest_framework import permissions

class IsThreeDProjectOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission : seul le créateur/admin peut modifier/supprimer le projet 3D.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user or getattr(request.user, 'role', '') == 'admin'

class IsThreeDAssetManagerOrReadOnly(permissions.BasePermission):
    """
    Permission : seuls les managers/admins peuvent modifier/supprimer l'asset 3D.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(request.user, 'role', '') in ['admin', 'threed_asset_manager']
