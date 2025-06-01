"""
Dihya – Django Banque & Finance Permissions Ultra Avancées
----------------------------------------------------------
- Permissions RBAC, ABAC, PBAC pour comptes, transactions, virements, etc.
- Sécurité, logs, audit, RGPD, multilingue
"""
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or request.method in permissions.SAFE_METHODS)

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and (request.user.is_staff or obj['titulaire'] == request.user.username)

# ...ajouter d'autres permissions pour auditeur, conseiller, guest, etc.
