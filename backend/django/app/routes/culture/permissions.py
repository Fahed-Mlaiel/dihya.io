"""
Permissions avancées Culture (RBAC, multilingue, extensible)
"""
from rest_framework import permissions
from django.utils.translation import gettext_lazy as _

class IsOrganisateur(permissions.BasePermission):
    message = _('Seul l’organisateur peut modifier cet événement.')
    def has_object_permission(self, request, view, obj):
        return request.user and obj.organisateur == request.user.username
