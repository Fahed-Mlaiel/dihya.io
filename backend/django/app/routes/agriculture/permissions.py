"""
Dihya – Django Agriculture API Permissions Ultra Avancé
------------------------------------------------------
- Permissions RBAC, ABAC, PBAC, RGPD, sécurité, souveraineté
"""
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsAgriculteur(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role == 'agriculteur'

class IsConseiller(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role == 'conseiller'

class IsAuditeur(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role == 'auditeur'
