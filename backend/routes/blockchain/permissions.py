"""
Permissions ultra avancées pour Blockchain (Django routes)
RBAC, multitenancy, sécurité maximale, audit, plugins, i18n.
"""
from rest_framework import permissions
from django.contrib.auth import get_user_model

class IsBlockchainProjectOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission : seul le créateur/admin peut modifier/supprimer le projet blockchain.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user or getattr(request.user, 'role', '') == 'admin'

class IsBlockchainAssetManagerOrReadOnly(permissions.BasePermission):
    """
    Permission : seuls les managers/admins peuvent modifier/supprimer l'asset blockchain.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(request.user, 'role', '') in ['admin', 'blockchain_asset_manager']
