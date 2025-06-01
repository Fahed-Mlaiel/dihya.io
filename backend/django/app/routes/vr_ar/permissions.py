from rest_framework import permissions

class IsSceneOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission avancée : seuls les créateurs de la scène peuvent modifier/supprimer, lecture publique possible.
    Conforme RGPD, audit, multilingue, accessibilité.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user

class IsAssetManagerOrReadOnly(permissions.BasePermission):
    """
    Permission avancée : seuls les gestionnaires d’assets peuvent éditer les assets.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return hasattr(obj, 'manager') and obj.manager == request.user
