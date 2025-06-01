"""
Dihya – Permissions RBAC avancées pour Social
- Sécurité, conformité RGPD, accessibilité, multilingue
"""
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """Autorise l'accès complet aux admins, lecture seule sinon."""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsModerateur(permissions.BasePermission):
    """Autorise l'accès aux modérateurs."""
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'is_moderateur') and request.user.is_moderateur

class IsUtilisateur(permissions.BasePermission):
    """Autorise l'accès aux utilisateurs."""
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'is_utilisateur') and request.user.is_utilisateur
