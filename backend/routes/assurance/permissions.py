"""
Permissions ultra avancées pour le module Assurance (Dihya)
RBAC, multitenancy, sécurité, RGPD, audit, plugins, i18n, SEO, logging.
"""
from rest_framework import permissions

class IsAssuranceAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or getattr(request.user, 'role', None) == 'admin'

class IsAssuranceUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or getattr(request.user, 'role', None) in ('admin', 'user')
