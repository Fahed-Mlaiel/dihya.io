"""
Permissions avancées Construction (RBAC, multilingue, extensible)
"""
from rest_framework import permissions
from django.utils.translation import gettext_lazy as _

class IsChefChantier(permissions.BasePermission):
    message = _('Seuls les chefs de chantier peuvent modifier ce chantier.')
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='chef_chantier').exists()
