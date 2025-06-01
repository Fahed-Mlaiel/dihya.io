"""
Permissions avancées Crypto (RBAC, multilingue, extensible)
"""
from rest_framework import permissions
from django.utils.translation import gettext_lazy as _

class IsWalletOwner(permissions.BasePermission):
    message = _('Seul le propriétaire du wallet peut modifier ce wallet.')
    def has_object_permission(self, request, view, obj):
        return request.user and obj.proprietaire == request.user.username
