"""
Permissions avancées Journalisme (RBAC, multilingue, extensible)
"""
from rest_framework import permissions
from django.utils.translation import gettext_lazy as _

class IsAuteur(permissions.BasePermission):
    message = _('Seul l’auteur peut modifier cet article.')
    def has_object_permission(self, request, view, obj):
        return request.user and obj.auteur == request.user.username
