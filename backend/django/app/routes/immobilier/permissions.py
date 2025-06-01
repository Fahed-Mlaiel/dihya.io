"""
Permissions avancées Immobilier (RBAC, multilingue, extensible)
"""
from rest_framework import permissions
from django.utils.translation import gettext_lazy as _

class IsProprietaire(permissions.BasePermission):
    message = _('Seul le propriétaire peut modifier ce bien immobilier.')
    def has_object_permission(self, request, view, obj):
        return request.user and obj.proprietaire == request.user.username
