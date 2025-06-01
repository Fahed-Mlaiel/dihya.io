"""
Permissions avancées Health (RBAC, multilingue, extensible)
"""
from rest_framework import permissions
from django.utils.translation import gettext_lazy as _

class IsMedecinOrOwner(permissions.BasePermission):
    message = _('Seul le médecin référent ou le patient peut accéder/modifier ce dossier.')
    def has_object_permission(self, request, view, obj):
        return (request.user and (obj.medecin == request.user.username or obj.patient == request.user.username))
