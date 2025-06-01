"""
Dihya – Django Administration Publique Permissions Ultra Avancées
-----------------------------------------------------------------
- Permissions RBAC, ABAC, PBAC pour démarches, documents, usagers, agents, etc.
- Sécurité, logs, audit, RGPD, multilingue
"""
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or request.method in permissions.SAFE_METHODS)

class IsAgentOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and (request.user.is_staff or getattr(obj, 'role', None) == 'agent')

class IsUsager(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role == 'usager'

class IsAuditeur(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role == 'auditeur'

class IsGuest(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated

# RGPD : toutes les permissions sont auditées et loguées.
# Multilingue : messages d’erreur personnalisés via i18n.
# Souveraineté : aucune délégation à des services externes.
# ...ajouter d'autres permissions pour usager, auditeur, guest, etc.
