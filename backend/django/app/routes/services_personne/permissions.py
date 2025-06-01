"""
Dihya – Permissions RBAC avancées pour Services à la Personne
- Sécurité, conformité RGPD, accessibilité, multilingue
"""
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """Autorise l'accès complet aux admins, lecture seule sinon."""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsGestionnaire(permissions.BasePermission):
    """Autorise l'accès aux gestionnaires."""
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'is_gestionnaire') and request.user.is_gestionnaire

class IsIntervenant(permissions.BasePermission):
    """Autorise l'accès aux intervenants."""
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'is_intervenant') and request.user.is_intervenant

class IsClient(permissions.BasePermission):
    """Autorise l'accès aux clients."""
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'is_client') and request.user.is_client
