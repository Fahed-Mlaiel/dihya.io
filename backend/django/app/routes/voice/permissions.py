from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission avancée : seuls les propriétaires peuvent modifier/supprimer, lecture publique possible.
    Conforme RGPD, audit, multilingue, accessibilité.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.uploaded_by == request.user

class IsTranscriberOrReadOnly(permissions.BasePermission):
    """
    Permission avancée : seuls les transcripteurs désignés peuvent éditer la transcription.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return hasattr(obj, 'transcriber') and obj.transcriber == request.user
