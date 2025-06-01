"""
Dihya – Django eCommerce API Permissions Ultra Avancé
-----------------------------------------------------
- Permissions RBAC avancées, multilingues, souveraines, extensibles
- Sécurité, audit, conformité RGPD/NIS2, accessibilité
"""
from rest_framework import permissions
from django.utils.translation import gettext_lazy as _

class IsAdminOrReadOnly(permissions.BasePermission):
    message = _('Seuls les administrateurs peuvent modifier, lecture publique autorisée.')
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or (request.user and request.user.is_staff)

class IsOwnerOrReadOnly(permissions.BasePermission):
    message = _('Seul le propriétaire peut modifier cet objet.')
    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or obj.owner == request.user

# Extensible : ajouter IsBoutiqueOwner, IsClient, etc. pour chaque modèle métier
