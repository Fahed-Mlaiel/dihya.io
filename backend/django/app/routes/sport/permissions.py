"""
Dihya – Permissions RBAC avancées pour Sport
- Sécurité, conformité RGPD, accessibilité, multilingue
"""
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """Autorise l'accès complet aux admins, lecture seule sinon."""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsCoach(permissions.BasePermission):
    """Autorise l'accès aux coachs."""
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'is_coach') and request.user.is_coach

class IsAthlete(permissions.BasePermission):
    """Autorise l'accès aux athlètes."""
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'is_athlete') and request.user.is_athlete
