"""
Dihya – Permissions RBAC avancées pour Tourisme
- Sécurité, conformité RGPD, accessibilité, multilingue
"""
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """Autorise l'accès complet aux admins, lecture seule sinon."""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsAgent(permissions.BasePermission):
    """Autorise l'accès aux agents."""
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'is_agent') and request.user.is_agent

class IsGuide(permissions.BasePermission):
    """Autorise l'accès aux guides."""
    def has_permission(self, request, view):
        return request.user and hasattr(request.user, 'is_guide') and request.user.is_guide
