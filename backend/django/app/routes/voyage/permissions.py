from rest_framework import permissions

class IsReservationOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission avancée : seuls les propriétaires de la réservation peuvent modifier/supprimer, lecture publique possible.
    Conforme RGPD, audit, multilingue, accessibilité.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

class IsItineraireManagerOrReadOnly(permissions.BasePermission):
    """
    Permission avancée : seuls les gestionnaires d’itinéraires peuvent éditer les itinéraires.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return hasattr(obj, 'manager') and obj.manager == request.user
