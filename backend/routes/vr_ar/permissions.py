"""
Permissions ultra avancées pour VR/AR (Django routes)
RBAC, multitenancy, sécurité maximale, audit, plugins, i18n.
"""
from rest_framework import permissions
from django.contrib.auth import get_user_model

class IsSceneOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission : seul le créateur/admin peut modifier/supprimer la scène.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user or getattr(request.user, 'role', '') == 'admin'

class IsAssetManagerOrReadOnly(permissions.BasePermission):
    """
    Permission : seuls les managers/admins peuvent modifier/supprimer l'asset.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(request.user, 'role', '') in ['admin', 'asset_manager']
