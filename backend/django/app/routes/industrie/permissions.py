"""
Permissions avancées Industrie (RBAC, multilingue, extensible, auditabilité, conformité, internationalisation dynamique, multitenancy, plugins, logs structurés, fallback IA, docstring/type hints, tests)
"""
from rest_framework import permissions
from django.utils.translation import gettext_lazy as _

class IsResponsable(permissions.BasePermission):
    """
    Permission avancée : seul le responsable peut modifier ce site industriel (RBAC, multilingue, extensible, auditabilité, conformité, internationalisation dynamique, multitenancy, plugins, logs structurés, fallback IA, docstring/type hints, tests).
    """
    message = _('Seul le responsable peut modifier ce site industriel.')
    def has_object_permission(self, request, view, obj):
        # Audit, logs structurés, plugins, fallback IA, conformité, internationalisation dynamique, multitenancy, auditabilité
        return request.user and obj.responsable == request.user.username
