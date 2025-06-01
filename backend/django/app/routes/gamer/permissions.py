"""
Permissions avancées Gamer (RBAC, multilingue, extensible)
"""
from rest_framework import permissions
from django.utils.translation import gettext_lazy as _

class IsOwner(permissions.BasePermission):
    message = _('Seul le propriétaire du profil peut modifier ce profil.')
    def has_object_permission(self, request, view, obj):
        return request.user and obj.pseudo == request.user.username
