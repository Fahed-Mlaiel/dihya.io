"""
Permissions avancées Hôtellerie (RBAC, multilingue, extensible)
"""
from rest_framework import permissions
from django.utils.translation import gettext_lazy as _

class IsResponsable(permissions.BasePermission):
    message = _('Seul le responsable peut modifier cet hôtel.')
    def has_object_permission(self, request, view, obj):
        return request.user and obj.responsable == request.user.username
